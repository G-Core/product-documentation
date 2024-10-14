---
title: hls-and-mp4
displayName: HLS, MPEG-DASH, and MP4
published: true
order: 70
toc:
   --1--HLS TS and CMAF formats: "hls-ts-and-cmaf-formats"
   --1--DASH format: "dash-format"
   --1--MP4 format: "mp4-format"
   --1--Get HLS, DASH, and MP4 links: "get-hls-dash-and-mp4-links"
   --2--Customer Portal: "customer-portal"
   --2--API: "api"
   --1--Limit quality: "limit-the-lowest-and-highest-quality-in-hls-adaptive-bitrate"
pageTitle: Guide to HLS, DASH, and MP4 Video Streaming Formats | Gcore
pageDescription: Explore the uses, benefits, and how to optimize HLS, MPEG-DASH, and MP4 formats for video streaming, from adaptive bitrate streaming to offline viewing.
---

# HLS, MPEG-DASH, and MP4

Gcore Video Streaming allows you to deliver video-on-demand (VOD) content optimized for different devices and platforms. We offer multiple video formats as part of the service, so you're not limited by the technical constraints of a single playback option and can choose a format that best fits your use case and functional requirements. 

We offer the following formats for playback: 

* **HLS TS**: A default VOD delivery to all devices. Has codecs limitations. For instance, it supports H264 video codec up to High Profile <a href="https://en.wikipedia.org/wiki/Advanced_Video_Coding#Levels" target="_blank">level 4.1</a> but using newer codecs like H265 and AV1 isn't possible.  

* **HLS CMAF**: A common format supported by all modern devices (e.g., iOS 10 and later). Supports a fragmented MP4 (fMP4) format of video chunks that allows using a wide range of modern technologies such as new H265 and AV1 codecs.  

* **MPEG-DASH**: A popular video delivery format with the advantages of a universal single manifest. It provides buffer-based (BOLA) and hybrid (dynamic) bitrate adaptation algorithms and natively supports all modern codecs. Most preferred on Android and Windows platforms.  

* **MP4**: A format for downloading videos as a single file in an MP4 container. Used when a user doesn't just want to watch a video but download it locally, for example, for editing.

You can also find a description of supported video formats and relevant use cases in our <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id" target="_blank">API documentation</a>.  

## HLS TS and CMAF formats

The HTTP Live Streaming (HLS) format is the most common format for delivering videos online. This format allows you to:

* **Use adaptive bitrate**. This provides viewers with video content at a quality level determined by the speed of their internet connection.
* **Slice into chunks**. Video content is chunked into segments from 2 to 6 seconds and cached for fast delivery worldwide using CDNs.
* **Protect content from unauthorized use**. HLS supports AES-128 encryption and is compatible with major DRM (Digital Rights Management) systems. This ensures secure delivery and controlled access to video content. 

The `hls_url` contains a URL to the manifest (.m3u8) that tells players the order in which they should play the chunks into which the video is divided. 

The `hls_cmaf_url` contains a URL to the master playlist HLS (master-cmaf.m3u8) with CMAF-based chunks. The chunks are in the fMP4 container, which is codec-agnostic and allows the use of anything like H264, H265, or AV1.  

Considering the existing limitations of the old HLS, it's important to understand how the manifest and chunks will be formed. Chunk type is selected automatically according to the used type of video codec: 

* master.m3u8: 

    * **MPEG TS** if the video was encoded in H264 only. 
    * **CMAF** if the video was encoded in additional HEVC and AV1. CMAF is used because Apple devices don’t support HEVC/AV1 over MPEG TS and aren’t standardized in TS-container. 

* master-cmaf.m3u8 will always contain CMAF chunks for any video codec. 

Here is the full possible format of the link to get the master manifest:

