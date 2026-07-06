"""Convert <img src="..." alt="..." width="N%"/> to markdown shorthand ![alt](src).

Only converts img tags that have a percentage width attribute.
Handles any attribute order. Writes UTF-8 LF without BOM.
"""
import argparse
import logging
import os
import re
import sys

log = logging.getLogger(__name__)

# Matches self-closing <img .../> that contains a width="N%" attribute
IMG_PATTERN = re.compile(r'<img\b([^>]*?)\/>', re.DOTALL)


def _get_attr(attrs: str, name: str) -> str | None:
    """Extract attribute value by name from an attribute string."""
    m = re.search(rf'{name}="([^"]*)"', attrs)
    return m.group(1) if m else None


def convert_content(content: str) -> tuple[str, int]:
    """Return (updated_content, replacement_count)."""
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        attrs = m.group(1)
        # Only process if it has a percentage width attribute
        width = _get_attr(attrs, "width")
        if not width or not width.endswith("%"):
            return m.group(0)
        src = _get_attr(attrs, "src")
        alt = _get_attr(attrs, "alt") or ""
        if not src:
            return m.group(0)
        count += 1
        return f"![{alt}]({src})"

    updated = IMG_PATTERN.sub(replacer, content)
    return updated, count


def convert_file(path: str, dry_run: bool) -> int:
    with open(path, encoding="utf-8") as fh:
        original = fh.read()

    updated, count = convert_content(original)
    if count == 0:
        return 0

    if dry_run:
        log.info("DRY RUN %s: %d replacement(s)", path, count)
        return count

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(updated)
    log.info("Fixed %s: %d replacement(s)", path, count)
    return count


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=".", help="Root directory to scan")
    args = parser.parse_args()

    total_files = 0
    total_replacements = 0

    for dirpath, dirnames, filenames in os.walk(args.root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for fname in filenames:
            if not fname.endswith(".mdx"):
                continue
            path = os.path.join(dirpath, fname)
            n = convert_file(path, args.dry_run)
            if n:
                total_files += 1
                total_replacements += n

    log.info("Done: %d replacement(s) in %d file(s)", total_replacements, total_files)
    if args.dry_run:
        log.info("Re-run without --dry-run to apply.")


if __name__ == "__main__":
    main()
