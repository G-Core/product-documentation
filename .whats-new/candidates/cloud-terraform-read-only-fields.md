---
product: Cloud
status: Needs verification
release_date: unknown
published_page: null
---

# Read-only fields removed from Cloud Terraform resources

Customer change: Terraform provider v2 removes these attributes from the resources and their data sources: `has_router` from gcore_cloud_network_subnet, `network` from gcore_cloud_reserved_fixed_ip (`network_id` stays), `floating_ips` from gcore_cloud_load_balancer, `pool_count` from gcore_cloud_load_balancer_listener, and `interfaces[].type` from gcore_cloud_network_router. References to a removed attribute fail with "Unsupported attribute". State drops the attributes on refresh, and no resource is replaced.
Affected users: Accounts that use the v2 provider and read these attributes, or set `type` in router `interfaces`.
Release evidence: not verified. Merged to the staging provider on 2026-11-16 (G-Core/stlc-config#262). It is not in a published provider release yet; 2.0.0-rc.3 still has these attributes.
Open verification: The first published provider release that contains the change, and its date.
Source tickets/PRs: GCLOUD2-31403, https://github.com/G-Core/stlc-config/pull/262, https://github.com/G-Core/product-documentation/pull/3349
Documentation links: cloud/networking/create-and-manage-a-router.mdx
Duplicate check: not found
Published entry: none
