"""
Diff OpenAPI specs (old vs new) and map changes to documented articles.

Uses doc_index.json (built by build_doc_index.py) to answer operation- and
field-level questions: which articles actually call a given (method, path)
and which request fields they set, not just "does this product exist".

For operations newly added in this push, also reports the spec's own
x-codeSamples signal per language (fast, network-free, but known to lag
real SDK releases — see build_endpoint_index.py's module docstring). This is
informational only, not treated as a confirmed gap.

Exit codes:
    0 — no spec changes affect documented operations
    1 — changes found (caller should create/update an issue)

Writes GITHUB_OUTPUT variables:
    has_changes     — true | false
    has_doc_impact  — true | false
    spec_diff       — human-readable markdown diff

Usage:
    python3 diff_api_spec.py <old_specs_dir> <new_specs_dir> <doc_index.json>

<old_specs_dir> and <new_specs_dir> hold the pre- and post-push versions of
api-reference/services_documented/*.yaml (a missing file in <old_specs_dir>
means the product spec is new).
"""

import json
import logging
import os
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from build_endpoint_index import GO_CALL_RE, HTTP_METHODS, PY_CALL_RE, extract_call, normalize_path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def resolve_schema_props(node, components: dict, seen: set[str] | None = None) -> set[str]:
    """Best-effort top-level property name resolution, following one level
    of $ref / anyOf / oneOf. Not a full JSON Schema resolver — good enough
    to notice added/removed request fields, not to validate full shapes."""
    if seen is None:
        seen = set()
    if not isinstance(node, dict):
        return set()

    ref = node.get("$ref")
    if ref:
        name = ref.rsplit("/", 1)[-1]
        if name in seen:
            return set()
        target = components.get(name, {})
        return resolve_schema_props(target, components, seen | {name})

    props = set(node.get("properties", {}).keys())
    for combinator in ("anyOf", "oneOf", "allOf"):
        for sub in node.get(combinator, []):
            props |= resolve_schema_props(sub, components, seen)
    return props


def get_param_names(op: dict) -> set[str]:
    return {
        p.get("name")
        for p in op.get("parameters", []) or []
        if isinstance(p, dict) and p.get("name")
    }


def get_request_fields(op: dict, components: dict) -> set[str]:
    schema = (
        (op.get("requestBody") or {})
        .get("content", {})
        .get("application/json", {})
        .get("schema")
    )
    if not schema:
        return set()
    return resolve_schema_props(schema, components)


def extract_operations(spec: dict) -> dict[tuple[str, str], dict]:
    ops: dict[tuple[str, str], dict] = {}
    for raw_path, methods in (spec.get("paths", {}) or {}).items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            ops[(method.upper(), normalize_path(raw_path))] = {**op, "raw_path": raw_path}
    return ops


def articles_using_operation(doc_index: dict, method: str, path: str) -> list[str]:
    return doc_index.get("operation_to_articles", {}).get(f"{method} {path}", [])


def articles_using_field(doc_index: dict, method: str, path: str, field: str) -> list[str]:
    return doc_index.get("operation_field_to_articles", {}).get(f"{method} {path}::{field}", [])


def format_articles(articles: list[str]) -> str:
    return ", ".join(f"`{a}`" for a in articles)


def code_sample_note(op: dict) -> str:
    samples = op.get("x-codeSamples", []) or []
    has_py = extract_call(samples, "Python", "cloud", PY_CALL_RE) is not None
    has_go = extract_call(samples, "Go", "Cloud", GO_CALL_RE) is not None
    if has_py and has_go:
        return "spec already has Python and Go code samples"
    missing = [lang for lang, has in (("Python", has_py), ("Go", has_go)) if not has]
    return (
        f"spec has no {'/'.join(missing)} code sample yet — this often lags the real SDK "
        "release, confirm directly against gcore-python/gcore-go before assuming no SDK support"
    )


def diff_operation(
    method: str,
    path: str,
    old_op: dict,
    new_op: dict,
    old_components: dict,
    new_components: dict,
    doc_index: dict,
) -> tuple[list[str], bool]:
    old_fields = get_param_names(old_op) | get_request_fields(old_op, old_components)
    new_fields = get_param_names(new_op) | get_request_fields(new_op, new_components)

    added = sorted(new_fields - old_fields)
    removed = sorted(old_fields - new_fields)

    if not (added or removed):
        return [], False

    key_label = f"`{method} {path}`"
    lines = [f"\n#### {key_label}"]
    has_impact = False

    for field in removed:
        arts = articles_using_field(doc_index, method, path, field)
        if arts:
            has_impact = True
            lines.append(
                f"- **REMOVED** `{field}` — **{len(arts)} article(s) use this field "
                f"and must be updated:** {format_articles(arts)}"
            )
        else:
            lines.append(f"- **REMOVED** `{field}` — no articles use this field (no action needed)")

    for field in added:
        arts = articles_using_operation(doc_index, method, path)
        if arts:
            lines.append(
                f"- **ADDED** `{field}` — {len(arts)} article(s) document this operation "
                f"and may want to cover it: {format_articles(arts)}"
            )
        else:
            lines.append(f"- **ADDED** `{field}` — operation not yet documented")

    return lines, has_impact


