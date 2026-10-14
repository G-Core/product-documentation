"""Check one or more MDX files for encoding problems.

Usage (from the repository root):
    python .agents/tools/check_mdx_encoding.py path/to/article.mdx [more.mdx ...]
    python .agents/tools/check_mdx_encoding.py --fix path/to/article.mdx
    python .agents/tools/check_mdx_encoding.py --fix-dirty

Checks:
    NOT_UTF8   the file is not valid UTF-8
    BOM        the file starts with a UTF-8 BOM (breaks the YAML frontmatter)
    CRLF       the file contains Windows line endings (MDX here is LF only)
    GARBAGE    mojibake sequences such as the mangled em dash, produced when a tool
               reads UTF-8 as a legacy codepage
--fix removes a BOM and converts CRLF to LF. It never touches garbage: restore the
file from git and re-apply the edits instead.
--fix-dirty does that for MDX files git already lists as modified. A file whose
bytes already match the index is left alone, including one stored with CRLF.
Staged paths are staged again after a fix. The git hooks in .githooks run this.
Exit code 0 = clean, 1 = problems found, 2 = usage error.
"""
import re
import subprocess
import sys
from pathlib import Path

BOM = b"\xef\xbb\xbf"

# UTF-8 bytes of typographic characters decoded with a legacy codepage.
GARBAGE_PATTERNS = {
    "cp437 mojibake (e.g. mangled em dash)": re.compile("\u0393\u00c7"),
    "cp1252 mojibake of E2 80 xx (dashes, quotes)": re.compile("\u00e2\u20ac"),
    "cp1252 mojibake of two-byte letters": re.compile(
        "\u00c3[\u0080-\u00bf\u0152\u0153\u0160\u0161\u0178\u017d\u017e\u0192\u02c6\u02dc"
        "\u2013\u2014\u2018-\u201e\u2020-\u2022\u2026\u2030\u2039\u203a\u2122]"
    ),
    "replacement character": re.compile("\ufffd"),
}


def check(path: Path, fix: bool) -> list[str]:
    data = path.read_bytes()
    problems: list[str] = []

    try:
        data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [f"NOT_UTF8   byte {exc.start}: {exc.reason}"]

    changed = False
    if data.startswith(BOM):
        problems.append("BOM")
        if fix:
            data = data[len(BOM):]
            changed = True
    if b"\r\n" in data:
        problems.append("CRLF")
        if fix:
            data = data.replace(b"\r\n", b"\n")
            changed = True

    text = data.decode("utf-8")
    for label, pattern in GARBAGE_PATTERNS.items():
        hits = [i + 1 for i, line in enumerate(text.split("\n")) if pattern.search(line)]
        if hits:
            problems.append(f"GARBAGE   {label}: lines {hits[:8]}{'...' if len(hits) > 8 else ''}")

    if fix and changed:
        path.write_bytes(data)
        problems = [p + " (fixed)" if p in ("BOM", "CRLF") else p for p in problems]
    return problems


def _git(args: list[str]) -> bytes:
    return subprocess.check_output(["git", *args])


def fix_dirty() -> int:
    """Normalize BOM and CRLF on MDX files that git already reports as modified."""
    root = Path(_git(["rev-parse", "--show-toplevel"]).decode("utf-8").strip())
    raw = _git(["diff", "--name-only", "-z", "HEAD", "--", "*.mdx"])
    staged_raw = _git(["diff", "--cached", "--name-only", "-z", "--", "*.mdx"])
    names = {p.decode("utf-8").replace("\\", "/") for p in raw.split(b"\0") if p}
    names.update(p.decode("utf-8").replace("\\", "/") for p in staged_raw.split(b"\0") if p)
    cached = {
        p.decode("utf-8").replace("\\", "/")
        for p in _git(["diff", "--cached", "--name-only", "-z"]).split(b"\0")
        if p
    }

    for rel in sorted(names):
        path = root / rel
        if not path.is_file():
            continue
        try:
            blob = _git(["show", f":{rel}"])
        except subprocess.CalledProcessError:
            blob = None
        if blob is not None and path.read_bytes() == blob:
            continue
        problems = check(path, fix=True)
        if not any(p.endswith("(fixed)") for p in problems):
            continue
        print(f"normalized {rel}")
        if rel in cached:
            subprocess.check_call(["git", "add", "--", rel], cwd=root)
    return 0


def main() -> int:
    args = sys.argv[1:]
    if "--fix-dirty" in args:
        return fix_dirty()
    fix = "--fix" in args
    files = [Path(a) for a in args if a not in ("--fix", "--fix-dirty")]
    if not files:
        print(__doc__)
        return 2

    bad = 0
    for f in files:
        if not f.is_file():
            print(f"{f}: not found")
            bad += 1
            continue
        problems = check(f, fix)
        unfixed = [p for p in problems if not p.endswith("(fixed)")]
        if not problems:
            print(f"{f.as_posix()}: OK")
        else:
            print(f"{f.as_posix()}:")
            for p in problems:
                print(f"  {p}")
        if unfixed:
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
