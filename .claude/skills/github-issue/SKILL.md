---
name: github-issue
description: >-
  Use this skill to triage and work on GitHub issues from
  G-Core/product-documentation one at a time. It fetches the issue via gh or
  GitHub API, checks whether the work is already on main, classifies the request,
  finds the affected MDX article, creates an issue/{number}-{slug} branch, routes
  to update-page, write-from-scratch, full-audit, or cookbook, and closes the
  loop with a PR that references Closes #N. Trigger when the user says "work on
  GitHub issues", "pick up issue #1845", "next issue from the queue", pastes
  a link to github.com/G-Core/product-documentation/issues/, or asks to start
  documentation work from the issue tracker. Use BEFORE loading other writing
  skills unless the user already completed triage. Do not use for Jira tickets
  (use jira-context instead).
---
@../../../.agents/skills/github-issue/SKILL.md
