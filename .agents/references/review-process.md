# Review Process

Six-step process for reviewing any documentation article.
Load this file when a skill tells you to run the review process.

Follow steps sequentially. Do not batch-read all steps upfront.
Complete and fix each step fully before moving to the next.

---

## Step 1 — Run the tools

Run all four from the repository root. They catch the mechanical violations so the manual steps can focus on what a script cannot see.

```powershell
python .agents/tools/style_check.py {relative/path/to/article.mdx}
python .agents/tools/check_mdx_encoding.py {relative/path/to/article.mdx}
.\.agents\tools\validate_mdx.ps1 {relative/path/to/article.mdx}
python .agents/tools/check_article_images.py {relative/path/to/article.mdx}
```

- `style_check.py` covers: "you/your", forbidden words, UK spelling, em-dash spacing, link text, meta-preamble openers, number style, alt text, heading style, callout prefixes, frontmatter.
- `check_mdx_encoding.py` covers: BOM, CRLF, garbage characters, invalid UTF-8.
- `validate_mdx.ps1` covers: MDX that does not compile. It does not catch a missing `.jsx` in the MethodSwitch import.
- `check_article_images.py` covers: images from another folder, missing files, duplicates, unreferenced files.

Fix every real violation and re-run until each tool reports no problems. Note false positives (a term inside a URL or a technical name that must stay) and leave that text unchanged.

---

## Step 2 — Structure and formatting

```powershell
# Forbidden sections and heading openers
Select-String -Path article.mdx -Pattern '^## (Next steps|Prerequisites|Requirements|Related documentation|See also|Get started|What''s next|What |How |Why |When )'
```

**Manual checks:**
- Every `##` and `###` heading is followed by a prose sentence before any code, table, or list
- No two consecutive headings without text between them
- Opening paragraph does not describe the document — it states what the reader achieves
- No separate `## Prerequisites` section — requirements are in the opening paragraph
- Bold only for UI elements, field names, and section names. List the bold text and check each one:
  ```powershell
  Select-String -Path article.mdx -Pattern '\*\*[^*]+\*\*' -AllMatches
  ```
- Procedure format matches the step size: all short steps as a numbered list; large or mixed steps as `<Steps>`, with no step title duplicated by its body (see `procedures.md`, "Choosing the format")
- After any table or code block introducing 3+ new terms: an orienting sentence follows
- All tab groups (`<Tabs>`) have the same set of tabs throughout the article
- Screenshots appear AFTER the step text, not before or in the middle

---

## Step 3 — Links

```powershell
# Standalone link sentences (banned patterns)
Select-String -Path article.mdx -Pattern 'For more details|^See \[|Learn more in|Refer to \[|For more information'

# All external URLs, to check for duplicates
Select-String -Path article.mdx -Pattern '\]\(https?://'
```

**Manual checks:**
- Link text is 1–2 words. Exception: Gcore product names such as "Gcore Customer Portal" are never shortened (see `style-guide.md`, "Links")
- For each URL appearing more than once: all occurrences after the first are plain text
- No sentence whose only purpose is to contain a link
- Internal links are root-relative

---

## Step 4 — Voice and terminology

```powershell
Select-String -Path article.mdx -Pattern 'permanent (API )?token|the following|click on|\bgo to\b|\bchoose\b|type in|\bplatform\b' 
```

**Manual checks:**
- "navigate to" (not "go to"), "click" (not "click on"), "select" (not "choose"), "enter" (not "type in")
- Navigation paths use `>` as the separator: `**Section** > **Subsection**`
- API tokens are never called "permanent"
- "you/your" is fixed in authored prose and inside `<Info>`, `<Note>`, `<Warning>`, `<Tip>` blocks. Code blocks and terminal output stay verbatim
- Read adjacent sentence pairs — join cause-effect or contrast pairs with a connector
- Voice is consistent throughout (tutorial or reference, not mixed)

---

## Step 5 — Content accuracy

**Verify each internal link:**
1. Extract the path from the link
2. Check that the file exists at `{repo_root}/{path}.mdx` or `{repo_root}/{path}/index.mdx`
3. If not found → flag as broken

Images are already checked by `check_article_images.py` in Step 1. Do not change an image path without confirming the file exists at the new path.

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
