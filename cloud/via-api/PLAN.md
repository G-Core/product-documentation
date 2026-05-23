# Via API Articles — Work Plan

Branch: `cloud-api-guides`  
Last updated: 2026-05-23  
Status: **Paused — waiting for quota approval (Luxembourg-3, ~2 business days)**

---

## Articles completed (4/11)

| # | File | Status | Notes |
|---|------|--------|-------|
| 1 | `deploy-vm-from-scratch.mdx` | ✅ Done | Fully tested in Frankfurt-2 (region 180) |
| 2 | `deploy-vm-with-block-storage.mdx` | ✅ Done | Fully tested: create + attach + mount + cleanup |
| 3 | `deploy-bare-metal-server.mdx` | ✅ Done | BM server existed in Luxembourg-3; BM images have `-ironic` suffix, not in standard images list |
| 4 | `set-up-private-network.mdx` | ✅ Done | Network/subnet/router tested in Luxembourg (region 6); VM part not tested due to no VM capacity there |

---

## Articles remaining (7/11)

| # | Slug | Flow | Region to use | Notes |
|---|------|------|---------------|-------|
| 5 | `deploy-load-balanced-app.mdx` | VMs → LB → listener → pool → members → floating IP | Luxembourg-3 | Needs: Networks×1, LB×1, VMs×2, Floating IP×1 |
| 6 | `configure-firewall.mdx` | Create security group → add rules → attach to VM | Luxembourg-3 | Needs: Firewall×1, VM×1 |
| 7 | `deploy-kubernetes-cluster.mdx` | Create cluster → kubeconfig → deploy sample app | Luxembourg-3 | Needs: K8s cluster×1; test kubectl locally |
| 8 | `add-persistent-storage-to-k8s.mdx` | PVC → stateful deployment | Luxembourg-3 | Depends on article 7 cluster |
| 9 | `deploy-container-via-caas.mdx` | Push image → create container → expose endpoint | Luxembourg-3 | Needs container-registry + CaaS |
| 10 | `create-postgresql-instance.mdx` | Create instance → connection string → create DB | Luxembourg-3 (has_dbaas check needed) | Needs: managed PostgreSQL |
| 11 | `mount-file-share-to-vm.mdx` | Create file share → VM → mount NFS | Luxembourg-3 (has_sfs=true) | Needs: file-share×1, VM×1 |

---

## Articles needing revisit after quota approval

### Article 4 — set-up-private-network
**Problem:** VM creation was not tested end-to-end because Luxembourg (region 6, where networks work) had no VM capacity, and Frankfurt-2 (region 180, where VMs work) had network_count quota = 0.

**What was verified:** Network creation, subnet creation, router auto-creation, all responses real.  
**What was NOT verified:** VM creation with private subnet interface, ping between two VMs.  
**Action needed:** Re-test Steps 3–5 in Luxembourg-3 once quota arrives. Confirm private IP assignment structure in `addresses` field.

### Article 3 — deploy-bare-metal-server
**Problem:** BM images (`is_baremetal: true`, `-ironic` suffix) are NOT returned by `GET /cloud/v1/images` list endpoint. Discovery method unclear from API alone.  
**Action needed:** Verify if there is a proper API-based way to list BM images. If not, update article to direct users to the Customer Portal for image discovery and document this explicitly as a known API limitation.

---

## Known account constraints (test account ID 1000503)

| Region | ID | VM quota | Network quota | Notes |
|--------|----|----------|---------------|-------|
| Frankfurt-2 | 180 | ✅ Works | ❌ network_count=0 | Good for VM-only tests |
| Luxembourg | 6 | ❌ All flavors at capacity | ✅ 1 network (was 0 routers after cleanup) | Network tests only |
| Luxembourg-2 | 76 | ❌ Cleared | ❌ | Empty after cleanup |
| Luxembourg-3 | 148 | ❓ Pending quota | ✅ 4 networks, 4 routers, 4 LB, 4 k8s | **Use this for all remaining articles** |

**Quota request submitted:** 2026-05-23  
Luxembourg-3 new quotas incoming: 4× Networks, 4× Routers, 4× Floating IPs, 4× LBs, 4× Firewalls, 4× K8s clusters, 4× External IPs, 2× Secrets

---

## How to resume

1. Wait for quota approval email (~2 business days from 2026-05-23)
2. Verify quotas in Luxembourg-3: `POST /cloud/v1/instances/1186668/148/check_limits`
3. Also check LB quota: `GET /cloud/v1/quotas` for region 148
4. Use image `ubuntu-22.04-x64` from region 148 (ID `a3734f07-8347-47e7-ae7a-29b224dc2abb`)
5. SSH key `docops-bm-key` (id `0c205b35-...`) or `docops-test-key` (id `94e8584f-...`) available
6. Work through articles 5–11 in order
7. After completing all 11, re-test article 4 with 2 VMs in Luxembourg-3

---

## API test credentials

See `C:\Projects\docops-agent2\access.md`  
project_id: `1186668`  
Preferred region for new articles: Luxembourg-3, region_id `148`

---

# Developer Tools: REST API section — Proposal

## Background

There are two types of developers who come to the API docs:

**Type A — "I know APIs, show me the endpoints"**  
They go straight to `api-reference/` (OpenAPI/Swagger). Already served well.

**Type B — "I want to automate Gcore, where do I start?"**  
They don't know about project_id/region_id, task polling, or how tokens work with SSO. No single place guides them. Currently they fall through the gap between Account Settings (tokens) and the API reference (endpoint listing).

The `cloud/via-api/` guides we're building serve a third type:  
**Type C — "I need to do X, walk me through the API calls for that specific task."**

