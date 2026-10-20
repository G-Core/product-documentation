# Phase 5 — Apply fixes

Before rewriting any section, load `.agents/references/content-types.md` and identify
the article's content type (how-to, conceptual, reference, or combined). Keep the
content type intact when rewriting — do not convert a how-to into a reference or vice versa.

If any `<MethodSwitch>` structure will be changed, load `.agents/references/mdx-rules.md`.

Apply all confirmed findings to the article. For each fix:

1. Find the exact location in the article.
2. Read the surrounding paragraph or section to understand tone and structure.
3. Write the fix so it fits naturally — do not leave mechanical edits that break flow.

## Rules for applying fixes

**UI label or field name changed:**
- Replace every occurrence throughout the article.
- Check whether surrounding sentences now read awkwardly and rewrite if needed.
- Update alt text on any screenshot that shows the renamed element.

**Step added or removed:**
- Rewrite the affected section, do not patch individual sentences.
- Renumber all steps in the section.
- Verify the intro sentence of the section still describes what follows.

**Navigation path changed:**
- Update the path in all occurrences.
- Check whether the step introducing navigation needs rewording.

**Screenshot replaced:**
- Replace the `<Frame>` content with the new filename using the correct format:
  ```mdx
  <Frame>![Alt text](/images/docs/{product}/{slug}/filename.png)</Frame>
  ```
  Always write the `<Frame>` on a single line with the markdown `![alt](src)` shorthand inside. Do not add `width` attributes or `<img>` tags.
- Update the alt text to describe what the new screenshot shows.
- Delete the old file with `git rm`.

**Duplicate screenshots:** after placing all new screenshots run `python .agents/tools/check_article_images.py {article}` and fix every `DUPLICATE`, `UNREFERENCED`, `WRONG_FOLDER`, and `MISSING` line as described in Phase 3. Never copy the same source screenshot to two different filenames.

**Prerequisite dependency noted:**
- Add a cross-link to the prerequisite article where the relevant step appears.
- If no article exists for the prerequisite, add a `<Note>` or `<Info>` block
  describing what must exist before the step. Do not add a `## Prerequisites` section.

**Broken flow / feature works differently:**
- Describe the actual current behavior in the article.
- Remove steps that no longer apply.
- If the replacement flow is significantly different, rewrite the section from scratch.

## Hard rules — never do these

- Never touch `<MethodSection id="api">` — API sections are a separate update cycle.
- Never rename article files or change slugs.
- Never edit `docs.json` without explicit user confirmation.
- Apply only fixes from the confirmed findings list. Note any other issues you notice
  at the end — do not fix them silently.

## `<p>` tag rules

The rule depends on whether the article uses `<MethodSwitch>`:

**Articles WITHOUT `<MethodSwitch>`:**
- Remove any stray `<p>` wrappers around plain prose paragraphs — they are not needed
  outside JSX and produce unnecessary markup.
- Bullet lists must never be wrapped in `<p>`.

**Articles WITH `<MethodSwitch>` (inside `<MethodSection>` only):**
- Prose paragraphs that sit immediately before or after a `<Frame>`, a fenced code
  block, or a `<Tabs>` component **must** be wrapped in `<p>` — otherwise they merge
  visually with the adjacent block element.
- Every numbered step is written as `<p>1. text</p>`, with a blank line between steps. Without
  `<p>` the steps merge into one paragraph. Prose that sits between numbered steps is wrapped in `<p>` too.
- Sub-items of a step are plain bullets indented 3 spaces, placed after the step's `<p>`.
- Bullet-only lists must NOT be wrapped in `<p>` — they are block-level and render
  correctly without it.
- Never delete a `<p>` tag that acts as a structural separator between numbered steps
  inside `<MethodSection>`. If the text inside is outdated, replace the text — not the tag.
