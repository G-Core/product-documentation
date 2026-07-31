# Jira MCP — Reference

Instructions for using Jira MCP to fetch and process documentation tickets.
Load this file when a skill tells you to. Do not load it proactively.

---

## Project and ticket format

- **Project:** DOC
- **Ticket format:** `DOC-{number}` — e.g. `DOC-1030`, `DOC-1142`
- Tickets that do not start with `DOC-` are not documentation tickets — stop processing

---

## Key operations

```
jira_get_issue(issue_id)          — fetch full ticket with all fields and comments
jira_search(jql)                  — search tickets by JQL query
jira_get_linked_issues(issue_id)  — get tickets linked to this one
jira_add_comment(issue_id, text)  — add a comment to a ticket
jira_transition(issue_id, id)     — change ticket status (use transition IDs below)
```

---

## What to extract from a ticket

When fetching a ticket, collect:

| Field | Why |
|-------|-----|
| `summary` | The headline — what needs to be documented |
| `description` | Full context of the change |
| `status` | Determines if work can start — see status table below |
| `reporter` | Who created the ticket (SME or team contact) |
| `assignee` | Who is responsible |
| `labels` | May indicate product area or type |
| `linked issues` | Usually points to the dev ticket with technical details |
| `comments` | May contain blockers, updates, clarifications from SMEs |
| `attachments` | Screenshots, specs, Confluence links |

Read all comments — blockers and important clarifications often appear in comments,
not in the description.

---

## Status table

| Status | Category | Agent can work? |
|--------|----------|-----------------|
| Backlog | To Do | **YES** |
| To Do | To Do | **YES** |
| Reopened | To Do | **YES** — treat as To Do |
| In Progress | In Progress | NO — someone else is working |
| In Review | In Progress | NO — already submitted |
| Blocked | In Progress | NO — on hold |
| BLOCKED- Need Info | In Progress | NO — waiting for SME answer |
| In SEO review | In Progress | NO — treat as In Review |
| Done | Done | NO — already completed |
| Cancelled | Done | NO |

**If the status is not in the YES list — stop immediately.** Do not read the article,
do not make changes. Report the status and why work cannot start.

---

## Blocker detection in comments

Before starting work, scan all comments for:
- "wait for..." / "waiting for..."
- "not ready" / "on hold"
- "blocked by..." / "depends on..."
- "feature not released" / "not in production"
- Any indication work should not start yet

If blocking comments are found — stop and report to the user.

---

## Status transitions

### When to change status

| Event | New status | Transition ID |
|-------|-----------|---------------|
| Starting work on a ticket | In Progress | 11 (from To Do) |
| Need SME answer | BLOCKED- Need Info | 91 |
| Draft ready, PR created | In Review | 81 (from In Progress) |
| Ticket is not documentable | Cancelled | 131 |

### Full transition path (Backlog → In Review)

```
Backlog --[101]--> To Do --[11]--> In Progress --[81]--> In Review
```

**Rules:**
- Never change the status of a ticket that is not in To Do / Backlog
- Always add a comment when changing status — explain why
- Use "BLOCKED- Need Info" (not "Blocked") when waiting for answers
- Use @mention for the reporter or assignee when adding a blocking comment

---

## JQL queries

### Find tickets ready to work on

```jql
project = DOC
AND status IN (Backlog, "To Do", Reopened)
AND assignee IS EMPTY
ORDER BY created DESC
```

### Find all unfinished tickets

```jql
project = DOC
AND status NOT IN (Done, Cancelled)
ORDER BY updated DESC
```

### Find tickets waiting for info

```jql
project = DOC
AND status = "BLOCKED- Need Info"
ORDER BY updated DESC
```

### Search by keyword

```jql
project = DOC
AND text ~ "load balancer"
AND status IN (Backlog, "To Do")
ORDER BY created DESC
```

---

## Linked dev ticket

Most DOC tickets have a linked dev ticket (from engineering). Always fetch it:

1. Get linked issues from the DOC ticket
2. Find the link with type "is caused by" or "relates to" or "is blocked by"
3. Fetch that ticket to get technical details:
   - What changed in the product
   - Which API endpoints were added or modified
   - Which UI screens were affected
   - Acceptance criteria (most detailed technical spec)

Dev ticket stakeholders matter:
- If stakeholders are **only internal teams** (Team DX, DevOps, Support, Backend Team)
  → the change is likely not customer-facing → classify as INTERNAL_DOC or NOT_DOCUMENTABLE
- If stakeholders include customers or customer-facing teams → proceed with documentation

---

## Ticket classification (quick rules)

Before doing any documentation work, classify the ticket. Full classification logic is
in `.agents/skills/jira-context/SKILL.md`. Quick rules:

| Signal | Classification |
|--------|----------------|
| `[BUG]` in title (product bug, not doc typo) | BUG_FIX → cancel |
| `/admin/` API, internal stakeholders only | INTERNAL_DOC → cancel |
| Refactoring, library update, DB migration | NOT_DOCUMENTABLE → cancel |
| New feature visible to customers | PUBLIC_PRODUCT_DOC → proceed |
| Customer-visible error or troubleshooting | PUBLIC_TROUBLESHOOTING → proceed |
| Doc typo, grammar, outdated screenshot | PUBLIC_PRODUCT_DOC → update |
| `api-reference/` YAML file changes | NOT_DOCUMENTABLE → cancel (backend owns this) |
