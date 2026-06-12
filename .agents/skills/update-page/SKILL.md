---
name: update-page
description: Update existing documentation when product, feature, or portal UI changes are provided. Use when the user describes changes and wants affected articles updated.
---

Update existing articles based on provided context about product or UI changes.

## Scope — read exactly these files

1. This SKILL.md
2. The article file(s) identified during Phase 1
3. `.agents/references/style-guide.md` — when rewriting prose or restructuring
4. `.agents/references/mdx-rules.md` — when editing MethodSwitch structure or frontmatter
5. `.agents/references/mcp-tools/playwright.md` — only if user agrees to Playwright testing

Do not read other articles for context unless they are directly linked from the
article being updated.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Description of what changed | Yes | Product change, UI rename, new option, changed flow |
| Article path | No | If not provided, agent searches for it |
| Screenshots | No | If provided, use them directly — no Playwright needed |
| Jira ticket / Confluence link | No | Additional context if available |

---

## Phase 1 — Find affected articles

If the article path is given — skip to Phase 2.

If not, search the repository:

```powershell
# Search by product or feature name
grep -r "keyword" --include="*.mdx" -l

# Search by UI element name that changed
grep -r "old button name" --include="*.mdx" -l
```

Read the first sentence of each match to confirm it is relevant before proceeding.
Multiple articles may be affected — process each one separately.

**Do not update articles you are not sure are affected.** If unsure, list them
and ask the user which ones to update.

---

## Phase 2 — Understand the article

Before making any change, read the full article:

- What is the article's goal? What task does it walk the reader through?
- How is it structured? (Tabbed / portal-only / API-only)
- Where exactly do the provided changes fit?
- What surrounding content might need adjustment for the change to read naturally?

Do not start editing until you can answer these questions.

---

## Phase 3 — Playwright decision

**If screenshots were provided** → skip this phase, use the provided screenshots.

**If the changes involve UI elements** (button names, navigation paths, form fields,
new UI screens) **and no screenshots were provided** → ask the user:

> The changes you described affect the portal UI.
> Should I open the portal and capture updated screenshots?
>
> - **Yes** — I will navigate to the relevant section, verify the current UI,
>   and take new screenshots.
> - **No** — I will update the text only. You can add screenshots separately.

Wait for the answer before proceeding.

- If **yes** → follow the protocol in `.agents/references/mcp-tools/playwright.md`
- If **no** → continue to Phase 4 with text-only changes

**If the changes are text-only** (new limits, new field descriptions, changed behavior,
new API parameters) → skip this phase entirely.

---

## Phase 4 — Apply changes

### What to change

Apply only what was described in the input. Do not fix unrelated issues you notice
along the way — note them separately at the end.

For each change:

1. Find the exact location in the article
2. Read the surrounding paragraph or section — understand the tone and structure
3. Write the change so it fits naturally into that context

### How to make changes organically

Mechanical replacement ("find X, replace with Y") is rarely enough. The goal is
that the reader cannot tell which sentences were changed.

**If renaming a UI element:**
- Replace in all occurrences throughout the article
- Check if any surrounding sentences now read awkwardly — rewrite if needed
- Check alt text on screenshots that show the renamed element

**If adding a new option or field:**
- Find where similar options are described
- Add the new one in the same style and structure
- If it changes the step count — renumber steps

**If a flow changed (steps reordered, step added, step removed):**
- Rewrite the affected section — do not patch individual sentences
- Ensure the intro sentence for the section still matches what follows
- Check if `ai-navigation` frontmatter still accurately describes the article

**If restructuring a section:**
- Read the full section before and after in your head — does it flow?
- Verify headings are still in logical order
- Check all internal anchor links — renaming a heading breaks them

### Do not touch

- `<MethodSection id="api">` — API sections are maintained separately
- Article filename and slug — broken URLs are worse than outdated content
- `docs.json` navigation — only if a new top-level section is added, and only
  after confirming with the user

---

## Phase 5 — Validate

After making changes, check:

**MDX:**
- [ ] No unescaped `{identifier}` in inline code spans (use `<code>` with `&nbsp;`)
- [ ] If MethodSwitch was touched: closing tags at column 0 after lists
- [ ] If MethodSwitch was touched: prose inside `<MethodSection>` wrapped in `<p>` tags
- [ ] No `####` headings inside `<MethodSection>`

**Frontmatter:**
- [ ] `ai-navigation` still accurately describes the article after changes
  (update it if the article's scope changed)
- [ ] No `description` field present

**Style:**
- [ ] New prose follows sentence case headings
- [ ] No forbidden sections added (`## Next steps`, `## Prerequisites`, etc.)
- [ ] Bold used only for UI element names
- [ ] No forbidden words: just, simply, ensure, platform, obviously

**Links:**
- [ ] Any renamed heading has no broken anchor links pointing to it
- [ ] Internal links still root-relative

---

## Output

After completing all phases, report:

```
Article: [path]

Changes made:
- [description of change 1]
- [description of change 2]

Screenshots: [replaced N / text-only update / N new screenshots added]

Unrelated issues noticed (not changed):
- [issue] at [location] — recommend fixing separately
```

If multiple articles were updated — one report block per article.

When the user confirms the result looks good — load `.agents/skills/pr/SKILL.md`
to create the branch, commit, and open a draft PR.
