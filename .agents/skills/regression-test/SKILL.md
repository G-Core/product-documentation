---
name: regression-test
description: Full regression test of an existing article against the live portal. Use when articles may be stale and need end-to-end verification against the current portal UI before updating.
---

Perform a complete regression test of a documentation article: follow its instructions
step by step in the live portal as a real customer would, record every discrepancy,
then apply all fixes and check against the style guide.

---

## FIRST ACTION — Create a todo list

Before doing anything else, create a todo list with every phase as a separate item,
all set to `pending`. Update each item to `in_progress` when you start it and
`completed` only when it is fully done. Do not start a new phase until the previous
one is marked `completed`.

Phases to track:

- Phase 0: Find and read the article; claim in plan
- Phase 1: Open the portal and log in
- Phase 2: Regression test (follow steps, record FINDINGs)
- Phase 3: Screenshot audit (retake all screenshots)
- Phase 4: Findings summary + create Jira ticket
- Phase 5: Apply fixes
- Phase 6: Style guide check
- Phase 7: MDX rules check
- Phase 8: LLM quality review
- Phase 9: Present for review (pre-commit checklist + commit + push)
- Phase 10: Send to review (Jira transition + plan update + changelog)

If a phase is not `completed`, do not move to the next one.
If you are unsure whether a phase is done, re-read its section below and verify.

---

## STRICT RULE: one phase at a time

**Work on exactly one phase. Finish it completely. Then stop.**

Do not read ahead. Do not plan the next phase while executing the current one.
Do not try to hold all phases in mind simultaneously.
The goal is not speed — it is thoroughness within each isolated step.

When a phase is done:
- Report what was completed
- Immediately start the next phase without asking for permission

**EXCEPTION — after Phase 10 (article fully complete):**
Stop completely. Do NOT move to the next article.
Wait for explicit user instruction to proceed to the next article.
The auto-progression rule applies only to phases within a single article.

Violating this rule produces shallow work across all phases instead of
deep work within each phase. This is forbidden.

---

## Scope — read exactly these files

1. This SKILL.md
2. The article file identified in Phase 0
3. `.agents/references/style-guide.md` — Phase 6 only
4. `.agents/references/procedures.md` — Phase 6 only (numbered steps check)
5. `.agents/references/content-types.md` — Phase 5 only (before rewriting any section)
6. `.agents/references/mdx-rules.md` — Phase 5 (if MDX structure is changed) and Phase 7
7. `.agents/references/mcp-tools/playwright.md` — Phase 1, Phase 2, and Phase 3

Do not read other articles for context unless they are directly linked from the
article being tested.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Article path or topic | Yes | Full path or description to locate it |
| Portal region | No | Default: **Luxembourg-3** |

---

## Phase 0 — Find and read the article

If the article path is given — open the file directly.

If only a topic is given — search the repository:

```powershell
rg "keyword" --glob "*.mdx" -l
```

### Claim the article before doing any work

Before reading the article, open the plan file specified in the task and mark the article as `in_progress`.

Find the row for this article and change its status from `pending` to `in_progress`.

**Why this matters:** two agents may be running in parallel on separate repository
clones. Both can see the same `pending` rows. Claiming the article first — before
reading it, before opening the portal — ensures no other agent picks up the same
article and produces duplicate work or a merge conflict.

**If the article's status is already `in_progress` or `done`:** stop immediately.
Report to the user: "Article [path] is already claimed or completed in the plan.
Choose a different article." Do not proceed until the user confirms a different target.

After updating the plan, proceed to read the article.

Read the entire article before touching the portal.
Build a mental map:
- What is the user expected to achieve by the end?
- What steps does the article prescribe?
- What UI elements, buttons, field names, and navigation paths does it mention?
- How many screenshots are in the article and what do they show?
- Are there prerequisites that require other resources (network, cluster, SSH key, etc.)?

List each prerequisite resource and check whether a documentation article covers
its creation. Note the article path for each — do not open or test those articles now.
They will be tested in their own turn.

---

## Phase 1 — Open the portal

Load `.agents/references/mcp-tools/playwright.md` now.

### Open an isolated browser session first

**Before navigating to the portal**, open a new incognito window to get a clean,
isolated session that does not interfere with any other agent currently using the browser:

```javascript
// browser_evaluate — opens a new incognito window
window.open('about:blank', '_blank');
```

Or use the Playwright MCP `browser_navigate` with a `--incognito` context if the MCP
server supports it. The goal is a browser context with **no shared cookies, no shared
tabs, no shared history** with any other session on this machine.

**Why this is required:** Playwright MCP runs a single browser process shared across
all agents running on the same machine. Without isolation, two parallel agents click in
the same browser window — one agent's navigation overwrites the other's. An incognito
window is a separate context: separate cookies (separate login session), separate tabs,
no cross-contamination.

**If you cannot open an isolated context** — stop and tell the user:
> "Playwright MCP is sharing a browser session with another agent. A separate
> incognito window is required to proceed safely. Please confirm the incognito
> window is open before I continue."

Do not proceed with portal testing until you are certain you are in an isolated session.

### Log in

Follow the SSO login flow from `.agents/references/mcp-tools/playwright.md` exactly,
inside the isolated session:

1. Navigate to `https://auth.gcore.com/login/signin`
2. Click **SSO**
3. Enter `gcore.com` in the Work domain field and press Enter
4. Verify the browser is at `https://portal.gcore.com`

### Select the region

After login, navigate to the region the article targets.
Default region: **Luxembourg-3**.
Select it from the region dropdown in the portal header before starting any steps.

**Why Luxembourg-3:** all quotas needed for testing are available in this region.
Do not use any other regions — quota availability differs. Other regions are allowed only if you don't find the required resource on Luxembourg-3.

Verify the region switcher in the portal header shows **Luxembourg-3** before proceeding.

