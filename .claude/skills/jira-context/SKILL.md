---
name: jira-context
description: >-
  Use this skill to analyze a Jira ticket and produce a structured documentation
  brief: it fetches the ticket and any linked dev/Confluence pages, checks status,
  classifies whether the change is customer-facing (PUBLIC_PRODUCT_DOC,
  PUBLIC_TROUBLESHOOTING, BUG_FIX, INTERNAL_DOC, NOT_DOCUMENTABLE,
  INCIDENT_POSTMORTEM), finds the affected article, scores update complexity, and
  recommends the next skill. Trigger it whenever the user gives a Jira ticket ID or
  URL (especially a DOC-#### key) and asks what work is needed, for example "look
  at DOC-1234", "what does this ticket need", "should we document this ticket", "is
  this ticket documentable", "triage this Jira ticket", "what doc work does this
  require", or pastes a Jira link and asks to understand the change. Use it BEFORE
  writing or editing any article, since it only produces a brief and decides
  whether documentation work should happen at all. Do not use it to actually write
  or update docs (use update-page or write-from-scratch after).
---
@../../../.agents/skills/jira-context/SKILL.md
