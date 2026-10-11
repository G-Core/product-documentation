"""Evaluate documentation article quality using an LLM.

Sends the article content to an LLM and returns scores (1-10) on 11 criteria.
Target: average score >= 9.5 before sending the article for human review.

Supports two backends:
    openai    - uses OPENAI_API_KEY and --model (default: gpt-4o)
    deepseek  - uses DS_API_KEY, DS_API_URL, and DS_MODEL from .env

Usage:
    python .agents/tools/review_article_quality.py --article PATH/TO/article.mdx
    python .agents/tools/review_article_quality.py --article PATH/TO/article.mdx --dry-run
    python .agents/tools/review_article_quality.py --article PATH/TO/article.mdx --backend deepseek

    # Second iteration with conversation context (LLM sees its previous response):
    python .agents/tools/review_article_quality.py --article PATH/TO/article.mdx --history PATH/TO/history.json

Exit codes:
    0 - average score >= PASS_THRESHOLD
    1 - average score < PASS_THRESHOLD
    2 - error (missing file, API failure, etc.)
"""
import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path

# Force UTF-8 output on Windows regardless of the console code page.
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]

import openai
from dotenv import load_dotenv

log = logging.getLogger(__name__)

PASS_THRESHOLD = 9.5

MODEL_DEFAULT = "gpt-4o"
BACKEND_DEFAULT = "openai"

CRITERIA = [
    "Clarity for the reader",
    "Logical flow",
    "Structure",
    "Ease and smoothness of reading",
    "Transitions between ideas",
    "Relevance to the topic",
    "Completeness and content economy",
    "Errors and contradictions",
    "Practical value",
    "Stumble points",
    "Over-explanation",
]

SYSTEM_PROMPT = """\
You are an expert in technical documentation for enterprise/cloud products.
You evaluate technical documentation articles for a team of technical writers.

When scoring, apply the following editorial principles:

- An article may contain several independent tabs (for example, Customer Portal, REST API, Terraform). Evaluate each tab as a standalone guide. Multiple tabs are an architectural choice, not overload.
- Accordion, Tabs, Info, Tip, and Warning are documentation UI elements. Accordion content is supplementary and must not be treated as overload of the main scenario.
- If the article describes a wizard or a form, the document structure should follow the interface structure. Do not suggest moving information to other articles if the user cannot complete the current process without it.
- Technical terms such as SSH, API, SDK, Terraform, cloud-init, IPv4, CIDR, DHCP, and similar terms are not defects. Score only how clearly they are used.
- Do not suggest adding connective sentences between sequential instruction steps if the transition is already obvious from numbering or context.
- Do not suggest expanding explanations if the article deliberately links to dedicated documentation instead of duplicating it.
- Do not score documentation architecture (tab placement, section order, navigation method) unless the user explicitly asks for that.
- Repeated step structure in a how-to article is a strength, not mechanical writing: it helps the reader predict the next step.
- Do not lower the score because the article does not describe the product as a whole. It may be one article in a set.
- If a screenshot sits next to the text (Frame tag or img), treat the visual information as available to the reader. Do not require a verbal description of UI that is obvious from the screenshot.

Audience and explanation level:

- Assume the audience level matches the section of the article.
- Do not require explanations of basic tools and technologies that are prerequisites for the target audience: bash, curl, SSH, Python, Go, Terraform, RDP, cloud-init, REST API, environment variables, package managers, and similar concepts.
- A reader of a REST API or SDK section already has an API key, knows Project ID and Region ID, and is about to call the API. Explaining how to open a terminal makes the article worse.
- A reader of a Terraform section knows HCL and terraform init/apply/destroy.
- A reader of a Customer Portal section can sign in to the web interface and click buttons.

Information architecture:

- Each article solves one task. Do not require a self-contained guide that covers every related topic.
- Links to neighboring articles are intentional architecture, not a gap. Do not mark them as missing information.
- Do not require an article about creating a resource to also include a full guide to connecting, monitoring, or deleting it. Separate articles exist for that.
"""

