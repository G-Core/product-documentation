---
title: protect-your-content-with-temporary-links-and-secure-tokens
displayName: Protected temporary link
published: true
order: 50
toc:
   --1--Why protect?: "why-protect-video-content"
   --1--How Gcore protects: "how-does-gcore-protec-video-content"
   --1--Temporary links: "what-are-protected-temporary-links"
   --1--Restrictions: "cdn-resources-and-scope-of-restrictions"
   --1--Enable Secure Token: "how-to-enable-the-secure-token-feature"
   --1--Format: "format-of-protected-temporary-links"
   --1--Expiration time: "a-note-on-the-expiration-time"
   --1--Create protected links: "how-to-create-protected-links-with-the-secure-token"
   --2--Python: "python"
   --2--Go: "go"
pageTitle: Protected Temporary Links | Gcore
pageDescription: A guide on how to restrict access to your video content using the Secure Token feature.
---
# Protect your content with temporary links and secure tokens

## Why protect video content?

By default, videos are available by their links with no restrictions and can be placed on any website or in any mobile application. But in some cases, platform owners or rights holders need to ensure that video content does *not* offer public access, such as when a video is only for paid access, private access, access by country, temporary access, or access on a specific site.

## How does Gcore protect video content?

Gcore has several methods of protecting video content:

1. Protected temporary links
2. <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies#country-access-policy" target="_blank">Country access policy (Geo-restrictions)</a>
3. <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies#allow-referrer-policy" target="_blank">Referrer validation</a>
4. <a href="https://gcore.com/docs/streaming-platform/video-hosting/protect-your-videos-with-the-aes-128-encryption" target="_blank">AES-128 encryption</a>

We plan to add more types of protections in the future, such as watermarking. Contact us via [support@gcore.com](mailto:support@gcore.com) if you want to suggest additional options.

In this article, we will look at the first option: protected temporary links and, relatedly, Secure Tokens.

## What are protected temporary links?

Protected temporary links are generated using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/about-secure-token" target="_blank">Secure Token</a> feature, which allows configuring access with tokenized URLs. When using this option, you add a special character set to every URL. Check out the examples below with the special characters highlighted in bold. At Gcore, we call these special characters *Secure Tokens*.

- Public: https://demo-public.gvideo.io/videos/2675_3dk4NsRt6vWsffEr/master.m3u8 
- Protected: https://demo-protected.gvideo.io/videos/2675_3dk4NsRt6vWsffEr/4KF8O8YERpLuwIIO_p3RFQ/1861919999/master.m3u8 

Unlike content with a public URL, which is available to any user, content with a protected temporary link verifies that the user has a special *hash key* that matches the generated token.

There are three possible scenarios:

- HTTP 2xx response code, if the hash key is valid and unexpired
- HTTP 403 Forbidden response, if the hash key is invalid
- HTTP 410 Gone response, if the hash key is valid but expired

Here is an example of what happens if we try to access the video when the token is expired:

```
curl --head https://demo-protected.gvideo.io/videos/2675_3dk4NsRt6vWsffEr/bbP3uBs-rBM_HY1VfWS5-Q/1688124955/master.m3u8

HTTP/1.1 410 Gone
Server: nginx
Date: Fri, 07 Jul 2023 06:42:28 GMT
Content-Type: text/html
Content-Length: 136
Connection: keep-alive
X-ID: ed-hw-edge-gc38
X-ID-FE: ed-hw-edge-gc38
```

## CDN resources and scope of restrictions

Video content hosted via the Streaming Platform is viewed and delivered through our CDN, so by default your account has only one hidden CDN resource in the format *\*\*\*\*\*\*.gvideo.io*.

The restriction policies, such as the Secure Token for links protection, apply specifically to CDN resources because a CDN resource covers all video content at once. This means you don’t need to create rules and make permissions for each video separately—it is enough to create and apply permissions only once to the CDN resource.

Moreover, your account can have several CDN resources leading to the same content (origin). These CDN resources can be with different access policies. So you can combine open access on one CDN resource, and private access on another one, etc.

## How to enable the Secure Token feature?

To enable the Secure Token feature and start protecting your links, please <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token" target="_blank">check out our product docs on the topic</a>.

## Format of protected temporary links

Secure Token-protected temporary links have the following format: 

<code-block>
https://domain.com/videos|cmaf/<span style="color:#FF5913">{client_id}</span>_<span style="color:#FF5913">{video_id}</span>/<span style="color:#FF5913">{token}</span>/<span style="color:#FF5913">{expiration}</span>/manifest.m3u8
</code-block>

Where:

- <span style="color:#FF5913">{client_id}</span> is your account ID
- <span style="color:#FF5913">{video_id}</span> is the identifier of the video or live stream
- <span style="color:#FF5913">{token}</span> is the MD5 hash of the video and other attributes
- <span style="color:#FF5913">{expiration}</span> is the unix time in seconds of how long will the link be valid

Example: https://demo-protected.gvideo.io/cmaf/2675_201693/cFLm6j00eFFuvos2HZ-6hA/1861919999/master.m3u8 

