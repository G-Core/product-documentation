---
name: regression-test
description: Full regression test of an existing article against the live portal. Use when articles may be stale and need end-to-end verification against the current portal UI before updating.
---

Perform a complete regression test of a documentation article: follow its instructions
step by step in the live portal as a real customer would, record every discrepancy,
then apply all fixes and check against the style guide.

---

## STRICT RULE: one phase at a time

**Work on exactly one phase. Finish it completely. Then stop.**

Do not read ahead. Do not plan the next phase while executing the current one.
Do not try to hold all phases in mind simultaneously.
The goal is not speed — it is thoroughness within each isolated step.

When a phase is done:
- Report what was completed
- Immediately start the next phase without asking for permission

Violating this rule produces shallow work across all phases instead of
deep work within each phase. This is forbidden.

---

## Scope — read exactly these files

1. This SKILL.md
2. The article file identified in Phase 0
3. `.agents/references/style-guide.md` — Phase 5 only
4. `.agents/references/procedures.md` — Phase 5 only (numbered steps check)
5. `.agents/references/content-types.md` — Phase 4 only (before rewriting any section)
6. `.agents/references/mdx-rules.md` — Phase 4 (if MDX structure is changed) and Phase 6
7. `.agents/references/mcp-tools/playwright.md` — Phase 1 and Phase 2

Do not read other articles for context unless they are directly linked from the
article being tested.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Article path or topic | Yes | Full path or description to locate it |
| Portal region | No | Default: Luxembourg 3 (`ed-3`) |

---

## Phase 0 — Find and read the article

If the article path is given — open the file directly.

If only a topic is given — search the repository:

```powershell
rg "keyword" --glob "*.mdx" -l
```

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

Follow the SSO login flow from that file exactly:

1. Navigate to `https://auth.gcore.com/login/signin`
2. Click **SSO**
3. Enter `gcore.com` in the Work domain field and press Enter
4. Enter `sergey.kostichev@gcore.com` on the Microsoft login page and click **Next**
5. **STOP — ask the user to complete Windows Hello authentication**
6. Wait for confirmation, then verify the browser is at `https://portal.gcore.com`

After login, navigate to the region the article targets.
Default region: **Luxembourg 3 (`ed-3`)**.
Verify the correct region is selected in the portal header before starting any steps.

---

## Phase 2 — Regression test

**Mindset: you are a customer reading this article for the first time.**
You have no prior knowledge of the product. You follow the article literally.
If something is unclear, confusing, or missing — it is a finding.

### Execution rules

- Follow the article's steps in exact order.
- At each step, use `browser_snapshot` to read the actual current UI labels, button
  names, field names, and navigation paths.
- If the article says to create something — create it.
- If the article says to delete something — delete it.
- If something the article describes does not exist or works differently — do not skip it.
  Explore what the portal actually shows now and document the divergence as a FINDING.
- If a step requires a prerequisite resource (a network, a cluster, an SSH key,
  a volume, etc.) that does not yet exist:
  - Do not create it silently — note it as a finding.
  - Check whether a documentation article exists for creating that resource.
  - Record: `PREREQUISITE: [resource type] — covered in [article path or "no article found"]`
  - Do not proceed to test that other article — only note the dependency.
- If a feature is unavailable in this region or account — note it as a finding,
  describe how far you got, and mark related findings as UNVERIFIED.

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

### Screenshot audit

For every `<Frame>` in the article:

1. Navigate to the same screen in the portal.
2. Use `browser_snapshot` to read the actual current UI.
3. Compare what the article screenshot is supposed to show vs. what the portal shows now.
4. If they differ — record a FINDING with category `Outdated screenshot`.
5. Decide whether to capture now or defer:

**Capture NOW (during Phase 2)** — only when the portal state is transient and cannot
be reproduced later without repeating the full flow:
- A dialog that appears only mid-wizard (e.g., "Create resource" confirmation screen)
- A state that depends on a resource you just created during this test run
- An error message or validation state that requires a specific trigger

**Defer to Phase 4** — for all static UI screenshots that can be retaken at any time:
- Page views, filter panels, table lists, graph tabs
- Any screen reachable by navigation without prerequisites

For deferred screenshots, note the FINDING with the portal URL and the
navigation path needed to reach the screen again. The screenshot will be taken
in Phase 4 after all text fixes are applied.

For screenshots captured now, save to:
```
C:\Projects\product-documentation\images\docs\{product}\{article-slug}\{filename}.png
```
Use a new filename — never overwrite the old file directly (CDN caching).
Note both the old filename and the new filename in the FINDING.

