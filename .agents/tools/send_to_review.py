"""Transition a Jira ticket To Do -> In Progress -> In Review (or Blocked) and post a comment.

Usage:
    python .agents/tools/send_to_review.py --ticket DOC-1234 --branch DOC-1234 --article-path cdn/create-a-cdn-resource
    python .agents/tools/send_to_review.py --ticket DOC-1234 --branch DOC-1234 --article-path cdn/x --blocked "reason"
    Add --dry-run to print the plan without calling Jira.

Idempotent: if the ticket is already In Review or Blocked, no transitions are applied.
A comment is still posted (with the preview URL) so the reviewer sees the latest link.
"""
import argparse
import json
import logging
import os
import re
import sys
import urllib.request

from create_jira_ticket import add_comment, transition_issue

log = logging.getLogger(__name__)
JIRA_BASE = "https://jira.gcore.lu"


def _get_ticket_status(ticket: str) -> str:
    """Return the current status name of a Jira ticket (e.g. 'In Review', 'To Do')."""
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.environ.get("JIRA_MCP_TOKEN", os.environ.get("JIRA_API_KEY", ""))
    url = f"{JIRA_BASE}/rest/api/2/issue/{ticket}?fields=status"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    return data["fields"]["status"]["name"]


def _mintlify_url(branch: str, article_path: str) -> str:
    return f"https://gcore-{branch.lower()}.mintlify.app/{article_path}"


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(
        description="Transition a Jira ticket to In Review (or Blocked) and post a comment."
    )
    parser.add_argument("--ticket", required=True, help="Jira ticket key, e.g. DOC-1234")
    parser.add_argument("--branch", required=True, help="Git branch name used for the Mintlify preview URL")
    parser.add_argument("--article-path", required=True, help="Article path without extension, e.g. cdn/create-a-cdn-resource")
    parser.add_argument("--blocked", default="", metavar="REASON", help="Move the ticket to Blocked with this reason instead of In Review")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be done without calling the Jira API")
    args = parser.parse_args()

    TICKET = args.ticket
    BLOCKED = bool(args.blocked)
    BLOCKED_REASON = args.blocked
    preview_url = _mintlify_url(args.branch, args.article_path)

    if BLOCKED:
        target_status = "Blocked"
        comment_body = (
            f"Blocked - portal verification incomplete.\n\n"
            f"Reason: {BLOCKED_REASON}\n\n"
            f"Changes pushed. Preview:\n{preview_url}"
        )
        transitions = ["Blocked"]
    else:
        target_status = "In Review"
        comment_body = f"Please review\n\n{preview_url}"
        transitions = ["To Do", "Start Progress", "Review"]

    if args.dry_run:
        log.info("DRY RUN - would perform:")
        log.info("  Ticket:      %s", TICKET)
        log.info("  Transitions: %s", " -> ".join(transitions))
        log.info("  Status:      %s", target_status)
        log.info("  Comment:     %s", comment_body)
        return

    try:
        current_status = _get_ticket_status(TICKET)
        log.info("Current ticket status: %s", current_status)

        if current_status == target_status:
            log.info("Ticket %s is already %s - skipping transitions.", TICKET, target_status)
        else:
            for t in transitions:
                transition_issue(TICKET, t)

        add_comment(TICKET, comment_body)
        log.info("Done: %s is now %s. Preview: %s", TICKET, target_status, preview_url)
    except Exception as exc:
        log.error("Failed: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()


