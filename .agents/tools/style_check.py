"""
Style guide linter for Gcore product documentation MDX files.

Checks detectable violations from .agents/references/style-guide.md.
Skips frontmatter, code blocks, and image alt text where rules do not apply.

Usage:
    python scripts/style_check.py <path/to/article.mdx>
    python scripts/style_check.py hosting/virtual-servers/order-a-virtual-server.mdx
"""

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable


@dataclass
class Violation:
    line: int
    rule: str
    detail: str
    text: str


def strip_skipped_regions(lines: list[str]) -> list[tuple[int, str]]:
    """
    Return (line_number, line_text) pairs with code blocks zeroed out.
    Frontmatter (between --- markers) is also excluded.
    Line numbers are 1-based and preserved for accurate reporting.
    """
    result: list[tuple[int, str]] = []
    in_frontmatter = False
    in_code_block = False
    frontmatter_done = False

    for i, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        if not frontmatter_done:
            if i == 1 and stripped == "---":
                in_frontmatter = True
                result.append((i, ""))
                continue
            if in_frontmatter:
                if stripped == "---":
                    in_frontmatter = False
                    frontmatter_done = True
                result.append((i, ""))
                continue

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append((i, ""))
            continue

        if in_code_block:
            result.append((i, ""))
            continue

        result.append((i, raw))

    return result


