---
title: create-a-live-stream
displayName: Create a live stream
published: true
order: 10
toc:
   --1--1. Initiate process: "initiate-the-process"
   --1--2. Set type and features: "step-2-set-the-stream-type-and-additional-features"
   --1--3. Configure push, pull, or WebRTC to HLSl: "step-3-configure-your-stream-for-push-pull-or-webrtc-to-hls"
   --2--Push ingest type: "push-ingest-type" 
   --2--Pull ingest type : "pull-ingest-type"
   --2--WebRTC to HLS ingest type: "webrtc-to-hls-ingest-type"   
   --1--4. Start stream: "step-4-start-the-stream"
   --1--5. Embed to app: "step-5-embed-the-stream-to-your-app" 
pageTitle: Guide to Creating Live Streams | Gcore
pageDescription: A step-by-step tutorial on how to create live streams using Gcore's interface. Learn about stream types, encoder settings, and embedding options.
---
# Create a live stream

## Step 1. Initiate the process

1\. In the Gcore Customer Portal, navigate to <a href="https://streaming.gcore.com/streaming">Streaming</a> > **Live Streaming**.

2\. Click **Create Live stream**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-streaming-annotated.png" alt="Live stream button on the life streaming page" width="80%">

<expandable-element title="The Create… button is unavailable">

If the button is non-responsive, you have exceeded your live stream limit. To create a new stream, remove an existing stream from the list or request [technical support](mailto:support@gcore.com) to increase your limits.

</expandable-element>

2\. Enter the name of your live stream in the window that appears and click **Create**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/9651635790481.png" alt="Enter the name of your live stream" width="50%">

A new page will appear. Perform the remaining steps there. 

## Step 2. Set the stream type and additional features 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-settings.png" alt="Live stream page" width="80%">

1\. Make sure that the **Enable live stream** toggle is on.

<expandable-element title="Low latency explanation">

By default, we offer live streams with low latency (a 4–5 second delay.) Low latency is available in two protocols: LL-DASH (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">compatible with all devices except iOS</a>) and LL-HLS (compatible with iOS). You can also obtain legacy HLS with MPEGTS format segments, in which case, please read <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">our article</a>.

</expandable-element>

2\. (Optional) Review the live stream name and update it if needed.

3\. Enable additional features If you activated them previously: 

* <a href="https://gcore.com/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos" target="_blank">Record</a> for live stream recording. It will be active when you start streaming. Remember to enable the toggle if you require a record of your stream.  
* <a href="https://gcore.com/docs/streaming-platform/live-streaming/pause-and-rewind-the-live-streams" target="_blank">DVR</a> for an improved user experience. When the DVR feature is enabled, your viewers can pause and rewind the broadcast.

4\. Select the relevant stream type: **Push**, **Pull**, or **WebRTC => HLS**.

* Choose **Push** if you don't use your own media server. Establish the URL of our server and the unique stream key in your encoder (e.g. OBS, Streamlabs, vMix, or LiveU Solo). You can use protocols RTMP, RTMPS, and SRT too. The live stream will operate on our server, will be converted to MPEG-DASH and HLS protocols, and will be distributed to end users via our CDN.

* Choose **Pull** if you have a streaming media server. The live stream will operate on your server. Our server will convert it from the RTMP, RTMPS, SRT, or other protocols to MPEG-DASH and HLS protocols. Then, our CDN will distribute the original live stream in the new format to end users.

* Choose **WebRTC => HLS** if you want to convert your live video stream from WebRTC to HLS (HTTP Live Streaming) and DASH (Dynamic Adaptive Streaming over HTTP) formats.  

## Step 3. Configure your stream for push, pull, or WebRTC to HLS

### Push ingest type

1\. Select the protocol for your stream: **RTMP**, **RTMPS**, or **SRT**. The main difference between these protocols is their security levels and ability to handle packet loss.

- RTMP is the standard open-source protocol for live broadcasting over the internet. It supports low latency. 
- RTMPS is a variation of RTMP that incorporates SSL usage.
- SRT is a protocol designed to transmit data reliably with protection against packet loss.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/push-ingest-type-encoder-urls.png" alt="URLs for encoder configuration" width="80%">

2\. Copy the relevant data to insert into your encoder.

<expandable-element title="RTMP(S)">

Insert the following values:

- **Server (URL)** is the target server where your encoder will relay the broadcast; e.g., ```rtmp://vp-push-ed1.gvideo.co/in/ ```.
- **Stream key** is the unique identifier of the created live stream.

</expandable-element>

<expandable-element title="SRT">

Copy the Push URL SRT. It contains the server URL, port, stream ID (internal for Gcore,) and stream key. For example:

```
srt://vp-push-ed1-srt.gvideo.co:5001?streamid=000000#12ab345c678901d…
```

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/srt.png" alt="SRT configuration" width="80%">

</expandable-element>

<expandable-element title="Backup links">

We provide backup links, which you can specify in the encoder interface. In case of inaccessibility and overloading of your primary server, the stream will be minimally interrupted and will continue automatically from the backup server.

</expandable-element>

### Pull ingest type

In the **URL** field, insert a link to the stream from your media server. Check the full list of supported protocols in our <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">Input parameters</a> guide.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/pull-ingest-type.png" alt="Live streaming section" width="80%">

<alert-element type="tip" title="Tip">

You can specify multiple media servers separated by space in the URL field. 

In this case, the first media server will be the primary source, and the subsequent ones will serve as backup servers. If the signal from the first source fails, we will automatically continue the stream from the second source. For example: `rtmps://main-server/live1 rtmp://backup-server/live1 rtmp://backup-server/live2`.

</alert-element>

### WebRTC to HLS ingest type

Insert the link from the WHIP URL field to any library or tool that supports WHIP (WebRTC-HTTP Ingestion Protocol). This will convert your stream into HLS format.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/webrtc-hls.png" alt="WebRTC to HLS settings" width="80%">

## Step 4. Start the stream

Start a live stream on your media server or encoder. You will see a streaming preview on the Gcore Live Stream Settings page if everything is configured correctly.

## Step 5. Embed the stream to your app

Embed the created live stream into your web app by one of the following methods:

- Copy the iframe code to embed the live stream within the Gcore built-in player.
- Copy the export link in a suitable protocol and paste it into your player. Use the **LL-DASH** link if your live stream will be viewed from any device except iOS. Use **LL HLS** for iOS viewing.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/embed-to-app.png" alt="Links for embeding them to the app" width="80%">

That’s it. Your viewers can see the live stream.

<alert-element type="warning" title="Warning">

We only support <a href="https://gcore.com/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing" target="_blank">statistic data</a> collection for Gcore players. If you use your own, non-Gcore player, the statistics page will be empty. Independent of the player, you can view <a href="https://gcore.com/docs/streaming-platform/live-streaming/view-your-live-stream-metrics" target="_blank">monitoring metrics</a> for performance analysis and troubleshooting. 

</alert-element>