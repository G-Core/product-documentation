---
name: changelog-label
description: >-
  Decides whether a documentation change is customer-facing product news and,
  when it is, drafts one changelog feed record, rebuilds changelog.mdx, and
  labels the pull request. Use when opening a pull request (the pr skill calls
  it before staging), after a documentation edit, or when the user asks whether
  a change belongs in the changelog. The decision depends on customer impact,
  not on diff size, and repo-only or documentation-only changes are skipped.
  It never commits, pushes, or opens a pull request, and it does not edit
  streaming/whats-new.mdx.
---

# Changelog label

Decide if this change belongs on the public changelog. Size does not matter. A one-line API break can qualify. A large rewrite of existing behavior does not.

This skill does not commit, push, or open a pull request. The `pr` skill does that and calls this skill first.

Do not edit `streaming/whats-new.mdx`. That page stays until the global changelog is in production.

Do not rewrite old feed records. The only edits allowed to an existing feed file are the two under Duplicates: add a source to the record that covers the same change, or add an `id` to `distinct_from`.

The decision is a proposal. The reviewer can edit the feed record or remove it before merge.

## When to run

Run once per pull request, on the article diff for this session. Repo-only work (skills, CI, styles, scripts) is `Skip` unless the user is changing a customer product. A repo-only `Skip` gets only the `Changelog:` line in the pull request body. It is not logged, because it is not a decision about a product article.

If this skill already ran earlier in the session and the pull request opens on a later day, set `announced_at` again to the pull request day and update the date sentence in the pull request body.

Read the diff before deciding:

```powershell
git diff -- '*.mdx'              # changes not committed yet
git diff main...HEAD -- '*.mdx'  # changes already committed on the branch
```

## Decision

Answer one question: after this change, can the customer do something new, or must they act differently?

`Include` when any of these is true:

- A new customer capability.
- A changed default, limit, region, price, or compatibility.
- A deprecation or a breaking change, including a small API or parameter change that existing integrations must follow.
- An impactful fix of product behavior. A fix of the documentation itself is not this.

`Skip` when the product behavior is unchanged. Examples:

- Typo, grammar, formatting, or frontmatter.
- Sections reordered, renamed, or moved, with the same facts.
- Screenshot added or replaced.
- Navigation, tab, or anchor change.
- Clearer wording for something the product already did.
- A new API or Terraform tab that documents existing behavior.
- Examples, translation, or style.

`Needs verification` when the diff looks like a product change but the article does not say what the customer can do now. Do not guess. Do not write a feed record. A missing customer date is not this case: use the pull request day, as the date rule below says.

## Duplicates

Before writing a file, search `.whats-new/feed/` and `.whats-new/candidates/` for the same product change. Match a source ticket, the same guide and the same behavior, or a candidate that already describes it. Several tickets for one change share one feed record.

- A feed record already covers this change: `Skip`. Do not write a second record. Add the new ticket to `sources` on the existing record when this pull request is that same change.
- A candidate already describes it: update that candidate. Do not create a second candidate file.
- Two feed records share a source and describe different changes: each lists the other's `id` in `distinct_from`. These two edits to an existing feed file are the only ones allowed.

## Include: draft the feed record

Write one new file, `.whats-new/feed/{id}.json`. Do not edit other feed files, except as Duplicates allows.

`id` is `{folder}-{short-slug}`, unique, stable, lowercase. `folder` is the docs folder (`streaming`, `cdn`, `cloud`) and must be a key in `.whats-new/products.json`. Check that the id is free before writing:

```powershell
Get-ChildItem .whats-new/feed -Name
```

```json
{
  "id": "cdn-example",
  "product": "cdn",
  "title": "Customer-facing title in the present tense",
  "summary": "One or two sentences about what the customer can do. No announcement language.",
  "available_since": "YYYY-MM-DD",
  "announced_at": "YYYY-MM-DD",
  "url": "/changelog#cdn-example",
  "guide_url": "/cdn/article-path",
  "guide_label": "Short link text",
  "kind": "new",
  "sources": ["DOC-0000"],
  "distinct_from": []
}
```

Rules for the fields:

