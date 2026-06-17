# Style Guide — Gcore Product Documentation

Canonical writing and formatting rules for all documentation work.
Load this file when a skill tells you to. Do not load it proactively.

---

## Target audience

The reader is a **medium-technical Gcore customer**: a developer or DevOps engineer
who knows cloud infrastructure (VMs, networks, APIs) but may not know the specific
Gcore product being documented.

- Knows: cloud concepts, CLI tools, APIs, JSON/YAML, basic scripting
- May not know: the specific Gcore service, its terminology, its configuration format
- Goal: get something working as fast as possible, without reading more than necessary

**Rules:**
- Define every product-specific term on first use. One sentence: "A provider is a plugin that..." not "The provider connects to..."
- Do not open with jargon. If the first sentence requires prior knowledge, rewrite it.
- Show value before mechanics. The reader needs to understand *why* before *how*.

**Self-check:** Read the article's first three sentences aloud. If a medium-technical
reader would stop and ask "what is X?" without finding an answer — rewrite before continuing.

---

## Voice and tone

### No meta-preamble openers

Never open with a sentence that describes the document itself.

**Banned openers:**
- `This guide covers...`
- `This article explains...`
- `In this document, you will learn...`
- `This tutorial walks you through...`
- `This section describes...`

Start with the subject matter directly.

| Bad | Good |
|-----|------|
| "This guide covers installing Terraform and configuring the Gcore provider." | "Terraform manages infrastructure as code through configuration files — a [Gcore account](...) and a [permanent API token](...) are the only requirements." |
| "This article explains how import works." | "Terraform import reads an existing resource's state from the API and writes it to the state file." |

### No "you" or "your" in authored prose

Rephrase to imperative (without subject) or neutral third person.
This applies everywhere — body text, `<Info>`, `<Note>`, `<Warning>`, `<Tip>` blocks.

| Bad | Good |
|-----|------|
| "You need a permanent API token." | "A permanent API token is required." |
| "Your configuration file should include..." | "The configuration file must include..." |
| "When you run terraform plan..." | "When running terraform plan..." |
| "It is not linked to your Gcore account." | "It is not linked to the Gcore account." |

**Exception:** terminal output verbatim (e.g. "Your infrastructure matches the configuration") — do not alter.

### Voice — who is the subject

Use the right subject for each situation:

| Situation | Voice | Example |
|-----------|-------|---------|
| Gcore does something automatically | 1st person plural | "We support SRT and WebVTT formats." |
| Explaining a technology or feature | 3rd person | "5G technology improves industrial automation." |
| Gcore as a product providing something | 3rd person | "Gcore provides the following disk types." |
| Instruction for the reader | Imperative (no subject) | "Navigate to the DNS section." |

**"We" for Gcore:** use it, but not in every sentence. Vary with 3rd person to avoid repetition.

### Contractions

Common contractions are allowed — they make documentation sound like a real person wrote it.

Allowed: it's, don't, can't, won't, doesn't, they're, we've, there's

Avoid contractions that include "you" or "I" (you're, you'll, I'm, I'd) — these conflict with the no "you/your" rule.

### Be direct

- Active voice — avoid passive where possible
- Imperative mood for instructions — no "you should", just the action
- Avoid passive constructions: "The configuration must be updated" → "Update the configuration"

**Good:** "Click **Save** to apply changes."
**Good:** "Navigate to **DNS** > **Records**."
**Good:** "Gcore configures X automatically."
**Good:** "We support SRT and WebVTT formats."
**Bad:** "The Save button should be clicked to apply changes."

### Consistent voice within an article

Every article must maintain one voice throughout:
- **Tutorial voice** (guides, how-to): direct, action-oriented, explains what happens and what to do next
- **Reference voice** (API docs, resource indexes): concise, neutral, states facts without narration

Do not mix. A tutorial section that drifts into reference tone must be rewritten.

---

## Sentence structure

### Causal connectors

Two adjacent sentences that share a cause-effect or contrast relationship must be
joined with a connector, not separated by a full stop.

