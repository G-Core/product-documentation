---
title: protect-your-videos-with-the-aes-128-encryption
displayName: AES-128
published: true
order: 50
toc:
   --1--What is AES-128: "what-is-aes-128"
   --1--How it works with VoDs: "how-does-aes-128-work-with-vods"
   --1--Enable: "enable-aes-128"
   --1--Configure: "configure-the-keyserver"
pageTitle: Overview of AES-128 Protection | Gcore
pageDescription: A comprehensive guide on how to protect your videos with AES-128 encryption.
---
# Protect your videos with the AES-128 encryption
  
## What is AES-128?

AES-128, or the Advanced Encryption Standard, is a block encryption algorithm. It operates by using substitutions and permutations on data blocks of 16 bytes with a 128-bit key length, making it difficult for anyone to intercept and decode the information. This encryption method is ideal for scenarios where you need to restrict access to content, such as videos with paid subscriptions. 

For maximum security, it is recommended to use AES-128 in conjunction with the <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies#country-access-policy" target="_blank">country</a> or <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies#referrer-access-policy" target="_blank">domain access policy</a>.

## How does AES-128 work with VoDs?

We deliver VoDs through the <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">HLS protocol</a>. Each video is divided into playlists made up of fragments, or chunks. Using the AES-128 algorithm, these chunks are transmitted in encrypted form. On your end, you need to deploy a server, referred to as a keyserver, that determines which viewers have access to the video and which do not. Viewers who can watch it must retrieve the decryption key from us.

The process for AES-128 video processing is as follows:

**1.** The viewer requests to watch the video and his request is sent to your keyserver.

**2.** The keyserver analyzes the request parameters, which will determine whether the video should be made available to the viewer. This could be based on the presence of cookies, session parameters, or any other method you choose.

**3.a.** If the request does not meet the necessary parameters, access to the video is denied.

**3.b.** If the request meets the required parameters, the keyserver sends a GET request to the Gcore API to retrieve the decryption key.

**4.** The Gcore API provides the key to the keyserver.

**5.** The keyserver sends the key to the viewer, providing access to the video.

## Enable AES-128

To enable the ability to send video using AES-128 encryption, please contact technical support either by email at [support@gcore.com](mailto:support@gcore.com) or through chat.  In the request specify the URL of the keyserver, for example, *client-keyserver.com*. 

Once encryption is enabled, an EXT-X-KEY tag will be added to the playlists (*m3u8*), indicating the URL from which the player will retrieve the key to decrypt the content as follows:

```
EXT-X-KEY:METHOD=AES-128,URI="https://client-keyserver.com/videos/clientId_videoslug/encryption"
```

## Configure the keyserver

When AES-128 is enabled for your account, you need to configure the keyserver to send and redirect requests for the decryption key. 

To do so, use API integration. Send an API request to Gcore API as follows:

```
GET baseUrl/videos/12345_0zdztmmvdxe8zpo/encryption
```

Were

- *12345* is the ID of your Gcore account;
- *0zdztmmvdxe8zpo* is the slug that identifies the video.

This request will allow your keyserver to retrieve the decryption key, which should then pass to the viewer in its original format. An example of a decryption key is: 

```
W�U����<)B�4�
```

To pass the key in this format, you can use the following HTTP headers:

- Content-transfer-encoding: binary
- Content-type: application/octet-stream