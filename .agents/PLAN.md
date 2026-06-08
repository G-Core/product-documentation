# Agent Infrastructure Plan — Gcore Product Documentation

## Context for a new session

This file is the source of truth for building the agent orchestration system
in this repository. Read it at the start of any session before doing anything.
The working directory is `C:\Projects\product-documentation`.

### What this repo is

Mintlify-based documentation site for Gcore products. Content is MDX files
organized by product folder (`cloud/`, `cdn/`, `dns/`, etc.). The custom
`MethodSwitch` component handles tabbed articles (Customer Portal / REST API /
Terraform / CLI) in a single MDX file. OpenAPI specs live in
`api-reference/services_documented/`.

### What we are building

An agent orchestration system that lets two audiences use AI to work with
this documentation:

**Technical writers (internal team):**
- Update an existing article
- Write a new article from scratch
- Analyze a Jira ticket to understand what needs documenting
- Add a REST API tab to an existing Customer Portal article
- Run a full audit of an article: test every step in the real portal or via
  API, find discrepancies, update the article

**Contributors (product teams):**
- Provide context about a new feature or change, get a draft PR back

**Special format:**
- Cookbook articles: given a topic, collect steps from multiple articles and
  compile into one end-to-end guide

### Available MCP tools

The following MCP servers are configured in this environment:

| MCP | Use for |
|-----|---------|
| Jira | Reading tickets, acceptance criteria, linked issues |
| Confluence | Internal product docs, release notes, specs |
| Playwright | Browser-based portal testing at https://portal.gcore.com |

---

## Architecture

```
product-documentation/
│
├── AGENTS.md                         ← AI entry point (auto-loaded by agent)
├── CONTRIBUTING.md                   ← Human entry point (leave for later)
│
└── .agents/
    ├── PLAN.md                       ← THIS FILE
    │
    ├── skills/
    │   ├── update-page/
    │   │   └── SKILL.md
    │   ├── write-from-scratch/
    │   │   └── SKILL.md
    │   ├── jira-context/
    │   │   └── SKILL.md
    │   ├── api-use-case/
    │   │   └── SKILL.md
    │   ├── full-audit/
    │   │   └── SKILL.md
    │   ├── feature-draft/
    │   │   └── SKILL.md
    │   └── cookbook/
    │       └── SKILL.md
    │
    └── references/
        ├── style-guide.md
        ├── mdx-rules.md
        ├── content-types.md
        └── mcp-tools.md
```

---

## Implementation order and status

Work through files in this exact order. Update the status column as you go.

## Source files (read before writing any skill or reference)

These existing files contain ready-made content. Do not write from scratch
what already exists here. Adapt, extract, and combine.

| Source file | Contains | Used by |
|-------------|----------|---------|
| `C:\Projects\docops-agent2\CLAUDE.md` | api-use-case algorithm (4 phases), article structure A+B, code style, quality checklist, MDX rules | `skills/api-use-case`, `references/mdx-rules` |
| `C:\Projects\update_outdated_articles\CLAUDE.md` | full-audit algorithm (4 phases), Playwright protocol, screenshot standards, git workflow, SSO login flow, portal quirks | `skills/full-audit`, `references/mcp-tools` |
| `C:\Projects\docops-agent2\.continue\guides\style-guide.md` | 694-line style guide: voice, formulas, forbidden words, Gcore naming | `references/style-guide` |
| `C:\Projects\docops-agent2\.continue\guides\style-rules-formatting.md` | Bold rules, em-dash, cognitive load density | `references/style-guide` |
| `C:\Projects\docops-agent2\.continue\guides\style-rules-links.md` | Link text rules, duplicate link rules, banned patterns | `references/style-guide` |
| `C:\Projects\docops-agent2\.continue\guides\style-rules-structure.md` | Heading rules, forbidden sections, prose-before-code | `references/style-guide` |
| `C:\Projects\docops-agent2\.continue\guides\style-rules-voice.md` | No "you/your", forbidden words, connector rules | `references/style-guide` |
| `C:\Projects\docops-agent2\.continue\guides\scope-guide.md` | 6-category Jira classification, matrix, red/green flags, examples | `skills/jira-context` |
| `C:\Projects\docops-agent2\.continue\guides\reflection-guide.md` | Logical reasoning rules, anti-patterns, source verification | `AGENTS.md` (add section) |
| `C:\Projects\docops-agent2\.continue\reference\jira-statuses.md` | Which Jira statuses allow work, which do not | `skills/jira-context` |
| `C:\Projects\docops-agent2\.continue\guides\proofreading-checklist.md` | Pre-commit checklist | `skills/full-audit`, `skills/write-from-scratch` |
| `C:\Projects\product-documentation\CONTRIBUTING.md` | MethodSwitch rules, MDX gotchas, frontmatter fields | `references/mdx-rules` |