| Relationship | Connector | Example |
|---|---|---|
| Cause | because, as, since | "Pin the version because v0 and v2 use incompatible formats." |
| Contrast | while, whereas | "New projects start with v2, while existing projects stay on v0." |
| Result | so, which means | "It syncs automatically, so new resources become available faster." |
| Condition | when, if | "When the project grows, split config into multiple files." |

**Bad:** "Specify the version to avoid upgrades. v0 and v2 have different formats."
**Good:** "Specify the version to avoid upgrades, because v0 and v2 use different, incompatible formats."

### Paragraph flow and transitions

The opening sentence of each paragraph must establish its relationship to the previous one.

| Type | Signal |
|------|--------|
| Narrowing | "For [specific case],..." / "When [condition],..." |
| Causal | "As a result,..." / "This means..." |
| Continuation | Start with "It" or "This" referring back explicitly |
| Contrast | "Unlike v0,..." / "In contrast,..." |

### Stop when the point is made

If a sentence already makes a complete point, stop. Do not append "— specifically in X, Y, and Z"
unless the enumeration is genuinely necessary for the reader to act correctly.

When "everywhere" or "in all cases" is used, a list that follows is usually redundant.

### Avoid redundant reassurance

State a reassurance once — at the moment it is most useful. Repeating "no infrastructure
will be created" three times in one page patronizes the reader.

### Do not over-explain the obvious

A medium-technical reader knows how to click a button, type a value, open a terminal,
and read a prompt. Do not explain actions that the interface or terminal output already describes.

**Forbidden:**
- Showing a terminal prompt that says `Enter a value: yes` then writing "Type `yes` when prompted"
- Explaining what a button does after the reader just clicked it
- "Click **Save** to save your changes" — saving is implied by clicking Save

### No redundancy or tautology

Do not restate information the reader already has from a heading, table, code block, or the previous sentence.

| Bad | Why |
|-----|-----|
| "follow the migration guide for step-by-step instructions" | a guide already implies step-by-step |
| "different schemas and are not interchangeable" | "not interchangeable" is implied by "different schemas" |
| prose repeating what a table just said | paragraph must add context the table does not contain |

---

## Paragraph writing formulas

Use these formulas for writing concise, non-repetitive paragraphs.
These are structure rules, not example text.

### Formula A: Two semantic steps (one paragraph = 2 sentences max)

**Sentence 1 (WHAT):**
```
{Vendor} {enables|includes|supports} {Feature} {by default|automatically} {in|on|for} {Scope}.
```

**Sentence 2 (WHY):**
```
It {mechanism}, {benefit}.
```

**Rules:**
- Feature name appears ONCE (sentence 1), then only "It" or "This"
- "automatic/by default" appears ONCE, NOT in sentence 2
- No filler in sentence 2: "significantly", "advanced", "optimization", "performance benefits"
- After sentence 2: STOP. No sentence 3.

### Formula B: Mechanism → Effect

Structure: `It {mechanism} → {effect}.`

One mechanism, one effect. Not: "reduces A and B and C".

### Formula C: Third idea = new paragraph

If a third semantic step is needed ("when to use"), it is a NEW paragraph:
```
Paragraph 1: Formula A (2 sentences)

Paragraph 2: This matters most for {workload_type}.
```

### Formula D: Confidence based on source

- Fact exists in source material → `It {does X}.`
- Fact not in source material → Do NOT write. Or: `It can {do X} on supported configurations.`

**Forbidden without source:** "typically", "always", "significantly", "in most cases"

### Formula E: No root-word pairs in one paragraph

These pairs are **forbidden** in the same paragraph:

| Word 1 | Word 2 | Fix |
|--------|--------|-----|
| optimize | optimization | use "improve" instead of one |
| reduce | reduction | use "lower" or "decrease" instead |
| configure | configuration | use "set up" or "settings" instead |
| automatic | automatically | keep only one |
| perform | performance | rewrite sentence |

### Self-check before finishing a paragraph

- [ ] 2 sentences maximum
- [ ] Feature mentioned once, then "It"
- [ ] No root-word pairs
- [ ] No filler words
- [ ] 30–50 words

If any check fails — DELETE and rewrite. Do not "slightly adjust".

---

## Structure and headings

### Headings

