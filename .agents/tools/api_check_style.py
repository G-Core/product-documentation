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
_GCORE_API_KEY_CTOR = re.compile(r"Gcore\s*\(\s*api_key\s*=")
_WITH_API_KEY = re.compile(r"option\.WithAPIKey")
_CONTEXT_TODO = re.compile(r"context\.TODO\s*\(")
_COMBINED_STEP = re.compile(r"(?:#|//)\s*Step\s+\d+\s*\+\s*\d+", re.IGNORECASE)
_METHOD_SWITCH_IMPORT_BARE = re.compile(
    r"""from\s+["']/snippets/method-switch["']"""
)

_IMPORT_OS = re.compile(r"^\s*import\s+os\b")
_OS_USAGE = re.compile(r"\bos\.(?:environ|getenv)\b")
_METHOD_SWITCH_OPEN = re.compile(r"<MethodSwitch\b")
_METHOD_SWITCH_IMPORT_LINE = re.compile(
    r"""from\s+["']/snippets/method-switch(?:\.jsx)?["']"""
)
_INDENTED_METHOD_SECTION_CLOSE = re.compile(r"^\s+</MethodSection>")
_GO_IMPORT_BARE = re.compile(r'"github\.com/G-Core/gcore-go"')
_GO_IMPORT_WITH_ALIAS = re.compile(r'\bgcore\s+"github\.com/G-Core/gcore-go"')
_METHOD_SECTION_OPEN = re.compile(r"<MethodSection\b")
_METHOD_SECTION_API = re.compile(r'<MethodSection\s[^>]*id=["\']api["\']')
_METHOD_SECTION_CLOSE = re.compile(r"</MethodSection>")
_JSX_BLOCK_OPEN = re.compile(
    r"<(Info|Warning|Tip|Note|Tabs|Tab|Accordion|Frame|Steps|Step)\b"
)
_JSX_BLOCK_CLOSE = re.compile(
    r"</(Info|Warning|Tip|Note|Tabs|Tab|Accordion|Frame|Steps|Step)>"
)
_P_OPEN = re.compile(r"<p\b")
_P_CLOSE = re.compile(r"</p>")
_NUMBERED_ITEM = re.compile(r"^\d+[.\\]")
_BULLET_ITEM = re.compile(r"^[-*+]\s|^\d+\\?\.\s")

_SKIP_DIR_NAMES = frozenset(
    {
        "_drafts",
        "_planning",
        "_deprecated",
        "node_modules",
        ".git",
        "venv",
        "__pycache__",
        # Non-article directories — tools, tests, specs, components
        ".agents",
        ".cursor",
        ".playwright-mcp",
        "snippets",
        "api-reference",
    }
)


@dataclass(frozen=True)
class Violation:
    """A single checker finding."""

    line: int
    rule: str
    detail: str
    text: str


@dataclass(frozen=True)
class Warning:
    """A review signal that does not fail the build but requires human judgment."""

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


def check_forbidden_sdk_patterns(lines: Sequence[str]) -> list[Violation]:
    """Flag SDK samples that ignore client-level env vars or use TODO context.

    ``Gcore()`` / ``gcore.NewClient()`` read ``GCORE_*`` env vars. Passing
    ``api_key`` or ``option.WithAPIKey`` is redundant and drifts from the
    canonical pattern. ``context.TODO()`` is a placeholder, not production
    sample code.
    """
    violations: list[Violation] = []
    in_fence = False
    lang = ""

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            if not in_fence:
                lang = _fence_lang(raw)
                in_fence = True
            else:
                in_fence = False
                lang = ""
            continue
        if not in_fence:
            continue

        stripped = raw.strip()
        if lang in {"python", "py"} and _GCORE_API_KEY_CTOR.search(raw):
            violations.append(
                Violation(
                    line=lineno,
                    rule="sdk-gcore-api-key-ctor",
                    detail=(
                        "Gcore() reads GCORE_API_KEY. Do not pass api_key= "
                        "to the constructor."
                    ),
                    text=stripped[:120],
                )
            )
        if lang == "go":
            if _WITH_API_KEY.search(raw):
                violations.append(
                    Violation(
                        line=lineno,
                        rule="sdk-with-api-key",
                        detail=(
                            "gcore.NewClient() reads GCORE_API_KEY. Do not "
                            "pass option.WithAPIKey."
                        ),
                        text=stripped[:120],
                    )
                )
            if _CONTEXT_TODO.search(raw):
                violations.append(
                    Violation(
                        line=lineno,
                        rule="sdk-context-todo",
                        detail=(
                            "Use ctx := context.Background(), not "
                            "context.TODO()."
                        ),
                        text=stripped[:120],
                    )
                )

    return violations


