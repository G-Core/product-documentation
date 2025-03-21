---
title: optimize-large-file-delivery
displayName: Large files delivery
published: true
order: 60
toc:
   --1--Configuration guidelines: "configuration-guidelines"
   --1--Configuration steps: "configuration-steps"
pageTitle: Optimizing Large File Delivery via CDN | Gcore
pageDescription: Guide on efficiently serving large files (>10MB) using Gcore CDN Large File Delivery Optimization feature.
---
# Optimize large file delivery

We recommend using the Large File Delivery Optimization feature if you are serving content larger than 10 MB. With this option enabled, Gcore CDN will make range requests to the origin to retrieve 10 MB chunks of content. These chunks are then collected in the cache, and once the CDN has the necessary portions of the requested content, the response is assembled and returned to the end user.

A range request includes the *Range* HTTP header to indicate the byte or part of the content to be returned. For example, if the request has a *Range: bytes=123537047-123545047* header, the CDN will request a 10 MB chunk from the origin (byte range 115343360-125829119), cache this chunk, and serve the requested range (123537047-123545047) to the end user.

For this option to work, the origin server must support range requests.

## Configuration guidelines

Large File Delivery Optimization can be configured in the Resource Settings and Rules. Review the following requirements and recommendations before configuring the option:

- The origin server must support HTTP Range Requests.
- The *Content-Length* and *Etag* headers must be consistent across the origin.
- Large File Delivery Optimization will be applied to all contents in the CDN resource, which could lead to an increased load on the origin. Therefore, consider activating <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> before using this feature, or make any updates during off-peak hours.
- Remember to <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purge the resource cache</a> after enabling Large File Delivery Optimization.
- Large File Delivery Optimization cannot be used in conjunction with <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-fetch-compression" target="_blank">Fetch Compressed</a>, <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression#gzip" target="_blank">Gzip Compression</a>, and <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression#brotli" target="_blank">Brotli Compression</a> within the Resource Settings or within the same rule.

## Configuration steps

To enable Large File Delivery Optimization option via the Gcore Customer Portal, follow these three steps:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/optimize-large-file-delivery/12478782810513.png" alt=" CDN resource ">

2\. In the navigation panel, under **Content**, click **Large files delivery optimization**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/optimize-large-file-delivery/12479228932497.png" alt="Content section" width="80%">

3\. Turn on the toggle for **Enable Large files delivery optimization**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/optimize-large-file-delivery/12479601956241.png" alt="Enable Large files delivery optimization " width="50%">

<alert-element type="warning" title="Warning">

When Large File delivery optimization is enabled, the HTTP *Etag* header will be concealed in responses.

</alert-element>