For Gcore Video on Demand (VOD) and Gcore Live Streaming, a relative path is used for all file types used to deliver video content, such as additional manifests, chunks, and MP4 renditions. Therefore, the path of the main manifest is taken as the basis and the following path is built relative to it.

Examples of protected links for VOD:

- ```https://domain.com/videos/{client_id}_{video_slug}/{token}/{expiration}/```<b>manifest.m3u8</b>
- ```https://domain.com/videos/{client_id}_{video_slug}/{token}/{expiration}/```<b>segment-1-svod720n-v1-a1.ts</b>
- ```https://domain.com/videos/{client_id}_{video_slug}/{token}/{expiration}/```<b>720.mp4</b>


Examples of protected links for Gcore Live Streaming:

- ```https://domain.com/cmaf/{client_id}_{stream_id}/{token}/{expiration}/```<b>master.m3u8</b>
- ```https://domain.com/cmaf/{client_id}_{stream_id}/{token}/{expiration}/```<b>index.mpd</b>
- ```https://domain.com/cmaf/{client_id}_{stream_id}/{token}/{expiration}/```<b>004chunk-stream4-10000000-05213.m4s?part=4</b>

## A note on the expiration time

The expiration time must be at least equal to the duration of the original video or the expected duration of the live playback. When the signed URL expires, URLs will no longer be played, even if playback has already begun. Because video expiration time is integrated into the URL described above, new chunks will no longer be given by the relative path.

Your app also needs to handle cases where a user starts to play a video, then leaves your app for a long time, and then comes back later and tries to play the video again. You will probably need to detect this behavior and reacquire the new signed URL to make sure playback can start.

To handle both cases, ensure you set the expiration far enough into the future that users won’t experience playback interruptions.

```
expires = 1861919999   # Sunday, December 31, 2028 23:59:59 GMT
```

## How to create protected links with the secure token

**Note**: Generating a Secure Token requires the same process for both VOD and Live Streaming. 

### Python

```
import base64
from hashlib import md5
from time import time

def gethash(client_id, video_id, secret, expires):
    hash_body = "%s_%s_%s_%s_" % (client_id, video_id, secret, expires)   # set of unique parameters of video
    hash_md5 =  base64.b64encode(                                         # get MD5 hash from parameters of video
            md5(hash_body.encode()).digest()                            
        ).decode().replace("+", "-").replace("/", "_").replace("=", "")   # preparation for use in URL 
    return hash_md5

client_id = "2675"       # enter your account ID here
secret = ""              # enter your secret key from CDN-resource here

#VOD
video_slug = "3dk4NsRt6vWsffEr"     # enter your video's slug here
expires = int(time()) + 24*60*60    # 24 hours, unixtime in seconds

token = gethash(client_id, video_slug, secret, expires)
print(f"https://demo-protected.gvideo.io/videos/{client_id}_{video_slug}/{token}/{expires}/master.m3u8")

#LIVE
stream_id = "201693"                      # enter your live stream id here
expires = int(time()) + 24*60*60    # 24 hours, unixtime in seconds

token = gethash(client_id, stream_id, secret, expires)
print(f"https://demo-protected.gvideo.io/cmaf/{client_id}_{stream_id}/{token}/{expires}/master.m3u8")

```

### Go

```
package main

import (
	"crypto/md5"
	"encoding/base64"
	"fmt"
	"strings"
	"time"
)

func gethash(client_id string, video_id string, secret string, expires int64) string {
	hash_body := fmt.Sprintf("%s_%s_%s_%d_", client_id, video_id, secret, expires)   // set of unique parameters of video

	md5sum := md5.Sum([]byte(hash_body))                   // get MD5 hash from parameters of video
	hash_md5 := base64.StdEncoding.EncodeToString(md5sum[:])

	hash_md5 = strings.Replace(hash_md5, "+", "-", -1)     // preparation for use in URL
	hash_md5 = strings.Replace(hash_md5, "/", "_", -1)
	hash_md5 = strings.Replace(hash_md5, "=", "", -1)
	return hash_md5
}

func main() {
	client_id := "2675"        // enter your account ID here
	secret := ""               // enter your secret key from CDN-resource here

	//VOD
	video_slug := "3dk4NsRt6vWsffEr"		// enter your video's slug here
	expires := time.Now().Unix() + 24*60*60		// now + 24 hours, unixtime in seconds

	token := gethash(client_id, video_slug, secret, expires)
	fmt.Printf("https://demo-protected.gvideo.io/videos/%s_%s/%s/%d/master.m3u8 \n", client_id, video_slug, token, expires)

	//LIVE
	stream_id := "201693"				// enter your live stream id here
	expires = time.Now().Unix() + 24*60*60		// now + 24 hours, unixtime in seconds

	token = gethash(client_id, stream_id, secret, expires)
	fmt.Printf("https://demo-protected.gvideo.io/cmaf/%s_%s/%s/%d/master.m3u8 \n", client_id, stream_id, token, expires)
}

```