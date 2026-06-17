---
name: pr
description: Create a draft GitHub pull request after documentation changes are complete. Use when the user confirms they want to open a PR.
---

Create a draft PR for changes made in the current session.
Always create as draft — the writer reviews the deploy preview before requesting review.

## Scope — read exactly these files

1. This SKILL.md

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
  "Set-Location 'C:\Projects\product-documentation'; mintlify dev"
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

If the change spans multiple products, list the two most prominent: `[Cloud, CDN]`.

---

## Step 3 — Ensure main is up to date and create branch

```powershell
cd C:\Projects\product-documentation
git checkout main
git pull origin main
git checkout -b {branch-name}
```

**Branch naming:**

| What was done | Branch name |
|---------------|-------------|
| New article | `new-article/{product}-{slug}` |
| Added API tab | `api-tab/{product}-{slug}` |
| Updated article | `update/{product}-{slug}` |
| Audited article | `audit/{product}-{slug}` |
| Feature draft (contributor) | `feature-draft/{ticket-id-or-slug}` |

Where `{slug}` is the article filename without `.mdx`.

**If branch already exists** — do not reuse it. Delete and recreate:
```powershell
git branch -D {branch-name}
git checkout -b {branch-name}
```

---

## Step 4 — Stage and commit

Stage only the files changed in this session — by name, never `git add .`:

```powershell
git add {file1} {file2} {screenshot-paths}
```

Before staging, run `git status` and verify the list. If unrelated files appear
in the working tree — do not stage them. Ask the user if they should be included.

Commit message format: `[Product] Short description`

```powershell
git commit -m "[Cloud] Add REST API tab to create-an-instance article"
git commit -m "[CDN] Update origin group configuration steps"
git commit -m "[Cloud] Draft: GPU cluster auto-scaling feature"
```

Rules:
- Imperative mood: "Add", "Update", "Fix", "Draft" — not "Added", "Updated"
- Under 72 characters
- No period at the end

---

## Step 5 — Push

```powershell
git push -u origin {branch-name}
```

**After pushing**, two CI workflows may auto-commit to your branch:
- `sanitize-ai-navigation` — fixes `:` or `#` in `ai-navigation` frontmatter
- `normalize-images` — renames images and updates MDX paths

Wait ~30 seconds, then run `git pull` before any follow-up commits.
If you commit without pulling, the push will be rejected with "non-fast-forward".

---

## Step 6 — Create the PR

```powershell
gh pr create --base main --draft --title "[{Product}] {short description}" --body-file /tmp/pr-body.md
```

Always `--draft`. Always `--base main`.

**PR title** follows the same format as the commit message:
- Content changes: `[Product] Short description`
- Contributor draft: `[Product] Draft: Feature name`

**PR body** — write to a temp file first, then use `--body-file`:

```markdown
## What changed

{1-3 sentences: what was done and why. Link to Jira ticket if available.}

## Files changed

- `{file path}` — {what was done to it}

## TODO before publishing

{List every {TODO:} item from the draft, as checkboxes.
If no TODOs — write "No TODOs. Ready for review."}

- [ ] {TODO item 1}
- [ ] {TODO item 2}
- [ ] Writer review and approval
```

Write the body with the Write tool, then clean up:
```powershell
# After gh pr create runs:
Remove-Item /tmp/pr-body.md
```

---

## Step 7 — Report

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
