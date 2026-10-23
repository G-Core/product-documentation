---
name: technical-landing-pages
description: >-
  Writes, rewrites, and reviews Gcore documentation landing pages: product and
  section overviews, API reference overviews, and developer landing pages. Use
  when creating or editing a docs landing or overview, including api-reference
  product pages and a section landing such as Account settings or CDN, or when
  asked to check one. Decides whether the model needs a separate concept
  article. Show the design and wait for approval before writing any page text.
  Not for how-to articles, the concept article itself (use write-from-scratch),
  generated API method pages, What's new pages, or pages on the gcore.com
  marketing site.
---

# Technical landing pages

One skill covers every documentation landing page in this repo. Three kinds of page exist, and they do not share one outline.

This skill does not cover the public marketing site, a how-to article, or a What's new page. A how-to uses the article skill. What's new uses `product-whats-new`.

The style guide and the MDX rules apply when writing, with the landing exceptions in `references/landing-writing.md`. This skill decides what a sentence is allowed to say, and the sequence comes from the approved design.

## The failure to prevent

The agent describes the documentation instead of the system the documentation covers. Sidebar labels become sentences. A definition repeats the term it defines. An endpoint is credited with the work the product does. A card stacks true facts that do not connect, or explains one term through another so that only an expert can follow it.

If a sentence would still be true after the names were swapped for any other product, delete it.

## Principles

1. **Model before navigation.** Explain the concepts, relationships, and boundaries the reader needs before opening the child articles. The sidebar already lists those articles. Keep only the part of the model that the navigation needs. A longer explanation belongs in a concept article.
2. **Distinctions, not keywords.** When two areas have similar names, say how they differ. Do not join section titles into a sentence, and do not write a circular definition.
3. **Information density.** Every sentence adds a fact about the subject, a capability, or how two things relate. A sentence that only repeats a heading or a navigation label comes out.
4. **Technical accuracy.** Do not invent product behavior, and do not attribute the product's job to the endpoints. Take API claims from the spec. Take product claims from the child articles, and leave out a claim that one article makes and another contradicts.
5. **Connected sentences.** Each sentence sets up the next. Two facts side by side do not make a thread. Do not announce navigation that is already clear.
6. **Task before term.** The reader is mid-level: they know the generic concept but not the Gcore names. Say what the reader can do or gets, then name the feature.

These principles are not a template. Do not copy one landing's headings, order, or sentences onto another.

For every fact proposed for the page, ask: does this help the reader understand the subject or choose where to go next? If it does not, it belongs elsewhere.

## Procedure

Use the same phases for a new page and for a rewrite. Do not skip to prose because the request said "write" or "rewrite".

### 1. Analysis

Do not draft the page.

Name the kind: product or section landing, API reference overview, or developer landing.

Read the sources for that kind. Do not design from titles.

- **Product or section landing.** Read `docs.json` for the group, then read the child articles. Recover the model: ownership, scope, relationships, dependencies, permissions, and operational consequences. Look for an existing overview or concept article that already holds part of the model. Do not assume the product menu explains those relationships.
- **API reference overview.** Read the tag list and the operation summaries in the product spec. Confirm every distinction from those summaries.
- **Developer landing.** Read the pages for the tools this landing has to distinguish.

For a product or section landing, also collect the terms. For each key entity (who requests the content, what holds the originals, the main features), note the word each child article uses and the word the interface uses, and mark where they disagree. The naming rules are in `references/landing-writing.md`, section Terms.

Separate what the reader must understand on the landing from detail that belongs in a child article or on one operation. Record gaps in the source and contradictions between child articles, and report them. Do not fix them on the landing, and do not repeat a contradicted claim.

### 2. Design

Show the scheme in the chat. Do not draft sentences, cards, or MDX.

For a product or section landing, show:

- **Product model.** The concepts and boundaries, in a few statements.
- **Landing responsibility.** What the reader learns here, and what stays in each child article.
- **Split.** Whether the model needs a separate concept article (see Split below), and what stays on the landing if it does.
- **Terms.** The word chosen for each key entity, and each conflict between articles that has no rule yet. Ask the user about those conflicts, and do not decide them.
- **Exclusions.** Related material that does not belong, and why. Do not promise a section that has no article. A topic that fits no card is a sentence, not a card.
- **Sequence.** The order of explanations, interface context, and navigation, and why this subject needs that order.
- **Navigation.** One responsibility per card or link. If cards are the wrong presentation, say what to use instead.
- **Open choices.** Decide for this page, and say why. Choose a visual by the reader's task: a diagram for relations or a path, a table only when the reader makes a real choice, a card for an entry point, a screenshot when the interface must be seen. "It fits in text" is not a reason to skip a visual. Say where the visual lives so it is not repeated on two pages. Account settings and CDN are cases, not defaults.
- **Gaps.** Facts the child articles do not support or contradict. Leave them out.

For an API reference overview, show what the introduction establishes, each group that earns a sentence (the operation, the distinction, and what the sentence will not claim), and what stays off this page.

For a developer landing, show the job each tool is for.

### Stop

After the design, stop. Wait until the user approves that scheme in a later message.

Asking for the landing is not approval of the scheme. A correction to the scheme is not permission to write. Show the revised scheme and stop again.

### 3. Writing

Start only after the user has approved the scheme.

Follow `.agents/references/ticket-and-branch.md`: use the Jira ticket the user named, or create one, then create its branch with the helper. Every edit lands on that branch.

Read `.agents/references/style-guide.md`, `.agents/references/mdx-rules.md`, and `references/landing-writing.md` in this skill's folder. Read one published landing of the same kind to judge depth. Do not copy its headings or its sentences.

Write only what the approved scheme contains. Then apply the kind rules below. A landing's `title` and `sidebarTitle` are both `Overview`. When the user dictates a sentence, put it in as written and report any conflict with the style guide afterwards.

When the new page is not in `docs.json`, add it to the correct group after reading the sibling entries, and show the change to the user.

Validate before showing the page. Run the four tools from `.agents/references/review-process.md`, Step 1, on the page and fix every real violation. The checker marks three kinds of flag on a landing as a possible false positive: a sentence-initial "For example,", a measured use of "you", and a number inside a JSX attribute (`references/landing-writing.md` explains why). Show those flags to the user, who decides which to fix. Do not ignore them and do not fix them on your own. Confirm `description` is one sentence, 140 characters maximum, ASCII only, without `{ } / : #`, and does not name Portal, API, or Terraform. Then reread every sentence against the failure to prevent, the "Do not write" list for the kind, and the checks at the end of `references/landing-writing.md`.

Show the page and the file path. Do not commit, push, or open a PR unless the user asks.

### 4. Moves log

When the work touched more than the landing (a split, a moved sentence, an edited neighbor), finish with a short list: each file changed, what moved from where to where, which links were added or removed, and which statements were left out and why. Put the same list in the ticket description.

### Review

If the user asked only to review, do not edit. Read the page and the same sources as in analysis. Quote the sentence and name the principle it breaks. Name the missing fact when a label replaced a distinction.

## Split

A landing gives direction. A concept article explains how the system works. Decide which the material needs, by the reader's task and not by length.

- Keep the explanation on the landing when it fits the cards: one definition and the boundaries the cards state.
- Write a concept article when the reader needs an independent explanation, for example how a request travels through the product, that the cards cannot carry. The landing then keeps one definition and links to the article from a sentence that states a fact.
- Check first whether an existing overview or concept article holds that material. Rework it before writing a new one.

The concept article is a separate task for `write-from-scratch` (Type 5 in `content-types.md`). This skill decides whether it is needed and what stays on the landing, and records the split in the moves log. When the user approves the split, both pages may be handled in one session and on one ticket.

## Product or section landing

A landing introduces an area by explaining the concepts, relationships, and boundaries readers need before they explore its documentation. Navigation reflects those distinctions.

The reader is choosing where to go. Open with what this area is responsible for. Do not open on a secondary concept before saying why it matters. Do not open with a promotional claim.

Then explain the model that makes the navigation meaningful. The model can be short. Its job is explanation.

Include an access instruction or a screenshot only when the approved design says the reader must see the interface to understand the area. Other landings need neither.

A paragraph after a screenshot must add a relationship. It must not announce that cards follow.

Each card or link explanation has one subject. Supporting sentences clarify that subject, distinguish it from a neighbor, or state a limit that changes where the reader goes. Do not give every card the same shape or length. Cards are not miniature child articles, and they are not a feature inventory. The writing rules for cards, leads, lists, links, and titles are in `references/landing-writing.md`.

Do not write:

- The page title repeated as a definition that adds nothing
- The same features the cards already name
- A "central place" for a list of activities
- A hypothetical reader invented to lengthen the introduction
- "The sections below provide instructions..." or any announcement of the next block
- "Whether you're doing X or Y..."
- Vague claims about workflows or day-to-day work
- Requirements, plan notes, or limits that the child article owns

Detailed procedures and exhaustive feature lists stay in the child articles.

### Cases, not templates

Account settings needed a model the menu does not show: a login is a person; an account holds services, billing, and users; one login can reach several accounts; the portal works in one account at a time; some settings are personal and some affect other people. The page put the access instruction and one screenshot before the cards, because the reader had to see the Profile menu before the personal-versus-account distinction made sense.

CDN needed a different treatment: the model was a path (user, edge cache, origin), which a diagram explains better than cards, so it moved to a concept article and the landing kept one definition, one entry card for the first step, grouped cards for settings, and plain lists for the rest. Video did not fit any card, so it became one sentence under the entry card. Its card text is in `references/landing-writing.md` as calibration.

Do not reuse either page's order, cards, or sentences on another product.

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

## Developer landing

The reader is choosing a tool and making a first call.

Open with which job each tool is for: call the API, manage infrastructure as code, or connect an agent. Do not open with the names of the folders.

Then separate the tools by the situation that picks one. Say what the reader controls with each tool and what it leaves to another. Tools overlap in what they can create, so the distinction is the job and the workflow, not the resource list. Take every tool claim from that tool's own pages. Do not claim parity between tools unless those pages show it.

Point each tool to the page where the first call or first apply happens. One tool gets one link and one reason to choose it. Do not write a step of the first call here.

Do not write:

- A feature list for each tool
- "Powerful", "flexible", or any other quality claim
- Authentication, rate limits, or pagination details that the REST API pages own
- A tool the repo has no page for

For a review, quote each sentence that names a tool without saying when to choose it, and name the missing distinction.

## Examples

Bad: `DDoS Protection endpoints guard networks with profiles, announces, and event logs.`

The endpoints do not guard anything. The sentence is a list of group names.

Good: `Put a network under protection, select the rules that drop traffic, and read what was blocked.`

Bad: `Profiles are the protection profiles created on the account, and Templates are what those profiles are created from.`

Good: `An account can activate its own rule set. A protected network uses a different rule set, built from a different starting configuration.`

Bad: `Authentication, rate limits, SDKs, and Terraform are in the API overview. Product setup is in FastEdge.`

The first sentence points away for topics this page does not need to introduce. The second repeats the product the reader is already in.

Bad: an Account settings introduction that lists profile, account, billing, users, API tokens, and notifications.

Those are the sidebar. The reader still cannot tell the areas apart.

Good: a login identifies the person, and the account holds the services, billing, and users. That difference is what makes the later sections distinct.
