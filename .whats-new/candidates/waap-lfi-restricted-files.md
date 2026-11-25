---
product: WAAP
status: Include
release_date: 2026-11-16
published_page: null
---

# Local file inclusion blocks restricted-file requests

Customer change: The Local file inclusion (LFI) policy blocks a request for a restricted file, not only inclusion of a file already on the server. Build files and rc dotfiles match only at the path root. Secret files match at any depth. A repository URL such as /owner/repo/blob/main/go.mod does not match.
Affected users: Accounts that enable the WAF and OWASP top threats rule set with the Local file inclusion policy set to block.
Release evidence: The rule has been blocking in production since 2026-11-16. On 2026-11-25, domain store.gcdn.co had the policy enabled with action Block, and WAAP events recorded /vercel.json, /.git-credentials, /sendgrid.env, and /go.mod as block under that policy. The domain itself was in monitor mode, so the HTTP response stayed a 404.
Open verification: none for the policy action. A nested repository URL was not requested live.
Source tickets/PRs: DOC-3067, WS-3136
Documentation links: waap/waap-policies/waf-and-owasp-top-threats.mdx
Duplicate check: not found
Published entry: null
