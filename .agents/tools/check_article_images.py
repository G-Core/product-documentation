"""Check the images of one MDX article against the repository image rules.

Usage (from the repository root):
    python .agents/tools/check_article_images.py path/to/article.mdx

The images folder of an article is images/docs/<article path without .mdx>/.
Reports, one finding per line:
    WRONG_FOLDER  an image reference points outside the article's own folder
    NO_EXTENSION  an image reference has no file extension
    MISSING       a referenced file does not exist on disk
    DUPLICATE     two files in the article's folder have identical content
    UNREFERENCED  a file in the article's folder is not used by the article
Exit code 0 = no findings, 1 = findings, 2 = usage error.
"""
import hashlib
import re
import sys
from pathlib import Path

# Screenshots: markdown images and <img src>. They must live in the article's own folder.
SCREENSHOT_PATTERNS = [
    re.compile(r"""!\[[^\]]*\]\(\s*(/images/docs/[^)\s"']+)"""),
    re.compile(r"""<img\b[^>]*?\bsrc=["'](/images/docs/[^"'\s]+)["']"""),
]
# Any quoted /images/docs/ value (icon="...", img="...") counts as "used", like in
# scripts/normalize_images.py, but is not required to live in the article's folder.
ANY_REF_PATTERN = re.compile(r"""["'](/images/docs/[^"'\s]+)["']""")


def referenced_images(text: str) -> tuple[list[str], list[str]]:
    screenshots: list[str] = []
    for pattern in SCREENSHOT_PATTERNS:
        screenshots.extend(pattern.findall(text))
    everything = screenshots + ANY_REF_PATTERN.findall(text)
    return screenshots, everything


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    article = Path(sys.argv[1])
    if article.suffix != ".mdx" or not article.is_file():
        print(f"Not an .mdx file: {article}")
        return 2

    slug = article.with_suffix("").as_posix()
    folder = Path("images/docs") / slug
    expected_prefix = f"/images/docs/{slug}/"
    screenshots, refs = referenced_images(article.read_text(encoding="utf-8"))

    findings: list[str] = []
    referenced_files: set[Path] = set()

    for ref in dict.fromkeys(refs):
        path = Path(ref.lstrip("/"))
        if ref in screenshots and not ref.startswith(expected_prefix):
            findings.append(f"WRONG_FOLDER  {ref}  (expected prefix {expected_prefix})")
        if not path.suffix:
            findings.append(f"NO_EXTENSION  {ref}")
        if not path.is_file():
            findings.append(f"MISSING       {ref}")
        else:
            referenced_files.add(path)

    folder_files = sorted(p for p in folder.iterdir() if p.is_file()) if folder.is_dir() else []

    by_hash: dict[str, list[Path]] = {}
    for p in folder_files:
        by_hash.setdefault(hashlib.sha256(p.read_bytes()).hexdigest(), []).append(p)
    for group in by_hash.values():
        if len(group) > 1:
            findings.append("DUPLICATE     " + " == ".join(p.name for p in group))

    for p in folder_files:
        if p not in referenced_files:
            findings.append(f"UNREFERENCED  {p.as_posix()}")

    print(f"Article:        {article.as_posix()}")
    print(f"Images folder:  {folder.as_posix()}  ({'exists, ' + str(len(folder_files)) + ' files' if folder.is_dir() else 'does not exist'})")
    print(f"References:     {len(set(refs))} unique")
    if not findings:
        print("OK - no image findings")
        return 0
    for line in findings:
        print(line)
    print(f"{len(findings)} finding(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
