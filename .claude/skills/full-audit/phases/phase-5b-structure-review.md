# Phase 5b — Structure and flow review

Load `.agents/references/docs-styleguide-anti-reference.md` now.

Read the article top to bottom as a single document — not section by section. Apply the four checks below in sequence.

## UI inventory test

Could the article outline be recreated by reading the UI from top to bottom? If the sections map to tabs, panels, or form fields rather than to user tasks or decisions — restructure.

## Flow test

Does the article restart its workflow, repeat setup instructions in a different location, or surface information before the reader needs it? Specifically:

- Credentials, URLs, or keys must be obtained before they are discussed or used.
- Related modes (e.g., PUSH and PULL) must be grouped before common behavior or limits shared by both.
- Demos, examples, and code snippets must follow the content they illustrate — not appear pages later.
- The same fact must not appear twice in different phrasing. Merge or remove the duplicate.
- Optional or recommended settings must not be presented as mandatory requirements.

## Positioning test

Does any language make a claim stronger than the evidence supports?

- "Cause:" in troubleshooting must name a confirmed cause, not a possible one. If the cause is not confirmed, use "Possible cause:".
- "Best choice for", "always", "will" used as guarantees without showing the comparison or basis — soften or remove.
- Optional/recommended settings labeled as required — fix the labeling.
- Universal protocol claims ("X only supports Y") when the actual constraint is the product's implementation — scope to the product.

## Section heading test

Does any H2 or H3 exist solely to name a concept or list what is available, with no user action or decision inside?

Examples of headings that signal a reference dump: "Main principles", "Overview", "Key concepts", or a standalone H2 that contains only a cross-reference paragraph. Merge into the preceding section, inline the content, or convert to a cross-reference sentence.

## Applying fixes

For each structural issue found, record it in the FINDING format from `../finding-formats.md` with category `Structural flow` or `Content positioning`:

```
FINDING: Structural flow
Location: Section "[heading]"
Issue: [one-line description — e.g., "PUSH setup restarts workflow after URL anatomy"]
Action needed: [reorder / merge / remove / rewrite]
```

Apply all structural fixes before proceeding to Phase 6. Do not treat structural issues as "nice to have" — they affect whether the article reads as a single document or as an assembly of independent sections.

**Do not move to Phase 6 until the article reads as one continuous document.**
