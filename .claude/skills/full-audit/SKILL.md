---
name: full-audit
description: >-
  Audits an existing article step by step against the live portal with
  Playwright, records every discrepancy (UI labels, navigation, step order,
  missing steps, screenshots, deprecated options), then fixes the article,
  creates the Jira ticket and branch, and runs the style, MDX, and LLM reviews.
  Use when the user asks to audit, verify, regression-test, or update an article
  against the real portal, when the UI changed, or when a Jira ticket asks to
  update a specific article. Not for new articles (use write-from-scratch),
  small edits without portal verification (use update-page), or API tabs (use
  api-audit).
---

Perform a complete regression test of a documentation article: follow its instructions step by step in the live portal as a real customer would, record every discrepancy, then apply all fixes and check against the style guide.

This skill is an orchestrator. It keeps the progress table and the rules. Each phase lives in its own file under `phases/` and is read only when that phase starts.

## Resuming a session

If the conversation has a prior summary, run these checks before anything else:

```powershell
git branch --show-current   # must NOT be main — must be the ticket branch
git status --short
```

If the branch is `main` and the Jira ticket was already created in Phase 4 of the previous session, do NOT create a new ticket. Run `.\.agents\tools\create_branch.ps1 DOC-XXXX` with the existing ticket key and continue from the phase where the previous session stopped.

If `send_to_review.py` already ran for this ticket, do NOT run it again. Check the ticket status first and skip Phase 10 if it is already In Review.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Article path or topic | Yes | Full path or a description to locate it |
| Portal region | No | Default: **Luxembourg-3** |

## First action — create the progress table

**This is the very first thing you do. No exceptions.** Post the table as your first message and keep it updated. Every row starts as `[ ]`. Mark `[V]` only after the specific deliverable exists.

```
| Row | Deliverable | Done |
|-----|-------------|------|
| 0a  | Article file read; full content in context | [ ] |
| 0b  | Images folder checked with check_article_images.py | [ ] |
| 0c  | Article claimed in plan (status → in_progress), or n/a if no plan file | [ ] |
| 0d  | portal_type, portal_url, login_method, jira_org_unit recorded | [ ] |
| 1   | Portal open, logged in, correct region confirmed with screenshot | [ ] |
| 2a  | Every article step followed in portal in order | [ ] |
| 2b  | Every tested element has a VERIFIED OK or FINDING block | [ ] |
| 2c  | Test resources cleaned up | [ ] |
| 3   | Screenshot checklist posted; every <Frame> row has ok / retaken / skip | [ ] |
| 4a  | All findings presented as numbered grouped list | [ ] |
| 4b  | Jira ticket created; key and URL shown | [ ] |
| 4c  | Feature branch created (create_branch.ps1 output shown) | [ ] |
| 5   | Every confirmed FINDING applied; each fix shown with before/after | [ ] |
| 5b  | All 4 anti-reference checks run: UI inventory, flow, positioning, headings | [ ] |
| 6a  | Style linter run; terminal output shown; exit code 0 | [ ] |
| 6b  | Manual checklist: every item marked [V] in the message | [ ] |
| 7   | MDX rules checklist: every item marked [V] in the message | [ ] |
| 8   | LLM review script run; score shown; score ≥ 9.5 or fixes applied | [ ] |
| 9a  | Pre-commit checklist: every item [V] in the message | [ ] |
| 9b  | git commit + push — ONLY after user says коммить/commit/пуш/push | [ ] |
| 10  | Jira status confirmed; plan file row updated to done (if a plan file exists) | [ ] |
```

### Gate rule — before every [V] mark

Write one sentence naming the specific evidence:

> **Evidence:** [exact output / screenshot / terminal line / file path that proves this row is done]

If you cannot name specific evidence, the row is not done. For these rows the evidence is the **literal output pasted inline**, not a sentence:

| Row | Required inline output |
|-----|------------------------|
| 0b  | The checker output |
| 0c  | The exact line changed in the plan file (old → new) |
| 4b  | The Jira URL printed by the script |
| 4c  | The `create_branch.ps1` output line |
| 6a  | The full style linter output block (last line must be `OK` or list what was fixed) |
| 6b  | The full manual checklist with every item marked `[V]` |
| 7   | The full MDX checklist with every item marked `[V]` |
| 8   | The score line from the review script (e.g. `Score: 9.64 / 10`) |
| 9b  | The `git commit` output line and the `git push` output line |
| 10  | The plan file line after update (status = done) |

