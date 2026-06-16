---
name: create-page
description: Write a new documentation article from scratch. Use when creating a new MDX file that does not yet exist in the repository.
---

# Create a new documentation article

## Step 1. Read before writing

Read these files before writing a single word:

1. `.agents/references/style-guide.md`
2. `.agents/references/mdx-rules.md`
3. If the article covers portal UI: `.agents/references/mcp-tools/playwright.md`

Do not skip. Do not rely on memory.

## Step 2. Decide structure

Answer these questions before writing:

- What is the single task this article helps the reader accomplish?
- Does it need MethodSwitch (Portal + API)? If the action is doable via both — yes.
- Are there existing articles with the same structure to follow as a pattern?

## Step 3. Write the article

### Opening paragraph — execute this checklist

- [ ] Does NOT start with "This guide...", "This article...", "In this document..."
- [ ] Does NOT contain the word "you" or "your"
- [ ] Prerequisites are in this paragraph as plain text — NOT in a `## Prerequisites` section
- [ ] Two paragraphs max: (1) what this is and why, (2) what is required

### Every paragraph — execute this checklist

- [ ] Develops ONE idea — not a list of isolated facts
- [ ] Does NOT start with the pattern `[Subject] is/are/links/shows`
- [ ] No sentence exists ONLY to host a link — every link is embedded in a content sentence
- [ ] No "see [X] for more", "for details see [X]", "refer to [X]" patterns

### Every link — execute this checklist

- [ ] Link text is 1–2 words maximum — never a full clause
- [ ] If this destination was already linked earlier in the article — this is plain text, not a link

### Every heading — execute this checklist

- [ ] Sentence case (not Title Case)
- [ ] Does NOT start with What, How, Why, When
- [ ] Is NOT: `## Prerequisites`, `## Requirements`, `## Next steps`, `## Get started`, `## See also`, `## Related documentation`
- [ ] Followed by at least one prose sentence before any code block, list, or table

### Forbidden words — scan before finishing

- [ ] No: just, simply, ensure, be sure, make sure, platform, obviously, clearly, seamlessly, robust, scalable, etc., and so on, leverage, utilize

## Step 4. Validate MDX

```powershell
node -e "
const {compile}=require('@mdx-js/mdx');
const fs=require('fs');
const c=fs.readFileSync('PATH_TO_FILE','utf8');
compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));
"
```

Fix any errors before proceeding.

## Step 5. Check frontmatter

- [ ] `title` present
- [ ] `sidebarTitle` present (if different from title)
- [ ] `ai-navigation` present — one sentence, starts with action verb, no colons or special chars
- [ ] No `description` field

## Step 6. Update docs.json

Add the new article to the correct group in `docs.json`. Validate JSON is still valid:

```powershell
node -e "JSON.parse(require('fs').readFileSync('docs.json','utf8')); console.log('OK')"
```

## Step 7. Article readiness checklist

Before telling the user the article is ready, confirm all four:

- [ ] **Content** — structure correct, no forbidden sections, all links embedded in content sentences
- [ ] **Testing** — every command and code block was actually executed and passed
- [ ] **Style** — style guide checklist from Step 3 passed for every paragraph
- [ ] **Human review** — article shown to user, user confirms it is ready

Do NOT commit or push until the user explicitly says to.
