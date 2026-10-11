"""Crop a full-viewport screenshot to the area an article step describes.

Usage (from the repository root):
    python .agents/tools/crop_screenshot.py in.png out.png --box X,Y,W,H [--box X,Y,W,H ...] [--pad 24]

Each --box is the bounding box of one UI element the step names, taken from
browser_snapshot with boxes=true (viewport-relative CSS pixels, [box=x,y,width,height]).
The crop is the union of all boxes plus padding, clamped to the image. The input file
is never modified, so the full screenshot stays available for another attempt.

Options:
    --pad N     padding in pixels around the union of the boxes (default 12; keep it below half the gap to neighbouring elements)
    --scale S   image pixels per CSS pixel; use 1 for screenshots taken with scale=css (default 1)

Prints the final box and warnings. Exit code 0 = cropped, 1 = cropped with a warning
the caller must check, 2 = usage error.
"""
import argparse
import sys
from pathlib import Path

from PIL import Image

MIN_WIDTH = 160
MIN_HEIGHT = 60
FULL_FRAME_RATIO = 0.9


def parse_box(text: str) -> tuple[float, float, float, float]:
    parts = [p for p in text.replace(" ", "").split(",") if p]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError(f"box must be X,Y,W,H, got {text!r}")
    x, y, w, h = (float(p) for p in parts)
    if w <= 0 or h <= 0:
        raise argparse.ArgumentTypeError(f"box must have positive width and height: {text!r}")
    return x, y, w, h


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--box", action="append", type=parse_box, required=True)
    parser.add_argument("--pad", type=float, default=12)
    parser.add_argument("--scale", type=float, default=1.0)
    args = parser.parse_args()

    src = Path(args.input)
    dst = Path(args.output)
    if not src.is_file():
        print(f"Input not found: {src}")
        return 2
    if src.resolve() == dst.resolve():
        print("Output must differ from input: the full screenshot is kept for retries")
        return 2

    image = Image.open(src)
    width, height = image.size

    left = min(b[0] for b in args.box)
    top = min(b[1] for b in args.box)
    right = max(b[0] + b[2] for b in args.box)
    bottom = max(b[1] + b[3] for b in args.box)

    outside = [
        b for b in args.box
        if b[0] < 0 or b[1] < 0 or (b[0] + b[2]) * args.scale > width or (b[1] + b[3]) * args.scale > height
    ]

    left = max(0, round((left - args.pad) * args.scale))
    top = max(0, round((top - args.pad) * args.scale))
    right = min(width, round((right + args.pad) * args.scale))
    bottom = min(height, round((bottom + args.pad) * args.scale))

    warnings: list[str] = []
    if outside:
        warnings.append(
            f"{len(outside)} box(es) reach outside the screenshot: scroll so the element is fully visible, "
            "take a new screenshot, and take new boxes from a new snapshot (boxes are relative to the current scroll position)"
        )
    if right <= left or bottom <= top:
        print("Crop is empty: the boxes are outside the image. Check that they come from the same screenshot state.")
        return 2
    if right - left < MIN_WIDTH or bottom - top < MIN_HEIGHT:
        warnings.append(f"crop is very small ({right - left}x{bottom - top}px): the chosen element may be too narrow, include its parent")
    if (right - left) >= width * FULL_FRAME_RATIO and (bottom - top) >= height * FULL_FRAME_RATIO:
        warnings.append("crop covers almost the whole screenshot: keep the full viewport or choose a tighter element")

    dst.parent.mkdir(parents=True, exist_ok=True)
    image.crop((left, top, right, bottom)).save(dst)

    print(f"Input:   {src.as_posix()} ({width}x{height})")
    print(f"Crop:    left={left} top={top} right={right} bottom={bottom} -> {right - left}x{bottom - top}")
    print(f"Output:  {dst.as_posix()}")
    for w in warnings:
        print(f"WARNING: {w}")
    return 1 if warnings else 0


if __name__ == "__main__":
    sys.exit(main())
