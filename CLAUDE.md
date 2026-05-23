# Gcore Product Documentation — CLAUDE.md

## What this repo is

This is the Gcore product documentation repository. It contains:
- UI-based how-to articles for the Gcore Customer Portal (organized by product → resource)
- API reference specs in `api-reference/services_documented/`
- Use-case articles in `cloud/use-cases/`

## Current task: Generate "Via API" developer guides for Gcore Cloud

We are converting UI-based articles into developer-oriented API guides. These go in `cloud/via-api/` (create if it doesn't exist).

**Goal:** A developer reading a "Via API" article should be able to reproduce the full workflow using only the Gcore REST API — no portal required.

---

## API test credentials

The test API token for real validation is in `C:\Projects\docops-agent2\access.md`.
- project_id: `1186668` (Default project)
- Use Frankfurt-2 (`region_id: 180`) for general VM testing — active, has standard volumes, k8s, dbaas.

---

## Flow catalog (11 articles planned)

| # | Slug | Short description | Endpoints touched |
|---|------|-------------------|-------------------|
| 1 | `deploy-vm-from-scratch` | SSH key → image/flavor → instance → public IP → SSH | ssh_keys, images, flavors, instances |
| 2 | `deploy-vm-with-block-storage` | Create VM → create volume → attach → mount | instances, volumes |
| 3 | `deploy-bare-metal-server` | BM flavor → create server → assign IP → SSH | bare-metal-servers |
| 4 | `set-up-private-network` | Network → subnet → router → 2 VMs → verify | networks, subnets, routers, instances |
| 5 | `deploy-load-balanced-app` | VMs → load balancer → listener + pool + members → floating IP | instances, load-balancers, floatingips |
| 6 | `configure-firewall` | Create security group → add rules → attach to VM | security-groups, instances |
| 7 | `deploy-kubernetes-cluster` | Create cluster → kubeconfig → deploy app | kubernetes/clusters |
| 8 | `add-persistent-storage-to-k8s` | PVC → stateful deployment | kubernetes/storage |
| 9 | `deploy-container-via-caas` | Push image → create container → expose endpoint | caas, container-registry |
| 10 | `create-postgresql-instance` | Create instance → connection string → create DB | managed-database-postgresql |
| 11 | `mount-file-share-to-vm` | Create file share → create VM → mount NFS | file-shares, instances |

---

## Algorithm: how to generate a Via API article

**Every article goes through 4 phases: research → real testing → draft → review.**
You cannot skip testing. You cannot skip review. Articles based on theory will mislead customers.

---

### Phase 1 — Research

Read the relevant UI article(s) in this repo to understand:
- What resources are created and in what order
- What dependencies exist between steps (e.g., subnet needs network_id)

Relevant UI articles are usually at:
- `cloud/virtual-instances/*.mdx`
- `cloud/networking/*.mdx`
- `cloud/kubernetes/clusters/*.mdx`

---

### Phase 2 — Real API testing (mandatory before writing)

Execute the full flow end-to-end in the terminal using `curl` against `https://api.gcore.com`.

For each API call:
1. Run it. Record the real response — exact fields, structure, timing.
2. Catch every error: wrong methods, missing fields, validation rules, account constraints.
3. Note everything a user would need to know that isn't obvious from the spec.

**Only after the full flow runs end-to-end** move to drafting.

#### Finding endpoints

Grep the YAML spec for the right path and method:

```powershell
Select-String -Path "api-reference\services_documented\cloud_api.yaml" -Pattern "/cloud/v\d+/instances"
```

Always use the latest non-deprecated API version (`v2` over `v1` when both exist).

#### Key endpoints for Cloud flows

| Operation | Endpoint |
|-----------|----------|
| List SSH keys | `GET /cloud/v1/ssh_keys/{project_id}` |
| Add SSH key | `POST /cloud/v1/ssh_keys/{project_id}` |
| List images | `GET /cloud/v1/images/{project_id}/{region_id}?visibility=public` |
| **List flavors** | `GET /cloud/v1/flavors/{project_id}/{region_id}` |
| Create instance | `POST /cloud/v2/instances/{project_id}/{region_id}` |
| Create network | `POST /cloud/v1/networks/{project_id}/{region_id}` |
| Create subnet | `POST /cloud/v1/subnets/{project_id}/{region_id}` |
| Create floating IP | `POST /cloud/v1/floatingips/{project_id}/{region_id}` |
| Assign floating IP | `PATCH /cloud/v2/floatingips/{project_id}/{region_id}/{floating_ip_id}` |
| Poll task | `GET /cloud/v1/tasks/{task_id}` |

#### Known gotchas (update this list as you discover more)

- `GET /cloud/v1/instances/{project_id}/{region_id}/available_flavors` is a **POST** requiring volume data. To list flavors, use `GET /cloud/v1/flavors/{project_id}/{region_id}`.
- Instance `name` field is blocked on reseller accounts; they require `name_templates` with region-specific patterns (e.g., `"frn-c2-{ip_octets}"`). Standard Gcore accounts support `name` normally.
- `addresses` field uses the **network name** as the key (e.g., `"pub_net"`), not a fixed string like `"external"`. Iterate over all keys.
- The default security group is applied automatically and allows SSH (port 22) and ICMP inbound.
- Default SSH user for Ubuntu: `ubuntu`. Debian: `debian`. CentOS: `centos`. Rocky: `rocky`. Fedora: `fedora`.
- Task completion for VM creation: 15–30 seconds.
- **Bare Metal servers require a quota request** before the first server can be created. Default quota is 0. Check with `POST /cloud/v1/bminstances/{project_id}/{region_id}/check_limits`. BM quota with `limit > 0` exists in region 148 (Luxembourg-3) on the test account.
- **BM images are separate from VM images**: BM-compatible images have an `-ironic` suffix (e.g., `ubuntu-24.04-x64-ironic`) and `is_baremetal: true`. They are NOT returned by `GET /cloud/v1/images` — they cannot be listed via API. Find them in the Customer Portal under Bare Metal → create form → Distributions, or use a known image ID directly.
- **BM creation time: 4–5 minutes** (not 30 seconds like VMs).
- BM servers have **no security groups** — `security_groups: []`. All ports are open by default.
- BM uses **local storage only** — `volumes: []`. No block volumes can be attached.
- BM network interface is **bond0** (LACP-bonded), not eth0. Sub-interfaces appear as `bond0.<vlan_id>`.
- BM `available_flavors` (`POST /cloud/v1/bminstances/{project_id}/{region_id}/available_flavors`) validates image+flavor compatibility — use it to confirm an image works before creating.

---

### When information is missing or uncertain

Never guess. Never write a step based on "this is probably how it works". If something is unclear, find the answer using the hierarchy below — in order.

#### 1. Real API call (highest priority)

If the YAML spec and the real API response disagree, the real response wins. Document the discrepancy in the Known gotchas list above.

If a behavior is unclear from the spec (e.g., what does `addresses` look like for a private interface?), run a real call and observe the result.

#### 2. Existing UI articles in this repo

Before writing any explanation of a concept, search the repo first:

```powershell
# Find articles about a concept
Get-ChildItem "cloud" -Recurse -Filter "*.mdx" | Select-String "floating IP" | Select-Object Path
```

If an article already explains the concept (e.g., what a floating IP is, how security groups work), cross-link to it — do not duplicate the explanation. Link text: 1–2 words.

Key articles to reference when needed:

| Topic | Location |
|-------|----------|
| Floating IPs | `cloud/networking/ip-address/create-and-configure-a-floating-ip-address.mdx` |
| Security groups | `cloud/networking/add-and-configure-a-firewall.mdx` |
| Networks / subnets | `cloud/networking/create-and-manage-a-network.mdx` |
| SSH connection | `cloud/virtual-instances/connect/connect-via-ssh.mdx` |
| Volumes | `cloud/virtual-instances/volumes/create-and-configure-volumes.mdx` |
| Kubernetes connect | `cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster.mdx` |

#### 3. Query the API to discover real constraints

When the spec says a field accepts a value but you're unsure what values exist (e.g., volume types, available regions for a feature, image architectures), list them:

```bash
# What volume types exist in this region?
curl "https://api.gcore.com/cloud/v1/regions" -H "Authorization: APIKey $KEY" \
  | grep -o '"available_volume_types":\[[^]]*\]'

# Does this region support k8s?
# Check "has_k8s": true in the /regions response

# What images are available?
curl "https://api.gcore.com/cloud/v1/images/$PROJECT_ID/$REGION_ID?visibility=public" ...
```

Use real query results in the article, not invented values.

#### 4. Third-party tools, OS-level steps, and web search

Some flows require non-API steps: mounting a volume, installing kubectl, connecting to PostgreSQL, configuring kubeconfig. These involve third-party tools with their own documentation.

**Step-by-step:**

1. **Check the repo first** — an existing UI article may already have the correct commands. Use them verbatim and cross-link rather than duplicating.

2. **Search official documentation on the web.** Claude Code has internet access via `WebSearch` and `WebFetch` — use them.

   When to search:
   - The step involves a third-party tool: kubectl, psql, nfs-common, helm, docker, certbot, etc.
   - A command syntax or flag needs to be version-specific.
   - A link to an official external doc is needed in the article.

   How to search:
   ```
   WebSearch: "kubernetes kubectl install official docs"
   WebSearch: "postgresql 16 connection string psql cli"
   WebSearch: "ubuntu 22.04 mount nfs share fstab"
   ```

   Always prefer:
   - `kubernetes.io/docs` over any blog post
   - `docs.docker.com` over tutorials
   - `postgresql.org/docs` over Stack Overflow
   - The official project's own documentation domain

3. **Fetch the exact page** when a specific version or command is needed:
   ```
   WebFetch: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
   ```
   Extract only what is needed for the step. Do not copy entire pages.

4. **Test the commands** against a real instance (created via the API in Phase 2). Confirm the output before writing it into the article.

**Link rules for external third-party docs:**
- Link to the official source once, with 1–2 word link text: `[kubectl docs](https://kubernetes.io/docs/reference/kubectl/)` not `[official Kubernetes kubectl documentation](...)`.
- If the tool has a version that matters (PostgreSQL 16, Kubernetes 1.30), link to the version-specific page.
- Do not link to community tutorials, blog posts, or unofficial guides — only to the tool's own documentation.

**Do not write OS/tool commands from memory without verification.**

#### 5. When the answer cannot be found

If after all the above a step cannot be verified (e.g., a region is unavailable, a feature is not enabled on the test account), do not publish speculation. Instead:

- Write the step based on the YAML spec
- Add a `<Warning>` block: "This step has not been verified against a live environment. If the response differs from the example shown, update the Known gotchas section in CLAUDE.md."
- Add a TODO comment at the top of the file: `{/* TODO: verify step N in region X */}`

---

### Phase 3 — Draft

#### Article structure (DO/Cloudflare/Hetzner standard)

Every Via API article follows this structure exactly:

```
1. Opening paragraph  — what is built + API call count, no meta-preamble
2. Prerequisites callout — API token + IDs as an <Info> block (not a ## heading)
3. env vars block — export commands for reuse
4. Step 1. [Verb + object]
   - One sentence: why this step is needed
   - Key parameters table (only the important ones, not all 47)
   - curl + Python SDK in <Tabs>
   - Response excerpt with inline `// → use as NEXT_VAR` comments
   - "The full parameter list is in the [API reference](link)." embedded in prose
5. Step N. ...
6. Step N+1. Verify the result  — GET or SSH to confirm success
```

**There is no `## Prerequisites` heading, no `## What's next` heading, no `## Next steps` heading.** These are forbidden by style rules. Prerequisites go in a leading `<Info>` block. Cross-links are embedded inline.

#### Step anatomy (competitor standard)

Each step has exactly these parts, in order:

1. **One prose sentence:** why this step matters in the flow. No "In this step, you will..."
2. **Key parameters table** (when the endpoint has non-obvious required fields):

   | Parameter | Required | Description |
   |-----------|----------|-------------|
   | `ssh_key_name` | Yes | Must match the `name` from the SSH key creation step, not the UUID |
   | `boot_index` | Yes | Set to `0` for the primary boot volume |

3. **Code block** with curl + Python SDK in `<Tabs>`
4. **Response excerpt** showing only the fields needed:

   ```json
   {
     "tasks": ["b63f0fff-..."]  // → save as TASK_ID
   }
   ```

5. **Inline API reference link:** natural sentence ending with a link, e.g., "The full parameter list is in the [API reference](https://api.gcore.com/docs/cloud#tag/Instances/operation/InstanceCreateSetV2.post)."

#### Polling pattern

When an endpoint returns `{"tasks": [...]}`, immediately follow with:
- A note that polling is needed
- An explicit instruction: "Run the GET request every 5 seconds until `state` is `FINISHED`."
- A response snippet showing both `RUNNING` and `FINISHED` states
- Where to find the created resource ID in `created_resources`

---

### Phase 4 — Review (mandatory)

After drafting, run the sequential review process from:
`C:\Projects\docops-agent2\.continue\guides\review-process.md`

The review orchestrator runs 5 sequential steps with grep checks. Run all 5 before declaring an article done.

#### Critical rules summary (violations that fail the review)

**Structure:**
- Heading case: sentence case only ("Add an SSH key", not "Add an SSH Key")
- Heading length: 5–8 words max
- No headings starting with What, How, Why, When
- No sections named: Prerequisites, Next steps, What's next, Requirements, Related documentation, See also
- Every heading must be followed by a prose sentence before any code block or table
- No meta-preamble openers: "This guide covers...", "This article explains...", "In this tutorial..."

**Formatting:**
- Bold only for: UI button names, UI field names, UI section names. Never for emphasis or concepts.
- Em-dash always spaced: ` — ` not `—`
- Response excerpts: inline `// comment` on the relevant line, not prose after the block

**Links:**
- Link text: 1–2 words maximum
- Link each URL once per article. Subsequent mentions are plain text.
- No standalone "See [X]" or "Learn more in [X]" sentences. Embed links into content sentences.
- First mention of the Customer Portal: `[Gcore Customer Portal](https://portal.gcore.com)`. All later: "the Customer Portal" (plain text, no link).

**Voice:**
- No "you" or "your" in prose — use imperative (no subject) or neutral third person
- Forbidden words: just, simply, obviously, clearly, ensure, be sure, make sure, etc., platform
- Consistent tutorial voice throughout: direct, action-oriented

**Content quality — anti-patterns caught in review (do not repeat):**

- **No stub sections.** A section heading followed by one thin sentence is a stub. If a section cannot be explained in at least 2–3 meaningful sentences, either expand it or fold it into a neighbouring section.
- **No "read when needed" or similar meta-labels.** Never tell the reader how or when to read. Present content directly and let them decide. Labels like "Reference guides (read when needed):" are condescending.
- **No "X vs Y" headings between our own products.** "API vs other tools" implies competition between Gcore's own tools. If a comparison is genuinely useful, frame it as "Related tools" or remove it entirely.
- **No sentences that exist only to host a link.** "The full parameter list is in the [API reference].", "Full task management endpoints are in the [API reference].", "Full error format is covered in [Error handling]." — all forbidden. These sentences carry no information beyond the link itself. If a cross-reference is genuinely needed, embed the link in a sentence that already has content: "Token sharing and role-based management are available in the [Customer Portal](...)." If no such sentence exists naturally, remove the link entirely — the reader can navigate from the sidebar.
- **Section intros must explain WHY, not just WHAT.** "One API token works across all products. Each product has its own base URL:" tells the reader nothing useful. "Each Gcore product has a dedicated base URL. The same permanent API token authenticates to all of them — no separate credentials per product:" explains the benefit and the constraint.
- **Numbered lists must be truly sequential.** Using `—` as a step number in a table looks like a rendering bug. If steps 6–8 are less critical than 1–5, make that clear through description, not through broken numbering.
- **Every table needs a real intro sentence.** Not "Each product has its own base URL:" (obvious from the table itself), but a sentence that provides context a reader cannot get by just scanning the table.

---

## Article template

```mdx
---
title: "{Verb} {object} via API"
sidebarTitle: "{Short verb phrase}"
---

{Opening sentence: what is built and in how many API calls. No "This guide...".}

<Info>
**Before starting:** A permanent [API token](/account-settings/api-tokens) is required, along with a project ID and region ID. Retrieve them from the Customer Portal or by calling `GET /cloud/v1/projects` and `GET /cloud/v1/regions`.
</Info>

Set these as environment variables for use throughout the guide:

```bash
export GCORE_API_KEY="{YOUR_API_KEY}"
export PROJECT_ID="{YOUR_PROJECT_ID}"
export REGION_ID="{YOUR_REGION_ID}"
```

## Step 1. {Verb + object}

{One sentence: why this step is needed in the flow.}

| Parameter | Required | Description |
|-----------|----------|-------------|
| `param` | Yes | What it does and how to get it |

<Tabs>
  <Tab title="curl">
    ```bash
    curl -X POST "https://api.gcore.com/path/$VAR" \
      -H "Authorization: APIKey $GCORE_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{...}'
    ```
  </Tab>
  <Tab title="Python SDK">
    ```python
    import os
    from gcore import Gcore
    client = Gcore(api_key=os.environ["GCORE_API_KEY"])
    result = client.cloud.resource.method(...)
    ```
  </Tab>
</Tabs>

```json
{
  "id": "abc-123",   // → save as RESOURCE_ID
  ...
}
```

The full parameter list is in the [API reference](https://api.gcore.com/docs/cloud#tag/...).

## Step N. Verify the result

{Confirmation sentence.}

```bash
ssh -i ~/.ssh/key user@{IP_ADDRESS}
```
```

---

## Code style

- curl is Tab 1, Python SDK is Tab 2 in every `<Tabs>` block
- Placeholders: `{YOUR_API_KEY}`, `{PROJECT_ID}`, `{REGION_ID}`, `{INSTANCE_ID}`, etc.
- After the initial `export` block, use `$VAR` form in curl
- Response excerpts: show only what the reader needs, truncate the rest with `...`
- Inline comment format for extracted values: `"id": "abc"   // → save as INSTANCE_ID`
- Python SDK: always `import os` + `api_key=os.environ["GCORE_API_KEY"]`, never hardcode keys

---

## File naming and location

- Directory: `cloud/via-api/`
- Filename: `{slug}.mdx` (verb-noun-noun, e.g., `deploy-vm-from-scratch.mdx`)
- After creating an article, add a navigation entry to `docs.json` (or note it for manual addition)

---

## Quality checklist

**Phase 2 — Real testing:**
- [ ] Full flow executed end-to-end against `api.gcore.com`
- [ ] Every error encountered is documented (either in article or in Known gotchas above)
- [ ] Every response example comes from a real API call

**Phase 3 — Draft:**
- [ ] Opening sentence states what is built, no meta-preamble
- [ ] Prerequisites in `<Info>` block, no `## Prerequisites` heading
- [ ] Each step has: why sentence → key params table → code → response with inline comments → API ref link
- [ ] Polling steps include explicit "every 5 seconds until FINISHED" instruction
- [ ] No `## What's next` or `## Next steps` — cross-links embedded inline

**Phase 4 — Review (run review-process.md):**
- [ ] Step 1 (Structure): headings sentence-case, no forbidden sections, prose before every code block
- [ ] Step 2 (Formatting): bold only for UI elements, em-dashes spaced, response comments inline
- [ ] Step 3 (Links): link text ≤2 words, each URL linked once, no standalone "See X" sentences
- [ ] Step 4 (Voice): no "you/your", no forbidden words, consistent tutorial voice
- [ ] Step 5 (Final read): reads naturally from start to finish
