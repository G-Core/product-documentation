"""Build the Gcore changelog page.

Reads ``.whats-new/feed/*.json`` and ``.whats-new/products.json``. Writes
``changelog.mdx``. The same inputs always produce the same file.

Each product is one full-width card. The page embeds the records in
``changelog.mdx`` and ``snippets/changelog-dashboard.jsx`` renders them.
Card order uses ``announced_at``. Months inside a card use ``available_since``.

Usage:
    python scripts/build_changelog.py --repo C:/Projects/product-documentation
    python scripts/build_changelog.py --repo C:/Projects/product-documentation --check
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

log = logging.getLogger(__name__)

KINDS = ("new", "improved", "fixed")
KIND_LABEL = {"new": "New", "improved": "Improved", "fixed": "Fixed"}
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
ANCHOR_RE = re.compile(r"""\bid=["']([^"']+)["']""")
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
SHORT_MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


class ChangelogError(Exception):
    """The feed cannot be built into pages."""


@dataclass(frozen=True)
class FeedItem:
    """One published news item."""

    id: str
    product: str
    title: str
    summary: str
    available_since: date
    announced_at: date
    url: str
    guide_url: str
    guide_label: str
    kind: str
    sources: tuple[str, ...]
    distinct_from: tuple[str, ...]
    path: Path


@dataclass(frozen=True)
class ProductInfo:
    """Display name for a docs folder, plus folder renames."""

    labels: dict[str, str]
    renames: dict[str, str]

    def resolve(self, product: str) -> str:
        """Return the current docs folder for a product name."""
        return self.renames.get(product, product)

    def label(self, product: str) -> str:
        """Return the customer-facing product name."""
        folder = self.resolve(product)
        return self.labels[folder]


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="Repository root.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 when generated files differ from what is on disk.",
    )
    return parser.parse_args()


def heading_slug(text: str) -> str:
    """Match Mintlify's heading id for a heading string."""
    lowered = text.strip().lower()
    cleaned = re.sub(r"[^\w\s-]", "", lowered, flags=re.UNICODE)
    return re.sub(r"\s+", "-", cleaned).strip("-")


def parse_iso(value: str, field: str, path: Path) -> date:
    """Parse an ISO date or raise ChangelogError."""
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except (TypeError, ValueError) as exc:
        raise ChangelogError(f"{path}: {field} must be YYYY-MM-DD") from exc


def load_products(repo: Path) -> ProductInfo:
    """Load product labels and the rename map."""
    path = repo / ".whats-new" / "products.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    labels = {str(key): str(value) for key, value in data.get("products", {}).items()}
    renames = {str(key): str(value) for key, value in data.get("renames", {}).items()}
    if not labels:
        raise ChangelogError(f"{path}: products is empty")
    return ProductInfo(labels=labels, renames=renames)


def load_feed(repo: Path) -> list[FeedItem]:
    """Load every feed record."""
    folder = repo / ".whats-new" / "feed"
    if not folder.is_dir():
        raise ChangelogError(f"{folder} does not exist")
    items: list[FeedItem] = []
    for path in sorted(folder.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        sources = tuple(str(item) for item in data.get("sources", []))
        distinct = tuple(str(item) for item in data.get("distinct_from", []))
        items.append(
            FeedItem(
                id=str(data["id"]),
                product=str(data["product"]),
                title=str(data["title"]),
                summary=str(data["summary"]),
                available_since=parse_iso(str(data["available_since"]), "available_since", path),
                announced_at=parse_iso(str(data["announced_at"]), "announced_at", path),
                url=str(data["url"]),
                guide_url=str(data["guide_url"]),
                guide_label=str(data["guide_label"]),
                kind=str(data["kind"]),
                sources=sources,
                distinct_from=distinct,
                path=path,
            )
        )
    return items


def page_file(repo: Path, url_path: str) -> Path:
    """Return the MDX file for a root-relative docs path."""
    relative = url_path.strip("/")
    return repo / f"{relative}.mdx"


def guide_exists(repo: Path, url_path: str) -> bool:
    """Return whether a docs path is an MDX page or a navigation entry."""
    if page_file(repo, url_path).is_file():
        return True
    docs_file = repo / "docs.json"
    if not docs_file.is_file():
        return False
    needle = url_path.strip("/")

    def walk(node: object) -> bool:
        if isinstance(node, str):
            return node.strip("/") == needle
        if isinstance(node, dict):
            directory = node.get("directory")
            if isinstance(directory, str) and directory.strip("/") == needle:
                return True
            return any(walk(value) for value in node.values())
        if isinstance(node, list):
            return any(walk(value) for value in node)
        return False

    return walk(json.loads(docs_file.read_text(encoding="utf-8")))


def anchors_in(path: Path) -> set[str]:
    """Return heading slugs and explicit ids in an MDX file."""
    if not path.is_file():
        return set()
    text = path.read_text(encoding="utf-8")
    found = {heading_slug(match.group(1)) for match in HEADING_RE.finditer(text)}
    found.update(ANCHOR_RE.findall(text))
    return found


def require(condition: bool, message: str, errors: list[str]) -> None:
    """Append message when condition is false."""
    if not condition:
        errors.append(message)


def validate(repo: Path, products: ProductInfo, items: list[FeedItem]) -> None:
    """Reject a feed that would publish a broken or duplicate page."""
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}
    by_source: dict[str, list[FeedItem]] = {}
    known_ids = {item.id for item in items}

    for item in items:
        folder = products.resolve(item.product)
        require(folder in products.labels, f"{item.path}: unknown product {item.product}", errors)
        require(item.kind in KINDS, f"{item.path}: kind must be one of {', '.join(KINDS)}", errors)
        require(bool(item.sources), f"{item.path}: sources is empty", errors)
        expected = f"/changelog#{item.id}"
        require(item.url == expected, f"{item.path}: url must be {expected}", errors)
        require("{" not in item.summary and "}" not in item.summary, f"{item.path}: summary must not contain braces", errors)
        if item.id in seen_ids:
            errors.append(f"{item.path}: duplicate id {item.id}")
        seen_ids[item.id] = item.path
        for source in item.sources:
            by_source.setdefault(source, []).append(item)
        for other in item.distinct_from:
            require(other in known_ids, f"{item.path}: distinct_from {other} is not a feed id", errors)
        guide_path, _, fragment = item.guide_url.partition("#")
        guide_file = page_file(repo, guide_path)
        require(guide_exists(repo, guide_path), f"{item.path}: guide page does not exist: {guide_path}", errors)
        if fragment:
            require(
                guide_file.is_file() and fragment in anchors_in(guide_file),
                f"{item.path}: guide anchor does not exist: {fragment}",
                errors,
            )

    for source, group in by_source.items():
        if len(group) < 2:
            continue
        ids = {item.id for item in group}
        for item in group:
            if not ids.issubset(set(item.distinct_from) | {item.id}):
                errors.append(f"{item.path}: source {source} is shared and not marked distinct_from the other ids")

    if errors:
        raise ChangelogError("\n".join(errors))