---

## Phase 2 — Regression test

**Mindset: you are a customer reading this article for the first time.**
You have no prior knowledge of the product. You follow the article literally.
If something is unclear, confusing, or missing — it is a finding.

### Resource naming

Any resource created during testing — instance, cluster, network, volume, bucket,
container, firewall, load balancer, or any other cloud object — must have a name
a real customer would give it on their first day using the product.

**Correct pattern:** `my-instance-1`, `my-cluster-1`, `my-network-1`, `my-volume-1`,
`my-bucket-1`, `my-vm-1`, `my-lb-1`, `my-registry-1`, and so on.

**Never use:** `docs-*`, `audit-*`, `test-*`, `regression-*`, `doc-*`, article slugs,
Jira ticket IDs, or any name that signals internal tooling or automation.

**Why this matters:** resource names appear in screenshots published as documentation.
A customer reading the article sees those names in the UI. Names like `test-audit-vm`
or `regression-cluster-1` break the customer's suspension of disbelief — they signal
that the article was written by automation, not by someone doing the task for real.
Names like `my-cluster-1` read as the customer's own work and make the article
immediately relatable.

This rule applies to all resources created during Phase 2 testing and to all
screenshots taken in Phase 2, Phase 3, and Phase 5.

### Execution rules

- Follow the article's steps in exact order.
- At each step, use `browser_snapshot` to read the actual current UI labels, button
  names, field names, and navigation paths.
- If the article says to create something — create it.
- If the article says to delete something — delete it.
- If something the article describes does not exist or works differently — do not skip it.
  Explore what the portal actually shows now and document the divergence as a FINDING. Make a full investigation of functionality related to this.
- If a step requires a prerequisite resource (a network, a cluster, an SSH key,
  a volume, a load balancer, etc.) that does not yet exist:

  **MANDATORY: Create the resource before proceeding. Do NOT skip or note as UNVERIFIED.**

  The test account has all necessary quotas in **Luxembourg-3**. There is no valid
  reason to skip portal testing because a resource does not exist yet.

  - Create the required resource in Luxembourg-3 using the portal.
  - Name it using the standard naming pattern (`my-lb-1`, `my-vm-1`, etc.).
  - Then continue testing the article from the step that requires it.
  - Note the resource creation as "test environment setup" — not a finding.

  This applies to: Load Balancers, Virtual Machines, Networks, Routers, Subnetworks,
  Volumes, SSH Keys, Security Groups, Floating IPs, Reserved IPs, Kubernetes clusters,
  Secrets, Container Registries, and any other prerequisite.

  **The only valid reason to mark something UNVERIFIED is if the feature is gated
  (requires a special plan, a support ticket, or is physically unavailable in the
  portal UI). Absence of a test resource is never a valid reason.**

  After the test is complete, delete the resources created during testing
  (or leave them if they will be needed for subsequent articles in the same batch).

- If a feature is genuinely unavailable in this region or account (gated by plan,
  requires support enablement, or does not appear in the portal) — note it as a
  finding, describe how far you got, and mark related findings as UNVERIFIED.

### Non-portal articles

Some articles require tools other than the Customer Portal. Identify the article type
before starting Phase 2 and apply the rules below.

**General rule: never stop because a tool or environment is unavailable.**
If a testing environment is inaccessible — no GUI app, no CLI tool, no portal access
for a specific feature — do NOT wait for the user, do NOT ask for permission.
Skip testing for those specific steps, apply style guide and MDX checks to the full
article, and document the untested steps as UNVERIFIED in Phase 4. Continue to Phase 5
and beyond as normal. Style guide compliance applies to every article regardless of
whether its steps can be portal-verified.

#### Terminal articles (AWS CLI, S3cmd, shell commands)

The test machine has PowerShell and internet access. AWS CLI and S3cmd can be
installed and used directly.

**Testing rules:**

1. Verify that the tool is installed before following the article steps:
   ```powershell
   aws --version
   s3cmd --version
   ```
   If a tool is not installed — install it following the article's own instructions
   (if the article covers installation) or using the tool's official installer.
   Installation is test-environment setup, not a FINDING.

2. Obtain real credentials from the portal before running any command:
   - Navigate to the storage in the portal.
   - Copy the Access Key, Secret Key, and endpoint URL from the storage Details.
   - Use these credentials in all commands. Never fabricate credentials.

3. Follow every command in the article, run it in PowerShell, and record the actual
   output. Compare the expected output described in the article with what the terminal
   shows.

4. If a command produces an error — investigate whether the article's syntax is wrong
   or the endpoint has changed. Record as a FINDING with category `Broken flow`.

5. If a command produces no output where output is expected — record as a FINDING.

6. Files created during testing (JSON, XML, config files) must be deleted after the
   test unless the article explicitly says to keep them.

**What cannot be tested in terminal:**
- AWS JavaScript SDK examples — verify the SDK version and syntax only; mark
  version-specific claims as needing manual browser verification.

#### GUI desktop application articles (FileZilla, WinSCP, etc.)

The agent cannot open or interact with GUI desktop applications.
**Do not stop. Do not ask the user for access. Proceed immediately with style-only mode.**

**Testing rules:**

1. Skip Phase 2 portal testing entirely for GUI-only steps. Do not attempt to
   navigate the portal for steps that belong to the external app.

2. Proceed directly to Phase 6 (style guide check) and Phase 7 (MDX rules check)
   for the full article — these phases apply regardless of tool type.

3. Mark all GUI-specific steps as UNVERIFIED in the Phase 4 findings summary
   (not in the article text itself). Use this format:
   ```
   UNVERIFIED: GUI desktop application step — cannot be tested by agent.
   Location: Step N / section "[heading]"
   Instruction: [the step verbatim]
   Concern: Requires manual verification with [app name] installed locally.
   ```

