"""Create a Jira ticket.

Usage:
    python .agents/tools/create_jira_ticket.py --summary "..." --description "..."
    python .agents/tools/create_jira_ticket.py --summary "..." --description-file ticket.txt --dry-run

Optional:
    --project     Jira project key (default: DOC)
    --epic        Epic Link key. Optional: only when the user names an epic for this batch
    --description-file  Read the description from a UTF-8 file (use for long, multi-line text)
    --dry-run     Print the ticket fields and exit without calling Jira
    --org-unit    Org unit field ID (default: 16037 = Edge Network, DOC project only)
    --issuetype   Issue type ID (default: 12504)
    --link-to     Issue key to create a "relates to" link (e.g. DOC-1349)
"""
import argparse
import json
import logging
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv

log = logging.getLogger(__name__)

JIRA_BASE = "https://jira.gcore.lu"


def _get_token() -> str:
    load_dotenv()
    return os.environ["JIRA_MCP_TOKEN"]


def _jira_request(
    method: str, path: str, token: str, payload: dict | None = None
) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers: dict[str, str] = {"Authorization": f"Bearer {token}"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(
        f"{JIRA_BASE}{path}",
        data=data,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            log.debug("HTTP %d %s", resp.status, body[:200])
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read()
        log.error("HTTP %d from %s: %s", exc.code, path, body[:400])
        raise


def create_ticket(
    summary: str,
    description: str,
    epic: str = "",
    org_unit: str = "16037",
    issuetype: str = "12504",
    assignee: str | None = None,
    project: str = "DOC",
    labels: list[str] | None = None,
) -> str:
    """Create a Jira issue and return its key."""
    token = _get_token()
    fields: dict = {
        "project": {"key": project},
        "issuetype": {"id": issuetype},
        "summary": summary,
        "description": description,
    }
    # org-unit field is DOC-project-specific
    if project == "DOC" and org_unit:
        fields["customfield_14411"] = {"id": org_unit}
    if epic:
        fields["customfield_10500"] = epic
    if assignee:
        fields["assignee"] = {"name": assignee}
    if labels:
        fields["labels"] = labels
    result = _jira_request("POST", "/rest/api/2/issue", token, {"fields": fields})
    return result["key"]


def link_issues(source_key: str, target_key: str, link_type: str = "Relates") -> None:
    """Create a 'relates to' link between two Jira issues."""
    token = _get_token()
    payload = {
        "type": {"name": link_type},
        "inwardIssue": {"key": source_key},
        "outwardIssue": {"key": target_key},
    }
    _jira_request("POST", "/rest/api/2/issueLink", token, payload)


def get_transitions(key: str) -> dict[str, str]:
    """Return available transitions for an issue as {name: id}."""
    token = _get_token()
    result = _jira_request("GET", f"/rest/api/2/issue/{key}/transitions", token)
    return {t["name"]: t["id"] for t in result.get("transitions", [])}


def transition_issue(key: str, transition_name: str) -> None:
    """Transition an issue by name (case-insensitive substring match).

    Args:
        key: Jira issue key, e.g. ``DOC-1545``.
        transition_name: Full or partial transition name, e.g. ``"In Progress"``.

    Raises:
        ValueError: If no transition matching ``transition_name`` is found.
    """
    token = _get_token()
    transitions = get_transitions(key)
    match = next(
        (tid for name, tid in transitions.items() if transition_name.lower() in name.lower()),
        None,
    )
    if match is None:
        raise ValueError(
            f"Transition '{transition_name}' not found for {key}. "
            f"Available: {list(transitions.keys())}"
        )
    _jira_request(
        "POST",
        f"/rest/api/2/issue/{key}/transitions",
        token,
        {"transition": {"id": match}},
    )
    log.info("Transitioned %s via '%s' (id=%s)", key, transition_name, match)


def add_comment(key: str, body: str) -> None:
    """Add a plain-text comment to a Jira issue."""
    token = _get_token()
    _jira_request("POST", f"/rest/api/2/issue/{key}/comment", token, {"body": body})
    log.info("Comment added to %s", key)


def create_and_link(
    summary: str,
    description: str,
    epic: str = "",
    org_unit: str = "16037",
    issuetype: str = "12504",
    link_to: str | None = None,
    assignee: str | None = None,
    project: str = "DOC",
    labels: list[str] | None = None,
) -> str:
    """Create a ticket and optionally link it to another issue. Returns the new key."""
    key = create_ticket(
        summary, description, epic, org_unit, issuetype, assignee, project, labels
    )
    url = f"{JIRA_BASE}/browse/{key}"
    if link_to:
        link_issues(key, link_to)
        return f"{key} - {url} (linked to {link_to})"
    return f"{key} - {url}"


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Create a Jira ticket.")
    parser.add_argument("--summary", required=True, help="Ticket summary")
    parser.add_argument("--description", default="", help="Ticket description")
    parser.add_argument("--description-file", default=None, help="Read the description from this UTF-8 file")
    parser.add_argument("--project", default="DOC", help="Jira project key (default: DOC)")
    parser.add_argument("--epic", default="", help="Epic Link key. Optional: only when the user names an epic for this batch")
    parser.add_argument("--org-unit", default="16037", help="Org unit field ID (DOC project only)")
    parser.add_argument("--issuetype", default="12504", help="Issue type ID")
    parser.add_argument("--link-to", default=None, help="Issue key to link as 'relates to'")
    parser.add_argument("--assignee", default="sergey.kostichev@gcore.lu", help="Jira username to assign the ticket to (default: the documentation writer)")
    parser.add_argument("--label", action="append", default=[], help="Jira label. Repeat to add more than one.")
    parser.add_argument("--dry-run", action="store_true", help="Print the ticket fields without calling Jira")
    args = parser.parse_args()

    description = args.description
    if args.description_file:
        with open(args.description_file, encoding="utf-8") as fh:
            description = fh.read()
    if not description:
        parser.error("provide --description or --description-file")

    if args.dry_run:
        print("DRY RUN - ticket would be created with:")
        print(f"  Project:     {args.project}")
        print(f"  Summary:     {args.summary}")
        print(f"  Epic:        {args.epic}")
        print(f"  Org unit:    {args.org_unit}")
        print(f"  Issue type:  {args.issuetype}")
        print(f"  Assignee:    {args.assignee}")
        print(f"  Link to:     {args.link_to}")
        print(f"  Labels:      {args.label}")
        print("  Description:")
        print(description)
        return

    result = create_and_link(
        summary=args.summary,
        description=description,
        epic=args.epic or "",
        org_unit=args.org_unit,
        issuetype=args.issuetype,
        assignee=args.assignee,
        link_to=args.link_to,
        project=args.project,
        labels=args.label,
    )
    print(f"Created: {result}")


if __name__ == "__main__":
    main()
