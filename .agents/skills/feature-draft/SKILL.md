---
name: feature-draft
description: Draft documentation for new Gcore product features or product changes, research context, update or create the right article, and open a draft PR. Use when product teams provide feature context and want a documentation draft.
---

Take context from a contributor about a new feature or product change, research
it, find the right place in the documentation, write a draft, and open a draft PR
for a technical writer to review.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/mcp-tools/setup.md` — verify required MCPs are available
3. `.agents/references/mcp-tools/jira.md` — if a Jira ticket is provided
4. `.agents/references/mcp-tools/confluence.md` — if Confluence links are present
5. `.agents/references/mcp-tools/playwright.md` — only if user agrees to portal testing
6. `.agents/references/content-types.md` — to determine article type and structure
7. `.agents/references/style-guide.md` — writing rules for the draft
8. `.agents/references/procedures.md` — step format and ordering rules
9. `.agents/references/mdx-rules.md` — MDX and frontmatter rules
9. One existing article of the same type as a style reference

---

## Inputs

Accepts any combination of:

| Input | Notes |
|-------|-------|
| Jira ticket ID or URL | Best source — has acceptance criteria and linked dev ticket |
| Confluence page URL | Internal spec, release notes, architecture doc |
| Free-text description | What the feature does, what changed, who it affects |
| Screenshots or attachments | UI screenshots of the new feature |

At least one input is required. If none is provided — ask the contributor
to describe what changed and who it affects.

---

## Phase 1 — Gather context

Collect everything available before writing anything.

**From Jira** (if ticket provided):
- Fetch the main ticket: summary, description, status, labels
- Fetch the linked dev ticket: acceptance criteria, stakeholders, Confluence links
- Read all comments — important clarifications often appear there
- Check ticket status — if Done or Cancelled, ask the contributor if this is already live

**From Confluence** (if URL provided or linked from Jira):
- Fetch the page: feature description, API changes, known limitations
- Never copy Confluence text verbatim — use it to understand the feature

**From free-text description:**
- Note what is clearly stated vs what needs verification
- Ask one clarifying question if critical information is missing
  (e.g. "Is this change visible in the Customer Portal, the API, or both?")

**Build a mental model:**
- What does the feature do?
- Who uses it and when?
- What changed compared to before?
- Is it visible in the Customer Portal, the API, or both?
- Is it already live or still upcoming?

If the feature is not yet live — note this clearly and mark the draft as
`{TODO: verify in portal before publishing}`.

---

## Phase 2 — Quick documentability check

Before searching for an article, verify this is worth documenting:

**Skip documentation if:**
- The change is purely internal (admin API, internal tool, backend refactoring)
- The change is a product bug fix with no customer-visible behavior change
- The change affects only internal Gcore teams (check stakeholders in dev ticket)
- The Jira ticket is already Done and the docs were updated at the time

**Proceed if:**
- The feature is visible to customers in the portal or public API
- The change affects what customers can do, configure, or plan for
- The contributor is confident this needs documenting

If unsure — ask: "Does a customer need to know about this to use the product
correctly, or to plan their setup?" If yes → document.

---

## Phase 3 — Find or determine the article

Search the repository for an existing article about this feature:

```powershell
grep -r "feature or product name" --include="*.mdx" -l
```

Read the first few lines of any matches to confirm they are relevant.

**If an existing article is found:**
- This is an UPDATE — the draft will modify the existing article
- Note which sections are affected by the change
- Confirm with content-types.md that the article type still matches

**If no article is found:**
- This is a NEW article
- Determine the correct product folder and file path:
  ```
  /{product}/{section}/{article-name}.mdx
  ```
- Determine the article type using `.agents/references/content-types.md`

---

## Phase 4 — Portal testing (ask the contributor)

If the feature is accessible in the portal — ask:

> I can open the Gcore Customer Portal and navigate through the new feature
> to document the exact steps and capture screenshots.
>
> - **Yes, test in the portal** — more accurate, I will document what I actually see
> - **No, write from the description** — faster, I will mark steps that need
>   verification as TODO

Wait for the answer.

**If yes:**
- Follow the Playwright protocol in `.agents/references/mcp-tools/playwright.md`
- Navigate to the feature in the portal
- Document the UI flow from direct observation — not from the description alone
- Capture screenshots following the standards in `.agents/references/mcp-tools/playwright.md`

**If no:**
- Write from the provided context
- Mark every UI step that could not be verified:
  `{TODO: verify in portal — confirm button name and navigation path}`

---

## Phase 5 — Write the draft

### Before writing

Read one existing article of the same type from the same product folder.
Use it as a style reference — depth of explanation, step format, tone.

### Article structure

Use the template from `.agents/references/content-types.md` for the determined type.

For most how-to articles:
- Portal section: numbered steps, bold UI element names, screenshots
- API section: mark as `{TODO: API section — add if REST API coverage is needed}`
  unless the contributor specifically provided API details

### Writing rules

Follow `.agents/references/style-guide.md`. Key rules for contributors:

- **Opening sentence:** state what the reader will accomplish — not "This guide covers..."
- **Steps:** use imperative ("Click **Save**") — not "You should click Save"
- **Bold:** only for UI element names and button labels — not for emphasis
- **No forbidden sections:** no `## Prerequisites`, `## Next steps`, `## See also`
- **One sentence per paragraph action** — result on the next line if needed

