"""Draft frontmatter descriptions with the preprod AI Gateway.

Sends each article's title, headings, and opening prose to DeepSeek and
replaces only the ``description`` line when the reply passes the search-summary
rules. Existing article bodies are left unchanged.

The API key is read from ``PREPROD_API_KEY`` via dotenv. The key is never logged.

Usage:
    python scripts/generate_seo_descriptions.py --repo .
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

log = logging.getLogger(__name__)

GATEWAY_URL = "https://agent-platform-ai-gateway-preprod.i.gc.onl/v1/chat/completions"
MODEL = "deepseek-ai/DeepSeek-V4.1-Flash"
MAX_CHARS = 140
MAX_ATTEMPTS = 3
EXCERPT_CHARS = 1800
SKIP_DIRS = {".agents", ".claude", ".git", "node_modules", "venv"}
BANNED_WORDS = re.compile(r"\b(portal|api|apis|terraform|cli)\b", re.IGNORECASE)
BANNED_CHARS = (":", "#", "/", "{", "}", "`", "[", "]", "|", "\u2014", "\u2013")

SYSTEM_PROMPT = """You write the meta description for one Gcore documentation page.
Return only the description sentence. No label, no quotes, no explanation.
Rules:
- One sentence, 140 characters maximum. Do not pad the sentence to reach the limit.
- Summarize what the page is about, using the feature name and words a person would type into search.
- Do not use the words Portal, API, Terraform, or CLI, even if the page title contains them.
- Do not use these characters: colon, hash, slash, curly braces, backticks, square brackets, pipe, em dash.
- Do not use you, your, this article, or learn how to.
- End with a period.
"""


@dataclass
class Article:
    """One documentation page selected for a description draft."""

    path: Path
    title: str
    headings: list[str]
    excerpt: str
    old_description: str


@dataclass
class Outcome:
    """Result of drafting one description."""

    relative_path: str
    status: str
    old_description: str
    new_description: str
    detail: str


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True, help="Repository root.")
    parser.add_argument("--workers", type=int, default=6, help="Parallel requests.")
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="JSONL report path. Defaults to .agents/research/seo-description-report.jsonl",
    )
    return parser.parse_args()


def iter_articles(repo: Path) -> list[Path]:
    """Return MDX files under the repo, excluding agent and research trees."""
    files: list[Path] = []
    for path in repo.rglob("*.mdx"):
        if any(part in SKIP_DIRS for part in path.relative_to(repo).parts):
            continue
        files.append(path)
    return sorted(files)


def split_frontmatter(text: str) -> tuple[str, str] | None:
    """Split a file into frontmatter and body.

    Returns None when the file does not open with a frontmatter block.
    """
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    # Include the closing marker line in the frontmatter slice end.
    newline = text.find("\n", end + 1)
    if newline == -1:
        return None
    return text[: newline + 1], text[newline + 1 :]


def frontmatter_value(frontmatter: str, key: str) -> str:
    """Return a single-line frontmatter value, without surrounding quotes."""
    match = re.search(rf"^{key}:[ \t]*(.*)$", frontmatter, flags=re.MULTILINE)
    if match is None:
        return ""
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def plain_text(markdown: str) -> str:
    """Drop MDX tags, code fences, and links so the model sees prose."""
    text = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    text = re.sub(r"^import\s+.+$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)]\([^)]*\)", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def load_article(path: Path) -> Article | None:
    """Read title, headings, and an opening excerpt from one MDX file."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    parts = split_frontmatter(text)
    if parts is None:
        return None
    frontmatter, body = parts
    title = frontmatter_value(frontmatter, "title")
    headings = [
        re.sub(r"[*_`]", "", item).strip()
        for item in re.findall(r"^#{2,3} +(.+)$", body, flags=re.MULTILINE)
    ]
    prose = plain_text(body)
    prose = re.sub(r"^#{1,6} .+$", " ", prose, flags=re.MULTILINE)
    prose = re.sub(r"\s+", " ", prose).strip()
    return Article(
        path=path,
        title=title,
        headings=headings[:12],
        excerpt=prose[:EXCERPT_CHARS],
        old_description=frontmatter_value(frontmatter, "description"),
    )


def clean_reply(raw: str) -> str:
    """Keep the first line of a model reply and drop a leading field label."""
    text = raw.strip()
    text = re.sub(r"^```[a-z]*\n?", "", text)
    text = text.replace("```", "")
    line = text.splitlines()[0].strip() if text else ""
    line = re.sub(r"^description:\s*", "", line, flags=re.IGNORECASE)
    if len(line) >= 2 and line[0] == line[-1] and line[0] in {'"', "'"}:
        line = line[1:-1].strip()
    line = re.sub(r"\s+", " ", line).strip()
    if line and not line.endswith(".") and len(line) < MAX_CHARS:
        line = f"{line}."
    return line


def validation_error(description: str) -> str:
    """Return a rule violation, or an empty string when the sentence is usable."""
    if not description:
        return "The description is empty."
    if len(description) < 40:
        return "The description is too short to summarize the article."
    if len(description) > MAX_CHARS:
        return f"The description is {len(description)} characters. The maximum is {MAX_CHARS}."
    if not description.endswith("."):
        return "The description must end with a period."
    if description.lower().startswith(("you ", "your ", "this article", "learn how")):
        return "Do not address the reader or describe the article."
    match = BANNED_WORDS.search(description)
    if match:
        return f"Do not use the word {match.group(0)}."
    for char in BANNED_CHARS:
        if char in description:
            return f"Do not use the character {char!r}."
    if '"' in description:
        return "Do not use double quotes."
    return ""


