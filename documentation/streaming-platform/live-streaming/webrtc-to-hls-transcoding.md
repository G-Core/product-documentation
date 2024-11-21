---
title: webrtc-to-hls-transcoding
displayName: WebRTC ingest and transcoding to HLS/DASH
published: true
order: 15
toc:
   --1--Benefits of WebRTC and HLS/DASH conversion: "advantages-of-webrtc-andconversion-to-hls-dash"
   --1--How it works: "how-it-works"
   --1--WebRTC stream encoding parameters: "webrtc-stream-encoding-parameters"
   --2--Supported WHIP clients: "supported-whip-clients"
   --2--LL-HLS and LL-DASH outputs: "ll-hls-and-ll-dash-outputs"
   --1--Convert WebRTC in the Customer Portal: "convert-webrtc-to-hls-in-the-customer-portal"
   --1--Convert WebRTC in your environment: "convert-webrtc-to-hls-in-your-environment"
   --2--With the WebRTC WHIP library: "start-a-stream-with-the-gcore-webrtc-whip-library"
   --2--With your backend or frontend: "start-a-stream-with-your-own-backend-or-frontend"
   --2--Play HLS or DASH: "play-hls-or-dash"
   --2--Deactivate a stream: "deactivate-a-finished-stream"
   --2--Demo projects: "demo-projects-of-streaming-with-frontend-and-backend"
   --1--Troubleshooting: "troubleshooting"
   --2--Error handling: "error-handling"
   --2--Sudden disconnection of camera or microphone: "sudden-disconnection-of-camera-or-microphone"
   --2--Debugging with Chrome WebRTC internals: "debugging-with-chrome-webrtc-internals-tool"
   --2--Network troubleshooting: "network-troubleshooting"
pageTitle: Guide to Creating Live Streams | Gcore
pageDescription: A step-by-step tutorial on how to create live streams using Gcore's interface. Learn about stream types, encoder settings, and embedding options.
---
# WebRTC ingest and transcoding to HLS/DASH

Streaming videos using HLS and MPEG-DASH protocols is a simple and cost-effective way to show your video to large audiences. However, this requires the original streams to be in a certain format that browsers do not support natively. 

At the same time, WebRTC protocol works in any browser, but it’s not as flexible when streaming to large audiences. 

Gcore <a href="https://gcore.com/streaming-platform" target="_blank">Video Streaming</a> supports both WebRTC HTTP Ingest Protocol (WHIP) and WebRTC to HLS/DASH converter, giving you the advantages of these protocols. 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/diagram-whip-hls-protocols-supported.png" alt="A diagram depicting WebRTC converting to LL-HLS/DASH" width="80%">

## Advantages of WebRTC and conversion to HLS/DASH

WebRTC ingest for streaming offers two key advantages over traditional RTMP and SRT protocols: 

1\. It runs directly in the presenter's browser, so no additional software is needed. 

2\. WebRTC can reduce stream latency. 

By using WebRTC WHIP for ingest, you can convert  WebRTC to HLS/DASH playback, which provides the following benefits: 

* Fast ingest via WebRTC from a browser. 
* Optimal stream distribution using HLS/DASH with <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-after-transcoding-bitrate-frame-rate-and-codecs#what-is-transcoding-with-abr" target="_blank">adaptive bitrate streaming</a> (ABR) through the CDN. 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/diagram-how-transcoding-is-configured.png" alt="A diagram depicting WebRTC transcoding and distribution via HLS/DASH" width="80%">

## How it works 

We use a dedicated WebRTC WHIP server to manage WebRTC ingest. This server handles both signaling and video data reception. Such a setup allows you to configure WebRTC on demand and continue to use all system capabilities to set up transcoding and delivery via CDN.  

The RTC WHIP server organizes signaling and receives video data. Signaling refers to the communication between WebRTC endpoints that are necessary to initiate and maintain a session. WHIP is an open specification for a simple signaling protocol that starts WebRTC sessions in an outgoing direction, such as streaming from your device. 

We use local servers in each region to ensure a minimal route from a user-presenter to the server. 

### WebRTC stream encoding parameters 

The stream must include at least one video track and one audio track: 

* Video must be encoded using H.264.
* Audio must use OPUS codec. 

