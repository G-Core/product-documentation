---
name: write-concept
description: Write or rewrite a Gcore conceptual documentation article. Use when the article explains what a feature is, how it works architecturally, or what options exist — not when it describes step-by-step tasks. Apply when writing overview pages, landing pages, or architectural explanations.
---

# Writing conceptual articles

A concept article answers one or more of these questions:

- What does this feature do and how do I access it?
- What are my options and how do they relate to each other?
- How does the underlying mechanism work?
- What do the results mean and how do I use them?

It does not teach the reader to perform a task step by step. That is a how-to article.

---

## Before writing

Load these files:

1. `.agents/references/content-types.md` — confirm the article is Type 5
2. `.agents/references/style-guide.md` — writing rules
3. `.agents/references/mdx-rules.md` — frontmatter and MDX structure

---

## Structure

Build the article around **sequential reader questions**. Each section answers
exactly one question the reader has at that point. Sections must be ordered so
that each one is intelligible only after reading the previous one.

Test the order: "Could the reader skip section N and still understand section N+1?"
If yes, merge or reorder.

Allowed sections for a concept article (use only those that are needed):

| Section | Reader question it answers |
|---------|---------------------------|
| Opening paragraph (no heading) | What does this do and where do I access it? |
| `## {Feature name or task type}` | What options exist and how do I choose? |
| `## {Mechanism name}` | How does it work technically? |
| `## {Interpretation or output}` | What do the results mean and what is my role? |

No section exists just to be complete. If a section has one sentence that
could fit in another section, absorb it.

---

## Opening paragraph

Two to three sentences. No heading.

**Sentence 1:** What the feature does mechanically — verb + object + output.
Use precise verbs: analyzes, processes, returns, generates, stores, routes.
Do not say: "is a powerful solution", "enables", "provides the ability to".

**Sentence 2:** How to access it. Link the portal to the exact portal page URL
(not the root `portal.gcore.com`). Link the REST API reference separately.
Do not write portal navigation paths with arrows (Streaming → AI → AI tasks).
That format belongs in a how-to first step, not in a conceptual intro.

```
Gcore AI content moderation analyzes video and image files and returns
detected objects with confidence scores. The feature is available via the
[Gcore Customer Portal](https://portal.gcore.com/streaming/ai/list)
and via the [REST API](/api-reference/streaming/ai/create-ai-task).
```

---

## Options section

When the feature has multiple variants (task types, modes, tiers, plans),
explain **relationships**, not a catalog.

### Step 1 — find the organizing principle

Ask: what do these options have in common, and how do they differ?

- If they differ in scope or strictness along a continuum → describe the
  continuum with links embedded in prose.
- If some share a common purpose while others serve a different one → group
  the related ones, then describe the outlier separately.
- If they differ on a decision axis the reader must choose → use a table where
  each row answers "when to use X".

### Step 2 — write around the relationships, not the items

Embed links inside the sentence that explains the relationship. The link text
is the option name. The surrounding sentence explains what sets it apart.

```
The three nudity checks differ in scope:
[NSFW materials](/path) applies the broadest classification and can flag
content even without explicit nudity;
[Soft nudity](/path) focuses on full or partial nudity across a wider range
of body-part categories;
and [Hard nudity](/path) is limited to exposed primary and secondary sex organs.

[Sport activities](/path) serves a different purpose, identifying sporting
activities, events, and key moments in video content.
```

Do not use this pattern:
```
* [NSFW materials] — detects NSFW content
* [Soft nudity] — detects partial nudity
* [Hard nudity] — detects explicit nudity
* [Sport activities] — detects sports
```
That is a reference catalog. It lists items; it does not explain the system.

### What not to add

Do not add a "## Use cases" section. Use cases expressed as generic bullet
lists ("Ensure delivery of age-appropriate content") are unverifiable claims.
If use is important, describe it through the capability: what the task detects
already implies where it is useful.

---

## Mechanism section

Explains how the feature works technically. One section, not split into
sub-sections unless there are genuinely distinct mechanisms.

Write with precision. Each sentence must be verifiable.

**Include:**
- How processing is triggered (on upload? on request? keyframe-based? batch?)
- What is included vs excluded from analysis
- What the feature returns — exact field names, data types, units, built-in thresholds
- What happens to the input data after processing (retention, deletion)

**Precision rules:**

| Vague | Precise |
|-------|---------|
| "only some frames are analyzed" | "objects between keyframes are not detected" |
| "low-confidence results are filtered" | "results below 30% are excluded by the service" |
| "images are also supported" | "image duration is treated as 1 second" |
| "processes video in real time" | "the analysis frequency matches the keyframe interval" |

"In real time" implies continuous or live analysis. Use it only if the feature
genuinely processes a live stream with no batch delay. For file-based or
keyframe-based processing, describe the actual mechanism.

---

## Interpretation section

Add this section only when the reader must make a decision based on the
feature's output — for example, setting a confidence threshold, choosing
a response action, or applying business logic to returned scores.

**Critical distinction: Gcore's decision vs. the reader's decision.**

State explicitly which threshold, cutoff, or behavior is built into the service
and which is the reader's responsibility. Conflating them misleads the reader.

