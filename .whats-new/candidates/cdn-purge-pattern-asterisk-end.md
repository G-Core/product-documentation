---
product: CDN
status: Include
release_date: 2026-11-26
published_page: null
---

# CDN purge patterns allow the asterisk only at the end

Customer change: A purge-by-pattern path may use * only as the last character. A pattern such as /static/* is accepted. A pattern with * at the start or before a file extension is not the current rule.
Affected users: Customers who purge CDN cache by pattern.
Release evidence: The production Purge by pattern card on 2026-11-26 says the asterisk substitutes any number of symbols at the end of the pattern. The examples on that card are /img/city.jpg, /img/*, and /static/*.
Open verification: none
Source tickets/PRs: none yet
Documentation links: cdn/clear-cdn-resource-cache-by-url-pattern-or-all.mdx
Duplicate check: cdn-purge-url-validation.md is the earlier rejection of vertical bars and bad percent encoding, not this rule
Published entry: null
