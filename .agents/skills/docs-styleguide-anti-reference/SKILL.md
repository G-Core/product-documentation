---
name: docs-styleguide-anti-reference
description: Prevent technical documentation from drifting into Wikipedia-like, reference-heavy, UI-inventory prose. Use when reviewing or rewriting how-to, setup, manage, configuration, or troubleshooting articles that feel encyclopedic, obvious, field-by-field, tab-by-tab, or insufficiently task-oriented.
---

# Anti-reference style guide

Use this as a narrow extension to the main documentation style guide.

## Core rule

Do not turn a task article into a reference article.

A how-to or manage article should move through the user's task, decisions, actions, consequences, and observable result. Do not systematically explain every concept, field, tab, setting, or UI element merely because it exists in the source material.

## Reject these patterns

**Wikipedia opening:** `X is...` followed by definitions, properties, use cases, and alternatives before the task begins.

**UI inventory:** article structure mirrors the interface: Volumes tab, Access tab, Power tab, Networking tab.

**Field inventory:** every form field becomes its own step or definition. Do not automatically document a form as a list of `Field — description` entries. This turns a task into reference documentation and often explains information already visible in the UI. Mention a field only when the user needs guidance to choose its value, understand a non-obvious consequence, or complete the task. Describe related fields together as part of the user's action instead of defining each control separately.

- Bad: `Name — unique identifier...`, `Security Groups — optional firewall rules...`
- Better: `Select the network and subnetwork to connect to, and optionally assign security groups.`

This anti-pattern appears at three levels: **UI inventory** (article structure mirrors tabs), **tab inventory** (section structure mirrors sub-tabs or panels), **field inventory** (prose mirrors form fields). All three share the same root cause: documenting what is visible instead of what the user does.

**Heading -> definition:** `### SSH keys` followed by `SSH keys authenticate...`; `### Volumes` followed by `Volumes provide...`.

**Button-stop procedure:** a section ends with `Click Add...` even though that button only opens the real workflow.

**Obvious explanation:** prose restates what the control label already tells the reader.

**Capability inventory:** every section independently describes an object, control, status, or available operation — structured as "here is the VM, here is everything you can do with it." Reference-like writing is not only `Term — definition`. It also appears at the section level when the article is organized around what the product offers rather than what the user is trying to accomplish.

In task-oriented documentation, connect information around a user situation or decision. Prefer prose that answers "what should I do in this situation?" over inventories of "what options exist?" Tables and bullet lists should be used when comparison itself is the task, not as the default way to document every set of options.

- Bad: `Attach storage → list available storage actions` / `Power → table of lifecycle actions` / `Networking → list interface actions`
- Better: `Need more storage → add or reuse a volume` / `Need to interrupt a workload → choose pause, stop, or reboot based on consequence` / `Need another network path → attach an interface`

**Source-dump completeness:** every available fact is included even when it does not help complete the current task.

## Prefer

Organize around what the reader is trying to accomplish, not around nouns in the UI.

Prefer:

- `Attach storage` over `Volumes tab`
- `Access the instance from the console` over `Access tab`
- `Stop, pause, or restart` over `Power tab`
- `Connect to a network` over separate definitions of Network, Subnetwork, Floating IP, and Security Group

Explain only information that affects a choice, prevents an error, changes the outcome, or helps verify success.

## Three checks before approving text

**UI inventory test:** If the outline could be recreated by reading the UI from top to bottom, restructure it.

**Button test:** If `Click X` only opens another dialog or workflow, continue until the user's task is actually complete.

**Necessity test:** If removing an explanatory sentence would not change what the reader chooses, does, avoids, or verifies, remove it or move it to reference/concept documentation.

## Put context before instruction

Do not default to imperative-first writing. Before telling the reader what to click, select, use, or configure, provide the information they need to understand the action or choose between alternatives.

Prefer **context → distinction or consequence → action** over **command → explanation of why the command makes sense**.

- Bad: `Use **Pause** when the workload must be suspended without releasing its allocated resources. Use **Stop** when the VM no longer needs to remain on the current host.`
- Better: `**Pause** suspends the instance while keeping its allocated resources reserved. **Stop** shuts it down and releases those resources; when started again, the instance may run on a different host. **Soft reboot** restarts the guest OS without changing the host.`

- Bad: `Click **Add Volume** and select **Data Volume** to create a new empty disk.`
- Better: `Additional storage can be provided by creating a new data volume or reusing a previously detached volume. Both options are available under **Volumes** → **Add Volume**.`

Do not invent a motivation merely to avoid an imperative opening. If the source does not establish why or when a feature is used, introduce what the feature does or the choice it provides instead.

Do not force this pattern onto every sentence. Direct commands are appropriate once the reader already has enough context and is performing the procedure.

**General principle: explain before you instruct when the explanation is necessary to make the instruction meaningful.**

Do not open an article or section with navigation unless navigation itself is the task. Introduce the purpose or available capability first, then tell the reader where to access it.

## Do not invent user intent to avoid reference-style prose

Task-oriented writing does not mean inventing a problem for every feature. If the source says only that a capability exists, describe it plainly. Do not fabricate a scenario — "when SSH is unavailable", "useful for troubleshooting", "for recovery" — unless that use case is explicitly documented or verified.

Invented intent is harder to maintain, misleads users about when to use a feature, and is not more helpful than a neutral description.

- Bad: `If SSH or network access is unavailable, the browser console provides direct access...`
- Better: `You can access the instance directly through a VNC session in your browser.`

Task-oriented != every feature must have a manufactured problem it solves.

## Mechanical action openings

Do not start every task section with a UI command such as `Open`, `Click`, `Select`, or `Navigate`. Repeated imperative openings make documentation feel mechanical and disconnected.

Start with the user situation, intent, or consequence when it helps connect the section to what came before. Then introduce the UI action naturally.

- Bad: `Open **Access** and click **Launch console**.`
- Better: `If SSH is unavailable, use the browser console to access the instance directly. In **Access**, click **Launch console**.`

- Bad: `Open **Networking** and click **Add Interface** when the VM needs connectivity to another network.`
- Better: `Additional interfaces let the VM connect to another private network or subnet. Add one from **Networking** with **Add Interface**.`

Do not force a bridge into every section. Use it when the section would otherwise begin as an isolated UI instruction. Vary sentence structure and read consecutive section openings together — if several begin with the same verb or pattern, rewrite them.

**Do not treat each section as an independent mini-procedure. Read the article top to bottom and make neighboring sections feel like parts of one document.**

## Examples

Consult [references/examples.md](references/examples.md) when this anti-pattern appears. Add new real examples there over time instead of expanding this file.
