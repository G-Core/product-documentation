---
product: Edge Proxy
status: Include
release_date: 2026-11-05
published_page: null
---

# Public Edge Proxy API

Customer change: A customer API token can create an Edge Proxy profile, receive a protected IP, and read that profile back. After processing finished, the profile status was ACTIVE without a separate activate call. Delete is rejected while processing is in progress and succeeds after it finishes.
Affected users: Edge Proxy customers using the public API at api.gcore.com.
Release evidence: On 2026-11-05 a customer API token called the production API. List templates and list profiles returned 200. Create returned 201 with a protected IP, status INACTIVE, and is_processing true. A later read showed status ACTIVE and is_processing false. Delete then returned 204, and the following read returned 404. The test profile was removed.
Open verification: none
Source tickets/PRs: DOC-2898, DP-4585
Documentation links: /edge-proxy/how-protection-works, /edge-proxy/quick-start, /api-reference/edge-proxy/proxy-profiles/list-proxy-profiles
Duplicate check: not found
Published entry: none