- **Sentence case:** "Create a virtual machine" — not "Create a Virtual Machine"
- **Length:** 5–8 words maximum
- **Levels:** H2 for main sections, H3 for subsections
- **Form:** declarative or imperative only

**Forbidden heading patterns:**

| Forbidden | Use instead |
|-----------|-------------|
| `## What changes in v2` | `## Changes in v2` |
| `## How import works` | `## Import process` |
| `## When to use import` | `## Use cases` |
| `## What is a provider?` | `## Provider overview` |
| `## Why use Terraform?` | `## Terraform overview` |

Any heading starting with **What, How, Why, When** is forbidden.

**No infinitives in headings.** Use action verbs, not "To + verb":

| Bad | Good |
|-----|------|
| `## To create a project` | `## Create and configure projects` |
| `## To enable the feature` | `## Enable the feature` |

Exception: FAQ articles where the title is a question.

**Step headings** use "Step N." format with a period after the number:
```
## Step 1. Clone the repository
## Step 2. Configure the provider
```

**Headings are noun phrases, not instructions.**
A heading describes a topic — it does not tell the reader to do something.

| Bad | Good |
|-----|------|
| `## Find the endpoint URL` | `## Endpoint URL` |
| `## Send a request` | `## Chat completions` |
| `## Secure the endpoint` | `## Endpoint authentication` |
| `## List available models` | `## Available models` |

**No consecutive headings.**
A heading must not be immediately followed by another heading. Write at least
1–2 sentences of text before the next heading.

### Every heading needs an intro sentence

After every `##` and `###` heading, the next line must be a prose sentence.
A code block, table, or list appearing immediately after a heading is a violation.

**Bad:**
```
### Authentication

| | v0 | v2 |
```

**Good:**
```
### Authentication

Both versions use the same token value, but the attribute name and environment variable changed.

| | v0 | v2 |
```

### Forbidden sections

These headings must never appear:

| Forbidden | Why |
|-----------|-----|
| `## Next steps` | Sidebar already shows structure; use inline cross-links |
| `## Prerequisites` | Integrate into the opening paragraph |
| `## Requirements` | Same as Prerequisites |
| `## Related documentation` | No link dumps; link inline where topic is relevant |
| `## See also` | Same as Related documentation |
| `## What's next` | Same as Next steps |

### Opening paragraph rules

- No meta-preamble (see Voice section)
- Start with the subject matter: what the product does, or what the reader achieves
- Prerequisites go in the opening paragraph as plain text, not a separate section
- Every article opens with its own unique sentence — never a template sentence that could appear in three different articles

---

## Links

### Link once per destination per article

If a URL has already appeared as a link, all subsequent mentions are **plain text**.
The first occurrence is the canonical link.

### Link text: 1–2 words maximum

The link text must be the noun or short verb phrase that names the destination.
Never use a full clause, sentence fragment, or description.

| Bad | Good |
|-----|------|
| `[install Terraform and configure the provider first](...)` | `[install the provider](...)` |
| `[v2 documentation on Terraform Registry](...)` | `[v2 documentation](...)` |
| `[follow the migration guide for step-by-step instructions](...)` | `[migration guide](...)` |

### Banned link sentence patterns

These create empty sentences. Merge the link into the previous sentence instead.

- `For more details, see [X]`
- `See [X] for more information`
- `Learn more in [X]`
- `For details, see [X]`
- `Refer to [X] for`
- Any standalone sentence whose only purpose is to host a link

**Bad:**
```
For more details, see [API tokens](/account-settings/api-tokens).
```

**Good:**
```
Generate a [permanent token](/account-settings/api-tokens) in account settings.
```

### Links must carry meaning

No separate sentence constructed to host a link.
Embed the link into an existing content sentence as a natural part of the text.

**Forbidden:** "The full parameter list is in the [API reference](...)." — this sentence carries no information beyond the link. If no natural sentence exists for the link, remove the link entirely.

### Gcore Customer Portal naming

| Context | Use |
|---------|-----|
| First mention in article | `[Gcore Customer Portal](https://portal.gcore.com)` |
| All subsequent mentions | plain text: "the Customer Portal" (no link, no "Gcore" prefix) |

