"""
Diff two Terraform provider schemas and map changes to documented articles.

Uses doc_index.json (built by build_doc_index.py) to answer attribute-level
questions: which articles actually USE a removed attribute, not just which
articles declare the resource.

Exit codes:
    0 — no schema changes in documented resources
    1 — changes found (caller should create an issue)

Writes GITHUB_OUTPUT variables:
    has_changes  — true | false
    schema_diff  — human-readable markdown diff
"""

import json
import logging
import os
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_resource_schemas(schema: dict) -> dict:
    """Extract resource_schemas from a full provider schema JSON."""
    provider_key = next(iter(schema.get("provider_schemas", {})), None)
    if not provider_key:
        return {}
    return schema["provider_schemas"][provider_key].get("resource_schemas", {})


def get_attrs(resource_schema: dict) -> dict:
    return resource_schema.get("block", {}).get("attributes", {})


def articles_using_resource(index: dict, resource_type: str) -> list[str]:
    return index.get("resource_to_articles", {}).get(resource_type, [])


def articles_using_attr(index: dict, resource_type: str, attr: str) -> list[str]:
    key = f"{resource_type}::{attr}"
    return index.get("resource_attr_to_articles", {}).get(key, [])


def format_article_list(articles: list[str]) -> str:
    return ", ".join(f"`{a}`" for a in articles)


def describe_attr_change(old_a: dict, new_a: dict) -> str:
    parts = []
    if old_a.get("required") != new_a.get("required"):
        parts.append(f"required: {old_a.get('required')} → {new_a.get('required')}")
    if old_a.get("optional") != new_a.get("optional"):
        parts.append(f"optional: {old_a.get('optional')} → {new_a.get('optional')}")
    if old_a.get("type") != new_a.get("type"):
        parts.append(f"type: `{old_a.get('type')}` → `{new_a.get('type')}`")
    return "; ".join(parts) if parts else "unknown change"


def diff_resource(
    resource_type: str,
    old_schema: dict,
    new_schema: dict,
    index: dict,
) -> tuple[list[str], bool]:
    """
    Diff one resource's schema. Returns (markdown_lines, has_doc_impact).

    has_doc_impact is True only when there are changes that affect documented
    content (i.e., broken examples or missing required documentation).
    """
    old_attrs = get_attrs(old_schema)
    new_attrs = get_attrs(new_schema)

    added = sorted(set(new_attrs) - set(old_attrs))
    removed = sorted(set(old_attrs) - set(new_attrs))
    changed = []
    for attr in sorted(set(old_attrs) & set(new_attrs)):
        old_a = old_attrs[attr]
        new_a = new_attrs[attr]
        if (
            old_a.get("required") != new_a.get("required")
            or old_a.get("optional") != new_a.get("optional")
            or old_a.get("type") != new_a.get("type")
        ):
            changed.append(attr)

    if not (added or removed or changed):
        return [], False

    lines: list[str] = [f"\n#### `{resource_type}`"]
    has_impact = False

    for attr in removed:
        arts = articles_using_attr(index, resource_type, attr)
        if arts:
            has_impact = True
            lines.append(
                f"- **REMOVED** `{attr}` — "
                f"**{len(arts)} article(s) use this attribute and must be updated:** "
                + format_article_list(arts)
            )
        else:
            lines.append(
                f"- **REMOVED** `{attr}` — "
                "no articles use this attribute (no action needed)"
            )

    for attr in changed:
        arts = articles_using_attr(index, resource_type, attr)
        change_desc = describe_attr_change(old_attrs[attr], new_attrs[attr])
        if arts:
            has_impact = True
            lines.append(
                f"- **CHANGED** `{attr}` ({change_desc}) — "
                f"**{len(arts)} article(s) may need review:** "
                + format_article_list(arts)
            )
        else:
            lines.append(
                f"- **CHANGED** `{attr}` ({change_desc}) — "
                "no articles use this attribute"
            )

    for attr in added:
        candidate_arts = articles_using_resource(index, resource_type)
        if candidate_arts:
            lines.append(
                f"- **ADDED** `{attr}` — "
                f"{len(candidate_arts)} article(s) may want to document it: "
                + format_article_list(candidate_arts)
            )
        else:
            lines.append(f"- **ADDED** `{attr}` — resource not yet documented")

    return lines, has_impact


def main() -> None:
    if len(sys.argv) != 4:
        log.error(
            "Usage: diff_schemas.py <old_schema.json> <new_schema.json> <doc_index.json>"
        )
        sys.exit(2)

    old_path, new_path, index_path = sys.argv[1], sys.argv[2], sys.argv[3]

    old_schema = load_json(old_path)
    new_schema = load_json(new_path)
    index = load_json(index_path)

    documented_resources = sorted(
        index.get("resource_to_articles", {}).keys()
    )

    old_resources = get_resource_schemas(old_schema)
    new_resources = get_resource_schemas(new_schema)

    all_lines: list[str] = []
    has_changes = False
    has_doc_impact = False

    for resource_type in documented_resources:
        old = old_resources.get(resource_type)
        new = new_resources.get(resource_type)
        articles = articles_using_resource(index, resource_type)

        if old is None and new is not None:
            all_lines.append(f"\n#### `{resource_type}` — NEW resource")
            all_lines.append(
                "This resource is now available in the provider but not yet documented."
            )
            has_changes = True

        elif old is not None and new is None:
            all_lines.append(f"\n#### `{resource_type}` — REMOVED from provider")
            if articles:
                has_doc_impact = True
                all_lines.append(
                    f"**{len(articles)} article(s) reference this resource and must be updated:** "
                    + format_article_list(articles)
                )
            has_changes = True

        elif old is not None and new is not None:
            lines, impact = diff_resource(resource_type, old, new, index)
            if lines:
                has_changes = True
                if impact:
                    has_doc_impact = True
                all_lines.extend(lines)

    if not has_changes:
        all_lines.append("No schema changes detected in documented resources.")

    output = "\n".join(all_lines)
    print(output)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as f:
            f.write("schema_diff<<DIFF_EOF\n")
            f.write(output + "\n")
            f.write("DIFF_EOF\n")
            f.write(f"has_changes={'true' if has_changes else 'false'}\n")
            f.write(f"has_doc_impact={'true' if has_doc_impact else 'false'}\n")

    sys.exit(0 if not has_changes else 1)


if __name__ == "__main__":
    main()
