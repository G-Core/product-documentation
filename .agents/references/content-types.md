# Content Types — Gcore Product Documentation

Defines the article types used in this repository, when to use each,
and the required structure for each type.
Load this file when a skill tells you to. Do not load it proactively.

---

## Decision: which type to use

Answer these two questions before starting any article:

**1. Does the feature have both a Customer Portal UI and a REST API?**
- Yes → use a **Tabbed article** (MethodSwitch with portal + api sections)
- Portal only → use a **Portal-only article**
- API only → use an **API-only article**

**2. For the API section — do the steps require sequential execution?**
- Yes (outputs of earlier steps feed into later steps) → use **Structure A** (Quickstart + Step-by-step)
- No (operations are independent, can be done in any order) → use **Structure B** (standalone sections)

**Rule of thumb:** "create" and "deploy" articles are almost always sequential (Structure A).
"manage" and "configure" articles are almost always independent (Structure B).
Test: "Can the user do Step 3 without having done Steps 1 and 2?" If yes → Structure B.

---

## Type 1: Tabbed article (most common)

### When to use

The feature is accessible via both the Customer Portal UI and the REST API.
All methods live in one MDX file — never create separate files per method.

### File location

```
/{product}/{section}/{article-name}.mdx
```

### Frontmatter

```yaml
---
title: Create a Virtual Machine
sidebarTitle: Create an instance
ai-navigation: Create Linux or Windows Virtual Machines in Gcore Cloud via Customer Portal by configuring image, flavor, volumes, network, and firewall, or via REST API using the Instances API.
---
```

### Structure

```mdx
---
title: ...
sidebarTitle: ...
ai-navigation: ...
---

import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

  {Portal content — see Portal section rules below}

  </MethodSection>
  <MethodSection id="api" label="REST API">

  {API content — use Structure A or Structure B depending on the flow}

  </MethodSection>
</MethodSwitch>
```

### Portal section rules

- Opening sentence inside `<MethodSection>` — what the user will accomplish
- Numbered steps using `1.` (not `1\.`) — see mdx-rules.md
- Prose paragraphs between steps wrapped in `<p>` tags
- Screenshots in `<Frame>` blocks after the relevant step
- Bold for UI element names: Click **Create Instance**, In the **Name** field
- No `####` headings — use bold text for sub-labels instead

### API section — Structure A (sequential flow)

Use when steps must be executed in order and outputs feed into later steps.

```mdx
<MethodSection id="api" label="REST API">

{One intro sentence: what this section enables — not "The steps below..."}

<Info>
A permanent [API token](/account-settings/api-tokens) is required, along with a
[project ID](...) and a [region ID](...).
</Info>

## Quickstart

{One sentence: what the scripts do. Not "Complete scripts for the full flow."}

<Tabs>
  <Tab title="Python SDK">
    ```python
    # Step 1. ...
    # Step 2. ...
    ```
  </Tab>
  <Tab title="Go SDK">
    ```go
    // Step 1. ...
    // Step 2. ...
    ```
  </Tab>
</Tabs>

## Step-by-step

<p>Each step below explains what the call does, which parameters matter, and what the response looks like.</p>

<Accordion title="Show all steps">

### Step 1. {Verb + object}

{One sentence: why this step is needed.}

| Parameter | Required | Description |
|-----------|----------|-------------|
| `param` | Yes | What it does |

<Tabs>
  <Tab title="Python SDK">```python ... ```</Tab>
  <Tab title="Go SDK">```go ... ```</Tab>
  <Tab title="curl">```bash ... ```</Tab>
</Tabs>

The API returns:

```json
{"tasks": ["abc-123"]}
```

</Accordion>

</MethodSection>
```

### API section — Structure B (independent operations)

Use when operations are unrelated and can be performed in any order.

```mdx
<MethodSection id="api" label="REST API">

{One intro sentence.}

<Info>...</Info>

## {Operation name}

{One sentence: what this operation does.}

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

...

</MethodSection>
```

---

## Type 2: Portal-only article

### When to use

The feature exists only in the Customer Portal UI, or the API tab has not been written yet.
Mark the API tab as TODO if you know it will be added later.

### Structure

Same as Tabbed article but with only the portal `<MethodSection>`.
If an API section will be added in the future:

```mdx
<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
  {Portal content}
  </MethodSection>
  <MethodSection id="api" label="REST API">
  <p>{TODO: API section — link to Jira ticket or note what is needed.}</p>
  </MethodSection>
</MethodSwitch>
```

Do not publish a completely empty API section — add the TODO note.

---

## Type 3: API-only article

### When to use

A standalone guide for performing a workflow entirely via REST API.
Lives in `/{product}/via-api/` or `/{product}/api/`.
No Customer Portal steps — no MethodSwitch component.

### File location

```
/{product}/via-api/{article-name}.mdx
```

### Frontmatter

```yaml
---
title: Deploy a Linux VM via API
sidebarTitle: Deploy a VM
ai-navigation: Deploy a Linux Virtual Machine using the Gcore Cloud REST API — create SSH keys, select a flavor and image, create the instance, and assign a floating IP address.
---
```

### Structure A: sequential creation flow