---

## Formatting

### Bold

Bold is **only** for:
- Clickable UI elements: Click **Save**
- UI field names: In the **Name** field, enter...
- Section names the reader must find on a page: the **Import** section

**Never use bold for:**
- Technical terms or concepts being introduced
- Table row labels or column labels
- Emphasis on important words mid-sentence

**Exception:** version labels directly before paired code blocks (`**v0:**` / `**v2:**`)
may use bold to visually separate the two blocks.

If a concept needs emphasis, rewrite the sentence so the concept carries weight through
structure. Use a definition pattern: "A provider is a plugin that..." not "The **provider** is a plugin that..."

### Em-dash spacing

Always use a **spaced** em-dash: ` — ` (space before and after).
Never use an unspaced em-dash `—`.

| Wrong | Correct |
|-------|---------|
| `configuration files—a Gcore account` | `configuration files — a Gcore account` |
| `API calls—it defines` | `API calls — it defines` |

### Code

- Inline code: backticks — `api_key`, `terraform plan`
- Code blocks: fenced with language tag — ` ```bash `, ` ```json `, ` ```powershell `
- File names referenced inline: backticks — `providers.tf`
- Include expected terminal output when it helps verify a step succeeded

### Consistent tab sets

All tab groups (`<Tabs>`) in an article must have the same set of tabs.
If one section has Python SDK + Go SDK + curl, every other section must have
Python SDK + Go SDK + curl. No mixing tab sets within an article.

### Cognitive load density

After any table or code block that introduces 3+ new terms, add at least one orienting
sentence before the next code block or table.

**Signs of excessive density:**
- Three or more config attribute names in one sentence
- A paragraph requiring the reader to hold more than two new concepts simultaneously
- A table immediately followed by a code block followed by another table with no prose break

### Tables

- Use for structured comparisons, not for information that reads naturally as prose
- Keep column headers short
- Row labels in the first column: plain text, no bold
- Every table needs a real intro sentence — not one that just restates what the table shows

---

## Procedures

For full step-writing rules — format, ordering, Optional prefix, login steps,
sub-step hierarchy, notes and warnings — see `.agents/references/procedures.md`.

### No stub sections

A section heading followed by one thin sentence is a stub. If a section cannot be
explained in at least 2–3 meaningful sentences, expand it or fold it into a neighbouring section.

---

## Images and screenshots

### When to include

- Complex UI workflows where the path is non-obvious
- Settings that are hard to describe in prose
- Verification steps ("after clicking Apply, the status changes to Active")

### When to skip

- Simple single-click actions described in one sentence
- Frequently changing UI elements

### Screenshot placement

Screenshots go **after** the step text that describes them — never before, never
in the middle of a step. The reader reads what to do, then sees what it looks like.

**Wrong:**
```
<Frame>![Create instance form](screenshot.png)</Frame>

1. In the **Name** field, enter a name for the instance.
```

**Correct:**
```
1. In the **Name** field, enter a name for the instance.

