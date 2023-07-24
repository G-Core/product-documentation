---
title: how-the-streaming-platform-interact-with-the-cdn
displayName: Interaction with CDN
published: true
order: 40
toc:
   --1--How is video content distributed: "how-does-our-streaming-platform-distribute-video-content"
   --1--From which subdomain?: "from-which-subdomain-is-your-content-distributed"
   --1--Change the subdomain: "change-the-default-subdomain"
pageTitle: Interaction with CDN | Gcore
pageDescription: An explanation of how the Streaming Platform interacts with CDN.
---
# How the Streaming Platform interact with the CDN
 
## How does our Streaming Platform distribute video content?

Our <a href="https://gcore.com/streaming-platform" target="_blank">Streaming Platform</a> distributes video content through the Gcore CDN network. Edge servers pull videos from storage or live streams from the media server and deliver them quickly to end users.

## From which subdomain is your content distributed? 

Content is distributed to viewers from a CDN resource subdomain name. When you create an account and activate the Streaming Platform, we create a subdomain in the format:

```
clientID.gvideo.io
```

The *clientID* is a unique identifier for your account, which can be found in the <a href="https://accounts.gcore.com/profile/company" target="_blank">General</a> section under the "Client ID" field. For example, if your clientID is *12345*, the subdomain for the Streaming Platform will be *12345.gvideo.io*. 

This subdomain is included in the URLs of all your videos or live streams uploaded to the Streaming Platform, such as ```https://12345.gvideo.io/cmaf/12345_00000/master.m3u8``` (a link to a live stream) or ```https://12345.gvideo.io/videos/12345_ABcdefg123HiJ``` (a link to a VoD).

## Change the default subdomain

If you want to change the default subdomain to set a custom domain name, configure geo-restrictions, or implement other settings, please contact our [support team](mailto:support@gcore.com) or your personal manager.