---
product: Streaming
status: Published
release_date: unknown
published_page: /streaming/whats-new
---

# SRT ingest passphrase

Customer change: An SRT PUSH stream can require srt_passphrase. The encoder must send the same value. SRT encrypts the MPEG-TS ingest. Playback URLs are not encrypted by this setting.
Affected users: Customers pushing live streams over SRT
Release evidence: Added to the SRT article on 2026-05-28 in commit 5e4639991, message VP-6489 SRT passphrase protection. Month heading is the documentation date.
Open verification: A product release record that names a ship date independently of the article edit
Source tickets/PRs: VP-6489, commit 5e4639991
Documentation links: streaming/live-streaming/protocols/srt.mdx
Duplicate check: not found
Published entry: May 2026 — Protect SRT ingest with a passphrase
