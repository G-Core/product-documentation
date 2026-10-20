# Phase 8 — LLM quality review

Before presenting the article to the user, run the automated quality review script.
This must happen after Phase 7 and before Phase 9 — never skip it.

```powershell
python .agents/tools/review_article_quality.py --article "{article-path}.mdx"
```

The script sends the article to the configured LLM backend and scores it on 11 criteria (1–10 each).

## Step 1 — Classify every remark

For each remark the LLM produces, classify it before doing anything:

**Automatic false positives — reject without fixing:**

- Suggests explaining bash, curl, SSH, Python, Go, Terraform, RDP, cloud-init,
  or any tool that is a prerequisite for the section's audience.
- Suggests making the article self-contained by adding information that belongs
  in a separate article and is already linked.
- Complains that an Accordion, Tabs, Info, Tip, or Warning adds cognitive load.
- Complains about the position of a method tab (Portal/API/Terraform order).
- Suggests adding transition sentences between numbered steps where the
  numbering already makes the sequence obvious.
- Flags technical terms (IPv4, CIDR, DHCP, SDK, API key, region ID) as jargon
  requiring explanation.
- Suggests the article is incomplete because a related topic (connecting,
  monitoring, deleting) is not covered — those are separate articles.
- Flags a screenshot caption or alt text as insufficient when the screenshot
  itself makes the meaning clear.
- Suggests adding detail about a UI element that is visible on the adjacent screenshot.

**Requires judgment — verify before deciding:**

- Mentions a diagram or image that the article references but the LLM cannot see.
  → Check whether the referenced visual actually exists in the article. If it does,
  false positive. If it does not exist, it is a real finding.
- Flags a sentence as hard to read.
  → Read the sentence yourself. If a native English speaker would pause on it,
  fix it. If the sentence is just technical, reject.
- Flags repeated information across sections.
  → Check whether the repetition is intentional (e.g., a warning duplicated at
  the point of action) or genuine duplication. Fix only genuine duplication.

**Always real — fix immediately:**

- A specific word that has a simpler, equally precise alternative
  (e.g., "prior" → "before", "utilize" → "use").
- A sentence that contains two nested clauses that could be two sentences.
- Information stated twice in consecutive paragraphs with no structural reason.
- A step that promises a result ("The window opens") but the result never comes.

## Step 2 — Apply fixes

Fix only the remarks classified as real. Do not touch:
- Factual content verified against the portal in Phase 2.
- Step numbering.
- Portal-verified UI labels, button names, field names.
- The structure of MethodSwitch tabs.

## Step 3 — Re-run (max 2 iterations)

After applying fixes, re-run the script. Compare the new score to the previous one.

- If the score improved and all remaining remarks are false positives — stop.
- If the score did not improve despite real fixes — stop after this second run.
  Do not loop a third time.
- If no real remarks were found in the first run — proceed directly to Phase 9
  without re-running.

## Step 4 — Report to the user

Do NOT ask the user to approve fixes or review individual remarks.
Do NOT present the raw LLM output to the user.

When this phase is complete, include a single block in the Phase 8 report:

```
Auto-review (LLM): X.X / 10
  Fixed: [list of real fixes applied, one line each]
  Rejected as false positives: [count] remarks
  Remaining remarks (not fixed): [list only if they are genuinely debatable]
```

If no fixes were needed and no debatable remarks remain, write:
```
Auto-review (LLM): X.X / 10 — no actionable remarks.
```
