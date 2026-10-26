"""Style guide linter for Gcore product documentation MDX files.

Checks detectable violations from .agents/references/style-guide.md.
Usage: python .agents/tools/style_check.py hosting/path/to/article.mdx

Landing pages (see .claude/skills/technical-landing-pages/references/landing-writing.md):
the checker still flags three things on a landing, and the flags are intentional.
The output marks them as a possible false positive. Show them to the user, who decides
which to fix. Do not ignore them and do not fix them on your own, because the user
may have allowed one on purpose:
  - "you" / "your" (check_you_your): allowed on a landing in small doses.
  - "For example," at the start of a sentence (check_forbidden_words): allowed.
  - a digit inside a JSX attribute such as cols={2} (check_numbers): a false positive.
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


@dataclass
class Violation:
    line: int
    rule: str
    detail: str
    text: str


def strip_skipped_regions(lines: list[str]) -> list[tuple[int, str]]:
    """Return (lineno, text) pairs with frontmatter and code blocks zeroed out."""
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
    """Remove URLs and link targets to avoid false matches inside them."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"https?://\S+", "", text)
    return text


def check_you_your(lines: list[tuple[int, str]]) -> list[Violation]:
    # On a landing page a measured use of "you" can be intentional. Check with the user, do not auto-fix.
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
        # A sentence-initial "For example," on a landing is intentional. Check with the user, do not auto-fix.
        (r"\bfor example\b", "for example (inline) — restructure the sentence or use a dash"),
        (r"\bsuch as\b", "such as — complete the list or restructure"),
        (r"\bpermanent (api token|token)\b", "permanent API token — tokens have optional expiry, use 'API token'"),
        (r"\bwhitelist\b", "whitelist — use 'allowlist'"),
        (r"\bblacklist\b", "blacklist — use 'blocklist'"),
        (r"\bclick on\b", "click on — use 'click'"),
        (r"\bgo to\b", "go to — use 'navigate to'"),
        (r"\btype in\b", "type in — use 'enter'"),
        # Only the UI action is flagged. "Choose between two types" is a decision in prose and stays.
        (r"\bchoose\s+(?:the\s+|an?\s+)?(?:\*\*|[\"“`])", "choose before an interface label — use 'select'"),
        (r"\blog\s+into\b", "log into — use 'log in to' (three words, not two)"),
        (r"\bno spend\b", "draft note — delete it. State the current product, not an empty account"),
        (r"\bno expenses\b", "draft note — delete it. State the current product, not an empty account"),
        (r"\bno data yet\b", "draft note — delete it. State the current product"),
        (r"\bnothing to show\b", "draft note — delete it. State the current product"),
        (r"\bempty chart\b", "draft note — delete it. Name the controls on the screen"),
        (r"\bwill appear later\b", "draft note — delete it. Do not promise a later update"),
        (r"\bcoming soon\b", "draft note — delete it. Do not promise a later update"),
        (r"\bto be updated\b", "draft note — delete it. Do not promise a later update"),
        (r"\bdeveloper promised\b", "draft note — delete it. Do not write process notes"),
        (r"\bwaiting for a screenshot\b", "draft note — delete it. Do not write process notes"),
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


def check_bullet_label_dash(lines: list[tuple[int, str]]) -> list[Violation]:
    """Flag a bullet that names a term and then describes it with a dash.

    Style guide, "Bold labels in bullets": use a colon. Link-list glosses
    ("- [Name](/path) — description") are a different pattern and stay dashes.
    """
    violations: list[Violation] = []
    pattern = re.compile(
        r"^\s*[-*+]\s+"
        r"(?!\[[^\]]+\]\([^)]+\))"
        r"(?:\*\*[^*]+\*\*|`[^`]+`|\w[\w .+/()-]{0,40}?)"
        r"\s+[—–]\s+\S"
    )
    for lineno, text in lines:
        if pattern.search(text):
            violations.append(Violation(
                line=lineno,
                rule="Bullet label punctuation",
                detail="Bullet names a term and then uses a dash. Use a colon: '- **Term**: description'",
                text=text.strip(),
            ))
    return violations


