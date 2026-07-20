# Hosting Section — Regression Audit Plan

Epic: DOC-1701
Total articles: 71 (70 in hosting/ + hosting.mdx landing page)

Statuses: `todo` | `in_progress` | `done` | `blocked`

Branch convention: one branch per article, named after the Jira ticket created in Phase 4.
Example: `git checkout -b DOC-1702` after the ticket is created.

---

## How to use this plan

Work one group at a time, top to bottom within each group.
Finish all articles in a group before starting the next group.
Mark each article `in_progress` before opening the portal (Phase 0 claim).
Mark `done [DOC-XXXX]` after Phase 10 is complete.

---

## Group A — Virtual Servers: Lifecycle (start here)

These are the most-visited articles. Do these first.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1704 | `hosting/virtual-servers/order-a-virtual-server.mdx` |
| done | DOC-1734 | `hosting/virtual-servers/upgrade-your-virtual-server.mdx` |
| done | DOC-1759 | `hosting/virtual-servers/delete-a-virtual-server.mdx` |

---

## Group B — Virtual Servers: Before Purchase

Short informational articles. No portal steps required for most.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1730 | `hosting/virtual-servers/before-purchase/choose-a-virtual-server-for-your-needs.mdx` |
| done | DOC-1732 | `hosting/virtual-servers/before-purchase/test-the-connectivity-between-your-location-and-the-server-you-want-to-buy.mdx` |

---

## Group C — Virtual Servers: Connect

Requires a running VS from Group A.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1738 | `hosting/virtual-servers/manage/connect/connect-to-a-virtual-server-via-vnc.mdx` |
| done | DOC-1739 | `hosting/virtual-servers/manage/connect/linux-server/connect-to-a-linux-server-via-control-panel.mdx` |
| done | DOC-1740 | `hosting/virtual-servers/manage/connect/linux-server/connect-to-linux-server-via-ssh.mdx` |
| done | DOC-1742 | `hosting/virtual-servers/manage/connect/linux-server/change-the-port-for-ssh-connections.mdx` |
| done | DOC-1741 | `hosting/virtual-servers/manage/connect/linux-server/manage-ssh-keys.mdx` |

---

## Group D — Virtual Servers: Operating System

Requires a running VS. VMmanager articles may need a separate test environment.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1748 | `hosting/virtual-servers/manage/operating-system/install-a-linux-os-from-a-template.mdx` |
| done | DOC-1750 | `hosting/virtual-servers/manage/operating-system/install-a-linux-os-from-your-iso-image.mdx` |
| done | DOC-1751 | `hosting/virtual-servers/manage/operating-system/install-an-os-from-a-template-in-vmmanager-6.mdx` |
| done | DOC-1752 | `hosting/virtual-servers/manage/operating-system/install-an-os-from-iso-in-vmmanager-6.mdx` |
| done | DOC-1747 | `hosting/virtual-servers/manage/operating-system/buy-a-windows-server.mdx` |

---

## Group E — Virtual Servers: Networking

Requires a running VS.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1756 | `hosting/virtual-servers/manage/networking/additional-ip-addresses/configure-an-additional-ip-address.mdx` |
| done | DOC-1754 | `hosting/virtual-servers/manage/networking/allocate-an-ipv6-address-in-vmmanager-6.mdx` |

---

## Group F — Virtual Servers: Other Management

Requires a running VS.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1736 | `hosting/virtual-servers/manage/main-features-and-functions-of-vmmanager-6.mdx` |
| done | DOC-1745 | `hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian.mdx` |
| done | DOC-1325 | `hosting/virtual-servers/manage/reboot-a-server.mdx` |
| done | DOC-1758 | `hosting/virtual-servers/manage/set-up-a-ptr-record.mdx` |

---

## Group G — Virtual Servers: Troubleshooting

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1762 | `hosting/virtual-servers/troubleshooting/remove-your-ip-address-from-blacklists.mdx` |
| done | DOC-1760 | `hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment.mdx` |
| done | DOC-1764 | `hosting/virtual-servers/troubleshooting/troubleshoot-blocked-smtp-ports.mdx` |
| done | DOC-1775 | `hosting/virtual-servers/troubleshooting/troubleshoot-errors-with-iso-image-installation.mdx` |
| done | DOC-1777 | `hosting/virtual-servers/troubleshooting/troubleshoot-issues-with-ssh-connection.mdx` |

---

## Group H — Dedicated Servers: Lifecycle

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1811 | `hosting/dedicated-servers/order-a-dedicated-server.mdx` |
| done | DOC-1812 | `hosting/dedicated-servers/upgrade-your-dedicated-server.mdx` |
| todo | — | `hosting/dedicated-servers/delete-a-dedicated-server.mdx` |
| todo | — | `hosting/dedicated-servers/check-statistics-of-your-dedicated-server.mdx` |

---

## Group I — Dedicated Servers: Connect and Access

Requires a running DS. IPMI and DCImanager access may require special account access.