---

## Implementation order and status

Work through files in this exact order. Update the status column as you go.

| # | File | Status | Action | Primary source |
|---|------|--------|--------|----------------|
| 1 | `.agents/PLAN.md` | DONE | Written | — |
| 2 | `AGENTS.md` | DONE | Written | — |
| 3 | `.agents/references/style-guide.md` | DONE | Adapt + combine | docops-agent2/guides/style-*.md (5 files) |
| 4 | `.agents/references/mdx-rules.md` | DONE | Combine | CONTRIBUTING.md + both CLAUDE.md MDX sections |
| 5 | `.agents/references/content-types.md` | DONE | Write new | — |
| 6 | `.agents/references/mcp-tools/` | DONE | Подпапка: playwright.md + jira.md + confluence.md + setup.md | update_outdated_articles/CLAUDE.md + jira-statuses.md |
| 6b | `.agents/references/review-process.md` | DONE | Write new | docops-agent2/guides/review-process.md + proofreading-checklist.md |
| 6c | `.agents/references/procedures.md` | DONE | Write new | Cloudflare procedures.md + new rules not in docops-agent2 |
| 7 | `.agents/skills/update-page/SKILL.md` | DONE | Write new | reflection-guide.md + style/mdx references |
| 8 | `.agents/skills/jira-context/SKILL.md` | DONE | Adapt | scope-guide.md + jira-statuses.md |
| 9 | `.agents/skills/write-from-scratch/SKILL.md` | DONE | Write new | docops-agent2/CLAUDE.md Phase 3 + content-types.md |
| 10 | `.agents/skills/api-use-case/SKILL.md` | DONE | Adapt | docops-agent2/CLAUDE.md (near-complete) |
| 11 | `.agents/skills/full-audit/SKILL.md` | DONE | Adapt | update_outdated_articles/CLAUDE.md (near-complete) |
| 12 | `.agents/skills/feature-draft/SKILL.md` | DONE | Write new | Combine Jira + Playwright + draft phases |
| 13 | `.agents/skills/cookbook/SKILL.md` | DONE | Write new | — |

---

## File specifications

What each file must contain. Use this as the brief when writing each file.

---

### File 2: `AGENTS.md`

**Purpose:** The only file an agent reads automatically. It is a dispatch
table, not a manual. Every critical rule that applies to ALL tasks goes here
inline. Everything task-specific stays in skills.

**Must contain:**

1. One-paragraph repo overview (framework, content format, key constraint)
2. Folder structure — patterns only, no file lists:
   - `/{product}/{section}/article.mdx` — content
   - `/api-reference/services_documented/{product}_api.yaml` — OpenAPI specs
   - `/snippets/` — shared JSX/MDX components
   - `/.agents/skills/` — skills (load on demand)
   - `/.agents/references/` — references (load when skill says to)
3. Three critical inline rules (apply to every task, no exceptions):
   - Never create separate files for Portal/API/Terraform — use MethodSwitch tabs
   - Never use `description` in frontmatter — use `ai-navigation`
   - Internal links must be root-relative, no `https://docs.gcore.com` prefix
