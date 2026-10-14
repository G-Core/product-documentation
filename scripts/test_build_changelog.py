"""Tests for changelog feed validation and page generation."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from build_changelog import ChangelogError, build, heading_slug


def write_json(path: Path, payload: dict) -> None:
    """Write one JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def item(item_id: str, product: str, announced: str, source: str, **extra: object) -> dict:
    """Return a valid feed record."""
    payload = {
        "id": item_id,
        "product": product,
        "title": f"Title {item_id}",
        "summary": "A customer can do this.",
        "available_since": announced,
        "announced_at": announced,
        "url": f"/changelog#{item_id}",
        "guide_url": "/guides/topic#section",
        "guide_label": "Guide",
        "kind": "new",
        "sources": [source],
        "distinct_from": [],
    }
    payload.update(extra)
    return payload


def repo_with(items: list[dict]) -> Path:
    """Create a temporary repo with a guide page and feed records."""
    root = Path(tempfile.mkdtemp())
    guide = root / "guides" / "topic.mdx"
    guide.parent.mkdir(parents=True)
    guide.write_text("# Topic\n\n### Section\n", encoding="utf-8")
    write_json(root / ".whats-new" / "products.json", {"products": {"streaming": "Video Streaming", "cdn": "CDN"}, "renames": {}})
    for payload in items:
        write_json(root / ".whats-new" / "feed" / f"{payload['id']}.json", payload)
    return root


class SlugTests(unittest.TestCase):
    """Heading ids match the docs renderer."""

    def test_slug_drops_punctuation(self) -> None:
        self.assertEqual(heading_slug("PUSH link formats"), "push-link-formats")


class BuildTests(unittest.TestCase):
    """Generator order, limits, and refusals."""

    def test_same_inputs_write_the_same_pages(self) -> None:
        root = repo_with(
            [
                item("streaming-b", "streaming", "2026-09-22", "src-b"),
                item("streaming-a", "streaming", "2026-09-22", "src-a"),
                item("cdn-a", "cdn", "2026-10-01", "src-c"),
            ]
        )
        build(root, check=False)
        first = (root / "changelog.mdx").read_text(encoding="utf-8")
        build(root, check=True)
        self.assertEqual((root / "changelog.mdx").read_text(encoding="utf-8"), first)
        self.assertIn("ChangelogDashboard", first)
        self.assertIn("CDN", first)
        self.assertLess(first.index("CDN"), first.index("Video Streaming"))
        self.assertLess(first.index('"id": "streaming-a"'), first.index('"id": "streaming-b"'))
        self.assertNotIn("changelog-items", first)
        self.assertFalse((root / "streaming" / "whats-new.mdx").exists())

    def test_window_lists_every_record(self) -> None:
        payloads = [item(f"streaming-{index}", "streaming", f"2026-01-{index:02d}", f"src-{index}") for index in range(1, 8)]
        root = repo_with(payloads)
        build(root, check=False)
        text = (root / "changelog.mdx").read_text(encoding="utf-8")
        self.assertLess(text.index('"id": "streaming-7"'), text.index('"id": "streaming-1"'))
        self.assertIn("A customer can do this.", text)

    def test_duplicate_source_is_rejected(self) -> None:
        root = repo_with(
            [
                item("streaming-a", "streaming", "2026-09-01", "same"),
                item("streaming-b", "streaming", "2026-09-02", "same"),
            ]
        )
        with self.assertRaises(ChangelogError):
            build(root, check=False)

    def test_marked_distinct_source_is_allowed(self) -> None:
        root = repo_with(
            [
                item("streaming-a", "streaming", "2026-09-01", "same", distinct_from=["streaming-b"]),
                item("streaming-b", "streaming", "2026-09-02", "same", distinct_from=["streaming-a"]),
            ]
        )
        build(root, check=False)

    def test_missing_guide_anchor_is_rejected(self) -> None:
        payload = item("streaming-a", "streaming", "2026-09-01", "src")
        payload["guide_url"] = "/guides/topic#missing"
        root = repo_with([payload])
        with self.assertRaises(ChangelogError):
            build(root, check=False)


if __name__ == "__main__":
    unittest.main()
