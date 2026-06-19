---
name: full-audit
description: Audit and update an existing documentation article by testing each step against the live Gcore portal. Use when asked to verify, audit, or fix an outdated article through portal testing.
---

Walk through an existing article as a real user would, execute every step
in the live portal using Playwright, record all discrepancies, then fix the
article. Do not skip portal verification — articles updated without testing
mislead customers.

## Scope — read exactly these files

1. This SKILL.md
2. The article file specified by the user
3. `.agents/references/mcp-tools/setup.md` — verify Playwright MCP is available
4. `.agents/references/mcp-tools/playwright.md` — Playwright protocol and screenshot standards
5. `.agents/references/review-process.md` — Phase 4 review process and grep commands
6. `.agents/references/style-guide.md` — only during Phase 4 review
7. `.agents/references/mdx-rules.md` — only if making structural edits to MethodSwitch

Do not read other articles. Do not read the API section of the article —
it is out of scope for this skill.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Article path | Yes | The MDX file to audit |
| Jira ticket | No | Defines what must be fixed — but does NOT limit audit scope |

**Important:** if a Jira ticket is provided, it is an additional input to Phase 3,
not a replacement for Phases 1–2. The audit scope is always the full article —
every step, every UI element, every screenshot.

---

## Before starting — report blockers first

Before creating a branch or making any changes, check Phase 2 feasibility:

- Is the feature accessible with the test account?
- Are there destructive actions (delete, wipe) that cannot be safely tested?
- Is the feature behind a paywall or regional restriction?

If any blocker exists — **stop and tell the user before doing any work.**
Describe exactly what cannot be tested and ask how to proceed.
Do not silently proceed and bury the problem in the changelog.

---

## Phase 1 — Read the article

1. Read the full article MDX file
2. Understand the **goal**: what task does the article walk the user through?
3. Extract all steps: what to do, in what order, via which UI elements
4. List every screenshot reference (`<Frame>` blocks) — you will verify each one
5. Note the `<MethodSection id="portal">` — this is the only section being audited

Use this as your roadmap in Phase 2. The article may have errors in the details,
but it is correct enough to understand the intent and navigate the portal.

---

## Phase 2 — Portal execution (mandatory)

**Do not just read the portal. Actually perform the task.**

First, verify Playwright MCP is available. If not — follow `.agents/references/mcp-tools/setup.md` and stop.

Log in to the portal following the SSO flow in `.agents/references/mcp-tools/playwright.md`.
If Windows Hello authentication is required — ask the user to confirm it, then continue.

### Execution protocol

1. Open the portal and navigate to the section the article describes
2. Follow the article's steps in order, as a real user would
3. At each step, use `browser_snapshot` to read actual current UI labels
4. Use `browser_screenshot` to capture screens that have a corresponding screenshot in the article
5. Continue until the task is fully completed or until a genuine blocker is hit

**Resource naming during execution:** any resource you create (instance, network, bucket, etc.) must use a neutral user-style name — `my-instance-1`, `my-network-1`, `my-bucket-1`. Never use `docs-`, `audit-`, `test-`, article slugs, or Jira IDs as names. These names end up in screenshots that are published as documentation. See the full naming table in `.agents/references/mcp-tools/playwright.md`.

**Do not fix anything during Phase 2. Only collect findings.**

### What to look for

| Category | Example |
|----------|---------|
| Wrong UI element names | Article: "Click **Add Instance**" — Portal: "**Create Instance**" |
| Changed navigation path | Article: **Cloud** > **Instances** — Portal: **Cloud** > **Virtual Machines** |
| Step order changed | Article describes A then B — Portal now shows B then A |
| Missing steps | Portal has a new mandatory step the article does not mention |
| Outdated screenshots | Screenshot shows old layout, old button positions, old field names |
| Missing sections | Portal shows a new tab or option the article does not document |
| Wrong field names | Article names form fields incorrectly |
| Deprecated options | Article documents an option that no longer exists |

### Finding format

Record each discrepancy:

```
FINDING: [category from table above]
Location: Step N / screenshot [filename]
Article says: "..."
Portal shows: "..."
Action needed: rename / reorder / add step / update screenshot / remove
```

### If the task cannot be completed

Note the blocker, describe how far you got, mark specific findings as unverified:
```
BLOCKED at Step N: [reason — feature gated, account limitation, region unavailable]
Findings before blocker: [list]
Unverified: Steps N through M
```

