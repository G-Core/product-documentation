"""
Build a structured index of all Terraform HCL blocks in MDX documentation.

For each article the index records: which gcore_* resources and data sources
are declared, which attributes each block uses, and where in the file the
block appears. This lets downstream tools answer attribute-level questions
("which articles use gcore_cloud_load_balancer::listeners?") rather than
resource-level questions ("which articles mention gcore_cloud_load_balancer?").

Output: terraform-provider/doc_index.json
"""

import io
import json
import logging
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import hcl2
    HCL2_AVAILABLE = True
except ImportError:
    HCL2_AVAILABLE = False
    logging.warning("python-hcl2 not installed; falling back to regex parser")

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

FENCE_RE = re.compile(
    r"```(?:hcl|terraform)\n(.*?)```",
    re.DOTALL,
)
FENCE_LINE_RE = re.compile(r"```(?:hcl|terraform)\n")

BLOCK_RE = re.compile(
    r'(resource|data)\s+"(gcore_\w+)"\s+"([^"]+)"\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',
    re.DOTALL,
)
ATTR_RE = re.compile(r"^\s{0,8}(\w+)\s*[={]", re.MULTILINE)

# Patterns used to sanitize HCL before regex parsing.
# Replaces Terraform interpolations (${...}) with a placeholder so braces
# inside strings don't break the brace-counting in BLOCK_RE.
INTERPOLATION_RE = re.compile(r"\$\{[^}]*\}")
# jsonencode / toset / tolist calls whose argument contains nested braces
FUNC_CALL_RE = re.compile(r"\w+\(\[.*?\]\)", re.DOTALL)

TERRAFORM_TAB_OPEN = re.compile(r'<MethodSection[^>]*id=["\']terraform["\']', re.IGNORECASE)
TERRAFORM_TAB_CLOSE = re.compile(r"</MethodSection>", re.IGNORECASE)

ATTR_TABLE_RE = re.compile(
    r"\|\s*`?(\w+)`?\s*\|[^|]+\|[^|]+\|",
)

# All top-level content directories that could contain Terraform HCL examples.
# Kept deliberately broad: the indexer skips files with no HCL content, so
# listing extra directories has negligible cost.
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


def line_number(content: str, pos: int) -> int:
    return content[:pos].count("\n") + 1


def is_in_terraform_tab(content: str, fence_pos: int) -> bool:
    """
    Return True if the code fence at fence_pos is inside a Terraform MethodSection.
    Articles like manage-cloud-via-terraform-v2.mdx have no MethodSection at all;
    for those, every HCL block is considered to be in the Terraform context.
    """
    has_any_method_section = bool(re.search(r"<MethodSection", content, re.IGNORECASE))
    if not has_any_method_section:
        return True

    last_open = -1
    for m in TERRAFORM_TAB_OPEN.finditer(content):
        if m.start() < fence_pos:
            last_open = m.start()

    if last_open == -1:
        return False

    close_after_open = TERRAFORM_TAB_CLOSE.search(content, last_open)
    if close_after_open and close_after_open.start() < fence_pos:
        return False

    return True


def parse_hcl2(hcl_text: str) -> list[dict]:
    """Parse HCL block with python-hcl2. Returns list of block dicts."""
    try:
        parsed = hcl2.load(io.StringIO(hcl_text))
    except Exception as exc:
        log.debug("hcl2 parse error: %s", exc)
        return []

    blocks = []
    for block_type in ("resource", "data"):
        for type_map in parsed.get(block_type, []):
            for resource_type, instances in type_map.items():
                if not resource_type.startswith("gcore_"):
                    continue
                for resource_name, body in instances.items():
                    if not isinstance(body, dict):
                        continue
                    blocks.append(
                        {
                            "block_type": block_type,
                            "resource_type": resource_type,
                            "resource_name": resource_name,
                            "attributes": sorted(body.keys()),
                            "parsed_by": "hcl2",
                        }
                    )
    return blocks


def sanitize_for_regex(hcl_text: str) -> str:
    """
    Remove constructs that confuse the brace-counting in BLOCK_RE:
    - Terraform interpolations ${...} → __INTERPOLATION__
    - function calls with nested brackets → __FUNC__
    - documentation placeholders ... → (removed)
    """
    text = INTERPOLATION_RE.sub("__INTERPOLATION__", hcl_text)
    text = FUNC_CALL_RE.sub('"__FUNC__"', text)
    text = re.sub(r"^\s*\.\.\.\s*$", "", text, flags=re.MULTILINE)
    return text


def parse_regex(hcl_text: str) -> list[dict]:
    """Fallback regex-based HCL parser."""
    sanitized = sanitize_for_regex(hcl_text)
    blocks = []
    for m in BLOCK_RE.finditer(sanitized):
        block_type = m.group(1)
        resource_type = m.group(2)
        resource_name = m.group(3)
        body = m.group(4)
        attrs = sorted(set(ATTR_RE.findall(body)))
        blocks.append(
            {
                "block_type": block_type,
                "resource_type": resource_type,
                "resource_name": resource_name,
                "attributes": attrs,
                "parsed_by": "regex",
            }
        )
    return blocks


def parse_hcl_text(hcl_text: str) -> list[dict]:
    if HCL2_AVAILABLE:
        blocks = parse_hcl2(hcl_text)
        if blocks:
            return blocks
    return parse_regex(hcl_text)