If you use <a href="https://obsproject.com/" target="_blank">OBS</a> or your own WHIP library, use the following video encoding parameters: 

* Codec H.264 with no B-frames and fast encoding: 
  * **Encoder**: x264, or any of H.264 
  * **CPU usage**: veryfast
  * **Keyframe interval**: 1 sec
  * **Profile**: baseline
  * **Tune**: zerolatency 
  * **x264 options**: bframes=0 scenecut=0 

* Bitrate:  
  * The lower the bitrate, the faster the data will be transmitted to the server. Choose the optimal one for your video. For example, 1-2 Mbps is usually enough for video broadcasts of online training format or online broadcasts with a presenter. 

For example, you might have the following settings in OBS:

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/example-obs-settings.png" alt="Example of listed OBS settings" width="80%">

### Supported WHIP clients

You can use any libraries to send data via the WebRTC WHIP protocol. 

* Gcore WebRTC WHIP client 
* <a href="https://obsproject.com/" target="_blank">OBS</a> (Open Broadcaster Software)
* <a href="https://web.whip.eyevinn.technology/" target="_blank">@eyevinn/whip-web-client</a>
* <a href="https://github.com/ggarber/whip-go" target="_blank">whip-go</a>
* Larix Broadcaster (free apps for iOS and Android with WebRTC based on Pion; SDK is available) 

### LL-HLS and LL-DASH outputs

Streams sent via WebRTC are transcoded in the way as other streams received via RTMP and SRT.  

At the output, you can view the streams using any available protocols: 

* **MPEG-DASH**: ±2-4 seconds latency to a viewer with ABR.
* **LL-HLS**: ±3-4 seconds latency to a viewer with ABR.
* **HLS MPEG-TS**: legacy with <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works#switch-to-legacy-hls-modes" target="_blank">non-low-latency</a> (±10 seconds latency) with ABR.  

For WebRTC mode, we use a method of constant transcoding with an initial given resolution. This means that if WebRTC in a viewer’s browser reduces the quality or resolution of the master stream (for example, to 360p) due to restrictions on the viewer's device (such as network conditions or CPU consumption), the transcoder will continue to transcode the reduced stream to the initial resolution (for example 1080p ABR).

When the restrictions on the viewer's device are removed, quality will improve again.  

<alert-element type="tip" title="Tip">
 
For more details about low-latency streaming, check out <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-low-latency-streaming-works" target="_blank">How low-latency streaming works</a>. 
 
</alert-element>

## Convert WebRTC to HLS in the Customer Portal

For instructions on how to convert a stream via API, refer to the <a href="https://api.gcore.com/docs/streaming#tag/Streams/operation/get_streams_id" target="_blank">API documentation</a>.  

1\. In the Gcore Customer Portal, navigate to **Streaming**. 
**
2\. Open the Live Streaming** page and find a needed live stream. If you don’t have one, create a stream first. 

3\. Click the stream name to open its settings.  

4\. In the **Quick start in browser** section, click **Go Live**. The broadcast will start automatically.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/go-live-button.png" alt="Example of live broadcast" width="80%">

5\. Allow Gcore to access your camera and microphone. In several seconds the HLS/DASH stream will appear in an HTML video player.  

You’ll see the result under the **Video preview** instead of a black area with the “No active streams found” message. This large window of an HTML video player is the transcoded version of the stream in HLS/DASH protocols using adaptive bitrate.  

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/started-live-stream.png" alt="Example of a fully launched stream" width="80%">

A small window in the top-right corner is from your camera. It shows the stream taken from the webcam. 

There are also settings for selecting a camera and microphone if you have more than one option on your device. 

## Convert WebRTC to HLS in your environment

We provide a <a href="https://rtckit.gvideo.io/0.72.0/index.esm.js" target="_blank">WebRTC WHIP library</a> for working in browsers. It implements the basic system calls and simplifies working with WebRTC: 

* Wrapper for initializing WebRTC stream and connecting to the server. 
* Camera and mic wrapper. 
* Monitoring WebRTC events and calling appropriate handlers in your code. 

The latest library version, 0.72.0, is available at https://rtckit.gvideo.io/0.72.0/index.esm.js.

### Start a stream with the Gcore WebRTC WHIP library

