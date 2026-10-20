---
product: Streaming
status: Published
release_date: unknown
published_page: /streaming/whats-new
---

# Path-based RTMP ingest for legacy cameras

Customer change: A legacy RTMP camera that cannot send a query string can place the push token in the path. The same form is accepted on the backup ingest URL.
Affected users: Customers ingesting with legacy RTMP cameras or encoders
Release evidence: Added to the RTMP and primary-backup articles on 2026-08-26 in commit 30e18143b. No separate release record. Month heading is the documentation date.
Open verification: A product release record that names a ship date independently of the article edit
Source tickets/PRs: commit 30e18143b; later restated in PR 3158 / VP-6671
Documentation links: streaming/live-streaming/primary-backup.mdx, streaming/live-streaming/protocols/rtmp.mdx
Duplicate check: not the October rewrite of the RTMP article
Published entry: August 2026 — Use a path-based RTMP ingest URL for legacy cameras
