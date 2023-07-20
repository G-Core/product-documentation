---
title: about-gcore-streaming-platform
displayName: Overview
published: true
order: 10
toc:
   --1--Streaming directly via CDN: "method-1-streaming-directly-via-cdn"
   --1--Streaming via the Streaming Platform: "method-2-streaming-via-the-streaming-platform-with-cdn"
pageTitle: Understanding Two Ways of Streaming | Gcore
pageDescription: Explore the Streaming Platform overview and its high moments. 
---
# About Gcore Streaming Platform  

## Method 1: Streaming directly via CDN

If you have your own media server that produces a stream in HLS format, you will need one CDN resource with special settings for playlists (.m3u8) and chunks (.ts). For more information about settings, see the article <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">Live streaming via CDN using the HLS protocol</a>.

You can protect the stream with a token. The token to encrypt the streaming is configured via a script on the origin server, enabling the Secure Token option in the CDN Resource settings according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token" target="_blank">Configure and use Secure Token</a>" guide.

## Method 2: Streaming via the Streaming Platform with CDN

Use this method if a stream from your server is not in HLS format.

Streaming via our Streaming Platform has advantages and additional features, such as:

*   <a href="https://gcore.com/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos" target="_blank">Live stream recording</a> records the broadcast and saves it as VOD.
*   <a href="https://gcore.com/docs/streaming-platform/live-streaming/pause-and-rewind-the-live-streams" target="_blank">DVR</a> allows you to rewind the stream, stop it and return to viewing it later.
*   <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media" target="_blank">Restreaming</a> allows you to send a broadcast to several media services simultaneously, such as Facebook and YouTube.
*   <a href="https://gcore.com/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player" target="_blank">Own player and statistics</a> allow you to collect statistics on views, geography, and popularity of individual broadcasts.
*   <a href="https://gcore.com/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos" target="_blank">Ads</a> allow you to integrate advertisements into a video or broadcast using five types of playback (pre-roll, mid-roll, etc)


The formats and specifications supported by the Streaming Platform are described in the <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">article</a>.

When you stream via the Streaming platform, there are two ways to send us the stream: PUSH and PULL.

- To use PULL, you need a server with a stream in RTMP (or other) format. The stream is sent to our servers, which convert it into HLS.
- Use PUSH if you stream directly from your computer, camera, or any other device using third-party <a href="https://gcore.com/docs/streaming-platform/live-streaming/push-live-streams-software/push-live-streams-via-obs" target="_blank">software</a>. In this case, there is a unique key in your Control panel that you insert into your program, and the stream is sent to us. The Streaming Platform converts it into HLS and sends it to end-users.

We can receive SRT streams in either PULL or PUSH format. To send us PULL-SRT, just specify a link in the required protocol in the URL field. If you want to get a PUSH link to send SRT streams to us, write to support via [support@gcore.com](mailto:support@gcore.com) or your manager. We will set up an SRT-PUSH link on your account.

About PULL and PUSH in detail, you can read in the "<a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">Create a live stream</a>" guide (step 3.2).