---
name: full-audit
description: Audit and update an existing documentation article by testing each step against the live Gcore portal. Use when asked to verify, audit, or fix an outdated article through portal testing.
---

Walk through an existing article as a real user would, execute every step
in the live portal using Playwright, record all discrepancies, then fix the
article. Do not skip portal verification — articles updated without testing
mislead customers.

## CRITICAL EXECUTION RULE

**Execute ONE phase per user message. After completing a phase, stop and wait.**
Do not proceed to the next phase automatically. Do not batch phases.
The user controls phase sequencing.

At the end of every phase, run this PowerShell command as the very last step:
```powershell
"a{N}_p{P}_done" | Out-File -FilePath "C:\Projects\docops-agent2\phase_done.txt" -Encoding utf8
```
Where `{N}` is the article number in the audit plan and `{P}` is the phase number.
The user will provide the exact signal string with each phase instruction.

---

## Scope — read exactly these files

Load on demand as each phase requires them:

| File | When to load |
|------|-------------|
| The target article MDX | Phase 0 |
| `.agents/references/content-types.md` | Phase 0, Phase 5 |
| `.agents/references/mcp-tools/setup.md` | Phase 1 (verify Playwright) |
| `.agents/references/mcp-tools/playwright.md` | Phase 1, Phase 3 |
| `_planning/hosting-account-map.md` | Phase 1 (hosting articles only) |
| `_planning/hosting-audit-plan.md` | Phase 0 (mark in_progress), Phase 10 (mark done) |
| `.agents/references/style-guide.md` | Phase 6 |
| `.agents/references/procedures.md` | Phase 6 |
| `.agents/references/mdx-rules.md` | Phase 7, and Phase 5 if MethodSwitch structure changes |

Do not read other articles. Do not read the API section of the article —
it is out of scope for this skill.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Article path | Yes | The MDX file to audit |
| Jira ticket | No | Additional fixes to apply in Phase 5 — does NOT limit audit scope |

---

## Platform routing (hosting articles)

Before logging in during Phase 1, determine the correct platform from the article path.
Read `_planning/hosting-account-map.md` for full platform details and current service state.

| Article path prefix | Platform | URL | How to access |
|---------------------|----------|-----|---------------|
| `hosting/` (any) | BillMgr | https://hosting.gcore.com/billmgr | Credentials: `_private/access.md` lines 13–16 |
| `hosting/virtual-servers/manage/` (VMmanager articles) | VMmanager 6 | https://sqr-v6.vm.gcore.com | In BillMgr: Products/Services → Virtual private servers → select row → **To panel**. Auto-login, no separate credentials. |
| `hosting/dedicated-servers/manage/` | DCImanager | Shown after server provisioned | In BillMgr: Products/Services → Dedicated servers → select row → **To panel**. Auto-login. |
| `cloud/` or any non-hosting path | Cloud portal | https://portal.gcore.com | SSO flow from `.agents/references/mcp-tools/playwright.md` |

If the required platform has no active service (e.g., no dedicated server provisioned yet),
stop and report the blocker to the user before doing any work.

---

## Phase 0 — Find and read the article

1. Read the full article MDX file.
2. Read `.agents/references/content-types.md`. Determine the article type:
   `how-to` | `conceptual` | `reference` | `combined`. Record it — do not change the type.
3. Extract the article's goal: what task does it walk the user through?
4. List all steps in order, noting UI elements, navigation paths, and field names.
5. List every `<Frame>` block — filename, alt text, what it shows. This is the screenshot inventory for Phase 3.
6. Note whether `<MethodSection id="portal">` exists — this is the only section being audited.
7. Open `_planning/hosting-audit-plan.md`. Find the row for this article. Change status from `todo`/`reopen` to `in_progress`.

Report to the user:
- Article type
- Goal in one sentence
- Step count
- Screenshot count
- Any obvious blocker (feature gated, account required, destructive action)

---

## Phase 1 — Open the portal and log in

1. Verify Playwright MCP is available. If not — follow `.agents/references/mcp-tools/setup.md` and stop.
2. Open an incognito browser session. This is mandatory to avoid conflicts with other open sessions.
   If incognito cannot be opened — stop and tell the user.
3. Determine the correct platform using the routing table above.
4. Navigate to the platform URL and log in using credentials from `_private/access.md`.
5. Confirm successful login by taking a screenshot of the dashboard/home screen.
6. For hosting articles: navigate to the relevant service section and confirm it is accessible.

