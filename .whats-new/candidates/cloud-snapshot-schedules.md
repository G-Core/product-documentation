---
product: Cloud
status: Include
release_date: 2026-09-22
published_page: null
---

# Cloud snapshot schedules in the SDK

Customer change: Python and Go SDK v0.57.0 and later name the snapshot schedule client cloud.snapshot_schedules. The REST path remains /cloud/v1/lifecycle_policy.
Affected users: Customers who create, list, pause, or delete automatic volume snapshot schedules with the SDK
Release evidence: Python SDK v0.57.0 published 2026-09-22. The same client names are present in v0.59.0. Create, list, pause, resume, and delete were run on production for issue 2939. Not published on the What's new page.
Open verification: none
Source tickets/PRs: https://github.com/G-Core/product-documentation/issues/2939, https://github.com/G-Core/product-documentation/issues/3165
Documentation links: cloud/virtual-instances/snapshots/set-up-automatic-snapshot-creation.mdx
Duplicate check: same event as issue 2939, not yet on a What's new page
Published entry: null
