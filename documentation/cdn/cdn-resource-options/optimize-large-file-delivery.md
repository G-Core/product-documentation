---
title: optimize-large-file-delivery
displayName: Large files delivery
published: true
order: 60
toc:
   --1--About the option: "about-the-option"
   --1--Configuration guidelines: "configuration-guidelines"
   --1--Configuration steps: "configuration-steps"
---
  
  

About the option
----------------

If you are serving content larger than 10 MB, we recommend using the _Large Files Delivery Optimization_. With this option, the CDN will make range requests to the origin to retrieve 10-MB chunks of the content. These chunks are then collected in the cache, and once the CDN has the necessary portions of the requested content, the response is assembled and returned to the end user.

A range request includes the _Range_ HTTP header to indicate the byte or part of the content to be returned. For example, if the request has a _Range: bytes=123537047-123545047_ header, the CDN will request a 10-MB chunk from the origin (byte range 115343360-125829119), cache this chunk, and serve the requested range (123537047-123545047) to the end user.

For this option to work, the origin server must support range requests.

Configuration guidelines
------------------------

Make sure to review these requirements and recommendations before configuring the option.

*   The origin server must support HTTP Range Requests.
*   The _Content-Length_ and _Etag_ headers must be consistent across the origin.
*   This optimization will be applied to all contents in the CDN resource, which could lead to an increased load on the origin. Therefore, consider activating [Origin Shielding](https://gcore.com/support/articles/214080309/) before using this feature, or make any updates during off-peak hours.
*   This option can be configured in the Resource Settings and Rules.
*   Remember to [purge](https://gcore.com/support/articles/11762165947665/) the resource cache after updating this option.
*   This option is mutually exclusive and cannot be used in conjunction with [Fetch Compressed](https://gcore.com/support/articles/360006563578/), [Gzip Compression](https://gcore.com/support/articles/360006563858/), and [Brotli Compression](https://gcore.com/support/articles/360006563858/) within the Resource Settings or within the same rule.

Configuration steps
-------------------

To configure Large Files Delivery Optimization option via the control panel:

1\. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/12478782810513" alt="CDN_resource.png">

2\. In the navigation panel, under the **Content** section, click **Large files delivery optimization**.

<img src="https://support.gcore.com/hc/article_attachments/12479228932497" alt="Large_Files_Delivery_Optimization_option.png">

3\. Turn on the toggle for **Enable Large files delivery optimization** to enable the option.

<img src="https://support.gcore.com/hc/article_attachments/12479601956241" alt="Enable_Large_Files_Delivery_Optimization_option.png" width="524" height="226">