Report: platform used, login status, dashboard screenshot.

---

## Phase 2 — Regression test

**You are a customer reading this article for the first time. You have no prior knowledge of the product. Follow the article literally.**

### Before starting

- If a step requires a resource that does not exist (server, IP, etc.) — create it now.
  This is test environment setup, not a finding.
- Resource naming: use neutral user-style names only — `my-server-1`, `my-instance-1`.
  Never use `docs-`, `audit-`, `test-`, article slugs, or Jira IDs. These names appear in screenshots.

### Execution

1. Follow each article step in order.
2. At each step, use `browser_snapshot` to read the actual current UI labels.
3. Record the result for every step:

```
VERIFIED OK: Step N — [what was confirmed]
```
or
```
FINDING: [category]
Location: Step N / screenshot [filename]
Article says: "..."
Portal shows: "..."
Action needed: rename / reorder / add step / update screenshot / remove
```

4. **Simultaneously build an execution trace** — one line per action taken in the portal.
   Append each line as you go, do not reconstruct from memory at the end:

```
TRACE | Phase 2 | BillMgr | Navigated to Products/Services → Virtual private servers
TRACE | Phase 2 | BillMgr | Clicked Order button — catalog opened at Luxembourg DC 2
TRACE | Phase 2 | BillMgr | Observed plan list: KVM-SSD-1 through KVM-SSD-8, KVM-HIGHCPU-SSD — no KVM-SAS visible
TRACE | Phase 3 | gcore.com/hosting/vds | Navigated to plan configurator, applied Luxembourg filter
TRACE | Phase 3 | gcore.com/hosting/vds | Screenshot saved as choose-a-virtual-server-for-your-needs-image2.png
```

   This trace is included verbatim in the Phase 10 changelog.

Finding categories:
- Wrong UI element names
- Changed navigation path
- Step order changed
- Missing steps
- Outdated screenshots
- Missing sections
- Wrong field names
- Deprecated options

4. After completing all steps — delete any test resources created.

### Special cases

**GUI-only articles** (install software, configure OS inside the server): skip live execution steps,
mark them as `UNVERIFIED: GUI-only step`, continue with style review phases.

**Terminal/CLI articles**: execute commands in PowerShell using real credentials from the portal.

### If blocked

```
BLOCKED at Step N: [reason — feature gated, account limitation, region unavailable]
Findings before blocker: [list]
Unverified: Steps N through M
```

**Do not apply any fixes in this phase. Collect only.**

---

## Phase 3 — Screenshot audit

Replace EVERY screenshot in the article. Do not skip screenshots that look correct — UI changes subtly.

### Preparation

Build a table before starting:

| # | Current filename | What it shows | Status |
|---|-----------------|---------------|--------|
| 1 | filename.png | description | todo |

### For each screenshot

1. Navigate to the exact screen in the portal using Playwright.
2. Collapse the sidebar (if present).
3. Zoom to the relevant area. Crop to show only what is necessary.
4. Capture with `browser_take_screenshot` using the `filename` parameter set to the **full absolute path**
   of the target file in the repo. This saves directly to the correct location — no copy step needed:
   ```
   filename: "C:/Projects/product-documentation_2/images/docs/{product}/{article-slug}/{new-filename}.png"
   ```
   Use forward slashes in the path. Always use a new filename — reusing the old name causes CDN caching issues.
5. Verify the file was saved: `git status` should show the new file as untracked in the correct folder.
   If it does not appear — the MCP saved it elsewhere. Find it with:
   ```powershell
   Get-ChildItem "$env:USERPROFILE\*.png" | Sort-Object LastWriteTime -Descending | Select-Object -First 5
   ```
   Then copy it manually with `Copy-Item` to the correct path and delete the misplaced file.
6. Delete the old file: `git rm images/docs/{product}/{article-slug}/{old-filename}.png`
7. Update the `<Frame>` block in the article: new filename, updated alt text.
8. Mark the row in the table as `done`.

Screenshot folder rule: `images/docs/{product}/{article-slug}/`
Never save to the product root folder.

Requirements for every screenshot:
- Light mode
- English UI
- No personal data visible (blur or crop out emails, IPs, account names)
- Sidebar collapsed
- Focused on the relevant UI area

**Phase 3 is complete only when ALL rows in the table are `done`.**

If a screenshot cannot be taken (platform inaccessible, feature not provisioned):
mark row as `SKIPPED — [reason]` and note it in the findings.

---

## Phase 4 — Findings summary and Jira ticket