def check_link_text(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    link_pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
    banned_routing_verbs = re.compile(
        r"\b(see|refer to|learn more|for more details|for details|read the|check the|open the|use the)\b",
        re.IGNORECASE,
    )
    for lineno, text in lines:
        for m in link_pattern.finditer(text):
            link_text = m.group(1)
            href = m.group(2)

            words = link_text.replace("&nbsp;", " ").split()
            is_portal_link = link_text.strip() == "Gcore Customer Portal"
            if len(words) > 3 and not is_portal_link:
                violations.append(Violation(
                    line=lineno,
                    rule="Link text length",
                    detail=f"Link text '{link_text}' is {len(words)} words — max 3 words",
                    text=text.strip(),
                ))

            if 2 <= len(words) <= 3 and "&nbsp;" not in link_text and not link_text.startswith("Gcore Customer Portal"):
                violations.append(Violation(
                    line=lineno,
                    rule="Link &nbsp;",
                    detail=f"Multi-word link '[{link_text}]' missing &nbsp; between words",
                    text=text.strip(),
                ))

            sentence_before = text[:m.start()].strip()
            if banned_routing_verbs.search(sentence_before):
                violations.append(Violation(
                    line=lineno,
                    rule="Banned link pattern",
                    detail=f"Link sentence uses banned routing verb before '[{link_text}]'",
                    text=text.strip(),
                ))

            try:
                parsed = urlparse(href)
                if parsed.netloc == "docs.gcore.com":
                    violations.append(Violation(
                        line=lineno,
                        rule="Internal link must be root-relative",
                        detail=f"Link '{href}' must be root-relative (start with '/'), not a full docs.gcore.com URL",
                        text=text.strip(),
                    ))
                if href.startswith("../") or href.startswith("./"):
                    violations.append(Violation(
                        line=lineno,
                        rule="Relative link path",
                        detail=f"Link '{href}' uses relative path — use root-relative path starting with '/'",
                        text=text.strip(),
                    ))
            except ValueError:
                pass
    return violations


def check_meta_preamble(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    patterns = [
        r"this (guide|article|document|tutorial|section|page) (covers|explains|describes|walks|shows)",
        r"in this (guide|article|document|section|page)", r"here you will find",
        r"the sections below", r"below you (will|can) find",
        r"the following (guide|article|document|tutorial) (covers|explains|describes)",
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
    # A digit inside a JSX attribute (cols={2}) is a false positive. Confirm with the user, do not rewrite the markup.
    violations: list[Violation] = []
    measurement_units = re.compile(
        r"\d+\s*(ms|s|sec|seconds?|min|minutes?|hours?|days?|GB|MB|KB|TB|Gbps|Mbps|vCPU|rpm|"
        r"px|em|rem|%|cores?|nodes?|instances?|MB/s|KB/s)\b",
        re.IGNORECASE,
    )
    skip_context = re.compile(
        r"IPv[46]|step\s+\d|v\d|\d\.|port\s+\d|\d{1,3}\.\d{1,3}|"
        r"\d\s+to\s+\d|\d+\s*(to|[-\u2013])\s*\d+|[-\u2013]\d+\b|\(\d+|"
        r"\blayer\s*\d\b|\bL\d\b|[A-Za-z]+/\d",
        re.IGNORECASE,
    )
    digit_word = re.compile(r"\b([1-9])\b")
    inline_code = re.compile(r"`[^`\n]+`")
    for lineno, text in lines:
        clean = strip_urls_and_links(text)
        clean = inline_code.sub("", clean)
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


def check_alt_text(lines: list[tuple[int, str]]) -> list[Violation]:
    violations: list[Violation] = []
    img_pattern = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
    bad_starts = re.compile(r"^(screenshot of|image of|a picture of|a screenshot|picture of)", re.IGNORECASE)
    for lineno, text in lines:
        for m in img_pattern.finditer(text):
            alt = m.group(1).strip()
            if not alt:
                violations.append(Violation(
                    line=lineno,
                    rule="Alt text missing",
                    detail="Image has no alt text — add a descriptive sentence (max 125 chars)",
                    text=text.strip(),
                ))
                continue
            if len(alt) > 125:
                violations.append(Violation(
                    line=lineno,
                    rule="Alt text length",
                    detail=f"Alt text is {len(alt)} chars — max 125 chars",
                    text=text.strip(),
                ))
            if bad_starts.match(alt):
                violations.append(Violation(
                    line=lineno,
                    rule="Alt text content",
                    detail=f"Alt text must not start with '{alt.split()[0:3]}' — describe what is shown, not that it is a screenshot",
                    text=text.strip(),
                ))
    return violations


def check_opening_heading(raw_lines: list[str]) -> list[Violation]:
    """Article body must open with a prose paragraph, not a heading.

    The title: field renders as the page H1. A ## heading immediately after
    the frontmatter creates two headings in a row with no context for the reader.
    """
    violations: list[Violation] = []
    in_frontmatter = False
    frontmatter_closed = False
    fence_count = 0

    for i, raw in enumerate(raw_lines, start=1):
        stripped = raw.strip()
        if i == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
                frontmatter_closed = True
            continue
        if not frontmatter_closed:
            continue
        if stripped == "":
            continue
        if stripped.startswith("import ") or stripped.startswith("<"):
            continue
        if stripped.startswith("##"):
            violations.append(Violation(
                line=i,
                rule="Opening heading",
                detail="Article body opens with a heading — add an intro paragraph before the first ## heading",
                text=raw.strip(),
            ))
        elif re.match(
            r"^The\s+\S+(?:\s+\S+){0,8}\s+(monitors|provides|enables|supports)\b",
            stripped,
            re.IGNORECASE,
        ):
            violations.append(Violation(
                line=i,
                rule="Intro opens on the component",
                detail="Intro starts with the component and a capability verb (monitors, provides, enables, supports). State what the reader can do. Do not open with a command. See intro-writing.md",
                text=raw.strip(),
            ))
        break

    return violations


def check_heading_style(raw_lines: list[str]) -> list[Violation]:
    violations: list[Violation] = []
    forbidden_starts = re.compile(
        r"^#{2,3}\s+(what|how|why|when|to\s+\w+)\b",
        re.IGNORECASE,
    )
    forbidden_sections = {
        "next steps", "get started", "prerequisites", "requirements",
        "related documentation", "see also", "what's next",
        "key benefits", "benefits", "overview",
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


def check_callout_prefix(raw_lines: list[str]) -> list[Violation]:
    violations: list[Violation] = []
    callout_open = re.compile(r"^<(Note|Warning|Info|Tip)>", re.IGNORECASE)
    callout_close = re.compile(r"^</(Note|Warning|Info|Tip)>", re.IGNORECASE)
    prefix_pattern = re.compile(r"^\*\*(Note|Warning|Info|Tip)\*\*", re.IGNORECASE)
    inside: str | None = None
    for i, raw in enumerate(raw_lines, start=1):
        stripped = raw.strip()
        if m_open := callout_open.match(stripped):
            inside = m_open.group(1)
            continue
        if callout_close.match(stripped):
            inside = None
            continue
        if inside and prefix_pattern.match(stripped):
            violations.append(Violation(
                line=i,
                rule="Callout prefix",
                detail=f"Remove '**{inside}**' prefix inside <{inside}> — the component already renders the label",
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
        if not in_fm:
            continue

        if re.match(r"^ai-navigation\s*:", stripped):
            violations.append(Violation(
                line=i,
                rule="Frontmatter",
                detail="'ai-navigation:' was renamed to 'description:'",
                text=raw.strip(),
            ))

        if re.match(r"^description\s*:", stripped):
            value = stripped.split(":", 1)[1].strip()

            if value.startswith('"') or value.startswith("'"):
                violations.append(Violation(
                    line=i,
                    rule="description quotes",
                    detail="description value must not be wrapped in YAML quotes",
                    text=raw.strip(),
                ))

            val = value.strip("\"'")

            if ":" in val:
                violations.append(Violation(
                    line=i,
                    rule="description syntax",
                    detail="description must not contain ':' — YAML treats it as a key separator",
                    text=raw.strip(),
                ))
            if "#" in val:
                violations.append(Violation(
                    line=i,
                    rule="description syntax",
                    detail="description must not contain '#' — YAML treats it as a comment start",
                    text=raw.strip(),
                ))
            for ch in ["/", "{", "}"]:
                if ch in val:
                    violations.append(Violation(
                        line=i,
                        rule="description syntax",
                        detail=f"description must not contain '{ch}' — use descriptive text without URL paths or template variables",
                        text=raw.strip(),
                    ))

            if "\u2014" in val:
                violations.append(Violation(
                    line=i,
                    rule="description em-dash",
                    detail="description must not contain em-dash '\u2014' — llms.txt generator encodes it as garbage; use a comma or semicolon instead",
                    text=raw.strip(),
                ))

            if len(val) > 160:
                violations.append(Violation(
                    line=i,
                    rule="description length",
                    detail=f"description is {len(val)} chars — maximum 160",
                    text=raw.strip(),
                ))

            if re.search(r"\b(portal|api|terraform)\b", val, re.IGNORECASE):
                violations.append(Violation(
                    line=i,
                    rule="description search summary",
                    detail="description must summarize the article for search and must not name Portal, API, or Terraform",
                    text=raw.strip(),
                ))

    return violations


CHECKERS = [
    check_you_your, check_forbidden_words, check_uk_spelling, check_em_dash,
    check_bullet_label_dash,
    check_link_text, check_meta_preamble, check_numbers, check_alt_text,
]


LANDING_NOTE = (
    " | possible false positive on a landing page: show it to the user, "
    "who decides whether to fix it. Do not ignore it and do not fix it on your own"
)


def is_landing(path: Path) -> bool:
    """A landing is a root-level page (cdn.mdx) or a top-level api-reference page."""
    repo_root = Path(__file__).resolve().parents[2]
    try:
        parts = path.resolve().relative_to(repo_root).parts
    except ValueError:
        return False
    return len(parts) == 1 or (parts[0] == "api-reference" and len(parts) == 2)


def is_landing_review_flag(v: Violation) -> bool:
    if v.rule == "No you/your":
        return True
    if v.rule == "Forbidden word/phrase" and v.detail.startswith("for example"):
        return True
    return v.rule == "Number style" and v.text.lstrip().startswith("<")


def lint(path: Path) -> list[Violation]:
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    filtered = strip_skipped_regions(raw_lines)
    violations: list[Violation] = []
    for checker in CHECKERS:
        violations.extend(checker(filtered))
    violations.extend(check_opening_heading(raw_lines))
    violations.extend(check_heading_style(raw_lines))
    violations.extend(check_callout_prefix(raw_lines))
    violations.extend(check_frontmatter(raw_lines))
    violations.sort(key=lambda v: v.line)
    if is_landing(path):
        for v in violations:
            if is_landing_review_flag(v):
                v.detail += LANDING_NOTE
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
