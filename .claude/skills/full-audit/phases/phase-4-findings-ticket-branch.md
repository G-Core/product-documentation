# Phase 4 — Findings summary and Jira ticket

After completing Phase 2, present all findings to the user as a numbered list
grouped by category.

Also present:
- Total number of findings
- List of prerequisites noted, with article paths where available
- List of screenshots that need replacement, with old and new filenames
- Any steps where the feature was unavailable (UNVERIFIED)

## Create the Jira ticket immediately after presenting findings

Do not wait for the user to ask. Create the ticket now, while the findings are
fresh and before any fixes are applied.

**If a Jira ticket already exists for this article** (e.g. the article is being
redone after a partial run), do NOT create a duplicate ticket. Use the existing
ticket number and continue directly to Phase 5.

Follow `.agents/references/ticket-and-branch.md` to create the ticket. Write the description to `$env:TEMP\ticket-description.txt` in the format from `../finding-formats.md` ("Jira ticket description"). Use `--summary "Update {article title}"` and take the other values from Phase 0 routing:

- `--org-unit` — `jira_org_unit`

Do not pass `--epic`, `--link-to`, or `--assignee`: no epic is set unless the user names one for the current batch, and the assignee is the script default.

Run with `--dry-run` first, show the output to the user, then run without it immediately after. Do not wait for separate confirmation unless the user objects.

**What belongs in the description — every finding in full.**

Copy the full FINDING blocks from Phase 2 verbatim. Do not summarise, shorten,
or paraphrase. The description must read as a complete audit report so that
anyone opening the ticket understands the exact scope of work without
reading the article or the portal.

Group findings by category, include the finding number, location, "Article says",
"Portal shows", and "Action needed" for each one. This is the same format used
in Phase 2 — reproduce it exactly.

**Do NOT include in the description:**
- Style guide micro-fixes (Phase 6)
- MDX structure and encoding issues (Phases 7 and 9)
- CRLF/LF, BOM, or p-tag cleanup

Report the created ticket key and URL to the user. Record the ticket key — it is needed in Phases 9 and 10.

## Create the feature branch immediately after the ticket

Do not wait until Phase 9. Create the branch now, so all subsequent edits land on the feature branch and never on `main`. Follow `.agents/references/ticket-and-branch.md` (`create_branch.ps1` with the ticket key just returned).

Immediately proceed to Phase 5 without asking for confirmation.
