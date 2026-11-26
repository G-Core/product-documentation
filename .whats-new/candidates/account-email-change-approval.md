---
product: Account settings
status: Include
release_date: 2026-11-26
published_page: null
---

# Email address changes need approval from the current address

Customer change: The login email stays unchanged until the current address approves the request and the new address confirms it. A password alone cannot complete the change. Cancelling an unexpected request logs out every session and deletes API keys linked to that request.
Affected users: Customers who change the login email, and customers who receive an email-change message they did not request.
Release evidence: On 2026-11-26 the production profile showed the password dialog, then reported that both links are valid for 24 hours. The production approve page shows Approve change. The production cancel page shows Cancel change and the session and API-key warning.
Open verification: none
Source tickets/PRs: DOC-3060, IMP-2691
Documentation links: account-settings/my-profile/change-email.mdx
Duplicate check: not found
Published entry: null
