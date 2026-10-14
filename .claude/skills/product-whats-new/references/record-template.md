# Candidate record format

Use one file per underlying product event under `.whats-new/candidates/`. The file is internal workflow metadata, not a public release note.

```md
---
product: Streaming
status: Needs verification # Include | Skip | Needs verification | Published
release_date: unknown # ISO date only if confirmed
published_page: null
---

# Multi-codec VOD transcoding

Customer change: [What became possible or changed; do not speculate]
Affected users: [Who and under what conditions]
Release evidence: [ticket/release link and exact evidence; or "not verified"]
Open verification: [Precisely what is missing]
Source tickets/PRs: [links or IDs]
Documentation links: [specific internal MDX paths]
Duplicate check: [existing What's new entry or "not found"]
Published entry: [heading if published]
```

For an `Include` record, `Release evidence`, `Customer change`, `Affected users`, and `Documentation links` must be concrete. A successful check on a production account is release evidence: customers already have the behavior, so the decision is `Include` or `Skip`, not `Needs verification`. Do not hold that record because a Jira status is still In Progress or because the resolution date is empty. An unknown release date means hold as `Needs verification` only when the behavior was not seen working on a production account and no other authoritative source confirms that customers can use it.
