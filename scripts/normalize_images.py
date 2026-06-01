"""
normalize_images.py — Normalize image naming convention in product-documentation.

Convention:
    images/docs/{product}/{article-slug}/image{N}.{ext}
    where N is the 1-based order of first appearance in the corresponding MDX article.
    The article slug is carried by the folder; the filename itself is just imageN.

Actions performed:
  - Rename non-conforming images based on their position in the MDX article.
  - Renumber images so numbering is sequential with no gaps.
  - Move images that belong to a different article folder based on MDX references.
  - Delete images not referenced by any MDX (orphaned), unless they were
    added in the current PR (--pr-images) — those get a grace period.
  - Update all image references in MDX files after renames/moves.

Usage:
    # Dry-run: preview all changes without writing anything
    python scripts/normalize_images.py --repo . --dry-run

    # Process only folders affected by changed files (for CI use):
    python scripts/normalize_images.py --repo . --changed-files f1.png f2.mdx

    # Mark PR-added images so they are not deleted if temporarily unreferenced:
    python scripts/normalize_images.py --repo . --pr-images img1.png img2.png

    # Full run (all folders):
    python scripts/normalize_images.py --repo .
"""

import argparse
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

IMAGES_ROOT = "images/docs"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}

# Image product folder names that differ from MDX product folder names.
PRODUCT_FOLDER_MAP: dict[str, str] = {
    "streaming-platform": "streaming",
}

# Reverse map: MDX product folder → image product folder.
MDX_TO_IMAGE_PRODUCT: dict[str, str] = {v: k for k, v in PRODUCT_FOLDER_MAP.items()}

# Regex patterns to extract image paths from MDX content.
_IMAGE_REF_PATTERNS = [
    re.compile(r'!\[[^\]]*\]\((/images/docs/[^)\s"\']+)\)'),        # ![alt](/images/...)
    re.compile(r'src=["\']([^"\']*?/images/docs/[^"\']+)["\']'),    # src="/images/..."
    re.compile(r'href=["\']([^"\']*?/images/docs/[^"\']+)["\']'),   # href="/images/..."
]

# Pattern matching the current convention: imageN.ext
_CONVENTION_RE = re.compile(r'^image(\d+)(\.[^.]+)$')


# ── Data ────────────────────────────────────────────────────────────────────


@dataclass
class ImageOp:
    """A single file operation to be applied."""
    kind: str           # "rename" | "move" | "delete"
    src: Path           # absolute source path
    dst: Optional[Path] # absolute destination path (None for delete)


# ── Parsing helpers ──────────────────────────────────────────────────────────


def _extract_refs_in_order(text: str) -> list[str]:
    """Return image paths in order of first appearance in MDX text."""
    positions: dict[str, int] = {}
    for pat in _IMAGE_REF_PATTERNS:
        for m in pat.finditer(text):
            raw = m.group(1).strip().lstrip("/").split("?")[0].split("#")[0]
            if raw.startswith("images/docs/") and raw not in positions:
                positions[raw] = m.start()
    return sorted(positions, key=lambda p: positions[p])


def _is_image(path: Path) -> bool:
    return path.suffix.lower() in IMAGE_EXTENSIONS


# ── Build global maps ────────────────────────────────────────────────────────


def build_ref_map(repo_root: Path) -> dict[str, list[Path]]:
    """
    Build a map: image_rel_str → [MDX paths that reference it].
    Image paths are relative to repo_root, forward-slash separated.
    """
    ref_map: dict[str, list[Path]] = {}
    for mdx in repo_root.rglob("*.mdx"):
        try:
            text = mdx.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for ref in _extract_refs_in_order(text):
            ref_map.setdefault(ref, []).append(mdx)
    return ref_map


def build_mdx_image_order(mdx_path: Path) -> list[str]:
    """Return image paths (relative to repo_root) in appearance order from one MDX."""
    try:
        text = mdx_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    return _extract_refs_in_order(text)


# ── Folder ↔ Article mapping ─────────────────────────────────────────────────


def mdx_product_folder(img_product: str) -> str:
    """Map image product folder name to MDX product folder name."""
    return PRODUCT_FOLDER_MAP.get(img_product, img_product)


def image_folder_for_mdx(mdx_rel: Path) -> Path:
    """
    Compute the canonical image folder for a given MDX file.
    cdn/add-an-origin-group.mdx → images/docs/cdn/add-an-origin-group/
    """
    parts = mdx_rel.with_suffix("").parts  # ("cdn", "add-an-origin-group")
    mdx_product = parts[0]
    img_product = MDX_TO_IMAGE_PRODUCT.get(mdx_product, mdx_product)
    rest = parts[1:]
    return Path(IMAGES_ROOT) / img_product / Path(*rest) if rest else Path(IMAGES_ROOT) / img_product