| Status | Ticket | File |
|--------|--------|------|
| in_progress | — | `hosting/dedicated-servers/manage/connect/connect-to-a-linux-server.mdx` |
| done | DOC-1737 | `hosting/dedicated-servers/manage/connect/connect-to-a-windows-server.mdx` |
| in_progress | — | `hosting/dedicated-servers/manage/log-in-to-dcimanager.mdx` |
| done [DOC-1814](https://jira.gcore.lu/browse/DOC-1814) | DOC-1814 | `hosting/dedicated-servers/manage/log-in-to-ipmi.mdx` |

---

## Group J — Dedicated Servers: Operating System

Requires a running DS.

| Status | Ticket | File |
|--------|--------|------|
| in_progress | — | `hosting/dedicated-servers/manage/operating-system/install-a-linux-os-from-a-template.mdx` |
| todo | — | `hosting/dedicated-servers/manage/operating-system/install-a-linux-os-from-your-iso-image.mdx` |

---

## Group K — Dedicated Servers: Networking

Requires a running DS.

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1755 | `hosting/dedicated-servers/manage/networking/additional-ip-addresses/buy-an-additional-ip-address.mdx` |
| done [DOC-1819](https://jira.gcore.lu/browse/DOC-1819) | DOC-1819 | `hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card.mdx` |
| todo | — | `hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan.mdx` |

---

## Group L — Dedicated Servers: Other Management

| Status | Ticket | File |
|--------|--------|------|
| in_progress | — | `hosting/dedicated-servers/manage/reboot-a-server.mdx` |

---

## Group M — Dedicated Servers: Troubleshooting

| Status | Ticket | File |
|--------|--------|------|
| done | DOC-1761 | `hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-is-not-responding-to-ping-requests.mdx` |
| done | DOC-1763 | `hosting/dedicated-servers/troubleshooting/troubleshoot-errors-with-iso-image-installation.mdx` |
| todo | — | `hosting/dedicated-servers/troubleshooting/troubleshoot-ipmi-errors.mdx` |
| done | DOC-1765 | `hosting/dedicated-servers/troubleshooting/troubleshoot-issues-with-an-incorrect-ip-location.mdx` |
| done | DOC-1778 | `hosting/dedicated-servers/troubleshooting/troubleshoot-packet-loss-or-high-ping.mdx` |

---

## Group N — Payments

No portal resource prerequisites. Can be done independently of Groups A-M.

| Status | Ticket | File |
|--------|--------|------|
| todo | — | `hosting/payments/pay-for-gcore-services-payment-methods.mdx` |
| todo | — | `hosting/payments/check-the-payment-history.mdx` |
| todo | — | `hosting/payments/renew-your-server.mdx` |
| todo | — | `hosting/payments/set-up-auto-payment.mdx` |
| todo | — | `hosting/payments/request-a-refund.mdx` |
| todo | — | `hosting/payments/troubleshoot-payment-errors.mdx` |

---

## Group O — Account Management

No portal resource prerequisites. Can be done independently of Groups A-M.

| Status | Ticket | File |
|--------|--------|------|
| todo | — | `hosting/account-management/manage-your-password.mdx` |
| todo | — | `hosting/account-management/set-up-two-factor-authentication.mdx` |
| todo | — | `hosting/account-management/set-up-notifications.mdx` |
| todo | — | `hosting/account-management/view-the-authorization-history-of-your-account.mdx` |
| todo | — | `hosting/account-management/users/add-a-new-user-to-your-account.mdx` |
| todo | — | `hosting/account-management/users/configure-user-rights.mdx` |

---

## Group P — Other Services

Each service is self-contained. Do in any order within the group.

| Status | Ticket | File |
|--------|--------|------|
| todo | — | `hosting/other-services/bgp/activate-bgp.mdx` |
| todo | — | `hosting/other-services/ddos-protection/activate-ddos-protection-for-your-dedicated-servers.mdx` |
| todo | — | `hosting/other-services/dns-hosting/manage-dns-hosting.mdx` |
| todo | — | `hosting/other-services/link-aggreagtion/activate-link-aggregation.mdx` |
| todo | — | `hosting/other-services/ssl-certificates/activate-an-ssl-certificate.mdx` |

---

## Group Q — Top-Level Articles

| Status | Ticket | File |
|--------|--------|------|
| todo | — | `hosting/become-reseller-and-resell-our-services.mdx` |
| todo | — | `hosting/contact-our-technical-support.mdx` |
| todo | — | `hosting/manage-hosting-services-via-api.mdx` |

---

## Group R — Overview and Conceptual Articles (audit last)

Audit after all how-to articles in the same product are done.
Content accuracy depends on how-tos being correct first.

| Status | Ticket | File |
|--------|--------|------|
| todo | — | `hosting/virtual-servers/about-virtual-servers.mdx` |
| todo | — | `hosting/dedicated-servers/about-dedicated-servers.mdx` |
| todo | — | `hosting/other-services/ssl-certificates/about-ssl-certificates.mdx` |
| todo | — | `hosting/other-services/ddos-protection/about-gcore-ddos-protection-for-dedicated-servers.mdx` |
| todo | — | `hosting.mdx` |
