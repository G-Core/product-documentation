---
name: cookbook
description: >-
  Compiles an end-to-end, multi-product cookbook article that stitches together
  steps from several Gcore products into one unified scenario guide, with explicit
  cross-product handoffs and an expected-outcome section. Use this skill when the
  user asks to write a cookbook, a use-case guide, an end-to-end or integration
  walkthrough, or a "how to do X using A + B + C" article that spans more than one
  Gcore product or section (for example "set up live streaming with CDN and DDoS
  protection", "deploy Kubernetes with load balancing and object storage", "write a
  use case combining streaming and CDN", "create an end-to-end guide that connects
  these products"). It finds the relevant source articles across the repo,
  determines the correct setup sequence and dependencies, optionally verifies the
  flow end-to-end in the Customer Portal via Playwright, and writes the article
  following the cookbook template and style rules. Do not use it for documenting a
  single product feature (use update-page or write-from-scratch instead).
---
@../../../.agents/skills/cookbook/SKILL.md
