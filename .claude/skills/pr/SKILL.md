---
name: pr
description: >-
  Creates a draft GitHub pull request for documentation changes made in the
  current session. Use at the end of a docs workflow when the user asks to open
  a PR, create a pull request, ship the article, or get the changes reviewed.
  Checks gh and git auth, optionally starts a Mintlify local preview, derives
  the product from the file path, uses the ticket branch, stages only the
  session's files, commits with a [Product] message, pushes, and opens a draft
  PR with a What changed, Files changed, and TODO body. Does not edit
  documentation.
---

## HARD RULES — NEVER VIOLATE

- **NEVER commit without explicit user instruction: "commit" or "сделай коммит"**
- **NEVER push without explicit user instruction: "push" or "запушь"**
- **NEVER create a PR without explicit user instruction**
- **NEVER do any git write operation proactively**

Create a draft PR for changes made in the current session.
Always create as draft — the writer reviews the deploy preview before requesting review.

## Scope — read exactly these files

1. This SKILL.md
2. `.agents/references/troubleshooting.md` — if the Mintlify preview shows a blank page or 404

Do not read any other files. All context needed comes from the calling skill's output.

---

## Step 0 — Check prerequisites

Before doing anything else, verify that the required tools are available.

### Check `gh` CLI

```powershell
gh auth status
```

If the command fails or says "not logged in":

> **GitHub CLI is not authenticated.**
>
> To fix this, choose one of:
>
> **Option A — Interactive login (recommended):**
> ```powershell
> gh auth login
> ```
> Follow the prompts. Select HTTPS or SSH, then authenticate via browser.
>
> **Option B — Personal access token:**
> 1. Go to https://github.com/settings/tokens
> 2. Generate a token with `repo` scope
> 3. Set it as an environment variable:
>    ```powershell
>    $env:GH_TOKEN = "your-token-here"
>    ```
>    Or add it permanently via Windows environment variables.
>
> After authenticating, run `gh auth status` again to confirm.

### Check git push access

```powershell
git ls-remote origin
```

If this fails:

> **Git cannot connect to the remote repository.**
>
> To fix this:
>
> **If using SSH (recommended):**
> 1. Check if you have an SSH key: `ls ~/.ssh/id_*.pub`
> 2. If not, generate one: `ssh-keygen -t ed25519 -C "your@email.com"`
> 3. Add the public key to GitHub: https://github.com/settings/keys
> 4. Test: `ssh -T git@github.com`
>
> **If using HTTPS:**
> 1. Git will prompt for credentials on push
> 2. Use a personal access token as the password (not your GitHub password)
>    Generate at: https://github.com/settings/tokens (scope: `repo`)

**Do not proceed until both checks pass.**

---

## Inputs (from the calling skill)

Before creating the PR, confirm you have:

- List of files changed or created
- What was done (summary of changes)
- Any `{TODO:}` items that remain in the draft
- The product area (from the file path)

---

## Step 1 — Local preview (recommended before pushing)

Running the local preview lets the user verify the article renders correctly
before creating a PR. Run it now, then continue with the steps below — do not
wait for it to finish loading.

### Check if Mintlify is installed

```powershell
mintlify --version
```

If the command is not found:

> **Mintlify CLI is not installed.**
>
> Install it once with npm (Node.js required):
> ```powershell
> npm i -g mintlify
> ```
> Node.js download: https://nodejs.org (LTS version)
>
> After installing, run `mintlify --version` to confirm.

### Start the local preview

Run from the repository root (where `docs.json` lives) **in the background** —
do not wait for output, continue immediately with Step 1:

```powershell
# Start in a separate window so it doesn't block
Start-Process powershell -ArgumentList "-NoExit", "-Command", `
  "Set-Location '$($PWD.Path)'; mintlify dev"
