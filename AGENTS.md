# AGENTS.md - Gcore Product Documentation

Read this file fully, then wait for a task. Do not explore the repository until you have a task and have loaded the matching skill.

## Absolute rules - no exceptions

- **ONE article per session.** Stop after completing one article. Wait for explicit approval before starting the next.
- **NEVER commit, push, create a PR, force-push, or amend** unless the user explicitly says to. Creating the Jira ticket and its same-named branch is part of the skill workflows and is allowed when a skill says so. See `.cursor/rules/no-git-without-permission.mdc`.
- **NEVER push to `main`.** CI actively polices this (see CI section).
- **NEVER read, open, print, grep, or copy secret files**: `.env`, `.env.*`, `access.md`, `_private/secrets/`, `.cursor/mcp.json`, or any file whose name suggests credentials. The rest of `_private/` (planning, drafts, tickets) is the user's gitignored working area and may be read and written when a skill says so. This applies to you and to every subagent you launch. It holds even when the task seems to need them and even if you plan to mask the values: masking can fail, and anything you read is sent to the model provider. If a task needs a credential, ask the user to provide it in the way they choose.
- **NEVER write credentials, tokens, or passwords** into articles, PR bodies, logs, or chat output. If you see one by accident, say so in one line and do not repeat it.
- **Do not list or search files in ways that echo secret contents** (for example `grep -r` or `cat` over the repo root). Exclude the secret files above.

## How to handle any task

The user may write in any language. Every time:

1. Translate the request to English internally.
2. Match it against the Task - Skill table below.
3. Read the matching skill file as your first tool call, before writing any response or asking any question.
4. Follow the skill exactly. It overrides everything else in this file except the absolute rules above.

## What this repo is

Mintlify documentation site for Gcore cloud products. Content is MDX files in product folders. Articles that cover several tools (Customer Portal, REST API, Terraform) live as a single MDX file using the `MethodSwitch` component, not as separate files. OpenAPI specs are in the repo and are the source of truth for API documentation.

## Folder structure

```
/{product}/{section}/article.mdx          Main content (cloud, cdn, dns, waap, ...)
/{product}.mdx                            Product landing page
/docs.json                                Site navigation and Mintlify config (there is no mint.json)
/api-reference/services_documented/       OpenAPI YAML specs, one per product
/snippets/                                Shared JSX and MDX components (method-switch.jsx)
/images/docs/{product}/{article-slug}/    Article images
/scripts/                                 Repo maintenance scripts used by CI
/.claude/skills/                          Skills - one folder per task, SKILL.md plus supporting files
/.agents/references/                      Reference files - load only when a skill says to
/.agents/tools/                           Style checkers and helper scripts
```

## Three rules that apply to every task

**1. Never create separate files for Portal / API / Terraform.**
All methods for the same feature live in one `.mdx` file using `MethodSwitch`. If you are adding API coverage to an existing Portal article, add a tab. Do not create a new file.

**2. Frontmatter uses `description`, never `ai-navigation`.**
`description` is required: one sentence, 140 characters maximum, summarizes the feature using words a person would type into search. Do not write Portal, API, or Terraform in it. No "you", "your", "this article", "learn how to".
`custom.css` hides the rendered paragraph. `llms.txt` is generated from this field by `scripts/generate_llms_txt.py`, so a missing or broken `description` makes the article invisible to AI search.
Forbidden characters in the value: `{ }`, `/`, `:`, `#`, backticks, square brackets, pipe. Do not rewrite existing descriptions unless the task is a description pass. Full rules: `.agents/references/mdx-rules.md`.

**3. Internal links are always root-relative.**
Use `/cloud/virtual-instances/create-an-instance`. Never a full `https://docs.gcore.com/...` URL and never a relative `../` path.

## Available MCP tools

Skills that need them will say so.

| MCP | Purpose |
|-----|---------|
| Jira | Fetch tickets, acceptance criteria, linked issues |
| Confluence | Internal product specs, release notes |
| Playwright | Browser testing at https://portal.gcore.com |

