---
title: specify-http-headers-that-cdn-adds-to-requests-to-the-origin
displayName: Add request headers
published: true
order: 10
toc:
pageTitle: Setting HTTP Headers for CDN Origin Requests | Gcore
pageDescription: A step-by-step guide to configure HTTP headers that a CDN will include when requesting the origin.
---
# Specify HTTP headers that CDN adds to requests to the origin

The Request Headers option allows you to specify HTTP headers that CDN will include when making requests to the origin.

To configure request headers via the control panel:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin/12412498171665.png" alt="CDN_resource.png">

2\. In the navigation panel, under the "HTTP headers" section, click **Request headers**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin/12420674380177.png" alt="navigation panel" width="80%">

3\. Navigate to the "Request headers" section and enable the **Add request headers** toggle option.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin/12422000303377.png" alt="Request headers" width="50%">

4\. In the form that appears, enter the name and value for the request header.

- **Header name**: This field accepts letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_).
- **Value**: This field accepts letters (A-Z, a-z), numbers (0-9), dashes (-), underscores (_), slashes (/), colons (:), equal (=), dots (.), and spaces.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin/12412750658833.png" alt="form " width="50%">

**Note**: If your "Value" field includes multiple words, you can add a space between them. However, the Value field cannot begin or end with a space.

5\. Continue to click **Add header** to add a new item.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin/12412740365585.png" alt="Add header" width="50%">