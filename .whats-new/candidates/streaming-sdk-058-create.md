---
product: Streaming
status: Include
release_date: 2026-09-29
published_page: null
---

# Streaming SDK create responses

Customer change: Python and Go SDK v0.58.0 and later return the created player, video, and playlist from create. Player create uses CreatePlayerParam. Playlist create and update fields are set directly. name is optional on player update.
Affected users: Customers who create players, videos, or playlists with the Python or Go SDK
Release evidence: Python SDK v0.58.0 published 2026-09-29. The same signatures are present in v0.59.0. Create and delete were run on production for issue 3055. Not published on the What's new page.
Open verification: none
Source tickets/PRs: https://github.com/G-Core/product-documentation/issues/3055, https://github.com/G-Core/product-documentation/issues/3165
Documentation links: streaming/player/customize-appearance-of-the-built-in-player.mdx, streaming/video-hosting/upload-a-video-and-embed-it-to-your-app.mdx, streaming/ai-video-service/generate-ai-subtitles-and-add-them-to-video/generate-captions-in-customer-portal.mdx, streaming/video-hosting/create-and-configure-playlists-for-videos.mdx, streaming/video-hosting/create-an-illusion-of-a-live-broadcast-with-uploaded-videos.mdx
Duplicate check: same event as issue 3055, not yet on a What's new page
Published entry: null