4. Task → Skill mapping table (all 6 skills)
5. Hard stop: "Load one skill per task. Read no other files until the skill
   tells you to."

**Must NOT contain:**
- Lists of actual article files
- Full MDX syntax rules (those go in mdx-rules.md)
- Style rules (those go in style-guide.md)
- Anything that makes the agent want to explore the repo before getting a task

---

### File 3: `.agents/references/mdx-rules.md`

**Purpose:** All technical MDX rules distilled from CONTRIBUTING.md.
Loaded only when a skill explicitly says to.

**Must contain:**

1. MethodSwitch component — full rules:
   - Import line (with `.jsx` extension — critical, blank page without it)
   - Structure: `<MethodSwitch>` → `<MethodSection id="..." label="...">` 
   - Tab IDs and labels table (portal, api, terraform, cli)
   - Order: portal always first
   - Heading rules: use `##` and `###` only, never `####` inside MethodSection
   - List before `</MethodSection>` — closing tag must NOT be indented
2. Frontmatter rules:
   - `title` — required
   - `sidebarTitle` — optional, shorter sidebar label
   - `ai-navigation` — required for tabbed articles, max 160 chars, starts with
     action verb, mentions all methods, no "you/your/this article"
   - `description` — DO NOT USE (Mintlify renders it as visible page text)
3. MDX parsing gotchas:
   - `{identifier}` inside backtick inline code → use `<code>` with `&nbsp;`
   - UTF-8 BOM at file start → breaks YAML frontmatter parser
   - `####` (h4) inside MethodSection → appears in wrong tab's TOC
4. Internal links:
   - Always root-relative: `/cloud/virtual-instances/create-an-instance`
   - Never old paths: `/cloud/api/...` directory no longer exists
   - Anchor links work as normal: `/cloud/virtual-instances/create-an-instance#step-1`
5. Validation command (local):
   ```
   node -e "const {compile}=require('@mdx-js/mdx'); ..."
   ```

**Source:** CONTRIBUTING.md in this repo (already written, needs distillation)

---

### File 4: `.agents/references/style-guide.md`

**Purpose:** Writing rules — voice, structure, formatting. Loaded by skills
that write or review content.

**Must contain:**

1. Voice and tone:
   - Gcore audience: technical, cloud infrastructure, developer-oriented
   - Direct, no marketing language, no filler phrases
   - Second person "you" is fine, but don't overuse
2. Sentence structure:
   - Steps use imperative: "Click Save", "Enter the value", "Run the command"
   - One action per step
   - Result statements after the action: "The instance appears in the list."
3. Headings:
   - `##` for main sections
   - `###` for sub-steps or sub-sections
   - Title case for `##`, sentence case for `###`
   - Never skip levels
4. Code blocks:
   - Always specify language identifier
   - Terminal commands: no `$` prefix
   - Placeholders: use `<angle-brackets>` not `{curly-braces}` in prose
5. `ai-navigation` field rules (critical, repeated from mdx-rules for emphasis):
   - One sentence, max 160 characters
   - Starts with action verb
   - Describes all methods in the article
6. Links:
   - Link text describes the destination, not "click here"
   - External links: full URL
   - Internal links: root-relative path

**Note:** We don't have a full written style guide yet. Build this from
patterns in existing articles + team knowledge. Start with what's known,
expand over time.

---

### File 5: `.agents/references/content-types.md`

**Purpose:** Defines the types of articles that exist, their structure, and
when to use each type. Loaded by write-from-scratch and feature-draft skills.

**Must contain:**

1. Tabbed article (most common in this repo):
   - When: feature accessible via both Portal and API
   - Structure: MethodSwitch with portal + api sections
   - Both sections use same `##` headings (parallel structure)
2. Single-method article:
   - When: Portal-only or API-only feature
   - No MethodSwitch needed
