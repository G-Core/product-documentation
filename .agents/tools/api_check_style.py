"""API MethodSection style checker for Gcore documentation MDX.

Usage:
    python .agents/tools/api_check_style.py path/to/article.mdx

Add a new function to CHECKS when a repeatable API-tab mistake shows up.
Pair it with a case in test_api_check_style.py.
"""

from __future__ import annotations

import argparse
import logging
import sys
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger(__name__)

CheckFn = Callable[[list[str]], list["Violation"]]


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


def check_response_outside_tabs(lines: Sequence[str]) -> list[Violation]:
    """HTTP response JSON / 'The API returns' must sit inside the producing tab.

    Content after ``</Tabs>`` is visible in every method tab (Python, Go, curl).
    Curl response bodies therefore belong inside ``<Tab title="curl">``, not
    after the closing ``</Tabs>``.
    """
    violations: list[Violation] = []
    in_fence = False
    after_tabs = False

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            lang = _fence_lang(raw)
            if not in_fence and after_tabs and lang == "json":
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

        if "</Tabs>" in stripped:
            after_tabs = True
            continue

        if after_tabs and (
            stripped.startswith("##")
            or stripped.startswith("<Tabs")
            or stripped.startswith("</MethodSection>")
            or stripped.startswith("<Accordion")
            or stripped.startswith("</Accordion>")
        ):
            after_tabs = False
            continue

        if after_tabs and "the api returns" in stripped.lower():
            violations.append(
                Violation(
                    line=lineno,
                    rule="response-json-outside-tabs",
                    detail=(
                        "'The API returns' is after </Tabs>. Move the response "
                        "into the matching method tab."
                    ),
                    text=stripped[:120],
                )
            )

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


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point. Returns 0 on a clean file, 1 on violations."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description="Check REST API tab style in an MDX article.")
    parser.add_argument("path", type=Path, help="Path to the article .mdx file")
    args = parser.parse_args(argv)

    if not args.path.exists():
        log.error("File not found: %s", args.path)
        return 1

    violations = lint(args.path)
    if not violations:
        log.info("OK - no API style violations in %s", args.path)
        return 0

    log.info("%s violation(s) in %s", len(violations), args.path)
    log.info("-" * 72)
    for item in violations:
        log.info("Line %4d  [%s]", item.line, item.rule)
        log.info("       %s", item.detail)
        log.info("       > %s", item.text)
        log.info("")
    return 1


if __name__ == "__main__":
    sys.exit(main())
