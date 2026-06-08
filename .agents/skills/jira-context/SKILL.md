---
name: jira-context
description: Analyze a Jira ticket and produce a structured brief of what needs
to be documented. Load when given a Jira ticket ID or URL and asked to understand
what work is needed.
---

Fetch a Jira ticket, determine whether documentation work is needed, classify
the type of change, find the affected article, and produce a clear brief.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/mcp-tools/setup.md` — verify Jira MCP is available first
3. `.agents/references/mcp-tools/jira.md` — Jira operations and status reference
4. `.agents/references/mcp-tools/confluence.md` — only if Jira ticket links to Confluence pages

Do not read article files during this skill. This skill produces a brief —
it does not make changes to documentation.

---

## Phase 1 — Verify MCP and fetch ticket

**Step 1.** Check that Jira MCP is available. If not — follow the instructions
in `.agents/references/mcp-tools/setup.md` and stop.

**Step 2.** Validate the ticket key format: must start with `DOC-` followed by numbers.
If the format is wrong — tell the user and stop.

**Step 3.** Fetch the ticket:
- Summary, description, status, reporter, assignee, labels
- All comments — read every one, blockers often appear here
- All linked issues — fetch the linked dev ticket if present

**Step 4.** Fetch the linked dev ticket (if exists):
- Description and acceptance criteria — most detailed technical spec
- Stakeholders field — critical for classification
- Any linked Confluence pages — fetch if present

---

## Phase 2 — Status check

Check the ticket status against this table:

| Status | Can work? |
|--------|-----------|
| Backlog | YES |
| To Do | YES |
| Reopened | YES |
| In Progress | NO — someone else is working |
| In Review | NO — already submitted for review |
| Blocked | NO — on hold |
| BLOCKED- Need Info | NO — waiting for SME answer |
| In SEO review | NO — treat as In Review |
| Done | NO — already completed |
| Cancelled | NO |

**If status is not in the YES list — stop immediately.**

Report to the user:
```
Ticket: [TICKET-ID]
Status: [status]
Cannot start: [reason]
```

**Also scan all comments** for blocking signals before proceeding:
- "wait for..." / "waiting for..."
- "not ready" / "on hold"
- "feature not released" / "not in production"
- "blocked by..." / "depends on..."

If any blocking signal found — stop and report to the user.

---

## Phase 3 — Classify the ticket

Classification determines whether documentation work is allowed.
**Do not write or search for articles until classification is complete.**

### The primary test: Customer Decision & Planning

Ask: does knowing about this change help a customer do any of the following?

- [ ] Choose between product options or configurations
- [ ] Plan their architecture, resources, or costs
- [ ] Set correct expectations about system behavior
- [ ] Compare Gcore capabilities with alternatives
- [ ] Make operational decisions (monitoring, scaling, troubleshooting)

If **any box is checked** → likely PUBLIC_PRODUCT_DOC. Continue to category check.
If **none checked** → likely NOT_DOCUMENTABLE or INTERNAL_DOC. Verify with the rules below.

### Categories

**PUBLIC_PRODUCT_DOC** — document this
- New feature or change in the Customer Portal
- New public API endpoint customers can use
- Changed UI workflow, renamed element, new field
- New pricing tier, limit, or quota
- Automatic feature that affects performance, reliability, or planning decisions
- Documentation error (typo, wrong command, outdated screenshot) — always update

**PUBLIC_TROUBLESHOOTING** — document this
- Error message customers encounter and can troubleshoot
- Common mistake and how to fix it
- Workaround for a known limitation

**BUG_FIX** — cancel, do not document
- Ticket title contains `[BUG]` AND describes fixing broken product behavior
- Exception: if the bug is a documentation error (wrong text, broken link) → treat as PUBLIC_PRODUCT_DOC

**INTERNAL_DOC** — cancel, do not document
- Admin APIs (`/admin/v1/...`)
- Internal billing processes
- Features for internal teams (Team DX, DevOps, Support)
- Stakeholders in dev ticket are internal-only

**NOT_DOCUMENTABLE** — cancel, do not document
- Code refactoring, library update, infrastructure migration
- `api-reference/` YAML file changes — those are owned by backend developers
- Zero customer-facing effect

**INCIDENT_POSTMORTEM** — draft only, needs human approval
- Major service outage or security incident

### Hard rules (always apply)

**Rule 1:** If `[BUG]` is in the title AND it describes fixing broken *product* behavior → BUG_FIX → cancel. No exceptions.

**Rule 2:** If the only stakeholders in the dev ticket are internal teams → INTERNAL_DOC or NOT_DOCUMENTABLE → cancel.

**Rule 3:** If the ticket asks to modify files in `api-reference/` → NOT_DOCUMENTABLE → cancel. Backend team owns those files. Exception: if the ticket asks to write a *how-to guide* about using an API (in a regular `.mdx` file) → PUBLIC_PRODUCT_DOC.

**Rule 4:** "Automatic" or "behind the scenes" does NOT mean not documentable. If the feature affects what the customer gets — document it.

**Rule 5:** If no existing article exists AND the ticket has fewer than 3 sentences of useful customer-facing information AND stakeholders are internal → NOT_DOCUMENTABLE.

### Red flags (verify carefully before proceeding)

| Signal | Likely category |
|--------|----------------|
| `[BUG]` in title | BUG_FIX |
| `/admin/`, "internal", "admin API" | INTERNAL_DOC |
| "refactor", "merge", "consolidate" | NOT_DOCUMENTABLE |
| "library update", "lib", "dependency" | NOT_DOCUMENTABLE |
| "Team DX", "DevOps team", "Backend team" in stakeholders | INTERNAL_DOC |
| `api-reference/`, "OpenAPI", "swagger", "YAML spec" | NOT_DOCUMENTABLE |
| "GitLab to GitHub", "migrate repo", "publish internally" | NOT_DOCUMENTABLE |

### Green flags (proceed)

| Signal | Category |
|--------|----------|
| "new feature", "new in portal" | PUBLIC_PRODUCT_DOC |
| "customer", "user" as audience | PUBLIC_PRODUCT_DOC |
| "how to", "guide", "tutorial" | PUBLIC_PRODUCT_DOC |
| "error message", "troubleshooting" | PUBLIC_TROUBLESHOOTING |
| "now supports", "started to support" | PUBLIC_PRODUCT_DOC |
| "pricing", "limits", "quotas" | PUBLIC_PRODUCT_DOC |
| "automatically enabled" + affects performance | PUBLIC_PRODUCT_DOC |

### If category requires cancel

Output exactly this — nothing more:

```
Ticket: [TICKET-ID]
Category: [category]
Decision: CANCEL
Reason: [1-2 sentences]
```

Do NOT summarize the ticket. Do NOT rephrase the information. Do NOT create
"alternative" internal documentation. CANCEL means CANCEL.

---

## Phase 4 — Find the affected article

Only reached if category is PUBLIC_PRODUCT_DOC or PUBLIC_TROUBLESHOOTING.

Search the repository for the relevant article:

```powershell
# By product or feature name
grep -r "feature name" --include="*.mdx" -l

