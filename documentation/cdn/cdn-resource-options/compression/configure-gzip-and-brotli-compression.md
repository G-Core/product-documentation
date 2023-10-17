---
title: configure-gzip-and-brotli-compression
displayName: GZip, Brotli
published: true
order: 10
toc:
   --1--About the option: "about-the-option"
   --1--Compression methods: "compression-methods"
   --2--Gzip: "gzip"
   --2--Brotli: "brotli"
   --1--Features: "features"
   --1--Configuration guidelines: "configuration-guidelines"
   --1--Configuration steps: "configuration-steps"
pageTitle: Setting Up GZip and Brotli Compression | Gcore
pageDescription: A detailed guide on configuring GZip and Brotli compression on CDN for efficient content delivery.
---
# Configure GZip and Brotli compression

## About the option

Our CDN supports Gzip and Brotli edge compression, so even if your origin server does not support it, you can still serve Gzip or Brotli content to your end users through this feature. When enabled, content is requested in an uncompressed format from the origin, compressed and cached on the edge, and then served to browsers that can support compression.

## Compression methods

### Gzip

The Gzip method reduces file size by 80% and up to 90%. The following MIME types can be compressed using Gzip:

- application/javascript
- application/json
- application/x-javascript
- application/xml
- application/xml+rss
- application/wasm
- text/css
- text/html
- text/javascript
- text/plain
- text/xml
- image/svg+xml

### Brotli

The Brotli method has a higher compression ratio compared to Gzip, and the minimum file size that can be compressed is 128 bytes.

CDN supports Brotli compression only when <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> is activated. If a resource has no shielding set, the content will not be compressed even if the Brotli option is enabled. To activate Origin Shielding, please reach out to our [support team](mailto:support@gcore.com).

You can specify the MIME types to be considered for Brotli compression. These types include:

- **application/javascript**. Selected by default.
- **application/json**. Selected by default.
- **application/x-javascript**. Selected by default.
- **application/xml**. Selected by default.
- **application/xml+rss**. Selected by default.
- **text/css**. Selected by default.
- **text/html**. Selected by default. Cannot be deselected.
- **text/javascript**. Selected by default.
- **text/plain**. Selected by default.
- **text/xml**. Selected by default.
- **application/vnd.ms-fontobject**. Not added by default.
- **application/x-font-ttf**. Not added by default.
- **image/x-icon**. Not added by default.
- **image/svg+xml**. Not added by default.
- **application/wasm**. Not added by default.

**Note**: Image formats (e.g., image/jpeg, image/png), video formats (e.g., video/mpeg), PDF, and other binary formats are already compressed. It is not recommended to apply additional compression to these types as it can actually increase the file size.

## Features

- In order to receive a compressed response, a request must include the *Accept-Encoding* header. This header indicates which compression methods the browser supports. If this header is missing, or if it does not contain a *gzip* or *br* value, the response is given to the user uncompressed.
- If the browser supports both methods and the MIME type of the requested content is configured for both methods, CDN gives precedence to Brotli. If the browser does not support Brotli, CDN falls back to Gzip when the browser supports it. For example, if both compression options are activated. When a browser requests a document of type *text/html* and includes an *Accept-Encoding: gzip, br* header, the response will be compressed with Brotli if Origin Shielding is activated. Otherwise, Gzip will be used.
- Contents that are already cached when Gzip and Brotli are enabled will not be compressed. After enabling the feature, the CDN resource cache must first be purged to ensure that the contents are compressed.
    

## Configuration guidelines

Check the following requirements and recommendations before configuring the options:

- Both Gzip and Brotli compressions can be configured in the Resource Settings and Rules.
- You need to <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purge</a> the CDN resource cache after updating these options.
- Brotli compression is only supported when <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> is enabled. If Brotli is enabled without activating Origin Shielding, the option will not work.
- Gzip and Brotli compressions are not mutually exclusive and can be used together.
- Gzip and Brotli compressions are mutually exclusive with <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-fetch-compression" target="_blank">Fetch Compressed</a> and <a href="" target="_blank">Large Files Delivery Optimization</a> within the Resource Settings and within the same rule. This means that you cannot enable the latter options when Gzip or Brotli is already enabled.
- You can allow all incoming requests to be compressed on the edge, and also allow certain requests to be compressed on the origin. This can be accomplished by enabling Gzip and Brotli compressions in the Resource Settings, and enabling Fetch Compressed in the Rules.  
    
**Note**: Doing it the other way around is not possible. That is, you cannot enable Gzip and Brotli compressions in the Rules when Fetch Compressed is already enabled in the Resource Settings.
    

## Configuration steps

To configure Gzip and Brotli options via the control panel:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression/12422800579217.png" alt="Gzip and Brotli options">

2\. In the navigation panel, under the "Content" section, click **Gzip compression** or **Brotli compression**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression/12423128187537.png" alt="navigation panel">

3\. Turn on the toggle for **Enable Gzip compression** to enable the option.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression/12423333741969.png" alt="Enable_Gzip.png" width="50%">

4\. Turn on the toggle for **Enable Brotli compression** to enable the option. Select the MIME types you want to compress in the "Content types" area.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression/12423398729873.png" alt="Enable_Brotli.png" width="50%">
