---
title: protect-your-video-content-with-temporary-links
displayName: Secure Token
published: true
order: 50
toc:
   --1--What is a Secure token, and how it works: "what-is-a-secure-token-and-how-it-works"
   --1--Configure: "configure-protection-with-temporary-links"
   --2--Enable a feature: "enable-the-secure-token--feature"
   --2--Use PHP script to generate links: "use-the-php-script-for-the-generation-of-urls"
   --3--PHP script for live streams: "php-script-for-live-streams"
---


What is a Secure token, and how it works
----------------------------------------

The Secure token is a Gcore CDN feature that helps to protect files from unwanted downloading. You will find more information about the feature in the "[What is Secure Token? How does it work?](https://www.gcore.com/support/articles/214496445/)" article.

As far as streaming is concerned, protection using a Secure token is as follows:

1\. A live stream or video is received into the Streaming Platform with no Secure token protection.

2\. Streaming Platform transcodes the content and forwards it to CDN for delivery.

3\. The Secure token will be added to the following URLs:

*   _https://123456.gvideo.io/streams/123456\_WG99BSGMdZIwKy/1552551429/playlist.m3u8_ (live stream);
*   _https://123456.gvideo.io/videos/123456\_aJ0o71wfUwJvFDklkjlcu/master.m3u8_ (VoD)

Configure protection with temporary links
-----------------------------------------

### Enable the "Secure token" feature  

1\. Go to the [CDN resources](https://cdn.gcore.com/resources/list) section and open the settings of the [CDN resource used for the streaming](https://www.gcore.com/support/articles/5499359292561/).  

<img src="https://support.gcore.com/hc/article_attachments/13094971331729" alt="mceclip0.png" width="640" height="226">
-----------------------------------------------------------------------------------------------------------------------

2\. Go to the "Access" section, select **Secure token**, and enable the feature.

<img src="https://support.gcore.com/hc/article_attachments/13095035340305" alt="mceclip1.png" width="640" height="269">

3\. Enter a signature key between 6 and 32 characters and click **Save changes**. 

**Note**: Leave the "Add a client's IP to the token" box unchecked.

<img src="https://support.gcore.com/hc/article_attachments/13095149599633" alt="mceclip2.png" width="639" height="548">

### Use the PHP script for the generation of URLs 

Once the feature is enabled, a PHP script can generate temporary links for live streams and videos on demand (VoDs).

#### **PHP script for live streams**

<?php $secret = 'iFCjcO1AhQ'; $vhost = '123456.gvideo.io'; $client\_id = '1'; $stream\_id = '123'; $expires = time() + 10000; $link = "{$client\_id}\_{$stream\_id}\_${secret}\_${expires}\_"; $md5 = md5($link, true); $md5 = base64\_encode($md5); $md5 = strtr($md5, '+/', '-\_'); $md5 = str\_replace('=', '', $md5); $url = "https://{$vhost}/streams/{$client\_id}\_${stream\_id}/${md5}/${expires}/playlist.m3u8"; echo $url; echo "\\n"; 

### PHP script for VoD

<?php  
$secret = 'iFCjcO1AhQ';  
$vhost = '123456.gvideo.io';  
$client\_id = '2';  
$video\_id = 'aJ0o71wfUwJvFcu';  
$expires = time() + 10000;  
$link = "{$client\_id}\_{$video\_id}\_${secret}\_${expires}\_";  
$md5 = md5($link, true);  
$md5 = base64\_encode($md5);  
$md5 = strtr($md5, '+/', '-\_');  
$md5 = str\_replace('=', '', $md5);  
$url = "https://{$vhost}/videos/{$client\_id}\_${video\_id}/${md5}/${expires}/master.m3u8";  
echo $url;  
echo "\\n";

Where you need to substitute your values after the equals in the following lines:

*   _$secret_ — a signature key specified in step 3 of this guide.
*   _$vhost_ — a subdomain that is used for the streaming,
*   _$video\_id_ —  slug, an individual parameter in VOD's URL. You will find it in the [Video Hosting](https://streaming.gcore.com/video/list) section when you open the video and go to the export tab. For example, in this URL _https://123456.gvideo.io/videos/123456\_**AHgywxonRd8F9ctX**_, AHgywxonRd8F9ctX is a slug.
*   _$expires_  — URL expiration time (in seconds),
*   _$link_ — token generation schema,
*   _$url_ — URL.
