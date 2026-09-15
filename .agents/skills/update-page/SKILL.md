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
5. `.agents/references/sdk-best-practices.md` — SDK usage patterns (use `*_and_poll()`, no manual polling)
6. `.agents/references/mcp-tools/playwright.md` — only if user agrees to Playwright testing

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

## Phase 0 — Relevance gate

**Run this before touching any file.** Decide whether an MDX update is actually warranted.

### The two conditions that justify an update

Update documentation only when **at least one** of these is true:

1. **Existing MDX content is factually wrong** — a UI label was renamed, a command no longer works, a field was removed, a limit changed, a step was reordered, a response example shows a value that is no longer returned.
2. **A customer following the article would fail or be blocked** — a new mandatory field was added, authentication changed, a required step is missing, a new required configuration must be set before the feature works.

### Signals that do NOT justify an update

Stop and cancel if the change is only one of the following:

- **New optional/diagnostic field or header** that we do not currently document — goes in the API Reference, not our narrative MDX. We do not mirror every response header or parameter from OpenAPI specs.
- **Backend or API-spec fix** where the dev ticket is Done and the fix was applied by backend developers to YAML/code, not to our MDX — the work is already complete without us.
- **Informational addition** (new metric, new response header, new log field) that customers can discover in the API Reference or portal UI — we do not duplicate the API Reference.
- **Internal-only change** — admin API, internal billing, backend refactoring, library update.
- **We never documented this thing** and it is not blocking any task described in our articles — silence is fine; adding it would be noise.

### Decision checklist

Go through these in order. Stop at the first YES or NO that resolves the question.

| Question | YES → | NO → |
|----------|-------|------|
| Does the change make existing MDX text **factually wrong**? | Proceed | Next |
| Is this a **UI change** (renamed button, new portal field, changed navigation path)? | Proceed | Next |
| Would a customer following our article **fail to complete the task** without this info? | Proceed | Next |
| Do we **already document** this specific element (field, header, option) and it changed? | Proceed | Next |
| Was the fix applied by a **backend developer** to YAML/code, and is the dev ticket Done? | Cancel | Next |
| Would this update **duplicate content already in API Reference or portal UI**? | Cancel | Next |
| Is the new information **optional, diagnostic, or monitoring-only**? | Cancel | Proceed |

### If the answer is Cancel

Report exactly this and stop:

```
Change: [description]
Decision: CANCEL — no MDX update needed
Reason: [one sentence from the checklist above]
```

Do not search for articles. Do not open any files. Do not propose alternative updates.

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

When adding or replacing screenshots, always use the single-line Frame format:

```mdx
<Frame>![Alt text](/images/docs/{product}/{section}/{article-slug}/{filename}.png)</Frame>
```

Never use `<img>` tags with JSX `style={{...}}` inside `<Frame>`. Never multi-line Frame with indented image content.

**If the changes are text-only** (new limits, new field descriptions, changed behavior,
new API parameters) → skip this phase entirely.

---

## Phase 3b — Verify behavioral claims via live API test

**If the change describes a behavioral restriction or capability** (e.g. "feature X is not
supported", "operation Y is blocked", "field Z is required") — verify it with a live API
test before writing it into the article. Do not trust Jira ticket descriptions alone.

**Steps:**

1. Identify the resource type involved (volume, instance, load balancer, etc.)
2. If no such resource exists in the account — **create one**. Use the smallest/cheapest
   configuration. Delete it after the test.
3. Attempt the operation described in the change (resize, attach, delete, etc.)
4. Record the actual API response — success, error code, error message.
5. Base the documentation on the observed behavior, not on the ticket description.

**If creation is not possible** (no quota, region unavailable, feature gated):
- State the blocker explicitly and ask the user how to proceed.
- Do not write documentation based on an untested claim.

**Never write a restriction or limitation into documentation without a live test.**
Jira tickets describe intent and bugs — not necessarily the current production behavior.

---

## Phase 4 — Apply changes

### What to change

Apply only what was described in the input. Do not fix unrelated issues you notice
along the way — note them separately at the end.

**If updating SDK code examples:**
Read `.agents/references/sdk-best-practices.md` BEFORE making changes.
- Replace manual polling with `*_and_poll()` / `*AndPoll()` methods
- Remove `import time` when using `*_and_poll()`
- Remove `os.environ["GCORE_API_KEY"]` - SDK reads it automatically

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

### Structural elements — text only, never remove tags

Inside `<MethodSection>`, `<Info>`, `<Warning>`, and `<p>` tags between numbered list
items are structural separators for the MDX parser. Removing one — even if its text
is outdated — can blank the entire page with no build error.

**If the content inside a structural element must be removed:**
- Replace the text with neutral, accurate content
- Never delete the tag itself
- Never convert a separate `<p>Click ...` into inline text appended to the step header

This rule applies even when the element contains information you want to fully remove
(e.g. a deprecated restriction, an old warning). Keep the tag; change what it says.

### Do not touch without explicit instruction

- `<MethodSection id="api">` — API tab content is updated only when the user explicitly asks to update the API section or when a curl example, endpoint, or parameter in that section is factually wrong. Do not add new API parameters or response fields just because they appeared in an OpenAPI spec update.
- Article filename and slug — broken URLs are worse than outdated content.
- `docs.json` navigation — only if a new top-level section is added, and only after confirming with the user.

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


---

## Terminology rule

Never use the word `permanent` when referring to API tokens. The expiration is user-controlled.
Always write: `An [API token](/account-settings/api-tokens) is required.`
