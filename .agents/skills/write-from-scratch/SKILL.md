---
name: write-from-scratch
description: Write a new Gcore documentation article from source material such as a Jira brief, Confluence page, or direct description. Use when asked to create an article that does not exist yet.
---

Write a new article from source material, following the correct structure for
the article type and the project style guide.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/content-types.md` — article type decision and templates
3. `.agents/references/style-guide.md` — writing rules
4. `.agents/references/procedures.md` — step format, Optional prefix, location/purpose before action
5. `.agents/references/mdx-rules.md` — MDX and frontmatter rules
5. One or two existing articles of the same type (found during Phase 3)
6. Source material: Jira brief, Confluence page, or user input
7. `.agents/references/mcp-tools/confluence.md` — only if fetching from Confluence
8. `.agents/references/mcp-tools/jira.md` — only if fetching from Jira directly

Do not read more than two reference articles. Do not read articles from other
product areas unless directly relevant.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Topic or feature description | Yes | What the article is about |
| Source material | One of these | Jira brief, Confluence URL, or free-text description |
| Article type | No | If not specified, determine from content-types.md |
| Product area | No | If not specified, infer from topic |

If coming from `jira-context` skill — the brief from that skill is your source material.
Do not re-fetch the Jira ticket.

---

## Phase 1 — Gather source material

Collect everything needed to write accurately. Do not write from memory or assumptions.

**If a jira-context brief was provided:**
Use it directly. The brief already contains what changed, which article, and scope of work.

**If a Jira ticket ID is provided directly:**
Fetch the ticket. Extract: summary, description, acceptance criteria, linked dev ticket.
Follow the instructions in `.agents/references/mcp-tools/jira.md`.

**If a Confluence URL is provided:**
Fetch the page. Look for: feature description, API fields, known limitations, screenshots.
Follow the instructions in `.agents/references/mcp-tools/confluence.md`.
Never copy Confluence text verbatim — use it to understand the feature, write in your own words.

**If free-text description is provided:**
Use it as the primary source. Note what is known vs what needs verification.

**For API content — check the OpenAPI spec:**
Find the relevant YAML file in `/api-reference/services_documented/{product}_api.yaml`.
Verify field names, parameter types, and endpoint paths against the spec — not against
Confluence or memory.

**Mark gaps:** If important details are missing (exact field names, UI navigation path,
behavior in edge cases), note them as `{TODO: verify X}` inline in the draft.
Do not invent technical details.

---

## Phase 2 — Determine article type

Read `.agents/references/content-types.md` and answer two questions:

**1. Does the feature have both Customer Portal UI and REST API coverage?**
- Both → Tabbed article
- Portal only → Portal-only article
- API only → API-only article

**2. For articles with an API section — do the steps require sequential execution?**
- Yes (outputs feed into next steps) → Structure A: Quickstart + Step-by-step
- No (independent operations) → Structure B: standalone sections

**Rule of thumb:**
- "Create" / "Deploy" articles → almost always sequential (Structure A)
- "Manage" / "Configure" articles → almost always independent (Structure B)
- Test: "Can the user do Step 3 without Steps 1 and 2?" If yes → Structure B

If unsure — ask the user before writing.

---

## Phase 3 — Find the file path and a reference article

**Determine the file path:**
```
/{product}/{section}/{article-name}.mdx
```

- Product: matches the top-level folder (`cloud`, `cdn`, `dns`, `waap`, etc.)
- Section: matches the subfolder within the product
- Filename: lowercase, hyphens, verb-noun pattern — `create-an-instance.mdx`,
  `configure-firewall-rules.mdx`

**Find one reference article:**
Look for an existing article of the same type in the same product folder:
```powershell
ls {product}/{section}/*.mdx
```

Read it fully. Use it to understand:
- The depth of explanation typical for this product
- How UI steps are formatted
- How code examples are presented
- The tone and level of assumed knowledge

---

## Phase 4 — Write the article

Use the template from `.agents/references/content-types.md` for the article type
determined in Phase 2.

### Opening sentence

The first sentence must state what the reader will accomplish and why it matters.
Never open with "This guide covers...", "This article explains...", or any description
of the document itself.

**Bad:** "This guide covers creating a virtual machine using the Gcore Cloud API."
**Good:** "Deploy a Linux virtual machine using the Gcore Cloud REST API — create
SSH keys, select a flavor and image, and assign a floating IP address."

### Writing each section

Before writing a section:
1. Know what the section's goal is — what does the reader need after reading it?
2. Write the intro sentence for that section first
3. Then the content

Follow the paragraph formulas in `style-guide.md`:
- Maximum 2 sentences per paragraph (Formulas A and B)
- No root-word pairs in the same paragraph
- No filler words: just, simply, ensure, platform

### Portal steps

For `<MethodSection id="portal">`:
- Numbered steps using `1.` (not `1\.`)
- Bold for UI element names: Click **Create**, In the **Name** field
- Wrap standalone prose paragraphs in `<p>` tags
- No `####` headings — use **bold text** for sub-labels
- Screenshot placeholders where needed: `{TODO: screenshot — [what it shows]}`

### API steps

For `<MethodSection id="api">` or standalone API articles:

**Opening sentence** (required, before the `<Info>` block):
Describe what this section enables. Not "The steps below...".
Good: "Create a subnet inside an existing network and customize its DHCP settings."

**`<Info>` block** (required):
```mdx
<Info>
A permanent [API token](/account-settings/api-tokens) is required, along with a
[project ID](...) and a [region ID](...).
</Info>
```

**Tab order:** always Python SDK → Go SDK → curl (curl always last).
**In Quickstart:** Python SDK and Go SDK only — no curl tab.

**Step anatomy** (for Structure A sequential steps):
1. One sentence: why this step matters in the flow
2. Key parameters table (non-obvious required fields only)
3. Code tabs: Python SDK → Go SDK → curl
4. `The API returns:` label, then the response JSON
5. Inline link to API reference on a meaningful noun

**Quickstart scripts:**
- Comment every step: `# Step 1.` / `// Step 1.` — never combine (`# Step 3+4`)
- Must run as-is after setting three env vars — no other substitutions
- Never hardcode region-specific IDs — select by characteristics:
  ```python
  # IDs are region-specific; selects 2 vCPU / 4 GB RAM
  flavor = next(f for f in flavors if f.vcpus == 2 and f.ram == 4096)
  ```

### Marking uncertainty

When technical details cannot be verified from source material:
```
{TODO: verify — [what needs to be checked and where]}
```

Use for: exact UI navigation paths, field names not in the spec, behavior in
edge cases, screenshot content.

Do not publish speculation as fact.

---

## Phase 5 — Verify agent-added claims

Before writing frontmatter, find everything you wrote that did NOT come directly
from the provided source material.

**The rule:** if the contributor or source gave you the information — trust it and
use it, even if it is not yet in Jira or Confluence. Verification only targets
what you added through your own reasoning.

**What counts as agent-added:**
- A number or limit you inferred: "the timeout is probably 30 seconds" or "standard
  limit is 100" — when the source didn't state it
- A behavioral claim you deduced: "since it uses REST, it returns JSON" or "this
  will automatically scale"
- A step you added because "it seems logical this would be needed"
- Any phrase starting with "typically", "usually", "generally", "by default" when
  the source did not say this

**What does NOT need verification:**
- Numbers, limits, and specs explicitly stated by the contributor in their input
- Values taken directly from the Jira ticket description or Confluence page
- Technical details confirmed by real API testing in Phase 1
- Values copied from the OpenAPI YAML spec

**For each agent-added claim, check in order:**

1. **Main Jira ticket** — is it stated in description or acceptance criteria?
2. **Parent ticket** — does the parent epic specify this?
3. **Sibling tickets** — other issues linked to the same parent
4. **Confluence pages** — linked from any ticket or searchable by feature name

Use `.agents/references/mcp-tools/jira.md` and `.agents/references/mcp-tools/confluence.md`.

**Decision:**

| Situation | Action |
|-----------|--------|
| Claim came from contributor or source | Keep it — no verification needed |
| Claim confirmed in Jira or Confluence | Keep it |
| Claim is your own reasoning, not found anywhere | `{TODO: verify — added by agent, not confirmed in source}` |
| Sources disagree | Use most authoritative (Confluence spec > ticket description), note the discrepancy |

When in doubt, ask yourself: **"Where did I get this from?"**
If the answer is "I reasoned it" or "it seemed logical" — mark it as TODO.

---

## Phase 6 — Frontmatter

Every article requires these fields:

```yaml
---
title: [Full title — shown in browser tab]
sidebarTitle: [Short sidebar label]
ai-navigation: [One sentence, starts with action verb, max 160 chars, no {braces} or /slashes/]
---
```

Write `ai-navigation` last — after the article is complete, it is easier to
summarize accurately.

Check the rules in `.agents/references/mdx-rules.md` — curly braces and colons in
`ai-navigation` break the Mintlify build.

---

## Phase 7 — Validate before showing

**MDX:**
- [ ] Import line includes `.jsx` extension: `from "/snippets/method-switch.jsx"`
- [ ] `<MethodSwitch>` wraps both sections, `label` is on `<MethodSection>`
- [ ] All prose inside `<MethodSection>` wrapped in `<p>` tags or proper list syntax
- [ ] No `{identifier}` in inline backtick spans — use `<code>` with `&nbsp;`
- [ ] No `####` headings inside `<MethodSection>`
- [ ] Closing `</MethodSection>` tags at column 0 (not indented after a list)

**Frontmatter:**
- [ ] `title` present
- [ ] `ai-navigation` present, no forbidden characters
- [ ] No `description` field

**Style:**
- [ ] Opening sentence does not describe the document
- [ ] No forbidden sections: `## Prerequisites`, `## Next steps`, `## See also`
- [ ] Every `##` heading followed by a prose sentence before code or table
- [ ] Headings in sentence case
- [ ] Bold only for UI element names
- [ ] No forbidden words: just, simply, ensure, platform, obviously

---

## Phase 8 — Output

Show the complete article content. Then:

```
File: [path]
Article type: [type from content-types.md]
Structure: [A — sequential / B — independent / N/A]

TODO items requiring verification:
- {TODO: ...} at Step N — [what to check]
- {TODO: ...} in [section] — [what to check]

Recommended next step:
- No TODOs → ready for review, create PR with skill pr
- Has portal TODOs → run skill full-audit to verify UI steps
- Has API TODOs → verify against API spec or test manually
```

When the user confirms the result looks good — load `.agents/skills/pr/SKILL.md`
to create the branch, commit, and open a draft PR.
