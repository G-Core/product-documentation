#!/usr/bin/env python3
"""
afterFileEdit hook: sanitize MDX description fields.

Runs after any Write/TabWrite to an .mdx file.
- Strips non-ASCII invisible/control characters from the description: line.
- Normalizes line endings to LF.
"""
import json
import re
import sys
import unicodedata

FORBIDDEN_CATEGORIES = {"Zs", "Cf", "Cc", "Zl", "Zp"}
# Unicode category Zs = space separators (non-breaking space etc.)
# Cf = format chars (zero-width space, soft hyphen etc.)
# Cc = control chars
# Zl/Zp = line/paragraph separators


def sanitize_description(value: str) -> str:
    result = []
    for ch in value:
        if ord(ch) < 128:
            result.append(ch)
        elif unicodedata.category(ch) in FORBIDDEN_CATEGORIES:
            result.append(" ")
        else:
            result.append(ch)
    # Collapse multiple spaces
    return re.sub(r"  +", " ", "".join(result)).rstrip()


def process(file_path: str) -> None:
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return

    def fix_desc(m: re.Match) -> str:
        prefix = m.group(1)
        value = m.group(2)
        clean = sanitize_description(value)
        return f"{prefix}{clean}"

    new_content = re.sub(
        r"^(description:\s*)(.+)$",
        fix_desc,
        content,
        flags=re.MULTILINE,
    )
    # Normalize line endings to LF
    new_content = new_content.replace("\r\n", "\n").replace("\r", "\n")

    if new_content != content:
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)


def main() -> None:
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)

    path = data.get("path") or data.get("file_path") or ""
    if path.endswith(".mdx"):
        process(path)

    sys.exit(0)


if __name__ == "__main__":
    main()
