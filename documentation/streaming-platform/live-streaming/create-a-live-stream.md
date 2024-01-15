---
title: create-a-live-stream
displayName: Create a live stream
published: true
order: 10
toc:
   --1--1. Start creation: "step-1-start-creation"
   --1--2. Set type and features: "step-2-set-the-stream-type-and-additional-features"
   --1--3. Configure Push or Pull: "step-3-configure-your-stream-for-push-or-pull"
   --2--Pull: "if-you-selected-pull" 
   --2--Push: "if-you-selected-push"
   --1--4. Start stream: "step-4-start-the-stream"
   --1--5. Embed to app: "step-5-embed-the-stream-to-your-app" 
pageTitle: Guide to Creating Live Streams | Gcore
pageDescription: A step-by-step tutorial on how to create live streams using Gcore's interface. Learn about stream types, encoder settings, and embedding options.
---
# Create a live stream

## Step 1. Start creation

1\. Navigate to the <a href="https://streaming.gcore.com/streaming/list">Live streaming</a> section and select **Create Live stream**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13542247871633.png" alt="Live streaming section" width="80%">

<expandable-block title="The Create… button is unavailable">

If the button is non-responsive, you have exceeded your live stream limit. To create a new stream, remove an existing stream from the list or request [technical support](mailto:support@gcore.com) to increase your limits.

</expandable-element>


2\. Enter the name of your live stream in the window that appears and click **Create**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/9651635790481.png" alt="Enter the name of your live stream" width="50%">

A new page will appear. Do the remaining steps connected with Gcore’s interface in it. 

## Step 2. Set the stream type and additional features 

1\. Ensure the **Enable live stream** switch is on.

<expandable-block title="Low Latency explanation">

By default, we offer live streams with Low Latency (a 4–5 second delay). Low Latency is available in two protocols: LL-DASH (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">compatible with all devices except iOS</a>) and LL-HLS (compatible with iOS). Also, you can obtain legacy HLS with MPEGTS format segments. If you need it, read <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">our article</a>.

</expandable-element>

2\. (Optional) Review the live stream name and modify if necessary.

3\. Select the suitable stream type: Push or Pull. 

- The **Pull stream type** will suit you if you have a streaming media server. The live stream will operate on your server. Our server will convert it from the RTMP, RTMPS or SRT protocol to  MPEG-DASH and HLS protocols. After that, our CDN will distribute the original live stream in the new format to end users.

- The **Push stream type** will suit you if you do not use your own media server. Establish the URL of our server and the unique stream key in your encoder (e.g., OBS, Streamlabs, vMix, LiveU Solo, etc). You can use protocols RTMP, RTMPS, and SRT too. Following this, the live stream will operate on our server, be converted to MPEG-DASH and HLS protocols, and be distributed to end users via our CDN.

4. Enable additional features If you activated them earlier:

- <a href="https://gcore.com/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos" target="_blank">Record</a> for live stream recording. It will be active when you start streaming. Remember to enable the toggle if you require a record of your stream.  
- <a href="https://gcore.com/docs/streaming-platform/live-streaming/pause-and-rewind-the-live-streams" target="_blank">DVR</a> for an improved user experience: when the DVR feature is enabled, your viewers can pause and rewind the broadcast.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/stream-settings.png" alt="Live stream page" width="80%">


## Step 3. Configure your stream for Push or Pull 

### If you selected Pull

Insert a link to a stream from your media server in the URL field.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/13542997210897.png" alt="Live streaming section" width="50%">

> **Tip**: You can specify multiple media servers separated by space in the URL field. In this case, the first media server will be the primary source, and the subsequent ones will serve as backup servers. If the signal from the first source fails, we will automatically continue the stream from the second source. Example: “rtmps://main-server/live1 rtmp://backup-server/live1 rtmp://backup-server/live2”.

### If you selected Push

1\. Select the encoder (OBS, VMix, Wirecast) you use for streaming from the drop-down list. 

2\. Select the protocol for your stream: RTMP, RTMPS, or SRT. The main difference between these protocols is their security levels and ability to handle packet loss.

- RTMP is the standard open-source protocol for live broadcasting over the Internet which supports low latency. 
- RTMPS is a variation of RTMP but incorporates SSL usage. 
- SRT is a protocol designed to transmit data reliably with protection against packet loss.

3\. Copy the relevant data to insert into your encoder.

<expandable-element title="RTMP(S)">

Copy the following values:

- **Server (URL)** is the target server where your encoder will relay the broadcast. E.g., ```rtmp://vp-push-ed1.gvideo.co/in/ ```
- **Stream key** is the unique identifier of the created live stream

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/rtmps.png" alt="URLs for encoder configuration" width="80%">

</expandable-element>

<expandable-element title="SRT">

Copy Push URL SRT. It will contain the server URL, port, stream ID (internal for Gcore), and stream key. For example:

```
srt://vp-push-ed1-srt.gvideo.co:5001?streamid=000000#12ab345c678901d…
```

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/srt.png" alt="SRT configuration" width="80%">

</expandable-element>

<expandable-element title="Backup links">

We provide backup links. You can specify it in the encoder interface. In case of inaccessibility and overloading of your primary server, the stream will be minimally interrupted and continue from the backup server.

</expandable-element>

## Step 4. Start the stream

Start a live stream on your media server or encoder. You will see a streaming preview on the Gcore Live stream settings page if everything is configured correctly.

## Step 5. Embed the stream to your app

Embed the created live stream into your web app by one of the following methods:

- Copy the iframe code to embed the live stream within the Gcore built-in player.
- Copy the export link in a suitable protocol and paste it into your player. Use the **LL-DASH** link if your live stream will be viewed from any device except iOS. Use **LL HLS** for iOS viewing.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/embed-to-app.png" alt="Links for embeding them to the app" width="80%">

That’s it. Your viewers see the live stream.

> **Warning**: We support <a href="https://gcore.com/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing" target="_blank">statistic data</a> collection only for Gcore players. If you use your player, the statistics page will be empty. Independently from the player, you can view <a href="https://gcore.com/docs/streaming-platform/live-streaming/view-your-live-stream-metrics" target="_blank">monitoring metrics</a> for performance analysis and troubleshooting. 