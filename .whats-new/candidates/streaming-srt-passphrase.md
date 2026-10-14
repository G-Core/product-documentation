---
product: streaming
status: Include
published_as: streaming-srt-passphrase
available_since: 2026-05-28
---

# SRT ingest passphrase

Customer change: An SRT PUSH stream can require srt_passphrase. The encoder must send the same value. SRT encrypts the MPEG-TS ingest. Playback URLs are not encrypted by this setting.
Affected users: Customers pushing live streams over SRT
Evidence: Added to the SRT article on 2026-05-28 in commit 5e4639991, message VP-6489 SRT passphrase protection. Month heading is the documentation date.
Open verification: A product release record that names a ship date independently of the article edit
Sources: VP-6489, commit 5e4639991
Guide: /streaming/live-streaming/protocols/srt
Duplicate check: not found
Previously published entry (streaming/whats-new.mdx): May 2026 — Protect SRT ingest with a passphrase
