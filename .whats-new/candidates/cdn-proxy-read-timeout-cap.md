---
product: CDN
status: Needs verification
release_date: unknown
published_page: null
---

# Self-service CDN read timeout cap of 120 seconds

Customer change: A customer can set proxy_read_timeout from 1 second through 120 seconds. The previous self-service cap was 30 seconds. The default when the option is not set stays 30 seconds. A value above 120 seconds is still rejected for a customer.
Affected users: CDN resource owners who set a custom read timeout in the Customer Portal, the CDN API, or Terraform.
Release evidence: CDP-2719 is Closed as Resolved on 2026-10-26, and the CDN API source describes a migration that raises the cap to 120 seconds. The live API and the Customer Portal were not checked.
Open verification: Confirm on the production or preprod API that a customer request with proxy_read_timeout 120s is accepted and 121s returns HTTP 400.
Source tickets/PRs: DOC-3026, CDP-2719
Documentation links: cdn/getting-started/cdn-timeouts.mdx, cdn/cdn-resource-options/general/customize-connection-and-read-timeouts.mdx, cdn/troubleshooting/5xx-error-how-to-solve-server-issues.mdx
Duplicate check: not found
Published entry:
