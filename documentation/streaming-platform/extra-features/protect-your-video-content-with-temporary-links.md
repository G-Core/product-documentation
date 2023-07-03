---
title: protect-your-video-content-with-temporary-links
displayName: Secure Token
published: true
order: 50
toc:
   --1--What is a Secure token, and how it works: "what-is-a-secure-token-and-how-it-works"
   --1--Configure: "configure-protection-with-temporary-links"
   --2--Enable a feature: "enable-the-secure-token-feature"
   --2--Use PHP script to generate links: "use-the-php-script-for-the-generation-of-urls"
   --3--PHP script for live streams: "php-script-for-live-streams"
---
# Protect your content with temporary links

## What is a Secure token, and how it works

The Secure token is a Gcore CDN feature that helps to protect files from unwanted downloading. You will find more information about the feature in the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/about-secure-token" target="_blank">About Secure Token</a>" article.

As far as streaming is concerned, protection using a Secure token is as follows:

1\. A live stream or video is received into the Streaming Platform with no Secure token protection.

2\. Streaming Platform transcodes the content and forwards it to CDN for delivery.

3\. The Secure token will be added to the following URLs:

*   ```https://123456.gvideo.io/streams/123456_WG99BSGMdZIwKy/1552551429/playlist.m3u8``` (live stream);
*   ```https://123456.gvideo.io/videos/123456_aJ0o71wfUwJvFDklkjlcu/master.m3u8``` (VoD)

## Configure protection with temporary links

### Enable the "Secure token" feature  

1\. Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> section and open the settings of the <a href="https://gcore.com/docs/streaming-platform/how-the-streaming-platform-interact-with-the-cdn" target="_blank">CDN resource used for the streaming</a>.  

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/protect-your-video-content-with-temporary-links/13094971331729.png" alt="" width="80%">

2\. Go to the "Access" section, select **Secure token**, and enable the feature.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/protect-your-video-content-with-temporary-links/13095035340305.png" alt="" width="80%">

3\. Enter a signature key between 6 and 32 characters and click **Save changes**. 

**Note**: Leave the "Add a client's IP to the token" box unchecked.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/protect-your-video-content-with-temporary-links/13095149599633.png" alt="" width="80%">

### Use the PHP script for the generation of URLs 

Once the feature is enabled, a PHP script can generate temporary links for live streams and videos on demand (VoDs).

#### PHP script for live streams

<code-block>

\<?php 
<span style="color:#FF5913">$secret</span> = 'iFCjcOAhQ'; 
<span style="color:#FF5913">$vhost</span> = '123456.gvideo.io'; 
<span style="color:#FF5913">$client_id</span> = '1'; 
<span style="color:#FF5913">$stream_id</span> = '123'; 
<span style="color:#FF5913">$expires</span> = time() + 10000; 
<span style="color:#FF5913">$link</span> = "{$client_id}_{$stream_id}_${secret}_${expires}_"; 
$md5 = md5($link, true); 
$md5 = base64_encode($md5); 
$md5 = strtr($md5, '+/', '-_'); 
$md5 = str_replace('=', '', $md5); 
<span style="color:#FF5913">$url</span> = "https://{$vhost}/streams/{$client_id}_${stream_id}/${md5}/${expires}/playlist.m3u8"; 
echo $url; 
echo "\n";>

</code-block>

### PHP script for VoD

<code-block>
<?php  
<span style="color:#FF5913">$secret</span> = 'iFCjcOAhQ';  
<span style="color:#FF5913">$vhost</span> = '123456.gvideo.io';  
<span style="color:#FF5913">$client_id</span> = '2';  
<span style="color:#FF5913">$video_id</span> = 'aJ0o71wfUwJvFcu';  
<span style="color:#FF5913">$expires</span> = time() + 10000;  
<span style="color:#FF5913">$link</span> = "{$client_id}_{$video_id}_${secret}_${expires}_";  
$md5 = md5($link, true);  
$md5 = base64_encode($md5);  
$md5 = strtr($md5, '+/', '-_');  
$md5 = str_replace('=', '', $md5);  
<span style="color:#FF5913">$url</span> = "https://{$vhost}/videos/{$client_id}_${video_id}/${md5}/${expires}/master.m3u8";  
echo $url;  
echo "\n";
</code-block>

Where you need to substitute your values after the equals in the following lines:

- <span style="color:#FF5913">$secret</span> — a signature key specified in step 3 of this guide.
- <span style="color:#FF5913">$vhost</span> — a subdomain that is used for the streaming,
- <span style="color:#FF5913">$video_id</span> —  slug, an individual parameter in VOD's URL. You will find it in the <a href="https://streaming.gcore.com/video/list" target="_blank">Video Hosting</a> section when you open the video and go to the export tab. For example, in this URL ```https://123456.gvideo.io/videos/123456_AHgywxonRd8F9ctX```, AHgywxonRd8F9ctX is a slug.
- <span style="color:#FF5913">$expires</span>  — URL expiration time (in seconds),
- <span style="color:#FF5913">$link</span> — token generation schema,
- <span style="color:#FF5913">$url</span> — URL.
