---
name: full-audit
description: >-
  Audits an existing documentation article by walking through every step against
  the live portal with Playwright, recording all discrepancies (wrong UI labels,
  changed navigation paths, reordered or missing steps, outdated screenshots,
  deprecated options), then fixing the article and running a mandatory style
  review. Use this skill when the user wants to verify, audit, test, or update an
  existing/outdated article by checking it in real conditions — e.g. "audit this
  article", "verify this doc against the portal", "this article is outdated, update
  it", "test these steps in the live portal", "check the screenshots are current",
  "the UI changed, fix the doc". Also use when a Jira ticket asks to update a
  specific article (the ticket adds required changes but the audit still covers the
  whole portal section). For writing a brand-new article from scratch, use
  write-from-scratch instead; for a small targeted edit to one page without portal
  verification, use update-page.
---
@../../../.agents/skills/regression-test/SKILL.md
