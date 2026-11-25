---
product: CDN
status: Include
release_date: 2026-11-25
published_page: null
---

# CDN purge rejects invalid paths

Customer change: Purge by URL and purge by pattern reject a path that contains a vertical bar, a line break, or a tab, and a percent sign that is not followed by two hexadecimal digits. A pattern ending in * is accepted when it does not contain a vertical bar.
Affected users: Customers who purge CDN cache by URL or by pattern
Release evidence: Production POST /cdn/resources/1067414/purge on 2026-11-25. A plain path and %20 returned success. A vertical bar, a line break, and %ZZ returned 400 with the two error strings now in the article. A pattern ending in * returned success. A pattern containing a vertical bar returned 400.
Open verification: none
Source tickets/PRs: DOC-3061, CDM-2192
Documentation links: cdn/clear-cdn-resource-cache-by-url-pattern-or-all.mdx
Duplicate check: not found
Published entry: null