def mdx_for_image_folder(folder_abs: Path, repo_root: Path) -> Optional[Path]:
    """
    Derive the MDX article for an image folder, or None if not found.
    images/docs/cdn/add-an-origin-group/ → cdn/add-an-origin-group.mdx
    """
    images_root_abs = repo_root / IMAGES_ROOT
    try:
        rel = folder_abs.relative_to(images_root_abs)
    except ValueError:
        return None
    parts = rel.parts
    if not parts:
        return None
    img_product, *rest_parts = parts
    mdx_product = mdx_product_folder(img_product)
    candidate = repo_root / mdx_product / Path(*rest_parts).with_suffix(".mdx") if rest_parts else None
    if candidate and candidate.exists():
        return candidate
    return None


def mdx_for_image(img_abs: Path, repo_root: Path, ref_map: dict[str, list[Path]]) -> Optional[Path]:
    """
    Find the primary MDX article for an image.
    Prefers the ref_map lookup; falls back to folder convention.
    """
    img_rel = str(img_abs.relative_to(repo_root)).replace("\\", "/")
    mdxs = ref_map.get(img_rel, [])
    if mdxs:
        return mdxs[0]
    return mdx_for_image_folder(img_abs.parent, repo_root)


# ── Plan computation ─────────────────────────────────────────────────────────


def compute_plan(
    repo_root: Path,
    affected_folders: set[Path],
    ref_map: dict[str, list[Path]],
    pr_images: set[str],
) -> tuple[list[ImageOp], dict[str, str]]:
    """
    Compute all operations needed to normalize affected image folders.

    Returns:
        ops: List of ImageOp to execute.
        rename_map: old_rel → new_rel for MDX reference updates.
    """
    ops: list[ImageOp] = []
    rename_map: dict[str, str] = {}

    for folder in sorted(affected_folders):
        if not folder.is_dir():
            continue

        images_in_folder = sorted(
            p for p in folder.iterdir() if p.is_file() and _is_image(p)
        )
        if not images_in_folder:
            continue

        # Find the corresponding MDX article.
        mdx = mdx_for_image_folder(folder, repo_root)

        if mdx is None:
            # No MDX found via path convention — check ref_map.
            # Pick the MDX that references the most images in this folder.
            mdx_hits: dict[Path, int] = {}
            for img in images_in_folder:
                img_rel = str(img.relative_to(repo_root)).replace("\\", "/")
                for m in ref_map.get(img_rel, []):
                    mdx_hits[m] = mdx_hits.get(m, 0) + 1
            if mdx_hits:
                mdx = max(mdx_hits, key=lambda m: mdx_hits[m])

        if mdx is None:
            # No article claims these images — all are orphaned.
            for img in images_in_folder:
                img_rel = str(img.relative_to(repo_root)).replace("\\", "/")
                if img_rel not in pr_images:
                    log.info("DELETE orphaned (no article): %s", img_rel)
                    ops.append(ImageOp("delete", img, None))
            continue

        # Determine canonical folder for this article.
        mdx_rel = mdx.relative_to(repo_root)
        canonical_folder_rel = image_folder_for_mdx(mdx_rel)
        canonical_folder_abs = repo_root / canonical_folder_rel

        # Get images ordered by appearance in MDX.
        ordered_refs = build_mdx_image_order(mdx)
        # Only keep refs that fall inside the canonical folder (or current folder).
        def _in_our_folder(ref: str) -> bool:
            return (
                ref.startswith(str(canonical_folder_rel).replace("\\", "/") + "/")
                or ref.startswith(
                    str(folder.relative_to(repo_root)).replace("\\", "/") + "/"
                )
            )
        ordered_refs = [r for r in ordered_refs if _in_our_folder(r)]

        # Build ordered list of actual file paths (some may not exist yet if MDX is ahead).
        ordered_abs: list[Optional[Path]] = []
        for ref in ordered_refs:
            candidate = repo_root / ref
            ordered_abs.append(candidate if candidate.exists() else None)

        # Collect images in folder that are NOT in ordered_refs (orphaned or misplaced).
        referenced_abs = {p for p in ordered_abs if p is not None}
        for img in images_in_folder:
            img_rel = str(img.relative_to(repo_root)).replace("\\", "/")
            if img not in referenced_abs:
                if img_rel in pr_images:
                    # Grace period: newly added, not yet in MDX — skip.
                    log.info("SKIP newly added (not yet in MDX): %s", img_rel)
                else:
                    log.info("DELETE orphaned (unreferenced): %s", img_rel)
                    ops.append(ImageOp("delete", img, None))

        # Assign canonical names based on position in article.
        for idx, img_abs in enumerate(ordered_abs, start=1):
            if img_abs is None:
                continue
            ext = img_abs.suffix.lower()
            new_name = f"image{idx}{ext}"
            new_abs = canonical_folder_abs / new_name
            old_rel = str(img_abs.relative_to(repo_root)).replace("\\", "/")
            new_rel = str(new_abs.relative_to(repo_root)).replace("\\", "/")

            if img_abs == new_abs:
                continue  # Already correct.

            kind = "move" if img_abs.parent != new_abs.parent else "rename"
            log.info("%s: %s → %s", kind.upper(), old_rel, new_rel)
            ops.append(ImageOp(kind, img_abs, new_abs))
            rename_map[old_rel] = new_rel

    return ops, rename_map


def collect_affected_folders(
    repo_root: Path,
    changed_files: list[str],
    ref_map: dict[str, list[Path]],
) -> set[Path]:
    """
    Given a list of changed file paths (relative to repo_root),
    return the set of image folders that need processing.
    """
    folders: set[Path] = set()
    for f in changed_files:
        p = repo_root / f
        if _is_image(p) and IMAGES_ROOT in f:
            folders.add(p.parent)
        elif f.endswith(".mdx"):
            # Also process all image folders referenced by this MDX.
            mdx_abs = repo_root / f
            for ref in build_mdx_image_order(mdx_abs):
                img_folder = (repo_root / ref).parent
                if img_folder.is_dir():
                    folders.add(img_folder)
    return folders


# ── Execution ────────────────────────────────────────────────────────────────


def execute_ops(ops: list[ImageOp], dry_run: bool) -> None:
    """Apply file operations: rename, move, delete."""
    for op in ops:
        if op.kind in ("rename", "move"):
            if not dry_run:
                op.dst.parent.mkdir(parents=True, exist_ok=True)
                op.src.rename(op.dst)
            log.info("[%s] %s] %s → %s", "DRY" if dry_run else "OK", op.kind, op.src.name, op.dst.name)
        elif op.kind == "delete":
            if not dry_run:
                op.src.unlink(missing_ok=True)
            log.info("[%s] DELETE %s", "DRY" if dry_run else "OK", op.src.name)


def update_mdx_refs(rename_map: dict[str, str], repo_root: Path, dry_run: bool) -> int:
    """
    Replace old image paths with new ones in all MDX files.
    Returns the number of files modified.
    """
    if not rename_map:
        return 0

    modified = 0
    for mdx in repo_root.rglob("*.mdx"):
        try:
            text = mdx.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        new_text = text
        for old_rel, new_rel in rename_map.items():
            # Match both with and without leading slash.
            for old in (old_rel, "/" + old_rel):
                new = ("/" if old.startswith("/") else "") + new_rel
                new_text = new_text.replace(old, new)

        if new_text != text:
            modified += 1
            if not dry_run:
                mdx.write_text(new_text, encoding="utf-8")
            log.info("[%s] Updated refs in %s", "DRY" if dry_run else "OK",
                     mdx.relative_to(repo_root))

    return modified


# ── CLI ──────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path,
                        help="Path to the product-documentation repo root.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing anything.")
    parser.add_argument("--changed-files", nargs="*", default=[],
                        help="Files changed in this PR (relative to repo root). "
                             "If omitted, all image folders are processed.")
    parser.add_argument("--pr-images", nargs="*", default=[],
                        help="Image paths (relative) added in this PR — "
                             "these are not deleted even if temporarily unreferenced.")
    return parser.parse_args()


def main() -> int:
    """Entry point."""
    args = parse_args()
    repo_root = args.repo.resolve()

    if not (repo_root / IMAGES_ROOT).is_dir():
        log.error("images/docs/ not found in repo: %s", repo_root)
        return 1

    log.info("Building image reference map...")
    ref_map = build_ref_map(repo_root)
    log.info("Found references to %d unique image paths.", len(ref_map))

    pr_images: set[str] = {p.replace("\\", "/") for p in args.pr_images}

    if args.changed_files:
        affected_folders = collect_affected_folders(repo_root, args.changed_files, ref_map)
        log.info("Processing %d affected folder(s).", len(affected_folders))
    else:
        images_root_abs = repo_root / IMAGES_ROOT
        affected_folders = {
            p for p in images_root_abs.rglob("*")
            if p.is_dir() and any(_is_image(c) for c in p.iterdir() if c.is_file())
        }
        log.info("Full run: processing %d image folder(s).", len(affected_folders))

    ops, rename_map = compute_plan(repo_root, affected_folders, ref_map, pr_images)

    log.info(
        "Plan: %d rename/move, %d delete, %d MDX ref updates.",
        sum(1 for o in ops if o.kind in ("rename", "move")),
        sum(1 for o in ops if o.kind == "delete"),
        len(rename_map),
    )

    if not ops and not rename_map:
        log.info("Nothing to do.")
        return 0

    execute_ops(ops, args.dry_run)
    modified = update_mdx_refs(rename_map, repo_root, args.dry_run)
    log.info("MDX files updated: %d", modified)

    if args.dry_run:
        log.info("Dry-run complete. No files were changed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
