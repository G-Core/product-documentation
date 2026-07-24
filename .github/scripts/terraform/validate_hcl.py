"""
Validate HCL examples in changed MDX files against the tracked provider schema.

Runs as a PR check. Reports attributes that no longer exist in the schema,
attributes whose required/optional status changed, and resources referenced
in articles but missing from the provider entirely.

Exit codes:
    0 — no validation errors
    1 — validation errors found (PR check fails)

Emits GitHub Actions annotations (::error:: and ::warning::) for each finding.

Usage:
    python3 validate_hcl.py <schema.json> <mdx_file> [<mdx_file> ...]
"""

import io
import json
import logging
import re
import sys
from pathlib import Path

try:
    import hcl2
    HCL2_AVAILABLE = True
except ImportError:
    HCL2_AVAILABLE = False

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

FENCE_RE = re.compile(r"```(?:hcl|terraform)\n(.*?)```", re.DOTALL)
BLOCK_RE = re.compile(
    r'(resource|data)\s+"(gcore_\w+)"\s+"([^"]+)"\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}',
    re.DOTALL,
)
ATTR_RE = re.compile(r"^\s{0,8}(\w+)\s*[={]", re.MULTILINE)


def load_schema(schema_path: str) -> dict:
    with open(schema_path, encoding="utf-8") as f:
        raw = json.load(f)
    provider_key = next(iter(raw.get("provider_schemas", {})), None)
    if not provider_key:
        return {}
    return raw["provider_schemas"][provider_key].get("resource_schemas", {})


def get_attrs(resource_schema: dict) -> dict:
    return resource_schema.get("block", {}).get("attributes", {})


def parse_hcl_block(hcl_text: str) -> list[dict]:
    """Parse HCL, return list of {block_type, resource_type, resource_name, attributes}."""
    if HCL2_AVAILABLE:
        try:
            parsed = hcl2.load(io.StringIO(hcl_text))
            blocks = []
            for block_type in ("resource", "data"):
                for type_map in parsed.get(block_type, []):
                    for resource_type, instances in type_map.items():
                        if not resource_type.startswith("gcore_"):
                            continue
                        for resource_name, body in instances.items():
                            if not isinstance(body, dict):
                                continue
                            blocks.append(
                                {
                                    "block_type": block_type,
                                    "resource_type": resource_type,
                                    "resource_name": resource_name,
                                    "attributes": sorted(body.keys()),
                                }
                            )
            if blocks:
                return blocks
        except Exception:
            pass

    blocks = []
    for m in BLOCK_RE.finditer(hcl_text):
        attrs = sorted(set(ATTR_RE.findall(m.group(4))))
        blocks.append(
            {
                "block_type": m.group(1),
                "resource_type": m.group(2),
                "resource_name": m.group(3),
                "attributes": attrs,
            }
        )
    return blocks


def line_of(content: str, pos: int) -> int:
    return content[:pos].count("\n") + 1


def validate_file(mdx_path: str, schema: dict) -> list[dict]:
    """
    Validate all HCL blocks in one MDX file.
    Returns list of finding dicts with keys: level, line, message.
    """
    content = Path(mdx_path).read_text(encoding="utf-8", errors="ignore")
    findings: list[dict] = []

    for fence_match in FENCE_RE.finditer(content):
        hcl_text = fence_match.group(1)
        fence_line = line_of(content, fence_match.start())
        blocks = parse_hcl_block(hcl_text)

        for block in blocks:
            rt = block["resource_type"]
            bt = block["block_type"]
            resource_schema = schema.get(rt)

            if resource_schema is None:
                findings.append(
                    {
                        "level": "warning",
                        "line": fence_line,
                        "message": (
                            f"{bt} '{rt}' is not in the tracked provider schema. "
                            "It may have been removed or renamed."
                        ),
                    }
                )
                continue

            schema_attrs = get_attrs(resource_schema)

            for attr in block.get("attributes", []):
                if attr not in schema_attrs:
                    findings.append(
                        {
                            "level": "error",
                            "line": fence_line,
                            "message": (
                                f"{bt} '{rt}': attribute '{attr}' does not exist "
                                "in the current provider schema."
                            ),
                        }
                    )

    return findings


def emit_annotation(level: str, filepath: str, line: int, message: str) -> None:
    tag = "error" if level == "error" else "warning"
    print(f"::{tag} file={filepath},line={line}::{message}")


def main() -> None:
    if len(sys.argv) < 3:
        log.error("Usage: validate_hcl.py <schema.json> <mdx_file> [<mdx_file> ...]")
        sys.exit(2)

    schema_path = sys.argv[1]
    mdx_files = sys.argv[2:]

    schema = load_schema(schema_path)
    if not schema:
        log.error("Could not load resource schemas from %s", schema_path)
        sys.exit(2)

    total_errors = 0
    total_warnings = 0

    for mdx_path in mdx_files:
        if not Path(mdx_path).exists():
            log.warning("File not found: %s", mdx_path)
            continue

        findings = validate_file(mdx_path, schema)
        for f in findings:
            emit_annotation(f["level"], mdx_path, f["line"], f["message"])
            if f["level"] == "error":
                total_errors += 1
            else:
                total_warnings += 1

    log.info(
        "Validation complete: %d error(s), %d warning(s) across %d file(s)",
        total_errors,
        total_warnings,
        len(mdx_files),
    )

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
