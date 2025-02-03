---
title: what-initial-parameters-of-your-live-streams-and-videos-we-can-accept
displayName: Input parameters
published: true
order: 10
toc:
   --1--Supported parameters: "supported-parameters"
   --1--Recommended parameters: "recommended-stream-parameters"
   --1--Multiple ingesting points: "multiple-ingesting-points"
   --1--RTMP, RTMPS, and SRT: "rtmp-rtmps-and-srt-for-live-streaming"
   --1--RTMPS troubleshooting: "rtmps-troubleshooting"
pageTitle: Guide to Gcore Streaming Parameters | Gcore
pageDescription: Overview of the supported and recommended parameters for optimizing live streams and videos using Gcore Video Streaming.
---
# Accepted initial parameters of your live streams and videos

## Supported parameters

Gcore Video Streaming supports:

- Receiving live streams from <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">your server (PULL) or a dedicated publishing point (PUSH)</a> using numerous protocols including RTMP(S) and SRT. All supported live protocols are listed in the table below. The stream is transcoded and sent with <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-after-transcoding-bitrate-frame-rate-and-codecs#output-parameters-after-transcoding" target="_blank">adaptive streaming</a> via CDN in  HLS/MPEG-DASH (CMAF low latency) formats. 
- Videos uploaded in almost any format, from standard MP4 to 4K HDR Video, are first transcoded to get videos of lower quality. Then, they're sent with adaptive streaming via CDN in HLS format. 

## Recommended stream parameters

We recommend the following parameters for streams:

<table border="=" cellpadding="=" data-tablestyle="MsoTableGrid" data-tablelook="1696">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><strong><span data-contrast="auto">Parameters</span></strong></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><strong><span data-contrast="auto">Value</span></strong></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" rowspan="6" data-celllook="0">
<p><span data-contrast="none">Video bitrate and resolution</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Quality</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p>&nbsp;</p>
<p><span data-contrast="none">Resolution</span></p>
<p>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Video bitrate range</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="auto">4k</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">3840x2160</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">20,000&ndash;51,000 Kbps (60 fps),&nbsp;</span></p>
<p><span data-contrast="none">13,000&ndash;34,000 Kbps (30 fps)</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="auto">1440</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">2560x1440</span>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">9,000&ndash;18,000 Kbps (60 fps),&nbsp;</span></p>
<p><span data-contrast="none">6,000&ndash;13,000 Kbps (30 fps)</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="auto">1080</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">1920x1080&nbsp;</span><span data-contrast="auto">&nbsp;</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">4,500&ndash;9,000 Kbps (60 fps),&nbsp;</span></p>
<p><span data-contrast="none">3,000&ndash;6,000 Kbps (30 fps)</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="auto">720</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">1280x720</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">2,250&ndash;6,000 Kbps (60 fps),</span></p>
<p><span data-contrast="none">1,500&ndash;4,000 Kbps (30 fps)</span>&nbsp;</p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="auto">480</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">854x480</span>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">500&ndash;2,000 Kbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Frame rate</span></p>
<p>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="auto">Up to&nbsp;</span><span data-contrast="none">60&nbsp;fps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Audio codec</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">AAC, MP3</span>&nbsp;</p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Video codec</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">H.264, H.265, AV1</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Max original file size <strong>(VOD)</strong></span></p>
<p>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p>up to 30 GB</p>
</td>
</tr>
<tr>
<td>
<p class="wysiwyg-text-align-center"><span data-contrast="none">Container<strong>&nbsp;(VOD)</strong></span></p>
</td>
<td colspan="3">
<p class="wysiwyg-text-align-center"><span data-contrast="none">3g2, 3gp,&nbsp;asf,&nbsp;avi,&nbsp;dif, dv,&nbsp;flv, f4v, m4v, mov, mp4, mpeg, mpg,&nbsp;mts, m2t, m2ts, qt,&nbsp;wmv,&nbsp;vob,&nbsp;mkv,&nbsp;ogv,&nbsp;webm,&nbsp;vob,&nbsp;ogg,&nbsp;mxf,&nbsp;quicktime, x-ms-wmv, mpeg-tts, vnd.dlna.mpeg-tts</span></p>
</td>
</tr>
<tr>
<td>Live protocols <strong>(Live)</strong></td>
<td colspan="3">RTMP, RTMPS, SRT, RTSP, HLS, WebRTC</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Keyframe frequency&nbsp;<strong>(Live)</strong></span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">1-2s</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Bitrate encoding</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">CBR</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Pixel aspect ratio</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">Square</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Chroma subsampling</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">[4:2:0](https://en.wikipedia.org/wiki/Chroma_subsampling)</span></p>
</td>
</tr><tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Audio sample rate</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">44.1/48 kHz</span>&nbsp;</p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Audio bitrate</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">128 Kbps&nbsp;stereo</span></p>
</td>
</tr>
</tbody>
</table>

If the recommended parameters do not suit your stream (codecs, custom FPS, ProRes, High 4:4:4, Enhanced RTMP, etc.), write to us in the chat, send an email to [support@gcore.com](mailto:support@gcore.com), or contact your manager to find the solution.

## Multiple ingesting points

To ensure smoother and more reliable streaming, we offer entry servers in key regions, including Luxembourg, Ashburn, Miami, and Singapore. By connecting your streaming equipment to the nearest upload server, you can minimize latency and improve performance before the stream is distributed globally through our CDN.

If your streams originate from multiple locations worldwide, this feature becomes especially valuable. You can specify preferred upload servers and the number of streams per region. With this information, our team will configure your account to match your streaming setup. Reach out to our support team or your account manager for setup assistance or additional details.


## RTMP, RTMPS, and SRT for live streaming

- RTMP (Real-Time Messaging Protocol) is a protocol for transmitting audio, video, and data over the Internet between a player and a server, supporting low-latency communication for real-time streaming.
- RTMPS is a variation of RTMP but incorporates SSL usage. 
- RTSP (Real Time Streaming Protocol) is a communication protocol used to control servers that stream media content. RTSP uses the Real-time Transport Protocol (RTP) with Real-time Control Protocol (RTCP) to deliver media streams.
- SRT (Secure Reliable Transport) is an open-source video transport protocol for delivering high-quality, secure, low-latency video across unreliable networks.

You can use Push or Pull methods where applicable.

## RTMP(S) troubleshooting

<table>
<thead>
<tr>
<td><b>Error</b></td>
<td><b>Cause</b></td>
<td><b>Solution</b></td>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left">SSL issues</td>
<td style="text-align: left">You used <pre>rtmps://</pre> but in the encoder <pre>rtmp://</pre> is specified</td>
<td style="text-align: left">Check the protocol in your encoder. Follow <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream#step-3-configure-your-stream-for-push-or-pull" target="_blank">step 3 of the guide</a>.</td>
</tr>
<tr>
<td style="text-align: left">You used a port (80) unsuitable for secure data transfer</td>
<td style="text-align: left">Manually add a correct port (443) to the server link, e.g.:
rtmp://vp-push-ed1.gvideo.co:<span style="color:#FF5913">443</span>/in/</td>
</tr>
<tr>
<td style="text-align: left">No transcoding or image degradation when using web cameras with custom video codecs</td>
<td style="text-align: left">The video codec H264+ extension has an over-increased keyframe</td>
<td style="text-align: left">Check the outgoing live stream parameters of the web camera:
<ul>
   <li>Streams must be encoded by H264. No hacks/codecs like H264+ maybe be used.</li>
   <li>“Smart” mode codecs must be turned off. </li>
</ul>
<img src="https://assets.gcore.pro/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept/dahua-video-codec-settings-2.png" alt="Web camera codec settings">
</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left">“Connection timed out”</td>
<td style="text-align: left">The server URL is incorrect</td>
<td style="text-align: left">Check the server URL in the encoder settings. Ensure that protocol is <pre>rtmps://</pre>.</td>
</tr>
<tr>
<td style="text-align: left">Your encoder doesn’t support RTMPS</td>
<td style="text-align: left">Check if there is RTMPS support, change encoder if required</td>
</tr>
</tbody>
</table>
