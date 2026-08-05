"""
Build a structured index of all REST API and SDK usage in MDX documentation.

For each article the index records: which REST operations (method + path),
Python SDK methods, and Go SDK methods are actually demonstrated, and which
request fields each usage sets. This lets downstream tools answer precise
questions ("which articles call POST /cloud/v2/baremetal/{}/{}/{}/action?")
rather than vague ones ("which articles mention bare metal servers?").

Mirrors the design of .github/scripts/terraform/build_doc_index.py.

Output: api-sdk-tracker/doc_index.json
"""

import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

# All top-level content directories that could contain API/SDK examples.
# Kept deliberately broad, same list as the Terraform indexer.
MDX_DIRS = [
    "account-settings",
    "cdn",
    "cloud",
    "colocation",
    "ddos-protection",
    "developer-tools",
    "dns",
    "edge-ai",
    "edge-proxy",
    "fastedge",
    "hosting",
    "reseller-support",
    "storage",
    "streaming",
    "waap",
]

BASH_FENCE_RE = re.compile(r"```bash\n(.*?)```", re.DOTALL)
PYTHON_FENCE_RE = re.compile(r"```python\n(.*?)```", re.DOTALL)
GO_FENCE_RE = re.compile(r"```go\n(.*?)```", re.DOTALL)

CURL_METHOD_RE = re.compile(r"-X\s+(GET|POST|PUT|PATCH|DELETE)\b", re.IGNORECASE)
CURL_HAS_DATA_RE = re.compile(r"(?:^|\s)(-d\b|--data\b|--data-raw\b|--data-binary\b)")
CURL_URL_RE = re.compile(r"""["'](https://api\.gcore\.com[^"']*)["']""")

# A path segment is "dynamic" if it is a shell variable, a bare integer,
# a UUID-like token, or a literal {placeholder} — never a fixed keyword.
DYNAMIC_SEGMENT_RE = re.compile(
    r"^(\$\{?\w+\}?|-?\d+|\{[^}]+\}|[0-9a-fA-F]{6,}(-[0-9a-fA-F]{2,}){2,})$"
)

PY_METHOD_RE = re.compile(r"\bclient\.cloud\.((?:\w+\.)+\w+)\s*\(")
GO_METHOD_RE = re.compile(r"\bclient\.Cloud\.((?:\w+\.)+\w+)\s*\(")

# Best-effort field extraction: look at a bounded window of text right after
# the call site up to the first line that closes the call (a lone ')' / '}'
# at the start of a line), or a fixed line cap, whichever comes first.
CALL_WINDOW_MAX_LINES = 40
PY_KWARG_RE = re.compile(r"^\s*(\w+)\s*=", re.MULTILINE)
GO_FIELD_RE = re.compile(r"^\s*(\w+):", re.MULTILINE)
JSON_KEY_RE = re.compile(r'"(\w+)"\s*:')


def line_number(content: str, pos: int) -> int:
    return content[:pos].count("\n") + 1


def normalize_path(path: str) -> str:
    """Replace dynamic path segments with '{}' so curl examples, SDK source
    paths, and OpenAPI paths all collapse to the same comparable key."""
    path = path.split("?", 1)[0]
    segments = [s for s in path.strip("/").split("/") if s]
    normalized = [
        "{}" if DYNAMIC_SEGMENT_RE.match(seg) else seg for seg in segments
    ]
    return "/" + "/".join(normalized)


def split_curl_statements(bash_text: str) -> list[tuple[int, str]]:
    """Split a bash fence into individual curl invocations, following shell
    line-continuation (`\\` at end of line) to join multi-line commands.

    Returns a list of (start_line_offset, statement_text) tuples, where
    start_line_offset is 0-based relative to the start of the fence.
    """
    statements: list[tuple[int, str]] = []
    current: list[str] = []
    current_start = 0
    in_statement = False

    for idx, raw_line in enumerate(bash_text.splitlines()):
        stripped = raw_line.strip()
        if not in_statement:
            if stripped.startswith("curl"):
                in_statement = True
                current = [raw_line]
                current_start = idx
            else:
                continue
        else:
            current.append(raw_line)

        if in_statement and not raw_line.rstrip().endswith("\\"):
            statements.append((current_start, "\n".join(current)))
            current = []
            in_statement = False

    if current:
        statements.append((current_start, "\n".join(current)))

    return statements


def extract_curl_operations(content: str) -> list[dict]:
    """Find every curl call in every bash fence, return operation usages."""
    operations: list[dict] = []

    for fence_match in BASH_FENCE_RE.finditer(content):
        bash_text = fence_match.group(1)
        fence_pos = fence_match.start()
        base_line = line_number(content, fence_pos)

        for start_offset, statement in split_curl_statements(bash_text):
            url_match = CURL_URL_RE.search(statement)
            if not url_match:
                continue

            path = url_match.group(1)[len("https://api.gcore.com") :]
            if not path.startswith("/"):
                continue

            method_match = CURL_METHOD_RE.search(statement)
            if method_match:
                method = method_match.group(1).upper()
            elif CURL_HAS_DATA_RE.search(statement):
                method = "POST"
            else:
                method = "GET"

            fields = sorted(set(JSON_KEY_RE.findall(statement)))

            operations.append(
                {
                    "method": method,
                    "path": normalize_path(path),
                    "fields": fields,
                    "line": base_line + start_offset,
                }
            )

    return operations


