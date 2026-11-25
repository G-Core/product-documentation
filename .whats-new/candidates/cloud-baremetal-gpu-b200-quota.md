---
product: Cloud
status: Include
release_date: 2026-11-23
published_page: null
---

# Bare metal GPU B200 quota

Customer change: Cloud quotas include a B200 GPU bare metal limit and usage, `baremetal_gpu_b200_count_limit` and `baremetal_gpu_b200_count_usage`, in each region.
Affected users: Accounts that check or request Cloud quotas for GPU bare metal servers.
Release evidence: cloud-frontend 8.5.0 is recorded as deployed to cloud-frontend/prod on 2026-11-23. Production GET /cloud/v2/client_quotas returned both fields on 2026-11-25.
Open verification: none
Source tickets/PRs: DOC-3069, GCLOUD2-31835
Documentation links: cloud/getting-started/request-a-quota-increase.mdx
Duplicate check: not found
Published entry: null
