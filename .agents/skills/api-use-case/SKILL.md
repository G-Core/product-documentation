---
name: api-use-case
description: Add REST API coverage to an existing Customer Portal article with MethodSwitch and repository OpenAPI specs. Use when asked to add API coverage or create a REST API tab for a portal-only article.
---

Read an existing Customer Portal article, find the matching API endpoints in the
OpenAPI spec, and write a complete `<MethodSection id="api">` section.

## Scope — read exactly these files

1. This SKILL.md
2. The existing article specified by the user
3. `/api-reference/services_documented/{product}_api.yaml` — the relevant OpenAPI spec
4. `.agents/references/mdx-rules.md` — MethodSwitch structure rules
5. `.agents/references/style-guide.md` — writing rules for the API section prose
6. `.agents/references/procedures.md` — step format and ordering rules

Do not read other articles unless the existing article cross-links to them and
the link is directly relevant to mapping a Portal step to an API call.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Path to existing Portal article | Yes | The article that will receive the API tab |
| Real API testing | No | Ask the user — see Phase 2 |

---

## Phase 1 — Read the Portal article

Read the full article. Understand:

1. **What resources are created and in what order** — e.g. network → subnet → instance → floating IP
2. **Dependencies between steps** — e.g. subnet needs `network_id` from step 2
3. **The overall flow type:**
   - Steps feed into each other → **sequential** → use Structure A (Quickstart + Step-by-step)
   - Steps are independent operations → **independent** → use Structure B (standalone sections)

**Rule:** "Create" / "Deploy" articles are almost always sequential (Structure A).
"Manage" / "Configure" articles are almost always independent (Structure B).
Test: "Can the user do Step 3 without Steps 1 and 2?" If yes → Structure B.

4. **Identify the product** from the file path — determines which OpenAPI YAML to load.

---

## Phase 2 — API testing (ask the user)

Before writing, ask:

> The API section can be based on the OpenAPI spec alone, or I can also run
> the actual API calls against the live environment to verify real responses,
> catch undocumented errors, and confirm field behavior.
>
> - **Yes, test with real API** — more accurate, takes longer
> - **No, use the spec only** — faster, mark uncertain steps as `{TODO: verify}`

Wait for the answer before proceeding.

**If yes → real testing:**
- API credentials are in `C:\Projects\docops-agent2\access.md`
- Use Luxembourg-3 (`region_id: 148`) for general VM and networking
- Use Frankfurt-2 (`region_id: 180`) for DBaaS and Kubernetes
- Run each API call end-to-end in the terminal using `curl` against `https://api.gcore.com`
- Record real responses — exact fields, structure, error messages
- Only after the full flow runs end-to-end — move to Phase 3
- Do NOT delete test resources until the user approves the final article

**If no → spec only:**
- Mark steps that cannot be verified from the spec as `{TODO: verify in live environment}`
- These will need a follow-up `full-audit` run to verify

---

## Phase 3 — Find the API endpoints

Open the OpenAPI YAML for the product:
```
/api-reference/services_documented/{product}_api.yaml
```

For each Portal step, find the equivalent API operation:

```powershell
# Search for an endpoint by path pattern
Select-String -Path "api-reference\services_documented\cloud_api.yaml" `
              -Pattern "/cloud/v\d+/instances"
