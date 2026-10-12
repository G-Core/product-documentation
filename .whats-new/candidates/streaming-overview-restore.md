---
product: Streaming
status: Published
release_date: unknown
published_page: /streaming/whats-new
---

# Restream audio, statistics filter, ingest region, SRT targets

Customer change: A restream can drop or silence audio, and can send the original stream or the transcoded stream with overlays. YouTube rejects a stream with no audio track. Statistics aggregation accepts a live, VOD, or playlist type filter. A live stream response includes the active ingest region. A restream can push to an SRT endpoint in caller mode.
Affected users: Streaming customers using restreams, statistics, or live ingest
Release evidence: Documentation appearance, used as the month heading because no separate release record was found. Restream audio and source, statistics type, and active ingest region are in articles and the overview list from September 2026. SRT restream targets are in the overview list from 2026-05-08. October 2026 streaming commits on main only rewrite descriptions.
Open verification: A product release record that names a ship date independently of the article edit
Source tickets/PRs: DOC-2321, DOC-2333, DOC-2136, DOC-2141, overview list removed in 600c15047
Documentation links: streaming/live-streaming/create-and-configure-a-restream-to-social-media.mdx, streaming/statistics/view-statistics-of-live-streams-videos-and-billing.mdx, streaming/live-streaming/primary-backup.mdx
Duplicate check: not found
Published entry: September 2026 — Control audio and source selection for restreams; Filter Streaming statistics by content type; Identify the active ingest region through the API. May 2026 — Send restreams to SRT endpoints.
