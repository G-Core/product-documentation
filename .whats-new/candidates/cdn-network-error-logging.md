---
product: CDN
status: Include
release_date: unknown
published_page: null
---

# Network Error Logging on CDN resources

Customer change: A CDN resource can add NEL and Report-To response headers so browsers report network errors for that resource. The customer turns this on or off in resource settings. There is no report view in the portal.
Affected users: CDN resource owners. On the resource checked in production the switch was off until it was enabled. Default for a newly created resource was not checked.
Release evidence: Production Customer Portal, 2026-10-29. Resource settings, General, Network Error Logging. Enabling the switch and saving added the NEL and Report-To headers on the next response. Disabling it and saving removed them.
Open verification: none for the switch itself. Default state of a new resource was not checked by creating one.
Source tickets/PRs: DOC-2862
Documentation links: /cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource
Duplicate check: not found
Published entry: none