4. Screenshot replacement for GUI app screenshots: do NOT retake them in Phase 3.
   Mark them in the screenshot checklist as `SKIP — GUI app, manual retake required`.

5. Note all GUI-only UNVERIFIED items in the Jira ticket description (Phase 4)
   so a human can complete the visual verification.

#### Reference table articles (endpoint URLs, region names)

Articles that consist mainly of tables of URLs, endpoints, or region names
do not have portal steps to follow. Verify the data differently:

1. Cross-reference each URL against the portal:
   - Navigate to a storage → Details to see the actual endpoint format.
   - Compare with the table in the article.

2. If the table lists regions or locations, verify each one exists in the portal's
   region dropdown or storage creation form.

3. Record any mismatch as a FINDING with category `UI label mismatch` or
   `Deprecated option`.

---

### VERIFIED OK format

For every article claim that is confirmed correct in the portal, record it immediately
after testing that claim. Do not skip this step — every element tested must appear in
either a VERIFIED OK block or a FINDING block. This log is the primary output that
the human reads to understand what was actually tested.

```
VERIFIED OK: [what was checked — one line description]
Location: Step N / section "[heading]" / screenshot "[filename]"
Article says: "..."
Portal shows: "..." (matches)
```

Record a VERIFIED OK for every:
- Navigation path confirmed in the portal
- UI label, button name, or field name that matches
- URL schema or hostname format that is still valid
- Screenshot that is visually current (will be retaken in Phase 3 but content is accurate)
- Feature or option that still exists as described

### FINDING format

Record every discrepancy using this format:

```
FINDING: [category]
Location: Step N / screenshot "[filename]" / section "[heading]"
Article says: "..."
Portal shows: "..."
Action needed: [rename / reorder steps / add step / remove step / update screenshot / rewrite / investigate]
```

Categories:
- `UI label mismatch` — button, field, or menu name differs
- `Navigation path changed` — the path to reach the screen changed
- `Step order changed` — steps are in a different order than documented
- `Missing step` — a mandatory step exists in the portal that the article omits
- `Removed step` — the article describes a step that no longer exists
- `Outdated screenshot` — screenshot no longer matches the current portal UI
- `Missing screenshot` — the article has no screenshot but one would help
- `Wrong field name` — a form field has a different label
- `Deprecated option` — an option the article mentions no longer exists
- `New option` — an option exists in the portal that the article does not mention
- `Prerequisite` — a required resource must exist before this step
- `Feature unavailable` — the feature cannot be tested (gated, region, account)
- `Broken flow` — the described action produces an error or unexpected result
- `Missing context` — the article does not explain why a step is needed
- `Unverified procedure` — a technical instruction that may have side effects or may not be
  the standard approach, but cannot be confirmed without SME input

### Potentially dangerous technical instructions

When a step performs an irreversible or high-impact action — for example: re-running an
initialization tool on a running system, purging state files, resetting configuration
modules, or any command that says `clean`, `purge`, `reset`, `wipe`, or `reformat` —
do NOT assume it is wrong, do NOT replace it with an alternative, and do NOT skip it silently.

Record it as:

```
UNVERIFIED: This procedure may have side effects. Technical validation by an SME is
required before changing or publishing it.
Location: [section / step number]
Instruction: [the specific command or procedure verbatim]
Concern: [one sentence describing the potential risk]
```

Do not add this note to the published article. It belongs only in the Jira ticket
description (Phase 3) and the changelog (Phase 9). The published text stays as-is
until an SME confirms or corrects the procedure.

### Screenshots during Phase 2

If a portal state that is transient and cannot be reproduced later (a mid-wizard dialog,
a resource-dependent state, an error message triggered by a specific action) differs
from the article screenshot — capture it NOW and note both the old filename and the
new filename as a FINDING with category `Outdated screenshot`.

For all other screenshots, record a FINDING with category `Outdated screenshot` if
the UI has changed, and note the portal URL and navigation path. All static screenshots
will be retaken systematically in Phase 3.

**Do not apply any fixes during this phase. Collect all findings first.**

After completing all steps, clean up any test resources created during testing
(instances, networks, etc.).

---

## Phase 3 — Screenshot audit

For each screenshot in the article, navigate to the corresponding screen in the portal and **compare the current UI with the existing screenshot**. Retake only if the UI has visibly changed — layout, labels, buttons, or missing/added elements. If the screenshot still accurately represents the current portal state, mark it as `ok` and move on.

**Do not retake screenshots unconditionally.** Retake only when the comparison reveals a real discrepancy. If the user has explicitly told you the screenshots are current, mark all as `ok` without opening the browser.

### Checklist

Before starting, list every `<Frame>` in the article with the following table:

| # | Filename | Screen to reach | Status |
|---|----------|-----------------|--------|
| 1 | `filename.png` | Navigation path or step | pending |

For each row, set status to:
- `ok` — screenshot matches current portal UI, no retake needed
- `retaken` — screenshot was outdated and has been replaced
- `skip` — screenshot cannot be verified (GUI app, gated feature, user confirmed current)

Do not mark Phase 3 as completed until every row has a final status.

### How to take each screenshot

For each screenshot in the article:

1. Navigate to the correct screen in the portal using the existing article
   text as a guide — it describes what each screenshot should show.

2. **Set the viewport to 1400×900** using `browser_resize`:
   ```
   browser_resize(width=1400, height=900)
   ```
   Do this once at the start of Phase 3, before the first screenshot.
   Do NOT use `browser_evaluate` with `window.resizeTo` — that call is ignored
   by headless Playwright. Only `browser_resize` actually changes the viewport.

