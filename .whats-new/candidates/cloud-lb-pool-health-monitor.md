---
product: Cloud
status: Include
release_date: 2026-10-30
published_page: null
---

# Load balancer pool health monitor in Terraform

Customer change: On Terraform provider v2, a load balancer pool health monitor is the resource gcore_cloud_load_balancer_pool_health_monitor. The pool resource does not accept a healthmonitor attribute.
Affected users: Accounts that manage Gcore load balancers with the v2 provider.
Release evidence: Provider 2.0.0-rc.3, published 2026-10-30. Live apply in Luxembourg-3 created the monitor, an in-place delay change applied, and import with PROJECT_ID/REGION_ID/POOL_ID left an empty plan. A nested healthmonitor attribute on the pool was rejected at plan. The test resources were destroyed.
Open verification: none
Source tickets/PRs: DOC-2884, GCLOUD2-30616, https://github.com/G-Core/terraform-provider-gcore/releases/tag/v2.0.0-rc.3
Documentation links: cloud/networking/create-and-configure-a-load-balancer.mdx
Duplicate check: not found
Published entry: none
