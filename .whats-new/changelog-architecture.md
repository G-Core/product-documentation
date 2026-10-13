# Gcore changelog architecture

The public site is static. A browser does not fetch news when the page opens. "Dynamic windows" means the showcase is rebuilt from stored records whenever a news item is announced. Hand-editing the showcase is not part of the workflow.

Three stages:

1. Detect. Automation finds possible changes.
2. Decide. A person accepts, skips, or holds each candidate. This stage exists so one product cannot publish every commit.
3. Assemble. Automation rebuilds `changelog.mdx` from accepted records. The decision drafted on the pull request is a proposal. The reviewer accepts it by merging, or edits or removes the feed record before merge.

GitHub releases never skip the decision stage. A release can contain internal fixes and dependency bumps. It becomes a candidate, not a public item.

## Stored records

One file per published news item under `.whats-new/feed/`. Each file is JSON. Candidates in `.whats-new/candidates/` record Include and Needs verification. Skip is one line in `.whats-new/triage-log.md`. The feed contains only items that are allowed on the public page.

Fields:

- `id`. Stable slug, unique across products. It does not change when a product folder is renamed.
- `product`. Current docs folder, such as `streaming` or `cdn`.
- `title`. Customer-facing change, not a documentation topic.
- `summary`. One or two sentences.
- `available_since`. ISO date for the history month. For the current backfill this is the documentation commit date.
- `announced_at`. ISO date this news item was published. This is the date that moves a product window.
- `url`. Permanent path on the changelog page, `/changelog#{id}`. It is not rewritten when a product folder changes.
- `sources`. Tickets, release URLs, or doc commits used as evidence. Not shown on the page.

`available_since` groups the product history by the month the customer got the change. `announced_at` orders the showcase. Announcing a September capability on 12 October lifts that product's window on 12 October. The history entry stays under September.

A candidate that is accepted stores `published_as` set to the feed `id`. A later detect pass sees that mark and does not open a second candidate for the same change.

Products with no feed records do not get a window.

## Order

Showcase windows sort by the latest `announced_at` in that product, newest first. Equal dates sort by the product folder name.

Entries inside a window sort by `announced_at`, newest first. Equal dates sort by `id`. Months inside a window follow `available_since`. The same files always produce the same page.

## Checks before write

The generator refuses to write pages when any of these fail:

- `product` is not a current docs folder and is not in the rename map below.
- `url` is not `/changelog#{id}`.
- `guide_url` does not point at an existing page, or its anchor is missing on that page.
- Two feed records share an `id`.
- Two feed records list the same source and neither is marked as a distinct change. The mark is a field on the record, `distinct_from`, naming the other `id`.

## Renames

A product folder rename or merge does not change feed `id` values or `url` values. A short map in the generator config points the old folder name at the current one, and that map is used only to place the window. Old public paths get redirects in `docs.json`. Historical links keep working.

## One page, one feed

The generator reads the feed and writes `changelog.mdx`. Nobody edits that file by hand.

Each product is one full-width card. A filter column lists products and counts. The first cards are open; the rest start as a single header row. An open card shows the five latest updates. One control expands that card with the updates that did not fit. "View all" opens the same product as a full history grouped by month. The anchor on an entry is the permanent URL, `/changelog#{id}`.

A separate product What's new page is not generated. `streaming/whats-new.mdx` stays as a static page until the global changelog is in production.

## What runs automatically

### Assemble, first

`scripts/build_changelog.py` reads `.whats-new/feed/` and writes `changelog.mdx`.

A pull request check runs the same script and fails if the generated files do not match the feed. Shipping a feed record without the regenerated pages is not possible.

Adding one feed record and running the script adds that entry to the product window and moves the window when the new date is the latest.

### Detect inside this repository, second

A workflow looks at commits that touch product article folders. It opens or updates a candidate in `.whats-new/candidates/` with status Needs verification. It does not write the feed and does not change the public page. It skips sources already listed on a feed record or on a candidate with `published_as` set.

`changelog-label` decides on the pull request whether the article change is a product change. Only an accepted record, with both dates and a working `url`, is copied into `.whats-new/feed/`. The candidate then stores `published_as` set to that feed `id`. A `Skip` is one line in `.whats-new/triage-log.md`.

### Detect in product repositories, third

A scheduled workflow, same pattern as `check-api-sdk` and `check-terraform-provider`, reads a map of product to GitHub repository. For each new release or changelog entry it opens a draft candidate and a documentation PR. It does not publish.

The map is maintained in this repo. A release with no documentation URL stays a candidate. It cannot appear on the showcase, because every public item needs a permanent docs URL.

Release text is evidence. It is not copied onto the page unchanged.

### Feed file, later

An RSS or Atom feed can be generated from the same records. It is not part of the first version. The static HTML and the permanent product URLs are enough for search and for readers.

## What stays manual

- The customer-facing title and summary.
- `available_since`. Use the day the article or ticket says the customer got the change. When neither states that day, use the pull request open day and say so in the pull request body. The current backfill keeps the documentation commit date.
- `announced_at`, set when the item is accepted for the public page.
- The decision to skip a documentation edit, or to mark a candidate as already published.
- Creating the docs article that the permanent URL points at.
- The rename map and the redirects.

## Not in this design

- A request from the browser to an API that holds the news.
- Windows for products that have no accepted records.
- Hand-written order of windows.
- Publishing a GitHub release without a human decision.
