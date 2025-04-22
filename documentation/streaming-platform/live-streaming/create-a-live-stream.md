---
title: create-a-live-stream
displayName: Create a live stream
published: true
order: 10
toc:
    --1--1. Initiate process: 'initiate-the-process'
    --1--2. Set type and features: 'step-2-set-the-stream-type-and-additional-features'
    --1--3. Configure ingest type and additional features: 'step-3-configure-ingest-type-and-additional-features'
    --1--4. Start stream: 'step-4-start-the-stream'
    --1--5. Embed to app: 'step-5-embed-the-stream-to-your-app'
pageTitle: Guide to Creating Live Streams | Gcore
pageDescription: A step-by-step tutorial on how to create live streams using Gcore's interface. Learn about stream types, encoder settings, and embedding options.
---

# Create a live stream

## Step 1. Initiate the process

1\. In the **Gcore Customer Portal**, navigate to **Streaming** > <a href="https://portal.gcore.com/streaming/streaming/list" target="_blank">**Live Streaming**</a>.

2\. Click the **Create Live stream** button on the top right.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-streaming-annotated.png" alt="Live stream button on the life streaming page" width="80%">

<expandable-element title="The Create… button is unavailable">

If the button is non-responsive, you have exceeded your live stream limit. To create a new stream, remove an existing stream from the list or request [technical support](mailto:support@gcore.com) to increase your limits.

</expandable-element>

2\. Enter the name of your live stream in the window that appears and click the **Create** button.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/9651635790481.png" alt="Enter the name of your live stream" width="50%">

A new page will appear. Perform the remaining steps there.

## Step 2. Set the ingest type and additional features

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-settings-push.png" alt="Live stream page" width="80%">

1\. Make sure that the **Enable live stream** toggle is on.

<expandable-element title="Low latency explanation">

By default, we offer live streams with low latency (a 4–5 second delay.) Low latency is available in two protocols: LL-DASH (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">compatible with all devices except iOS</a>) and LL-HLS (compatible with iOS). You can also obtain legacy HLS with MPEGTS format segments, in which case, please read <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">our article</a>.

</expandable-element>

2\. Review the live stream name and update it if needed.

3\. Enable additional features:

-   <a href="https://gcore.com/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos" target="_blank">Record</a> for live stream recording. It will be active when you start streaming. Remember to enable the toggle if you require a record of your stream.
-   <a href="https://gcore.com/docs/streaming-platform/live-streaming/pause-and-rewind-the-live-streams" target="_blank">DVR</a> for an improved user experience. When the DVR feature is enabled, your viewers can pause and rewind the broadcast.

4\. Select the relevant **Ingest type**: **Push** or **Pull**.

-   Choose **Push** if you don't use your own media server. Establish the URL of our server and the unique stream key in your encoder (e.g. OBS, Streamlabs, vMix, or LiveU Solo). You can use protocols RTMP, RTMPS, and SRT too. The live stream will operate on our server, will be converted to MPEG-DASH and HLS protocols, and will be distributed to end users via our CDN.

-   Choose **Pull** if you have a streaming media server. The live stream will operate on your server. Our server will convert it from the RTMP, RTMPS, SRT, or other protocols to MPEG-DASH and HLS protocols. Then, our CDN will distribute the original live stream in the new format to end users.

## Step 3. Configure your stream

Depending on the selcected ingest type and protocol, your settings will differ. Refer to specific
protocol pages for more details:

-   <a href="https://gcore.com/docs/streaming-platform/live-streaming/protocols/rtmp" target="_blank">RTMP/RTMPS</a>
-   <a href="https://gcore.com/docs/streaming-platform/live-streaming/protocols/srt" target="_blank">SRT</a>
-   <a href="https://gcore.com/docs/streaming-platform/live-streaming/protocols/webrtc-to-hls-encoding" target="_blank">WebRTC to HLS</a>

## Step 4. Start the stream

Start a live stream on your media server or encoder. You will see a streaming preview on the **Live Stream Settings** page if everything is configured correctly.

## Step 5. Embed the stream to your app

Embed the created live stream into your web app by one of the following methods:

-   Copy the iframe code to embed the live stream within the Gcore built-in player.
-   Copy the export link in a suitable protocol and paste it into your player. Use the **LL-DASH** link if your live stream will be viewed from any device except iOS. Use **LL HLS** for iOS viewing.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/embed-to-app.png" alt="Links for embeding them to the app" width="80%">

That’s it. Your viewers can see the live stream.

<alert-element type="warning" title="Warning">

We only support <a href="https://gcore.com/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing" target="_blank">statistic data</a> collection for Gcore players. If you use your own, non-Gcore player, the statistics page will be empty. Independent of the player, you can view <a href="https://gcore.com/docs/streaming-platform/live-streaming/view-your-live-stream-metrics" target="_blank">monitoring metrics</a> for performance analysis and troubleshooting.

</alert-element>
