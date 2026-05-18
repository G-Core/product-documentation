# Streaming MCP Server: Articles Plan

## Principle

Each article = one user goal, not one product feature.
The AI collects parameters before acting, because some settings cannot be
changed after creation. Each article includes:
1. A table of questions the AI must ask and why.
2. An example conversation showing the full flow.
3. A ready-to-use prompt the user can paste into Claude Code or Cursor.

General setup articles (install, configure, connect clients) live in
`developer-tools/mcp-server/` and are shared across all products. Each
scenario article links back to them via a shared Prerequisites snippet.

---

## Articles (6 total)

### 1. Set up a live stream
**File:** `set-up-a-live-stream.mdx` ✅ DONE
**Covers:** ~18 articles in `live-streaming/`
**Key constraint:** `low_latency_enabled` cannot be changed after creation.

Questions AI must ask:
- Stream name
- Encoder software (OBS / vMix / browser / Larix / other)
- Low latency needed? (immutable — must be decided upfront)
- Recording enabled?
- DVR enabled?
- Restream to other platforms?

---

### 2. Upload and manage videos
**File:** `upload-and-manage-videos.mdx`
**Covers:** ~15 articles in `video-hosting/`
**Key decisions:** upload method, subtitles, playlist, access protection

Questions AI must ask:
- Where is the video? (local file / remote URL / Google Drive)
- Add AI-generated subtitles, upload an SRT file, or no subtitles?
- Organize into a playlist?
- Should original file be downloadable?
- Protect with AES-128 encryption or token auth?

Example outcome: video uploaded, subtitles generated, embed code returned.

---

### 3. Moderate video content with AI
**File:** `moderate-video-content.mdx`
**Covers:** ~8 articles in `ai-video-service/`
**Key decisions:** what to detect, action on detection, live vs VOD

Questions AI must ask:
- What content to detect? (NSFW / hard nudity / soft nudity / sports activities / all)
- Apply to live streams, uploaded videos, or both?
- What should happen when content is detected? (flag for review / auto-reject / webhook notification)
- What probability threshold triggers a flag? (default or custom)

Example outcome: moderation configured, test video analyzed, results returned.

---

### 4. View streaming statistics
**File:** `view-streaming-statistics.mdx`
**Covers:** ~4 articles in `statistics/`
**Key decisions:** scope (live vs VOD), metric type, time range

Questions AI must ask:
- Live streams, uploaded videos, or both?
- What do you want to see? (view counts / geographic distribution / playback quality / billing)
- Time period? (today / last 7 days / last 30 days / custom range)
- Specific stream or video, or aggregate across all?

Example outcome: stats returned in a structured summary the user can read or export.

---

### 5. Protect video content
**File:** `protect-video-content.mdx`
**Covers:** `video-hosting/protect-your-videos-with-the-aes-128-encryption.mdx`,
            `interaction-with-cdn/video-secure-token.mdx`,
            `interaction-with-cdn/token-auto-refresh.mdx`
**Key decisions:** protection method, scope (stream vs VOD)

Questions AI must ask:
- What to protect: live stream, uploaded video, or both?
- Protection method: AES-128 encryption (VOD only), secure token (stream URLs), or both?
- Token expiry duration?
- Should the token auto-refresh for long sessions?

Example outcome: AES-128 encryption enabled on VOD, secure token generated,
embed URL with token returned.

---

### 6. Integrate streaming with CDN
**File:** `integrate-streaming-with-cdn.mdx`
**Covers:** ~3 articles in `interaction-with-cdn/`, `extra-features/get-webhooks-from-the-streaming-platform.mdx`
**Key decisions:** own CDN vs Gcore CDN, webhooks needed

Questions AI must ask:
- Use Gcore CDN (default) or connect your own CDN resource?
- Need webhooks for stream start/stop/recording-complete events?
- Webhook endpoint URL?

Example outcome: CDN resource linked to stream, webhook configured, test event sent.

---

## What NOT to create

- A general "Manage Streaming via MCP" overview page — that is already
  covered by `gcore-mcp-server-available-products-and-tools.mdx` in
  `developer-tools/mcp-server/`.
- Separate articles for each encoder (OBS, ffmpeg, Larix) — the
  encoder-specific details belong inside scenario articles as conditional
  sections, not standalone pages.
- A copy of every existing streaming article with "via MCP" appended —
  that duplicates content without adding value.

---

## Navigation placement

Add a `mcp-server` group inside the `streaming` navigation section in
`docs.json`, after `live-streaming` and `video-hosting`. Example:

```json
{
  "group": "MCP Server",
  "pages": [
    "streaming/mcp-server/set-up-a-live-stream",
    "streaming/mcp-server/upload-and-manage-videos",
    "streaming/mcp-server/moderate-video-content",
    "streaming/mcp-server/view-streaming-statistics",
    "streaming/mcp-server/protect-video-content",
    "streaming/mcp-server/integrate-streaming-with-cdn"
  ]
}
```

---

## Shared snippet

All articles use `/snippets/mcp-server-prerequisites.mdx` which renders:

```
**Prerequisites:** Gcore MCP Server installed and connected to your AI client.
See [Install and configure](/developer-tools/mcp-server/install-and-configure-gcore-mcp-server).
Use `GCORE_TOOLS="streaming.*"` to load only Streaming tools.
```

This avoids repeating setup instructions in every scenario article.