Since WHIP is an open standard, many libraries have been released for it in different languages. You can use our <a href="https://rtckit.gvideo.io/0.72.0/index.esm.js" target="_blank">WebRTC WHIP</a> or any other library specified in the <a href="https://gcore.com/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding#supported-whip-clients" target="_blank">WHIP clients</a> section. 

Using our library, you can start the conversion with a few lines of code. To go live  immediately, create a live stream in the Gcore Streaming dashboard and paste a URL into the example linked below: 

1\. In the Gcore Customer Portal, open the <a href="https://portal.gcore.com/streaming/streaming/editor/1740470" target="_blank">Live Streaming</a> page. 

2\. Open the stream settings and copy a WHIP URL from the **WebRTC => HLS parameters** section.

3\. Open <a href="https://stackblitz.com/edit/stackblitz-starters-j2r9ar?file=index.html" target="_blank">WHIP demo app</a> and paste the WHIP URL into the `WHIP_ENDPOINT const`.  

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/copy-paste-whip-endpoint-in-demo-app.png" alt="WHIP endpoint where to paste the info" width="80%">

4\. Click the **Start** button. The steam will be started in Customer Portal. 

You can find the technical reference manual on data types, interfaces, methods, and other components in the <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.md" target="_blank">gcorevideo/rtckit</a> repository. 

### Start a stream with your own backend or frontend

<tabset-element>

#### Backend

To create a new stream, send a POST request to the following endpoint: `https://api.gcore.com/streaming/streams`.

Example request:

<code-block>
curl -L 'https://api.gcore.com/streaming/streams' \ 
-H 'Content-Type: application/json' \ 
-H 'Authorization: APIKey 1111$3ec8…9604e' \ 
-d '{ 
    "name": "WebRTC to HLS demo", 
    "active": true 
}' 
</code-block>
Example response: 

<code-block>
{ 
  "id": 1683264, 
    "name": "WebRTC to HLS demo", 
    "push_url_whip": "https://whip.gvideo.co/1965207_561f4742ec38ae6386a6e7e637c03041/whip",    … 
} 
</code-block>

Use the `“push_url_whip”` value from the response to start the stream. 

#### Frontend WHIP

Get access and data from the microphone and camera:  

<code-block>
import { WebrtcStreaming } from 'https://rtckit.gvideo.io/0.68.2/index.esm.js'; 
const WHIP_ENDPOINT = '{push_url_whip}'; 
const webrtc = new WebrtcStreaming(WHIP_ENDPOINT, {...}); 
</code-block>

Send a local stream to the WHIP server: 

<code-block>
webrtc.openSourceStream({ 
   audio: mic, 
   video: cam, 
   resolution: 1080, 
}) 
</code-block>

Note that if a user stops streaming to the ingester, for example, by closing the browser tab, the stream settings will be terminated. When the user resumes streaming from any browser, the ingester will pick up the stream. However, there will be a brief delay before the ingested stream becomes playable. 

If a user tries to stream to the same endpoint where another user is already streaming, the former will get an error message from the media server. The current stream will remain uninterrupted. 

</tabset-element>

### Play HLS or DASH

After sending the stream from frontend, the stream will start transcoding. In ±2-7 seconds, the HLS and MPEG-DASH versions will be ready for viewing.  

The stream can be viewed through the built-in web player or using direct links to the manifests. You can take these links from the API response.

Examples:

* Web player: https://player.gvideo.co/streams/102748_1965207  
* LL-HLS manifest: https://102748.gvideo.io/cmaf/102748_1965207/master.m3u8  
* DASH manifest: https://102748.gvideo.io/cmaf/102748_1965207/index.mpd 

Send a GET request to the following endpoint: `https://api.gcore.com/streaming/streams/{id}`.

Example request: 

<code-block>
curl -L 'https://api.gcore.com/streaming/streams/1965207' \ 
-H 'Authorization: APIKey 1111$3ec8…9604e'
</code-block>

Example response:

<code-block>
{ 
    "id": 1965207, 
    "iframe_url": "https://player.gvideo.co/streams/102748_1965207", 
    "hls_cmaf_url": "https://demo-public.gvideo.io/cmaf/102748_1965207/master.m3u8", 
    "hls_mpegts_url": "https://demo-public.gvideo.io/mpegts/102748_1965207/master_mpegts.m3u8", 
    "dash_url": "https://demo-public.gvideo.io/cmaf/102748_1965207/index.mpd", 
    … 
} 
</code-block>