FOLLOWUP_PROMPT_TEMPLATE = """\
In your previous evaluation you found issues and scored the article below 9.5.
The article was then revised.

Below is the revised version of the same article.
Score it again on the same 11 criteria.
Pay special attention to whether the issues from the previous evaluation are gone.
Do not lower scores for problems that have already been fixed.

Revised article:

{article_text}
"""

PROMPT_TEMPLATE = """\
Evaluate each article as a standalone document, as if reading it for the first time.

Give scores from 1 to 10 on the following criteria:

Clarity for the reader - is it clear what the article explains and what the reader must do.
Logical flow - sequence of ideas, no logical gaps.
Structure - quality of sections, headings, lists, tables, and the order of information.
Ease and smoothness of reading - natural language, no robotic tone, unjustified boilerplate, mechanical repetition, tautology, or obsessive reuse of the same words or constructions. Do not treat a repeated pattern as a defect by itself: if the same structure improves navigation and matches the document type, that is a strength.
Transitions between ideas - smooth movement between paragraphs and sections, no abrupt jumps.
Relevance to the topic - does the article answer the stated topic and stay on it.
Completeness and content economy - is there enough information to complete the task, with no important gaps. Also score whether the same information is duplicated across sections, and whether some sections should be shortened or replaced with a link to existing documentation.
Errors and contradictions - typos and terminological, factual, logical, or meaning mismatches.
Practical value - does the article help the user complete the task.
Stumble points - places where the reader slows down, rereads a sentence, or loses the thread.
Over-explanation - extra explanations, repeats, redundant lists, or details that add no practical value.

Response format:

1. Start with a scores table:

| Criterion | Score |
|----------|--------|
| Clarity for the reader | X |
| Logical flow | X |
| Structure | X |
| Ease and smoothness of reading | X |
| Transitions between ideas | X |
| Relevance to the topic | X |
| Completeness and content economy | X |
| Errors and contradictions | X |
| Practical value | X |
| Stumble points | X |
| Over-explanation | X |

2. Immediately after the table, one line: **Average score: X.X / 10**

3. Then a breakdown for every criterion that lost at least 1 point (score below 10). For each such criterion:
   - Put its name in bold.
   - Quote the specific fragment from the article (a quotation or exact location) that caused the lower score.
   - Explain the problem in one or two sentences.
   - If a criterion scored 10, do not mention it at all.

Do not describe strengths. Do not give generic advice unattached to the article text.
Score from the point of view of a real user, not a literary editor.
Do not propose changes that only alter style without a noticeable gain in clarity or practical use.
If a remark is subjective or depends on house style, do not treat it as a defect.

---

Article to evaluate:

{article_text}
"""


def _build_client(backend: str, model_override: str | None) -> tuple["openai.OpenAI", str]:
    """Return an OpenAI-compatible client and resolved model name.

    Args:
        backend: "openai" or "deepseek".
        model_override: Explicit model name from --model flag, or None to use defaults.

    Returns:
        Tuple of (client, model_name).

    Raises:
        SystemExit: If required environment variables are missing.
    """
    load_dotenv()

    if backend == "deepseek":
        api_key = os.environ.get("DS_API_KEY")
        base_url = os.environ.get("DS_API_URL")
        model = model_override or os.environ.get("DS_MODEL")
        missing = [k for k, v in [("DS_API_KEY", api_key), ("DS_API_URL", base_url), ("DS_MODEL", model)] if not v]
        if missing:
            log.error("Missing environment variables for DeepSeek backend: %s", ", ".join(missing))
            sys.exit(2)
        client = openai.OpenAI(api_key=api_key, base_url=base_url)
        return client, model  # type: ignore[return-value]

    # openai backend
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log.error("OPENAI_API_KEY not set in environment or .env file.")
        sys.exit(2)
    model = model_override or MODEL_DEFAULT
    return openai.OpenAI(api_key=api_key), model