def sort_items(items: list[FeedItem]) -> list[FeedItem]:
    """Sort newest announcement first. Equal dates sort by id."""
    return sorted(items, key=lambda item: (-item.announced_at.toordinal(), item.id))


def sort_products(products: ProductInfo, items: list[FeedItem]) -> list[str]:
    """Sort product folders by their newest announcement, then by folder name.

    Products with no records follow, ordered by folder name.
    """
    latest: dict[str, date] = {}
    for item in items:
        folder = products.resolve(item.product)
        current = latest.get(folder)
        if current is None or item.announced_at > current:
            latest[folder] = item.announced_at
    ranked = sorted(latest, key=lambda folder: (-latest[folder].toordinal(), folder))
    rest = sorted(folder for folder in products.labels if folder not in latest)
    return ranked + rest


def month_label(value: date) -> str:
    """Return a month heading such as September 2026."""
    return f"{MONTHS[value.month - 1]} {value.year}"


def product_items(products: ProductInfo, folder: str, items: list[FeedItem]) -> list[FeedItem]:
    """Return one product's records, newest announcement first."""
    own = [item for item in items if products.resolve(item.product) == folder]
    return sort_items(own)


def short_month(value: date) -> str:
    """Return a compact month such as Oct 2026."""
    return f"{SHORT_MONTHS[value.month - 1]} {value.year}"


def render_page(products: ProductInfo, items: list[FeedItem]) -> str:
    """Render the changelog page as data for the dashboard component."""
    payload_products = []
    payload_items = []
    for folder in sort_products(products, items):
        own = product_items(products, folder, items)
        payload_products.append({"id": folder, "label": products.label(folder), "count": len(own)})
        for item in own:
            payload_items.append(
                {
                    "id": item.id,
                    "product": folder,
                    "title": item.title,
                    "summary": item.summary,
                    "month": month_label(item.available_since.replace(day=1)),
                    "shortMonth": short_month(item.announced_at),
                    "kind": item.kind,
                    "kindLabel": KIND_LABEL[item.kind],
                    "guideUrl": item.guide_url,
                    "guideLabel": item.guide_label,
                }
            )
    encoded = json.dumps({"products": payload_products, "items": payload_items}, ensure_ascii=False, indent=2)
    encoded = encoded.replace("<", "\\u003c")
    parts = [
        "---",
        "title: Gcore changelog",
        "sidebarTitle: Changelog",
        "description: Product updates from Gcore, with each product history in its own window.",
        "---",
        "",
        "{/* Generated by scripts/build_changelog.py. Do not edit. */}",
        "",
        'import { ChangelogDashboard } from "/snippets/changelog-dashboard.jsx"',
        "",
        f"<ChangelogDashboard data={{{encoded}}} />",
        "",
    ]
    return "\n".join(parts)


def outputs(repo: Path, products: ProductInfo, items: list[FeedItem]) -> dict[Path, str]:
    """Return the files the generator would write."""
    return {repo / "changelog.mdx": render_page(products, items)}


def build(repo: Path, check: bool) -> None:
    """Validate the feed and write pages, or compare them in check mode."""
    products = load_products(repo)
    items = load_feed(repo)
    validate(repo, products, items)
    rendered = outputs(repo, products, items)
    drifted: list[str] = []
    for path, text in rendered.items():
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == text:
            continue
        if check:
            drifted.append(str(path.relative_to(repo)))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        log.info("Wrote %s", path.relative_to(repo))
    if drifted:
        raise ChangelogError("Generated files differ:\n" + "\n".join(drifted))


def main() -> None:
    """Run the generator."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    try:
        build(args.repo, args.check)
    except ChangelogError as exc:
        log.error("%s", exc)
        sys.exit(1)
    except (OSError, json.JSONDecodeError, KeyError) as exc:
        log.error("%s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
