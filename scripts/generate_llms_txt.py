"""
Generate per-product llms.txt files from docs.json navigation structure.

Reads docs.json from the product-documentation repo, extracts page paths
per top-level product group preserving section hierarchy, reads MDX frontmatter
for titles and descriptions, and writes per-product llms.txt files plus a
root llms.txt product index.

Root llms.txt is a curated meta-index (one entry per product) kept under
50,000 characters so it is not truncated by agent platforms. Per-product
llms.txt files contain the full article list with ai-navigation descriptions.

Usage:
    python scripts/generate_llms_txt.py \\
        --repo C:/Projects/product-documentation \\
        --base-url https://gcore.com/docs

Output:
    {repo}/llms.txt                    - root index linking to per-product files
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
MCP_ARTICLE_PATH = "developer-tools/mcp-server/gcore-mcp-server-overview"

ROOT_SIZE_WARN = 50_000
ROOT_SIZE_ERROR = 100_000


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
        content = mdx_path.read_text(encoding="utf-8-sig")
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
    """Convert a page path to a .md URL for direct Markdown delivery."""
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


def derive_product_summary(group: dict, repo_root: Path) -> str:
    """
    Derive a one-line product summary for use in the root index and blockquote.

    Tries, in order:
    1. ai-navigation of the product's root overview page (first string page in group).
    2. Comma-separated list of sub-group names from docs.json.

    Args:
        group: Top-level group dict from docs.json.
        repo_root: Root path of the product-documentation repo.

    Returns:
        A non-empty summary string.
    """
    pages = group.get("pages", [])

    for item in pages:
        if isinstance(item, str):
            mdx_path = repo_root / (item + ".mdx")
            fm = read_frontmatter(mdx_path)
            nav = fm.get("ai-navigation", "")
            if nav:
                return nav
            break

    sub_groups = [item["group"] for item in pages if isinstance(item, dict) and "group" in item]
    if sub_groups:
        return ", ".join(sub_groups) + "."

    return group.get("group", "")


def build_section_lines(
    node: object,
    repo_root: Path,
    base_url: str,
    depth: int = 0,
    missing_nav: Optional[list[str]] = None,
) -> list[str]:
    """
    Recursively build llms.txt lines from a navigation node.

    Preserves section hierarchy: sub-groups become ## headers,
    pages become list entries with title and description.

    Args:
        node: A navigation node - string (page path), dict (group), or list.
        repo_root: Root path of the product-documentation repo.
        base_url: Base URL for building page URLs.
        depth: Current nesting depth (0 = top-level product group).
        missing_nav: Optional list to collect paths missing ai-navigation.

    Returns:
        List of formatted text lines.
    """
    lines: list[str] = []

    if isinstance(node, str):
        mdx_file = repo_root / (node + ".mdx")
        if not mdx_file.exists():
            log.warning("MDX file not found, skipping: %s", mdx_file)
            return lines
        fm = read_frontmatter(mdx_file)
        title = fm.get("title") or fm.get("sidebarTitle") or node.split("/")[-1]
        description = fm.get("ai-navigation", "")
        url = page_to_url(node, base_url)
        if not url.endswith(".md"):
            log.warning("URL does not end with .md, check page_to_url: %s", url)
        if description:
            lines.append(f"- [{title}]({url}): {description}")
        else:
            lines.append(f"- [{title}]({url})")
            if missing_nav is not None:
                missing_nav.append(node)

    elif isinstance(node, dict):
        group_name = node.get("group", "")
        pages = node.get("pages", [])
        if group_name and depth > 0:
            lines.append(f"\n## {group_name}")
        for item in pages:
            lines.extend(
                build_section_lines(item, repo_root, base_url, depth + 1, missing_nav)
            )

    elif isinstance(node, list):
        for item in node:
            lines.extend(
                build_section_lines(item, repo_root, base_url, depth, missing_nav)
            )

    return lines


def build_product_llms(
    group: dict,
    repo_root: Path,
    base_url: str,
    missing_nav: list[str],
) -> tuple[str, Optional[str], str]:
    """
    Build llms.txt content for one top-level product group.

    Includes a spec-compliant blockquote summary between H1 and page list.

    Args:
        group: The top-level group dict from docs.json.
        repo_root: Root path of the product-documentation repo.
        base_url: Base URL for building page URLs.
        missing_nav: Accumulator for pages missing ai-navigation.

    Returns:
        Tuple of (file_content, product_prefix, product_summary).
    """
    group_name: str = group.get("group", "Unknown")
    product_prefix = get_product_prefix(group)
    page_count = len(collect_pages(group))

    summary = derive_product_summary(group, repo_root)
    body_lines = build_section_lines(group, repo_root, base_url, depth=0, missing_nav=missing_nav)

    while body_lines and body_lines[0] == "":
        body_lines.pop(0)

    lines = [
        f"# Gcore {group_name}",
        "",
        f"> {summary}",
        "",
    ]
    lines.extend(body_lines)
    content = "\n".join(lines) + "\n"
    log.info("  Built %s/llms.txt: %d pages", product_prefix or group_name, page_count)
    return content, product_prefix, summary


def build_root_llms(
    product_entries: list[tuple[str, str, int, str]],
    base_url: str,
) -> str:
    """
    Build the root llms.txt as a curated product meta-index.

    The root file links to per-product llms.txt files instead of listing all
    articles directly. This keeps the root under the 50,000 character threshold
    above which agent platforms may truncate the file.

    Per the llms.txt spec, the file contains:
    - H1 with site name
    - Blockquote with summary
    - H2 section with product index (links to per-product llms.txt)
    - H2 Optional section with agent integration links

    Args:
        product_entries: List of (group_name, product_prefix, page_count, summary).
        base_url: Base URL for building product index URLs.

    Returns:
        Content of the root llms.txt file.
    """
    mcp_url = page_to_url(MCP_ARTICLE_PATH, base_url)
    product_names = ", ".join(e[0] for e in product_entries)

    lines = [
        "# Gcore Docs",
        "",
        f"> Official documentation for Gcore products: {product_names}.",
        "> Each product section has a dedicated llms.txt with the full article index.",
        "",
        "## Products",
        "",
    ]

    for group_name, product_prefix, page_count, summary in product_entries:
        product_llms_url = f"{base_url.rstrip('/')}/{product_prefix}/llms.txt"
        short_summary = summary.rstrip(".")
        lines.append(
            f"- [{group_name}]({product_llms_url}): {short_summary} ({page_count} articles)."
        )

    lines += [
        "",
        "## Optional",
        "",
        f"- [Gcore MCP Server]({mcp_url}): Connect AI agents (Claude Code, Cursor IDE)"
        " to Gcore via MCP to manage Cloud, CDN, DNS, and other products through"
        " natural language commands.",
    ]

    return "\n".join(lines) + "\n"


def check_root_size(content: str, path: Path) -> None:
    """
    Warn if root llms.txt exceeds recommended size thresholds.

    Args:
        content: Root file content.
        path: Path for logging context.
    """
    size = len(content)
    if size > ROOT_SIZE_ERROR:
        log.warning(
            "Root %s is %d characters (>%d). Major agent platforms may truncate it."
            " Consider splitting into per-product files.",
            path, size, ROOT_SIZE_ERROR,
        )
    elif size > ROOT_SIZE_WARN:
        log.warning(
            "Root %s is %d characters (>%d). Approaching truncation risk.",
            path, size, ROOT_SIZE_WARN,
        )
    else:
        log.info("Root size: %d characters (within safe threshold).", size)


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
        log.info("Written: %s (%d chars, %d lines)", path, len(content), content.count("\n"))


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

    product_entries: list[tuple[str, str, int, str]] = []
    missing_nav: list[str] = []
    total_pages = 0

    for group in doc_tab.get("groups", []):
        group_name: str = group.get("group", "Unknown")
        page_count = len(collect_pages(group))

        if page_count == 0:
            log.warning("No pages found for group: %s", group_name)
            continue

        log.info("Processing group '%s': %d pages", group_name, page_count)
        content, product_prefix, summary = build_product_llms(
            group, repo_root, base_url, missing_nav
        )

        if not product_prefix:
            log.warning("Cannot determine prefix for group '%s', skipping", group_name)
            continue

        output_path = repo_root / product_prefix / "llms.txt"
        write_or_print(output_path, content, dry_run)
        product_entries.append((group_name, product_prefix, page_count, summary))
        total_pages += page_count

    root_content = build_root_llms(product_entries, base_url)
    root_path = repo_root / "llms.txt"
    check_root_size(root_content, root_path)
    write_or_print(root_path, root_content, dry_run)

    missing_count = len(missing_nav)
    if missing_count:
        log.warning(
            "ai-navigation missing: %d/%d pages. Files: %s",
            missing_count, total_pages,
            ", ".join(missing_nav[:10]) + ("..." if missing_count > 10 else ""),
        )
    else:
        log.info("ai-navigation coverage: %d/%d pages (100%%).", total_pages, total_pages)

    log.info(
        "Done. %d products, %d total pages, %d missing ai-navigation.",
        len(product_entries), total_pages, missing_count,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