1. Group all FINDINGs from Phase 2 by category. Present as a numbered list.
2. Report:
   - Total finding count
   - List of prerequisites (resources needed to test)
   - List of screenshots requiring replacement (from Phase 3)
   - UNVERIFIED steps and reason

3. Create a Jira ticket immediately — do not wait for a request.
   If a ticket already exists for this article — use its number and skip creation.

   Open `C:\Projects\docops-agent2\scripts\create_edge_cloud_regression_ticket.py`.
   Fill `SUMMARY` and `DESCRIPTION` with findings from Phase 2.
   Run dry-run first, show output, then run without `--dry-run`.
   After creation — reset `SUMMARY` and `DESCRIPTION` to placeholder values.

4. Record the ticket number — it is required in Phase 9 and Phase 10.

---

## Phase 5 — Apply fixes

Before starting:
- Read `.agents/references/content-types.md`. Confirm article type. Do not change it.
- If MethodSwitch structure will change — read `.agents/references/mdx-rules.md` first.

Apply all confirmed FINDINGs from Phase 2. Apply in this order:
1. Navigation paths and step order — structural changes first
2. UI element names and field names — rename throughout
3. Missing steps — add with correct prose
4. Missing sections — add new sections for undocumented features
5. Screenshots — already replaced in Phase 3; update `<Frame>` references if not done

If a Jira ticket was provided as input — apply those specific changes here too,
in addition to Phase 2 findings.

### CRITICAL: write only what you personally verified works

**Every sentence in the article must describe confirmed, working behavior.**

- If you verified a step — write exactly what you saw.
- If a step was UNVERIFIED or BLOCKED — **do not write it**. Do not guess, paraphrase, or carry over old text that you could not confirm.
- If an option, plan, or feature was not visible in the portal — **do not state it exists**. Add a note only if you can confirm it is regional or restricted, not as a fact.

**For everything unverified or unclear** — create a SME questions file:
```
C:\Projects\product-documentation_2\_planning\sme-questions\{article-slug}.md
```

Template:
```markdown
# SME questions — {article title}

**Ticket:** {jira}
**Audited:** {date}

## Questions

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | Section "..." | "..." | Not visible in portal | Is this feature deprecated / regional / gated? |
```

This file is committed to the repo. It is reviewed with the subject-matter expert before the article is published.

Do not write unverified content in the article and do not leave it silent. Every gap must appear in the SME file.

### Rules

- Use `StrReplace` only — one replacement at a time. Never use scripts for text replacement in MDX.
- For each fix: describe what changed and why.
- Wrap standalone prose inside `<MethodSection>` in `<p>` tags.
- Use `1.` for numbered steps (not `1\.`).
- Do not restructure `<MethodSwitch>` unless explicitly instructed.
- Do not touch `<MethodSection id="api">` — API sections are out of scope.
- Do not change the article filename or slug.
- Do not edit `docs.json` unless a new sidebar section is needed — confirm with user first.
- Do not update `ai-navigation` unless the article's topic fundamentally changed.

---

## Phase 6 — Style guide check

Read `.agents/references/style-guide.md` and `.agents/references/procedures.md`.

Go through every checklist item. Mark `[V]` only after real verification — never as a placeholder.
Fix every violation found. If a paragraph needs rewriting — rewrite it.
If any items remain unchecked after a full pass — re-examine those lines before finishing.

Use `StrReplace` for all edits — one replacement at a time.

---

## Phase 7 — MDX rules check

Read `.agents/references/mdx-rules.md`.

Check whether `<MethodSwitch>` is present in the article.

**If no `<MethodSwitch>`** — run basic checklist only:
- Frontmatter: `title`, `sidebarTitle`, `ai-navigation` present; no `description`
- `ai-navigation`: no `:`, `#`, `{`, `}`, `/` characters; starts with action verb; max 160 chars
- No inline backtick spans containing `{identifier}` — use `<code>` tag instead
- All internal links are root-relative (start with `/`)
- All image paths have file extension
- No `####` headings inside `<MethodSection>`
- `</MethodSection>` closing tags are at column 0

**If `<MethodSwitch>` is present** — run full checklist from `mdx-rules.md`.

Use `StrReplace` for all edits — one replacement at a time. Never use scripts.

---

## Phase 8 — LLM quality review

Run the quality review script:
```powershell
Set-Location "C:\Projects\docops-agent2"
.\.venv\Scripts\python.exe scripts\review_article_quality.py `
  --article "C:\Projects\product-documentation_2\{article-path}"