```
WRONG:
"A probability threshold can be configured to determine when a video
is inappropriate."
→ Implies a Gcore product setting exists.

CORRECT:
"Each task returns a confidence percentage. Results below 30% are excluded
by the service. Apply a cutoff to the returned scores based on the
requirements of the specific service."
→ Gcore's fixed behavior (30%) is stated separately from the reader's
decision (what threshold to apply above 30%).
```

When explaining the reader's decision, describe the principle — not a
recommendation pretending to be a fact:

```
WRONG:
"The acceptable threshold for an adult platform is higher than for a
children's platform."
→ Sounds like a product specification.

CORRECT:
"There is no universal cutoff. Process a representative sample and analyze
the score distribution to determine an appropriate cutoff before production."
→ States the principle; the reader makes the specific decision.
```

---

## Links

Do not use "## Next steps" or "## See also" sections.

Embed links to how-to articles inside the section where the reader naturally
wants to go deeper. After reading about an option, the reader should find the
link to that option's how-to article in the same paragraph.

Standalone link sentences — sentences that exist only to host a link — are
forbidden. Embed the link in a sentence that provides real information.

The ban applies to routing clauses too, not only standalone sentences. A clause
that exists only to send the reader elsewhere is the same violation:

```
WRONG:
"For more information, see the content moderation guide."
"General usage is free; translation may incur additional charges — details are on the [pricing page]."
→ "details are on the [pricing page]" carries no content; it only routes.

CORRECT:
"General usage is free; translation may incur [additional charges](url)."
→ The link is an attribute of the thing it describes, not a routing clause.

"[NSFW materials](/path) applies the broadest classification and can flag
content even without explicit nudity."
→ The link is inside a sentence that describes what makes this option distinct.
```

---

## Do not achieve cohesion by packing facts into compound sentences

Cohesion means one sentence creates the context for the next — not that several
facts share one sentence through colons, semicolons, dashes, or conjunctions.

**Wrong:** Compressing three facts into one sentence to avoid repetition:
```
Each task returns the detected object class, the frame number, and a confidence
percentage; the service excludes results below 30% — and above that threshold,
the cutoff depends on the use case, which varies across services.
```

**Correct:** A sequence of short connected thoughts where each follows from the previous:
```
Each task returns the detected object class, the video frame number, and a
confidence percentage. The service excludes results below 30%. Above that
threshold, the appropriate cutoff depends on the use case.
```

**Test:** Read the article as continuous prose, ignoring the headings. After
every sentence, ask: "Why is the next sentence here?" If the answer is only
"because this is another fact about the same subject" — the passage is not
cohesive yet. Each sentence should set up the next, not just add to it.

---

## Do not restart the subject at every heading

A heading changes the focus; it does not reset the article. Before writing a
section opening, read the final paragraph of the preceding section and continue
from the state of knowledge already established.

**Symptom:** Three consecutive section openings all start with the same noun:

```
Content moderation provides four tasks...
Content moderation processes video by analyzing keyframes...
Content moderation excludes results below 30%...
```

**Fix:** Use a bridge that expresses the relationship between sections:

```
Regardless of the selected task, video analysis runs on keyframes...
```

The bridge is not decorative — it states why the reader is moving to this
section after reading the previous one.

Preferred bridge patterns for concept articles:
- `Regardless of the selected task...` — when the mechanism applies to all options
- `In the returned results...` — when moving from mechanism to output
- `The service therefore does not...` — consequence of the mechanism just described
- No transition at all — when the connection is self-evident from the heading

Do not use: `Additionally,`, `Also,`, `Furthermore,` — these add no relationship.

---

## Section depth

A section heading is justified only when it introduces enough content to stand
alone — at minimum, two sentences or one sentence and a list.

A single-sentence section is micro-section fragmentation. Absorb it:

```
WRONG:
## Billing
Content moderation pricing is on the pricing page.

CORRECT: (no heading, closing sentence in the final substantive section)
Content moderation pricing is on the [pricing page](url).
```

---

## Terminology

Use the names the product uses — portal labels, API field names, response keys.
If the portal calls them "tasks", the article calls them "tasks" — not "checks",
"capabilities", or "content types".

Before writing the options section, confirm the correct names from:
- The portal UI (take a snapshot of the relevant form or dropdown)
- The API response schema or the existing child articles

---

## Checklist before finishing

- [ ] Opening sentence states what the feature does mechanically (no marketing language)
- [ ] Portal link goes to the exact feature page, not the root portal URL
- [ ] REST API is linked, not mentioned as plain text
- [ ] Options section explains relationships and selection principle, not a catalog
- [ ] Mechanism section uses precise, verifiable language
- [ ] Gcore's built-in behavior is distinguished from the reader's decisions
- [ ] No "## Use cases", "## Next steps", or "## See also" sections
- [ ] No standalone link sentences
- [ ] No section has a heading for fewer than two sentences of content
- [ ] No portal navigation breadcrumbs (Streaming → AI → AI tasks) in prose
- [ ] All multi-word link text uses `&nbsp;` between words
- [ ] Link text is three words or fewer
