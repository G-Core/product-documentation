"""Tests for SEO description validation and frontmatter replacement."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from generate_seo_descriptions import (
    clean_reply,
    validation_error,
    write_description,
)


class ValidationTests(unittest.TestCase):
    """Rule checks for a drafted description."""

    def test_accepts_a_short_summary(self) -> None:
        text = "Placement groups keep Virtual Machines together or spread them across servers."
        self.assertEqual(validation_error(text), "")

    def test_rejects_method_names_and_length(self) -> None:
        self.assertIn("Portal", validation_error("Create a resource via the Customer Portal."))
        long_text = ("A" * 140) + "."
        self.assertIn("141", validation_error(long_text))


class ReplyTests(unittest.TestCase):
    """Cleanup of model output."""

    def test_strips_label_and_quotes(self) -> None:
        self.assertEqual(clean_reply('description: "Create a volume."'), "Create a volume.")

    def test_adds_a_missing_period(self) -> None:
        self.assertEqual(clean_reply("Create a volume"), "Create a volume.")


class WriteTests(unittest.TestCase):
    """Frontmatter edits keep the file's line endings."""

    def test_replaces_description_and_keeps_crlf(self) -> None:
        original = "---\r\ntitle: Volumes\r\ndescription: Old text.\r\n---\r\n\r\nBody\r\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "article.mdx"
            path.write_bytes(original.encode("utf-8"))
            write_description(path, "Create a block storage volume.")
            updated = path.read_bytes().decode("utf-8")
        self.assertIn("description: Create a block storage volume.\r\n", updated)
        self.assertIn("title: Volumes\r\n", updated)
        self.assertNotIn("Old text.", updated)


if __name__ == "__main__":
    unittest.main()
