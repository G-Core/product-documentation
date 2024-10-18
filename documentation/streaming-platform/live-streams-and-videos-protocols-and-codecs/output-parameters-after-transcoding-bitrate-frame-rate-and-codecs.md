---
title: output-parameters-after-transcoding-bitrate-frame-rate-and-codecs
displayName: Output parameters
published: true
order: 20
toc:
   --1--Transcoding with ABR: "what-is-transcoding-with-abr"
   --1--Audio and video codecs: "audio-and-video-codecs"
   --1--Output parameters: "output-parameters-after-transcoding"
   --1--4K and custom settings: "how-to-apply-2k4k-and-custom-advanced-settings"
   --1--HTTP response codes: "http-response-codes-when-requesting-live-and-vod-videos"
pageTitle: Transcoding and Output Specs for Gcore Streams | Gcore
pageDescription: Learn about Gcore's transcoding process, including details on file bitrates, frame rates, and codecs for different video quality levels.
---
# Output parameters after transcoding: bitrate, frame rate, and codecs

## What is transcoding with ABR?

In a nutshell, transcoding is converting the original video from one format to another format with a set of extra qualities (ABR). Transcoding aims to make videos viewable across different platforms and devices and to expand the number of viewers, e.g., adding those who couldn't watch the video in its original format. Learn more about transcoding with our <a href="https://gcore.com/learning/what-is-transcoding/" target="_blank">in-depth article</a>.

Transcoding with adaptive bitrate streaming (ABR) works like this: 