### Deactivate a finished stream

<tabset-element>

#### Stop stream on backend

Update the stream sending a PATCH request to the following endpoint: `https://api.gcore.com/streaming/streams/{id}`.

Example request: 

<code-block>
curl -L -X PATCH 'https://api.gcore.com/streaming/streams/1965207' \ 
-H 'Content-Type: application/json' \ 
-H 'Authorization: APIKey 1111$3ec8…9604e' ' \ 
-d '{ 
    "active": false 
}' 
</code-block>

Alternatively, you can delete the stream by sending the DELETE request to `https://api.gcore.com/streaming/streams/$id`.

Example request: 

<code-block>
curl -L -X DELETE 'https://api.gcore.com/streaming/streams/1965207' \ 
-H 'Authorization: APIKey 1111$3ec8…9604e' 
</code-block>

#### Stop stream on frontend

Example command to close the stream: `webrtc.close()`

</tabset-element>

### Demo projects of streaming with frontend and backend

<tabset-element>

#### Demo 1. JavaScript WebRTC WHIP client app

You can find a detailed description of this version above. To view the full code, inspect the https://stackblitz.com/edit/stackblitz-starters-j2r9ar?file=index.html. 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/demo-1-example.png" alt="Example of demo project 1" width="80%">

#### Demo 2. Comprehensive full-stack implementation on Nuxt

This demo depicts a complete frontend and backend implementation with the Nuxt framework. It’s a fully functional prebuilt version with a demo stream from our demo server.  

The implementation includes: stream generation, initialization of WebRTC data in a browser, video transmission from the browser to the server, and displaying the HLS/DASH web player with transcoded broadcast.  

We’ve added the demo instance and source code to help you explore the implementation in action: 

* Demo app – https://gcore-webrtc-sdk-js-nuxt.vercel.app/host?token=123 
* Source code – https://github.com/G-Core/gcore-webrtc-sdk-js/tree/main/apps/ingest-demo-nuxt  

To start streaming: 

1\. Select your camera and microphone  

2\. In the **Host** section, click **Start** under the video preview. 

3\. Click the **Watch** link.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/demo-2-example.png" alt="Example of demo project 2" width="80%">

</tabset-element>

## Troubleshooting

If you experience issues related to our streaming service, check out the following sections. They outline common problems and recommended resolution steps.

### Error handling

**NetworkError**

For details, refer to <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.networkerror.md" target="_blank">NetworkError class</a>. 

The ingestion service is unavailable or is unreachable from the client’s network. The error message includes a description of the error cause.  

In such cases, the application should render itself unavailable and report the error to Gcore support. The app should not retry the operation, as the retry logic is already implemented in the SDK. 

**ServerRequestError**  

For details, check out <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.serverrequesterror.md" target="_blank">ServerRequestError class</a>. 

The ingestion server returned an error, which can be identified by inspecting the `status` and `detail` fields of the error object. 

<expandable-element title="Typical cases for ServerRequestError">
 
<table>
<tbody> 
<thead>
  <tr>
    <th>HTTP status code</th>
    <th>Explanation</th>
    <th>Example</th>
  </tr>
  </thead>
<tr>
    <td>400</td>
    <td>The client’s request is wrong. It may be due to the incorrect request parameters sent by the WHIP client. If you see this error with an unintelligible description or with no description at all, contact the <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a>.<br><br>
    A special case to note is when multiple clients attempt to stream to the same endpoint simultaneously. Check the example for details.</td>
    <td><strong>err.message</strong>: Server request failed with status 400<br>
    <strong>err.status</strong>: 400<br>
    <strong>err.detail</strong>: {“error”: “someone is already publishing to path '1960197_XXX'”}</td>
  </tr>
<tr>
    <td>403</td>
    <td>The endpoint you are trying to connect to is unreachable.<br><br>
    Probable causes:
    <ul>
     <li>A stream doesn’t exist.</li>
     <li>A stream was not closed correctly, but you push to that broken stream (time out is ±30 seconds. In this case, try again after that time).</li>
     <li>Your token is invalid.</li>
     <li>Another stream setting prevents it from ingesting WebRTC.</li>
    </ul>
    </td>
    <td><strong>err.message</strong>: Server request failed with status 403<br>
    <strong>err.status</strong>: 403</td>    
  </tr>
