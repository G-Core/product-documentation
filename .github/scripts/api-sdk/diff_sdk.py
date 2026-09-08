"""
Diff a Gcore SDK (Python or Go) release-to-release and report doc impact.

Combines three signals into one report for a single language:

1. Structural method diff — added/removed/changed methods between the
   pinned and latest SDK version, parsed from each repo's `cloud/api.md`
   (Go) / `src/gcore/resources/cloud/api.md` (Python). Cross-referenced
   against doc_index.json so only methods actually used in a documented
   example are flagged as needing article updates (same precision
   principle as the Terraform tracker's attribute-level index).

2. Exhaustive gap check — compares two endpoint_index.json snapshots (one
   built at the pinned SDK ref, one at the latest ref, both via
   build_endpoint_index.py's literal source-path matching). Only the DELTA
   is reported: operations that just gained SDK coverage (candidates to
   document, this is the exact DOC-1913 moment) or, rarer, ones that lost
   it. The full standing backlog of never-covered operations is collapsed
   to a per-product count — it is a known state, not new drift, and
   dumping the whole list every run would drown out the actual signal.

3. Release-notes watcher — every GitHub release between the pinned and
   latest tag, verbatim. This is the only signal that can catch a
   behavioral change with no structural footprint at all (the exact
   scenario found in this repo: gcore-go's client-level
   GCORE_CLOUD_PROJECT_ID / GCORE_CLOUD_REGION_ID env-var defaults, which
   changed no method signature and was never mentioned in a changelog
   either — release notes are read by a human either way, this just
   collects them in one place).

Exit codes:
    0 — no changes to report for this language
    1 — changes found (caller should include this language's section)

Writes GITHUB_OUTPUT variables (namespaced by language):
    <lang>_has_changes     — true | false
    <lang>_has_doc_impact  — true | false
    <lang>_sdk_diff        — human-readable markdown section

Usage:
    python3 diff_sdk.py <python|go> \\
        --pinned-ref <old_tag> --latest-ref <new_tag> \\
        --doc-index api-sdk-tracker/doc_index.json \\
        --old-endpoint-index api-sdk-tracker/endpoint_index.json \\
        --new-endpoint-index /tmp/endpoint_index-latest.json \\
        --repo <owner/repo>

<old-endpoint-index> is the currently committed snapshot (built at the
pinned refs). <new-endpoint-index> is freshly built by build_endpoint_index.py
against the latest refs before this script runs, and is not committed unless
a human bumps the pin files afterwards.
"""

import argparse
import json
import logging
import os
import re
import sys
import urllib.error
import urllib.request

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

CODE_LINE_RE = re.compile(r'<code title="(get|post|put|patch|delete) ([^"]+)">(.+?)</code>')
LINK_TAG_RE = re.compile(r"<a[^>]*>([^<]*)</a>")
PATH_PARAM_RE = re.compile(r"\{[^{}]+\}")

LANGUAGE_CONFIG = {
    "python": {
        "api_md_path": "src/gcore/resources/cloud/api.md",
        "call_re": re.compile(r"client\.cloud\.((?:\w+\.)+\w+)\("),
        "prefix": "cloud",
        "doc_index_key": "python_method_to_articles",
        "in_sdk_key": "in_python_sdk",
    },
    "go": {
        "api_md_path": "cloud/api.md",
        "call_re": re.compile(r"client\.Cloud\.((?:\w+\.)+\w+)\("),
        "prefix": "Cloud",
        "doc_index_key": "go_method_to_articles",
        "in_sdk_key": "in_go_sdk",
    },
}


def normalize_path(raw_path: str) -> str:
    return PATH_PARAM_RE.sub("{}", raw_path)


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fetch_raw_file(repo: str, ref: str, path: str) -> str | None:
    url = f"https://raw.githubusercontent.com/{repo}/{ref}/{path}"
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.URLError as exc:
        log.error("Could not fetch %s: %s", url, exc)
        return None


def strip_links(text: str) -> str:
    return LINK_TAG_RE.sub(r"\1", text)


def parse_api_md(text: str, call_re: re.Pattern, prefix: str) -> dict[str, dict]:
    """Parse one cloud/api.md into {dotted_method_name: {method, path, signature}}."""
    methods: dict[str, dict] = {}
    for m in CODE_LINE_RE.finditer(text):
        http_method = m.group(1).upper()
        raw_path = m.group(2)
        line_plain = strip_links(m.group(3))
        call_m = call_re.match(line_plain)
        if not call_m:
            continue
        dotted = f"{prefix}.{call_m.group(1)}"
        signature = line_plain[call_m.end() - 1 :].strip()
        methods[dotted] = {
            "method": http_method,
            "path": normalize_path(raw_path),
            "signature": signature,
        }
    return methods


