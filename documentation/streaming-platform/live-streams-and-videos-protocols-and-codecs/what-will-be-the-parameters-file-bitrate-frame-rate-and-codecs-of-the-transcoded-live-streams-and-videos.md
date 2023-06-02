---
title: what-will-be-the-parameters-file-bitrate-frame-rate-and-codecs-of-the-transcoded-live-streams-and-videos
displayName: Output parameters
published: true
order: 20
toc:
   --1--File bitrates for different qualities: "transcode-file-bitrates-for-different-qualities"
   --1--File frame rate: "transcode-frame-rate"
   --1--Codecs: "transcode-audio--video-codecs"
---

# What will be the parameters (file bitrate, frame rate, and codecs) of the transcoded live streams and videos  
  
To configure exceptional values (Live stream in 4K or higher quality, individual frame rate), write to us in the chat or at [support@gcore.com](mailto:support@gcore.com) or contact your manager.   

## Transcode file bitrates for different qualities

Transcoding is the video file parameters conversion. 

It includes not only changing the protocol but also splitting a stream into lower qualities with a suitable bitrate.

<table border="=" cellpadding="=" data-tablestyle="MsoTableGrid" data-tablelook="1696">
<tbody>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><strong>&nbsp;Video Quality&nbsp;</strong></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><strong>&nbsp;Resolution&nbsp;</strong></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><strong>&nbsp;Bitrate after transcoding&nbsp;</strong></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">Ultra HD, 4K</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">3840 &times; 2160</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">14 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">QHD</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">2560 &times; 1440</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">7.2 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">Full HD, 2K</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">1920 &times; 1080</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">4 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">720p</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">1280 &times; 720</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">1.8 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">480p</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">854 &times; 480</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">0.8 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">360p</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">640 &times; 360</span></p>
</td>
<td class="wysiwyg-text-align-center" data-celllook="4369">
<p><span data-contrast="none">0.45 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">240p</span></p>
</td>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">&nbsp;427 &times; 240</span></p>
</td>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">0.2 Mbps</span></p>
</td>
</tr>
<tr>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">144p</span></p>
</td>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">&nbsp;254 &times; 144</span></p>
</td>
<td class="wysiwyg-text-align-center">
<p><span data-contrast="none">0,072 Mbps</span></p>
</td>
</tr>
</tbody>
</table>

**Note**: We also change the incoming stream bitrate based on a standard set of bitrates optimal for each resolution. 

For example, if you send a stream in 1080p with a bitrate less or more than 4 Mbps, we will convert it to a standard 4 Mbit.

We also support: 

- transcoding with the original bitrate,  
- transcoding to any bitrate on request, 
- splinting into non-standard resolutions (for example, 1440p QHD or 4320p 8k UHD).  

## Transcode frame rate

The frame rate is the number of frames that change each other per second. The optimal frame rate for distribution on the Internet, which works on all devices, is 30 fps.

We default transcode the original steam frame rate to the standard 30 fps.

We can save the original stream frame rate or transcode it to the required value if necessary.

## Transcode audio / video codecs

Codecs are compression technologies with two components, an encoder to compress the files and a decoder to decompress them.

A transcoded video stream has the following codecs: 

Audio: AAC

Video: H264