3. **Hide PII before every screenshot** — the portal shows the logged-in user's
   email in the top-right corner. Remove it with `browser_evaluate`:
   ```javascript
   // Find and hide the email / account info element in the top-right corner.
   // The selector targets the most common portal patterns; adjust if needed.
   document.querySelectorAll(
     '[class*="user-info"], [class*="UserInfo"], [class*="account-email"], ' +
     '[class*="userEmail"], [class*="header__user"], [class*="userMenu"]'
   ).forEach(el => { el.style.visibility = 'hidden'; });
   // Fallback: hide any element whose text content looks like an email address.
   document.querySelectorAll('span, p, div, a').forEach(el => {
     if (/[^@\s]+@[^@\s]+\.[^@\s]+/.test(el.innerText) && el.children.length === 0) {
       el.style.visibility = 'hidden';
     }
   });
   ```
   Use `visibility: hidden` (not `display: none`) so the element still occupies
   space and the layout does not shift. Run this before EVERY screenshot — some
   portal navigation re-renders the header and makes the email visible again.

4. **Take a full-viewport screenshot** using `browser_take_screenshot`:
   - Do NOT pass `element` or `target` parameters — those crop the image.
   - Use the `filename` parameter to set the output filename:
     ```
     browser_take_screenshot(filename="screenshot-name.png")
     ```
   - The file is saved to `C:\Users\{username}\` (Playwright MCP home dir).
     After saving, copy it to the article images folder:
     ```powershell
     $dest = "C:\Projects\product-documentation_2\images\docs\{product}\{slug}\{slug}-imageN.png"
     Copy-Item "C:\Users\sergey.kostichev\screenshot-name.png" $dest -Force
     ```
   - Verify the file exists before moving on:
     ```powershell
     cmd /c "dir /b C:\Projects\product-documentation_2\images\docs\{product}\{slug}"
     ```

5. Update the `<Frame>` in the article to reference the new filename.
6. Update the alt text if the UI shown has changed.
7. Delete the old file:
   ```powershell
   cd C:\Projects\product-documentation_2
   git rm images/docs/{product}/{article-slug}/{old-filename}.png
   ```

### What NOT to do with screenshots

- **Never crop** by passing `element` or `target` to `browser_take_screenshot`.
  Full-viewport screenshots are always correct; cropped ones frequently look broken.
- **Never use `savePath`** — it is not a valid parameter. Use `filename` instead.
- **Never use `browser_evaluate` to resize** — `window.resizeTo()` has no effect
  in headless Playwright. Use `browser_resize` only.
- **Never skip the PII-hide step** — the logged-in email is always visible in the
  portal header and must not appear in published documentation.
- **Never take a screenshot immediately after scrolling** — give the page
  50–100 ms to finish rendering. Use a brief `browser_wait_for(time=100)` or
  take a `browser_snapshot` first (which forces a render cycle) before capturing.

### Resource names in screenshots

All portal resources visible in screenshots must follow the `my-*-1` naming
pattern: `my-instance-1`, `my-cluster-1`, `my-network-1`, etc.
Never show internal or automation names (`test-*`, `docs-*`, `regression-*`,
Jira IDs, article slugs).

### No duplicate screenshots

After all screenshots are saved:

1. Compare file sizes — identical byte counts before cropping indicate reuse.
2. For each duplicate, determine which filename has the correct semantic meaning
   and retake the other.
3. List all files in the images folder and confirm every file is referenced in
   the article. Remove unreferenced files with `git rm`.

### Transient screenshots (already captured in Phase 2)

If a screenshot was captured during Phase 2 (mid-wizard dialog, resource-dependent
state), skip retaking it here. Verify it is already saved with the correct filename
and that the `<Frame>` reference and alt text are updated.

---

## Phase 4 — Findings summary and Jira ticket

After completing Phase 2, present all findings to the user as a numbered list
grouped by category.

Also present:
- Total number of findings
- List of prerequisites noted, with article paths where available
- List of screenshots that need replacement, with old and new filenames
- Any steps where the feature was unavailable (UNVERIFIED)

### Create the Jira ticket immediately after presenting findings

Do not wait for the user to ask. Create the ticket now, while the findings are
fresh and before any fixes are applied.

**If a Jira ticket already exists for this article** (e.g. the article is being
redone after a partial run), do NOT create a duplicate ticket. Use the existing
ticket number and continue directly to Phase 5.

Open `c:\Projects\docops-agent2\scripts\create_edge_cloud_regression_ticket.py`
and fill in `SUMMARY` and `DESCRIPTION` with the article name and the findings
list collected in Phase 2.

**What belongs in the description — every finding in full.**

Copy the full FINDING blocks from Phase 2 verbatim. Do not summarise, shorten,
or paraphrase. The description must read as a complete audit report so that
anyone opening the ticket understands the exact scope of work without
reading the article or the portal.

Group findings by category, include the finding number, location, "Article says",
"Portal shows", and "Action needed" for each one. This is the same format used
in Phase 2 — reproduce it exactly.

**Do NOT include in the description:**
- Style guide micro-fixes (Phase 5)
- MDX encoding issues (Phase 6)
- CRLF/LF, BOM, or p-tag cleanup

Format:

```
SUMMARY = "Update {article title}"

DESCRIPTION = (
    "Regression findings for '{article title}':\n\n"
    "{Category 1} ({N})\n\n"
    "FINDING 1: {category}\n"
    "Location: {location}\n"
    "Article says: \"{...}\"\n"
    "Portal shows: \"{...}\"\n"
    "Action needed: {...}\n\n"
    "FINDING 2: ...\n"
    "...\n\n"
    "{Category 2} ({N})\n\n"
    "FINDING 3: ..."
)
```

Example of correct content (do not copy — fill with actual findings):

```
UI label mismatch (2)

FINDING 1: UI label mismatch
Location: Filter list, bullet 1
Article says: "ID (resource name)"
Portal shows: "Resource name"
Action needed: Rename filter

