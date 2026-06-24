# WAAP API Tab — Orchestration Checklist

Execute every phase in order. Read each file only when its phase arrives.

---

## Phase 0 — Load the skill

Read: `.agents/skills/api-use-case/SKILL.md`

---

## Phase 1 — Read the article

Read the target article in full.

Determine: Structure A (sequential) or Structure B (independent)?

---

## Phase 2 — Live API testing (ask the user)

Ask whether to test against the live API or use the spec only.
Wait for the answer before proceeding.

---

## Phase 3 — Find endpoints in the spec

Read: `api-reference/services_documented/waap_api.yaml` (relevant sections only)

---

## Phase 4 — Write the API section

Read before writing:
- `.agents/references/mdx-rules.md`
- `.agents/references/style-guide.md`

Then write the `<MethodSection id="api">` content.

---

## Phase 5 — Validate MDX

```powershell
cd C:\Temp
node -e "const {compile}=require('@mdx-js/mdx');const fs=require('fs');const c=fs.readFileSync('PATH','utf8');compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));"
```

Fix any error before proceeding.

---

## Phase 6 — Commit and push

```powershell
cd C:\Projects\product-documentation
git add <file>
git commit -m "feat(waap): add API tab to <article> (article N)"
git push origin waap-api-guides
```

If rejected: `git pull --rebase origin waap-api-guides && git push origin waap-api-guides`

---

## Phase 7 — Jira ticket

```powershell
cd C:\Projects\docops-agent2
.\venv\Scripts\python.exe scripts\create_jira_ticket.py `
  --summary "Add API tab: <title>" `
  --description "<operations covered>"
```

---

## Phase 8 — Update status file

Update `.agents/WAAP-API-TABS-STATUS.md`: set all columns to `OK`, add comment with endpoints and commit hash.