def check_combined_step_labels(lines: Sequence[str]) -> list[Violation]:
    """Flag combined Quickstart step comments such as ``# Step 3+4``."""
    violations: list[Violation] = []
    in_fence = False
    lang = ""

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            if not in_fence:
                lang = _fence_lang(raw)
                in_fence = True
            else:
                in_fence = False
                lang = ""
            continue
        if not in_fence:
            continue
        if lang not in {"python", "py", "go"}:
            continue
        if not _COMBINED_STEP.search(raw):
            continue
        violations.append(
            Violation(
                line=lineno,
                rule="combined-step-label",
                detail="One logical step per comment. Never combine (# Step 3+4).",
                text=raw.strip()[:120],
            )
        )

    return violations


def check_method_switch_import(lines: Sequence[str]) -> list[Violation]:
    """Flag MethodSwitch imports that omit the ``.jsx`` extension.

    Without ``.jsx`` the MDX compiler reports OK and the page renders blank.
    """
    violations: list[Violation] = []
    in_fence = False

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not _METHOD_SWITCH_IMPORT_BARE.search(raw):
            continue
        violations.append(
            Violation(
                line=lineno,
                rule="method-switch-import",
                detail=(
                    'Import from "/snippets/method-switch.jsx", not '
                    '"/snippets/method-switch".'
                ),
                text=raw.strip()[:120],
            )
        )

    return violations


def check_content_before_method_switch(lines: Sequence[str]) -> list[Violation]:
    """Flag non-empty content between the MethodSwitch import and <MethodSwitch>.

    Everything before <MethodSwitch> is visible outside any tab and breaks the
    tab-independent page contract. All intro prose must live inside a
    <MethodSection>.
    """
    violations: list[Violation] = []
    import_seen = False
    in_fence = False

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            in_fence = not in_fence

        if not import_seen:
            if _METHOD_SWITCH_IMPORT_LINE.search(raw):
                import_seen = True
            continue

        if _METHOD_SWITCH_OPEN.search(stripped):
            break

        if in_fence or not stripped:
            continue

        violations.append(
            Violation(
                line=lineno,
                rule="content-before-method-switch",
                detail=(
                    "Content found before <MethodSwitch>. Move all intro prose "
                    "inside a <MethodSection>."
                ),
                text=stripped[:120],
            )
        )

    return violations


def check_indented_method_section_close(lines: Sequence[str]) -> list[Violation]:
    """Flag </MethodSection> tags that are not at column 0.

    An indented </MethodSection> directly after a list item is treated by the
    MDX parser as list continuation, making the tag invisible and causing a
    blank or 404 page.
    """
    violations: list[Violation] = []

    for lineno, raw in enumerate(lines, start=1):
        if _INDENTED_METHOD_SECTION_CLOSE.match(raw):
            violations.append(
                Violation(
                    line=lineno,
                    rule="indented-method-section-close",
                    detail=(
                        "</MethodSection> must be at column 0. Indented tags "
                        "after lists cause the MDX parser to ignore them."
                    ),
                    text=raw.rstrip()[:120],
                )
            )

    return violations