def _strip_mdx(raw: str) -> str:
    """Remove MDX/JSX noise from article text before sending to LLM.

    Keeps prose, headings, lists, and table content.
    Removes: frontmatter, fenced code blocks, import statements,
    JSX component tags (but keeps their inner text), image tags.
    """
    text = raw

    # Strip UTF-8 BOM if present
    text = text.lstrip("\ufeff")

    # Strip frontmatter (--- ... ---)
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)

    # Strip import statements
    text = re.sub(r"^import .+$", "", text, flags=re.MULTILINE)

    # Strip fenced code blocks entirely (they are not documentation prose)
    text = re.sub(r"```[\s\S]*?```", "[code block omitted]", text)

    # Strip <img ...> tags completely
    text = re.sub(r"<img[^>]*/?>", "", text)

    # Strip <Frame>, <Accordion>, <MethodSwitch>, <MethodSection>, <Tabs>, <Tab>
    # opening/closing tags but keep content between them
    text = re.sub(
        r"<(Frame|Accordion|MethodSwitch|MethodSection|Tabs|Tab|Info|Warning|Note|Tip)"
        r"(\s[^>]*)?>",
        "",
        text,
    )
    text = re.sub(
        r"</(Frame|Accordion|MethodSwitch|MethodSection|Tabs|Tab|Info|Warning|Note|Tip)>",
        "",
        text,
    )

    # Strip <p> wrappers but keep content
    text = re.sub(r"<p>|</p>", "", text)

    # Collapse 3+ consecutive blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def _parse_scores(response_text: str) -> dict[str, float]:
    """Extract criterion scores from LLM response table.

    Returns a dict mapping criterion name to score, or empty dict if parsing fails.
    """
    scores: dict[str, float] = {}
    for criterion in CRITERIA:
        pattern = rf"\|\s*{re.escape(criterion)}\s*\|\s*(\d+(?:\.\d+)?)\s*\|"
        match = re.search(pattern, response_text)
        if match:
            scores[criterion] = float(match.group(1))
    return scores


def _format_summary(scores: dict[str, float], response_text: str) -> str:
    """Format a human-readable summary of scores and remarks."""
    lines = []

    # LLM response first - the main thing to read
    lines.append("=" * 60)
    lines.append("LLM EVALUATION")
    lines.append("=" * 60)
    lines.append("")
    lines.append(response_text)

    # Parsed score summary at the end
    lines.append("")
    lines.append("=" * 60)
    lines.append("PARSED SCORES")
    lines.append("=" * 60)

    if scores:
        avg = sum(scores.values()) / len(scores)
        lines.append("")
        lines.append(f"{'Criterion':<40} {'Score':>5}")
        lines.append("-" * 47)
        for criterion, score in scores.items():
            marker = "  <--" if score < 9 else ""
            lines.append(f"{criterion:<40} {score:>5.1f}{marker}")
        lines.append("-" * 47)
        lines.append(f"{'Average':<40} {avg:>5.2f}")
        lines.append("")
        status = "PASS" if avg >= PASS_THRESHOLD else "FAIL"
        lines.append(f"Result: {status} (threshold: {PASS_THRESHOLD})")
    else:
        lines.append("WARNING: could not parse scores from LLM response.")

    return "\n".join(lines)


