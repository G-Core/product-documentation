---
name: technical-landing-pages
description: >-
  Writes, rewrites, and reviews Gcore documentation landing pages: product
  overviews, API reference overviews, and developer landing pages. Use when
  creating or editing a docs landing or overview, including api-reference
  product pages, or when asked to check one. Not for how-to articles, generated
  API method pages, or pages on the gcore.com marketing site.
---

# Technical landing pages

Use this skill for a landing page in this documentation repo. Three kinds of page exist, and they do not share one outline.

This skill does not cover the public marketing site. A product page on gcore.com has a different job and different rules.

The style guide and the MDX rules still apply. This skill decides what a sentence is allowed to say.

## The failure to prevent

The agent replaces an explanation of what the reader can do with a retelling of the page. Sidebar labels become sentences. A definition repeats the term it defines. An endpoint is credited with the work the product does.

If a sentence would still be true after the names were swapped for any other product, delete it.

## Principles

1. **Purpose before structure.** First say why the product or API exists and which task the reader is trying to complete. Do not retell the table of contents.
2. **Capabilities, not keywords.** Describe real actions. Do not join section titles into a sentence.
3. **Meaningful distinctions.** When two groups have similar names, explain the difference. Do not write a circular definition.
4. **Information density.** Every sentence adds a fact about purpose, capability, or how two resources relate. A sentence that only repeats the heading or a navigation label comes out.
5. **Technical accuracy.** Do not attribute the product's job to the endpoints. The service filters traffic. The API registers a network, turns protection on, and reads events.
6. **Natural transitions.** A section opening helps the reader see a relationship. A stock sentence that could sit above any list comes out.

These principles are not a template. Do not copy one landing's headings onto another.

## API reference overview

Apply the following rules to an API reference overview. Do not apply them as a pattern for a product overview or a developer landing page.

Write API overview introductions around what developers can accomplish, not around the names of endpoint groups.

Do not turn the sidebar structure into a sentence by listing resource names. Describe meaningful API operations using accurate verbs and objects.

Avoid circular definitions, such as "profiles are protection profiles" or "templates are templates used to create profiles."

Every sentence must add information that helps the reader understand the API's purpose, capabilities, or resource relationships. If a sentence merely repeats the heading or navigation labels, remove it.

Keep introductions short. Do not add generic marketing language or explanations that belong in individual endpoint references.

Also for this kind of page:

- State the base URL. Do not repeat authentication, rate limits, SDKs, or Terraform. Those stay on the shared API overview.
- Do not add a sentence that sends the reader to the product guide by repeating the product name ("Product setup is in FastEdge").
- Link a sidebar group only when the words after the link say what the caller does there. The link text may be the group name. The explanation may not be the group name said again.
- A group has no page of its own. Link an operation that opens that group. Do not invent a group URL.
- Take verbs and objects from the operation summaries in the spec. Do not describe an operation the spec does not contain.

## Product overview

The reader is choosing where to go in the product documentation.

Open with what the product does. Link to the how-to articles that complete a task. The clause after a link says what the reader gets done there, not a paraphrase of the article title.

Use the overview shape in `.agents/references/content-types.md` (Type 4). These principles override any habit of listing the folder names.

## Developer landing

The reader is choosing a tool and making a first call.

Open with which job each tool is for: call the API, manage infrastructure as code, or connect an agent. Do not open with the names of the folders.

## Modes

Pick one mode. Do not mix them.

### Write

1. Name the kind: API reference overview, product overview, or developer landing. If the page is a how-to, stop and use the article skill instead.
2. Read `.agents/references/style-guide.md` and `.agents/references/mdx-rules.md`. Read one published landing of the same kind, to judge depth. Do not copy its headings or its sentences.
3. For an API reference overview, read the tag list and the operation summaries in the product spec. Confirm a distinction from those summaries before writing it.
4. Write the page. Show it.

### Rewrite

1. Read the page. Mark every sentence that only repeats a heading, a sidebar label, or a list of keywords.
2. Replace a marked sentence with a capability, a relationship, or a distinction. If it cannot carry new information, delete it.
3. Do not add detail that belongs on a single endpoint page.
4. Stay in the same kind. Do not turn a product overview into an API map, or the reverse.

### Review

Do not edit the page. Report each problem by quoting the sentence and saying which principle it breaks. Name the missing fact when a distinction or a capability was replaced by a label.

Check for:

- A sentence that restates the contents or the sidebar
- A circular definition
- An endpoint credited with the product's job
- A section opening that could be pasted above any list
- Two similarly named groups with no difference stated
- Marketing language, or a detail that belongs on a method page

## Examples

Bad: `DDoS Protection endpoints guard networks with profiles, announces, and event logs.`

The endpoints do not guard anything. The sentence is a list of group names.

Good: `Put a network under protection, select the rules that drop traffic, and read what was blocked.`

Bad: `Profiles are the protection profiles created on the account, and Templates are what those profiles are created from.`

Good: `An account can activate its own rule set. A protected network uses a different rule set, built from a different starting configuration.`

Bad: `Authentication, rate limits, SDKs, and Terraform are in the API overview. Product setup is in FastEdge.`

The first sentence points away for topics this page does not need to introduce. The second repeats the product the reader is already in.