def diff_product(
    product: str, old_spec: dict, new_spec: dict, doc_index: dict
) -> tuple[list[str], bool, bool]:
    old_ops = extract_operations(old_spec)
    new_ops = extract_operations(new_spec)
    old_components = (old_spec.get("components", {}) or {}).get("schemas", {}) or {}
    new_components = (new_spec.get("components", {}) or {}).get("schemas", {}) or {}

    added_keys = sorted(set(new_ops) - set(old_ops))
    removed_keys = sorted(set(old_ops) - set(new_ops))
    common_keys = sorted(set(old_ops) & set(new_ops))

    lines: list[str] = []
    has_changes = False
    has_doc_impact = False

    for method, path in removed_keys:
        arts = articles_using_operation(doc_index, method, path)
        has_changes = True
        if arts:
            has_doc_impact = True
            lines.append(
                f"\n#### `{method} {path}` — REMOVED from spec\n"
                f"**{len(arts)} article(s) reference this operation and must be updated:** "
                f"{format_articles(arts)}"
            )
        else:
            lines.append(f"\n#### `{method} {path}` — REMOVED from spec (not documented)")

    for method, path in added_keys:
        has_changes = True
        summary = new_ops[(method, path)].get("summary", "")
        note = code_sample_note(new_ops[(method, path)])
        lines.append(f"\n#### `{method} {path}` — NEW operation\n{summary} ({note})")

    for method, path in common_keys:
        op_lines, impact = diff_operation(
            method, path, old_ops[(method, path)], new_ops[(method, path)],
            old_components, new_components, doc_index,
        )
        if op_lines:
            has_changes = True
            if impact:
                has_doc_impact = True
            lines.extend(op_lines)

    if lines:
        lines.insert(0, f"\n### {product}")

    return lines, has_changes, has_doc_impact


def _normalize_to_spec_path(method: str, raw_path: str) -> str:
    """Convert method + raw path to spec-article-map.json path format."""
    encoded = raw_path.replace("/", "~1").replace("{", "{").replace("}", "}")
    return f"paths/{encoded}/{method.lower()}"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Diff OpenAPI specs and map changes to documented articles.",
    )
    parser.add_argument("old_specs_dir", type=Path)
    parser.add_argument("new_specs_dir", type=Path)
    parser.add_argument("doc_index", type=str)
    parser.add_argument(
        "--json-out", metavar="FILE",
        help="Write structured JSON diff to FILE for downstream routing scripts.",
    )
    args = parser.parse_args()

    doc_index = load_json(args.doc_index)

    all_lines: list[str] = []
    has_changes = False
    has_doc_impact = False
    structured: list[dict] = []

    for new_file in sorted(args.new_specs_dir.glob("*.yaml")):
        product = new_file.stem
        old_file = args.old_specs_dir / new_file.name
        old_spec = load_yaml(old_file)
        new_spec = load_yaml(new_file)

        old_ops = extract_operations(old_spec)
        new_ops = extract_operations(new_spec)
        old_components = (old_spec.get("components", {}) or {}).get("schemas", {}) or {}
        new_components = (new_spec.get("components", {}) or {}).get("schemas", {}) or {}

        # Collect structured entries before building markdown.
        for method, path in sorted(set(old_ops) - set(new_ops)):
            arts = articles_using_operation(doc_index, method, path)
            structured.append({
                "product": product,
                "spec_file": f"{product}_api.yaml",
                "spec_path": _normalize_to_spec_path(method, old_ops[(method, path)]["raw_path"]),
                "method": method,
                "path": path,
                "change_type": "operation_removed",
                "field": None,
                "articles_doc_index": arts,
            })

        for method, path in sorted(set(new_ops) - set(old_ops)):
            structured.append({
                "product": product,
                "spec_file": f"{product}_api.yaml",
                "spec_path": _normalize_to_spec_path(method, new_ops[(method, path)]["raw_path"]),
                "method": method,
                "path": path,
                "change_type": "operation_added",
                "field": None,
                "articles_doc_index": [],
            })

        for method, path in sorted(set(old_ops) & set(new_ops)):
            old_fields = get_param_names(old_ops[(method, path)]) | get_request_fields(old_ops[(method, path)], old_components)
            new_fields = get_param_names(new_ops[(method, path)]) | get_request_fields(new_ops[(method, path)], new_components)
            raw_path = new_ops[(method, path)]["raw_path"]
            spec_path = _normalize_to_spec_path(method, raw_path)
            for f in sorted(new_fields - old_fields):
                structured.append({
                    "product": product,
                    "spec_file": f"{product}_api.yaml",
                    "spec_path": spec_path,
                    "method": method,
                    "path": path,
                    "change_type": "field_added",
                    "field": f,
                    "articles_doc_index": articles_using_operation(doc_index, method, path),
                })
            for f in sorted(old_fields - new_fields):
                arts = articles_using_field(doc_index, method, path, f)
                structured.append({
                    "product": product,
                    "spec_file": f"{product}_api.yaml",
                    "spec_path": spec_path,
                    "method": method,
                    "path": path,
                    "change_type": "field_removed",
                    "field": f,
                    "articles_doc_index": arts,
                })

        lines, changed, impact = diff_product(product, old_spec, new_spec, doc_index)
        if changed:
            has_changes = True
            if impact:
                has_doc_impact = True
            all_lines.extend(lines)

    if not has_changes:
        all_lines.append("No API spec changes detected in documented operations.")

    output = "\n".join(all_lines)
    print(output)

    if args.json_out and structured:
        Path(args.json_out).write_text(
            json.dumps({"changes": structured}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write("spec_diff<<SPEC_DIFF_EOF\n")
            f.write(output + "\n")
            f.write("SPEC_DIFF_EOF\n")
            f.write(f"has_changes={'true' if has_changes else 'false'}\n")
            f.write(f"has_doc_impact={'true' if has_doc_impact else 'false'}\n")

    sys.exit(0 if not has_changes else 1)


if __name__ == "__main__":
    main()
