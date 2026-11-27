---
name: product-whats-new
description: After a documentation pull request, read that PR diff and the article and write the What's new entry in the same session. Use when a docs PR has just been opened or when publishing product What's new pages.
---

# Product What's New — Claude Code

## Purpose

Separate **product news** from **documentation edits**. A changed article is evidence to investigate, not evidence that a product changed. Review each completed documentation task, including small fixes, without creating noise or inventing releases.

## Modes

- **After the PR** (default): the session that opened the pull request reads the diff and the article and writes the entry. Do not modify public What's new pages in this mode.
- **Publish** (explicit request): copy those written entries onto the product What's new page. Do not rewrite them.
- **Audit** (explicit request): scan a specified set of PRs whose entries were never written.

**Automatic invocation is not guaranteed by SKILL.md alone.** The parent workflow calls this skill after the pull request, using `references/integration.md`. Never run a broad audit automatically after each small edit.

## After the pull request

Run this in the same session that opened the pull request, after the PR exists. Read the PR diff and the changed article. Write the What's new entry from that reading. Do not write a note for another agent to analyze later. The weekly report copies `Entry` and does not interpret it again.

One product change is one entry, even when the PR touches several articles.

Write `Entry` when the diff gives customers a new feature, or changes something they already use so that the old way fails, disappears, or ends on a date. A manager can tell a customer that sentence.

Do not write an entry when the diff only does one of these:

- The article now matches behavior that was already there.
- An existing action gains a confirmation or a cancellation step.
- An SDK or CLI call changes shape and the previous API request still works.
- An error code or message changes and the result stays the same.
- The diff corrects columns, field names, or labels.
- A second tool can set a feature the portal already has, and the portal path still works.
- The date a control moved is not in the diff.

A portal check during the article work is evidence of what the screen does. It does not by itself make an entry. Preprod and production are the same evidence. Do not leave the entry unwritten because the check was on preprod or because a Jira status is still open.

If the same change already has an `Entry`, update that text. Do not add a second file.

If none of the write conditions apply, write no file and say nothing.

Do not assign scores or publish to fill a week. A bug fix gets an entry only when the old customer request now fails or the feature is gone.

## Persistent decision register

Use `.whats-new/candidates/` in the repository root (create only if the workflow permits repository changes). Store **one Markdown record per underlying product event**, not one per article; use stable readable filenames, e.g. `streaming-multi-codec-vod.md`. On repeat evaluations update the existing record rather than creating a duplicate. See `references/record-template.md`.

Do not log `Skip` decisions. Avoid logging secrets, customer data, internal-only pricing, or unapproved release details. If the repository must not contain internal metadata, use an approved external tracker instead; do not silently create public-facing records. If persistent storage is unavailable, output the decision and explicitly state that it was not saved.

When you write `Entry`, report one line in the task summary: the PR link and the first sentence of `Entry`. When you write nothing, say nothing.

## Location and navigation

Maintain **one rolling What's new page per product** immediately after its landing/overview page in that product's sidebar. Do not create a global What's new section, a new page per ticket, or a new page per release. Find actual MDX paths and navigation schema first; add the page only if it does not exist. Preserve repository frontmatter conventions and navigation ordering. Avoid assuming a path such as `/streaming/whats-new` until confirmed by the repository.

Do not publish a new product page just because no news exists. When setting up a product What's new page, require at least one approved item or an explicit instruction to create an empty placeholder.

## Public writing format

Read `references/page-template.md` before publishing. Each entry needs:
- Date or period **of confirmed availability** (never infer from commit or documentation date).
- Clear, user-facing heading stating the change.
- 1–3 short paragraphs: what changed, who benefits/is affected, and any action or constraint that matters.
- `Learn more` with direct links to the **specific updated documentation pages**, using correct internal paths. Avoid generic product landing links when a specific guide exists.

Group entries in reverse chronological order, normally by month. Prefer meaningful prose over `Added/Fixed/New` inventories. Do not list internal flags, tickets, PRs, unconfirmed release dates, marketing superlatives, or detailed step-by-step instructions. Use product terminology and link labels consistent with the repository. Do not repeat whole articles. Do not call a documentation correction a product release.

## Weekly report

When the user asks for the week, copy `Entry` from records whose `changed_on` falls in that week. Paste that text. Do not open the article again and do not rewrite the sentence. A record with no `Entry` is not in the report. One product event is one row.

## Publish procedure

1. Copy `Entry` from the records for this release onto the product What's new page. Do not rewrite `Entry`. Do not load a file that has no `Entry`.
2. Place that text on the product page with its date and the documentation link already stored on the record. Do not reopen the article to rewrite it.
3. Merge multiple candidates describing one release, and check for already published equivalent entries.
4. Edit only the relevant product page(s) and navigation if needed; keep the overview page untouched unless explicitly requested.
5. Validate MDX/frontmatter/navigation, internal links, chronological ordering, factual scope, and absence of duplicates. Run existing repository checks when available.
6. Mark candidates `Published`, recording published page and entry heading. Never mark published before the file is successfully updated.
7. Report published entries and held candidates concisely.

## Examples

Write `Entry`: a purge pattern that used to allow `*` before the extension now accepts `*` only at the end. A new orderable GPU flavor appears in a region.

Do not write `Entry`: the article was updated to match a screen that already worked. An email change gains a confirmation step. An SDK call changes shape and the previous API request still works. A status code changes from 401 to 403 and the result is the same. Terraform can set a switch the portal already has.

## Guardrails

Do not invent functionality, technical claims, customer impact, release dates, billing consequences, or links. Do not confuse document edits with product events. Do not make public updates as a side effect of article edits without explicit publication instruction. If the parent workflow prohibits extra file modifications, return a structured candidate for its tracking mechanism rather than violating scope. Respect existing approvals, branching, and publishing processes.
