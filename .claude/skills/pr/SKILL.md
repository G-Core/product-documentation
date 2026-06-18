---
name: pr
description: >-
  Creates a draft GitHub pull request for documentation changes made in the current
  session. Use this skill at the very end of a docs workflow, after another skill
  (write a new doc, add an API tab, update an article, audit an article, or
  contributor feature draft) has finished and the user wants to ship the work.
  Trigger on phrases like "open a PR", "create a pull request", "raise a PR for
  these changes", "push this and make a draft PR", "submit my doc changes", "ship
  this article", or "let's get this reviewed". It checks gh and git auth, optionally
  starts a Mintlify local preview, derives the product name from the file path,
  creates a correctly named branch, stages only the session's files, commits with a
  [Product] message, pushes, and opens a draft PR (--base main --draft) with a What
  changed / Files changed / TODO body. Do not use it to make documentation edits —
  only to package finished work into a PR.
---
@../../../.agents/skills/pr/SKILL.md
