---
title: hls-and-mp4
displayName: HLS and MP4
published: true
order: 70
toc:
   --1--HLS format: "what-is-the-hls-format-for-streaming"
   --1--MP4 format: "what-is-the-mp4-format-used-for"
   --1--Enable MP4: "how-to-enable-mp4-support"
   --1--Get HLS and MP4 links: "get-hls-and-mp4-links"
   --2--Control panel: "control-panel"
   --2--API: "api"
   --1--Limit quality: "limitation-of-the-lowest-and-highest-quality-in-hls-adaptive-bitrate"
pageTitle: Adaptive Streaming & Offline Viewing Guide with HLS & MP4 Formats | Gcore
pageDescription: Explore the uses and benefits of HLS and MP4 formats for video streaming, from adaptive bitrate streaming to offline viewing. 
---

# HLS and MP4

## What is the HLS format for streaming?

The HLS format is the most common format for delivering videos online. This format allows you to:

- **Use adaptive bitrate.** This provides viewers with video content at a quality level determined by the speed of their internet connection.
- **Slice into chunks.** Video content is chunked into 2–3 second segments and cached for fast delivery worldwide using CDNs.
- **Reduce the cost.** You don’t pay for the complete duration of the video, only the part that the user watched.

Video content delivered in HLS format contains a manifest (.m3u8) which tells browsers the order in which they should play the chunks into which the video is divided.

Here is the format of the link to get the master manifest:

<code-block>
https://domain.com/videos/<span style="color:#FF5913">{client_id}</span>_<span style="color:#FF5913">{video_id}</span>/master[<span style="color:#FF5913">-min-N</span>][<span style="color:#FF5913">-max-N</span>][<span style="color:#FF5913">-img</span>].m3u8
</code-block>

Where:

- <span style="color:#FF5913">{client_id}</span>: your account ID
- <span style="color:#FF5913">{video_id}</span>: identifier of the video
- <span style="color:#FF5913">-min-N</span>: special suffix that specifies the lower available video quality limit
- <span style="color:#FF5913">-max-N</span>: special suffix that specifies the  upper available video quality limit
- <span style="color:#FF5913">-img</span>: special suffix, information about preview files is added to the manifest when specified. Read more in the article <a href="https://gcore.com/docs/streaming-platform/video-hosting/timeline-hover-previews-use-in-players-and-roku-devices#roku-trick-play" target="_blank">Timeline hover previews: use with players and Roku devices</a>

Example of the manifest link: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.m3u8 

## What is the MP4 format used for?

Video can be streamed and downloaded using the .mp4 file format when you want to handle the whole file at once instead of in chunks. So MP4 format allows users to:

- Watch videos offline on mobile devices
- Download video files for local modification
- Specify VAST ads as a progressive download
- Play videos even on very outdated devices
- Share videos on social networks and other streaming services

When using the MP4 format, users can work with each available video resolution separately. For example, select the video quality version (720p) and download only that version: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/720.mp4 

Example usage:

```
<video width="100%" height="auto" autoplay="autoplay" loop="true" playsinline="" oncanplay="this.play()">
     <source type="video/mp4" src="https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/720.mp4"/>
</video>
```

Gcore supports regular download requests for entire MP4 file downloads. We also support range requests specifying the HTTP "Range" header.

```
curl -v 'https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/720.mp4' -H 'range: bytes=4259840-'   

> GET /videos/2675_FnlHXwA16ZMxmUr/720.mp4 HTTP/2 
> Host: demo-public.gvideo.io 
> range: bytes=4259840-   

< HTTP/2 206 < content-type: video/mp4 
< content-length: 43497712 
< content-range: bytes 4259840-47757551/47757552
```

**Note**: <a href="https://gcore.com/docs/streaming-platform/extra-features/protect-your-content-with-temporary-links-and-secure-tokens" target="_blank">Video protection via the Security Tokens feature</a> is available for MP4 files.

## How to enable MP4 support

Gcore’s Streaming Platform provides HLS by default. If you want to enable MP4 support, contact our [support team](mailto:support@gcore.com).

## Get HLS and MP4 links

You can get links to videos in two ways: in the control panel or via the API.

### Control panel

Select the video in the <a href="https://streaming.gcore.com/video/list" target="_blank">Video Hosting</a> section, open the "Export" tab, and copy the following links.

- Web player: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr 
- HLS: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.m3u8 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/hls-and-mp4/image3526.png" alt="Control panel">

### API

To get information about the video, call a method:

```
https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id
```
Example request:

```
GET https://api.gcore.com/streaming/videos/2474723 
```

Example response:

```
{
    "id": 2474723,
    "name": "Coffee Run - Blender Open Movie",
    ...
    "hls_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.m3u8",
    "iframe_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr",
    "iframe_embed_code": "<iframe width="560" height="315" src="https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr" frameborder="0" allowfullscreen></iframe>",
    "converted_videos": [
        {
            "name": "vod720n",
            "width": 1720,
            "height": 720,
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/720.mp4"
        },
        {
            "name": "vod480n",
            "width": 1146,
            "height": 480,
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/480.mp4"
        },
       ...
    ]
} 
```

Where:

- ```iframe_url``` contains a web player link
- ```iframe_embed_code``` contains web player embed code
- ```hls_url``` contains the HLS link
- ```mp4_url``` contains the MP4 link

## Limitation of the lowest and highest quality in HLS adaptive bitrate

The manifest file (.m3u8) contains all possible video qualities by default. If you want to limit the quality for old devices, non-paying users, or a quick view, you can specify a suffix indicating the minimum and/or maximum allowed resolution:

- ```-min-N```: minimum resolution not less than specified
- ```-max-N```: maximum resolution not exceeding than specified

```N``` is a resolution (height or width) from 240 to 9999. If the video is horizontally oriented, the resolution is its height. If it's vertically oriented, it should be width. 

Here’s an example of how to get two qualities only—360 and 480—instead of the full set: 

```
curl https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master-min-360-max-719-img.m3u8 
```
The response is: 

```
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=928000,RESOLUTION=1148x480,FRAME-RATE=24.000,CODECS="avc1.4d401f,mp4a.40.2",VIDEO-RANGE=SDR
index-svod480n-v1-a1.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=514000,RESOLUTION=860x360,FRAME-RATE=24.000,CODECS="avc1.42c01e,mp4a.40.2",VIDEO-RANGE=SDR
index-svod360n-v1-a1.m3u8

#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=71839,RESOLUTION=1148x480,CODECS="avc1.4d401f",URI="iframes-svod480n-v1-a1.m3u8",VIDEO-RANGE=SDR
#EXT-X-I-FRAME-STREAM-INF:BANDWIDTH=35296,RESOLUTION=860x360,CODECS="avc1.42c01e",URI="iframes-svod360n-v1-a1.m3u8",VIDEO-RANGE=SDR
```