FINDING 2: UI label mismatch
Location: Opening sentence
Article says: "Gcore Edge Cloud"
Portal shows: navigation is under Cloud Management > User Actions
Action needed: Replace with "Gcore Customer Portal"

Missing step (1)

FINDING 3: Missing step
Location: Article opening — no navigation path given
Article says: (nothing)
Portal shows: Navigation path is Cloud Management > User Actions
Action needed: Add navigation instructions
```

Dry run first:

```powershell
cd C:\Projects\docops-agent2
.\venv\Scripts\python.exe scripts/create_edge_cloud_regression_ticket.py --dry-run
```

Show the dry-run output to the user, then run without `--dry-run` immediately
after — do not wait for separate confirmation unless the user objects.

```powershell
.\venv\Scripts\python.exe scripts/create_edge_cloud_regression_ticket.py
```

Report the created ticket key and URL to the user. Record the ticket key —
it is needed in Phase 9.

Reset `SUMMARY` and `DESCRIPTION` back to placeholder values after creating
the ticket so the script is ready for the next article.

Immediately proceed to Phase 5 without asking for confirmation.

---

## Phase 5 — Apply fixes

Before rewriting any section, load `.agents/references/content-types.md` and identify
the article's content type (how-to, conceptual, reference, or combined). Keep the
content type intact when rewriting — do not convert a how-to into a reference or vice versa.

If any `<MethodSwitch>` structure will be changed, load `.agents/references/mdx-rules.md`.

Apply all confirmed findings to the article. For each fix:

1. Find the exact location in the article.
2. Read the surrounding paragraph or section to understand tone and structure.
3. Write the fix so it fits naturally — do not leave mechanical edits that break flow.

### Rules for applying fixes

**UI label or field name changed:**
- Replace every occurrence throughout the article.
- Check whether surrounding sentences now read awkwardly and rewrite if needed.
- Update alt text on any screenshot that shows the renamed element.

**Step added or removed:**
- Rewrite the affected section, do not patch individual sentences.
- Renumber all steps in the section.
- Verify the intro sentence of the section still describes what follows.

**Navigation path changed:**
- Update the path in all occurrences.
- Check whether the step introducing navigation needs rewording.

**Screenshot replaced:**
- Replace the `<Frame>` path with the new filename.
- Update the alt text to describe what the new screenshot shows.
- Delete the old file with `git rm`.

**No duplicate screenshots — check before closing Phase 4:**

After placing all new screenshots in the article's images folder:
1. Verify each file shows visually distinct content from every other file in the folder.
   Compare by file size: identical byte counts before any cropping mean the source
   screenshot was reused — this is a mistake.
2. For each duplicate pair, determine which name has the correct semantic meaning
   (matches alt text and article context). Retake the one with wrong content.
3. Never copy the same source screenshot to two different destination filenames.
   If two places in the article show the same UI state, reference the same file twice
   rather than making a copy.
4. After verifying uniqueness, list all files in the images directory and confirm
   every file is referenced in the article. Remove any unreferenced file with `git rm`.

**Prerequisite dependency noted:**
- Add a cross-link to the prerequisite article where the relevant step appears.
- If no article exists for the prerequisite, add a `<Note>` or `<Info>` block
  describing what must exist before the step. Do not add a `## Prerequisites` section.

**Broken flow / feature works differently:**
- Describe the actual current behavior in the article.
- Remove steps that no longer apply.
- If the replacement flow is significantly different, rewrite the section from scratch.

### Hard rules — never do these

- Never touch `<MethodSection id="api">` — API sections are a separate update cycle.
- Never rename article files or change slugs.
- Never edit `docs.json` without explicit user confirmation.
- Apply only fixes from the confirmed findings list. Note any other issues you notice
  at the end — do not fix them silently.

### `<p>` tag rules

The rule depends on whether the article uses `<MethodSwitch>`:

**Articles WITHOUT `<MethodSwitch>`:**
- Remove any stray `<p>` wrappers around plain prose paragraphs — they are not needed
  outside JSX and produce unnecessary markup.
- Bullet lists must never be wrapped in `<p>`.

**Articles WITH `<MethodSwitch>` (inside `<MethodSection>` only):**
- Prose paragraphs that sit immediately before or after a `<Frame>`, a fenced code
  block, or a `<Tabs>` component **must** be wrapped in `<p>` — otherwise they merge
  visually with the adjacent block element.
- Prose that sits between numbered steps must be wrapped in `<p>` — removing the tag
  causes the MDX parser to merge step numbers into the paragraph.
- Bullet-only lists must NOT be wrapped in `<p>` — they are block-level and render
  correctly without it.
- Never delete a `<p>` tag that acts as a structural separator between numbered steps
  inside `<MethodSection>`. If the text inside is outdated, replace the text — not the tag.

---

## Phase 6 — Style guide check

Load `.agents/references/style-guide.md` and `.agents/references/procedures.md` now.

### Step 1 — Run the automated style linter

Run the style linter first. It catches mechanical violations automatically so the manual
checklist can focus on things the script cannot detect (flow, headings, structure, logic).

```powershell
cd C:\Projects\product-documentation_2
python .agents/tools/style_check.py {relative/path/to/article.mdx}
```

Replace `{relative/path/to/article.mdx}` with the actual path, for example:
```
python .agents/tools/style_check.py hosting/virtual-servers/order-a-virtual-server.mdx
```

For every violation the script reports:
1. Read the line it flagged.
2. Fix the violation if it is real.
3. If it is a false positive (e.g. a term matched inside a URL or a technical name
   that must stay as-is), note it and move on — do not change correct text.

Re-run the script after fixing until it reports **OK — no violations found**.

### Step 2 — Manual checklist

