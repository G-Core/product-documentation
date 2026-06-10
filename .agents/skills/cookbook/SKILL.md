---
name: cookbook
description: Compile an end-to-end scenario guide that combines multiple Gcore products or sections into one article. Use when asked for a real-world guide spanning more than one product or section.
---

Take a scenario topic, find all relevant source articles across the repository,
determine the correct sequence, and write a cookbook article that guides the
reader from start to finished result.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/content-types.md` — cookbook structure and template
3. `.agents/references/style-guide.md` — writing rules
4. `.agents/references/mdx-rules.md` — frontmatter and MDX rules
5. Source articles found during Phase 2 (read only the relevant sections)
6. `.agents/references/mcp-tools/playwright.md` — only if user agrees to end-to-end testing

Do not read every article in the repo. Read only articles confirmed relevant
during the search phase.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Scenario topic | Yes | What the reader wants to achieve end-to-end |
| Target audience | No | Infer from topic if not specified |
| Products involved | No | Infer from topic, confirm during Phase 1 |

**Example topics:**
- "Set up video streaming with CDN delivery and DDoS protection"
- "Deploy a Kubernetes application with load balancing and object storage"
- "Configure a multi-region CDN with custom SSL and origin shield"

---

## Phase 1 — Understand the scenario

Before searching for articles, build a clear picture of what the cookbook covers.

Answer these questions:

**Who is the reader?**
A developer or DevOps engineer who already knows the individual products and
wants to connect them into a working system. Not a beginner — do not explain
basic product concepts inline, link to overview articles instead.

**What will the reader have when done?**
State this as a concrete outcome, not a list of steps. Example:
- "A live video stream delivered via CDN with automatic DDoS mitigation"
- "A Kubernetes cluster with persistent storage and a public load balancer"

**Which Gcore products are involved?**
List each product. For each one — does it have existing documentation in this repo?
```powershell
ls {product}/ --directory
```

**What are the dependencies between products?**
Some products must be set up before others because they produce outputs the next
step needs. Map these before writing:

```
Example: video streaming + CDN
  1. Streaming — must come first, produces the origin URL
  2. CDN — needs the origin URL from step 1 to configure the resource
  3. DDoS Protection — can be added after CDN is working

Example: K8s + load balancer + object storage
  1. Network — load balancer needs a subnet
  2. Kubernetes cluster — needs the network
  3. Load balancer — connects to the cluster
  4. Object storage — independent, can be done in parallel with K8s
```

If the dependencies are unclear — determine them by reading the "what you need
before starting" context in the relevant product articles.

---

## Phase 2 — Find source articles

Search for articles covering each product in the scenario:

```powershell
# Find articles in a product folder
ls {product}/ -Recurse -Filter "*.mdx" | Select-Object Name, FullName

# Search by keyword across products
grep -r "load balancer" --include="*.mdx" -l
```

For each product in the scenario, find:
- The main how-to article (create / get started)
- Any prerequisite articles (e.g. "create a network" before "create a load balancer")

Read only the **first paragraph and headings** of each candidate article to confirm
it covers the right topic. Do not read full articles yet.

Build a source map:

```
Step 1: Create a streaming live stream
  Source: /streaming/live-streams/create-a-live-stream.mdx

Step 2: Configure CDN resource for streaming
  Source: /cdn/getting-started/create-cdn-resource.mdx

Step 3: Enable DDoS protection
  Source: /ddos-protection/...