1. Decoding of the original video (<a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">list of accepted parameters</a> for input video)
2. Processing, including scaling (resizing,) frame rate conversion, aspect ratio conversion, and other types of video processing
3. Encoding into the desired output format

Discover how we <a href="https://gcore.com/blog/how-we-lowered-the-bitrate-for-live-and-vod-streaming-by-32-5-without-sacrificing-quality/" target="_blank">lowered the bitrate</a> for live and VOD streaming by 32.5% without sacrificing quality. 

## Audio and video codecs

A transcoded video stream has the following codecs by default: 

- **Audio**: AAC, 44.1KHz, stereo 
- **Video**: H264, 30FPS, ABR 

## Output parameters after transcoding

<table>
<thead>
<tr>
<td><b>Video Quality </b></td>
<td><b> Resolution</b></td>
<td><b>FPS</b></td>
<td><b>Video bitrate, Mbps</b></td>
<td><b>Audio bitrate, Mbps</b></td>
</tr>
</thead>
<tbody>
<tr>
<td>UHD 8K<span style="color:#FF5913">*</span></td>
<td>7680 × 4320</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>UHD 4K<span style="color:#FF5913">*</span></td>
<td>3840 × 2160</td>
<td>30</td>
<td>14,000</td>
<td>0,196</td>
</tr>
<tr>
<td>QHD 2K<span style="color:#FF5913">*</span></td>
<td>2560 × 1440</td>
<td>30</td>
<td>7,200</td>
<td>0,196</td>
</tr>
<tr>
<td>Full HD 1080p</td>
<td>1920 × 1080</td>
<td>30</td>
<td>4,050</td>
<td>0,128</td>
</tr>
<tr>
<td>HD 720p</td>
<td>1280 × 720</td>
<td>30</td>
<td>1,800</td>
<td>0,128</td>
</tr>
<tr>
<td>SD 468p</td>
<td>832 × 468</td>
<td>30</td>
<td>0,800</td>
<td>0,096</td>
</tr>
<tr>
<td>360p</td>
<td>640 × 360</td>
<td>30</td>
<td>0,450</td>
<td>0,064</td>
</tr>
<tr>
<td>240p<span style="color:#FF5913">*</span></td>
<td>427 × 240</td>
<td>30</td>
<td>0,200</td>
<td>0,064</td>
</tr>
<tr>
<td>144p<span style="color:#FF5913">*</span></td>
<td>254 × 144</td>
<td>30</td>
<td>0,072</td>
<td>0,064</td>
</tr>
<tr>
<td>Audio only<span style="color:#FF5913">*</span></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0,128</td>
</tr>
</tbody>
</table>

<span style="color:#FF5913">*</span>To enable these qualities, contact the [support team](mailto:support@gcore.com).

The values in the table are given for videos with a horizontal aspect ratio of 16:9. 
The values must be reversed for vertical videos. For example, if a horizontal resolution is (1280 × 720), the relevant vertical resolution is (720 × 1280). 

We use variable bitrate (VBR) for encoding video. The table above shows average values. The Gcore Customer Portal shows a sum of audio and video bitrates.

**Note**: We don’t upscale videos. Your output will range from the lowest quality to that of your original bitrate. So, if you upload a 4K video, your output will range from the lowest quality up to 4K. Similarly, if you upload a 720p video, your output will vary from the lowest quality up to 720p only.

## HTTP response codes when requesting Live and VOD videos

The following table includes the possible HTTP response codes returned when requesting videos and live streams for manifests (.m3u8, .mpd) and chunks (.ts, mp4, etc.).

<table>
  <th>Code</th><th>Function</th><th>Description</th>
  <tr><td>200</td><td>OK</td><td>All OK</td></tr>
  <tr><td>403</td><td>Forbidden</td><td>Access is denied. If you use any distribution restriction such as geo-restriction or token, you must satisfy this condition for access.</td></tr>
  <tr><td>404</td><td>Not Found</td><td>There's no requested video, or the live stream is temporarily not delivering chunks. Check the request link or activate your video.<br/>For Live streams in CMAF format, you can check the extra header "X-Err-Code":<ul><li>1000 – Master-stream is missed. The stream is not pushed or not transcoded, so start a stream or restart transcoding.</li><li>2000 – Invalid StreamID. The identifier is not parsed from the requested URL; check the URL.</li><li>3000 – Stream is not ready for delivery. Inspect the logs or contact support. Oftentimes, this happens when the master-stream has wrong parameters, such as video and audio codecs, FPS, or bitrate. Verify the parameters to ensure everything works as expected. </li></ul></td></tr>
  <tr><td>422</td><td>Not Found</td><td>This is advanced functionality (i.e. custom encoding presets). To enable it, contact your manager or the support team.</td></tr>
  <tr><td>500</td><td>Internal Server Error</td><td>An unexpected issue happened on the server. This may be a local error in a specific video. In this case, check the video processing status in your personal account. If the error is global, the information will be on the status page.</td></tr>
  <tr><td>502</td><td>Bad Gateway</td><td>An unexpected issue happened on the server. This may happen when VOD or Live can't be delivered over CDN because an incorrect response was received from an origin (storage or live transcoder). In this case, check the video processing status or live stream transcoding in your personal account. If the error is global, the information will appear on the status page.</td></tr>
  <tr><td>503</td><td>Service Unavailable</td><td>An unexpected issue happened on the server. This may be a local error in a specific video. In this case, check the video processing status in your personal account. If the error is global, the information will be on the status page.</td></tr>
  <tr><td>504</td><td>Gateway Time-out</td><td>Timeout for receiving data from the source. Try checking the status of video sending/ingesting and transcoding.</td></tr>
</table>

<alert-element type="info" title="Info">
 
The system health status page is available at [https://status.gcore.com/](https://status.gcore.com/)
 
</alert-element>

## How to apply 2K/4K+ and custom advanced settings

Some settings require manual control. If you need them, contact the Gcore [support team](mailto:support@gcore.com) or your manager. 

The basic tariff plan doesn't include 2K/4K+ in the transcoding quality preset. For information about high-quality video processing costs, check our <a href="https://gcore.com/pricing/streaming-platform" target="_blank">pricing page</a>. To work with high-quality video, we'll provide you with new quality presets and a new tariff plan.

Additionally, you can ask to activate the following settings:
- Use codecs H265 HEVC, VP9, AV1, etc.,
- Add 8K quality,
- Add super-low quality 144p,
- Change preset of output ABR qualities for all or some renditions, remove low-quality renditions,
- Use 60+ FPS or use original FPS values,
- Increase bitrate for audio; use 48KHz,
- Use Dolby Digital, Dolby Atmos,
- Transmux VOD MP4 files into HLS on the fly.
- Transmux and “pass-through” instead of transcoding for LIVE streams.
