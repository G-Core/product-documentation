---
name: api-use-case
description: >-
  Adds a REST API tab as a MethodSection id api inside a MethodSwitch to an
  existing Customer Portal documentation article, mapping each Portal step to the
  matching endpoints from the product's OpenAPI spec in
  /api-reference/services_documented/. Use this skill when the user wants to give
  API coverage to a portal-only article or build the REST API side of a tabbed
  (Portal + API) article — for example "add an API tab to this article", "add API
  coverage to this guide", "write the REST API section for this page", "add a REST
  API method to this doc", "map these portal steps to API calls", or "show the API
  version of these steps". It reads the article, optionally runs live curl calls to
  verify responses, writes Python SDK / Go SDK / curl examples with quickstart and
  step-by-step sections, wraps content in MethodSwitch, and updates ai-navigation
  frontmatter. Do not use it to write a brand-new article from scratch or to audit
  an existing one — only to add the API method to an article that already exists.
---
@../../../.agents/skills/api-use-case/SKILL.md