- `summary` is the only text the page shows. One or two sentences must explain the change without a headline. Write a statement, not an instruction. "The outbound security group rule field is now called Targets." is a statement. "Name the outbound security group field Targets." is an instruction.
- `title` is stored and is not shown. The permanent URL uses `id`, not `title`.
- Do not write "now available", "added", or "we have introduced".
- `kind` is `new`, `improved`, or `fixed`.
- `announced_at` is the day this pull request is opened (`Get-Date -Format yyyy-MM-dd`). That date is what moves the product card. If the pull request opens on a later day than the record was written, set it again.
- `available_since` is the day the customer got the change, when the article or ticket states it. If it does not, use the same day as `announced_at` and say so in the pull request body.
- `url` is always `/changelog#{id}`. The script rejects any other value.
- `guide_url` is the article this change documents. It must be an existing page, and an existing heading if it has an `#anchor`. `guide_label` is a short name, not a sentence.
- `sources` must not be empty and is not shown on the page. Use the Jira key of the branch (`DOC-XXXX`), or the issue number for GitHub issue work. The pull request number does not exist yet when the record is written.
- `distinct_from` is `[]` unless another feed record has the same source. Then each of the two records lists the other's `id` here. Without that mark the script rejects both.
- `summary` must not contain `{`, `}`, `/`, `:`, `#`, backticks, square brackets, or `|`. The script rejects the braces. Avoid the other characters as well.

Then rebuild the page from the repository root. The script uses only the standard library, so no virtual environment is needed:

```powershell
python scripts\build_changelog.py --repo .
python scripts\build_changelog.py --repo . --check
```

The first command writes `changelog.mdx`. The second must exit 0: it confirms the page matches the feed. Do not hand-edit `changelog.mdx`. If the script fails, fix the feed record. Do not publish a record the script rejects.

## Register

One candidate file per underlying product change, in `.whats-new/candidates/`.

`Include` writes or updates `.whats-new/candidates/{id}.md`. Set `published_as` to the feed `id`. If a candidate for this change already exists under another name, update that file and set `published_as` there.

```md
---
product: cdn
status: Include
published_as: cdn-example
available_since: YYYY-MM-DD
---

# cdn-example

Customer change: The summary from the feed record.
Affected users: Who can now do something or must act differently. Optional.
Evidence: Where the change and its date come from.
Open verification: What is still unconfirmed. Required for Needs verification, otherwise optional.
Sources: DOC-0000
Guide: /cdn/article-path
Duplicate check: not found
```

- `product` is the docs folder key from `.whats-new/products.json`, in lowercase.
- A candidate that produced several feed records (an older backfill) lists every id as a YAML list in `published_as` and omits `available_since`, because each feed record carries its own date.

`Needs verification` writes or updates a candidate with `status: Needs verification`, no `published_as`, and an `Open verification:` line that names what is missing. It does not write a feed file.

`Skip` on a product article change appends one line to `.whats-new/triage-log.md` and does not write a candidate or a feed file. A repo-only `Skip` writes nothing (see When to run).

```md
- YYYY-MM-DD — DOC-0000, article path — CDN — Skip — reason
```

Return every path this skill wrote, so the `pr` skill can stage them: the feed JSON and `changelog.mdx` for `Include`, the candidate file when one was written or updated, and `.whats-new/triage-log.md` for a `Skip` that was logged. A repo-only `Skip` returns no paths.

## Label

The label is applied only for `Include`, and only after `gh pr create` returns a URL.

```powershell
gh pr edit {number} --add-label changelog
```

If GitHub reports that the label does not exist, create it once and retry. This adds a label to the shared repository, so it happens once and is mentioned to the user:

```powershell
gh label create changelog --description "Customer-facing product change" --color "E86A17"
gh pr edit {number} --add-label changelog
```

`Skip` and `Needs verification` do not get the label and do not get a feed file.

## Report

One line, in English, included in the pull request body under What changed:

- `Changelog: Include — {id}`
- `Changelog: Skip — {reason}`
- `Changelog: Needs verification — {what is missing}`

When `available_since` was set to the pull request day because the article and ticket give no date, add one more sentence to the body: `Customer availability date not stated; the pull request day is used.`

Example for repo-only work: `Changelog: Skip — repo-only change (agent rules and build tooling), product behavior unchanged`.
