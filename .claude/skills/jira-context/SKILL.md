---
name: jira-context
description: >-
  Analyzes a Jira ticket and produces a documentation brief: fetches the ticket
  and linked dev or Confluence pages, classifies whether the change is customer-facing (PUBLIC_PRODUCT_DOC, PUBLIC_TROUBLESHOOTING, BUG_FIX, INTERNAL_DOC,
  NOT_DOCUMENTABLE, INCIDENT_POSTMORTEM), finds the affected article, scores
  update complexity, and recommends the next skill. Use when the user gives a
  Jira ticket ID or URL (especially DOC-####) and asks what work it needs,
  whether it is documentable, or to triage it. Use before writing or editing any
  article. It only produces a brief and does not write or update docs.
---

Fetch a Jira ticket, determine whether documentation work is needed, classify
the type of change, find the affected article, and produce a clear brief.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/mcp-tools/setup.md` — verify Jira MCP is available first
3. `.agents/references/mcp-tools/jira.md` — Jira operations and status reference
4. `.agents/references/mcp-tools/confluence.md` — only if Jira ticket links to Confluence pages

This skill produces a brief. It does not make changes to documentation.

Phase 2c may search the published OpenAPI files and search `.mdx` files for a path or a behavior name. Open an article only when a search hit shows a sentence that states the old fact. Do not read articles to draft content.

---

## Decisions file

Use this one index for every run:

`_private/jira-context-decisions.md`

The index is one row. It is not the record of the check. The record is a separate file, written in the next section. Do not put a date or a timestamp in the index name.

`_private/` is gitignored. Do not commit these files. Do not put credentials or tokens in them. Do not copy customer identifiers into them: account IDs, emails, names, IP addresses. Do not read `_private/secrets/`.

Create the file only when it does not exist, with this table and no other content:

```markdown
| Ticket | Status | Category | Decision | Reason |
|--------|--------|----------|----------|--------|
```

If the file exists, append rows to it. After each ticket is classified, append one row before starting the next ticket. If that ticket already has a row, replace the row. Decision is `CANCEL`, `PROCEED`, `BLOCKED`, or `NOT_PORTAL`. Reason is one sentence.

If the user gave a list, a status stop or a blocking comment applies to that ticket only: write the row, then continue with the next ticket. For a single ticket, write the row, report, and stop as Phase 2 says.

The chat brief for each ticket stays as specified below. The index is the list of decisions for the run. The check trace is the record of how the decision was reached.

## Check trace

After the index row, write one file:

`_private/jira-context/{TICKET}.md`

`{TICKET}` is the key, for example `DOC-3036.md`. Create the directory if it is missing. If that ticket already has a file, replace the file. Do not append a second copy. Do not put this trace in the Jira comment, in the chat brief, or in the one-sentence Reason.

The file is the path the classification actually walked. A future agent reads it to see which step produced the decision. Write every step that was taken. Do not collapse the file into a summary, a single JSON line, or a list of conclusions.

For each step, write four things, in this order:

1. Why this step. Name the skill phase or the rule that required it.
2. Where you went. The ticket key, the file path, the URL, or the search.
3. How you looked. The tool, the query, the fields you read. Quote the query.
4. What came back. The status, the component, the matching line, or the empty result. An empty result is a result. Write it.

Then write the step you did not take, and why.

Keep the order of the work. Do not regroup it into a clean story that hides a dead end. If a search missed because of case or quoting, write that search and the search that followed.

End the file with the rule that fired. Quote the rule from this skill. Then write the rules that were in reach and did not fire, each with the result that kept it from firing.

Do not copy a customer account ID, email, name, or IP address into the file. Name the ticket that contained them.

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
- Labels and components — required to tell AI work from Customer Portal work
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

**If status is not in the YES list — do not classify the ticket.**

Append a row: Category `-`, Decision `BLOCKED`, Reason the status reason. Then report to the user:
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

A comment that says "preprod", "not yet", "not in production", or "deploy to prod" is the state on that comment's date. It is not a blocking signal by itself. Check the live production behavior first: the production API, the production portal, or the published spec the customer sees. Block only when that current check shows the behavior is absent, and name the check in the Reason. The task is to find what already works.

If any other blocking signal is found ("wait for", "on hold", "blocked by", "depends on") — append a row with Decision `BLOCKED` and the signal as Reason, then report to the user.

---

## Phase 2b — AI is not Customer Portal documentation

Run this before Phase 3. AI has its own documentation. Do not classify it as portal documentation, do not search this repository for a portal article, and do not cancel the ticket.

The Org Unit on the DOC ticket is not the source of truth. The drafting agent writes it, and it is often wrong. Open the linked developer ticket and read its labels and components.

The label `ai-enhanced` means an AI agent drafted the ticket text. It does not mean the product area is AI. Ignore that label in this phase. Do not stop classification because of it, and do not require the DOC ticket to carry it.

It is AI only when the developer ticket has the component `Everywhere AI`.

Org Unit `AI` on the DOC ticket does not prove it. Org Unit `Cloud` on the DOC ticket does not override the developer ticket.

When the developer ticket has the component `Everywhere AI`:

- Append a row: Category `AI_DOCS`, Decision `NOT_PORTAL`, Reason one sentence that names the component and says AI has its own documentation.
- Output only this, then continue with the next ticket. Do not run Phase 3 or Phase 4 for this ticket.

```
Ticket: [TICKET-ID]
Category: AI_DOCS
Decision: NOT_PORTAL
Reason: [1-2 sentences]
```

`NOT_PORTAL` is not `CANCEL`. Leave the Jira status unchanged.

---

## Phase 2c — An unpublished API is not a new article

Run this after Phase 2b and before Phase 3, whenever the DOC ticket or the developer ticket names an API path, an operation, a request or response field, or asks for a new API article or an edit under `api-reference/`. Skip this phase for a portal-only UI change that names no API.

A scanner ticket (label `docops-agent-v2`) proposing "new article", "customer-facing", or "how to" is a claim. It is not evidence. A live HTTP 200 on production is not publication. Production serves routes that are not in the public spec.

### What to open, and nothing else

1. List every path the two tickets name. Keep the path string, not a paraphrase.
2. Split those paths:
   - A path containing `/admin/` is an admin API. It is `INTERNAL_DOC`. Do not document it.
   - A path containing `/reseller/` belongs to the reseller spec, `api-reference/services_documented/{product}_reseller_api.yaml`. It is not a customer article unless an existing customer article already states that reseller behavior.
3. For each remaining path, search both published specs. Both must be checked, because they are not the same file:
   - The file `docs.json` mounts for that product. For IAM that is `api-reference/services_docs_mintlify_enriched/iam_api.yaml`. Read the `openapi.source` of the product group in `docs.json`. That file is what the customer sees in the API reference.
   - `api-reference/services_documented/{product}_api.yaml`. The API skills and CI treat this as the public spec.
4. Search `.mdx` for the same path and for the behavior name (the field, the error body, the old sentence). A hit is relevant only when the line states the fact the ticket changes. A different product using the same English words (CDN access control, storage ACL, a portal role) is not a hit.

### How to decide

| What the search shows | Decision |
|--------|----------|
| The path is in the published spec, and an article states the old fact | Continue to Phase 3. The later action is `UPDATE` of that sentence only. |
| The path is in the published spec, and no article states the old fact | Continue to Phase 3 only when the change is a rule the generated reference cannot carry and an existing article already walks that operation. Otherwise `CANCEL`: the reference already shows the operation, and a new page would duplicate it. |
| The path is in neither published file | `CANCEL`. A new article would be the first public description of an unpublished API. Do not edit the YAML to publish it. Backend owns `api-reference/`. |
| The developer ticket says `include_in_schema=False`, "internal spec only", or "no API shape or OpenAPI change", and the path is absent | `CANCEL`. The spec will not grow, and a narrative page must not replace it. |
| The error response already contains the fact the article would explain | `CANCEL`. The caller already receives it. A 403 that lists the missing permissions is such a fact. |
| The developer ticket is a bug or is labeled `security`, and it does not change a published operation | `CANCEL` as `BUG_FIX`, even when the DOC title has no `[BUG]`. Do not publish how a security check fails. |

The one exception to an absent path: an existing `.mdx` already documents that same operation and states a fact this change makes false. Then the action is `UPDATE` of that sentence, not a new article. The sentence must name the operation. A nearby article that talks about roles, tokens, or a similarly named feature is not that sentence.

When the table says `CANCEL`, append the decisions-file row and output the cancel block from Phase 3. Do not run Phase 3 or Phase 4.

This gate is how DOC-3076, DOC-3073, and DOC-3078 are decided. DOC-3076 names `/iam/v2/policies`, which is absent from both IAM specs; the published IAM spec contains account, users, and API tokens only, and no article describes Access Control policies. DOC-3073 names audit-log routes that are absent from the IAM spec, the developer recorded no OpenAPI change, and the ticket is a security bug. DOC-3078 names load-balancer reads the developer left at `include_in_schema=False`. In each case the scanner asked for a new or updated page. The search above is the refusal.

---

## Phase 3 — Classify the ticket

Classification determines whether documentation work is allowed.
Phase 2c has already searched the spec and the articles. Do not search again for context.

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

**Rule 3:** If the ticket asks to modify files in `api-reference/` → NOT_DOCUMENTABLE → cancel. Backend team owns those files. A request to write a how-to in an `.mdx` file does not override this. The how-to is allowed only after Phase 2c has found the operation in the published spec and an existing article that already walks it.

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
| Developer ticket component `Everywhere AI` | AI_DOCS, Decision `NOT_PORTAL`. Do not cancel. The label `ai-enhanced` only means an agent drafted the ticket. |

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

Append the decisions-file row first. Then output exactly this — nothing more:

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
Get-ChildItem -Recurse -Filter *.mdx | Select-String -Pattern "feature name" -List | Select-Object -ExpandProperty Path

# By UI section path
Get-ChildItem -Recurse -Filter *.mdx | Select-String -Pattern "Cloud > Networking" -List | Select-Object -ExpandProperty Path
```

Determine the action needed:

| Situation | Action |
|-----------|--------|
| Existing article found, needs update | UPDATE |
| No existing article, sufficient info to write | NEW |
| No existing article, info too sparse | BLOCKED |

**For NEW action — verify before proceeding:**
- Phase 2c found the operation in the published spec, or an existing article already documents that operation. If neither is true, return to Phase 2c and cancel. Do not open a new article to introduce an unpublished API.
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

A developer ticket is a point fix, not an epic. The scope is the sentence that states the old fact. Do not repeat the new fact in other articles, tabs, examples, or the API spec. If one sentence is wrong, the scope is that sentence. Name a second place only when that place states the same outdated fact.

---

## Output

Skip this section when the category requires cancel. That path already wrote the row and its short block.

Otherwise append the decisions-file row first, then produce this brief:

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
[Only the sentences that are wrong. One wrong sentence is one edit. Do not list places that do not state the old fact.]

### Suggested next skill
[One of the following:]
- Simple text update → load skill update-page
- Complex update (multiple locations, screenshots) → load skill update-page
- New article needed → load skill write-from-scratch
- Blocked — needs more context → ask user for [specific missing info]
- Cancel → no documentation work needed
```