Work through the article section by section and verify each rule. Do not skim.
For each checklist item: read the article, verify the rule, then mark the item with `[V]`.
Only mark `[V]` after you have actually checked — not as a placeholder.
When the full checklist is marked, scan for any remaining `[ ]` and re-check those lines before proceeding.

Checklist:

**Voice and tone:**
- [ ] No "you" or "your" in authored prose
- [ ] No meta-preamble opener ("This guide covers...", "This article explains...")
- [ ] No banned words: just, simply, ensure, obviously, platform, leverage, utilize, etc.
- [ ] No "permanent API token"

**Sentence structure:**
- [ ] Causal connectors used between related sentences
- [ ] No isolated facts in sequence (dictionary-card pattern)
- [ ] Opening paragraph does not have a `## Prerequisites` section

**Headings:**
- [ ] Sentence case
- [ ] No "What / How / Why / When" headings
- [ ] No infinitive headings ("To create...")
- [ ] No consecutive headings (at least one sentence between them)
- [ ] Every heading has an intro sentence before lists or code

**Forbidden sections:**
- [ ] No `## Next steps`, `## See also`, `## Related documentation`, `## Prerequisites`,
  `## Requirements`, `## Get started`, `## What's next`

**Links** (script catches text length, &nbsp;, banned patterns, relative paths, docs.gcore.com URLs):
- [ ] First mention of portal: `[Gcore Customer Portal](https://portal.gcore.com)`
- [ ] Subsequent mentions: plain "the Customer Portal" (no link, no "Gcore" prefix)

**Formatting:**
- [ ] Bold only for clickable UI elements and field names
- [ ] Inline code for commands, values, and file names
- [ ] Em-dashes spaced: ` — ` not `—`

**Procedures** (cross-check against `procedures.md`):
- [ ] Location before action in each step
- [ ] Optional steps prefixed with `(Optional)` exactly
- [ ] Login step uses "log in to" (three words, not "log into")
- [ ] No single-item numbered lists
- [ ] Sub-steps indented with 3 spaces under the parent step
- [ ] No "Step 1:" label in the step text itself — the number is enough
- [ ] No instruction to "press Enter" when a button click achieves the same thing
- [ ] Result sentences ("The X page opens.") placed after the step, not as a separate step

**Screenshots:**
- [ ] Each screenshot has alt text (under 125 characters, sentence case)
- [ ] Screenshots appear after the step text, not before

**Terminology:**
- [ ] "click" not "click on"
- [ ] "select" not "choose"
- [ ] "enter" not "type in"
- [ ] "navigate to" not "go to"
- [ ] US English spelling

**Numbers:**
- [ ] Zero through nine spelled out in body text; 10+ as digits
- [ ] Space between number and unit: "128 GB", "10 Gbps"

**Capitalization:**
- [ ] Gcore product names in Title Case: Bare Metal, Virtual Machines, etc.
- [ ] Article titles and headings in sentence case

Fix every violation found. If a fix requires rewriting a paragraph, do it.
If any items remain unmarked (`[ ]`) after the full pass — re-check those lines before closing Phase 6.

---

## Phase 7 — MDX rules check

Load `.agents/references/mdx-rules.md` now.

Check whether the article uses a `<MethodSwitch>` component:

```powershell
rg "MethodSwitch" path/to/article.mdx
```

**If `<MethodSwitch>` is not present** — this phase takes less than a minute.
Verify only the basic MDX rules below and move on.

**If `<MethodSwitch>` is present** — read the full `mdx-rules.md` and apply all
relevant checks for the component, its sections, and the import line.

### Checklist (all articles)

- [ ] No raw HTML tags (`<div>`, `<span>`, `<br>`) except where explicitly approved
- [ ] Outside `<MethodSection>`: no stray `<p>` wrappers around plain prose paragraphs
- [ ] Inside EVERY `<MethodSection>` (Portal, API, Terraform, CLI — all tabs): EVERY standalone prose paragraph IS wrapped in `<p>` — no exceptions, no analysis of what is adjacent; numbered list items and bullet list items are NOT wrapped in `<p>`
- [ ] `<Frame>` wraps each screenshot; no bare `![]()` outside `<Frame>`
- [ ] Every `<img>` inside `<Frame>` uses an explicit `width` attribute (`width="70%"`),
  not the markdown `![alt](src)` shorthand and not `style={{ width:"..." }}`.
  Run `scripts/fix_image_widths.py` if bulk conversion is needed (see `mdx-rules.md`).
- [ ] `<Tabs>` / `<Tab>` structure is valid: every `<Tab>` has a `title` attribute

**Callout blocks (`<Info>`, `<Warning>`, `<Note>`, `<Tip>`):**
- [ ] No redundant prefix inside the block: remove `**Info**`, `**Warning**`, `**Note**`, `**Tip**` text at the top — the component already renders the label
- [ ] Callout blocks are not nested inside each other
- [ ] No two callout blocks placed back-to-back without prose between them. If two callouts cover the same concern — merge them into one. If they cover different concerns — add a sentence of prose between them to give each block its own context
- [ ] Each callout is used for its semantic purpose: `<Warning>` for data loss / irreversible actions; `<Info>` for important non-obvious context; `<Note>` for supplementary detail; `<Tip>` for optional shortcuts

### Additional checklist (articles with `<MethodSwitch>`)

- [ ] Import line uses `.jsx` extension:
  `import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";`
- [ ] `label` attribute is on `<MethodSection>`, not on `<MethodSwitch>`
- [ ] Every `<MethodSection>` has an `id` attribute (`"portal"`, `"api"`, etc.)
- [ ] `<MethodSwitch>` wraps all `<MethodSection>` blocks — no sections outside
- [ ] Content written for the Portal tab does not bleed into other tabs
- [ ] Never touch `<MethodSection id="api">` — API sections are out of scope

