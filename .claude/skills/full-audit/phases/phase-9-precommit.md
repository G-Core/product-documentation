# Phase 9 — Pre-commit checklist + present for review

**STOP. DO NOT COMMIT. DO NOT PUSH.**

Phase 9 ends after the pre-commit checklist is complete and shown to the user.
Commit and push happen ONLY when the user explicitly says one of:
`коммить`, `коммит`, `commit`, `пуш`, `пушь`, `push`, `закоммить`, `запушь`.

If none of these words appear in the current user message — stop after showing the checklist.

**Branch context:** The feature branch was created in Phase 4 immediately after the Jira ticket.
The branch name is the Jira ticket key. All edits since Phase 4 already land on that branch.

Run the pre-commit checklist below and present the results to the user. Then stop and wait.

**PowerShell git commit — do NOT use bash heredoc syntax.**

`cat <<'EOF' ... EOF` is bash syntax. PowerShell will throw a parse error:
`The '<' operator is reserved for future use` / `MissingFileSpecification`.

Use a PowerShell here-string instead:

```powershell
$msg = @"
First line of commit message

- bullet 1
- bullet 2
"@
git commit -m $msg
```

The `@"..."@` markers must each be on their own line with nothing after the `@"` opener
and nothing before the `"@` closer.

## Pre-commit checklist

**Clean working directory — no junk files:**
- [ ] No temporary screenshots left in project roots or home folders
  (e.g. `$env:USERPROFILE\*.png`)
- [ ] No one-off scripts created during the session that are not part of
  the article or the permanent tooling
- [ ] `git status` shows only the article file, its images, and any deleted
  old images — nothing else

**UTF-8 encoding integrity — the most common source of silent corruption:**

MDX files in this repo are UTF-8 without BOM and use LF line endings. On Windows, any tool that reads or writes a file without specifying UTF-8 (PowerShell `Get-Content`, `Set-Content`, Notepad) uses the system ANSI codepage and silently corrupts every non-ASCII character. The corruption is invisible in the editor but renders as garbage in the browser, for example a mangled em dash.

Run the checker:

```powershell
python .agents/tools/check_mdx_encoding.py {relative/path/to/article.mdx}
```

- [ ] `BOM` or `CRLF` reported — run it again with `--fix`, which removes the BOM and converts to LF, then re-run without `--fix`.
- [ ] `GARBAGE` reported — the file was corrupted. Restore it from git and re-apply all edits using the UTF-8 safe method described in `.agents/references/mdx-rules.md`. Never try to replace corruption patterns by hand.
- [ ] `NOT_UTF8` reported — restore from git and re-apply the edits.
- [ ] The checker prints `OK` for the article.
