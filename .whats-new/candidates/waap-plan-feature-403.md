---
product: WAAP
status: Include
release_date: 2026-11-03
published_page: null
---

# Plan-gated WAAP features return 403

Customer change: An authenticated request for a WAAP feature the plan does not include returns 403 instead of 401. The error body is unchanged.
Affected users: API and Terraform callers whose WAAP plan does not include the feature they request.
Release evidence: QA confirmed the new behavior on preprod on 2026-11-03. The production image-tag deploy for gingerbread v0.78.0 is merged.
Open verification: none
Source tickets/PRs: DOC-3077, WS-2959
Documentation links: waap/manage-waap-via-terraform.mdx
Duplicate check: not found
Published entry: null
