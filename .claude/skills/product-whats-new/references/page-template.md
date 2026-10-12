# Product What's new page pattern

Adapt frontmatter, URL, heading hierarchy, and MDX syntax to the existing repository. Locate the page in the product sidebar immediately after its overview/landing page.

```md
---
title: What's new
sidebarTitle: What's new
description: New capabilities and important changes to [Product].
---

Follow important [Product] updates here. Each entry links to documentation explaining how to use the change.

## October 2026

### [Customer-facing change heading]

[Explain what changed, why it matters, and any important availability or action in 1–3 short paragraphs.]

**Learn more:** [Specific guide](/actual/product/path), [Relevant reference](/actual/reference/path).
```

The example month and paths are placeholders, not evidence of a release. Put the newest confirmed changes first. Do not force a monthly entry if there are no meaningful changes. Do not add an extra overview paragraph to every entry. Keep one public entry per underlying change, even when several guides or tickets are involved. Only link to pages that exist in the current repository or are part of the same approved change.