<code-block>
https://domain.com/videos/<span style="color:#FF5913">{client_id}</span>_<span style="color:#FF5913">{video_slug}</span>/master<span style="color:#FF5913">[-cmaf]</span><span style="color:#FF5913">[-min-N]</span><span style="color:#FF5913">[-max-N]</span><span style="color:#FF5913">[-img]</span><span style="color:#FF5913">[-(h264|hevc|av1)]</span>.m3u8
</code-block>

Where:

- <span style="color:#FF5913">{client_id}</span>: Your account ID.
- <span style="color:#FF5913">{video_slug}</span>: Slug identifier of the video.
- <span style="color:#FF5913">[-cmaf]</span>: The HLS CMAF version of the manifest. For details, check the hls_cmaf_url field description in our <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos" target="_blank">API docs</a>. 
- <span style="color:#FF5913">[-min-N]</span>: Special suffix that specifies the lowest video quality limit available in an Adaptive Bitrate (ABR) streaming. Learn more about the setting in the <a href="https://gcore.com/docs/streaming-platform/video-hosting/hls-and-mp4#limit-the-lowest-and-highest-quality-in-hls-adaptive-bitrate" target="_blank">Limit quality</a> section.
- <span style="color:#FF5913">[-max-N]</span>: Special suffix that specifies the highest video quality limit available in the ABR streaming. Learn more about the setting in the <a href="https://gcore.com/docs/streaming-platform/video-hosting/hls-and-mp4#limit-the-lowest-and-highest-quality-in-hls-adaptive-bitrate" target="_blank">Limit quality</a> section.
- <span style="color:#FF5913">[-img]</span>: The trick play feature for Roku devices allows thumbnail images to be embedded directly into the manifest. Read more in the article <a href="https://gcore.com/docs/streaming-platform/video-hosting/timeline-hover-previews-use-in-players-and-roku-devices#roku-trick-play" target="_blank">Timeline hover previews: use with players and Roku devices</a>.
- <span style="color:#FF5913">[-(h264|hevc|av1)]</span>: Video codec soft limitation. Applicable if the video was simultaneously transcoded into multiple codecs (264, H265, and AV1) and you want to return just one video codec in a manifest.  

For example, check out the following manifest links for a master playlist:  

* The link to the master playlist: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.m3u8 

* The link to the master playlist with CMAF-based chunks: https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master-cmaf.m3u8 

## DASH format

Dynamic Adaptive Streaming over HTTP (DASH) is the industry standard video format that’s widely adopted by streaming services and supported on most non-Apple devices and browsers. 

This format allows you to: 

* **Use adaptive bitrate**. You can stream videos of different quality and switch in the middle of a video from one quality level to another. 

* **Support for multiple DRM systems**. DASH is compatible with various Digital Rights Management (DRM) systems, allowing for the secure distribution of media across different platforms. 

* **Deliver content encoded in different formats**. DASH is designed to work with a wide range of audio and video codecs, which ensures seamless playback across different devices and platforms.  

Video content delivered in DASH format contains a manifest file (.mpd). This file informs players about the video structure (chunks and segments), available quality levels and bitrates, and the order and conditions under which each video chunk should be played. 

For DASH, chunks will also differ depending on the type of video codec that was used to encode the quality: 

* CMAF chunks for H264 and H265 video codecs 
* WebM chunks for AV1 video 

Example of the WebM output: 

```
... 
    <AdaptationSet 
        id="1" 
        segmentAlignment="true" 
        maxWidth="3840" 
        maxHeight="2160" 
        maxFrameRate="45000/751"> 
        <SegmentTemplate 
            timescale="1000" 
            media="dash-segment-$Number$-$RepresentationID$.webm" 
            initialization="dash-init-$RepresentationID$.webm" 
            startNumber="1"> 
... 
        </SegmentTemplate> 
      <Representation 
          id="f1-v1-x3" 
          mimeType="video/webm" 
          codecs="av01.0.13M.08" 
          width="3840" 
          height="2160" 
          frameRate="45000/751" 
          sar="1:1" 
          startWithSAP="1" 
```