def format_articles(articles: list[str]) -> str:
    return ", ".join(f"`{a}`" for a in articles)


def diff_methods(
    old_methods: dict[str, dict], new_methods: dict[str, dict], method_to_articles: dict[str, list]
) -> tuple[list[str], bool]:
    added = sorted(set(new_methods) - set(old_methods))
    removed = sorted(set(old_methods) - set(new_methods))
    changed = sorted(
        name
        for name in set(old_methods) & set(new_methods)
        if old_methods[name]["signature"] != new_methods[name]["signature"]
    )

    if not (added or removed or changed):
        return [], False

    lines: list[str] = []
    has_impact = False

    for name in removed:
        arts = method_to_articles.get(name, [])
        if arts:
            has_impact = True
            lines.append(
                f"- **REMOVED** `{name}` — **{len(arts)} article(s) use this method "
                f"and must be updated:** {format_articles(arts)}"
            )
        else:
            lines.append(f"- **REMOVED** `{name}` — no articles use this method (no action needed)")

    for name in changed:
        arts = method_to_articles.get(name, [])
        old_sig = old_methods[name]["signature"]
        new_sig = new_methods[name]["signature"]
        if arts:
            has_impact = True
            lines.append(
                f"- **CHANGED** `{name}` — **{len(arts)} article(s) may need review:** "
                f"{format_articles(arts)}\n  - old: `{old_sig}`\n  - new: `{new_sig}`"
            )
        else:
            lines.append(
                f"- **CHANGED** `{name}` — no articles use this method\n"
                f"  - old: `{old_sig}`\n  - new: `{new_sig}`"
            )

    for name in added:
        lines.append(f"- **ADDED** `{name}` — `{new_methods[name]['signature']}`")

    return lines, has_impact


def index_operations_by_key(endpoint_index: dict) -> dict[tuple[str, str, str], dict]:
    """Flatten products -> operations into {(product, method, path): op}."""
    flat: dict[tuple[str, str, str], dict] = {}
    for product, entry in endpoint_index.get("products", {}).items():
        for op in entry["operations"]:
            if op["deprecated"]:
                continue
            flat[(product, op["method"], op["path"])] = op
    return flat


def format_gap_diff(old_index: dict, new_index: dict, language: str) -> tuple[list[str], list[str]]:
    """Compare two endpoint_index snapshots for one language.

    Returns (delta_lines, backlog_lines). delta_lines lists operations whose
    coverage changed between the two snapshots — this is the actionable
    signal. backlog_lines is a compact per-product count of operations that
    were, and still are, uncovered — informational only, never itemized.
    """
    in_sdk_key = LANGUAGE_CONFIG[language]["in_sdk_key"]
    old_ops = index_operations_by_key(old_index)
    new_ops = index_operations_by_key(new_index)

    newly_covered: list[tuple[tuple[str, str, str], dict]] = []
    newly_gapped: list[tuple[tuple[str, str, str], dict]] = []
    backlog_count: dict[str, int] = {}
    backlog_total: dict[str, int] = {}

    for key, new_op in new_ops.items():
        product = key[0]
        old_op = old_ops.get(key)
        old_covered = old_op.get(in_sdk_key) if old_op else None
        new_covered = new_op.get(in_sdk_key)

        if new_covered is None:
            continue

        backlog_total[product] = backlog_total.get(product, 0) + 1
        if not new_covered:
            backlog_count[product] = backlog_count.get(product, 0) + 1

        if old_covered is False and new_covered is True:
            newly_covered.append((key, new_op))
        elif old_covered is True and new_covered is False:
            newly_gapped.append((key, new_op))

    delta_lines: list[str] = []
    for (product, method, path), op in sorted(newly_covered):
        delta_lines.append(
            f"- **NEWLY AVAILABLE** `{method} {path}` ({product}) — {op.get('summary', '')} "
            "— not yet documented, consider adding it"
        )
    for (product, method, path), op in sorted(newly_gapped):
        delta_lines.append(
            f"- **REGRESSION** `{method} {path}` ({product}) — {op.get('summary', '')} "
            f"— no longer has a matching {language.title()} SDK method"
        )

    backlog_lines: list[str] = []
    for product in sorted(backlog_count):
        gaps, total = backlog_count[product], backlog_total[product]
        if gaps == total:
            continue  # zero coverage at all — standing, uninteresting state
        backlog_lines.append(
            f"- **{product}**: {gaps} of {total} non-deprecated operation(s) still have no "
            f"matching {language.title()} SDK method (unchanged backlog, see endpoint_index.json)"
        )

    return delta_lines, backlog_lines


def version_tuple(tag: str) -> tuple[int, ...]:
    parts = re.findall(r"\d+", tag)
    return tuple(int(p) for p in parts) if parts else (0,)


