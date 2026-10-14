---
name: product-whats-new
description: Evaluate every completed Gcore product-documentation ticket or article change for customer-visible product news, record Include/Skip/Needs verification decisions, and maintain one What's new page immediately after each product landing page. Use after documentation edits, ticket reviews, PR reviews, release updates, or when preparing product What's new pages in Claude Code.
---

# Product What's New — Claude Code

## Purpose

Separate **product news** from **documentation edits**. A changed article is evidence to investigate, not evidence that a product changed. Review each completed documentation task, including small fixes, without creating noise or inventing releases.

## Modes

- **Triage** (default): evaluate one completed ticket, article edit, or PR; persist an auditable decision. Do not modify public What's new pages in this mode.
- **Publish** (explicit request): reconcile approved candidates against existing product What's new, update relevant product page(s), and mark records published.
- **Audit** (explicit request): scan a specified set of completed tickets/diffs for candidates missed by triage; deduplicate against the register and existing What's new.

**Automatic invocation is not guaranteed by SKILL.md alone.** To ensure triage after every article, add the one-line integration instruction from `references/integration.md` to the parent documentation workflow or project `CLAUDE.md`. Never run a broad audit automatically after each small edit.

## Required input and evidence

Inspect the **ticket/release context**, before/after diff, the resulting article, and relevant linked product/release information available in the workspace. If only the article is available, do not infer that its subject was just released. Use repository tools and existing local evidence; do not assume access to Jira, Slack, or external systems. Identify the affected product and its documentation landing page from the actual repository navigation configuration, not from a hardcoded product list.

When evidence is incomplete, ask for the missing fact only if needed to finish the main task; otherwise mark `Needs verification` and continue.

A production account where the behavior already worked is complete evidence. Do not replace that check with `Needs verification`.

## Decision procedure (run for every completed doc task)

1. **Identify the underlying change.** Is this a new product capability, material improvement, changed behavior/default/limit, deprecation, breaking change, availability/region/pricing change, or impactful customer-facing fix? Or merely new wording, screenshots, translation, navigation, formatting, examples, regression correction, or clarification of existing behavior?
2. **Determine customer impact.** Can a user do something new, must they act differently, does an integration change, or is there a meaningful effect on reliability, compatibility, security, pricing, limits, or availability? State who is affected and what changed, not just a feature name.
3. **Establish novelty and availability.** Find evidence the product change actually shipped and when it became available. Ticket creation, documentation publication, PR merge, or new page creation **are not** release evidence by themselves. A newly documented old capability is not automatically news.

   **A production check is release evidence.** If this work used the behavior on a production account and it worked, customers already have it. Record that check as the availability evidence. Then choose `Include` or `Skip` from what the customer gained. Do not mark `Needs verification`.

   Do not wait for a Jira status, a workflow button, a resolution date, or a comment that some other bug is still open. A ticket left In Progress does not remove a capability from the production account that already has it. `Needs verification` means the change was **not** seen working on a production account, and nothing else shows that customers can use it.
4. **Check duplicates.** Search the existing product What's new page and candidate register for the same underlying release. Several tickets/pages may describe **one** product event; link all relevant docs to one candidate.
5. **Decide:**
   - `Include`: verified, customer-relevant product change, not already published. A small but impactful change can qualify.
   - `Skip`: documentation-only work, inconsequential product change, or already covered. Record a brief reason; do not write public news.
   - `Needs verification`: plausible customer-relevant product change that was not seen working on a production account, and no other evidence shows customers can use it. Record what to verify; do not publish. Do not use this status after a successful production check.

Do not assign scores, force quotas, or publish merely to maintain a cadence. Do not treat all bug fixes as news or reject all fixes: evaluate impact.

## Persistent decision register

Use `.whats-new/candidates/` in the repository root (create only if the workflow permits repository changes). Store **one Markdown record per underlying product event**, not one per article; use stable readable filenames, e.g. `streaming-multi-codec-vod.md`. On repeat evaluations update the existing record rather than creating a duplicate. See `references/record-template.md`.

Keep `Skip` decisions lightweight: append a short entry to `.whats-new/triage-log.md` containing date (only if known), ticket/PR/article reference, product, `Skip`, and reason. Avoid logging secrets, customer data, internal-only pricing, or unapproved release details. If the repository must not contain internal metadata, use an approved external tracker instead; do not silently create public-facing records. If persistent storage is unavailable, output the decision and explicitly state that it was not saved.

For every completed article, report at most one compact line in the normal task summary, e.g. `What's new: Skip — corrected an existing RTMP URL example`, `What's new: Needs verification — release date for multi-codec VOD unknown`, or `What's new: Include — new customer-facing capability (recorded)`.

Do not block publication of ordinary documentation merely because a What's new candidate needs verification. Never silently skip triage.

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

## Publish procedure

1. Load approved `Include` candidates, relevant docs, and existing product What's new.
2. Confirm release evidence, availability date, customer impact, and exact target links; recheck candidate status at publish time.
3. Merge multiple candidates describing one release, and check for already published equivalent entries.
4. Edit only the relevant product page(s) and navigation if needed; keep the overview page untouched unless explicitly requested.
5. Validate MDX/frontmatter/navigation, internal links, chronological ordering, factual scope, and absence of duplicates. Run existing repository checks when available.
6. Mark candidates `Published`, recording published page and entry heading. Never mark published before the file is successfully updated.
7. Report published entries, held candidates, and skipped changes concisely.

## Examples of classification

- Rewriting an old CDN account limits article for clarity: `Skip` — no product behavior changed.
- Correcting RTMP `?` vs `/` documentation for an already supported encoder format: `Skip` unless evidence shows a newly introduced compatibility change.
- Adding a page about HEVC/AV1/VP9: `Needs verification` only when nobody has seen it work on a production account. If a production account already used it successfully, customers have it: `Include` for a new capability, `Skip` when the page only describes behavior that was already there.
- Reseller articles rewritten from a production reseller account that already showed the new sidebar: `Skip`. The production check is the availability evidence. A Jira status of In Progress does not reopen that check.
- Changing an API parameter required by existing integrations: potentially `Include` even if a small diff; verify release and impact.
- New region, material quota change, deprecation, or paid capability: potentially `Include`, with confirmed scope and effective date.

## Guardrails

Do not invent functionality, technical claims, customer impact, release dates, billing consequences, or links. Do not confuse document edits with product events. Do not make public updates as a side effect of article edits without explicit publication instruction. If the parent workflow prohibits extra file modifications, return a structured candidate for its tracking mechanism rather than violating scope. Respect existing approvals, branching, and publishing processes.
