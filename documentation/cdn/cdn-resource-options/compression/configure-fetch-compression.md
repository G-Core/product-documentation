---
title: configure-fetch-compression
displayName: Fetch
published: true
order: 20
toc:
   --1--Fetch compressed: "fetch-compressed"
   --1--Option features: "option-features"
   --1--Content compression without settings on CDN: "content-compression-without-settings-on-cdn"
   --2--Origin supports compression: "origin-supports-compression"
   --2--Origin doesn't support compression: "origin-doesnt-support-compression"
pageTitle: Guide to Configuring Fetch Compression | Gcore
pageDescription: Discover how to configure Fetch compression on CDN to reduce bandwidth and enhance content delivery speed.
---
# Configure Fetch compression

## Fetch compressed

The Fetch compressed option helps you to reduce the bandwidth between origin and CDN servers. Also, content delivery speed becomes higher because of reducing the time for compressing files in a CDN.   

You can activate the option in the resource settings in the Content section.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/compression/configure-fetch-compression/fetch_compressed.png" alt="Fetch compressed">

Enable "Fetch compressed" to make a CDN pull already compressed content.

Your server should support **GZip compression**.

**Note**: If the origin server compresses content using the Brotli method, the CDN gets the uncompressed content, unless otherwise configured. If the origin server compresses content using the Brotli method, but you want the CDN to get the compressed content, configure the origin to send a Brotli file when CDN requests a Gzip file.

## Option features

- CDN servers won't unzip your content, even if a user's browser doesn't accept compression.
- The Fetch compressed option and  <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression#gzip" target="_blank">GZip Compression</a> exclude each other and don't work together.  

## Content compression without settings on CDN 

### Origin supports compression 

If you want to send compressed or uncompressed content via CDN depending on the request received from the end-user, disable all compression settings in your personal account and make some settings on your server.  

On the origin should be configured two HTTP headers: Vary: Accept-Encoding and Content-Encoding.

While processing a request from end-users, CDN servers check the Accept-Encoding HTTP header.

If the header contains gzip and/or deflate, br, meaning that the browser can accept compressed content, the CDN will request the compressed version of the file from the origin. If there are no such directives, the server will send an uncompressed file. 

- If the Vary: Accept-Encoding header is not configured on the server, the CDN will cache the file that was first requested (compressed or not). This may cause difficulties in displaying content for the end-user. For example, you need to send an uncompressed file from the CDN to the end-user, but there is only a compressed file in the CDN cache. Then the user will get the compressed file, and the browser will not be able to display it. 

- If the Vary: Accept-Encoding header is configured, two versions of the file store in the CDN servers’ cache.   

### Origin doesn't support compression 

The CDN servers store an uncompressed version of the file. Regardless of whether the end-user requests a compressed file or not, from the cache will be sent an uncompressed file.