def build_user_prompt(article: Article, rejection: str) -> str:
    """Build the user message, including the previous rejection when retrying."""
    headings = "\n".join(f"- {item}" for item in article.headings) or "- none"
    prompt = (
        f"Path: {article.path.name}\n"
        f"Title: {article.title}\n"
        f"Headings:\n{headings}\n"
        f"Opening:\n{article.excerpt}"
    )
    if rejection:
        prompt += f"\n\nThe previous sentence was rejected: {rejection}\nWrite a new sentence."
    return prompt


def request_description(token: str, article: Article, rejection: str) -> str:
    """Call the gateway and return the assistant text."""
    payload = {
        "model": MODEL,
        "max_tokens": 2048,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(article, rejection)},
        ],
    }
    req = urllib.request.Request(
        GATEWAY_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"APIKey {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    message = data["choices"][0]["message"]
    content = message.get("content")
    if not isinstance(content, str) or not content.strip():
        reason = data["choices"][0].get("finish_reason")
        raise TimeoutError(f"empty content, finish_reason={reason}")
    return content


def request_with_retries(token: str, article: Article, rejection: str) -> str:
    """Call the gateway, backing off on rate limits and transient errors."""
    delay = 2.0
    last_error = ""
    for attempt in range(5):
        try:
            return request_description(token, article, rejection)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")[:300]
            last_error = f"HTTP {exc.code}: {body}"
            if exc.code not in {429, 500, 502, 503, 504}:
                raise RuntimeError(last_error) from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = str(exc)
        time.sleep(delay)
        delay = min(delay * 2, 30)
    raise RuntimeError(last_error or "gateway request failed")


def draft_description(token: str, article: Article) -> tuple[str, str]:
    """Return a valid description and an empty detail, or a failure detail."""
    rejection = ""
    last = ""
    for _ in range(MAX_ATTEMPTS):
        last = clean_reply(request_with_retries(token, article, rejection))
        rejection = validation_error(last)
        if not rejection:
            return last, ""
    return "", rejection or "The model did not return a usable sentence."


def write_description(path: Path, description: str) -> None:
    """Replace or insert the description line without changing other newlines."""
    with path.open("r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path} has no frontmatter")
    inserted = False
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            if not inserted:
                newline = "\r\n" if line.endswith("\r\n") else "\n"
                lines.insert(index, f"description: {description}{newline}")
            break
        if re.match(r"^description\s*:", line.lstrip("\ufeff")):
            newline = ""
            if line.endswith("\r\n"):
                newline = "\r\n"
            elif line.endswith("\n"):
                newline = "\n"
            lines[index] = f"description: {description}{newline}"
            inserted = True
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write("".join(lines))


def completed_paths(report_path: Path) -> set[str]:
    """Return paths already recorded as written, so a rerun can resume."""
    done: set[str] = set()
    if not report_path.exists():
        return done
    for line in report_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("status") == "written":
            done.add(row["path"])
    return done


def process_one(repo: Path, path: Path, token: str) -> Outcome:
    """Draft and, when valid, write one description."""
    relative = path.relative_to(repo).as_posix()
    article = load_article(path)
    if article is None:
        return Outcome(relative, "skipped", "", "", "no frontmatter")
    try:
        description, detail = draft_description(token, article)
    except RuntimeError as exc:
        return Outcome(relative, "failed", article.old_description, "", str(exc))
    if not description:
        return Outcome(relative, "failed", article.old_description, "", detail)
    if description == article.old_description:
        return Outcome(relative, "unchanged", article.old_description, description, "")
    write_description(path, description)
    return Outcome(relative, "written", article.old_description, description, "")


def append_report(report_path: Path, outcome: Outcome, lock: threading.Lock) -> None:
    """Append one JSONL row."""
    row = {
        "path": outcome.relative_path,
        "status": outcome.status,
        "old": outcome.old_description,
        "new": outcome.new_description,
        "detail": outcome.detail,
    }
    with lock:
        with report_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> None:
    """Draft descriptions for every article and write a JSONL report."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = parse_args()
    repo = args.repo.resolve()
    load_dotenv(repo / ".env", override=True)
    token = os.environ.get("PREPROD_API_KEY", "")
    if not token:
        raise SystemExit("PREPROD_API_KEY is not set")

    report_path = args.report or (repo / ".agents" / "research" / "seo-description-report.jsonl")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    done = completed_paths(report_path)
    files = [path for path in iter_articles(repo) if path.relative_to(repo).as_posix() not in done]
    log.info("articles to draft: %s (already written: %s)", len(files), len(done))

    lock = threading.Lock()
    counts = {"written": 0, "failed": 0, "skipped": 0, "unchanged": 0}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(process_one, repo, path, token) for path in files]
        for future in as_completed(futures):
            outcome = future.result()
            counts[outcome.status] = counts.get(outcome.status, 0) + 1
            append_report(report_path, outcome, lock)
            finished = sum(counts.values())
            if outcome.status == "failed":
                log.warning("%s failed: %s", outcome.relative_path, outcome.detail)
            if finished % 25 == 0 or finished == len(files):
                log.info("progress %s/%s %s", finished, len(files), counts)
    log.info("done %s", counts)
    log.info("report %s", report_path)


if __name__ == "__main__":
    main()