"Evidence: exit code 0" without the actual output does not satisfy the gate. Rerun and paste.

### Phase-end gate — before moving to the next phase

At the end of every phase repost the full table, count the rows that belong to the completed phase, and count how many are `[V]`. If any is still `[ ]`, stop and do it now. Reposting the table is the verification mechanism and is not optional.

### Todo list

Also create a todo list with every phase set to `pending` and advance it in step with the table.

## One phase at a time

Work on exactly one phase and finish it completely. Read the phase file only when you reach that phase. Do not read ahead and do not plan the next phase while executing the current one. When a phase is done, report what was completed and immediately start the next phase without asking for permission.

**Exception — after Phase 10:** stop completely. Do NOT move to the next article. Wait for explicit user instruction.

## Phases

| Phase | File | What it does |
|-------|------|--------------|
| 0 | [phase-0-prepare.md](phases/phase-0-prepare.md) | Find and read the article, portal and Jira routing, claim in plan, check image folders |
| 1 | [phase-1-portal-login.md](phases/phase-1-portal-login.md) | Open an isolated browser session and log in |
| 2 | [phase-2-regression-test.md](phases/phase-2-regression-test.md) | Follow every step in the portal, record VERIFIED OK and FINDING blocks |
| 3 | [phase-3-screenshots.md](phases/phase-3-screenshots.md) | Compare screenshots with the portal, retake outdated ones |
| 4 | [phase-4-findings-ticket-branch.md](phases/phase-4-findings-ticket-branch.md) | Present findings, create the Jira ticket and the ticket branch |
| 5 | [phase-5-apply-fixes.md](phases/phase-5-apply-fixes.md) | Apply the confirmed findings to the article |
| 5b | [phase-5b-structure-review.md](phases/phase-5b-structure-review.md) | Structure, flow, and positioning review |
| 6 | [phase-6-style-check.md](phases/phase-6-style-check.md) | Style linter and manual style checklist |
| 7 | [phase-7-mdx-check.md](phases/phase-7-mdx-check.md) | MDX rules checklist |
| 8 | [phase-8-llm-review.md](phases/phase-8-llm-review.md) | Automated LLM quality review |
| 9 | [phase-9-precommit.md](phases/phase-9-precommit.md) | Pre-commit checklist; commit and push only on request |
| 10 | [phase-10-send-to-review.md](phases/phase-10-send-to-review.md) | Move the ticket to In Review and post the preview link |

Shared by several phases: [finding-formats.md](finding-formats.md) (VERIFIED OK, FINDING, UNVERIFIED, ticket description).

## References loaded by phases

Read a reference only in the phase that names it:

- `.agents/references/product-routing.md` — Phase 0
- `.agents/references/mcp-tools/playwright.md` — Phases 1, 2, 3
- `.agents/references/content-types.md` — Phase 5, before rewriting any section
- `.agents/references/mdx-rules.md` — Phases 5 (if MDX structure changes) and 7
- `.agents/references/sdk-best-practices.md` — Phase 5, if fixing SDK code examples
- `.agents/references/docs-styleguide-anti-reference.md` — Phase 5b
- `.agents/references/style-guide.md` and `procedures.md` — Phase 6
- `.agents/references/ticket-and-branch.md` — Phase 4

Do not read other articles for context unless they are directly linked from the article being tested.

## Hard rules

- Never commit or push until the user says `коммить`, `коммит`, `commit`, `пуш`, `пушь`, `push`, `закоммить`, or `запушь`.
- Never touch `<MethodSection id="api">`: API sections are a separate update cycle (`api-audit`).
- Never rename article files, change slugs, or edit `docs.json` without explicit user confirmation.
- Never read `.env`, `access.md`, or `_private/secrets/`. The agent never handles portal credentials: the user logs in.
- Never change the browser viewport, window size, or zoom.
- Apply only fixes from the confirmed findings. Note other issues at the end; do not fix them silently.
- Never use scripts for text replacements in MDX. Use targeted edits, one replacement at a time.