**Before using any MCP tool:** verify it is available. If not, read `.agents/references/mcp-tools/setup.md` and give the user the exact setup instructions from that file. Do not work around a missing tool.

## Task - Skill

Identify the task, then read exactly one skill file. Read nothing else until the skill tells you to.

| Task | Skill (read this file) |
|------|------------------------|
| Product or UI changed - find affected articles and update them | `.claude/skills/update-page/SKILL.md` |
| Write a new article from scratch | `.claude/skills/write-from-scratch/SKILL.md` |
| Analyze a Jira ticket - what needs documenting | `.claude/skills/jira-context/SKILL.md` |
| Work from a GitHub issue | `.claude/skills/github-issue/SKILL.md` |
| Add a REST API tab to an existing Portal article | `.claude/skills/api-use-case/SKILL.md` |
| Audit, verify, or live-test an existing API tab | `.claude/skills/api-audit/SKILL.md` |
| Re-test API tabs after a backend change | `.claude/skills/api-retest/SKILL.md` |
| Add a Terraform tab to an existing article | `.claude/skills/terraform-use-case/SKILL.md` |
| Audit an article step by step against the live portal and fix it | `.claude/skills/full-audit/SKILL.md` |
| Product team: new feature - draft article and draft PR | `.claude/skills/feature-draft/SKILL.md` |
| Compile a multi-product end-to-end guide | `.claude/skills/cookbook/SKILL.md` |
| Take or retake a screenshot for an article step | `.claude/skills/article-screenshot/SKILL.md` |
| Create a PR after work is done | `.claude/skills/pr/SKILL.md` |

## Common mistakes

These errors are specific to this repository. They cause silent failures or broken builds that are hard to debug.

**1. MethodSwitch import missing `.jsx` - blank page, no error**
```mdx
Wrong:   import { MethodSwitch, MethodSection } from "/snippets/method-switch"
Correct: import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"
```
The MDX compiler reports OK. The blank page appears only in the Mintlify runtime.

**2. `{identifier}` in inline backtick code spans - MDX parse error**
```mdx
Wrong:   Poll `GET /tasks/{task_id}` every 5 seconds.
Correct: Poll <code>GET&nbsp;/tasks/{task_id}</code> every 5 seconds.
```
Safe inside triple-backtick fenced blocks. Only breaks in single-backtick inline spans.

**3. `</MethodSection>` indented after a list - tag becomes invisible to the parser**
```mdx
Wrong:
- Last item.

    </MethodSection>       <- indented = MDX treats as list continuation

Correct:
- Last item.

</MethodSection>           <- column 0
```

**4. Prose or numbered steps not wrapped in `<p>` inside `<MethodSection>` - content merges into one block**
```mdx
Wrong:   <MethodSection>Some intro text. 1. First step. 2. Second step.</MethodSection>
Correct: <MethodSection><p>Some intro text.</p><p>1. First step.</p><p>2. Second step.</p></MethodSection>
```
`MethodSwitch` compiles its children in expression mode: plain paragraphs become text strings, blank lines are stripped, and numbered steps merge into one paragraph. Wrap every prose paragraph and every numbered step in its own `<p>`. Bullet lists are not wrapped.

**5. `####` heading inside `<MethodSection>` - appears in the wrong tab's TOC**
```mdx
Wrong:   #### Subsection title       <- leaks into active tab's TOC
Correct: **Subsection title**        <- bold text, no TOC entry
```

**6. `description` with `{...}`, `/paths/`, `:` or `#` - breaks the build**
```yaml
Wrong:   description: Poll GET /tasks/{task_id} until state: FINISHED
Wrong:   description: See #overview for details
Correct: description: Create and manage virtual machines with the Gcore Cloud API.
```
Allowed: commas, periods, hyphens, parentheses, semicolons.

**7. Image file without extension - does not display in the browser**
```mdx
Wrong:   ![Alt text](/images/docs/cloud/create-vm/step-3)
Correct: ![Alt text](/images/docs/cloud/create-vm/step-3.png)
```
Always verify the file exists at the path before referencing it.

