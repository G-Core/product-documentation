---
title: how-low-latency-streaming-works
displayName: Low Latency streaming
published: true
order: 40
toc:
   --1--What is latency, and why it exists: "what-is-streaming-latency-and-why-does-it-exist"
   --1--How Gcore provides Low Latency: "how-does-gcore-provide-low-latency"
   --1--How LL-HLS and LL-DASH work: "how-do-ll-hls-and-ll-dash-work-in-comparison-to-the-standard-approach"
   --1--Use Low Latency streaming: "use-low-latency-streaming"
   --1--Switch to legacy HLS modes: "switch-to-legacy-hls-modes"
   --2--Regular HLS: "get-regular-hls-with-cmaf-mode"
   --2--HLSv3: "get-legacy-hlsv3-mode"
pageTitle: Understanding Low Latency Streaming | Gcore 
pageDescription: A guide explains streaming latency, how Gcore reduces it with LL-HLS and LL-DASH protocols, and how to use them.
---
# How Low Latency streaming works

## What is streaming latency, and why does it exist?

Streaming latency is the timespan between the moment a frame is captured and that frame is displayed on the viewers' screens. Latency occurs because each stream is processed several times during broadcasting to be delivered worldwide:

1.  **Encoding (or packaging).** In this step, the streaming service retrieves your stream in any format, converts it into the format for delivery through CDN, and divides it into small fragments.
2.  **Transferring.** In this step, CDN servers pull the processed stream, cache it, and send it to the end users.
3.  **Receipt by players.** In this step, end-user players load the fragments and buffer them.

Each step affects latency, so the total timespan can increase to 30–40 seconds, especially if the streaming processing isn't optimized. For some companies (such as sports or metaverse events, news releases, etc.), such latency is too large, and it's crucial to reduce it.

## How does Gcore provide low latency?

The Gcore Streaming Platform receives live streams in RTMP or SRT protocols; transcodes to ABR (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-we-optimize-live-stream-and-video-performance-by-creating-different-bitrates" target="_blank">adaptive bitrate</a>) via CDN in LL-HLS and LL-DASH protocols.

- LL-HLS (Low Latency HTTP Live Streaming) is an adaptive protocol developed by Apple for live streaming via the Internet. This protocol is based on HTTP, which allows it to be cached on CDN servers and distributed via CDN as static content. 
- LL-DASH (Low Latency Dynamic Adaptive Streaming over HTTP) is a data streaming technology that optimizes media content delivery via the HTTP protocol.

Also, Gcore uses CMAF (Common Media Application Format) as a base for LL-HLS/DASH. CMAF allows dividing segments into chunks (video fragments) for faster delivery over HTTP networks.

LL-HLS and LL-DASH reduce latency to 3–4 sec, depending on the network conditions.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/13544135637137.png" alt="How does Gcore provide low latency" width="80%">

## How do LL-HLS and LL-DASH work in comparison to the standard approach?

The standard video delivery approach involves sending the entirely created segment to the CDN, and once the CDN receives the complete segment, it transmits it to the player. With this approach, video latency depends on segment length. For example, if a segment is 7 seconds long when requesting and processing the first segment, the player displays a frame that is already 7 seconds late compared to the actual time.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/13082039137553.png" alt="How do LL-HLS and LL-DASH work in comparison to the standard approach?" width="80%">

The Low Latency approach uses the CMAF-CTE extension (Chunked Transfer-Encoding), which helps divide live stream segments into small, non-overlapping, and independent fragments (chunks) with a length of 0.5–2 seconds. The independence of the chunks allows the encoder not to wait for the end of the complete loading of the segment but to send it to the CDN and the player in ready-made small fragments.

This approach helps eliminate the segment duration factor affecting video latency in standard video delivery methods. Therefore, latency for 10-second and 2-second segments will be the same and minimal. The total latency between the CDN server and the viewers will be at most 4 seconds.

Compared to the standard approach, a 7-second segment will be divided into 2–3 seconds chunks. Thus, the total latency will be lower.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/13082040364817.png" alt="Compared to the standard approach" width="80%">

## Use Low Latency streaming

We support <a href="https://gcore.com/news/low-latency-hls/" target="_blank">Low Latency streaming</a> by default. It means your live streams are automatically transcoded to LL-HLSv6 or LL-DASH protocol when you <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">create and configure a live stream</a>. Links for embedding the live stream to your own player contain the */cmaf/* part and look as follows:

- ```https://12345.gvideo.io/cmaf/12345_111/index.mpd``` (LL-DASH, which is supported by any device but does not work with iOS). 
- ```https://12345.gvideo.io/cmaf/12345_111/master.m3u8``` (LL HLSv6, which is supported by iOS (Safari browser) but doesn’t work with non-Apple devices).

where *12345* is the unique ID of your account and *111* is the unique live stream ID.

## Switch to legacy HLS modes

We also support legacy modes for full backward HLS compatibility across all devices and infrastructures. 

### Get Regular HLS with CMAF mode  

Add at the end of the link for embedding the query string as follows:  

```
https://12345.gvideo.io/cmaf/12345_111/master.m3u8?HLS_version=cmaf
```
To return to using LL HLS, delete the query parameter in bold or replace it with the parameter: *?HLS_version=ll* (these actions are identical).

### Get legacy HLSv3 mode  

Contact the [support team](mailto:support@gcore.com) and ask to enable legacy HLSv3 mode for your account or add  *low_latency_enabled=false* parameter to the body of <a href="https://api.gcore.com/docs/streaming#tag/Streams/operation/patch_streams_id" target="_blank">the API request</a>.

The changeover to the legacy format will be displayed in the URL:

```
https://12345.gvideo.io/streams/12345_111/playlist.m3u8
```