```

If a required step has no article in the repo — note it as a gap:
`{TODO: no existing article for X — needs to be written separately}`

---

## Phase 3 — Determine file path and title

**File path:**
```
/{primary-product}/use-cases/{scenario-slug}.mdx
```
or if the scenario spans equally across products:
```
/use-cases/{scenario-slug}.mdx   (if this folder exists)
```

Use the product where the reader spends the most time as the primary product.

**Title:** the outcome the reader achieves, not a list of products.
- Good: "Stream live video with CDN delivery and DDoS protection"
- Bad: "Streaming + CDN + DDoS Protection setup guide"

**sidebarTitle:** short version of the title (5 words max):
- "Live streaming with CDN and DDoS"

---

## Phase 4 — End-to-end testing (ask the user)

If the scenario involves portal UI steps — ask:

> I can walk through this entire scenario in the Gcore Customer Portal to
> verify that the steps work in the correct order and that all required
> settings actually exist.
>
> - **Yes, test end-to-end** — I will verify each step produces the expected
>   output before the next step uses it
> - **No, write from existing articles** — I will document the sequence based
>   on what the source articles say, and mark unverified connections as TODO

Wait for the answer.

**If yes:**
- Follow the Playwright protocol in `.agents/references/mcp-tools/playwright.md`
- Execute the scenario from start to finish
- Specifically verify handoff points: does step N actually produce what step N+1 needs?
- Note any differences between what source articles describe and what the portal shows

**If no:**
- Write from source articles
- Mark every cross-product handoff that was not verified:
  `{TODO: verify that the output of step N is the correct input for step N+1}`

---

## Phase 5 — Write the cookbook

Use the cookbook template from `.agents/references/content-types.md`.

### Opening paragraph

State who this is for and what they will have when done.
Do not open with "This guide covers..." or a list of products.

Good:
> A live video stream requires three Gcore services working in sequence:
> Streaming provides the ingest endpoint and transcoding, CDN distributes
> the content to viewers, and DDoS Protection absorbs volumetric attacks
> before they reach the origin. This cookbook connects all three into a
> working pipeline.

### Prerequisites

Integrate into the opening paragraph as plain text — not a separate section.
State only non-obvious requirements: an active account, a specific plan tier,
a resource that must exist before starting.

### Steps

Each step follows this pattern:

```mdx
## Step N. {Verb + object — what happens in this step}

{One paragraph: why this step is needed at this point in the sequence.
What does it produce that the next step needs?}

{2–5 key actions the reader must take — brief, imperative.}

For the full procedure, see [{article name}]({path}).

{Optional: note the specific output to copy for the next step.}
> After completing this step, copy the **Origin URL** — you will need it in Step 2.
```

**Rules for each step:**
- Brief instructions only — do not duplicate the full how-to article
- Always link to the source article with 1–2 word link text
- Explain the dependency explicitly: "because Step 3 needs the X from Step 2"
- If a step produces an output the reader must copy — call it out explicitly

### Cross-product handoffs

These are the most important part of a cookbook — the connections that the
individual how-to articles do not cover. Make them explicit:

```mdx
## Step 2. Create a CDN resource

CDN needs an origin URL — the address where your content lives before delivery.
Use the playback URL from the streaming live stream created in Step 1.

1. In the Customer Portal, go to **CDN** > **CDN Resources** > **Create**.
2. In the **Origin** field, paste the streaming playback URL from Step 1.
...

For the full procedure, see [create a CDN resource](/cdn/getting-started/create-cdn-resource).
```

### Expected outcome section

End with a concrete description of what the reader should see when done.
Not a checklist — a paragraph describing the working system.

```mdx
## Expected outcome

{Describe the working system: what is running, how it behaves, how to verify it.}

If anything is not working as described, check:
- {common issue 1 and where to find help}
- {common issue 2 and where to find help}
```

---

## Phase 6 — Validate

**MDX:**
- [ ] Frontmatter complete: `title`, `sidebarTitle`, `ai-navigation`
- [ ] No `description` field
- [ ] No `{identifier}` in inline backtick spans

**Structure:**
- [ ] No `## Prerequisites` section — requirements in opening paragraph
- [ ] No `## Next steps` section — use inline links
- [ ] Every `##` heading followed by a prose sentence
- [ ] Headings in sentence case

**Content:**
- [ ] Each step links to its source article
- [ ] Every cross-product handoff explicitly documented
- [ ] `## Expected outcome` section present
- [ ] All `{TODO:}` items listed

**`ai-navigation`:**
One sentence, action verb, all products mentioned, max 160 chars,
no curly braces, no URL paths:
```yaml
ai-navigation: Stream live video through Gcore CDN with DDoS protection by
configuring a live stream origin, a CDN resource, and a DDoS protection profile.
```

---

## Output

Show the complete article. Then:

```
File: [path]
Source articles used: [N]
  - [path 1]
  - [path 2]

Cross-product handoffs documented: [N]

TODO items:
- {TODO: ...}

Gaps (steps with no source article):
- [step] — no existing article found

Recommended next step:
- No TODOs → ready for review, create PR
- Has TODOs → verify handoffs, then create PR
```

Do not commit without explicit user confirmation.