<tr>
    <td>500, 502, 503, 504, 5xx (infrequently)</td>
    <td>Gcore infrastructure is experiencing pressure or outage. Contact the <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a>.<br>
    The app should render itself unavailable. It should not retry the request.</td>
    <td><strong>err.message</strong>: Server request failed with status 504<br>
    <strong>err.status</strong>: 504</td>
  </tr>
</body> 
</table>
 
</expandable-element>

**TimeoutError**

For details, check out <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.timeouterror.md" target="_blank">TimeoutError class</a>. 

Some operation has timed out.  

<expandable-element title="Typical cases for TimeoutError">

<table>
<tbody> 
<thead>
  <tr>
    <th>Error message</th>
    <th>Explanation</th>
  </tr>
  </thead>
<tr>
    <td>Timeout waiting for ICE candidates</td>
    <td><strong>Cause 1</strong>. Incorrectly configured <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/3e45d6e8beebcc7221625bd9e3b3b1749d9405ae/packages/rtckit/docs/api/rtckit.whipclientoptions.md" target="_blank">ICE servers</a>. The default configuration (when no ICE servers are specified) is to fetch a list of them from the WHIP endpoint.<br><br>
    <strong>Cause 2</strong>. ICE servers fetched from the WHIP endpoint are unreachable from your client’s location. This is very unlikely to happen.<br><br>
    In both cases, start by checking the ICE servers your WebRTC uses as described in the <a href="https://gcore.com/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding#network-troubleshooting" target="_blank">Network troubleshooting section</a>. If that doesn’t work, contact the <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a>.<br><br>
    The client app should render itself unavailable due to network conditions as an explanation. </td>
  </tr>
</body> 
</table>

</expandable-element>

Other types of errors are described in the our <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.md" target="_blank">SDK docs</a>. End-users should not encounter these errors, and there is no way to handle them in a real application apart from reporting the error occurrence.  

Some SDK methods might also throw browser’s native exceptions, such as <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.webrtcstreaming.opensourcestream.md" target="_blank">WebrtcStreaming.openSourceStream</a> and the methods of the <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/main/packages/rtckit/docs/api/rtckit.mediadeviceshelper.md" target="_blank">MediaDevicesHelper</a> throw <a href="https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia#exceptions" target="_blank">getUserMedia-originated exceptions</a>. The application should handle them accordingly. 

### Sudden disconnection of camera or microphone

Sometimes, users use external or plug-in cameras and microphones, and these devices can be disconnected at any time. For example: 

* A USB camera cable might be unplugged. 
* AirPods may be placed back in their case. 

If a camera or microphone is accidentally disconnected, you need to track such cases programmatically. Enable the `mediaDevicesAutoSwitch` option and subscribe to the event: 

* set mediaDevicesAutoSwitch: true 
* catch WebrtcStreamingEvents  

The new algorithm ensures uninterrupted broadcasting by prompting the browser to switch to another available camera or microphone if the current device becomes unavailable. 

When such a situation occurs, you will know which device was disconnected and which one was connected instead. This will allow you to visualize (if necessary) the new connected device in your interface. 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/microphone-options.png" alt="A list of available devices with USB audio selected" width="60%">

### Debugging with Chrome WebRTC internals tool

Chrome is really good at working with WebRTC because it has built-in tool to help developers see how things are working.  

Chrome v87+ has a special page called chrome://webrtc-internals where you can check your WebRTC calls: 

1\. Open a new Chrome tab and navigate to chrome://webrtc-internals while you're in a WebRTC call. On this page, you can view detailed information about the video and audio streams, connection setup, and more. 

2\. Use the provided information to find potential problems. For instance, when videos won't play, calls won't connect, or videos are slow. 

One of the parameters you can monitor in Stats graphs for candiate-pair: 

* **AvailableOutgoingBitrate** 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/available-outgoing-bitrate-graph.png" alt="AvailableOutgoingBitrate graph in Chrome WebRTC internals" width="80%">

You can also follow the following parameters from the **Stats graphs for outbound-rtp**: 

* bytesSent_in_bits/s
* targetBitrate 
* frameWidth 
* frameHeight 
* framesSent/s 