def strip_urls_and_links(text: str) -> str:
    """Remove URLs and link targets so checkers don't match inside them."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def check_you_your(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    pattern = re.compile(r"\b(you|your|you're|you'll|you've)\b", re.IGNORECASE)
    for lineno, text in lines:
        clean = strip_urls_and_links(text)
        for m in pattern.finditer(clean):
            violations.append(Violation(
                line=lineno,
                rule="No you/your",
                detail=f"Found '{m.group()}' — rephrase to imperative or neutral",
                text=text.strip(),
            ))
    return violations


def check_forbidden_words(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    forbidden: list[tuple[str, str]] = [
        (r"\bplatform\b", "platform — use 'Gcore', 'Gcore Customer Portal', or specific service name"),
        (r"\bensure\b", "ensure — use 'verify', 'check', or 'confirm'"),
        (r"\bmaking sure\b", "make sure — use 'verify', 'check', or 'confirm'"),
        (r"\bmake sure\b", "make sure — use 'verify', 'check', or 'confirm'"),
        (r"\bbe sure\b", "be sure — use 'verify', 'check', or 'confirm'"),
        (r"\bsimply\b", "simply — remove entirely"),
        (r"\bjust\b", "just — remove entirely"),
        (r"\bobviously\b", "obviously — remove entirely"),
        (r"\bclearly\b", "clearly — remove entirely"),
        (r"\betc\.", "etc. — complete the list explicitly"),
        (r"\band so on\b", "and so on — complete the list explicitly"),
        (r"\bleverage\b", "leverage — use 'use'"),
        (r"\butilize\b", "utilize — use 'use'"),
        (r"\bseamlessly\b", "seamlessly — say what it actually does"),
        (r"\brobust\b", "robust — say what it actually does"),
        (r"\bscalable\b", "scalable — say what it actually does"),
        (r"\bprogrammatic access\b", "programmatic access — be specific"),
        (r"\bfor example\b", "for example (inline) — restructure the sentence or use a dash"),
        (r"\bsuch as\b", "such as — complete the list or restructure"),
        (r"\bpermanent (api token|token)\b", "permanent API token — tokens have optional expiry, use 'API token'"),
        (r"\bwhitelist\b", "whitelist — use 'allowlist'"),
        (r"\bblacklist\b", "blacklist — use 'blocklist'"),
        (r"\bclick on\b", "click on — use 'click'"),
        (r"\bgo to\b", "go to — use 'navigate to'"),
        (r"\btype in\b", "type in — use 'enter'"),
        (r"\bchoose\b", "choose — use 'select'"),
    ]
    for lineno, text in lines:
        clean = strip_urls_and_links(text)
        for pattern, message in forbidden:
            for m in re.finditer(pattern, clean, re.IGNORECASE):
                violations.append(Violation(
                    line=lineno,
                    rule="Forbidden word/phrase",
                    detail=message,
                    text=text.strip(),
                ))
    return violations



def check_uk_spelling(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    uk_words = {
        r"\bbehaviour\b": "behaviour → behavior",
        r"\bcolour\b": "colour → color",
        r"\bcentre\b": "centre → center",
        r"\borganise\b": "organise → organize",
        r"\brecognise\b": "recognise → recognize",
        r"\banalogue\b": "analogue → analog",
        r"\blabour\b": "labour → labor",
    }
    for lineno, text in lines:
        for pattern, message in uk_words.items():
            if re.search(pattern, text, re.IGNORECASE):
                violations.append(Violation(
                    line=lineno,
                    rule="UK spelling",
                    detail=message,
                    text=text.strip(),
                ))
    return violations


def check_em_dash(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    pattern = re.compile(r"(?<! )—|—(?! )")
    for lineno, text in lines:
        for m in pattern.finditer(text):
            violations.append(Violation(
                line=lineno,
                rule="Em-dash spacing",
                detail="Unspaced em-dash — must be ' — ' (space before and after)",
                text=text.strip(),
            ))
    return violations


def check_link_text(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    link_pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
    banned_starts = [
        "for more details", "see ", "learn more", "for details",
        "refer to", "use the ", "open the ", "read the ", "check the ",
    ]
    for lineno, text in lines:
        for m in link_pattern.finditer(text):
            link_text = m.group(1)
            href = m.group(2)

            words = link_text.replace("&nbsp;", " ").split()
            if len(words) > 2:
                violations.append(Violation(
                    line=lineno,
                    rule="Link text length",
                    detail=f"Link text '{link_text}' is {len(words)} words — max 2 words",
                    text=text.strip(),
                ))

            if len(words) == 2 and "&nbsp;" not in link_text and not link_text.startswith("Gcore Customer Portal"):
                violations.append(Violation(
                    line=lineno,
                    rule="Link &nbsp;",
                    detail=f"Multi-word link '[{link_text}]' missing &nbsp; between words",
                    text=text.strip(),
                ))

            sentence_before = text[:m.start()].strip().lower()
            for banned in banned_starts:
                if sentence_before.endswith(banned.rstrip()):
                    violations.append(Violation(
                        line=lineno,
                        rule="Banned link pattern",
                        detail=f"Link sentence uses banned routing verb before '[{link_text}]'",
                        text=text.strip(),
                    ))

            if href.startswith("https://docs.gcore.com"):
                violations.append(Violation(
                    line=lineno,
                    rule="Internal link must be root-relative",
                    detail=f"Link '{href}' must start with '/' not 'https://docs.gcore.com'",
                    text=text.strip(),
                ))
    return violations


def check_meta_preamble(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    patterns = [
        r"this (guide|article|document|tutorial|section) (covers|explains|describes|walks)",
        r"in this (guide|article|document|section)",
        r"here you will find",
        r"the sections below",
    ]
    combined = re.compile("|".join(patterns), re.IGNORECASE)
    for lineno, text in lines:
        if combined.search(text):
            violations.append(Violation(
                line=lineno,
                rule="Meta-preamble opener",
                detail="Article must not open with self-describing sentence",
                text=text.strip(),
            ))
    return violations


def check_numbers(lines: list[tuple[int, str]]) -> list[Violation]:
    """Flag digit 1-9 where a word is likely expected (non-measurement context)."""
    violations: list[Violation] = []
    measurement_units = re.compile(
        r"\d+\s*(ms|s|min|minutes?|hours?|days?|GB|MB|KB|TB|Gbps|Mbps|vCPU|rpm|"
        r"px|em|rem|%|cores?|nodes?|instances?|MB/s|KB/s)\b",
        re.IGNORECASE,
    )
    skip_context = re.compile(
        r"IPv[46]|step\s+\d|v\d|\d\.|"
        r"\d\s+to\s+\d|"
        r"1\s*(to|-)\s*\d|"
        r"\d+\s*(to|-)\s*\d+|"
        r"port\s+\d|"
        r"\d{1,3}\.\d{1,3}",
        re.IGNORECASE,
    )
    digit_word = re.compile(r"\b([1-9])\b")
    for lineno, text in lines:
        clean = strip_urls_and_links(text)
        for m in digit_word.finditer(clean):
            start = m.start()
            surrounding = clean[max(0, start - 15):start + 25]
            if not measurement_units.search(surrounding) and not skip_context.search(surrounding):
                violations.append(Violation(
                    line=lineno,
                    rule="Number style",
                    detail=f"Digit '{m.group()}' in body text — spell out one through nine unless it's a measurement, limit, or version",
                    text=text.strip(),
                ))
    return violations


def check_heading_style(raw_lines: list[str]) -> list[Violation]:
    """Check ## and ### headings for forbidden patterns."""
    violations: list[Violation] = []
    forbidden_starts = re.compile(
        r"^#{2,3}\s+(what|how|why|when|to\s+\w+)\b",
        re.IGNORECASE,
    )
    forbidden_sections = {
        "next steps", "get started", "prerequisites", "requirements",
        "related documentation", "see also", "what's next",
    }
    heading = re.compile(r"^(#{2,3})\s+(.+)")
    for i, raw in enumerate(raw_lines, start=1):
        m = heading.match(raw.strip())
        if not m:
            continue
        title = m.group(2).strip().lower()
        if title in forbidden_sections:
            violations.append(Violation(
                line=i,
                rule="Forbidden section",
                detail=f"Heading '## {m.group(2).strip()}' is forbidden",
                text=raw.strip(),
            ))
        if forbidden_starts.match(raw.strip()):
            violations.append(Violation(
                line=i,
                rule="Heading pattern",
                detail=f"Heading starts with forbidden word (What/How/Why/When/To+verb)",
                text=raw.strip(),
            ))
        words = m.group(2).strip().split()
        if len(words) > 8:
            violations.append(Violation(
                line=i,
                rule="Heading length",
                detail=f"Heading is {len(words)} words — max 8 words",
                text=raw.strip(),
            ))
    return violations