---

## Phase 3 — Fix the article

Apply fixes based on Phase 2 findings. Fix in this order:

1. **Navigation paths and step order** — structural changes first
2. **UI element names and field names** — rename throughout the article
3. **Missing steps** — add new required steps with prose
4. **Missing sections** — add new sections for undocumented features
5. **Screenshots** — replace outdated ones last (after prose is correct)

If a Jira ticket was provided — apply those specific changes as part of this phase,
in addition to all findings from Phase 2.

### Replacing screenshots

1. Navigate to the exact screen using Playwright
2. Follow all screenshot standards from `.agents/references/mcp-tools/playwright.md`:
   - Collapse the sidebar before every screenshot
   - Zoom and crop to the relevant area
   - Light mode, English UI, no personal data visible
3. Save screenshot to the current working directory first, then copy:
   ```powershell
   Copy-Item ".\screenshot.png" `
     "C:\Projects\product-documentation\images\docs\{product}\{slug}\{filename}.png" -Force
   ```
4. **Always rename when replacing** — reusing the same filename causes CDN caching issues
5. **Delete the old file:** `git rm old-filename.png`
6. Update the `<Frame>` block reference and alt text in the article

Screenshot folder rule: `images/docs/{product}/{article-slug}/{filename}.png`
Every article has its own subfolder — never save to the product root folder.

### Adding new steps

```mdx
1. Navigate to **Section** > **Subsection**.
2. Click **Button Name**.

<Frame>
  ![Description of what is shown](/images/docs/{product}/{slug}/{filename}.png)
</Frame>
```

For numbered steps inside `<MethodSection>`, use `1.` (not `1\.`) and wrap
standalone prose in `<p>` tags. See `.agents/references/mdx-rules.md`.

### Do not touch

- `<MethodSection id="api">` — API sections are maintained separately
- Article filename and slug — broken URLs are worse than outdated content
- `docs.json` — only edit if a new sidebar section is required; confirm with user first
- `ai-navigation` frontmatter — only update if the article's topic fundamentally changed

---

## Phase 4 — Style review (mandatory)

Run after every article update. Do not skip.

Run the full 6-step process from `.agents/references/review-process.md`.
Use the grep commands in that file for each step.

---

## Git workflow

```powershell
cd C:\Projects\product-documentation
git checkout main
git pull origin main
git checkout -b update-{product}-{article-slug}
```

**Rules:**
- Always pull before branching — never branch from a stale local main
- Never reuse an existing branch — delete it and recreate from updated main
- Stage files by name only — never `git add .` or `git add -A`
- Never commit without explicit user approval
- Branch naming: `update-{product}-{article-slug}` — both product and slug, not just product

---

## Changelog file

After completing Phase 3 (before the style review), create a changelog file.
This file stays in `C:\Projects\update_outdated_articles\changelogs\` — do NOT
commit it to the product-documentation repo.

Filename: `{product}--{article-slug}.md`

```markdown
# {article path relative to product-documentation}

**Audited:** {date}

## Changes

- {change description}

## Screenshots replaced

- {filename} — {reason}

## Not updated

- {item} — {reason it could not be updated}
```

Update this file if Phase 4 introduces additional edits.

---

## Self-documentation rule

If during the audit you encounter something not covered by these instructions —
a portal quirk, an extra required step, a workaround that worked — add it to
`.agents/references/mcp-tools/playwright.md` under "Known portal quirks" immediately.
Do not wait until the end of the session. Future audits should not have to
rediscover the same thing.

---

## Output

After completing all four phases:

```
Article: [path]
Product: [product area]

Findings:
- [N] UI element names updated
- [N] navigation paths corrected
- [N] steps added / reordered
- [N] screenshots replaced
- [N] new sections added

Status: updated / no changes needed / needs manual review

Branch: update-{product}-{article-slug}
```

If the article cannot be fully verified:
```
Status: PARTIALLY UPDATED
Unverified: [list of steps that could not be tested]
Recommendation: [what is needed to complete the audit]
```

When the user confirms the result looks good — load `.agents/skills/pr/SKILL.md`
to create the branch, commit, and open a draft PR.
```


---

## Terminology rule

Never use the word `permanent` when referring to API tokens. The expiration is user-controlled.
Always write: `An [API token](/account-settings/api-tokens) is required.`