def _load_history(history_path: Path) -> list[dict]:
    """Load conversation history from a JSON file.

    Args:
        history_path: Path to the history JSON file.

    Returns:
        List of message dicts, or empty list if file does not exist.
    """
    if not history_path.exists():
        return []
    try:
        return json.loads(history_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        log.warning("Could not load history file %s: %s", history_path, exc)
        return []


def _save_history(history_path: Path, messages: list[dict]) -> None:
    """Save conversation history to a JSON file.

    Args:
        history_path: Path to write the history JSON file.
        messages: List of message dicts to persist.
    """
    try:
        history_path.write_text(
            json.dumps(messages, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as exc:
        log.warning("Could not save history file %s: %s", history_path, exc)


def review_article(
    article_path: Path,
    model: str,
    dry_run: bool,
    backend: str = BACKEND_DEFAULT,
    history_path: Path | None = None,
) -> int:
    """Run quality review for a single article.

    When history_path is provided and the file exists, the previous LLM
    evaluation is included as conversation context so the model can assess
    whether issues from the prior iteration have been resolved.

    Args:
        article_path: Path to the MDX article file.
        model: Model identifier override (empty string uses backend default).
        dry_run: If True, print the prompt without calling the API.
        backend: "openai" or "deepseek".
        history_path: Optional path to a JSON file for storing conversation
            history between iterations.

    Returns:
        Exit code: 0 for pass, 1 for fail, 2 for error.
    """
    if not article_path.exists():
        log.error("Article not found: %s", article_path)
        return 2

    raw = article_path.read_text(encoding="utf-8")
    article_text = _strip_mdx(raw)

    model_override = model if model else None

    # Build message list, incorporating history when available.
    prior_messages = _load_history(history_path) if history_path else []
    is_followup = bool(prior_messages)

    if is_followup:
        # Second (or later) iteration: append a follow-up prompt to the
        # existing conversation so the LLM knows what changed.
        user_content = FOLLOWUP_PROMPT_TEMPLATE.format(article_text=article_text)
        messages = prior_messages + [{"role": "user", "content": user_content}]
        log.info("Continuing conversation from %s (%d prior messages)", history_path, len(prior_messages))
    else:
        # First iteration: build a fresh conversation.
        user_content = PROMPT_TEMPLATE.format(article_text=article_text)
        messages = [{"role": "user", "content": user_content}]

    if dry_run:
        load_dotenv()
        if backend == "deepseek":
            resolved_model = model_override or os.environ.get("DS_MODEL", "DS_MODEL not set")
        else:
            resolved_model = model_override or MODEL_DEFAULT
        iteration_label = "follow-up" if is_followup else "first"
        print(f"DRY RUN - would send {iteration_label} prompt to the LLM:")
        print("-" * 60)
        print(messages[-1]["content"][:2000], "..." if len(messages[-1]["content"]) > 2000 else "")
        print(f"\nArticle: {article_path}")
        print(f"Backend: {backend}")
        print(f"Model: {resolved_model}")
        print(f"Total messages in conversation: {len(messages)}")
        return 0

    client, resolved_model = _build_client(backend, model_override)

    iteration_label = "follow-up" if is_followup else "first"
    log.info(
        "Sending %s request to %s (%s) for quality review...",
        iteration_label,
        resolved_model,
        backend,
    )
    response = client.chat.completions.create(
        model=resolved_model,
        max_tokens=4096,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
    )

    response_text = response.choices[0].message.content or ""
    scores = _parse_scores(response_text)
    summary = _format_summary(scores, response_text)

    print(summary)

    # Persist updated conversation history for the next iteration.
    if history_path:
        updated_messages = messages + [{"role": "assistant", "content": response_text}]
        _save_history(history_path, updated_messages)
        log.info("Conversation history saved to %s", history_path)

    if not scores:
        return 2

    avg = sum(scores.values()) / len(scores)
    return 0 if avg >= PASS_THRESHOLD else 1


def main() -> None:
    """Entry point."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="Evaluate documentation article quality using an LLM.",
    )
    parser.add_argument(
        "--article",
        required=True,
        type=Path,
        help="Path to the MDX article file to evaluate.",
    )
    parser.add_argument(
        "--backend",
        default=BACKEND_DEFAULT,
        choices=["openai", "deepseek"],
        help=f"LLM backend to use (default: {BACKEND_DEFAULT}). "
             "deepseek reads DS_API_KEY, DS_API_URL, DS_MODEL from .env.",
    )
    parser.add_argument(
        "--model",
        default="",
        help="Model name override. For openai defaults to gpt-4o; "
             "for deepseek defaults to DS_MODEL from .env.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt without calling the API.",
    )
    parser.add_argument(
        "--history",
        default=None,
        type=Path,
        help=(
            "Path to a JSON file for storing conversation history between iterations. "
            "On the first run the file is created. On subsequent runs the previous "
            "LLM response is included as context so the model can assess whether "
            "issues from the prior iteration have been resolved. "
            "Example: --history /tmp/review-history.json"
        ),
    )
    args = parser.parse_args()

    exit_code = review_article(args.article, args.model, args.dry_run, args.backend, args.history)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
