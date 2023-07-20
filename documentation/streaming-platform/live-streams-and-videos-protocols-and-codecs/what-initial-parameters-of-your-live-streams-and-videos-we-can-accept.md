---
title: what-initial-parameters-of-your-live-streams-and-videos-we-can-accept
displayName: Input parameters
published: true
order: 10
toc:
   --1--Supported parameters: "supported-parameters"
   --1--Recommended parameters: "recommended-stream-parameters"
pageTitle: Guide to Gcore Streaming Parameters | Gcore
pageDescription: Overview of the supported and recommended parameters for optimizing live streams and videos using the Gcore Streaming Platform.
---
# What initial parameters of your live streams and videos we can accept

## Supported parameters

The Streaming Platform supports:

- Receiving live streams from <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">your server (PULL) or a dedicated publishing point (PUSH)</a> using the RTMP, RTSP, or SRT. The stream is transcoded to get streams of lower quality and sent with <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-we-optimize-live-stream-and-video-performance-by-creating-different-bitrates" target="_blank">adaptive streaming</a> via CDN in  HLS/MPEG-DASH (CMAF Low Latency) formats. 
- Uploading videos in almost any format, from standard MP4 to 4k HDR Video, is transcoded to get videos of lower quality and sent with adaptive streaming via CDN in HLS format.

**Note!** To get a PUSH point for the SRT protocol, write to us in the chat or at [support@gcore.com](mailto:support@gcore.com). 

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
<p><span data-contrast="none">Video Bitrate &amp; Resolution</span></p>
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
<p><span data-contrast="none">Video Bitrate Range</span></p>
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
<p><span data-contrast="none">H.264, H.265</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Max original file size <strong>(only for video)</strong></span></p>
<p>&nbsp;</p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p>30 GB</p>
</td>
</tr>
<tr>
<td>
<p class="wysiwyg-text-align-center"><span data-contrast="none">Container<strong>&nbsp;(only for video)</strong></span></p>
</td>
<td colspan="3">
<p class="wysiwyg-text-align-center"><span data-contrast="none">3g2, 3gp,&nbsp;asf,&nbsp;avi,&nbsp;dif, dv,&nbsp;flv, f4v, m4v, mov, mp4, mpeg, mpg,&nbsp;mts, m2t, m2ts, qt,&nbsp;wmv,&nbsp;vob,&nbsp;mkv,&nbsp;ogv,&nbsp;webm,&nbsp;vob,&nbsp;ogg,&nbsp;mxf,&nbsp;quicktime, x-ms-wmv, mpeg-tts, vnd.dlna.mpeg-tts</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="0">
<p><span data-contrast="none">Keyframe frequency&nbsp;<strong>(only for live stream)</strong></span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">2s (max&nbsp;4s)</span></p>
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
<p><span data-contrast="none">Audio sample rate</span></p>
</td>
<td class="wysiwyg-text-align-center" colspan="3" data-celllook="0">
<p><span data-contrast="none">44.1 kHz</span>&nbsp;</p>
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

If the recommended parameters do not suit your stream, write to us in the chat or via [support@gcore.com](mailto:support@gcore.com), or contact your manager to find the solution.