For example, consider how unevenly frames are sent from the browser in the following screenshot:

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/frame-graphs.png" alt="frameWidth and frameHeight graphs in Chrome WebRTC internals" width="80%">

### Network troubleshooting

#### Video stream is poorly transcoded or constantly stops

If a stream in the player constantly stops, is interrupted, or has poor quality, the issue is likely related to slow transmission of the original stream from a presenter via WebRTC.  

WebRTC is very demanding of the quality of internet connection from client to server. At the same time, standard implementations take into account many parameters on a local device, which can cause slower transmission of data or even stop it altogether until conditions are improved. 

To diagnose such situations: 

1\. Use the **VideoResolutionChangeDetector** plugin. It allows you to show a message about bad network conditions on a viewer’s device. 

2\. Use Chrome’s WebRTC debug tool that’s available via this link: chrome:\\webrtc-internals. 

Network congestion, occurring when resource demand surpasses capacity, leads to packet loss, increased latency, and jitter, hindering real-time communication, with congestion control algorithms optimizing performance by regulating data packet flow. You can read how WebRTC uses Transport Wide Congestion Control (TWCC) to control it in <a href="https://bloggeek.me/webrtcglossary/transport-cc/" target="_blank">thearticle about TWCC</a>. 

The available bitrate is calculated in the **availableOutgoingBitrate** parameter, which indicates the available outbound capacity of the network connection. The higher the value, the more bandwidth you can assume is available for outgoing data. The value is reported in bits per second and is computed over a 1-second interval. 

The most likely scenario for quality degradation occurs here, when the channel width becomes insufficient to send good resolution. 

However, sometimes the connection is even worse when packets are lost. In this case, the server starts sending NACK (Negative Acknowledgement) packets. You can read more about this issue in the <a href="https://bloggeek.me/webrtcglossary/nack/" target="_blank">NACK overview article</a>. 

More and more data start to be resent, which leads to increased latency or gaps in frames. In this case, the transcoder doesn’t receive frames on time, causing the video to interrupt or stop altogether. You can monitor and debug this issue in Chrome’s webrtc-internals tool: 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/sample-graphs-network-troubleshooting.png" alt="Example graphs in Chrome WebRTC internals tool" width="80%">

What to do in such situations: 

* Always show users a message about changed conditions. In 99% of cases, the issue is related to the user’s internet conditions.  
* Use TCP as the delivery protocol instead of UDP. 
* Use the TURN server for delivery instead of sending directly to the media server. 

#### Issues with ICE servers 

If you experience problems with timeout waiting for an ICE candidate, check your ICE server configuration.  

ICE servers used by the WHIP client can be configured explicitly using the iceServers <a href="https://github.com/G-Core/gcore-webrtc-sdk-js/blob/3e45d6e8beebcc7221625bd9e3b3b1749d9405ae/packages/rtckit/docs/api/rtckit.whipclientoptions.md" target="_blank">configuration option</a>. Otherwise, they are fetched from Gcore’s media server in the response to a session initiation request.  

In the case of the latter, check what the server returns in the `Link` headers. For example: 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/link-headers.png" alt="Example data in Link headers" width="80%">

<code-block>
Link: <stun:ed-c16-95-128-175.fe.gc.onl:3478>; rel="ice-server" 
Link: <turn:ed-c16-95-128-175.fe.gc.onl:443?transport=udp>; rel="ice-server"; username="1730558739:0nu0id47meqbsyvpz743"; credential="IswwB19KAEWQujy3X/c4D9GjZj8="; credential-type="password" 
Link: ... 
</code-block>

You can also inspect the servers using chrome://webrtc-internals or an alternative tool: 

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/webrtc-to-hls-transcoding/check-sever-config.png" alt="Example of servers check in Chome WebRTC internals" width="80%">

After you verify your server configuration, use the <a href="https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/" target="_blank">Trickle ICE</a> app to test the servers.  

Add a STUN or TURN server and check how it works. If everything functions correctly, the results will show: 

* A srvrflx candidate for STUN server 
* A relay candidate for a TURN server 

If you don't see these results, your STUN or TURN server may be misconfigured, or there is an outage. 

The <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a> will help you handle that. In the request, include the results of your ICE connectivity check to help us resolve the issue quickly.
