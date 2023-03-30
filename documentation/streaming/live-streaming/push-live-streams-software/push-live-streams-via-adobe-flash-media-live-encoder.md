---
title: push-live-streams-via-adobe-flash-media-live-encoder
displayName: Adobe Flash Media Live Encoder
published: true
order: 20
toc:
---
Download «Adobe Flash Media Live Encoder», install it, and launch it.

<img src="https://support.gcore.com/hc/article_attachments/360000493958/mceclip0.png">

You can find RTMP URL and a stream key in your control panel according to the [Create a live stream](https://www.gcore.com/support/articles/5307972492945/) guide. Choose the stream, click edit, and look at the Push URL.

Then in Adobe Flash Media Live Encoder, fill the «FMS URL» field with this part of the PUSH URL: 

rtmp://vp-push-ed1.gvideo.co/in/

Fill the «Stream» field with key (all the remaining symbols): 9cb3fdee0836564bd0046dasdb0e4de3sda32af712411313

Fill in the Device and choose the source (device or soft).

You can also configure the other options.

Recommended parameters

Format: H.264

Frame Rate: 30 fps  
Input Size: 1280x720  
Bit Rate: 2000 Kbps

For Audio:  
Device – audio source

Channels: Stereo

Bit Rate: 128 kbps

You can change them if you need to.

Click «Start» to run the stream.