Type B is currently unserved. That's the gap to fill.

---

## Where this content should live

`developer-tools/` already has `terraform/` and `mcp-server/` — both are "tools for developers." A new **`rest-api/`** subgroup fits the same pattern. It sits alongside Terraform, not under it.

```
developer-tools/
├── mcp-server/          (exists)
├── terraform/           (exists)
└── rest-api/            (NEW — proposed below)
```

This is distinct from `api-reference/` (pure endpoint reference) and `cloud/via-api/` (product workflow guides). The three together form a complete developer journey:

| Section | Question answered |
|---------|-------------------|
| `developer-tools/rest-api/` | How does the Gcore API work? Where do I start? |
| `cloud/via-api/` | How do I deploy/configure X? |
| `api-reference/` | What are all the parameters for endpoint Y? |

---

## Proposed articles for `developer-tools/rest-api/`

### 1. Overview (`overview.mdx`)
**What:** Single entry point. What the Gcore API is, when to use it vs Terraform vs MCP, base URLs per product, the single-header auth model.  
**Note:** `api-reference/overview.mdx` covers some of this — consider merging or cross-linking.

### 2. Authentication (`authentication.mdx`)
**What:** Everything a developer needs to authenticate, derived from real gaps found during testing.

Must cover:
- Permanent tokens vs session tokens (1-hour JWT): when to use each
- How to create a permanent token in the portal (link to `account-settings/api-tokens`)
- Token roles: what `Administrators` vs `Users` can do with a token
- The `$` character in API keys — must be escaped in shell (`\$` or quoted), or set as env var
- The authorization header format: `Authorization: APIKey {token}` — case-insensitive
- SSO accounts: tokens stay active even after SSO access is revoked — must delete manually
- Token expiry and rotation: 50-token limit per account, expiry notifications

### 3. Make your first API call (`first-api-call.mdx`)
**What:** Step-by-step guide for a developer starting from zero.

Flow:
1. Create a permanent token (link to portal)
2. Set it as an environment variable (never hardcode)
3. Make the first call: `GET /iam/clients/me` — verify account details
4. Find your project_id: `GET /cloud/v1/projects`
5. Find your region_id: `GET /cloud/v1/regions` — explain Core vs Edge, `has_kvm`, `has_k8s`, etc.
6. Make a resource call: list instances

### 4. Asynchronous operations (`async-operations.mdx`)
**What:** The task/polling pattern — the single most confusing thing for new Gcore API users.

Must cover:
- Why most write operations return `{"tasks": ["uuid"]}` instead of the created resource
- Task states: `NEW` → `RUNNING` → `FINISHED` or `ERROR`
- How to poll: `GET /cloud/v1/tasks/{task_id}`, recommended interval (5s for VMs, 30s for BM)
- How to extract the created resource ID from `created_resources`
- Error handling: what to do when state is `ERROR`
- Typical task durations: VM ~20s, BM ~5min, k8s cluster ~10min
- Python polling pattern (reusable snippet)

### 5. Pagination (`pagination.mdx`)
**What:** Every list endpoint in the Cloud API uses `limit` and `offset`. New developers commonly miss items when results exceed the default page size.

Must cover:
- Default limits (typically 1000 for Cloud)
- The `count` field — total number of results
- How to iterate all pages with offset
- When pagination matters (large projects with many resources)
- Code example: fetch all instances across pages

### 6. Error handling (`error-handling.mdx`)
**What:** The standard Gcore API error response format, common errors, and how to handle them.

Must cover:
- Error response structure: `exception_class`, `message`, `request_id`, optional `info`
- Common errors encountered in real testing:
  - `QuotaLimitExceed` — includes `current_usage`, `requested_usage`, `limit`
  - `ValidationError` — field-level errors, name template constraints
  - `NotFoundError` — resource not found or wrong region/project
  - `ForbiddenError` — flavor at regional capacity
  - `HTTP 405 Method Not Allowed` — wrong HTTP method (e.g., GET instead of POST)
- What `request_id` is for: include it when contacting support
- Retry strategy: which errors are safe to retry, which require fixing the request

### 7. SDK quick starts (`sdks.mdx`)
**What:** Get running with the Python or Go SDK in under 5 minutes.

Must cover:
- Python: `pip install gcore`, initialize client, first call
- Go: `go get github.com/G-Core/gcore-go`, first call
- How SDK methods map to API endpoints
- SDK vs raw curl: when to use which

---

## What NOT to include in `developer-tools/rest-api/`

- **Product-specific workflow guides** — those go in `cloud/via-api/` (and future `cdn/via-api/`, etc.)
- **Full endpoint reference** — that's `api-reference/`
- **Terraform** — separate tool, already has its own section
- **MCP server** — separate tool, already has its own section

---

## What already exists and can be cross-linked (not duplicated)

| Existing page | What it covers | Cross-link from |
|---------------|----------------|-----------------|
| `account-settings/api-tokens` | Create/delete/manage tokens | `authentication.mdx` |
| `api-reference/overview.mdx` | Base URLs, auth header, SDKs table | `overview.mdx` or merge |
| `developer-tools/terraform/overview.mdx` | When to use Terraform vs API | `overview.mdx` |

---

## Priority order

1. `authentication.mdx` — blocks everything else; people can't even start without a token
2. `async-operations.mdx` — single biggest source of confusion, applies to all Cloud APIs
3. `first-api-call.mdx` — onboarding for Type B developers
4. `error-handling.mdx` — needed when things go wrong (which happens a lot in testing)
5. `pagination.mdx` — needed for production use with real data volumes
6. `sdks.mdx` — nice to have, SDK READMEs already cover basics
7. `overview.mdx` — can be a thin page linking to the above