3. Overview article:
   - When: product or section landing page
   - Typically short, links to sub-articles
4. Concept article:
   - When: explaining what something is, not how to do it
   - No step-by-step, mostly prose
5. Cookbook article (special, built by cookbook skill):
   - When: end-to-end scenario spanning multiple products/sections
   - Structure: scenario → prerequisites → ordered steps pulling from
     multiple source articles → expected outcome

For each type: filename pattern, frontmatter fields, section structure.

---

### File 6: `.agents/references/mcp-tools.md`

**Purpose:** Documents available MCP tools and how to use them. Loaded only
by skills that need external data (jira-context, full-audit, feature-draft).

**Must contain:**

1. Jira MCP:
   - Use for: ticket context, acceptance criteria, linked tickets, comments
   - Key operations: get issue, search by JQL, get linked issues
   - What to extract: summary, description, acceptance criteria, labels,
     linked design docs or Confluence pages

2. Confluence MCP:
   - Use for: internal product specs, release notes, architecture docs
   - Key operations: get page by ID, search by keyword
   - What to look for: feature descriptions, API changes, known limitations

3. Playwright MCP:
   - Use for: testing UI steps described in an article
   - Entry point: https://portal.gcore.com
   - Standard testing protocol:
     a. Open the portal
     b. Navigate to the relevant section
     c. Execute each UI step from the article
     d. Verify the result matches what the article says
     e. Note discrepancies: wrong button names, missing fields, changed flows
     f. Take note of any steps the article skips
   - What counts as a passed step vs a failed step
   - How to report findings: structured list, not prose

---

### File 7: `.agents/skills/update-page/SKILL.md`

**Purpose:** Update an existing article. Simplest skill.

**Inputs:** article path + description of what to change

**Scope — read exactly these files:**
1. This SKILL.md
2. The article file specified by the user
3. `.agents/references/mdx-rules.md` — only if editing MethodSwitch structure
4. `.agents/references/style-guide.md` — only if rewriting significant prose

**Process:**
1. Read the article
2. Apply the requested change
3. Check: no new MDX parsing issues introduced
4. Check: `ai-navigation` still accurate after the change
5. Show diff to user before saving (or save and report what changed)

**Output:** Updated file. Short summary of what changed and why.

---

### File 8: `.agents/skills/jira-context/SKILL.md`

**Purpose:** Analyze a Jira ticket and produce a structured brief of what
needs to be documented.

**Inputs:** Jira ticket ID or URL

**Scope — read exactly these files:**
1. This SKILL.md
2. `.agents/references/mcp-tools.md` — Jira and Confluence sections
3. Jira ticket (via MCP) — fetched, not a local file
4. Linked Confluence pages (via MCP) — fetched if referenced in ticket
5. Existing article in repo — only if ticket references one

**Process:**
1. Fetch ticket from Jira MCP
2. Extract: what changed, what is new, affected product/feature
3. Search Confluence for related internal docs
4. Search repo for existing article about this feature
5. Produce structured output (see Output section)

**Output format:**
```
## Jira context: [TICKET-ID]

### What changed
[one paragraph]

### Affected documentation
- Existing article: [path or "none found"]
- Action needed: [update existing / create new / no doc needed]

### Scope of documentation work
[bullet list: what to add, what to remove, what to verify]

### Suggested next skill
- If updating existing: load skill update-page
- If creating new: load skill write-from-scratch
- If needs testing: load skill full-audit
```

---

### File 9: `.agents/skills/write-from-scratch/SKILL.md`

**Purpose:** Write a new article from a source (Jira, Confluence, or direct
description).

**Inputs:** topic + source (Jira ticket ID, Confluence URL, or free text
description) + article type (tabbed / single-method / overview / concept)

