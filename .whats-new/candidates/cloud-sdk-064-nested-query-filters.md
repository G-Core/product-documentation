---
product: Cloud
status: Include
release_date: 2026-11-25
published_page: null
---

# SDK nested query filters use brackets

Customer change: Python and Go SDK 0.64.0 send nested list filters as filter[key]=value. The dotted form is rejected. A bare metal GPU cluster list with name[prefix] and tags[env] is accepted. tags.env returns 400.
Affected users: Customers who filter GPU cluster or IAM user lists from the Python or Go SDK
Release evidence: SDK v0.64.0 published 2026-11-25. On 2026-11-27 a production list of bare metal GPU clusters sent name[prefix]=prod- and tags[env]=production and returned a page. The same list with tags.env=production returned 400. No cluster was created.
Open verification: none
Source tickets/PRs: DOC-3093
Documentation links: edge-ai/ai-infrastructure/manage-a-bare-metal-gpu-cluster.mdx
Duplicate check: cloud-sdk-064-instance-create.md is the instance create change in the same SDK release, not this query encoding
Published entry: null
