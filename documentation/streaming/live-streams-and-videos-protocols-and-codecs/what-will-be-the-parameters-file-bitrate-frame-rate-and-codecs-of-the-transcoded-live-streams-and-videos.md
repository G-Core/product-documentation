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
  
  
  

To configure exceptional values (Live stream in 4K or higher quality, individual frame rate), write to us in the chat or at [support@gcore.com](mailto:support@gcore.com) or contact your manager.   

Transcode file bitrates for different qualities
-----------------------------------------------

Transcoding is the video file parameters conversion. 

It includes not only changing the protocol but also splitting a stream into lower qualities with a suitable bitrate.

| \n Video Quality \n | \n Resolution \n | \n Bitrate after transcoding \n |
|---------------------|------------------|---------------------------------|
| \nUltra HD, 4K \n   | \n3840 × 2160 \n | \n14 Mbps \n                    |
| \nQHD \n            | \n2560 × 1440 \n | \n7.2 Mbps \n                   |
| \nFull HD, 2K \n    | \n1920 × 1080 \n | \n4 Mbps \n                     |
| \n720p \n           | \n1280 × 720  \n | \n1.8 Mbps \n                   |
| \n480p \n           | \n854 × 480 \n   | \n0.8 Mbps \n                   |
| \n360p \n           | \n640 × 360 \n   | \n0.45 Mbps \n                  |
| \n240p\n            | \n 427 × 240\n   | \n0.2 Mbps\n                    |
| \n144p \n           | \n 254 × 144\n   | \n0,072 Mbps \n                 |


   
**Please note!** We also change the incoming stream bitrate based on a standard set of bitrates optimal for each resolution. 

For example, if you send a stream in 1080p with a bitrate less or more than 4 Mbps, we will convert it to a standard 4 Mbit. 

We also support: 

*   transcoding with the original bitrate,  
*   transcoding to any bitrate on request, 
*   splinting into non-standard resolutions (for example, 1440p QHD or 4320p 8k UHD).  

Transcode frame rate
--------------------

The frame rate is the number of frames that change each other per second. The optimal frame rate for distribution on the Internet, which works on all devices, is 30 fps.

We default transcode the original steam frame rate to the standard 30 fps.

We can save the original stream frame rate or transcode it to the required value if necessary.

Transcode audio / video codecs
------------------------------

Codecs are compression technologies with two components, an encoder to compress the files and a decoder to decompress them.

A transcoded video stream has the following codecs: 

Audio**:** AAC

Video: H264
