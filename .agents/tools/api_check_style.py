"""API MethodSection style checker for Gcore documentation MDX.

Usage:
    python .agents/tools/api_check_style.py path/to/article.mdx
    python .agents/tools/api_check_style.py --all

Add a new function to CHECKS when a repeatable API-tab mistake shows up.
Pair it with a case in test_api_check_style.py.
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

CheckFn = Callable[[list[str]], list["Violation"]]

# SDK tabs where a raw HTTP JSON body after </Tabs> is the wrong surface.
# Language-variant curl groups (Modern Rust / JavaScript with bash) are ignored.
_SDK_TAB_TITLES = frozenset(
    {
        "python sdk",
        "go sdk",
        "python",
        "go",
    }
)

_TAB_TITLE = re.compile(r"<Tab\s+title=[\"']([^\"']+)[\"']", re.IGNORECASE)

_SKIP_DIR_NAMES = frozenset(
    {
        "_drafts",
        "_planning",
        "_deprecated",
        "node_modules",
        ".git",
        "venv",
        "__pycache__",
    }
)


@dataclass(frozen=True)
class Violation:
    """A single checker finding."""

    line: int
    rule: str
    detail: str
    text: str


def _is_fence(line: str) -> bool:
    return line.lstrip().startswith("```")


def _fence_lang(line: str) -> str:
    rest = line.lstrip()[3:].strip()
    if not rest:
        return ""
    return rest.split()[0].lower()


def _tab_title(line: str) -> str | None:
    match = _TAB_TITLE.search(line)
    if match is None:
        return None
    return match.group(1).strip().lower()


def _is_region_end(stripped: str) -> bool:
    return (
        stripped.startswith("##")
        or stripped.startswith("<Tabs")
        or stripped.startswith("</MethodSection>")
        or stripped.startswith("<Accordion")
        or stripped.startswith("</Accordion>")
        or stripped.startswith("<MethodSection")
    )


def check_response_outside_tabs(lines: Sequence[str]) -> list[Violation]:
    """HTTP response JSON after SDK Tabs belongs inside the curl tab.

    Content after ``</Tabs>`` is visible in every tab of that group. Flag a JSON
    fence only when the preceding group included a Python or Go SDK tab. OS
    tabs, language-variant curl groups (Modern Rust / JavaScript), and prose
    without a JSON block are ignored.
    """
    violations: list[Violation] = []
    in_fence = False
    tabs_depth = 0
    group_has_sdk = False
    after_sdk_tabs = False

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            lang = _fence_lang(raw)
            if not in_fence and after_sdk_tabs and lang == "json":
                violations.append(
                    Violation(
                        line=lineno,
                        rule="response-json-outside-tabs",
                        detail=(
                            "JSON response is after </Tabs>. Put it inside the "
                            "curl tab (or the tab whose call produced this body)."
                        ),
                        text=stripped[:120],
                    )
                )
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        if stripped.startswith("<Tabs"):
            tabs_depth += 1
            group_has_sdk = False
            after_sdk_tabs = False
            continue

        title = _tab_title(stripped)
        if title is not None and tabs_depth > 0 and title in _SDK_TAB_TITLES:
            group_has_sdk = True
            continue

        if "</Tabs>" in stripped:
            after_sdk_tabs = group_has_sdk
            if tabs_depth > 0:
                tabs_depth -= 1
            group_has_sdk = False
            continue

        if after_sdk_tabs and _is_region_end(stripped):
            after_sdk_tabs = False

    return violations


CHECKS: tuple[CheckFn, ...] = (check_response_outside_tabs,)


def lint(path: Path) -> list[Violation]:
    """Run every registered API style check against one MDX file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    violations: list[Violation] = []
    for check in CHECKS:
        violations.extend(check(lines))
    violations.sort(key=lambda item: item.line)
    return violations


def iter_mdx_files(root: Path) -> list[Path]:
    """Return article MDX files under root, skipping draft and vendor dirs."""
    found: list[Path] = []
    for path in root.rglob("*.mdx"):
        if any(part in _SKIP_DIR_NAMES for part in path.parts):
            continue
        found.append(path)
    found.sort()
    return found


def _repo_root() -> Path:
    here = Path(__file__).resolve().parent
    return here.parents[1]


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point. Returns 0 on a clean run, 1 on violations."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description="Check REST API tab style in MDX articles.")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="Path to one article .mdx file",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Scan every .mdx file in the documentation repo",
    )
    args = parser.parse_args(argv)

    if args.all:
        paths = iter_mdx_files(_repo_root())
    elif args.path is not None:
        if not args.path.exists():
            log.error("File not found: %s", args.path)
            return 1
        paths = [args.path]
    else:
        parser.error("pass a file path or --all")
        return 2

    dirty = 0
    total_hits = 0
    for path in paths:
        found = lint(path)
        if not found:
            continue
        dirty += 1
        total_hits += len(found)
        log.info("=== %s (%s) ===", path, len(found))
        for item in found:
            log.info("  L%s [%s] %s", item.line, item.rule, item.text)
        log.info("")

    if args.all:
        log.info("Scanned %s mdx files, %s with violations (%s hits)", len(paths), dirty, total_hits)
        return 1 if dirty else 0

    if total_hits == 0:
        log.info("OK - no API style violations in %s", paths[0])
        return 0

    log.info("%s violation(s) in %s", total_hits, paths[0])
    return 1


if __name__ == "__main__":
    sys.exit(main())
