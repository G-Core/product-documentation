# Review Process

Six-step process for reviewing any documentation article.
Load this file when a skill tells you to run the review process.

Follow steps sequentially. Do not batch-read all steps upfront.
Complete and fix each step fully before moving to the next.

---

## Step 1 — Structure

Run grep checks, fix all matches, then do manual scan.

```powershell
# Forbidden heading openers
grep -n "^## What \|^## How \|^## Why \|^## When " article.mdx

# Forbidden sections
grep -n "^## Next steps\|^## Prerequisites\|^## Requirements\|^## Related documentation\|^## See also\|^## What" article.mdx

# Meta-preamble openers
grep -n "^This guide covers\|^This article\|^In this \|^This tutorial\|^This guide walks\|^This guide shows" article.mdx
```

**Manual checks:**
- Every `##` and `###` heading is followed by a prose sentence before any code/table/list
- No two consecutive headings without text between them
- Opening paragraph does not describe the document — it states what the reader achieves
- No separate `## Prerequisites` section — requirements are in the opening paragraph

---

## Step 2 — Formatting

```powershell
# Bold used outside UI elements (verify each match)
grep -n "\*\*[^*]+\*\*" article.mdx

# Unspaced em-dashes
grep -n "[^ ]—\|—[^ ]" article.mdx
```

**Manual checks:**
- Each bold match: is it a UI button, field name, or section name? If not — remove bold
- After any table or code block introducing 3+ new terms: verify an orienting sentence follows
- All tab groups (`<Tabs>`) have the same set of tabs throughout the article
- Screenshots appear AFTER the step text, not before or in the middle

---

## Step 3 — Links

```powershell
# Link text longer than ~2 words (15+ characters between brackets)
grep -n "\[[^\]]\{15,\}\](" article.mdx

# Standalone link sentences (banned patterns)
grep -n "For more details\|^See \[\|Learn more in\|Refer to \[\|For more information" article.mdx

# All URLs — list for duplicate check
grep -n "](https\?://" article.mdx
```

**Manual checks:**
- For each URL appearing more than once: all occurrences after the first must be plain text
- No sentence whose only purpose is to contain a link

---

## Step 4 — Voice

```powershell
# Forbidden words
grep -in "\bjust\b\|\bsimply\b\|\bobviously\b\|\bclearly\b\|\bensure\b\|\bbe sure\b\|\bmake sure\b\|\betc\b\|\bplatform\b\|\bsuch as\b" article.mdx

# "you" and "your" in prose
grep -in "\byou\b\|\byour\b" article.mdx
```

**Manual checks:**
- Fix all "you/your" in authored prose — skip code blocks and terminal output verbatim
- Fix all "you/your" inside `<Info>`, `<Note>`, `<Warning>`, `<Tip>` blocks as well
- Read adjacent sentence pairs — join cause-effect or contrast pairs with a connector
- Verify consistent voice throughout (tutorial or reference — not mixed)

---

## Step 5 — Content accuracy

```powershell
# Find all internal links
grep -n "\](/[^)]+)" article.mdx

# Find all image references
grep -n "src=\"\|!\[" article.mdx
```

**Verify each internal link:**
1. Extract the path from the link
2. Check if file exists at `{repo_root}/{path}.mdx` or `{repo_root}/{path}/index.mdx`
3. If not found → flag as broken

**Verify each image:**
1. Extract the path from src or `![]()` syntax
2. Check file exists at `C:\Projects\product-documentation\{path}`
3. If not found → flag as broken
4. Do not change an image path without confirming the file exists at the new path

**Content checks:**
- Technical information matches the OpenAPI spec or live portal
- Code examples are syntactically correct

**Duplication check (mandatory — run before moving to Step 6):**

Read the intro paragraph(s) of each section against every named subsection within it.
Flag any sentence that:
- Restates a fact already covered by a subsection heading + its body
- Repeats the same constraint or note as a `<Note>`, `<Warning>`, or `<Info>` block elsewhere
- Appears verbatim or near-verbatim in two places in the same article or the same tab

Common patterns to catch:
- Intro says "X must have Y installed" → subsection "Y" says the same — remove from intro
- Closing sentence of section A says "see section B" → opening sentence of section B restates it — remove one
- Two adjacent paragraphs open with "Images must be in one of the supported formats" — merge

Fix: remove the weaker or less detailed occurrence. Never duplicate — pick the canonical location and keep it there only.

---

## Step 6 — Final read

Read the full article once as a medium-technical reader encountering it for the first time.

Fix anything that:
- Causes a pause or requires re-reading
- Sounds mechanical or machine-generated
- Contains a sentence that could appear in three different articles (too generic)
- Has a section that exists only to host a link

**Anti-patterns caught in review:**
- Opening sentence is a template ("The Gcore API provides programmatic access...")
- Section heading followed by one thin sentence — either expand or merge
- Closing sentence points to the next article ("With these basics in place, the next step is...")
- JSON block directly after `</Tabs>` without a label
- Numbered list that is not truly sequential (use bullets instead)

---

## Report format

After completing all six steps:

```
Review complete: [article path]

Issues fixed:
- [N] structure issues
- [N] formatting issues
- [N] link issues
- [N] voice issues
- [N] content accuracy issues

Remaining (needs human decision):
- [issue] at [location] — [why it needs human decision]

Status: ready / needs human review
```