def check_import_os_without_usage(lines: Sequence[str]) -> list[Violation]:
    """Flag Python code blocks that import os but never use os.environ/os.getenv.

    ``import os`` is only needed when the block reads additional env vars the
    SDK does not handle automatically. Importing it without usage is a sign the
    block was copied from a template without review.
    """
    violations: list[Violation] = []
    in_fence = False
    lang = ""
    block_start = 0
    block_lines: list[str] = []

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            if not in_fence:
                lang = _fence_lang(raw)
                in_fence = True
                block_start = lineno
                block_lines = []
            else:
                if lang in {"python", "py"} and block_lines:
                    import_lineno: int | None = None
                    has_usage = False
                    for rel, bline in enumerate(block_lines):
                        if _IMPORT_OS.match(bline):
                            import_lineno = block_start + rel + 1
                        if _OS_USAGE.search(bline):
                            has_usage = True
                    if import_lineno is not None and not has_usage:
                        violations.append(
                            Violation(
                                line=import_lineno,
                                rule="import-os-without-usage",
                                detail=(
                                    "`import os` is present but os.environ / "
                                    "os.getenv is never used in this block. "
                                    "Remove the import."
                                ),
                                text="import os",
                            )
                        )
                in_fence = False
                lang = ""
                block_lines = []
            continue

        if in_fence:
            block_lines.append(raw)

    return violations


def check_go_import_alias(lines: Sequence[str]) -> list[Violation]:
    """Flag Go imports of gcore-go that are missing the ``gcore`` alias.

    The canonical import is ``gcore "github.com/G-Core/gcore-go"``.
    Without the alias the package name is the last path segment (``gcore-go``)
    which is not a valid Go identifier — the code would not compile.
    """
    violations: list[Violation] = []
    in_fence = False
    lang = ""

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            if not in_fence:
                lang = _fence_lang(raw)
                in_fence = True
            else:
                in_fence = False
                lang = ""
            continue
        if not in_fence or lang != "go":
            continue
        stripped = raw.strip()
        if _GO_IMPORT_BARE.search(stripped) and not _GO_IMPORT_WITH_ALIAS.search(stripped):
            violations.append(
                Violation(
                    line=lineno,
                    rule="go-import-missing-alias",
                    detail=(
                        'Use gcore "github.com/G-Core/gcore-go" — '
                        "the alias is required because the package name "
                        "contains a hyphen."
                    ),
                    text=stripped[:120],
                )
            )

    return violations


