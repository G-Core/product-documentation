# Finding formats

Shared by Phase 2 (record results), Phase 4 (ticket description), and Phase 5b (structural findings).

## Contents

- VERIFIED OK
- FINDING and categories
- Potentially dangerous technical instructions (UNVERIFIED)
- Jira ticket description

---

## VERIFIED OK format

For every article claim that is confirmed correct in the portal, record it immediately
after testing that claim. Do not skip this step — every element tested must appear in
either a VERIFIED OK block or a FINDING block. This log is the primary output that
the human reads to understand what was actually tested.

```
VERIFIED OK: [what was checked — one line description]
Location: Step N / section "[heading]" / screenshot "[filename]"
Article says: "..."
Portal shows: "..." (matches)
```

Record a VERIFIED OK for every:
- Navigation path confirmed in the portal
- UI label, button name, or field name that matches
- URL schema or hostname format that is still valid
- Screenshot that is visually current (will be retaken in Phase 3 but content is accurate)
- Feature or option that still exists as described

## FINDING format

Record every discrepancy using this format:

```
FINDING: [category]
Location: Step N / screenshot "[filename]" / section "[heading]"
Article says: "..."
Portal shows: "..."
Action needed: [rename / reorder steps / add step / remove step / update screenshot / rewrite / investigate]
```

Categories:
- `UI label mismatch` — button, field, or menu name differs
- `Navigation path changed` — the path to reach the screen changed
- `Step order changed` — steps are in a different order than documented
- `Missing step` — a mandatory step exists in the portal that the article omits
- `Removed step` — the article describes a step that no longer exists
- `Outdated screenshot` — screenshot no longer matches the current portal UI
- `Missing screenshot` — the article has no screenshot but one would help
- `Wrong field name` — a form field has a different label
- `Deprecated option` — an option the article mentions no longer exists
- `New option` — an option exists in the portal that the article does not mention
- `Prerequisite` — a required resource must exist before this step
- `Feature unavailable` — the feature cannot be tested (gated, region, account)
- `Broken flow` — the described action produces an error or unexpected result
- `Missing context` — the article does not explain why a step is needed
- `Unverified procedure` — a technical instruction that may have side effects or may not be
  the standard approach, but cannot be confirmed without SME input

## Potentially dangerous technical instructions

When a step performs an irreversible or high-impact action — for example: re-running an
initialization tool on a running system, purging state files, resetting configuration
modules, or any command that says `clean`, `purge`, `reset`, `wipe`, or `reformat` —
do NOT assume it is wrong, do NOT replace it with an alternative, and do NOT skip it silently.

Record it as:

```
UNVERIFIED: This procedure may have side effects. Technical validation by an SME is
required before changing or publishing it.
Location: [section / step number]
Instruction: [the specific command or procedure verbatim]
Concern: [one sentence describing the potential risk]
```

Do not add this note to the published article. It belongs only in the Jira ticket description (Phase 4). The published text stays as-is
until an SME confirms or corrects the procedure.

---

## Jira ticket description

Write the description to a UTF-8 file and pass it with `--description-file`. Copy the full FINDING blocks verbatim, grouped by category.

```
Regression findings for '{article title}':

{Category 1} ({N})

FINDING 1: {category}
Location: {location}
Article says: "{...}"
Portal shows: "{...}"
Action needed: {...}

FINDING 2: ...
...

{Category 2} ({N})

FINDING 3: ...
```

Example of correct content (do not copy — fill with actual findings):

```
UI label mismatch (2)

FINDING 1: UI label mismatch
Location: Filter list, bullet 1
Article says: "ID (resource name)"
Portal shows: "Resource name"
Action needed: Rename filter

FINDING 2: UI label mismatch
Location: Opening sentence
Article says: "Gcore Edge Cloud"
Portal shows: navigation is under Cloud Management > User Actions
Action needed: Replace with "Gcore Customer Portal"

Missing step (1)

FINDING 3: Missing step
Location: Article opening — no navigation path given
Article says: (nothing)
Portal shows: Navigation path is Cloud Management > User Actions
Action needed: Add navigation instructions
```

Dry run first:

```powershell
python .agents/tools/create_jira_ticket.py --summary "Update {article title}" --description-file "$env:TEMP\ticket-description.txt" --org-unit {jira_org_unit} --dry-run
```

Show the dry-run output to the user, then run without `--dry-run` immediately
after — do not wait for separate confirmation unless the user objects.

```powershell
python .agents/tools/create_jira_ticket.py --summary "Update {article title}" --description-file "$env:TEMP\ticket-description.txt" --org-unit {jira_org_unit}
```
