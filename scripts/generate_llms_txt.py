"""
Generate per-product llms.txt files from docs.json navigation structure.

Reads docs.json from the product-documentation repo, extracts page paths
per top-level product group preserving section hierarchy, reads MDX frontmatter
for titles and descriptions, and writes per-product llms.txt files plus an
updated root llms.txt index.

Usage:
    python scripts/generate_llms_txt.py \
        --repo C:/Projects/product-documentation-test2/product-documentation \
        --base-url https://gcore.com/docs

Output:
    {repo}/llms.txt                    - root index with links to product files
    {repo}/{product}/llms.txt          - per-product page list with sections
"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

BASE_URL_DEFAULT = "https://gcore.com/docs"
DOCS_JSON_NAME = "docs.json"
DOCUMENTATION_TAB = "Documentation"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        required=True,
        type=Path,
        help="Path to the product-documentation repo root.",
    )
    parser.add_argument(
        "--base-url",
        default=BASE_URL_DEFAULT,
        help=f"Base URL for docs pages (default: {BASE_URL_DEFAULT}).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output to stdout instead of writing files.",
    )
    return parser.parse_args()


def collect_pages(node: object) -> list[str]:
    """Recursively collect all page path strings from a navigation node."""
    pages: list[str] = []
    if isinstance(node, str):
        pages.append(node)
    elif isinstance(node, dict):
        for item in node.get("pages", []):
            pages.extend(collect_pages(item))
    elif isinstance(node, list):
        for item in node:
            pages.extend(collect_pages(item))
    return pages


def read_frontmatter(mdx_path: Path) -> dict[str, str]:
    """
    Read YAML frontmatter from an MDX file.

    Returns a dict with keys: title, sidebarTitle, ai-navigation.
    Missing keys are returned as empty strings.
    """
    result: dict[str, str] = {"title": "", "sidebarTitle": "", "ai-navigation": ""}
    if not mdx_path.exists():
        return result
    try:
        content = mdx_path.read_text(encoding="utf-8")
    except OSError as exc:
        log.warning("Cannot read %s: %s", mdx_path, exc)
        return result

    if not content.startswith("---"):
        match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if match:
            result["title"] = match.group(1).strip()
        return result

    end = content.find("---", 3)
    if end == -1:
        return result
    fm_block = content[3:end]
    for line in fm_block.splitlines():
        for key in ("title", "sidebarTitle", "ai-navigation"):
            pattern = rf"^{key}:\s*['\"]?(.+?)['\"]?\s*$"
            m = re.match(pattern, line.strip())
            if m:
                result[key] = m.group(1).strip().strip("'\"")
    return result


def page_to_url(page_path: str, base_url: str) -> str:
    """Convert a page path (e.g. 'cloud/virtual-instances/create-an-instance') to URL."""
    return f"{base_url.rstrip('/')}/{page_path}.md"


def get_product_prefix(node: object) -> Optional[str]:
    """
    Determine the top-level directory prefix for a group by scanning all pages.
    Returns the first path component that appears most frequently.
    """
    pages = collect_pages(node)
    prefixes: dict[str, int] = {}
    for p in pages:
        parts = p.split("/")
        if parts:
            prefix = parts[0]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
    if not prefixes:
        return None
    return max(prefixes, key=lambda k: prefixes[k])


def build_section_lines(
    node: object,
    repo_root: Path,
    base_url: str,
    depth: int = 0,
) -> list[str]:
    """
    Recursively build llms.txt lines from a navigation node.

    Preserves section hierarchy: sub-groups become ## headers,
    pages become list entries with title and description.

    Args:
        node: A navigation node — string (page path), dict (group), or list.
        repo_root: Root path of the product-documentation repo.
        base_url: Base URL for building page URLs.
        depth: Current nesting depth (0 = top-level product group).

    Returns:
        List of formatted text lines.
    """
    lines: list[str] = []

    if isinstance(node, str):
        mdx_file = repo_root / (node + ".mdx")
        fm = read_frontmatter(mdx_file)
        title = fm.get("title") or fm.get("sidebarTitle") or node.split("/")[-1]
        description = fm.get("ai-navigation", "")
        url = page_to_url(node, base_url)
        if description:
            lines.append(f"- [{title}]({url}): {description}")
        else:
            lines.append(f"- [{title}]({url})")

    elif isinstance(node, dict):
        group_name = node.get("group", "")
        pages = node.get("pages", [])
        if group_name and depth > 0:
            lines.append(f"\n## {group_name}")
        for item in pages:
            lines.extend(build_section_lines(item, repo_root, base_url, depth + 1))

    elif isinstance(node, list):
        for item in node:
            lines.extend(build_section_lines(item, repo_root, base_url, depth))

    return lines


def build_product_llms(
    group: dict,
    repo_root: Path,
    base_url: str,
) -> tuple[str, Optional[str]]:
    """
    Build llms.txt content for one top-level product group.

    Preserves section hierarchy from docs.json as ## headers.

    Args:
        group: The top-level group dict from docs.json.
        repo_root: Root path of the product-documentation repo.
        base_url: Base URL for building page URLs.

    Returns:
        Tuple of (file_content, product_prefix).
    """
    group_name: str = group.get("group", "Unknown")
    product_prefix = get_product_prefix(group)
    page_count = len(collect_pages(group))

    header = [f"# Gcore {group_name}", ""]
    body_lines = build_section_lines(group, repo_root, base_url, depth=0)

    # Remove leading blank line if first body line is a section header
    while body_lines and body_lines[0] == "":
        body_lines.pop(0)

    content = "\n".join(header + body_lines) + "\n"
    log.info("  Built %s/llms.txt: %d pages", product_prefix or group_name, page_count)
    return content, product_prefix


def build_root_llms(
    product_entries: list[tuple[str, str, int]],
    product_bodies: list[tuple[str, list[str]]],
    base_url: str,
) -> str:
    """
    Build the root llms.txt with all articles from all products.

    The file starts with a short header and product index for quick navigation,
    then lists all pages grouped by product section. This ensures an AI agent
    reading only the root file gets complete discoverability without needing
    to follow per-product links.

    Args:
        product_entries: List of (group_name, product_prefix, page_count).
        product_bodies: List of (group_name, body_lines) for each product.
        base_url: Base URL for building product index URLs.

    Returns:
        Content of the root llms.txt file.
    """
    lines = [
        "# Gcore Docs",
        "",
        "Documentation for Gcore Cloud, CDN, DNS, Storage, FastEdge, and other products.",
        f"MCP Server: {base_url}/account-settings/integrations/gcore-mcp-server-overview.md",
        "GitHub repo (raw MDX): https://github.com/G-Core/product-documentation",
        "",
    ]

    for group_name, body_lines in product_bodies:
        lines.append(f"## {group_name}")
        lines.append("")
        lines.extend(body_lines)
        lines.append("")

    return "\n".join(lines)


def write_or_print(path: Path, content: str, dry_run: bool) -> None:
    """Write content to file, or print preview to stdout if dry_run."""
    if dry_run:
        print(f"\n{'='*60}")
        print(f"FILE: {path}")
        print("=" * 60)
        print(content[:800] + ("...\n" if len(content) > 800 else ""))
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        log.info("Written: %s (%d lines)", path, content.count("\n"))


def main() -> int:
    """Entry point."""
    args = parse_args()
    repo_root: Path = args.repo.resolve()
    base_url: str = args.base_url
    dry_run: bool = args.dry_run

    docs_json_path = repo_root / DOCS_JSON_NAME
    if not docs_json_path.exists():
        log.error("docs.json not found at %s", docs_json_path)
        return 1

    try:
        docs_json = json.loads(docs_json_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        log.error("Failed to read docs.json: %s", exc)
        return 1

    tabs = docs_json.get("navigation", {}).get("tabs", [])
    doc_tab = next((t for t in tabs if t.get("tab") == DOCUMENTATION_TAB), None)
    if not doc_tab:
        log.error("Tab '%s' not found in docs.json", DOCUMENTATION_TAB)
        return 1

    product_entries: list[tuple[str, str, int]] = []
    product_bodies: list[tuple[str, list[str]]] = []

    for group in doc_tab.get("groups", []):
        group_name: str = group.get("group", "Unknown")
        page_count = len(collect_pages(group))

        if page_count == 0:
            log.warning("No pages found for group: %s", group_name)
            continue

        log.info("Processing group '%s': %d pages", group_name, page_count)
        content, product_prefix = build_product_llms(group, repo_root, base_url)

        if not product_prefix:
            log.warning("Cannot determine prefix for group '%s', skipping", group_name)
            continue

        output_path = repo_root / product_prefix / "llms.txt"
        write_or_print(output_path, content, dry_run)
        product_entries.append((group_name, product_prefix, page_count))

        body_lines = build_section_lines(group, repo_root, base_url, depth=0)
        while body_lines and body_lines[0] == "":
            body_lines.pop(0)
        product_bodies.append((group_name, body_lines))

    root_content = build_root_llms(product_entries, product_bodies, base_url)
    root_path = repo_root / "llms.txt"
    write_or_print(root_path, root_content, dry_run)

    log.info("Done. Generated %d product files + root llms.txt", len(product_entries))
    return 0


if __name__ == "__main__":
    sys.exit(main())
