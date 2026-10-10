# Jira ticket and feature branch

Used by skills that edit articles. The ticket comes first, the branch second, and every edit lands on the ticket branch, never on `main`.

## If a Jira ticket already exists

Use that ticket key. Do not create a duplicate. Check out the existing branch (or create it from `main` if it does not exist yet).

## Create the ticket

Use the script in this repository. For a long description, write it to a UTF-8 file in `$env:TEMP` and pass `--description-file` instead of `--description`:

```powershell
python .agents/tools/create_jira_ticket.py `
  --summary "..." `
  --description-file "$env:TEMP\ticket-description.txt" `
  --org-unit <id>
```

Add `--dry-run` to print the fields without creating the ticket.

Resolve `--org-unit` from `.agents/references/product-routing.md`, Section B, by article path prefix (longest match). The assignee is always the documentation writer (the script default). Do not set an epic or a "relates to" link unless the user names one for the current batch: epics are temporary.

Description uses Jira wiki markup (`h3.` headings, `{{path}}` for monospace). Include the article path, what the work covers, and what was live-tested.

Report the created ticket key and URL to the user.

## Create the feature branch immediately after the ticket

```powershell
.\.agents\tools\create_branch.ps1 DOC-XXXX
```

Replace `DOC-XXXX` with the ticket key just returned by the script. The helper checks out `main`, pulls, and creates the branch named exactly as the ticket key.

All subsequent file edits go on this branch. Never write on `main`. Proceed without asking for confirmation.

## Commit and push

Do not commit or push until the user says one of: коммить / коммит / commit / пуш / пушь / push / закоммить / запушь. Then commit only the files changed in this session (never `git add .`), push the existing ticket branch, and load the `pr` skill if the user also asked for a PR. Never push to `main`.