def extract_attribute_tables(content: str) -> dict[str, list[str]]:
    """
    Find markdown attribute tables that document gcore_* resource attributes.
    Looks for a header line like '### `gcore_cloud_load_balancer`' followed
    by a table whose first column contains attribute names.
    Returns {resource_type: [attr, ...]} mapping.
    """
    tables: dict[str, list[str]] = {}
    resource_header = re.compile(r"#+\s+`?(gcore_\w+)`?")
    lines = content.splitlines()
    current_resource: str | None = None

    for line in lines:
        hm = resource_header.match(line)
        if hm:
            current_resource = hm.group(1)
            continue
        if current_resource and ATTR_TABLE_RE.match(line):
            col = line.split("|")[1].strip().strip("`")
            if re.match(r"^\w+$", col) and col not in ("Attribute", "Field", "Parameter", "Name"):
                tables.setdefault(current_resource, [])
                if col not in tables[current_resource]:
                    tables[current_resource].append(col)

    return tables


def index_file(mdx: Path) -> dict:
    """Parse one MDX file and return its index entry."""
    content = mdx.read_text(encoding="utf-8", errors="ignore")
    terraform_blocks: list[dict] = []
    parse_errors: list[str] = []

    for fence_match in FENCE_RE.finditer(content):
        hcl_text = fence_match.group(1)
        fence_pos = fence_match.start()
        start_line = line_number(content, fence_pos)
        in_tf_tab = is_in_terraform_tab(content, fence_pos)

        blocks = parse_hcl_text(hcl_text)
        if not blocks:
            if re.search(r'resource\s+"gcore_', hcl_text):
                parse_errors.append(f"line {start_line}: could not parse block")
            continue

        for block in blocks:
            block["line_start"] = start_line
            block["in_terraform_tab"] = in_tf_tab
            terraform_blocks.append(block)

    attribute_tables = extract_attribute_tables(content)

    return {
        "terraform_blocks": terraform_blocks,
        "attribute_tables": attribute_tables,
        "parse_errors": parse_errors,
    }


def build_lookup_maps(
    articles: dict[str, dict],
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """
    Build fast lookup maps from the per-article index.

    resource_to_articles:       resource_type -> [article_path, ...]
    resource_attr_to_articles:  "resource_type::attr" -> [article_path, ...]
    """
    resource_to_articles: dict[str, list[str]] = {}
    resource_attr_to_articles: dict[str, list[str]] = {}

    for path, entry in articles.items():
        seen_resources: set[str] = set()
        seen_attrs: set[str] = set()

        for block in entry.get("terraform_blocks", []):
            rt = block["resource_type"]
            if rt not in seen_resources:
                resource_to_articles.setdefault(rt, [])
                resource_to_articles[rt].append(path)
                seen_resources.add(rt)

            for attr in block.get("attributes", []):
                key = f"{rt}::{attr}"
                if key not in seen_attrs:
                    resource_attr_to_articles.setdefault(key, [])
                    resource_attr_to_articles[key].append(path)
                    seen_attrs.add(key)

        for rt, attrs in entry.get("attribute_tables", {}).items():
            if rt not in seen_resources:
                resource_to_articles.setdefault(rt, [])
                resource_to_articles[rt].append(path)
                seen_resources.add(rt)
            for attr in attrs:
                key = f"{rt}::{attr}"
                if key not in seen_attrs:
                    resource_attr_to_articles.setdefault(key, [])
                    resource_attr_to_articles[key].append(path)
                    seen_attrs.add(key)

    return resource_to_articles, resource_attr_to_articles


def main() -> None:
    repo_root = Path(__file__).parent.parent.parent.parent
    output_path = repo_root / "terraform-provider" / "doc_index.json"

    articles: dict[str, dict] = {}
    total_blocks = 0
    total_errors = 0

    for d in MDX_DIRS:
        base = repo_root / d
        if not base.exists():
            continue
        for mdx in sorted(base.rglob("*.mdx")):
            rel = str(mdx.relative_to(repo_root)).replace("\\", "/")
            entry = index_file(mdx)
            if entry["terraform_blocks"] or entry["attribute_tables"]:
                articles[rel] = entry
                total_blocks += len(entry["terraform_blocks"])
                total_errors += len(entry["parse_errors"])

    resource_to_articles, resource_attr_to_articles = build_lookup_maps(articles)

    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "hcl2_available": HCL2_AVAILABLE,
        "stats": {
            "articles_with_terraform": len(articles),
            "total_hcl_blocks": total_blocks,
            "parse_errors": total_errors,
            "unique_resources": len(resource_to_articles),
            "unique_resource_attr_pairs": len(resource_attr_to_articles),
        },
        "articles": articles,
        "resource_to_articles": resource_to_articles,
        "resource_attr_to_articles": resource_attr_to_articles,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")

    log.info(
        "Indexed %d articles, %d HCL blocks, %d unique resources, %d parse errors",
        len(articles),
        total_blocks,
        len(resource_to_articles),
        total_errors,
    )
    log.info("Output: %s", output_path)

    if total_errors:
        log.warning(
            "%d block(s) could not be parsed (likely placeholder syntax in examples). "
            "Index is still usable.",
            total_errors,
        )


if __name__ == "__main__":
    main()
