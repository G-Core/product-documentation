---
product: CDN
status: Needs verification
release_date: unknown
published_page: null
---

# Default edge cache TTL on new CDN resources

Customer change: A new CDN resource caches origin responses that have no cache headers for 120 minutes. Responses 302 and 303 use 20 minutes, and responses 404 and 410 use 3 minutes. A resource created earlier keeps its saved cache settings.
Affected users: Accounts that create a new CDN resource and whose origin does not send Cache-Control or Expires.
Release evidence: not verified on the portal. CDM-2414 is closed with merged pull requests on 2026-11-25.
Open verification: Create a new CDN resource and confirm the saved edge cache defaults.
Source tickets/PRs: DOC-3079, CDM-2414
Documentation links: cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin.mdx, cdn/terraform/manage-cdn-via-terraform.mdx
Duplicate check: not found
Published entry: null
