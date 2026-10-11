---
name: api-use-case
description: >-
  Adds a REST API tab (MethodSection id api inside MethodSwitch) to an existing
  Customer Portal article, mapping each Portal step to endpoints from the
  product's OpenAPI spec. Use when the user asks to add API coverage, an API
  tab, or the REST API version of the steps to a portal-only article, for
  example "add an API tab to this article" or "map these portal steps to API
  calls". Live-tests every curl, Python SDK, and Go SDK call, creates the Jira
  ticket and branch, writes the quickstart and step-by-step sections, and wraps
  content in MethodSwitch. Not for articles that already have an API tab (use
  api-audit), new articles (use write-from-scratch), or Terraform (use
  terraform-use-case).
---

Read an existing Customer Portal article, find the matching API endpoints in the OpenAPI spec, and write the `<MethodSection id="api">` section.

**Portal tab rule:** fix only the MDX syntax of the Portal tab (`<p>` tags around prose and numbered steps, `</MethodSection>` at column 0). Never touch its content, headings, or prose, not even one word. Read `.agents/references/api-portal-tab-rule.md` before editing the article.

## Scope — read exactly these files

1. This SKILL.md
2. The existing article specified by the user
3. `api-reference/services_documented/{product}_api.yaml` — the relevant OpenAPI spec
4. `.agents/references/api-live-testing.md` — Phases 2 and 3
5. `.agents/references/api-tab-structures.md` — Phase 5
6. `.agents/references/api-portal-tab-rule.md`
7. `.agents/references/sdk-best-practices.md` — SDK usage patterns
8. `.agents/references/ticket-and-branch.md` and `.agents/references/product-routing.md` — Phase 4
9. `.agents/references/mdx-rules.md`, `style-guide.md`, `procedures.md` — prose and MethodSwitch rules
10. `.agents/references/api-tab-review.md` — Phase 8

Do not read other articles unless the existing article cross-links to them and the link is directly relevant to mapping a Portal step to an API call.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Path to existing Portal article | Yes | The article that will receive the API tab |

---

## Phase 0 — Confirm the tab does not exist

```powershell
Select-String -Path "path/to/article.mdx" -Pattern 'MethodSection id="api"'
```

If `<MethodSection id="api">` already exists, stop and use the `api-audit` skill instead.

## Phase 1 — Read the Portal article

Read the full article. Identify:

1. What resources are created and in what order (for example network → subnet → instance → floating IP)
2. Dependencies between steps (for example the subnet needs `network_id` from an earlier step)
3. The flow type: sequential (Structure A) or independent operations (Structure B). The decision rule is in `api-tab-structures.md`.
4. The product from the file path — it determines which OpenAPI YAML to load.

## Phase 2 — Live API testing

Follow `.agents/references/api-live-testing.md`, "Live API testing". Test every call with `curl` and every Python SDK and Go SDK sample against the live API before writing anything.

## Phase 3 — Find the API endpoints

Follow `.agents/references/api-live-testing.md`, "Finding the API endpoints" and "Known gotchas". Run `python .agents/tools/api_check_style.py {article}` first and fix existing violations in the API tab. Look up SDK method signatures as described in `sdk-best-practices.md`, "Finding exact method signatures".

## Phase 4 — Create the Jira ticket and feature branch

**Mandatory. Do it immediately after live testing and endpoint mapping, before writing any MDX.** Do not wait for the user to ask. Do not write the API tab on `main`. Follow `.agents/references/ticket-and-branch.md`. In the ticket description include the article path, "Add API tab", the endpoints that were live-tested, and Structure A or B.

## Phase 5 — Write the API section

If `git branch --show-current` is `main`, Phase 4 was skipped. Stop writing, create the ticket and branch first.

Write the section using the template for the chosen structure in `.agents/references/api-tab-structures.md`. After writing each code block (curl, Python SDK, Go SDK), run the checker before moving on:

```powershell
python .agents/tools/api_check_style.py {relative/path/to/article.mdx}
```

Exit code must be 0. Fix every violation immediately.

## Phase 6 — Wrap in MethodSwitch

Run the checker immediately after wrapping. Exit code must be 0 before moving on.

### Critical layout rules — violations break every article

**Rule 1: `<MethodSwitch>` MUST be the first element after the import line.** Nothing — no paragraphs, no headings, no intro text — goes between the import and `<MethodSwitch>`. All content, including the article intro, belongs INSIDE a `<MethodSection>`.

```mdx
--- WRONG — content before MethodSwitch ---
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";

The intro paragraph explaining what this feature does.   ← WRONG

<MethodSwitch>
  ...
</MethodSwitch>

--- CORRECT — MethodSwitch immediately after import ---
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

<p>The intro paragraph explaining what this feature does.</p>

  ...
  </MethodSection>
  <MethodSection id="api" label="REST API">
  ...
  </MethodSection>
</MethodSwitch>
```

**Rule 2: Every prose paragraph and every numbered step inside `<MethodSection>` MUST be wrapped in `<p>` tags.** This applies to every standalone sentence or paragraph inside any `<MethodSection>`, and each numbered step is written as `<p>1. text</p>`. Bullet items (`-`) are NOT wrapped.

```mdx
--- WRONG ---
<MethodSection id="portal" label="Customer Portal">
This feature lets you configure X.

1. Open the portal.
2. Click **Create**.

--- CORRECT ---
<MethodSection id="portal" label="Customer Portal">

<p>This feature lets you configure X.</p>

<p>1. Open the portal.</p>

<p>2. Click **Create**.</p>
```

If the article has no MethodSwitch, wrap the existing portal content:

```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

  {existing portal content — do not change it, but wrap any prose in <p>}

  </MethodSection>
  <MethodSection id="api" label="REST API">

  {new API section written in Phase 5}

  </MethodSection>
</MethodSwitch>
```

If MethodSwitch already exists, add the `<MethodSection id="api">` after the portal section.

**Portal section:** fix `<p>` tags and `</MethodSection>` indentation only. See the Portal tab rule above.

## Phase 7 — Update frontmatter

Do not name Portal, API, or Terraform in `description`. If the article's subject changed, rewrite the sentence as a search summary of what the article is about:

```yaml
description: Create a Gcore Cloud Virtual Machine with an image, flavor, volume, and network.
```

Rules: one sentence, 140 characters maximum, no curly braces, no URL paths, no colons. Do not rewrite an existing description only because a method tab was added.

## Phase 8 — Review

Run the standalone tab test and every check in `.agents/references/api-tab-review.md`, including the API style checker with exit code 0.

---

## Output

Show the complete updated article. Then:

```
Article: [path]
API structure: [A — sequential / B — independent]
Steps covered: [N]
Real API tested: yes
Ticket: DOC-XXXX
Branch: DOC-XXXX
```

The ticket and branch already exist from Phase 4. Do not create another ticket or branch.

If a planning file exists for this batch (for example `_private/planning/cdn-api-tabs.md`), mark the finished article `[V]` with the ticket key immediately after the work is on `main`. Mark the next article in progress before starting it. Never leave the plan stale.

Commit and push only when the user asks, as described in `.agents/references/ticket-and-branch.md`. Load the `pr` skill if the user also asked for a PR.
