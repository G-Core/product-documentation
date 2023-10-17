---
title: configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs
displayName: Streaming via CDN (for paid tariffs)
published: true
order: 130
toc:
   --1--Conditions: "conditions-for-streams-and-videos-delivery-via-cdn"
   --1--Configure: "configure-the-delivery-of-streams-or-videos-via-cdn"
   --2--1. Send the request: "1-send-the-request"
   --2--2. Create a CDN resource: "2-create-a-cdn-resource"
   --2--3. Set cache settings: "3-set-cache-settings"
   --2--4. Integrate the stream with CDN: "4-integrate-the-stream-with-cdn"
   --2--5. Turn on the preset (only for streams): "5-turn-on-the-preset-only-for-streams" 
   --2--6. Share your stream or videos: "6-share-your-stream-or-videos"
pageTitle: Setting up CDN for Live Streams and Videos | Gcore
pageDescription: A comprehensive guide to configure live streams and video delivery via CDN.
---
# Configure live streams and video delivery via CDN (only for paid tariffs)
  
## Conditions for streams and videos delivery via CDN

If your live stream or videos are in HLS format, they can be proxied to end users via CDN servers to speed up the loading time. It’s possible because the HLS protocol is based on HTTP. It’s cached and distributed via CDNs like regular static files.

You can use a CDN service for streaming if the following conditions are met:

- You stream in HLS format
- You use Start, Pro 5 TB, or Pro 10 TB subscription

If your stream is in another format (RTMP, SRT, MP4), use the <a href="https://gcore.com/streaming-platform" target="_blank">Streaming</a> service.

## Configure the delivery of streams or videos via CDN

### 1. Send the request

Send us a request to activate the streaming workflow for the CDN at [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of our website. Please specify your ID in the request, so we can identify your account. You can find it on the main page of your control panel.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs/12947023694225.png" alt="Send the request" width="80%">

In the request, provide the following information:

- The domain of your website and company name
- The type of content you’re going to stream: Football games, educational content, series, etc.
- A sample of a typical stream URL
- The end users’ geography
- A broadcasting license if you create content yourselves or an illegal content policy if you are an intermediary (e.g., a video hosting platform).
- An email for prompt response to complaints from copyright holders and other authorities

We’ll notify you when we activate the workflow. After that, you’ll be able to configure streaming.

### 2. Create a CDN resource

Create a CDN resource according to the "<a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Create a CDN resource for only static files</a>" guide.

### 3. Set cache settings

Set short-term cache settings for the following types of HLS video files:

- *.ts* extension. Each such file consists of small segments of the stream.
- *.m3u8* extension. Each such file consists of information about the stream and the list of video segments in order. These files are also called playlists.

Firstly, the browser requests a playlist (.m3u8) and then playback segments (.ts) in the order they’re listed in the playlist.

**Segments (.ts) should be cached for 1 minute**. This period is a bit longer than the length of each video segment. It’s necessary for end users with a slow internet connection. When they receive the playlist with the list of the segments from the CDN server, it may already be outdated, and the origin of the CDN resource may have a new playlist with current segments. So, if segments are cached for less than 1 minute, the end user’s browser sends a request to the outdated segments from the origin, and it’ll receive a 404 error because these files don’t exist.

**Playlists (.m3u8) should be cached for 1–2 seconds**. This period should be very short, so that end users don’t receive the playlist with old segments from the cache.

You can set cache settings either on your origin (in the Cache-Control HTTP header) or in the control panel.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs/11775065795729.png" alt="set cache settings" width="80%">

1.  Go to the Resource settings and then the "Rules" section.
2.  Click **Create rule**.
3.  Select **Video segments template (.ts)**. A new page will open. Click **Create rule**. Repeat actions for **the Playlists template (.m3u8)**.

### 4. Integrate the stream with CDN

Change your domain address URLs from the origin to your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CDN domain name</a>. For example, ```http://domain/playlist.m3u8`` (a stream URL from origin) → ```http://cdn.domain/playlist.m3u8``` (a stream URL from the CDN).

You can check your stream on any player that supports online HLS streaming (for example, <a href="https://videolan.org" target="_blank">VLC</a>).

### 5. Turn on the preset (only for streams)

If you’re going to deliver videos (VOD), go to the next step. To reduce the load on CDN servers, turn on the Live streaming preset. It allows configuring file caching through RAM instead of through hard drives.

To do this, go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> list. Click the three dots next to the resource and choose **Turn on LIVE STREAMING preset**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs/12947072884881.png" alt="CDN resources list.">

### 6. Share your stream or videos

Publish the updated [stream URL](https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs#4-integrate-the-stream-with-cdn) on your website. If you expect more than 100 viewers simultaneously, we recommend you activate the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> option to reduce the load on your origin.