Fix every violation found. If fixing a `<MethodSwitch>` structure, re-read the
relevant section of `mdx-rules.md` before making changes to avoid silent regressions.

**Never use scripts for text replacements in MDX files.**
All fixes must be done with targeted StrReplace calls, one replacement at a time.
Scripts introduce quoting and encoding errors that corrupt the file silently.
StrReplace is explicit, auditable, and safe.

---

## Phase 8 — LLM quality review

Before presenting the article to the user, run the automated quality review script.
This must happen after Phase 6 and before Phase 8 — never skip it.

```powershell
cd C:\Projects\docops-agent2
.\venv\Scripts\python.exe scripts/review_article_quality.py --article "C:\Projects\product-documentation\{article-path}.mdx"
```

The script sends the article to GPT-4 and scores it on 11 criteria (1–10 each).

### Step 1 — Classify every remark

For each remark the LLM produces, classify it before doing anything:

**Automatic false positives — reject without fixing:**

- Suggests explaining bash, curl, SSH, Python, Go, Terraform, RDP, cloud-init,
  or any tool that is a prerequisite for the section's audience.
- Suggests making the article self-contained by adding information that belongs
  in a separate article and is already linked.
- Complains that an Accordion, Tabs, Info, Tip, or Warning adds cognitive load.
- Complains about the position of a method tab (Portal/API/Terraform order).
- Suggests adding transition sentences between numbered steps where the
  numbering already makes the sequence obvious.
- Flags technical terms (IPv4, CIDR, DHCP, SDK, API key, region ID) as jargon
  requiring explanation.
- Suggests the article is incomplete because a related topic (connecting,
  monitoring, deleting) is not covered — those are separate articles.
- Flags a screenshot caption or alt text as insufficient when the screenshot
  itself makes the meaning clear.
- Suggests adding detail about a UI element that is visible on the adjacent screenshot.

**Requires judgment — verify before deciding:**

- Mentions a diagram or image that the article references but the LLM cannot see.
  → Check whether the referenced visual actually exists in the article. If it does,
  false positive. If it does not exist, it is a real finding.
- Flags a sentence as hard to read.
  → Read the sentence yourself. If a native English speaker would pause on it,
  fix it. If the sentence is just technical, reject.
- Flags repeated information across sections.
  → Check whether the repetition is intentional (e.g., a warning duplicated at
  the point of action) or genuine duplication. Fix only genuine duplication.

**Always real — fix immediately:**

- A specific word that has a simpler, equally precise alternative
  (e.g., "prior" → "before", "utilize" → "use").
- A sentence that contains two nested clauses that could be two sentences.
- Information stated twice in consecutive paragraphs with no structural reason.
- A step that promises a result ("The window opens") but the result never comes.

### Step 2 — Apply fixes

Fix only the remarks classified as real. Do not touch:
- Factual content verified against the portal in Phase 2.
- Step numbering.
- Portal-verified UI labels, button names, field names.
- The structure of MethodSwitch tabs.

### Step 3 — Re-run (max 2 iterations)

After applying fixes, re-run the script. Compare the new score to the previous one.

- If the score improved and all remaining remarks are false positives — stop.
- If the score did not improve despite real fixes — stop after this second run.
  Do not loop a third time.
- If no real remarks were found in the first run — proceed directly to Phase 8
  without re-running.

### Step 4 — Report to the user

Do NOT ask the user to approve fixes or review individual remarks.
Do NOT present the raw LLM output to the user.

When Phase 7 is complete, include a single block in the Phase 8 report:

```
Auto-review (GPT-4): X.X / 10
  Fixed: [list of real fixes applied, one line each]
  Rejected as false positives: [count] remarks
  Remaining remarks (not fixed): [list only if they are genuinely debatable]
```

If no fixes were needed and no debatable remarks remain, write:
```
Auto-review (GPT-4): X.X / 10 — no actionable remarks.
```

---

## Phase 9 — Create branch, commit, and push

**One article = one branch.** The branch name is always the Jira ticket key
created in Phase 4 — even if the user mentioned a different name earlier in the
conversation. The Phase 4 ticket is the canonical source of truth for the branch name.

**CRITICAL — never reuse a ticket number from earlier in the conversation or from
a previous session's summary.** A number like "DOC-XXXX" may have been mentioned
during work on a different article as a planned next ticket — it does not belong
to the current article. Always use the ticket key that was actually created and
returned by the Phase 4 script in this session. Anything else is wrong.

```powershell
cd C:\Projects\product-documentation_2
git checkout main
git pull origin main
git checkout -b DOC-XXXX
```

Replace `DOC-XXXX` with the ticket key from Phase 4 (e.g. `DOC-1730`, not whatever
was mentioned earlier in the conversation).

Run the pre-commit checklist below, then commit and push.

**PowerShell git commit — do NOT use bash heredoc syntax.**

`cat <<'EOF' ... EOF` is bash syntax. PowerShell will throw a parse error:
`The '<' operator is reserved for future use` / `MissingFileSpecification`.

Use a PowerShell here-string instead:

```powershell
$msg = @"
First line of commit message

- bullet 1
- bullet 2
"@
git commit -m $msg
```

The `@"..."@` markers must each be on their own line with nothing after the `@"` opener
and nothing before the `"@` closer.

### Pre-commit checklist

**Clean working directory — no junk files:**
- [ ] No temporary screenshots left in project roots or home folders
  (e.g. `C:\Users\...\*.png`, `C:\Projects\docops-agent2\*.png`)
- [ ] No one-off scripts created during the session that are not part of
  the article or the permanent tooling
- [ ] `git status` shows only the article file, its images, and any deleted
  old images — nothing else

**UTF-8 encoding integrity — the most common source of silent corruption:**

