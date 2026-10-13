---
name: changelog-label
description: >-
  Decide whether a documentation change is customer-facing product news.
  Use when opening a pull request, or when the user asks if a change belongs
  in the changelog. A changelog decision depends on customer impact, not on
  diff size. On Include, draft one feed record and rebuild changelog.mdx.
  Apply the GitHub label changelog only after the pull request exists.
---

# Changelog label

Decide if this change belongs on the public changelog. Size does not matter. A one-line API break can qualify. A large rewrite of existing behavior does not.

This skill does not commit, push, or open a pull request. The `pr` skill does that and calls this skill first.

Do not edit a product What's new page. Do not rewrite old feed records.

## When to run

Run once per pull request, on the article diff for this session. Repo-only work (skills, CI, styles, scripts) is `Skip` unless the user is changing a customer product.

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

`Needs verification` when the diff looks like a product change but the article does not say what the customer can do now. Do not guess. Do not write a feed record.

## Include: draft the feed record

Write one file, `.whats-new/feed/{id}.json`. Do not edit other feed files.

`id` is `{folder}-{short-slug}`, unique, stable, lowercase. `folder` is the docs folder (`streaming`, `cdn`, `cloud`).

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
- `announced_at` is the day this pull request is opened. That date is what moves the product card.
- `available_since` is the day the customer got the change, when the article or ticket states it. If it does not, use the same day as `announced_at` and say so in the pull request body.
- `guide_url` is the article this change documents. `guide_label` is a short name, not a sentence.
- `sources` is the Jira key or the pull request number. It is not shown on the page.
- `summary` must not contain `{`, `}`, `/`, `:`, `#`, backticks, square brackets, or `|`.

Then rebuild the page from the repository root:

```powershell
.\.venv\Scripts\python.exe scripts\build_changelog.py --repo .
```

The script writes `changelog.mdx`. Do not hand-edit that file. If the script fails, fix the feed record. Do not publish a record the script rejects.

Return the two paths so the `pr` skill can stage them: the feed JSON and `changelog.mdx`.

## Label

The label is applied only for `Include`, and only after `gh pr create` returns a URL.

```powershell
gh pr edit {number} --add-label changelog
```

If GitHub reports that the label does not exist, create it once and retry:

```powershell
gh label create changelog --description "Customer-facing product change" --color "E86A17"
gh pr edit {number} --add-label changelog
```

`Skip` and `Needs verification` do not get the label and do not get a feed file.

## Report

One line, included in the pull request body:

- `Changelog: Include — {id}`
- `Changelog: Skip — {reason}`
- `Changelog: Needs verification — {what is missing}`
