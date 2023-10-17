---
title: specify-cache-lifetime-for-user-browsers
displayName: Configure browser caching
published: true
order: 30
toc:
   --1--Browser caching: "what-is-the-browser-caching-option"
   --2--Origin controlled: "origin-controlled"
   --2--CDN controlled: "cdn-controlled"
   --1--Configuration: "how-to-configure-the-browser-caching-option"
pageTitle: Understanding Browsers Cache Lifetime | Gcore
pageDescription: A guide on how to configure the browsers cache lifetime on the origin or CDN side.
---
# Specify cache lifetime for user browsers

## What is the Browser Caching option?

The Browser Caching option allows you to set the period of content caching in the end users' browser. The option has two modes: Origin controlled and CDN controlled. The difference between these two modes is that in the first case, the caching time is configured in your source site's configuration, and in the second case, in the Gcore control panel.

### Origin controlled

If you choose the Origin controlled mode, the content will be cached based on the origin settings specified in the Cache-Control header. For example, if your Cache-Control header is set as *Cache-Control: max-age=172800* on your origin in seconds, the content will be cached for 2 days on the CDN servers.

If the Cache-Control header is not specified, then most browsers will consider the Last-Modified header to decide how to handle files in the cache. 

**Note**: The content will not be cached if there are no cache settings on your origin. 

### CDN controlled

If you choose the CDN controlled mode, the content will be cached based on the cache duration set for this option in the control panel. You can select a value from the list or set a custom value in seconds.

**Note**: Here are the HTTP response codes that can be cached in browsers: 200, 201, 204, 206, 301, 302, 303, 304, 307, 308. Other response codes will not be cached.

If the CDN controlled is selected, the following will be added to the response headers:

- **Cache-Control**. This header specifies the maximum time the object should remain in the local cache as valid. For a 12 hours expiry period, you will see *Cache-Control: max-age=43200*
- **X-Cached-Since**. This header contains the timestamp when the object was initially cached in the CDN cache
- **Expires**. This is a timestamp resulting from ```"NOW()" + Cache-Control->max-age``` telling the client browser to keep this object in cache for the amount of time specified by the max-age parameter in the Cache-Control header.
- **Cache:HIT** or **Cache:MISS**. This shows if the file was delivered from the CDN cache or had to be pulled from the origin. It’s not relevant to the actual caching.

## How to configure the Browser Caching option

1\. Go to the <a href="https://cdn.gcore.com/" target="_blank">CDN resources</a> section.

2\. Click the custom domain name of the CDN resource for which you want to configure Browser Caching.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/browser-caching-10.png" alt="CDN resources tab from where you can open settings" width="80%">

The new page opens. Perform the remaining steps there.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/browser-caching-20.png" alt="Configure Browser Caching Option">

3\. Click on the **Cache** and then select the **Browser Caching** option. 

4\. Toggle on **Enable browser caching**.

5\. Select Origin controlled or CDN controlled in the list. If you set Origin controlled, the configuration is complete; continue to step six. If you select CDN controlled, follow the instructions in the expandable block. 

<expandable-element title="Configure CDN controlled mode">
Choose one of the options from the list. The recommended value is four days.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/" alt="CDN origin configuration/browser-caching-30.png" width="80%">

You can also choose “Custom value” to set an expiry period not presented in the list. For the custom value, you should specify the expiry period in seconds. For instance, if you want to cache content for one day, you need to enter 86400, as there are 86400 seconds in a day.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/" alt="CDN origin configuration/browser-caching-40.png" width="80%">

</expandable-element>

6\. Save changes. 