**Scope — read exactly these files:**
1. This SKILL.md
2. `.agents/references/content-types.md` — structure for the chosen type
3. `.agents/references/style-guide.md` — writing rules
4. `.agents/references/mdx-rules.md` — MDX and MethodSwitch rules
5. One existing article of the same type as a style reference
6. Source material (Jira/Confluence via MCP, or user input)

**Process:**
1. Determine article type
2. Read one reference article of the same type from the repo
3. Pull source material
4. Determine file path: `/{product}/{section}/{article-name}.mdx`
5. Write article following the type structure
6. Validate: frontmatter complete, ai-navigation present, no MDX issues
7. If tabbed article: both Portal and API sections must be present or explicitly
   marked as TODO

**Output:** New file at the determined path. Show full content before saving.

---

### File 10: `.agents/skills/api-use-case/SKILL.md`

**Purpose:** Add a REST API tab to an existing Customer Portal article using
the OpenAPI spec already in the repo.

**Inputs:** path to existing Portal article

**Scope — read exactly these files:**
1. This SKILL.md
2. The existing article file
3. The relevant OpenAPI YAML from `/api-reference/services_documented/`
   (determine which one from the product folder of the article)
4. `.agents/references/mdx-rules.md` — MethodSwitch rules

**Process:**
1. Read the existing article — understand all Portal steps
2. Identify the product (from file path)
3. Load the corresponding OpenAPI spec
4. For each Portal step, find the equivalent API endpoint:
   - Map UI action → API operation (e.g., "Click Create" → `POST /cloud/v1/instances`)
   - Extract required parameters, request body schema, example values
5. Write the REST API MethodSection:
   - Parallel structure to Portal section (same `##` headings)
   - Each step: explain what the call does + code block with curl example
   - Include: authentication header, required params, example response
6. Wrap existing Portal content in `<MethodSection id="portal">` if not already
7. Add `<MethodSection id="api">` after Portal section
8. Update `ai-navigation` to mention both methods

**Output:** Updated article with both tabs. Show full diff.

---

### File 11: `.agents/skills/full-audit/SKILL.md`

**Purpose:** Test every step of an existing article in real conditions using
the portal (Playwright) or API, find discrepancies, update the article.

**Inputs:** path to article to audit

**Scope — read exactly these files:**
1. This SKILL.md
2. The article to audit
3. `.agents/references/mcp-tools.md` — Playwright protocol section
4. `.agents/references/mdx-rules.md` — only if making structural edits

**Process:**

Phase 1 — Parse the article:
- Extract all numbered steps and UI element names
- Identify which steps are Portal steps vs API steps
- Build a test checklist

Phase 2 — Execute tests:
For each Portal step:
  1. Use Playwright to navigate to the relevant portal section
  2. Execute the step exactly as written
  3. Record: PASS (matches article) / FAIL (discrepancy found)
  4. For FAIL: note exact discrepancy (wrong label, missing button, changed
     flow, prerequisite not mentioned in article)

For each API step:
  1. Execute the curl/API call from the article
  2. Check response against expected outcome in article
  3. Record: PASS / FAIL + details

Phase 3 — Produce findings report:
```
## Audit findings: [article path]

### Tested: [date]
### Steps tested: [N]
### Steps passed: [N]
### Steps failed: [N]

### Discrepancies
1. [Step N] FAIL — Article says "X", portal shows "Y"
2. [Step N] FAIL — Step skips prerequisite: user must first do Z
...

### Missing content
- [anything the article should mention but doesn't]

### Outdated content
- [anything that is no longer true]
```

Phase 4 — Apply fixes (after user confirms findings):
- Update article with confirmed fixes
- Preserve voice and structure
- Update `ai-navigation` if scope changed

**Output:** Findings report first. Apply fixes only after user review.

---

### File 12: `.agents/skills/feature-draft/SKILL.md`

**Purpose:** For product teams (non-writers). Takes a feature description
and produces a documentation draft ready for writer review.

**Inputs:** one or more of:
- Jira ticket ID
- Confluence page URL
- Free-text description of the feature

