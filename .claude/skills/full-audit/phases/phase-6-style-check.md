# Phase 6 — Style guide check

Load `.agents/references/style-guide.md` and `.agents/references/procedures.md` now.

## Step 1 — Run the automated style linter

Run the style linter first. It catches mechanical violations automatically so the manual
checklist can focus on things the script cannot detect (flow, headings, structure, logic).

```powershell
python .agents/tools/style_check.py {relative/path/to/article.mdx}
```

Replace `{relative/path/to/article.mdx}` with the actual path, for example:
```
python .agents/tools/style_check.py hosting/virtual-servers/order-a-virtual-server.mdx
```

For every violation the script reports:
1. Read the line it flagged.
2. Fix the violation if it is real.
3. If it is a false positive (e.g. a term matched inside a URL or a technical name
   that must stay as-is), note it and move on — do not change correct text.

Re-run the script after fixing until it reports **OK — no violations found**.

## Step 2 — Manual checklist

The linter already enforces: "you/your", banned words, UK spelling, em-dash spacing, link text, meta-preamble openers, number style, alt text, heading style, callout prefixes, and frontmatter. The checklist below covers only what a script cannot see.

Work through the article section by section and verify each rule. Do not skim.
For each checklist item: read the article, verify the rule, then mark the item with `[V]`.
Only mark `[V]` after you have actually checked — not as a placeholder.
When the full checklist is marked, scan for any remaining `[ ]` and re-check those lines before proceeding.

Checklist:

**Voice and tone:**
- [ ] No "permanent API token"

**Sentence structure:**
- [ ] Causal connectors used between related sentences
- [ ] No isolated facts in sequence (dictionary-card pattern)
- [ ] Opening paragraph does not have a `## Prerequisites` section

**Headings:**
- [ ] Sentence case
- [ ] No "What / How / Why / When" headings
- [ ] No infinitive headings ("To create...")
- [ ] No consecutive headings (at least one sentence between them)
- [ ] Every heading has an intro sentence before lists or code

**Forbidden sections:**
- [ ] No `## Next steps`, `## See also`, `## Related documentation`, `## Prerequisites`,
  `## Requirements`, `## Get started`, `## What's next`

**Links** (script catches text length, &nbsp;, banned patterns, relative paths, docs.gcore.com URLs):
- [ ] First mention of portal: `[Gcore Customer Portal](https://portal.gcore.com)`
- [ ] Subsequent mentions: plain "the Customer Portal" (no link, no "Gcore" prefix)

**Formatting:**
- [ ] Bold only for clickable UI elements and field names
- [ ] Inline code for commands, values, and file names

**Procedures** (cross-check against `procedures.md`):
- [ ] Format matches the step size: all short steps as a numbered list; large or mixed steps as `<Steps>`, with no step title duplicated by its body (see `procedures.md`, "Choosing the format")
- [ ] Location before action in each step
- [ ] Optional steps prefixed with `(Optional)` exactly
- [ ] Login step uses "log in to" (three words, not "log into")
- [ ] No single-item numbered lists
- [ ] Sub-steps indented with 3 spaces under the parent step
- [ ] No "Step 1:" label in the step text itself — the number is enough
- [ ] No instruction to "press Enter" when a button click achieves the same thing
- [ ] Result sentences ("The X page opens.") placed after the step, not as a separate step

**Screenshots:**
- [ ] Each screenshot has alt text (under 125 characters, sentence case)
- [ ] Screenshots appear after the step text, not before

**Terminology:**
- [ ] "click" not "click on"
- [ ] "select" not "choose"
- [ ] "enter" not "type in"
- [ ] "navigate to" not "go to"

**Numbers:**
- [ ] Space between number and unit: "128 GB", "10 Gbps"

**Capitalization:**
- [ ] Gcore product names in Title Case: Bare Metal, Virtual Machines, etc.
- [ ] Article titles and headings in sentence case

Fix every violation found. If a fix requires rewriting a paragraph, do it.
If any items remain unmarked (`[ ]`) after the full pass — re-check those lines before closing Phase 6.
