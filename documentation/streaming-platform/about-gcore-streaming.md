---
title: about-gcore-streaming
displayName: Overview
published: true
order: 10
toc:
   --1--Streaming directly via CDN: "method-1-streaming-directly-via-cdn"
   --1--Streaming via the Streaming platform: "method-2-streaming-via-the-streaming-platform-with-cdn"
---
  

Method 1: Streaming directly via CDN
------------------------------------

If you have your own media server that produces a stream in HLS format, you will need one CDN resource with special settings for playlists (.m3u8) and chunks (.ts). For more information about settings, see the article [Live streaming via CDN using the HLS protocol.](https://gcore.com/support/articles/115002080125/)

You can protect the stream with a token. The token to encrypt the streaming is configured via a script on the origin server, enabling the Secure Token option in the CDN Resource settings according to the "[Secure Token. Configure and use](https://gcore.com/support/articles/6419123497873/)" guide.

Method 2: Streaming via the Streaming platform with CDN
-------------------------------------------------------

Use this method if a stream from your server is not in HLS format.

Streaming via our Streaming Platform has advantages and additional features, such as:

*   [Live stream recording](https://gcore.com/support/articles/360000522817/) records the broadcast and saves it as VOD.
*   [DVR](https://gcore.com/support/articles/360000615029/) allows you to rewind the stream, stop it and return to viewing it later.
*   [Restreaming](https://gcore.com/support/articles/9394950026257/) allows you to send a broadcast to several media services simultaneously, such as Facebook and YouTube.
*   [Own player and statistics](https://gcore.com/support/articles/5523465324945/) allow you to collect statistics on views, geography, and popularity of individual broadcasts.
*   [Ads](https://gcore.com/support/articles/360000472537/) allow you to integrate advertisements into a video or broadcast using five types of playback (pre-roll, mid-roll, etc.)

The formats and specifications supported by the Streaming platform are described in the [article](https://gcore.com/support/articles/360000604025/).

When you stream via the Streaming platform, there are two ways to send us the stream: PUSH and PULL.

*   To use PULL, you need a server with a stream in RTMP (or other) format. The stream is sent to our servers, which convert it into HLS.
*   Use PUSH if you stream directly from your computer, camera, or any other device using third-party [software](https://gcore.com/support/sections/360000084517/). In this case, there is a unique key in your Control panel that you insert into your program, and the stream is sent to us. The streaming platform converts it into HLS and sends it to end-users.

We can receive SRT streams in either PULL or PUSH format. To send us PULL-SRT, just specify a link in the required protocol in the URL field. If you want to get a PUSH link to send SRT streams to us, write to support via [support@gcore.com](mailto:support@gcore.com) or your manager. We will set up an SRT-PUSH link on your account.

About PULL and PUSH in detail, you can read in the "[Create a live stream"](https://gcore.com/support/articles/5307972492945/) guide (step 3.2).

You can protect the stream with a token. The token to encrypt the streaming is configured via a script on the origin server, enabling the Secure Token option in the CDN Resource settings according to the "[Secure Token: protect live streams and VOD with temporary links](https://gcore.com/support/articles/360002209478/)" guide.