**Scope — read exactly these files:**
1. This SKILL.md
2. `.agents/references/mcp-tools.md` — all three MCP sections
3. `.agents/references/content-types.md`
4. `.agents/references/style-guide.md`
5. `.agents/references/mdx-rules.md`
6. Source material via MCP (Jira, Confluence)
7. Existing article if updating, or one reference article if creating new

**Process:**

Phase 1 — Research:
- Fetch Jira ticket (if provided): summary, description, acceptance criteria
- Fetch Confluence pages (if linked): internal spec, release notes
- Determine: is this a new feature (new article) or change to existing feature
  (update existing article)?

Phase 2 — Locate or create article:
- If updating: find existing article path
- If creating: determine correct product folder and article name

Phase 3 — Test (if Playwright available and feature is UI-accessible):
- Open portal, navigate to the new/changed feature
- Execute the main user flow
- Document steps from direct observation (not from spec alone)

Phase 4 — Write draft:
- Follow content-types.md for structure
- Follow style-guide.md for voice
- Mark uncertain sections with `{TODO: verify}` inline
- For tabbed articles: write Portal section from Playwright observation,
  mark API section as `{TODO: API section needed}`

Phase 5 — Style check:
- Verify frontmatter fields
- Verify `ai-navigation` present and valid
- Check for MDX issues
- Check internal links are root-relative

Phase 6 — Create PR draft:
- Commit to a new branch: `feature-draft/{ticket-id}` or `feature-draft/{slug}`
- PR title: `[Product] Draft: [feature name]`
- PR body: brief summary + link to Jira ticket + `{TODO}` items listed

**Output:** PR URL. The writer reviews and refines from there.

---

### File 13: `.agents/skills/cookbook/SKILL.md`

**Purpose:** Compile a cookbook article — an end-to-end scenario guide that
pulls steps from multiple existing articles.

