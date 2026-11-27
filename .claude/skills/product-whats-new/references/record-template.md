# Candidate record format

Use one file per underlying product event under `.whats-new/candidates/`. The file is internal workflow metadata, not a public release note.

```md
---
product: Streaming
status: Include # Include | Published
changed_on: unknown # ISO date from the PR or the developer release. Not the day the page was opened.
published_page: null
---

# Multi-codec VOD transcoding

Entry: [The finished What's new paragraph. The weekly report pastes this and does not rewrite it.]
Source tickets/PRs: [the pull request and the developer ticket]
Documentation links: [specific internal MDX paths]
Duplicate check: [existing What's new entry or "not found"]
Published entry: [heading if published]
```

Write this file in the same session as the pull request, from the PR diff and the article. `Entry` is the public text. Do not leave a summary for another agent. If the diff is not a new feature or a critical change, do not create the file.
