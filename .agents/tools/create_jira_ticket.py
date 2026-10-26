"""Create a Jira ticket on https://gcore.atlassian.net.

Usage:
    python .agents/tools/create_jira_ticket.py --summary "..." --description "..."
    python .agents/tools/create_jira_ticket.py --summary "..." --description-file ticket.txt --dry-run

Optional:
    --project     Jira project key (default: DOC)
    --epic        Epic link key. Optional: only when the user names an epic for this batch
    --description-file  Read the description from a UTF-8 file (use for long, multi-line text)
    --dry-run     Print the ticket fields and exit without calling Jira
    --org-unit    Org unit field ID (default: 11816 = Edge Network, DOC project only)
    --issuetype   Issue type ID (default: 10330)
    --link-to     Issue key to create a "relates to" link (e.g. DOC-1349)

Authentication comes from JIRA_CLOUD_EMAIL and JIRA_CLOUD_API_TOKEN.
JIRA_CLOUD_URL overrides the site. The default site is https://gcore.atlassian.net.
"""
import argparse
import base64
import json
import logging
import os
import urllib.error
import urllib.parse
import urllib.request

from dotenv import load_dotenv

log = logging.getLogger(__name__)

DEFAULT_SITE = "https://gcore.atlassian.net"
ORG_UNIT_FIELD = "customfield_10675"
EPIC_LINK_FIELD = "customfield_10014"
DEFAULT_ORG_UNIT = "11816"
DEFAULT_ISSUE_TYPE = "10330"


def jira_base() -> str:
    """Return the Jira site URL without a trailing slash."""
    load_dotenv()
    return os.environ.get("JIRA_CLOUD_URL", DEFAULT_SITE).rstrip("/")


def _auth_header() -> str:
    """Build the Basic auth header for the Atlassian Cloud API."""
    load_dotenv()
    email = os.environ.get("JIRA_CLOUD_EMAIL", "")
    token = os.environ.get("JIRA_CLOUD_API_TOKEN", "")
    if not email or not token:
        raise RuntimeError(
            "JIRA_CLOUD_EMAIL and JIRA_CLOUD_API_TOKEN are required"
        )
    encoded = base64.b64encode(f"{email}:{token}".encode()).decode("ascii")
    return f"Basic {encoded}"


def jira_request(
    method: str, path: str, payload: dict | list | None = None
) -> dict | list:
    """Send one Jira REST request and return the decoded JSON body."""
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers: dict[str, str] = {
        "Authorization": _auth_header(),
        "Accept": "application/json",
    }
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(
        f"{jira_base()}{path}",
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


def _account_id(identifier: str) -> str:
    """Resolve an email address to an Atlassian account id.

    An identifier without @ is returned unchanged, so a caller can pass an
    account id directly.
    """
    if "@" not in identifier:
        return identifier
    query = urllib.parse.quote(identifier)
    users = jira_request("GET", f"/rest/api/3/user/search?query={query}")
    if not isinstance(users, list):
        raise RuntimeError("Jira user search did not return a list")
    wanted = identifier.lower()
    for user in users:
        if str(user.get("emailAddress", "")).lower() == wanted:
            account_id = user.get("accountId")
            if account_id:
                return str(account_id)
    raise RuntimeError(f"No Jira user found for {identifier}")


def create_ticket(
    summary: str,
    description: str,
    epic: str = "",
    org_unit: str = DEFAULT_ORG_UNIT,
    issuetype: str = DEFAULT_ISSUE_TYPE,
    assignee: str | None = None,
    project: str = "DOC",
    labels: list[str] | None = None,
) -> str:
    """Create a Jira issue and return its key."""
    fields: dict = {
        "project": {"key": project},
        "issuetype": {"id": issuetype},
        "summary": summary,
        "description": description,
    }
    if project == "DOC" and org_unit:
        fields[ORG_UNIT_FIELD] = {"id": org_unit}
    if epic:
        fields[EPIC_LINK_FIELD] = epic
    if assignee:
        fields["assignee"] = {"accountId": _account_id(assignee)}
    if labels:
        fields["labels"] = labels
    result = jira_request("POST", "/rest/api/2/issue", {"fields": fields})
    if not isinstance(result, dict) or "key" not in result:
        raise RuntimeError("Jira did not return an issue key")
    return str(result["key"])


def link_issues(source_key: str, target_key: str, link_type: str = "Relates") -> None:
    """Create a 'relates to' link between two Jira issues."""
    payload = {
        "type": {"name": link_type},
        "inwardIssue": {"key": source_key},
        "outwardIssue": {"key": target_key},
    }
    jira_request("POST", "/rest/api/2/issueLink", payload)


def get_transitions(key: str) -> dict[str, str]:
    """Return available transitions for an issue as {name: id}."""
    result = jira_request("GET", f"/rest/api/2/issue/{key}/transitions")
    if not isinstance(result, dict):
        raise RuntimeError("Jira did not return transitions")
    return {t["name"]: t["id"] for t in result.get("transitions", [])}


def transition_issue(key: str, transition_name: str) -> None:
    """Transition an issue by name (case-insensitive substring match).

    Args:
        key: Jira issue key, e.g. ``DOC-1545``.
        transition_name: Full or partial transition name, e.g. ``"In Progress"``.

    Raises:
        ValueError: If no transition matching ``transition_name`` is found.
    """
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
    jira_request(
        "POST",
        f"/rest/api/2/issue/{key}/transitions",
        {"transition": {"id": match}},
    )
    log.info("Transitioned %s via '%s' (id=%s)", key, transition_name, match)


def add_comment(key: str, body: str) -> None:
    """Add a plain-text comment to a Jira issue."""
    jira_request("POST", f"/rest/api/2/issue/{key}/comment", {"body": body})
    log.info("Comment added to %s", key)


def create_and_link(
    summary: str,
    description: str,
    epic: str = "",
    org_unit: str = DEFAULT_ORG_UNIT,
    issuetype: str = DEFAULT_ISSUE_TYPE,
    link_to: str | None = None,
    assignee: str | None = None,
    project: str = "DOC",
    labels: list[str] | None = None,
) -> str:
    """Create a ticket and optionally link it to another issue. Returns the new key."""
    key = create_ticket(
        summary, description, epic, org_unit, issuetype, assignee, project, labels
    )
    url = f"{jira_base()}/browse/{key}"
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
    parser.add_argument("--epic", default="", help="Epic link key. Optional: only when the user names an epic for this batch")
    parser.add_argument("--org-unit", default=DEFAULT_ORG_UNIT, help="Org unit field ID (DOC project only)")
    parser.add_argument("--issuetype", default=DEFAULT_ISSUE_TYPE, help="Issue type ID")
    parser.add_argument("--link-to", default=None, help="Issue key to link as 'relates to'")
    parser.add_argument("--assignee", default="sergey.kostichev@gcore.com", help="Atlassian account email to assign the ticket to (default: the documentation writer)")
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
        print(f"  Site:        {jira_base()}")
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