```

For each remark from the LLM — classify before acting:

| Classification | Action |
|---------------|--------|
| Valid — factual or structural problem | Apply fix immediately |
| Valid — style problem | Apply fix immediately |
| Opinion / subjective preference | Skip, note as skipped |
| Contradicts style guide | Skip, note why |
| Outside audit scope (API section, etc.) | Skip, note as out of scope |

Report to user:
- LLM score
- Each remark with classification
- Actions taken or skipped with reason

---

## Phase 9 — Commit and push

### Pre-commit checklist

- [ ] All Phase 5, 6, 7, 8 fixes applied
- [ ] No `description` in frontmatter
- [ ] No broken `<Frame>` references (all image files exist)
- [ ] Old screenshot files removed with `git rm`
- [ ] No unrelated files staged

### UTF-8 integrity check

```powershell
$bytes = [System.IO.File]::ReadAllBytes("C:\Projects\product-documentation_2\{article-path}")
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    Write-Host "BOM detected — remove it"
} else {
    Write-Host "No BOM — OK"
}
```

Also run:
```powershell
Select-String -Pattern "â€"|Ã¢|Ã©|Ã " -Path "C:\Projects\product-documentation_2\{article-path}"
```
If any matches — the file has encoding corruption. Fix before committing.

### Git workflow

```powershell
Set-Location "C:\Projects\product-documentation_2"
git checkout main
git pull origin main
git checkout -b {jira-ticket}
git add {article-path}
git add images/docs/{product}/{article-slug}/   # only if screenshots changed
git status   # verify only expected files are staged
git commit -m "{jira-ticket}: audit and update {article-slug}"
git push -u origin {jira-ticket}
```

Branch naming: use the Jira ticket number from Phase 4 (e.g., `DOC-1722`).
Always pull from main before branching. Never reuse an existing branch.
Stage files by name only — never `git add .` or `git add -A`.

---

## Phase 10 — Send to review

1. Open `C:\Projects\docops-agent2\scripts\send_to_review.py`.
   Fill the constants:
   - `TICKET` — Jira ticket number from Phase 4
   - `BRANCH` — branch name from Phase 9
   - `ARTICLE_PATH` — article path relative to repo root
   - `BLOCKED` — `True` if any steps were unverified, `False` otherwise
   - `BLOCKED_REASON` — describe what could not be tested (empty string if not blocked)

   Dry-run first, show output. Then run without `--dry-run`.
   After running — reset all constants to placeholder values.

2. Open `_planning/hosting-audit-plan.md`.
   Find the row for this article. Change status from `in_progress` to `done`.

3. Create a changelog file at `C:\Projects\update_outdated_articles\changelogs\{product}--{article-slug}.md`:

```markdown
# {Article title}

**Audited:** {YYYY-MM-DD}
**Ticket:** {jira-ticket}
**Branch:** {branch}
**Article:** {article path relative to repo root}

## Content fixes (Phase 5)

| # | Location | Article said | Portal shows | Fix applied |
|---|----------|-------------|--------------|-------------|
| 1 | Section "..." | "..." | "..." | Rewrote / added / removed |

## Style fixes (Phase 6)

- {fix description}

## MDX fixes (Phase 7)

- {fix description}

## LLM quality fixes (Phase 8)

- {fix description}

## Screenshots replaced (Phase 3)

| Old filename | New filename |
|-------------|--------------|
| old.png | new.png |

## SME questions (unverified items)

| # | Location | Article claims | Observed | Question |
|---|----------|----------------|----------|----------|
| 1 | ... | ... | Not visible | Is this deprecated / regional? |

If no open questions: `- None`

## Execution trace

All portal actions taken during this audit in order:

```
TRACE | Phase 1 | BillMgr | Login as sergey.kostichev@gcore.com — OK
TRACE | Phase 2 | {platform} | {action} — {result}
TRACE | Phase 3 | {platform} | {action} — {result}
```
```

This file goes in `C:\Projects\update_outdated_articles\changelogs\` — do NOT commit it to the product-documentation repo.

---

## Self-documentation rule

If during the audit you encounter a portal quirk, an extra required step, or a workaround —
add it to `.agents/references/mcp-tools/playwright.md` under "Known portal quirks" immediately.
Do not wait until the end of the session.

---

## Terminology rule

Never use the word `permanent` when referring to API tokens. The expiration is user-controlled.
Always write: `An [API token](/account-settings/api-tokens) is required.`
