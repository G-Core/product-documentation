---
product: CDN
status: Include
release_date: 2026-11-23
published_page: null
---

# Network Error Logging in Terraform

Customer change: gcore_cdn_resource can set network_error_logging. enabled false removes the NEL and Report-To headers. enabled true adds them. value stays true. A new resource leaves logging on when the block is omitted.
Affected users: Accounts that create CDN resources with the Gcore Terraform provider, including resellers that need logging off for some resources.
Release evidence: Provider v0.37.3 was published to the Terraform Registry on 2026-11-23, and the v2 schema gcore-2.0.0-rc.3 used by the docs tab includes options.network_error_logging. CDI-1578 is closed.
Open verification: none
Source tickets/PRs: DOC-3070, CDI-1578
Documentation links: cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource.mdx
Duplicate check: cdn-network-error-logging.md records the portal switch from 2026-10-29, not the Terraform attribute
Published entry: null
