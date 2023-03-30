---
title: what-initial-parameters-of-your-live-streams-and-videos-we-can-accept
displayName: Input parameters
published: true
order: 10
toc:
   --1--Supported parameters: "supported-parameters"
   --1--Recommended parameters: "recommended-stream-parameters"
---
  

Supported parameters
--------------------

The streaming platform supports:

*   Receiving live streams from [your server (PULL) or a dedicated publishing point (PUSH)](https://gcore.com/support/articles/5307972492945/) using the RTMP, RTSP, or SRT. The stream is transcoded to get streams of lower quality and sent with [adaptive streaming](https://gcore.com/support/articles/360000604285/) via CDN in  HLS/MPEG-DASH (CMAF Low Latency) formats. 
*   Uploading videos in almost any format, from standard MP4 to 4k HDR Video, is transcoded to get videos of lower quality and sent with adaptive streaming via CDN in HLS format.

**Note!** To get a PUSH point for the SRT protocol, write to us in the chat or at [support@gcore.com](mailto:support@gcorelabs.com). 

Recommended stream parameters
-----------------------------

We recommend the following parameters for streams:

| \nParameters \n                                | \nValue \n                                                                                                                                                                         |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \nVideo Bitrate &amp;Resolution \n             | \nQuality \n                                                                                                                                                                       | \n \nResolution \n \n                                            | \nVideo Bitrate Range \n |
| \n4k \n                                        | \n3840x2160 \n                                                                                                                                                                     | \n20,000–51,000 Kbps (60 fps),  \n13,000–34,000 Kbps (30 fps) \n |
| \n1440 \n                                      | \n2560x1440  \n                                                                                                                                                                    | \n9,000–18,000 Kbps (60 fps),  \n6,000–13,000 Kbps (30 fps) \n   |
| \n1080 \n                                      | \n1920x1080   \n                                                                                                                                                                   | \n4,500–9,000 Kbps (60 fps),  \n3,000–6,000 Kbps (30 fps) \n     |
| \n720 \n                                       | \n1280x720 \n                                                                                                                                                                      | \n2,250–6,000 Kbps (60 fps),  \n1,500–4,000 Kbps (30 fps)  \n    |
| \n480 \n                                       | \n854x480  \n                                                                                                                                                                      | \n500–2,000 Kbps \n                                              |
| \nFrame rate \n \n                             | \nUp to 60 fps \n                                                                                                                                                                  |
| \nAudio codec \n                               | \nAAC, MP3  \n                                                                                                                                                                     |
| \nVideo codec \n                               | \nH.264, H.265 \n                                                                                                                                                                  |
| \nContainer (only for video)\n                 | \n3g2, 3gp, asf, avi, dif, dv, flv, f4v, m4v, mov, mp4, mpeg, mpg, mts, m2t, m2ts, qt, wmv, vob, mkv, ogv, webm, vob, ogg, mxf, quicktime, x-ms-wmv, mpeg-tts, vnd.dlna.mpeg-tts\n |
| \nKeyframe frequency (only for live stream) \n | \n2s (max 4s)  \n                                                                                                                                                                  |
| \nBitrate encoding \n                          | \nCBR \n                                                                                                                                                                           |
| \nPixel aspect ratio \n                        | \nSquare \n                                                                                                                                                                        |
| \nAudio sample rate \n                         | \n44.1 kHz  \n                                                                                                                                                                     |
| \nAudio bitrate \n                             | \n28-Kbps stereo \n                                                                                                                                                                |


If the recommended parameters do not suit your stream, write to us in the chat or via [support@gcore.com](mailto:support@gcore.com), or contact your manager to find the solution.