**Inputs:** scenario topic (e.g. "Set up CDN for video streaming with DDoS
protection")

**Scope — read exactly these files:**
1. This SKILL.md
2. `.agents/references/content-types.md` — cookbook structure
3. `.agents/references/style-guide.md`
4. `.agents/references/mdx-rules.md`
5. Source articles found during step 2 of the process (search, then read)

**Process:**

Phase 1 — Understand the scenario:
- Parse the topic into: who is the user, what do they want to achieve,
  what Gcore products are involved

Phase 2 — Find source articles:
- Search repo for articles related to each product in the scenario
- Read only the articles that contain relevant steps (not all articles)
- Build a map: scenario step → source article → section

Phase 3 — Design the structure:
- Determine the end-to-end sequence of steps
- Identify prerequisites (what the user must have set up already)
- Identify the expected final outcome

Phase 4 — Write the cookbook article:
Structure:
  ```
  ---
  title: [Scenario title]
  ai-navigation: [one sentence, all products mentioned]
  ---

  ## Overview
  [What this guide achieves, who it's for]

  ## Prerequisites
  [What must be in place before starting]

  ## Step 1. [First major action]
  [Steps + link to full article for details]

  ## Step 2. [Second major action]
  ...

  ## Expected outcome
  [What the user should see when done]
  ```

- Each step: brief instructions + reference link to the source article
  for full details. Don't copy entire articles — link to them.
- Use cross-product links, not inline repetition.

**Output:** New file at `/cookbook/{scenario-slug}.mdx` or in the most
relevant product folder. Show full content before saving.

---

## Key decisions made in the planning session

1. **Two audiences, separate files:** CONTRIBUTING.md for humans (untouched
   for now), AGENTS.md for AI agents.

2. **AGENTS.md is a dispatch table**, not a manual. Critical rules inline,
   everything else in skills and references.

3. **Skills use explicit scope sections:** each SKILL.md starts with "read
   exactly these files." This prevents the agent from reading all 1000 files
   to "understand context."

4. **References are pull, not push:** AGENTS.md does not tell the agent to
   read references. Skills tell the agent to read specific references only
   when the task requires it.

5. **full-audit uses Playwright MCP** for real portal testing — not visual
   inspection but actual step execution. Output is a structured findings report
   before any edits are made.

6. **api-use-case uses the OpenAPI YAML** already in the repo
   (`/api-reference/services_documented/`) rather than guessing API behavior.

7. **feature-draft creates a draft PR**, not a final article. The writer
   reviews and refines. Uncertain sections are marked `{TODO: verify}`.

8. **cookbook articles link to source articles**, not copy them. They are
   navigation guides for end-to-end scenarios.

---

## Improvement backlog — findings from Cloudflare comparison

Compared our system against `C:\Projects\cloudflare-docs\.agents\` on 2026-06-06.
Items below are genuine gaps — things not found in docops-agent2 source files either.

### HIGH priority

**1. `AGENTS.md` — add "Common mistakes" section** DONE
10 Gcore-specific mistakes added: MethodSwitch .jsx, description frontmatter,
{identifier} in inline code, </MethodSection> indent, <p> wrap in MethodSection,
#### heading leak, ai-navigation forbidden chars, image without extension,
git add ., branching from stale main.

**2. `style-guide.md` — missing specific rules:** DONE
- Numbers formatting: added (spell out 0–9, digits for 10+, space before unit)
- Voice rules: added (We/1st person for Gcore, but not every sentence; contractions OK except you're/I'm)
- Contractions: explicitly allowed (it's, don't, can't, won't)
- Heading: no infinitives, Step N. format: added
- Product capitalization (Title Case): added
- "(Optional)", "log in to", location/purpose before action: moved to procedures.md
- Sentence length, "select vs click", placeholder format: not added — Cloudflare-specific, not Gcore convention

**3. Adversarial review pattern** — NOT APPLICABLE
Cloudflare uses this because they cannot run real tests. We already have something
stronger: api-use-case has real API testing (Phase 2), full-audit has real Playwright
testing. Real test results are stronger than any logical review by a second agent.
The {TODO: verify} markers in write-from-scratch cover the case where testing
is impossible (feature not yet live).

### MEDIUM priority

**4. Separate `skills/pr/SKILL.md`** DONE
Standalone PR skill created. Product bracket inferred from file path via table.
Skills write-from-scratch, api-use-case, update-page, full-audit now reference it.
feature-draft already had its own PR logic (kept as-is, more detailed for contributors).

**5. ELI5 / simplification skill** — NOT APPLICABLE
Gcore's approach is to write accessibly from the start (medium-technical audience,
value before mechanics, define terms on first use). Simplification is built into
the style guide, not a post-processing step. A separate skill would duplicate this.

### LOW priority (already mostly covered, minor gaps)

**6. Reserved example values**
No list of safe placeholder values for IPs and domains. Add to style-guide.md:
`192.0.2.0/24`, `example.com` (RFC 5737 — don't resolve to live origins).

**7. Inclusive language rules**
Not in docops-agent2 source files. allowlist/blocklist, gender-neutral pronouns.
Low priority for technical cloud docs aimed at developers.

### What was NOT missing (clarifications)

- **procedures.md**: Cloudflare separates step-writing rules into a dedicated file, but we
  already have most of these rules in `style-guide.md`. Not a separate file needed.
  The specific rules that ARE missing (Optional prefix, log in to, location/purpose before
  action) are captured in item #2 above.
- **Oxford comma**: Confirmed NOT in docops-agent2 source files. Cloudflare-specific.
- **Many of the "missing" rules**: Were actually in docops-agent2 style-guide.md and
  transferred to our style-guide.md correctly. The 2-sentence max, causal connectors,
  forbidden words, cognitive load rules — all present.

---

## How to resume after a session restart

Tell Claude:

> "Read .agents/PLAN.md and continue from where we left off."

That's it. No need to re-explain the architecture.
