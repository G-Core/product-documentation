"""
route_spec_changes.py

Cross-reference a structured API diff (from diff_api_spec.py --json-out) with
spec-article-map.json to find articles that cover changed endpoints via prose
but are not captured in doc_index.json (which tracks code snippets only).

Outputs a markdown section appended to the issue body, listing per-change
which additional articles from the semantic verifier mapping are affected.

Usage:
    python3 route_spec_changes.py \
        --diff     /tmp/api_diff.json \
        --map      data/spec-article-map.json \
        --output   /tmp/route_additions.md

Exit codes:
    0 — no additional articles found
    1 — additional articles found (append output to issue body)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_json(path: str) -> dict | list:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_path_to_articles(spec_map: dict) -> dict[str, list[str]]:
    """
    Build an inverted index: spec_path -> [article_ids].

    spec_map structure:
        { article_id: { spec_file, paths: [...], ... }, ... }
    """
    index: dict[str, list[str]] = {}
    for article_id, entry in spec_map.items():
        if not isinstance(entry, dict):
            continue
        for path in entry.get("paths", []):
            index.setdefault(path, []).append(article_id)
    return index


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Route spec changes to articles via spec-article-map.json.",
    )
    parser.add_argument("--diff", required=True, help="JSON diff from diff_api_spec.py --json-out")
    parser.add_argument("--map", required=True, help="Path to spec-article-map.json")
    parser.add_argument("--output", required=True, help="Output markdown file")
    args = parser.parse_args()

    diff_path = Path(args.diff)
    map_path = Path(args.map)

    if not diff_path.exists():
        Path(args.output).write_text("", encoding="utf-8")
        sys.exit(0)

    if not map_path.exists():
        Path(args.output).write_text("", encoding="utf-8")
        sys.exit(0)

    diff_data = load_json(args.diff)
    spec_map = load_json(args.map)

    if not isinstance(diff_data, dict) or not isinstance(spec_map, dict):
        Path(args.output).write_text("", encoding="utf-8")
        sys.exit(0)

    path_to_articles = build_path_to_articles(spec_map)
    changes: list[dict] = diff_data.get("changes", [])

    # Collect additional articles per change (not already in articles_doc_index).
    findings: list[dict] = []
    for change in changes:
        spec_path: str = change.get("spec_path", "")
        known: set[str] = set(change.get("articles_doc_index", []))
        additional = [a for a in path_to_articles.get(spec_path, []) if a not in known]
        if not additional:
            continue
        findings.append({
            "method": change.get("method", ""),
            "path": change.get("path", ""),
            "change_type": change.get("change_type", ""),
            "field": change.get("field"),
            "additional_articles": additional,
        })

    if not findings:
        Path(args.output).write_text("", encoding="utf-8")
        sys.exit(0)

    lines = [
        "",
        "---",
        "### Additional articles (semantic verifier mapping)",
        "",
        "These articles document the changed operations via prose and are not captured "
        "in the code-snippet index above. Verify them manually.",
        "",
    ]

    for f in findings:
        change_label = f["change_type"].replace("_", " ")
        field_note = f" — field `{f['field']}`" if f["field"] else ""
        lines.append(f"**`{f['method']} {f['path']}`** — {change_label}{field_note}")
        for article in f["additional_articles"]:
            lines.append(f"- `{article}`")
        lines.append("")

    output_text = "\n".join(lines)
    Path(args.output).write_text(output_text, encoding="utf-8")
    sys.exit(1)


if __name__ == "__main__":
    main()