def check_frontmatter(raw_lines: list[str]) -> list[Violation]:
    violations: list[Violation] = []
    in_fm = False
    for i, raw in enumerate(raw_lines, start=1):
        stripped = raw.strip()
        if i == 1 and stripped == "---":
            in_fm = True
            continue
        if in_fm and stripped == "---":
            break
        if in_fm:
            if re.match(r"^description\s*:", stripped, re.IGNORECASE):
                violations.append(Violation(
                    line=i,
                    rule="Frontmatter",
                    detail="'description:' is forbidden — use 'ai-navigation:' instead",
                    text=raw.strip(),
                ))
            if re.match(r"^ai-navigation\s*:", stripped):
                value = stripped.split(":", 1)[1].strip()
                if ":" in value or "#" in value:
                    violations.append(Violation(
                        line=i,
                        rule="ai-navigation syntax",
                        detail="ai-navigation must not contain ':' or '#'",
                        text=raw.strip(),
                    ))
    return violations


CHECKERS: list[Callable] = [
    check_you_your,
    check_forbidden_words,
    check_uk_spelling,
    check_em_dash,
    check_link_text,
    check_meta_preamble,
    check_numbers,
]


def lint(path: Path) -> list[Violation]:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    filtered = strip_skipped_regions(raw_lines)
    violations: list[Violation] = []
    for checker in CHECKERS:
        violations.extend(checker(filtered))
    violations.extend(check_heading_style(raw_lines))
    violations.extend(check_frontmatter(raw_lines))
    violations.sort(key=lambda v: v.line)
    return violations


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/style_check.py <path/to/article.mdx>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    violations = lint(path)

    if not violations:
        print(f"OK — no violations found in {path}")
        return

    print(f"\n{len(violations)} violation(s) in {path}\n")
    print("-" * 72)
    for v in violations:
        print(f"Line {v.line:>4}  [{v.rule}]")
        print(f"       {v.detail}")
        print(f"       > {v.text[:120]}")
        print()


if __name__ == "__main__":
    main()