```

**Mapping rules:**
- Always use the latest non-deprecated API version (`v2` over `v1` when both exist)
- Verify field names from the YAML spec — never write field names from memory
- Note gotchas discovered: wrong methods, missing required fields, non-obvious validation

**Known gotchas to check before writing** (add new ones as you discover them):
- `GET /cloud/v1/instances/{project_id}/{region_id}/available_flavors` is a POST requiring volume data — use `GET /cloud/v1/flavors/{project_id}/{region_id}` to list flavors
- Instance `name` field is blocked on reseller accounts — standard accounts support it normally; use `name` in article examples
- `addresses` field uses network name as key (e.g. `"pub_net"`), not a fixed string — iterate over all keys

---

## Phase 4 — Write the API section

### Structure A — Sequential creation flow

Use when Portal steps must execute in order and outputs feed into later steps.

**Opening sentence** (required, before `<Info>` block):
One sentence describing what this section enables. Rules:
- Do NOT start with "The steps below..."
- Do NOT explain what the product is (that belongs in an overview article)
- DO describe the user action and outcome

Good: `"Create a subnet inside an existing network and customize its DHCP and DNS settings."`
Good: `"Keep services reachable even when infrastructure changes by assigning a floating IP."`
Bad: `"The steps below create a subnet and configure DNS."` ← starts with "The steps below"

**`<Info>` block** (required):
```mdx
<Info>
An [API token](/account-settings/api-tokens) is required, along with a
[project ID](https://api.gcore.com/docs/cloud#tag/Projects/operation/ProjectsListV1.get)
and a [region ID](https://api.gcore.com/docs/cloud#tag/Regions/operation/RegionListV1.get).
</Info>
```
If the flow requires an existing resource (e.g. a network), add it:
`"...and the ID of an existing [network](/cloud/networking/create-and-manage-a-network)."`

**Environment variables block:**
```mdx
Open a terminal and set these environment variables before running the examples:

```bash
export GCORE_API_KEY="{YOUR_API_KEY}"
export GCORE_CLOUD_PROJECT_ID="{YOUR_PROJECT_ID}"
export GCORE_CLOUD_REGION_ID="{YOUR_REGION_ID}"
```
```

**Quickstart section:**
```mdx
## Quickstart

{One sentence: what the scripts do. Not "Complete scripts for the full flow."}

<Tabs>
  <Tab title="Python SDK">
    ```python
    # Step 1. {action}
    # Step 2. {action}
    ```
  </Tab>
  <Tab title="Go SDK">
    ```go
    // Step 1. {action}
    // Step 2. {action}
    ```
  </Tab>
</Tabs>
```

Quickstart rules:
- Python SDK and Go SDK tabs only — **no curl tab in Quickstart**
- Every logical step: `# Step 1.` — never combine (`# Step 3+4`)
- Script runs as-is after setting three env vars — no other substitutions needed
- **Never hardcode region-specific IDs** — select by characteristics:
  ```python
  # IDs are region-specific; selects 2 vCPU / 4 GB RAM
  flavor = next(f for f in flavors if f.vcpus == 2 and f.ram == 4096)
  ```
- Print useful output at each step (resource name, ID, SSH command)

**Step-by-step section:**
```mdx
## Step-by-step

<p>Each step below explains what the call does, which parameters matter,
and what the response looks like.</p>

<Accordion title="Show all steps">

### Step 1. {Verb + object}

{One sentence: why this step matters in the flow.}

| Parameter | Required | Description |
|-----------|----------|-------------|
| `param` | Yes | What it does and how to get it |

<Tabs>
  <Tab title="Python SDK">```python ... ```</Tab>
  <Tab title="Go SDK">```go ... ```</Tab>
  <Tab title="curl">
    ```bash
    curl -X POST "https://api.gcore.com/..." \
      -H "Authorization: APIKey $GCORE_API_KEY" \
      -d '{...}'
    ```

    Response:
    ```json
    {"tasks": ["abc-123"]}
    ```
  </Tab>
</Tabs>

The API returns:

```json
{"tasks": ["abc-123"]}   // save as TASK_ID
```

</Accordion>
```

**Step anatomy rules:**
1. One prose sentence: why this step matters — not "In this step, you will..."
2. Parameters table: non-obvious required fields only
3. Code tabs: Python SDK → Go SDK → curl (curl always last)
4. Response JSON: always labeled with `The API returns:` — never a bare JSON block after `</Tabs>`
5. Inline API reference link: embed in a meaningful sentence, not standalone

**Polling pattern** — when an endpoint returns `{"tasks": [...]}`:
```mdx
Run <code>GET&nbsp;/cloud/v1/tasks/{task_id}</code> every 5 seconds until
`state` is `FINISHED`, then read the resource ID from `created_resources`.

While provisioning:
```json
{"state": "RUNNING", "created_resources": {}}
```

When complete:
```json
{"state": "FINISHED", "created_resources": {"instances": ["abc-123"]}}
```
```

**Optional standalone sections** (after the accordion, as separate `##` headings):
- `## Add an SSH key`, `## Filter images by OS`, `## Attach to a private network`
- `## Clean up` — always standalone, never inside the accordion

**Forbidden sections:** `## Prerequisites`, `## Next steps`, `## What's next`, `## Requirements`

---

### Structure B — Independent operations

Use when operations are unrelated and can be done in any order (manage/configure articles).

```mdx
{Opening sentence}

<Info>...</Info>

```bash
export GCORE_API_KEY="{YOUR_API_KEY}"
...
```

## {Operation name}

{One sentence.}

<Tabs>
  <Tab title="Python SDK">```python ... ```</Tab>
  <Tab title="Go SDK">```go ... ```</Tab>
  <Tab title="curl">```bash ... ```</Tab>
</Tabs>

The API returns:
```json
{...}
```

## {Another operation name}
```

No Quickstart section for Structure B — operations are unrelated and a single
script would be artificial.

---

## Phase 5 — Wrap in MethodSwitch

If the article currently has no MethodSwitch, wrap the existing portal content:

```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

  {existing portal content — do not change it}

  </MethodSection>
  <MethodSection id="api" label="REST API">

  {new API section written in Phase 4}

  </MethodSection>
</MethodSwitch>
```

If MethodSwitch already exists, add the `<MethodSection id="api">` after the portal section.

**Do not modify the portal section** — it is out of scope for this skill.

---

## Phase 6 — Update frontmatter

Update `ai-navigation` to mention both methods:

```yaml
ai-navigation: Create Linux Virtual Machines in Gcore Cloud via Customer Portal
by configuring image, flavor, and network, or via REST API using the Instances API.
```

Rules: one sentence, starts with action verb, mentions both methods, max 160 chars,
no curly braces, no URL paths, no colons followed by space.

---

## Phase 7 — Review

Run these checks before showing the result:

**Structure:**
```
grep "^## What \|^## How \|^## Why \|^## When "
grep "^## Next steps\|^## Prerequisites\|^## Requirements\|^## See also"
grep "^This guide covers\|^This article\|^In this \|^The steps below"
```
Scan every `##` and `###` — verify a prose sentence follows before any code block or table.

**Formatting:**
- Bold only for UI elements — not for emphasis
- Em-dashes spaced: ` — ` not `—`
- Response JSON never appears directly after `</Tabs>` without a label
- Quickstart scripts have no combined step labels (`# Step 3+4`)
- Flavor and image IDs not hardcoded — selected dynamically

**Links:**
- Link text 1–2 words maximum
- Each URL linked only once — subsequent mentions plain text
- No standalone "For more details, see..." sentences

**Voice:**
- No "you" or "your" in prose
- No forbidden words: just, simply, obviously, ensure, platform

**MDX:**
- Import has `.jsx` extension
- `<MethodSwitch>` wraps both sections
- Closing `</MethodSection>` tags at column 0 after lists
- No `{identifier}` in inline backtick spans

---

## Output

Show the complete updated article. Then:

```
Article: [path]
API structure: [A — sequential / B — independent]
Steps covered: [N]
Real API tested: [yes / no — N steps marked TODO]

TODO items:
- {TODO: verify ...} at Step N — [what to check]
```

When the user confirms the result looks good — load `.agents/skills/pr/SKILL.md`
to create the branch, commit, and open a draft PR.
