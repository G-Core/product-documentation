---
title: create-a-live-stream
displayName: Create a live stream
published: true
order: 10
toc:
pageTitle: Guide to Creating Live Streams | Gcore
pageDescription: A step-by-step tutorial on how to create live streams using Gcore's interface. Learn about stream types, encoder settings, and embedding options.
---
# Create a live stream

1\. Go to the <a href="https://streaming.gcore.com" target="_blank">Live streaming</a> section in the Streaming tab and click **Create Live stream**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13542247871633.png" alt="Live streaming section">

2\. Enter the name of your live stream in the window that appears and click **Create**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/9651635790481.png" alt="Enter the name of your live stream" width="50%">

If the button is un-clickable, you have reached your live stream limit. To create a new stream, delete an existing stream from the list.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/9651664092049.png" alt="live stream limit" width="80%">

A new page will open. Do the remaining steps connected with Gcore’s interface in it. 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/create-live.png" alt="Live streaming settings">

**3.1.** Ensure the **Enable live stream (with Low Latency)** switch is turned on.

By default, we provide live streams with Low Latency (4–5 seconds of delay). Low Latency is available in two protocols: <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">LL-DASH (works on any devices except iOS) and LL-HLS (works on iOS)</a>. If you need to stream in regular HLS (8–10 seconds of delay), contact the [support team](mailto:support@gcore.com) or your personal manager for enabling.

**3.2.** Choose the appropriate stream type: Push or Pull. 

- The **Pull stream type** will suit you if you have a streaming media server. The live stream will be running on your server. Our server will convert it from the RTMP, RTSP, or SRT protocol to the Low Latency protocols. Furthermore, our CDN will deliver the initial live stream in the new format to end users.
- The **Push stream type** will suit you if you don’t use your own media server. Set the URL of our server and the unique stream key in your <a href="https://gcore.com/docs/streaming-platform/live-streaming/push-live-streams-software/push-live-streams-via-obs" target="_blank">encoder</a> (like OBS, LiveU Solo, and others). After that, the live stream will run on our server, be converted to HLS or CMAF (Low Latency) format, and be delivered to end users via our CDN.

**3.3.** Edit the name of the live stream from step#2 if necessary.

**3.4.** Enable additional features If you activated them earlier:

- <a href="https://gcore.com/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos" target="_blank">Record</a> for live stream recording.
- <a href="https://gcore.com/docs/streaming-platform/live-streaming/pause-and-rewind-the-live-streams" target="_blank">DVR</a> to allow viewers to pause the broadcast.  

The next step of the guide depends on the stream type you’ve chosen: Pull or Push (3.2).

4\. Set up the live stream.

**(If you selected Pull)** Put a link to a stream from your media server in the URL field.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13542997210897.png" alt="Live streaming section" width="50%">

You can specify in the URL field several media servers separated by space. In this case, the first media server will be used as the primary source and the next as backup servers. If the signal from the first source cuts out, we will automatically resume the stream from the second source.

**(If you selected Push)** Select the encoder that you will use for streaming from the drop-down list. Copy the server URL and Stream Key. In the screenshot below, *rtmp://vp-push-ed1.gvideo.co/* is the server URL while *425969?7395…* is the stream key.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13543145952785.png" alt="encoder" width="50%">

Insert the copied values in the interface of your encoder according to the appropriate instructions from the "Push live streams software" section.

5\. Start a live stream on your media server or encoder. If everything is configured correctly, you will see a streaming preview in the player.

6\. Use the appropriate way to embed the created live stream into your web application:

- Copy the iFrame code to embed the live stream within the built-in player.
- Copy the export link in the needed protocol to paste it into your player. Use the **LL-DASH** link if your live stream will be viewed from any device except iOS. Use **LL HLS** for iOS viewing.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13543414027409.png" alt="live streams" width="80%">

Then your viewers see the live stream.

<a href="https://gcore.com/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing" target="_blank">Statistical data</a> can only be collected if you stream via our player. If you use your player, the statistics page will be empty.