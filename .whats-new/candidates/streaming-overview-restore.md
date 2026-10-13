---
product: streaming
status: Include
published_as: [streaming-restream-audio, streaming-statistics-type, streaming-active-ingest-region, streaming-srt-restream]
---

# Restream audio, statistics filter, ingest region, SRT targets

Customer change: A restream can drop or silence audio. YouTube rejects a stream with no audio track. Statistics aggregation accepts a live, VOD, or playlist type filter. A restream can push to an SRT endpoint in caller mode. The active ingest region is recorded separately under June 2026.
Affected users: Streaming customers using restreams, statistics, or live ingest
Evidence: Documentation appearance, used as the month heading because no separate release record was found. Restream audio and source, statistics type, and active ingest region are in articles and the overview list from September 2026. SRT restream targets are in the overview list from 2026-05-08. October 2026 streaming commits on main only rewrite descriptions.
Open verification: A product release record that names a ship date independently of the article edit
Sources: DOC-2321, DOC-2333, DOC-2136, DOC-2141, overview list removed in 600c15047
Guide: /streaming/live-streaming/create-and-configure-a-restream-to-social-media, /streaming/statistics/view-statistics-of-live-streams-videos-and-billing, /streaming/live-streaming/primary-backup
Duplicate check: not found
Previously published entry (streaming/whats-new.mdx): September 2026 — Control audio and source selection for restreams; Filter Streaming statistics by content type; Identify the active ingest region through the API. May 2026 — Send restreams to SRT endpoints.