```mdx
---
...
---

{Opening sentence: what is built and why. No "This guide..."}

<Info>
A permanent [API token](/account-settings/api-tokens) is required, along with a
[project ID](...) and a [region ID](...).
</Info>

Open a terminal and set these environment variables before running the examples:

```bash
export GCORE_API_KEY="{YOUR_API_KEY}"
export GCORE_CLOUD_PROJECT_ID="{YOUR_PROJECT_ID}"
export GCORE_CLOUD_REGION_ID="{YOUR_REGION_ID}"
```

## Quickstart

{One sentence describing what the scripts do.}

<Tabs>
  <Tab title="Python SDK">```python ... ```</Tab>
  <Tab title="Go SDK">```go ... ```</Tab>
</Tabs>

## Step-by-step

<p>Each step below explains what the call does, which parameters matter,
and what the response looks like.</p>

<Accordion title="Show all steps">

### Step 1. {Verb + object}

{One sentence: why this step matters in the flow.}

| Parameter | Required | Description |
|-----------|----------|-------------|

<Tabs>
  <Tab title="Python SDK">```python ... ```</Tab>
  <Tab title="Go SDK">```go ... ```</Tab>
  <Tab title="curl">```bash ... ```</Tab>
</Tabs>

The API returns:

```json
{"tasks": ["abc-123"]}
```

</Accordion>

## {Optional section — standalone ##}

{e.g., ## Clean up, ## Add an SSH key, ## Filter by OS}
```

### Structure B: independent operations (manage/configure)

```mdx
---
...
---

{Opening sentence.}

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

## {Another operation name}
```

### Code tab order

Always: **Python SDK → Go SDK → curl** (curl is always last).
In Quickstart: Python SDK and Go SDK only — curl cannot be a single runnable script.

### Quickstart script rules

- Every logical step: `# Step 1.` (Python) or `// Step 1.` (Go) — never `# Step 3+4`
- Script must run as-is after setting the three env vars — no other substitutions
- Never hardcode region-specific IDs (flavor names, image IDs):
  - Flavor: select by characteristics — `next(f for f in flavors if f.vcpus == 2 and f.ram == 4096)`
  - Image: search by name pattern — `"ubuntu-22.04" in img.name`
- Add a comment when selecting: `# IDs are region-specific; selects 2 vCPU / 4 GB RAM`

### Forbidden sections in API articles

- `## Prerequisites` — put requirements in the `<Info>` block
- `## Next steps` / `## What's next` — use inline cross-links
- `## Clean up` inside the accordion — it is always a standalone `##` section at the end

---

## Type 4: Overview / landing article

### When to use

A product or section landing page. Introduces the product, lists what the section covers,
links to the main articles. Usually the `index.mdx` or `overview.mdx` of a folder.

### Structure

```mdx
---
title: Virtual Machines
sidebarTitle: Overview
ai-navigation: Overview of Gcore Cloud Virtual Machines — create, manage, connect, and configure VM instances using the Customer Portal or REST API.
---

{One paragraph: what this product is and what it enables. Value before mechanics.}

## {Main topic 1}

{One sentence intro.}

- [Article name](/path/to/article)
- [Article name](/path/to/article)

## {Main topic 2}

...
```

**Rules:**
- No step-by-step instructions — link to the relevant how-to articles
- No `## What's next` or `## Next steps`
- No standalone link-dump sections — every link must have a sentence of context

---

## Type 5: Concept article

### When to use

Explaining what something is, how it works architecturally, when to use it.
Not a step-by-step guide. No MethodSwitch.

### Structure

```mdx
---
title: Load Balancer overview
sidebarTitle: Overview
ai-navigation: ...
---

{One paragraph: what this thing is and what problem it solves.}

## How it works

{Explanation of the mechanism. Use Formula A/B from style-guide.md.}

## {Use cases / When to use}

{Describe the scenarios where this applies.}

## {Limitations / Known constraints}

{Only if there are non-obvious constraints the reader needs before starting.}
```

**Rules:**
- No numbered steps — this is explanation, not instruction
- No `## Prerequisites`
- Link to the relevant how-to article at the end using an inline link, not a `## Next steps` section

---

## Type 6: Cookbook article

### When to use

An end-to-end scenario guide that pulls steps from multiple products or sections.
The reader wants to accomplish a complete real-world goal (e.g., "set up CDN for video
streaming with DDoS protection"). Lives in `/cookbook/` or in the most relevant product folder.

### File location

```
/cookbook/{scenario-slug}.mdx
```
or
```
/{primary-product}/use-cases/{scenario-slug}.mdx
```

### Structure

```mdx
---
title: {Scenario title — what the reader will have when done}
sidebarTitle: {Short label}
ai-navigation: {All products involved, the outcome.}
---

{One paragraph: who this guide is for and what they will achieve.
Mention all Gcore products involved.}

## Prerequisites

{Integrate as prose in the opening paragraph OR as a brief inline list.
Never as a separate `## Prerequisites` section with bullets.}

## Step 1. {First major action}

{Brief instructions — 3–5 sentences max. Then link to the source article for full details.}

See [full instructions](/path/to/source-article) for the complete steps.

## Step 2. {Second major action}

...

## Expected outcome

{What the reader should see when done. One paragraph.}
```

**Rules:**
- Each step: brief instructions + link to the source article for full details
- Do NOT copy entire articles — link to them
- Cross-product links, not inline repetition of other articles' content
- `## Expected outcome` is the only section allowed at the end — no `## Next steps`

---

## Choosing between existing types: quick reference

| Situation | Type to use |
|-----------|-------------|
| Feature exists in Portal AND API, steps are sequential | Tabbed, Structure A |
| Feature exists in Portal AND API, operations are independent | Tabbed, Structure B |
| Feature exists only in Portal | Portal-only |
| Standalone API guide, sequential flow | API-only, Structure A |
| Standalone API guide, manage/configure | API-only, Structure B |
| Section landing page | Overview |
| Explaining what something is | Concept |
| End-to-end scenario across products | Cookbook |
| API tab not yet written | Tabbed with TODO placeholder in api section |