Here is the full possible format of the link to get the master manifest:

<code-block>
https://domain.com/videos/<span style="color:#FF5913">{client_id}</span>_<span style="color:#FF5913">{video_slug}</span>/master<span style="color:#FF5913">[-(h264|hevc|av1)]</span>.mpd
</code-block>

Where:

- <span style="color:#FF5913">{client_id}</span>: Your account ID.
- <span style="color:#FF5913">{video_slug}</span>: Slug identifier of the video.
- <span style="color:#FF5913">[-min-N]</span>: Special suffix that specifies the lowest video quality limit available in an Adaptive Bitrate (ABR) streaming (same behaviour as for HLS). Learn more about the setting in the <a href="#limit-the-lowest-and-highest-quality-in-hls-adaptive-bitrate">Limit quality</a> section.
- <span style="color:#FF5913">[-max-N]</span>: Special suffix that specifies the highest video quality limit available in the ABR streaming (same behaviour as for HLS). Learn more about the setting in the <a href="#limit-the-lowest-and-highest-quality-in-hls-adaptive-bitrate">Limit quality</a> section.
- <span style="color:#FF5913">[-(h264|hevc|av1)]</span>: Video codec soft limitation. Applicable if the video was simultaneously transcoded into multiple codecs (264, H265, and AV1) and you want to return just one video codec in a manifest. 

<alert-element type="info" title="Info">
 
ABR soft-limiting of video quality isn’t available for DASH format.
 
</alert-element>

Example of the manifest link:  

https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.mpd  

## MP4 format

Video can be streamed and downloaded using the .mp4 file format when you want to handle the whole file at once instead of in chunks. MP4 format allows users to:

- Watch videos offline on mobile devices
- Download video files for local modification
- Play videos even on very outdated devices
- Share videos on social networks and other streaming services
- Content can be protected with <a href="https://gcore.com/docs/streaming-platform/extra-features/protect-your-content-with-temporary-links-and-secure-tokens#how-to-enable-the-secure-token-feature" target="_blank">Secure Token</a>. DRM protection isn’t supported.

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

<alert-element type="tip" title="Tip">
 
You can protect MP4 files with the <a href="https://gcore.com/docs/streaming-platform/extra-features/protect-your-content-with-temporary-links-and-secure-tokens" target="_blank">Video protection via the Security Tokens feature</a>.
 
</alert-element>

## Get HLS, DASH, and MP4 links

You can get links to videos in two ways: in the Gcore Customer Portal or via the <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id" target="_blank">API</a>.

### Customer Portal

1\. In the <a href="https://streaming.gcore.com/video/list" target="_blank">Gcore Customer Portal</a>, navigate to **Streaming** > **Video Hosting**. 

2\. Open the video for which you want to export the link. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/hls-and-mp4/export-video-links.png" alt="Gcore Customer Portal" width="80%">

3\. In the **Links for the export** section, copy the relevant link: 

  * **Video page URL**: A Web player URL to access and play the video directly from a website. 
  * **HLS**: A URL to a master playlist HLS (master.m3u8) with MPEGTS container. 
  * **iFrame embed code**: A URL to our HTML video player with the video inside. It can be inserted into an iframe on your website and the video will automatically play in all browsers.


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
    "hls_cmaf_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master-cmaf.m3u8", 
    "dash_url": "https://demo-public.gvideo.io/videos/2675_FnlHXwA16ZMxmUr/master.mpd", 
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
- ```hls_cmaf_url``` contains the HLS link with CMAF chunks 
- ```dash_url``` contains the MPEG-DASH link 
- ```mp4_url``` contains the MP4 link

## Limit the lowest and highest quality in HLS adaptive bitrate

The manifest file (.m3u8) for HLS and HLS CMAF streaming contains all possible video qualities by default. If you want to limit the quality for old devices, non-paying users, or a quick view, you can specify a suffix indicating the minimum and/or maximum allowed resolution:

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
