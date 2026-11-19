---
product: Streaming
status: Needs verification
release_date: unknown
published_page: null
---

# Restream into another Gcore stream is not allowed

Customer change: Restreaming a stream into another ingest point of Gcore Streaming (the push URL of another stream of the same account) is not allowed because it consumes a large amount of resources for no reason. Customers should not create such restreams and should remove existing ones.
Affected users: Streaming customers whose restream target URL is the push URL of another Gcore stream (A to B setup).
Release evidence: not verified. The rule was stated by the product owner during VP-6901 work, with no date and no release ticket.
Open verification: Since when the rule applies and whether the restream API rejects such target URLs.
Source tickets/PRs: VP-6901
Documentation links: streaming/live-streaming/create-and-configure-a-restream-to-social-media.mdx, streaming/live-streaming/stream-and-restream-limits.mdx
Duplicate check: not found in streaming/whats-new.mdx
Published entry: none