### Marking uncertainty

Use `{TODO:}` for anything that could not be verified:

```
{TODO: verify navigation path — confirm exact menu location}
{TODO: screenshot needed — capture the creation form}
{TODO: verify field name — spec says "retention_period", confirm in UI}
{TODO: API section — add REST API coverage if needed}
```

Collect all TODOs — they become the PR description checklist.

### Frontmatter

```yaml
---
title: [Full descriptive title]
sidebarTitle: [Short sidebar label]
ai-navigation: [One sentence, action verb, max 160 chars, no {braces} or /slashes/]
---
```

Write `ai-navigation` last. Rules: one sentence, starts with action verb,
describes all methods covered, no curly braces, no URL paths, no colons followed by space.

---

## Phase 6 — Verify agent-added claims

Find everything in the draft that you wrote from your own reasoning — not from
what the contributor provided or what is in Jira/Confluence.

**The rule:** if the contributor gave you the spec directly — trust it. If Jira
or Confluence has the value — trust it. Verification targets only what you added
yourself through inference or "logical deduction".

**Signs of agent-added content:**
- A number or limit you assumed: "typically 30 seconds", "standard limit is 100"
- A behavioral claim you deduced from general knowledge: "since it's cloud-based,
  it automatically scales"
- A step you added because "it seemed necessary"
- Anything you wrote that the contributor did not explicitly tell you

**What does NOT need verification:**
- Specs and values the contributor provided directly in their input
- Values found in the Jira ticket, parent ticket, or Confluence
- Details confirmed through Playwright testing in Phase 4

**For each agent-added claim, check in order:**

1. **Main Jira ticket** — stated in description or acceptance criteria?
2. **Parent ticket** — epic or parent story (fetch if not yet loaded)
3. **Sibling tickets** — other issues under the same parent
4. **Confluence pages** — linked from tickets or searchable by feature name

Use `.agents/references/mcp-tools/jira.md` and `.agents/references/mcp-tools/confluence.md`.

**Decision:**

| Situation | Action |
|-----------|--------|
| Came from contributor or source material | Keep — no verification needed |
| Confirmed in Jira or Confluence | Keep |
| Your own reasoning, not in any source | `{TODO: verify — added by agent, not in source}` |

**Self-check:** for every technical claim, ask "Where did I get this?"
If the answer is "it seemed logical" — mark it.

---

## Phase 7 — Style check

Quick validation before creating the PR:

**MDX:**
- [ ] Import has `.jsx` extension if MethodSwitch is used
- [ ] No `{identifier}` in inline backtick spans
- [ ] Prose inside `<MethodSection>` wrapped in `<p>` tags

**Frontmatter:**
- [ ] `title` and `ai-navigation` present
- [ ] No `description` field

**Style:**
- [ ] No forbidden openers: "This guide...", "This article..."
- [ ] No forbidden sections: `## Prerequisites`, `## Next steps`
- [ ] Headings in sentence case
- [ ] No "you" or "your" in prose
- [ ] No forbidden words: just, simply, ensure, platform

---

## Phase 8 — Create draft PR

### Git

```powershell
cd C:\Projects\product-documentation
git checkout main
git pull origin main
git checkout -b feature-draft/{ticket-id-or-slug}
```

Stage only the files you created or modified:
```powershell
git add {article-path}
git add {screenshot-paths}
git commit -m "[{Product}] Draft: {feature name}"
git push -u origin feature-draft/{ticket-id-or-slug}
```

### PR

Create as a **draft PR** — it is not ready for review until a technical writer
has verified the content.

**Title format:** `[Product] Draft: {feature name}`
Examples:
- `[Cloud] Draft: GPU cluster auto-scaling`
- `[CDN] Draft: Origin shield configuration`

**PR body:**
```markdown
## What this documents

{1-2 sentences: what feature or change this documents, and the source (Jira ticket link if available)}

## Contributor notes

{Any context the writer should know — what was tested, what was assumed, known gaps}

## TODO before publishing

{List of all {TODO:} items from the draft}
- [ ] {TODO item 1}
- [ ] {TODO item 2}
- [ ] Verify portal steps with Playwright (if not already done)
- [ ] Add API section if REST API coverage is needed
- [ ] Technical writer review and approval
```

---

## Output

```
Draft created: [article path]
Action: [new article / updated existing article]
Portal tested: [yes / no — N steps marked TODO]

PR: [URL]
Branch: feature-draft/{name}

TODO items for the writer:
- [list from draft]

Next step: assign the PR to a technical writer for review
```


---

## Terminology rule

Never use the word `permanent` when referring to API tokens. The expiration is user-controlled.
Always write: `An [API token](/account-settings/api-tokens) is required.`
