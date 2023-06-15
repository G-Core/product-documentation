---
title: push-live-streams-via-adobe-flash-media-live-encoder
displayName: Adobe Flash Media Live Encoder
published: true
order: 20
toc:
---
# Push live streams via Adobe Flash Media Live Encoder

Download «Adobe Flash Media Live Encoder», install it, and launch it.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/push-live-streams-software/push-live-streams-via-adobe-flash-media-live-encoder/mceclip0.png" alt="">

You can find RTMP URL and a stream key in your control panel according to the <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream" target="_blank">Create a live stream</a> guide. Choose the stream, click edit, and look at the Push URL.

Then in Adobe Flash Media Live Encoder, fill the «FMS URL» field with this part of the PUSH URL: 

```
rtmp://vp-push-ed1.gvideo.co/in/
```

Fill the «Stream» field with key (all the remaining symbols): *9cb3fdee0836564bd0046dasdb0e4de3sda32af712411313*

Fill in the Device and choose the source (device or soft).

You can also configure the other options.

**Recommended parameters**:

For video: 

```
Format: H.264
Frame Rate: 30 fps  
Input Size: 1280x720  
Bit Rate: 2000 Kbps
```

For audio:  

```
Device – audio source
Channels: Stereo
Bit Rate: 128 kbps
```

You can change them if you need to.

Click «Start» to run the stream.