**Do not apply any fixes during this phase. Collect all findings first.**

After completing all steps and the screenshot audit, clean up any test resources
created during testing (instances, networks, etc.).

---

## Phase 3 — Findings summary

After completing Phase 2, present all findings to the user as a numbered list
grouped by category.

Also present:
- Total number of findings
- List of prerequisites noted, with article paths where available
- List of screenshots that need replacement, with old and new filenames
- Any steps where the feature was unavailable (UNVERIFIED)

Ask the user: "Should I proceed with applying all fixes?"

Wait for explicit confirmation before starting Phase 4.

---

## Phase 4 — Apply fixes

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

## Phase 5 — Style guide check

Load `.agents/references/style-guide.md` and `.agents/references/procedures.md` now.

Work through the article section by section and verify each rule. Do not skim.

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

**Links:**
- [ ] No standalone "For more details, see [X]" sentences
- [ ] Link text 1–2 words maximum
- [ ] First mention of portal: `[Gcore Customer Portal](https://portal.gcore.com)`
- [ ] Subsequent mentions: plain "the Customer Portal" (no link)

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

---

## Phase 6 — MDX rules check

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
- [ ] Inside `<MethodSection>`: prose adjacent to `<Frame>`, code blocks, or `<Tabs>` IS wrapped in `<p>`; prose between numbered steps IS wrapped in `<p>`; bullet lists are NOT wrapped in `<p>`
- [ ] `<Frame>` wraps each screenshot; no bare `![]()` outside `<Frame>`
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

---

## Phase 7 — Present for review

After completing Phase 6, present the article to the user for review.

Report:

```
Article: [path]

Regression findings applied: N
  - [brief description of each]

Style guide fixes applied: N
  - [brief description of each]

Unresolved / unverified findings:
  - [finding] — reason unverified

Prerequisites noted (not tested):
  - [resource type]: covered in [article path] / no article found

Unrelated issues noticed (not fixed):
  - [issue] at [location] — recommend fixing separately

Screenshots replaced: N
  - Old: [filename] → New: [filename]
```

Wait for the user's review feedback. Apply any additional fixes requested.

**When applying review feedback — verify before fixing.**

Do not apply review feedback blindly. Before making any change the user requests:

1. Check whether it is factually correct — verify against the portal snapshot,
   the article text, or the findings collected in Phase 2.
2. If the requested change conflicts with what the portal actually shows,
   or contradicts a finding already recorded — say so explicitly.
   State what the portal shows and why the change may be incorrect.
3. Only apply the fix after the user confirms, or after you have verified
   that the change is accurate.

**Never silently apply a correction that you have reason to believe is wrong.**
The review is a conversation — if the user is mistaken about a UI label, a
button name, or a factual detail, say so. Do not assume the user is always right
about portal details; they may not have the portal open in front of them.

**Do not create a commit or push until the user explicitly says to.**

When the user approves, run the pre-commit checklist below, then load
`.agents/skills/pr/SKILL.md` to create the branch, commit, and open a draft PR.

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

## Phase 8 — Create Jira ticket

Run this phase only after the PR has been pushed and the user confirms.

Open `c:\Projects\docops-agent2\scripts\create_edge_cloud_regression_ticket.py`
and fill in `SUMMARY` and `DESCRIPTION` with the actual article name and the list
of changes applied. Use past tense — describe what was done, not what to do.

Format:

```
SUMMARY = "Update {article title}"

DESCRIPTION = (
    "Updated the '{article title}' article:\n\n"
    "- {change 1}\n"
    "- {change 2}\n"
    "- {change 3}"
)
```

Do a dry run first to confirm the values look correct:

```powershell
python scripts/create_edge_cloud_regression_ticket.py --dry-run
```

Show the dry-run output to the user and wait for confirmation before creating
the ticket. After confirmation:

```powershell
python scripts/create_edge_cloud_regression_ticket.py
```

Report the created ticket key and URL to the user.

After the ticket is created, open `docs/PLAN_EDGE_CLOUD_UPDATE.md` in the
`docops-agent2` repository and mark the article as done. Find the article's row
in the plan table and add the Jira ticket key to it, or update the status column
to indicate the article has been fully updated and the ticket created.

```powershell
# Plan file location
C:\Projects\docops-agent2\docs\PLAN_EDGE_CLOUD_UPDATE.md
```