**8. `git add .` or `git add -A` - stages unrelated files from other sessions**
Always stage files by name: `git add cloud/virtual-instances/create-an-instance.mdx`

**9. Branching from a stale local `main` - silently includes other branches' commits**
There are three branch name formats: the Jira ticket key (`DOC-2405`) for work tied to a ticket, `issue/{number}-{short-slug}` for a GitHub issue, and `feature-draft/{name}` for a contributor draft. Create every branch with the helper, which checks out `main`, pulls, then branches:
```powershell
.\.agents\tools\create_branch.ps1 DOC-2405
```
Never run `git checkout -b` by hand. If a skill already created the branch, stay on it. See `.cursor/rules/git-branch-naming.mdc`.

**10. Writing content without reading the full product section first - creates duplicate content**
Before writing or expanding any article, read ALL sibling articles in the same product folder and check `docs.json` for the nav group structure. Only then can you determine what belongs in the target article and what is already covered elsewhere.

**11. "permanent" API token - incorrect product terminology**
```
Wrong:   A permanent API token is required.
Correct: An [API token](/account-settings/api-tokens) is required.
```
API tokens have an optional expiration set by the user. Never call them "permanent".

**12. Non-UTF-8 files or non-ASCII characters in `description` - fails CI**
A UTF-8 BOM is stripped by CI and any non-UTF-8 `.mdx` fails the build. On Windows, write files with `-Encoding UTF8` (PowerShell 5.1 `Set-Content` defaults to ANSI). Non-ASCII characters in `description` (long dashes, curly quotes) also fail the `llms.txt` check on PRs.

## CI workflows - what runs automatically

Nine GitHub Actions exist. These affect agent work directly.

| Workflow | When | What it does to you |
|----------|------|---------------------|
| `sanitize-ai-navigation` | Push to any non-main branch that touches `.mdx` | Strips UTF-8 BOM. Rewrites `description:` values: replaces `: # / { }` with a space. **Fails the job on any non-UTF-8 `.mdx`.** Auto-commits with `git add -A` to your branch. Run `git pull` before follow-up commits. (The file name says ai-navigation, the workflow edits `description`.) |
| `normalize-images` | PR touching `images/docs/**`, `**/*.mdx`, or `docs.json` | Moves images into `images/docs/{product}/{article-slug}/` and rewrites MDX paths. Original filenames are kept. **Deletes unreferenced images** (images added in the same PR get a grace period); the job fails if deletions hit `images/docs/portal-icons/` or `images/docs/home/`. Regenerates `llms.txt` files and **fails on any non-ASCII character** in them. Auto-commits to your branch. Run `git pull` before follow-up commits. |
| `validate-terraform-examples` | PR touching `**/*.mdx` | Validates HCL blocks in changed articles against the pinned Terraform provider schema. **Fails the PR on invalid HCL.** |
| `check-api-sdk` | Push touching `api-reference/services_documented/**`, daily 09:30 UTC | Opens an `api-sdk-tracker` issue and commits `api-sdk-tracker/doc_index.json`. |
| `check-terraform-provider` | Daily 09:00 UTC | Opens an issue and a schema-update PR when the provider changes. |
| `update-doc-index` | Push to `main` touching `.mdx` | Opens a `chore/update-doc-index` PR. |
| `generate-llms-txt` | Manual only | Opens an `automated/update-llms-txt` PR. |
| `block-direct-push-main` | Push to `main` | Fails and files a public GitHub issue if the push is not a merge commit. |
| `sync-preprod` | Daily 04:00 UTC | **Force-pushes `main` to `preprod`.** Never base work on `preprod`. |

Image folder convention: `images/docs/{product}/{article-slug}/`.

## Hard stop

Load one skill per task. Do not read other skill files. Do not read articles to "understand context". Do not read references unless the skill explicitly says to. When in doubt about what to do next, ask the user. Do not explore.