def call_window(fence_text: str, start: int) -> str:
    """Return a bounded slice of text after a call site, stopping at a
    line that closes the call at column 0 or after a fixed line cap."""
    rest = fence_text[start:]
    lines = rest.splitlines()
    window_lines: list[str] = []
    for ln in lines[: CALL_WINDOW_MAX_LINES]:
        window_lines.append(ln)
        if re.match(r"^(\)|\})\s*$", ln):
            break
    return "\n".join(window_lines)


def extract_sdk_calls(
    content: str, fence_re: re.Pattern, method_re: re.Pattern, field_re: re.Pattern
) -> list[dict]:
    calls: list[dict] = []

    for fence_match in fence_re.finditer(content):
        fence_text = fence_match.group(1)
        fence_pos = fence_match.start()
        base_line = line_number(content, fence_pos)

        for m in method_re.finditer(fence_text):
            dotted = m.group(1)
            call_line = base_line + fence_text[: m.start()].count("\n")
            window = call_window(fence_text, m.end())
            fields = sorted(set(field_re.findall(window)))
            calls.append({"method": dotted, "fields": fields, "line": call_line})

    return calls


def index_file(mdx: Path) -> dict:
    content = mdx.read_text(encoding="utf-8", errors="ignore")

    operations = extract_curl_operations(content)
    python_calls = extract_sdk_calls(content, PYTHON_FENCE_RE, PY_METHOD_RE, PY_KWARG_RE)
    go_calls = extract_sdk_calls(content, GO_FENCE_RE, GO_METHOD_RE, GO_FIELD_RE)

    return {
        "operations": operations,
        "python_calls": python_calls,
        "go_calls": go_calls,
    }


def build_lookup_maps(articles: dict[str, dict]) -> dict[str, dict]:
    operation_to_articles: dict[str, list[str]] = {}
    operation_field_to_articles: dict[str, list[str]] = {}
    python_method_to_articles: dict[str, list[str]] = {}
    python_method_field_to_articles: dict[str, list[str]] = {}
    go_method_to_articles: dict[str, list[str]] = {}
    go_method_field_to_articles: dict[str, list[str]] = {}

    def add(mapping: dict[str, list[str]], key: str, path: str) -> None:
        arts = mapping.setdefault(key, [])
        if path not in arts:
            arts.append(path)

    for path, entry in articles.items():
        for op in entry.get("operations", []):
            key = f"{op['method']} {op['path']}"
            add(operation_to_articles, key, path)
            for field in op.get("fields", []):
                add(operation_field_to_articles, f"{key}::{field}", path)

        for call in entry.get("python_calls", []):
            key = f"cloud.{call['method']}"
            add(python_method_to_articles, key, path)
            for field in call.get("fields", []):
                add(python_method_field_to_articles, f"{key}::{field}", path)

        for call in entry.get("go_calls", []):
            key = f"Cloud.{call['method']}"
            add(go_method_to_articles, key, path)
            for field in call.get("fields", []):
                add(go_method_field_to_articles, f"{key}::{field}", path)

    return {
        "operation_to_articles": operation_to_articles,
        "operation_field_to_articles": operation_field_to_articles,
        "python_method_to_articles": python_method_to_articles,
        "python_method_field_to_articles": python_method_field_to_articles,
        "go_method_to_articles": go_method_to_articles,
        "go_method_field_to_articles": go_method_field_to_articles,
    }


def main() -> None:
    repo_root = Path(__file__).parent.parent.parent.parent
    output_path = repo_root / "api-sdk-tracker" / "doc_index.json"

    articles: dict[str, dict] = {}
    total_ops = 0
    total_py = 0
    total_go = 0

    for d in MDX_DIRS:
        base = repo_root / d
        if not base.exists():
            continue
        for mdx in sorted(base.rglob("*.mdx")):
            rel = str(mdx.relative_to(repo_root)).replace("\\", "/")
            entry = index_file(mdx)
            if entry["operations"] or entry["python_calls"] or entry["go_calls"]:
                articles[rel] = entry
                total_ops += len(entry["operations"])
                total_py += len(entry["python_calls"])
                total_go += len(entry["go_calls"])

    lookup_maps = build_lookup_maps(articles)

    index = {
        "stats": {
            "articles_with_api_or_sdk": len(articles),
            "total_curl_operations": total_ops,
            "total_python_calls": total_py,
            "total_go_calls": total_go,
            "unique_operations": len(lookup_maps["operation_to_articles"]),
            "unique_python_methods": len(lookup_maps["python_method_to_articles"]),
            "unique_go_methods": len(lookup_maps["go_method_to_articles"]),
        },
        "articles": articles,
        **lookup_maps,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")

    log.info(
        "Indexed %d articles: %d curl operations, %d Python calls, %d Go calls",
        len(articles),
        total_ops,
        total_py,
        total_go,
    )
    log.info("Output: %s", output_path)


if __name__ == "__main__":
    sys.exit(main())