# By UI section path
grep -r "Cloud > Networking" --include="*.mdx" -l
```

Determine the action needed:

| Situation | Action |
|-----------|--------|
| Existing article found, needs update | UPDATE |
| No existing article, sufficient info to write | NEW |
| No existing article, info too sparse | BLOCKED |

**For NEW action — verify before proceeding:**
- Does the ticket describe a clear customer use case?
- Are there enough technical details to write accurately?
- If info is sparse (< 3 useful sentences) → BLOCKED, ask user for more context

---

## Phase 5 — Assess complexity

For UPDATE actions only. Determines which skill to use next.

Score the update based on these signals:

| Signal | Score |
|--------|-------|
| 2–3 articles affected | +2 |
| 4+ articles affected | +3 |
| Screenshots need updating | +2 |
| New feature added or removed | +2 |
| Cross-links between articles needed | +1 |
| Migration or upgrade involved | +2 |
| Typo, grammar, broken link | -3 |

**Score 0–2 → SIMPLE** — a targeted text change in one location
**Score 3+ → COMPLEX** — involves multiple locations, restructuring, or screenshots

---

## Output

Produce this brief — always, regardless of next action:

```
## Jira context: [TICKET-ID]

### Classification
- Category: [category]
- Decision: [PROCEED / CANCEL / BLOCKED]

### What changed
[1 paragraph: what the product change is, who it affects]

### Affected documentation
- Article: [path, or "none found"]
- Action: [UPDATE / NEW / CANCEL / BLOCKED]
- Complexity: [SIMPLE / COMPLEX] (for UPDATE only)

### Scope of work
[Bullet list: what specifically needs to be added, changed, or removed]

### Suggested next skill
[One of the following:]
- Simple text update → load skill update-page
- Complex update (multiple locations, screenshots) → load skill update-page
- New article needed → load skill write-from-scratch
- Blocked — needs more context → ask user for [specific missing info]
- Cancel → no documentation work needed
```
