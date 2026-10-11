# Phase 7 — MDX rules check

Load `.agents/references/mdx-rules.md` now.

Check whether the article uses a `<MethodSwitch>` component:

```powershell
Select-String -Path path/to/article.mdx -Pattern "MethodSwitch" -Quiet
```

**If `<MethodSwitch>` is not present** — this phase takes less than a minute.
Verify only the basic MDX rules below and move on.

**If `<MethodSwitch>` is present** — read the full `mdx-rules.md` and apply all
relevant checks for the component, its sections, and the import line.

## Checklist (all articles)

- [ ] No raw HTML tags (`<div>`, `<span>`, `<br>`) except where explicitly approved
- [ ] Outside `<MethodSection>`: no stray `<p>` wrappers around plain prose paragraphs
- [ ] Inside EVERY `<MethodSection>` (Portal, API, Terraform, CLI — all tabs): EVERY standalone prose paragraph AND every numbered step IS wrapped in `<p>` (`<p>1. text</p>`) — no exceptions, no analysis of what is adjacent; bullet list items are NOT wrapped in `<p>`
- [ ] `<Frame>` wraps each screenshot; no bare `![]()` outside `<Frame>`
- [ ] Every image inside `<Frame>` uses markdown shorthand `![alt](src)` — no `<img>` tags, no `width` attributes.
- [ ] `<Tabs>` / `<Tab>` structure is valid: every `<Tab>` has a `title` attribute

**Callout blocks (`<Info>`, `<Warning>`, `<Note>`, `<Tip>`):**
- [ ] No redundant prefix inside the block: remove `**Info**`, `**Warning**`, `**Note**`, `**Tip**` text at the top — the component already renders the label
- [ ] Callout blocks are not nested inside each other
- [ ] No two callout blocks placed back-to-back without prose between them. If two callouts cover the same concern — merge them into one. If they cover different concerns — add a sentence of prose between them to give each block its own context
- [ ] Each callout is used for its semantic purpose: `<Warning>` for data loss / irreversible actions; `<Info>` for important non-obvious context; `<Note>` for supplementary detail; `<Tip>` for optional shortcuts

## Additional checklist (articles with `<MethodSwitch>`)

- [ ] Import line uses `.jsx` extension:
  `import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";`
- [ ] `label` attribute is on `<MethodSection>`, not on `<MethodSwitch>`
- [ ] Every `<MethodSection>` has an `id` attribute (`"portal"`, `"api"`, etc.)
- [ ] `<MethodSwitch>` wraps all `<MethodSection>` blocks — no sections outside
- [ ] Content written for the Portal tab does not bleed into other tabs
- [ ] Never touch `<MethodSection id="api">` — API sections are out of scope

Fix every violation found. If fixing a `<MethodSwitch>` structure, re-read the
relevant section of `mdx-rules.md` before making changes to avoid silent regressions.

**Never use scripts for text replacements in MDX files.**
All fixes must be done with targeted StrReplace calls, one replacement at a time.
Scripts introduce quoting and encoding errors that corrupt the file silently.
StrReplace is explicit, auditable, and safe.
