"""
Assemble one GitHub issue body from whichever API/SDK diff sections ran.

Each section is optional: the push-triggered half of the workflow only ever
produces an API section; the cron/dispatch half produces Python and/or Go
SDK sections (only for the language(s) whose pin was behind). Whichever
sections are present get their own '## API' / '## Python SDK' / '## Go SDK'
heading; missing ones are omitted, not printed as empty.

Usage:
    python3 assemble_issue.py \\
        [--api-diff <path>] [--python-diff <path>] [--go-diff <path>] \\
        --output <path>
"""

import argparse
import sys
from pathlib import Path

SECTIONS = [
    ("api_diff", "## API"),
    ("python_diff", "## Python SDK"),
    ("go_diff", "## Go SDK"),
]

ACTION_CHECKLIST = """
### Action required

1. For each **REMOVED**, **CHANGED**, or **REGRESSION** entry above with listed articles, open those articles and update the examples.
2. For each **ADDED** operation or **NEWLY AVAILABLE** method, run a live test (curl / Python SDK / Go SDK, per the api-use-case skill) before documenting it — this tool only narrows down candidates, it does not confirm SDK behavior.
3. Read the release notes section(s) above in full, even if no method or gap changes are listed — behavioral changes with no structural footprint (for example, new client-level defaults) will not show up as a diff.
4. After docs are updated, update the relevant pin file(s) under `api-sdk-tracker/` and commit the rebuilt `endpoint_index.json` / `doc_index.json` to close this issue.
"""


def read_if_exists(path: str | None) -> str | None:
    if not path:
        return None
    p = Path(path)
    if not p.exists():
        return None
    text = p.read_text(encoding="utf-8-sig").strip()
    return text or None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--api-diff", default=None)
    parser.add_argument("--python-diff", default=None)
    parser.add_argument("--go-diff", default=None)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    contents = {
        "api_diff": read_if_exists(args.api_diff),
        "python_diff": read_if_exists(args.python_diff),
        "go_diff": read_if_exists(args.go_diff),
    }

    body_parts: list[str] = []
    for key, heading in SECTIONS:
        text = contents[key]
        if text:
            body_parts.append(f"{heading}\n\n{text}")

    if not body_parts:
        print("No sections with content; nothing to assemble.")
        sys.exit(1)

    body_parts.append(ACTION_CHECKLIST)
    output = "\n\n".join(body_parts)

    Path(args.output).write_text(output, encoding="utf-8")
    print(f"Assembled issue body ({len(body_parts) - 1} section(s)) -> {args.output}")


if __name__ == "__main__":
    main()
