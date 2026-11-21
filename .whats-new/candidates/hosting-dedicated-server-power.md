---
product: Hosting
status: Include
release_date: unknown
published_page: null
---

# Dedicated server power and reboot in the hosting portal

Customer change: Dedicated server power, OS reinstall from a template, the server console, and RMI are on the Dedicated servers page in the hosting portal. Power On/Off opens Server power, and Execute power action switches the server to the other state. Reboot opens a confirmation. The To panel path into DCImanager is not on that page.
Affected users: Customers with an active dedicated server in the Gcore Hosting Portal.
Release evidence: On 2026-11-19 the production portal at hosting.gcore.com showed Manage server and the row menu with Power On/Off and Reboot. Server power showed Current state (DCI) and Execute power action. The form action is dci_remote_install.power_toggle. Execute power action was not submitted.
Open verification: The exact date the hosting-portal controls replaced To panel is not in the ticket.
Source tickets/PRs: DOC-3009
Documentation links: hosting/dedicated-servers/manage/log-in-to-dcimanager.mdx, hosting/dedicated-servers/manage/log-in-to-ipmi.mdx, hosting/dedicated-servers/manage/operating-system/install-a-linux-os-from-a-template.mdx, hosting/dedicated-servers/manage/reboot-a-server.mdx, hosting/dedicated-servers/troubleshooting/troubleshoot-ipmi-errors.mdx
Duplicate check: not found
Published entry: null
