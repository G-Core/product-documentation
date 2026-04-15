"""Extract product SVG icons from Gcore portal shell chunk and write to images/docs/portal-icons/.

Update CHUNK_HASH if portal deploys a new main bundle (find in main.*.js: p.e(2345) and 2345:"<hash>").
"""
import re
import urllib.request
from pathlib import Path

CHUNK_HASH = "22b38581d17c74ae"
CHUNK_URL = f"https://portal.gcore.com/2345.{CHUNK_HASH}.js"
OUT_DIR = Path(__file__).resolve().parents[1] / "images" / "docs" / "portal-icons"

# Keys used on docs home.mdx (portal product icon names from shell config).
HOME_ICONS = frozenset(
    {
        "ai_infrastructure",
        "basic_vm",
        "cdn",
        "cloud",
        "dns",
        "fast_edge",
        "iaas",
        "shield_proxy",
        "storage",
        "streaming",
        "user",
        "waap",
    }
)


def apply_docs_brand_colors(svg: str) -> str:
    """Match docs primary orange (#ff4c00); portal uses currentColor (black as <img>)."""
    svg = svg.replace('stroke="currentColor"', 'stroke="#ff4c00"')
    svg = svg.replace('fill="currentColor"', 'fill="#ff4c00"')
    svg = svg.replace('fill="var(--gc-avatar-background-color)"', 'fill="#FFF2EA"')
    svg = svg.replace('fill="var(--gc-content-primary-color)"', 'fill="#ff4c00"')
    return svg


def main() -> None:
    js = urllib.request.urlopen(CHUNK_URL, timeout=120).read().decode("utf-8", "replace")
    # Icons are stored as: name:'<svg ... </svg>\n',
    pat = re.compile(r"([a-z_]+):'<(svg.*?</svg>)\\n'", re.DOTALL)
    found = pat.findall(js)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for name, inner in found:
        if name not in HOME_ICONS:
            continue
        svg = "<" + inner + "\n"
        svg = svg.replace("\\n", "\n")
        svg = apply_docs_brand_colors(svg)
        out = OUT_DIR / f"{name}.svg"
        out.write_text(svg, encoding="utf-8")
        written += 1
        print(f"  wrote {out.name} ({len(svg)} bytes)")
    print(f"Done. Wrote {written} / {len(HOME_ICONS)} expected icons.")


if __name__ == "__main__":
    main()