```

Mintlify chooses the port automatically (default 3000, increments if taken).
The URL appears in the terminal window that opened. Tell the user:

> Local preview is starting. The URL will appear in the new terminal window
> (usually http://localhost:3000). Navigate to the article you just edited
> to check how it renders. Continue — we'll create the PR in parallel.

---

## Step 2 — Determine the product name

Infer the product display name from the file path. Use this table:

| Folder | Display name |
|--------|-------------|
| `cloud/` | Cloud |
| `cdn/` | CDN |
| `dns/` | DNS |
| `waap/` | WAAP |
| `streaming/` | Streaming |
| `storage/` | Storage |
| `fastedge/` | FastEdge |
| `ddos-protection/` | DDoS Protection |
| `edge-ai/` | Edge AI |
| `hosting/` | Hosting |
| `account-settings/` | Account Settings |
| `developer-tools/` | Developer Tools |
| `reseller-support/` | Reseller Support |
| `.claude/`, `.agents/`, `.cursor/`, `.github/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTRIBUTING.md` | Repo |

If the change spans multiple products, list the two most prominent: `[Cloud, CDN]`.

---

## Step 3 — Determine the branch

Run `git branch --show-current`.

**If the current branch is not `main`,** the skill that did the work already created it. Use it as is and do not create another. There are three formats:

| Work comes from | Branch name | Created by |
|---|---|---|
| A Jira ticket (the default) | The ticket key, for example `DOC-1865` | `full-audit`, `api-use-case`, `api-audit`, or Step 3 below |
| A GitHub issue | `issue/{number}-{short-slug}` | `github-issue` |
| A contributor draft | `feature-draft/{name}` | `feature-draft` |

**If the current branch is `main`,** create the branch with `.\.agents\tools\create_branch.ps1 {name}` using the row of the table that matches where the work comes from. Never use any other pattern (`update/...`, `audit/...`, `new-article/...`). Never run `git checkout -b` by hand.

### If the work is tied to a Jira ticket that does not exist yet — create it first

For Jira-ticket work do not proceed to git operations without a ticket. Use the creation script:

```powershell
python .agents/tools/create_jira_ticket.py --summary "..." --description-file "$env:TEMP\ticket-description.txt" --org-unit <id> --dry-run
```

Take `--org-unit` from `.agents/references/product-routing.md`, Section B. The assignee is the script default and no epic is set unless the user names one.

**Work that is not an article** (agent rules, skills, references, tooling scripts, CI, repository docs such as `README.md`): there is no article path, so no row of Section B matches by prefix. Do not ask the user. Create the Jira ticket with `--org-unit 16038` (Platform/Web) and a summary that describes the work, then name the branch with the ticket key as usual. Use `[Repo]` as the product label in the commit message and the PR title.
Run without `--dry-run` to create the ticket. The script prints the created ticket key — create the branch with `.\.agents\tools\create_branch.ps1 {ticket-key}`.

---

## STOP — Ask the user before any git operations

**Do not run any git commands yet.**

After completing all content changes, report what was done and ask the user for permission to commit and push. Use this exact format:

> Work is complete. Here is what was changed:
>
> - `{file path}` — {what was done}
> - `{file path}` — {what was done}
>
> Proposed branch: `{branch-name}`
> Proposed commit message: `[{Product}] {short description}`
>
> Proceed with commit and push?

**Only after the user explicitly confirms** — run the git operations in this order. The branch already exists from Step 3: confirm with `git branch --show-current` that you are on it. Do not run `git checkout main` or create another branch.

Stage only the files changed in this session — by name, never `git add .`:

```powershell
git add {file1} {file2} {screenshot-paths}
```

Before staging, run `git status` and verify the list. If unrelated files appear
in the working tree — do not stage them. Ask the user if they should be included.

Commit message format: `[Product] Short description`

Rules:
- Imperative mood: "Add", "Update", "Fix", "Draft" — not "Added", "Updated"
- Under 72 characters
- No period at the end

```powershell
git commit -m "[Product] Short description"
git push -u origin {branch-name}
```

**After pushing**, two CI workflows may auto-commit to your branch:
- `sanitize-ai-navigation` — fixes `:` or `#` in `description` frontmatter
- `normalize-images` — moves images into `images/docs/{product}/{article-slug}/` and updates MDX paths

Wait ~30 seconds, then run `git pull` before any follow-up commits.
If you commit without pulling, the push will be rejected with "non-fast-forward".

---

## Step 4 — Create the PR

```powershell
gh pr create --base main --draft --title "[{Product}] {short description}" --body-file "$env:TEMP\pr-body.md"
```

Always `--draft`. Always `--base main`.

**PR title** follows the same format as the commit message:
- Content changes: `[Product] Short description`
- Contributor draft: `[Product] Draft: Feature name`

**PR body** — write to a temp file first, then use `--body-file`:

```markdown
## What changed

{1-3 sentences: what was done and why. Link to Jira ticket or GitHub issue if available.}

Closes #{issue-number}

## Files changed

- `{file path}` — {what was done to it}

## TODO before publishing

{List every {TODO:} item from the draft, as checkboxes.
If no TODOs — write "No TODOs. Ready for review."}

- [ ] {TODO item 1}
- [ ] {TODO item 2}
- [ ] Writer review and approval
```

Add the `Closes #N` line when the PR resolves a GitHub issue from
`G-Core/product-documentation`. Omit it for Jira-only work.

Write the body with the Write tool, then clean up:
```powershell
# After gh pr create runs:
Remove-Item "$env:TEMP\pr-body.md"
```

---

## Step 5 — Report

```
PR created: {URL}
Branch: {branch-name}
Status: Draft

Files staged:
- {file 1}
- {file 2}

{If TODOs exist:}
TODOs in draft ({N} items):
- {TODO 1}
- {TODO 2}

Next step: review the deploy preview, then mark as ready for review.
```

---

## If `gh` is not available

If the `gh` CLI is not installed or not authenticated, provide:

1. The PR title and body as text for copy-paste
2. The URL to open a PR manually:
   ```
   https://github.com/G-Core/product-documentation/compare/main...{branch-name}
   ```