def fetch_releases(repo: str, token: str | None) -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{repo}/releases?per_page=100"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        log.warning("Could not fetch releases for %s: %s", repo, exc)
        return []


def releases_between(releases: list[dict], pinned: str, latest: str) -> list[dict]:
    lo, hi = version_tuple(pinned), version_tuple(latest)
    result = [r for r in releases if lo < version_tuple(r.get("tag_name", "")) <= hi]
    result.sort(key=lambda r: version_tuple(r.get("tag_name", "")))
    return result


def format_release_notes(releases: list[dict], repo: str) -> str:
    if not releases:
        return "No releases found between the pinned and latest version."
    parts = []
    for r in releases:
        tag = r.get("tag_name", "?")
        body = (r.get("body") or "").strip() or "_(no release notes)_"
        parts.append(f"**[{tag}](https://github.com/{repo}/releases/tag/{tag})**\n\n{body}")
    return "\n\n---\n\n".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("language", choices=sorted(LANGUAGE_CONFIG))
    parser.add_argument("--pinned-ref", required=True)
    parser.add_argument("--latest-ref", required=True)
    parser.add_argument("--doc-index", required=True)
    parser.add_argument(
        "--old-endpoint-index",
        required=True,
        help="endpoint_index.json built at --pinned-ref (the currently committed snapshot)",
    )
    parser.add_argument(
        "--new-endpoint-index",
        required=True,
        help="endpoint_index.json freshly built at --latest-ref",
    )
    parser.add_argument("--repo", required=True, help="e.g. G-Core/gcore-python")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = LANGUAGE_CONFIG[args.language]

    if args.pinned_ref == args.latest_ref:
        log.info("Pinned and latest refs are identical (%s); nothing to do.", args.pinned_ref)
        sys.exit(0)

    old_text = fetch_raw_file(args.repo, args.pinned_ref, config["api_md_path"])
    new_text = fetch_raw_file(args.repo, args.latest_ref, config["api_md_path"])
    if old_text is None or new_text is None:
        log.error("Could not fetch api.md for %s; aborting", args.language)
        sys.exit(2)

    old_methods = parse_api_md(old_text, config["call_re"], config["prefix"])
    new_methods = parse_api_md(new_text, config["call_re"], config["prefix"])
    log.info(
        "Parsed %d method(s) @ %s, %d method(s) @ %s",
        len(old_methods), args.pinned_ref, len(new_methods), args.latest_ref,
    )

    doc_index = load_json(args.doc_index)
    old_endpoint_index = load_json(args.old_endpoint_index)
    new_endpoint_index = load_json(args.new_endpoint_index)
    method_to_articles = doc_index.get(config["doc_index_key"], {})

    method_lines, method_impact = diff_methods(old_methods, new_methods, method_to_articles)
    gap_delta_lines, gap_backlog_lines = format_gap_diff(old_endpoint_index, new_endpoint_index, args.language)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    releases = fetch_releases(args.repo, token)
    between = releases_between(releases, args.pinned_ref, args.latest_ref)
    release_notes = format_release_notes(between, args.repo)

    lang_title = args.language.title()
    all_lines: list[str] = []

    if method_lines:
        all_lines.append(f"\n### {lang_title} SDK method changes ({args.pinned_ref} -> {args.latest_ref})")
        all_lines.extend(method_lines)

    if gap_delta_lines:
        all_lines.append(
            f"\n### {lang_title} SDK gap check — coverage changes ({args.pinned_ref} -> {args.latest_ref})"
        )
        all_lines.extend(gap_delta_lines)

    if gap_backlog_lines:
        all_lines.append(f"\n### {lang_title} SDK gap check — unchanged backlog")
        all_lines.extend(gap_backlog_lines)

    all_lines.append(f"\n### {lang_title} SDK release notes ({args.pinned_ref} -> {args.latest_ref})")
    all_lines.append(release_notes)
    all_lines.append(
        "\n_Release notes can describe behavioral changes with no structural footprint "
        "(e.g. new client-level defaults). Read them even when no method or gap changes "
        "are listed above._"
    )

    has_changes = bool(method_lines) or bool(gap_delta_lines) or bool(between)
    has_doc_impact = method_impact or bool(gap_delta_lines)

    output = "\n".join(all_lines)
    print(output)

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        marker = f"{args.language.upper()}_SDK_EOF"
        with open(github_output, "a", encoding="utf-8") as f:
            f.write(f"{args.language}_sdk_diff<<{marker}\n")
            f.write(output + "\n")
            f.write(f"{marker}\n")
            f.write(f"{args.language}_has_changes={'true' if has_changes else 'false'}\n")
            f.write(f"{args.language}_has_doc_impact={'true' if has_doc_impact else 'false'}\n")

    sys.exit(0 if not has_changes else 1)


if __name__ == "__main__":
    main()
