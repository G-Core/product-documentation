---
product: Cloud
status: Include
release_date: 2026-11-23
published_page: null
---

# Bare metal GPU B200 quota

Customer change: GPU Cloud lists a B200 bare metal flavor, 8x NVIDIA B200 180GB, in Helsinki. Cloud quotas include a B200 GPU bare metal limit and usage, `baremetal_gpu_b200_count_limit` and `baremetal_gpu_b200_count_usage`, in each region.
Affected users: Accounts that create a Bare Metal GPU cluster or check Cloud quotas for GPU bare metal servers.
Release evidence: On 2026-11-27 the production GPU bare metal flavor list in Helsinki included `bm4-ai-1xlarge-b200-180-8` with 2TB RAM, 2x 960GB SSD and 4x 3.8TB NVMe, 3.2 Tbit/s InfiniBand, and 2x 100 Gbit/s Ethernet. cloud-frontend 8.5.0 is recorded as deployed to cloud-frontend/prod on 2026-11-23. Production GET /cloud/v2/client_quotas returned both quota fields on 2026-11-25.
Open verification: none
Source tickets/PRs: DOC-3049, DOC-3069, GCLOUD2-31759, GCLOUD2-31835
Documentation links: edge-ai/ai-infrastructure/about-gpu-cloud.mdx, edge-ai/ai-infrastructure/create-a-bare-metal-gpu-cluster.mdx, cloud/getting-started/request-a-quota-increase.mdx
Duplicate check: not found
Published entry: null
