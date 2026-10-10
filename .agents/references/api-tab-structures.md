# REST API tab structures

Templates and rules for writing the content of `<MethodSection id="api">`. Used by the `api-use-case` skill. The `api-audit` skill uses it to check an existing tab.

## Contents

- Choosing the structure
- Structure A — sequential creation flow
- Structure B — independent operations
- Polling pattern
- Optional and forbidden sections

---

## Choosing the structure

Read the Portal article and identify the flow type:

- Steps feed into each other (outputs become inputs) → **sequential** → Structure A (Quickstart + Step-by-step)
- Steps are independent operations → **independent** → Structure B (standalone sections)

"Create" / "Deploy" articles are almost always sequential. "Manage" / "Configure" articles are almost always independent.
Test: "Can the user do Step 3 without Steps 1 and 2?" If yes → Structure B.

---

## Structure A — sequential creation flow

Use when Portal steps must execute in order and outputs feed into later steps.

**Opening sentence** (required, before the `<Info>` block):
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
[project ID](/api-reference/cloud/projects/list-projects)
and a [region ID](/api-reference/cloud/regions/list-regions).
</Info>
```
If the flow requires an existing resource (e.g. a network), add it:
`"...and the ID of an existing [network](/cloud/networking/create-and-manage-a-network)."`

**Environment variables block:**
````mdx
Open a terminal and export the required variables:

```bash
export GCORE_API_KEY="{YOUR_API_KEY}"
export GCORE_CLOUD_PROJECT_ID="{YOUR_PROJECT_ID}"
export GCORE_CLOUD_REGION_ID="{YOUR_REGION_ID}"
```
````

**Quickstart section:**
````mdx
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
````

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
````mdx
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

    <p>The API returns:</p>

    ```json
    {"tasks": ["abc-123"]}
    ```
  </Tab>
</Tabs>

</Accordion>
````

**Step anatomy rules:**
1. One prose sentence: why this step matters — not "In this step, you will..."
2. Parameters table: non-obvious required fields only
3. Code tabs: Python SDK → Go SDK → curl (curl always last)
4. HTTP response body belongs **inside the tab that produced it**. For curl, that is the curl tab, immediately after the command, labeled `<p>The API returns:</p>` then a `json` fence. Never put response JSON (or "The API returns") after `</Tabs>` — that block is visible in every method tab.
5. Inline API reference link: embed in a meaningful sentence, not standalone

---

## Structure B — independent operations

Use when operations are unrelated and can be done in any order (manage/configure articles).

````mdx
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
  <Tab title="curl">
    ```bash
    curl ...
    ```

    <p>The API returns:</p>

    ```json
    {...}
    ```
  </Tab>
</Tabs>

## {Another operation name}
````

No Quickstart section for Structure B — operations are unrelated and a single script would be artificial.

---

## Polling pattern

When an endpoint returns `{"tasks": [...]}`:

**In SDK examples:** Use `*_and_poll()` / `*AndPoll()` methods (see `sdk-best-practices.md`). Never show manual polling loops with `time.sleep()` or `time.Sleep()`.

**In curl examples:** Show the manual polling pattern **inside the curl tab**, after the request:

````mdx
<p>Run `GET /cloud/v1/tasks/{task_id}` every 5 seconds until
`state` is `FINISHED`, then read the resource ID from `created_resources`.</p>

<p>While provisioning:</p>
```json
{"state": "RUNNING", "created_resources": {}}
```

<p>When complete:</p>
```json
{"state": "FINISHED", "created_resources": {"instances": ["abc-123"]}}
```
````

---

## Optional and forbidden sections

**Optional standalone sections** (after the accordion, as separate `##` headings):
- `## Add an SSH key`, `## Filter images by OS`, `## Attach to a private network`
- `## Clean up` — always standalone, never inside the accordion

**Forbidden sections:** `## Prerequisites`, `## Next steps`, `## What's next`, `## Requirements`
