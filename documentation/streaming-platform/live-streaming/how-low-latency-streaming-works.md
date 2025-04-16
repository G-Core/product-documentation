---
title: how-low-latency-streaming-works
displayName: Low Latency streaming
published: true
order: 45
toc:
    --1--How Gcore provides low Latency: 'how-does-gcore-provide-low-latency'
    --1--How LL-HLS and LL-DASH work: 'how-do-ll-hls-and-ll-dash-work-in-comparison-to-the-standard-approach'
    --1--Use Low Latency streaming: 'use-low-latency-streaming'
    --1--Switch to legacy HLS modes: 'switch-to-legacy-hls-modes'
pageTitle: Understanding Low Latency Streaming | Gcore
pageDescription: A guide explains streaming latency, how Gcore reduces it with LL-HLS and LL-DASH protocols, and how to use them.
---

# How Low Latency streaming works

Streaming latency is the timespan between the moment a frame is captured and when that frame is displayed on the viewers' screens. Latency occurs because each stream is processed several times during broadcasting to be delivered worldwide:

1\. **Encoding (or packaging).** In this step, the streaming service retrieves your stream in any format, converts it into the format for delivery through CDN, and divides it into small fragments.

2\. **Transferring.** In this step, CDN servers pull the processed stream, cache it, and send it to the end-users.

3\. **Receipt by players.** In this step, end-user players load the fragments and buffer them.

Each step affects latency, so the total timespan can increase to 30–40 seconds, especially if the streaming processing isn't optimized. For some companies (such as sports or metaverse events, or news releases), such latency is too large, and it's crucial to reduce it.

## How does Gcore provide low latency?

The Gcore Video Streaming receives live streams in RTMP or SRT protocols; transcodes to ABR (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-after-transcoding-bitrate-frame-rate-and-codecs#output-parameters-after-transcoding" target="_blank">adaptive bitrate</a>), via CDN in LL-HLS and LL-DASH protocols.

-   LL-HLS (Low Latency HTTP Live Streaming) is an adaptive protocol developed by Apple for live streaming via the Internet. This protocol is based on HTTP, which allows it to be cached on CDN servers and distributed via CDN as static content.
-   LL-DASH (Low Latency Dynamic Adaptive Streaming over HTTP) is a data streaming technology that optimizes media content delivery via the HTTP protocol.

Also, Gcore uses CMAF (Common Media Application Format) as a base for LL-HLS/DASH. CMAF allows dividing segments into chunks (video fragments) for faster delivery over HTTP networks.

LL-HLS and LL-DASH reduce latency to 2–4 sec, depending on the network conditions.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/gcore-vs-traditional-streaming.png" alt="How does Gcore provide low latency" width="80%">

## How do LL-HLS and LL-DASH work in comparison to the standard approach?

The standard video delivery approach involves sending the entirely created segment to the CDN. Once the CDN receives the complete segment, it transmits it to the player.

With this approach, video latency depends on segment length. For example, if a segment is 6 seconds long when requesting and processing the first segment, the player displays a frame that is already 6 seconds late compared to the actual time.

The Low Latency approach uses the CMAF-CTE extension (Chunked Transfer-Encoding), which helps divide live stream segments into small, non-overlapping, and independent fragments (chunks) with a length of 0.5–2 seconds. The independence of the chunks allows the encoder not to wait for the end of the complete loading of the segment but to send it to the CDN and the player in ready-made small fragments.

This approach helps eliminate the segment duration factor affecting video latency in standard video delivery methods. Therefore, latency for 10-second and 2-second segments will be the same and minimal. The total latency between the CDN server and the viewers will be at most 4 seconds.

Compared to the standard approach, a 6-second segment will be divided into 0.5-2 seconds chunks. Thus, the total latency will be lower.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/low-latency-casino.gif" alt="Example of how low latency works" width="80%">

## Use Low Latency streaming

We support <a href="https://gcore.com/news/low-latency-hls/" target="_blank">Low Latency streaming</a> by default. It means your live streams are automatically transcoded to LL-HLS or LL-DASH protocol when you <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">create and configure a live stream</a>.

Links for embedding the live stream to your own player contain the _/cmaf/_ part and look as follows:

-   MPEG-DASH, CMAF (low latency): `https://demo.gvideo.io/cmaf/2675_19146/index.mpd`
-   LL HLS, CMAF (low latency): `https://demo.gvideo.io/cmaf/2675_19146/master.m3u8`
-   Traditional HLS, MPEG TS (no low latency): `https://demo.gvideo.io/mpegts/2675_19146/master_mpegts.m3u8`

## Switch to legacy HLS modes

Some legacy devices or software require MPEG-TS (.ts) segments for streaming. To ensure full backward compatibility with HLS across all devices and infrastructures, we offer MPEG-TS streaming options.

We produce low-latency and non-low-latency streams in parallel, so you don't have to create a stream specifically for cases when the connection is unstable or a device doesn’t support low-latency. Both formats share the same segment sizes, manifest lengths for DVR functionality, and other related capabilities.

<alert-element type="tip" title="Tip">
 
For modern devices, we recommend using the HLS manifest URL (`hls_cmaf_url`). It’s more efficient and is highly compatible with streaming devices.

</alert-element>

You can get the non-low-latency in the same Links for export section in the Customer Portal:

1\. On the <a href="https://portal.gcore.com/streaming/streaming/list" target="_blank">Video Streaming</a> page, find the needed video.

2\. In the **Links for export** section, copy the link in the **HLS non-low-latency manifest URL** field. This link contains non low-latency HLSv3 and MPEG TS files as chunks.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works/export-non-low-latency-link.png" alt="HLS non-low-latency link example" width="80%">

For details on how to get the streams via API, check our <a href="https://api.gcore.com/docs/streaming#tag/Streams/operation/get_streams" target="_blank">API documentation</a>.
