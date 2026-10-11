# Phase 10 — Send to review

Run this phase only after the user has confirmed the commit and push (Phase 9).
Do not run Phase 10 automatically — wait for the user to trigger it explicitly or to say "коммить/пуш/commit/push".

The Jira ticket was already created in Phase 4. This phase only transitions it
to In Review and records the completion.

## Step 1 — Transition to In Review and post comment

Run `.agents/tools/send_to_review.py` with the ticket key, the branch, and the article path:

- `--ticket` — the key created in Phase 4, for example `DOC-1514`
- `--branch` — the branch created in Phase 4, same as the ticket key
- `--article-path` — path from `docs.json`, no leading slash, no `.mdx`,
  for example `hosting/virtual-servers/order-a-virtual-server`

The script will:
1. Transition the ticket: To Do → In Progress → In Review
2. Post a comment: `Please review` + the Mintlify branch preview URL

Mintlify preview URL template:
```
https://gcore-doc-{branch-number}.mintlify.app/{article-path}
```

Where `{branch-number}` is the numeric part of the branch name
(e.g. branch `DOC-1514` → number `1514`).

Dry run first:

```powershell
python .agents/tools/send_to_review.py --ticket DOC-1514 --branch DOC-1514 --article-path {article-path} --dry-run
```

Run without `--dry-run` immediately after — do not wait for separate confirmation unless the user objects:

```powershell
python .agents/tools/send_to_review.py --ticket DOC-1514 --branch DOC-1514 --article-path {article-path}
```

To move the ticket to Blocked instead, add `--blocked "reason"`.
