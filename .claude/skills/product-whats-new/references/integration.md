# Integration into Claude Code documentation workflows

A skill's description may trigger automatic use when Claude Code recognizes the task, but a skill **cannot guarantee** a post-task check by itself. Add a mandatory call to the existing parent article workflow, or add the following instruction to the repository's `CLAUDE.md`:

> After completing each documentation ticket, article update, or documentation PR review, invoke the `product-whats-new` skill in **Triage** mode using the ticket context and before/after diff. Record `Include`, `Skip`, or `Needs verification` in the approved persistent register. If the behavior was used on a production account and it worked, customers already have it: decide `Include` or `Skip`, and do not mark `Needs verification` because a Jira status is still open. Report the one-line decision in the task summary. Do not edit public What's new pages unless explicitly asked to publish.

For Claude Code, place the skill folder at `.claude/skills/product-whats-new/` (project scope) or `~/.claude/skills/product-whats-new/` (personal scope). Confirm skill discovery with Claude Code in the target project.

When an existing agent processes multiple tickets in one session, run triage after **each** ticket, not once at session end. If a task touches several pages about the same product change, triage once for that **underlying event** and link all relevant pages. Do not create separate candidates per file.

A periodic audit is optional and should be requested explicitly: inspect completed tickets since the last audit, identify missed candidate events, and reconcile with existing records. The audit does not automatically publish.

If the parent workflow uses orchestration bricks, put the triage invocation immediately after article validation and before the ticket is marked done; do not let a new candidate block the main task unless the task itself requires release verification.