<Frame>![Create instance form with Name field highlighted](screenshot.png)</Frame>
```
- Anything the prose already makes unambiguous

### Screenshot requirements

- **Format:** PNG
- **Alt text:** required, under 125 characters, sentence case, describes what is shown
- **Alt text bad:** "Screenshot of the DNS page"
- **Alt text good:** "DNS records list with the Add record button highlighted"

Full screenshot capture rules (browser settings, crop, zoom, sidebar collapse) are in
`.agents/references/mcp-tools/playwright.md`.

---

## Terminology and naming

### Gcore naming

| Context | Use |
|---------|-----|
| First mention of portal | Gcore Customer Portal |
| Subsequent mentions | the Customer Portal |
| Company as subject | Gcore (not "the platform", "the system", "we") |
| API | Gcore API |

### Forbidden words

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| platform | Vague | Gcore, Gcore Customer Portal, or specific service name |
| ensure, be sure, make sure | Not an action | verify, check, confirm |
| simply, just | Filler, condescending | remove entirely |
| obviously, clearly | Condescending | remove entirely |
| etc., and so on | Vague | complete the list explicitly |
| leverage, utilize | Corporate jargon | use |
| seamlessly, robust, scalable | Marketing filler | say what it actually does |
| programmatic access | Vague | what specifically: creates VMs, configures networks |
| for example (inline) | Breaks sentence flow | restructure the sentence or use a dash |
| such as | Implies incomplete list | complete the list or restructure |

### Common terms

| Use this | Not this |
|----------|----------|
| click | click on |
| select | choose |
| enter | type in |
| navigate to | go to |
| API key | api key, API Key |
| email address | email, e-mail |

### Inclusive language

Replace outdated terms. There are 19+ occurrences of these in the existing docs
and new articles should use the preferred terms from the start.

| Avoid | Use instead | Notes |
|-------|------------|-------|
| whitelist | allowlist | Always replaceable |
| blacklist | blocklist | Always replaceable |
| master (Kubernetes) | control plane | "master node" → "control plane node" |
| master (database) | primary | "master/slave replication" → "primary/replica" |
| slave (database) | replica | |

**Exception — do not change:**
- "master playlist" in HLS/video streaming context — this is the official term from the HLS specification and changing it would be technically incorrect

### Spelling (US English)

| Use (US) | Not (UK) |
|----------|----------|
| behavior | behaviour |
| color | colour |
| center | centre |
| organize | organise |

**Exception:** API identifiers, tag names, and system-generated content that use UK
spelling must be preserved exactly as they appear in the system.

### Avoid mechanical phrasing

Read each sentence aloud. If it sounds machine-generated, rewrite it.

| Mechanical | Natural |
|---|---|
| "all commands run in a terminal window" | "all interaction happens through a terminal window" |
| "no graphical interface exists" | "there is no application to launch" |
| "the installation process completes" | "once installed" |

Avoid noun-verb repetition within two adjacent sentences (e.g., "install" → "installation").

---

## Multi-article updates

### No copy-paste between articles

Each article has its own context and purpose. Adapt content to each article's context.

- **create-* article:** focus on what happens during creation
- **manage-* article:** focus on runtime behavior and limitations

### Cross-reference instead of duplicate

If detailed explanation exists in one article, link to it from others. Do not duplicate the explanation.

### No "Next steps" sections

No `## Next steps` at the end of articles. The sidebar navigation already shows the
full content structure. Use inline cross-links within the article text where the connection is meaningful.

---

## Numbers

- Spell out whole numbers zero through nine in body text: "three regions", "nine nodes"
- Use digits for 10 and above: "10 instances", "128 nodes"
- Always use digits for: measurements, limits, port numbers, version numbers, API values
- Always include a space between a number and its unit: "128 GB", "10 Gbps", "30 s"
- Unit symbols do not take a plural: "10 MB", not "10 MBs"
- Use a comma for numbers with four or more digits: "1,000 requests", "10,000 records"

---

## Capitalization

### Product and feature names — Title Case

Gcore product names and named features always use Title Case, everywhere:

| Title Case (correct) | Lowercase (wrong) |
|----------------------|-------------------|
| Bare Metal | bare metal |
| Virtual Machines | virtual machines |
| Cloud | cloud |
| Video Streaming | video streaming |
| Reserved IP | reserved IP |
| Origin Shielding | origin shielding |
| Object Storage | object storage |

Match the exact capitalization from the Gcore Customer Portal UI and official product pages.

### General capabilities and settings — sentence case

Generic descriptions, page titles, and settings use sentence case:

| Sentence case (correct) | Title Case (wrong) |
|-------------------------|-------------------|
| Create a virtual machine | Create a Virtual Machine |
| Configure logging | Configure Logging |
| Manage your account | Manage Your Account |

### When in doubt

If a term appears capitalized in the Gcore Customer Portal, capitalize it in docs.
If it is a general technical concept, use lowercase.

---

## No section exists only for a link

The following patterns are forbidden:
- "The full parameter list is in the [API reference](...)."
- "Full task management endpoints are in the [API reference](...)."
- "Complete steps are in the [migration guide](...)."

These sentences carry no information beyond the link. Embed the link in a content
sentence, or remove it entirely if no natural content sentence exists.