def check_prose_without_p_tags(lines: Sequence[str]) -> list[Violation]:
    """Flag prose paragraphs inside <MethodSection> not wrapped in <p> tags.

    Every standalone prose paragraph inside <MethodSection> must be wrapped in <p>.
    Skips: code fences, JSX block containers (Info/Tabs/Frame/etc.), numbered and
    bullet list items, headings, empty lines, and lines starting with a JSX tag.
    """
    violations: list[Violation] = []
    in_method_section = False
    in_fence = False
    in_p = False
    jsx_depth = 0

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        # Track code fences
        if _is_fence(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Track MethodSection boundaries (Portal and API both require <p> wrapping)
        if _METHOD_SECTION_OPEN.search(stripped):
            in_method_section = True
            jsx_depth = 0
            in_p = False
            continue
        if _METHOD_SECTION_CLOSE.search(stripped):
            in_method_section = False
            continue

        if not in_method_section:
            continue

        # Track <p> wrapping
        if _P_OPEN.search(stripped):
            in_p = True
        if _P_CLOSE.search(stripped):
            in_p = False
            continue
        if in_p:
            continue

        # Track JSX block depth
        opens = len(_JSX_BLOCK_OPEN.findall(stripped))
        closes = len(_JSX_BLOCK_CLOSE.findall(stripped))
        jsx_depth = max(0, jsx_depth + opens - closes)
        if opens > 0 or closes > 0:
            continue
        if jsx_depth > 0:
            continue

        # Skip empty lines
        if not stripped:
            continue

        # Skip lines starting with JSX tags, headings, import
        if stripped.startswith("<"):
            continue
        if stripped.startswith("#"):
            continue
        if _BULLET_ITEM.match(stripped):
            continue
        if stripped.startswith("import "):
            continue
        # Skip indented lines (continuation of list/step sub-items)
        if raw[0] == " " or raw[0] == "\t":
            continue
        # Skip markdown table rows and separators
        if stripped.startswith("|"):
            continue

        violations.append(
            Violation(
                line=lineno,
                rule="prose-without-p-tag",
                detail=(
                    "Prose paragraph inside <MethodSection> must be wrapped in <p> tags."
                ),
                text=stripped[:120],
            )
        )

    return violations


_METHOD_SWITCH_CLOSE = re.compile(r"</MethodSwitch>")


def warn_content_after_method_switch(lines: Sequence[str]) -> list[Warning]:
    """Warn when non-empty content follows </MethodSwitch>.

    Content after </MethodSwitch> renders on every tab in Mintlify, making it
    visible in both Portal and API tabs regardless of which is active.
    This is sometimes intentional (e.g. shared reference tables that apply to
    all methods) but sometimes wrong (e.g. portal-only embed instructions).

    Returns a Warning for human review — does not affect exit code.
    """
    warnings: list[Warning] = []
    after_close = False
    in_fence = False

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            in_fence = not in_fence
        if in_fence:
            continue

        stripped = raw.strip()
        if _METHOD_SWITCH_CLOSE.search(stripped):
            after_close = True
            continue

        if after_close and stripped:
            warnings.append(
                Warning(
                    line=lineno,
                    rule="content-after-method-switch",
                    detail=(
                        "Content after </MethodSwitch> renders on ALL tabs. "
                        "Verify it is intentional (shared reference) or move "
                        "it inside the appropriate <MethodSection>."
                    ),
                    text=stripped[:120],
                )
            )
            # Report only the first non-empty line to avoid noise
            break

    return warnings


def warn_forbidden_prose_words(lines: Sequence[str]) -> list[Warning]:
    """Warn when prose contains vague or informal words banned from technical docs.

    Flagged patterns (not a hard fail — verify context before fixing):
    - "example" / "examples" — use specific terms like "code" or "command"
    - "following" / "the following" — rephrase to direct phrasing
      e.g. "Set these variables:" not "Set the following variables:"

    Words inside fenced code blocks and frontmatter are ignored.
    """
    warnings: list[Warning] = []
    in_fence = False
    in_frontmatter = False
    frontmatter_done = False

    _forbidden = re.compile(
        r"\b(example[s]?|the following|following)\b",
        re.IGNORECASE,
    )

    for lineno, raw in enumerate(lines, start=1):
        # Skip frontmatter
        if lineno == 1 and raw.strip() == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if raw.strip() == "---":
                in_frontmatter = False
                frontmatter_done = True
            continue

        if _is_fence(raw):
            in_fence = not in_fence

        if in_fence:
            continue

        # Skip pure MDX/JSX tags (but NOT <p> prose lines), imports, and code-block annotations
        stripped = raw.strip()
        if (stripped.startswith("<") and not stripped.startswith("<p>")) or stripped.startswith("import "):
            continue

        for match in _forbidden.finditer(raw):
            warnings.append(
                Warning(
                    line=lineno,
                    rule="forbidden-prose-word",
                    detail=(
                        f"Banned word \"{match.group(0)}\" in prose. "
                        "Use direct phrasing: \"Open a terminal and export the required variables:\" "
                        "not \"Set the following variables before running the examples:\". "
                        "Verify context — false positives are possible."
                    ),
                    text=stripped[:120],
                )
            )
            # One warning per line is enough
            break

    return warnings


def warn_real_id_in_response(lines: Sequence[str]) -> list[Warning]:
    """Warn when a JSON response block contains a large numeric ID value.

    IDs with 6 or more digits in JSON response examples are likely real database
    records rather than placeholder values. Use small, clearly fictional IDs like
    42, 123, or 1001 in documentation response examples.

    Only inspects ``json`` fenced code blocks.
    """
    warnings: list[Warning] = []
    in_fence = False
    lang = ""

    # Match any field whose name ends in "id" (e.g. "id", "video_id", "stream_id")
    _large_id = re.compile(r'"(?:\w+_)?id":\s*(\d{7,})', re.IGNORECASE)

    for lineno, raw in enumerate(lines, start=1):
        if _is_fence(raw):
            if not in_fence:
                lang = _fence_lang(raw)
                in_fence = True
            else:
                in_fence = False
                lang = ""
            continue

        if not in_fence or lang != "json":
            continue

        match = _large_id.search(raw)
        if match:
            warnings.append(
                Warning(
                    line=lineno,
                    rule="real-id-in-response",
                    detail=(
                        f"Large numeric ID ({match.group(1)}) in JSON response "
                        "looks like real data. Use a small placeholder: 42, 123, 1001."
                    ),
                    text=raw.strip()[:120],
                )
            )

    return warnings


WARN_CHECKS: tuple[Callable[[list[str]], list[Warning]], ...] = (
    warn_content_after_method_switch,
    warn_forbidden_prose_words,
    warn_real_id_in_response,
)


def check_api_section_no_info_block(lines: Sequence[str]) -> list[Violation]:
    """Flag an API MethodSection that is missing an <Info> authentication block.

    Every REST API MethodSection must open with an <Info> block that states
    the API token requirement. Prose authentication sentences are not allowed —
    the <Info> component provides consistent visual treatment across all articles.
    """
    violations: list[Violation] = []
    in_api_section = False
    in_fence = False
    depth = 0
    section_start_line = 0
    has_info = False

    _api_open = re.compile(r'<MethodSection\b[^>]*\bid=["\']api["\']')
    _any_section_open = re.compile(r'<MethodSection\b')
    _section_close = re.compile(r'</MethodSection\s*>')
    _info_open = re.compile(r'<Info\b')

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            in_fence = not in_fence

        if in_fence:
            continue

        if _api_open.search(stripped):
            in_api_section = True
            depth = 1
            section_start_line = lineno
            has_info = False
            continue

        if in_api_section:
            if _any_section_open.search(stripped):
                depth += 1
            if _section_close.search(stripped):
                depth -= 1
                if depth <= 0:
                    if not has_info:
                        violations.append(
                            Violation(
                                line=section_start_line,
                                rule="api-section-no-info-block",
                                detail=(
                                    "API MethodSection is missing an <Info> authentication block. "
                                    "Add <Info>An [API&nbsp;token](/account-settings/api-tokens) "
                                    "is required...</Info> at the top of the section."
                                ),
                                text='<MethodSection id="api">',
                            )
                        )
                    in_api_section = False
                continue

            if _info_open.search(stripped):
                has_info = True

    return violations


def check_portal_section_no_headings(lines: Sequence[str]) -> list[Violation]:
    """Flag a Portal MethodSection that contains no ## or ### headings.

    A Portal section without headings produces an empty 'On this page' TOC
    when the user is on the Customer Portal tab. Every Portal MethodSection
    must have at least one ## or ### heading so navigation is usable.
    """
    violations: list[Violation] = []
    in_portal_section = False
    in_fence = False
    depth = 0
    section_start_line = 0
    has_heading = False

    _portal_open = re.compile(r'<MethodSection\b[^>]*\bid=["\']portal["\']')
    _any_section_open = re.compile(r'<MethodSection\b')
    _section_close = re.compile(r'</MethodSection\s*>')
    _heading = re.compile(r'^#{2,3}\s')

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            in_fence = not in_fence

        if in_fence:
            continue

        if _portal_open.search(stripped):
            in_portal_section = True
            depth = 1
            section_start_line = lineno
            has_heading = False
            continue

        if in_portal_section:
            if _any_section_open.search(stripped):
                depth += 1
            if _section_close.search(stripped):
                depth -= 1
                if depth <= 0:
                    if not has_heading:
                        violations.append(
                            Violation(
                                line=section_start_line,
                                rule="portal-section-no-headings",
                                detail=(
                                    "Portal MethodSection has no ## or ### headings. "
                                    "Add at least one heading so the 'On this page' TOC "
                                    "is populated when the user is on the Customer Portal tab."
                                ),
                                text="<MethodSection id=\"portal\">",
                            )
                        )
                    in_portal_section = False
                continue

            if _heading.match(stripped):
                has_heading = True

    return violations


_ESCAPED_NUMBERED_ITEM = re.compile(r"^\d+\\\.\s")


def check_escaped_numbered_items(lines: Sequence[str]) -> list[Violation]:
    r"""Flag backslash-escaped numbered list items inside <MethodSection>.

    Inside <MethodSection>, `1\. text` is treated as plain text by the MDX
    compiler -- blank lines between items are stripped, so all items merge into
    one block. Use `1. text` (no backslash) instead, which compiles to a proper
    <ol><li> element.

    Skips code fences.
    """
    violations: list[Violation] = []
    in_method_section = False
    in_fence = False

    for lineno, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if _is_fence(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if _METHOD_SECTION_OPEN.search(stripped):
            in_method_section = True
            continue
        if _METHOD_SECTION_CLOSE.search(stripped):
            in_method_section = False
            continue

        if not in_method_section:
            continue

        if _ESCAPED_NUMBERED_ITEM.match(stripped):
            violations.append(
                Violation(
                    line=lineno,
                    rule="escaped-numbered-item",
                    detail=(
                        r"Backslash-escaped `N\. text` inside <MethodSection> renders as plain text "
                        "and merges with adjacent content. Use `N. text` (no backslash) instead."
                    ),
                    text=stripped[:80],
                )
            )

    return violations


CHECKS: tuple[CheckFn, ...] = (
    check_response_outside_tabs,
    check_forbidden_sdk_patterns,
    check_combined_step_labels,
    check_method_switch_import,
    check_content_before_method_switch,
    check_indented_method_section_close,
    check_import_os_without_usage,
    check_go_import_alias,
    check_prose_without_p_tags,
    check_escaped_numbered_items,
    check_api_section_no_info_block,
    check_portal_section_no_headings,
)


def lint(path: Path) -> list[Violation]:
    """Run every registered API style check against one MDX file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    violations: list[Violation] = []
    for check in CHECKS:
        violations.extend(check(lines))
    violations.sort(key=lambda item: item.line)
    return violations


def warn(path: Path) -> list[Warning]:
    """Run every registered warning check against one MDX file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    warnings: list[Warning] = []
    for check in WARN_CHECKS:
        warnings.extend(check(lines))
    warnings.sort(key=lambda item: item.line)
    return warnings


def iter_mdx_files(root: Path) -> list[Path]:
    """Return article MDX files under root, skipping draft, vendor, and tool dirs.

    Skips:
    - Directories named in _SKIP_DIR_NAMES (node_modules, _drafts, snippets, etc.)
    - Any directory whose name starts with '.' (dotdirs: .git, .agents, .cursor, etc.)
    """
    found: list[Path] = []
    for path in root.rglob("*.mdx"):
        parts = path.parts
        if any(part in _SKIP_DIR_NAMES or part.startswith(".") for part in parts):
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
    total_warns = 0
    for path in paths:
        found = lint(path)
        found_warns = warn(path)
        if not found and not found_warns:
            continue
        if found:
            dirty += 1
            total_hits += len(found)
            log.info("=== %s (%s) ===", path, len(found))
            for item in found:
                log.info("  L%s [%s] %s", item.line, item.rule, item.text)
            log.info("")
        if found_warns:
            total_warns += len(found_warns)
            if not found:
                log.info("=== %s ===", path)
            for item in found_warns:
                log.info("  L%s [WARN:%s] %s", item.line, item.rule, item.text)
            if not found:
                log.info("")

    if args.all:
        log.info("Scanned %s mdx files, %s with violations (%s hits), %s warnings",
                 len(paths), dirty, total_hits, total_warns)
        return 1 if dirty else 0

    if total_hits == 0 and total_warns == 0:
        log.info("OK - no API style violations in %s", paths[0])
        return 0
    if total_hits == 0 and total_warns > 0:
        log.info("OK - no violations, %s warning(s) in %s (review required)", total_warns, paths[0])
        return 0

    log.info("%s violation(s) in %s", total_hits, paths[0])
    return 1


if __name__ == "__main__":
    sys.exit(main())
