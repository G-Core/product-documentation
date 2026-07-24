"""
Report which provider resources are documented, partially documented, or missing.

Compares the current provider schema against doc_index.json to produce a
coverage report. Prints a markdown summary and writes coverage.json.

Usage:
    python3 report_coverage.py <schema.json> <doc_index.json>
"""

import json
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

INTERNAL_ATTRS = frozenset({"id", "timeouts"})


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_resource_schemas(schema: dict) -> dict:
    provider_key = next(iter(schema.get("provider_schemas", {})), None)
    if not provider_key:
        return {}
    return schema["provider_schemas"][provider_key].get("resource_schemas", {})


def get_attrs(resource_schema: dict) -> set[str]:
    raw = resource_schema.get("block", {}).get("attributes", {})
    return {k for k in raw if k not in INTERNAL_ATTRS}


def main() -> None:
    if len(sys.argv) != 3:
        log.error("Usage: report_coverage.py <schema.json> <doc_index.json>")
        sys.exit(2)

    schema_path, index_path = sys.argv[1], sys.argv[2]
    schema = load_json(schema_path)
    index = load_json(index_path)

    resource_schemas = get_resource_schemas(schema)
    gcore_resources = sorted(
        rt for rt in resource_schemas if rt.startswith("gcore_")
    )
    documented = set(index.get("resource_to_articles", {}).keys())
    resource_attr_to_articles = index.get("resource_attr_to_articles", {})

    not_documented: list[str] = []
    partially_documented: list[dict] = []
    fully_documented: list[str] = []

    for rt in gcore_resources:
        schema_attrs = get_attrs(resource_schemas[rt])
        if not schema_attrs:
            continue

        if rt not in documented:
            not_documented.append(rt)
            continue

        documented_attrs = {
            key.split("::", 1)[1]
            for key in resource_attr_to_articles
            if key.startswith(f"{rt}::") and resource_attr_to_articles[key]
        }
        missing = sorted(schema_attrs - documented_attrs)

        if missing:
            partially_documented.append({"resource": rt, "missing_attrs": missing})
        else:
            fully_documented.append(rt)

    total = len(gcore_resources)
    doc_count = len(fully_documented) + len(partially_documented)
    pct = int(100 * doc_count / total) if total else 0

    lines = [
        f"## Terraform provider coverage",
        f"",
        f"**{doc_count}/{total} resources documented ({pct}%)**",
        f"",
    ]

    if not_documented:
        lines.append("### Not documented")
        lines.append("")
        for rt in not_documented:
            lines.append(f"- `{rt}`")
        lines.append("")

    if partially_documented:
        lines.append("### Partially documented (missing attributes)")
        lines.append("")
        for item in partially_documented:
            attrs = ", ".join(f"`{a}`" for a in item["missing_attrs"])
            lines.append(f"- `{item['resource']}` — missing: {attrs}")
        lines.append("")

    if fully_documented:
        lines.append(f"### Fully documented ({len(fully_documented)} resources)")
        lines.append("")
        for rt in fully_documented:
            lines.append(f"- `{rt}`")

    report = "\n".join(lines)
    print(report)

    coverage = {
        "total_provider_resources": total,
        "documented": doc_count,
        "coverage_pct": pct,
        "not_documented": not_documented,
        "partially_documented": partially_documented,
        "fully_documented": fully_documented,
    }

    output_path = Path(index_path).parent / "coverage.json"
    output_path.write_text(
        json.dumps(coverage, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    log.info("Coverage report written to %s", output_path)


if __name__ == "__main__":
    main()