MDX files in this repo are UTF-8 without BOM. On Windows, any tool that reads
or writes a file without explicitly specifying UTF-8 (PowerShell `Get-Content`,
`Set-Content`, Notepad, some editors) will use the system ANSI codepage
(Windows-1252 by default). This silently corrupts every non-ASCII character in
the file — em dashes, curly quotes, arrows, accented letters — replacing them
with garbage sequences. The corruption is invisible in the editor (VS Code shows
the file correctly) but renders as garbage in the browser.

**The most common corruption pattern is `ΓÇö`** — a mangled em dash `—`.
Other patterns include `â€"`, `Ã¢â‚¬â€"`, `?` surrounded by spaces.
These appear only in the rendered article, not in the raw file — making them
easy to miss in review.

Run all three checks before committing:

- [ ] **No UTF-8 BOM.** A BOM (`\xEF\xBB\xBF`) at the start of the file breaks
  the YAML frontmatter parser and causes a blank page. Check with:
  ```powershell
  python -c "d=open('path/to/article.mdx','rb').read(); print('BOM' if d.startswith(b'\xef\xbb\xbf') else 'OK')"
  ```
  If BOM is present — strip it (see `mdx-rules.md` for the fix).

- [ ] **No CRLF line endings.** Windows tools sometimes introduce `\r\n`.
  MDX is LF-only. Check with:
  ```powershell
  (Get-Content 'path/to/article.mdx' -Raw) -match '\r\n'
  ```
  If true — convert:
  ```powershell
  $c = [System.IO.File]::ReadAllText('path/to/article.mdx', [System.Text.Encoding]::UTF8)
  $c = $c -replace '\r\n', "`n"
  [System.IO.File]::WriteAllText('path/to/article.mdx', $c, [System.Text.Encoding]::UTF8)
  ```

- [ ] **No UTF-8 encoding corruption.** Search for known garbage patterns:
  ```powershell
  Select-String 'ΓÇö|â€"|Ã¢â‚¬â€|â€"' 'path/to/article.mdx'
  ```
  Also confirm em dashes are still present (they should appear in most articles):
  ```powershell
  Select-String '—' 'path/to/article.mdx'
  ```
  If the first search has matches, or the second has no matches when em dashes
  were present — the file was corrupted. Restore from git and re-apply all edits
  using the UTF-8 safe read/write method described in `mdx-rules.md`. Never try
  to manually replace corruption patterns — restore from source.

---

## Phase 10 — Send to review

Run this phase immediately after the commit has been pushed — do not wait for separate user confirmation.

The Jira ticket was already created in Phase 4. This phase only transitions it
to In Review and records the completion.

### Step 1 — Transition to In Review and post comment

Open `c:\Projects\docops-agent2\scripts\send_to_review.py` and fill in the
three constants:

```python
TICKET = "DOC-XXXX"           # the key created in Phase 4

BRANCH = "DOC-XXXX"           # branch created in Phase 9, same as ticket key

ARTICLE_PATH = "hosting/..."  # path from docs.json, no leading slash, no .mdx
                               # e.g. hosting/virtual-servers/order-a-virtual-server
```

The script will:
1. Transition the ticket: To Do → In Progress → In Review
2. Post a comment: `Please review` + the Mintlify branch preview URL

Mintlify preview URL template:
```
https://gcore-doc-{branch-number}.mintlify.app/{article-path}
```

Where `{branch-number}` is the numeric part of the branch name
(e.g. branch `DOC-1514` → number `1514`).

Dry run first:

```powershell
cd C:\Projects\docops-agent2
.\venv\Scripts\python.exe scripts/send_to_review.py --dry-run
```

Run without `--dry-run` immediately after — do not wait for separate confirmation unless the user objects:

```powershell
.\venv\Scripts\python.exe scripts/send_to_review.py
```

After running, reset the three constants back to placeholder values so the
script is ready for the next article.

### Step 2 — Mark the article as done in the plan

Open `_planning/hosting-audit-plan.md` in `C:\Projects\product-documentation_2`,
find the article's row, and update it:

```
| done [DOC-XXXX](https://jira.gcore.lu/browse/DOC-XXXX) | DOC-XXXX | `hosting/...` |
```

### Step 3 — Write the changelog entry

Create a file at:

```
C:\Projects\product-documentation_2\_planning\changelogs\{article-slug}.md
```

Where `{article-slug}` matches the MDX filename without the extension
(e.g. `view-statistics-on-expenses.md`).

Use this template:

```markdown
# Changelog: {Article title}

**Article path:** `{relative path in product-documentation}`
**Branch:** `{branch name}`
**Jira ticket:** [{key}](https://jira.gcore.lu/browse/{key})
**Regression date:** {YYYY-MM-DD}
**Agent:** regression-test skill, phases 0-9

---

## Summary of changes

### Content fixes (from regression findings)

| # | Location | Article said | Portal shows | Fix applied |
|---|----------|-------------|--------------|-------------|
| 1 | ... | ... | ... | ... |

### Style guide fixes (Phase 5)

- ...

### MDX fixes (Phase 6)

- ...

---

## Screenshots replaced

| Old filename | New filename | Notes |
|-------------|--------------|-------|

## Screenshots removed (orphaned)

- ...

---

## Portal verification log

All elements tested in Phase 2, with pass/fail status. Every tested item must appear
in this table — either as OK or as a reference to the FINDING number that covers it.

| # | Element tested | Article says | Portal confirmed | Status |
|---|---------------|--------------|-----------------|--------|
| 1 | ... | ... | ... | OK / FINDING N |

---

## Issues noted but not fixed (out of scope)

- ...

---

## Lessons learned (skill improvements made)

- ...
```

Fill every section from the findings and fixes recorded during phases 2-6.
The changelog is for future reference — describe what was actually done,
not what was planned. If a section has nothing to report, write "None."
