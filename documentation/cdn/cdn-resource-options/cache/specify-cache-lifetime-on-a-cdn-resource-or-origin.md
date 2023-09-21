---
title: specify-cache-lifetime-on-a-cdn-resource-or-origin
displayName: Configure CDN caching
published: true
order: 10
toc:
   --1--What is CDN caching?: "what-is-the-cdn-caching-feature"
   --1--Configure: "configure-cdn-caching"
   --2--Origin controlled: "origin-controlled"
   --2--CDN controlled: "cdn-controlled"
   --1--Check: "check-cdn-caching-settings"
   --2--using cURL: "check-through-curl"
   --2--in a browser: "check-with-devtools-in-a-browser"
   --2--caching headers: "check-caching-http-headers"
pageTitle: Setting CDN Cache Lifetime on Origin or CDN Side | Gcore
pageDescription: A guide on how to configure the CDN resource cache lifetime on the origin or CDN side.
---
# Specify cache lifetime on a CDN resource or origin

## What is the CDN caching feature?

Files cannot be stored in the CDN servers' cache indefinitely. The CDN caching feature allows setting how long requested files from your origin server will be stored in the CDN server's cache. If end-users request these files, they will be loaded from the cache without additional requests to the origin server, reducing delivery time, financial spending, and the origin server load.  

**Note**: Files users have not requested within 36 hours will be removed from the CDN servers' cache, regardless of the feature settings.

When the specified timespan for storing files in the cache has expired, CDN servers send requests to the origin to compare the HTTP "<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag" target="_blank">Etag</a>" header and determine if the files have changed.

If the values of the "Etag" header for previous and current versions do not match, CDN servers load a new version and cache it for the time specified in the feature. If the values match, the storage time of the file in the cache is extended for the specified time.

## Configure CDN caching

The CDN caching feature has two options: Origin controlled (enabled by default) and CDN controlled. You can choose one of them and set the caching time either in the origin server's HTTP "Cache-Control" header or the CDN control panel.

### Origin controlled

1\. Depending on your web server (Apache or Nginx), add the "Cache-Control" header with the _max-age_ and _public_ parameters to the .htaccess (for Apache) or nginx.conf (for Nginx) file.

Here is an example of the Apache configuration where we have established that .gif and .ico files can be cached (the _public_ parameter) and that they should be cached by CDN servers for 4 days (_max-age=345600_ in seconds):

```
<ifModule mod_headers.c>   
 <FilesMatch "\.(gif|ico)$">   
   Header set Cache-Control "max-age=345600, public"   
 </FilesMatch>   
</ifModule> 
```

Here is an example of the Nginx configuration where we have established that all ico, css, js, gif, jpeg, and png files can be cached (the _public_ parameter) and that they should be cached by CDN servers for about 1 day (_max-age=88000_ in seconds):

```
server {   
 #...   
  location ~* \.(?:ico|css|js|gif|jpeg|png)$ {   
    add_header Cache-Control "max-age=88000, public";   
  }   
 #...   
} 
```

2\. Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN</a> section in the control panel and click the custom domain of the resource on which origin you configured the Cache-Control header.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin/13249373793809.png" alt="CDN section">

The new page opens. Do the remaining steps on it.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin/13249168410769.png" alt="The new page opens" width="80%">

3\. Go to the "Cache" section and click **CDN caching**.

4\. Make sure that the “Origin controlled” option is selected in the feature.

5\. Specify the timespan in the "Default cache expiry" field. You can select the defined values from the list or choose **Custom value** and enter the time in seconds. If something goes wrong and the directives for the "Cache-Control" header are lost, files will be cached for the time specified in the field.

6\. Save changes.

### CDN controlled

1\. Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN</a> section in the control panel and click the custom domain of the resource for which you want to configure the CDN caching feature.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin/13249311265809.png" alt="CDN controlled">

The new page opens. Do the remaining steps on it.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin/13249271726353.png" alt="The new page opens" width="80%">

2\. Go to the "Cache" section and click **CDN caching**.

3\. Enable the "CDN controlled" option.

4\. Specify the timespan in the "Cache expiry" field. You can select the defined values from the list or choose **Custom value** and enter the time in seconds. If you specify "Do not cache", caching will be disabled.

**Note**: This caching time will be applied for response codes 200, 206, 301, and 302. Responses with 4xx and 5xx will not be cached.

5\. (Optional) Set advanced caching rules if you want to set different caching times for specific responses. Click **Add rule**, type the response code and select the caching time.

**Note**: "Advanced caching rules" values have a higher priority than the "Cache expiry" values.

For instance, if we set a cache expiry of 4 days and add two rules in the "Advanced caching rules" section: one for 200 response code configured for 10 minutes and the other for 404 response code for 1 minute - the requests will be cached as follows:

- Requests with response code 200 will be cached for 10 minutes.
- Requests with response code 404 will be cached for 1 minute.
- Requests with response codes 206, 301, and 302 will be cached for 4 days.
- Requests with response codes 4xx (except 404) and 5xx will not be cached.

6\. Save changes. 

## Check CDN caching settings

### Check through cURL

1\. Open the terminal on macOS or command prompt (cmd) on Windows.

2\. Run the following command:

<code-block>
curl -I <span style="color:#FF5913">http://cdn.testdomain.com/css/style.css</span>
</code-block>

where <span style="color:#FF5913">http://cdn.testdomain.com/css/style.css</span> is a link to your file delivered via CDN.

You will receive the output. Pay attention to the highlighted headers in bold. They are described in the "[Check caching headers](https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin#check-caching-http-headers)" section.

```
HTTP/1.1 200 OK   
Server: nginx/1.13.1   
Date: Fri, 09 Jun 2017 12:54:24 GMT   
Content-Type: image/jpeg   
Content-Length: 124024   
Connection: keep-alive   
X-Image-Generated: 29   
X-Image-Meta: 1024x768   
X-Image-Read: 71   
Expires: Wed, 06 Dec 2017 12:51:43 GMT   
Access-Control-Allow-Origin: *   
Last-Modified: Sun, 01 Jan 2017 12:00:00 GMT   
Cache-Control: max-age=3153600, public  
Cache: HIT   
X-Cached-Since: 2017-06-09T12:51:43+00:00  
X-ID: m9-up-e245
```

If you suspect any content caching issues, check the settings on the source, read the "<a href="https://gcore.com/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue" target="_blank">Troubleshooting Low Cache Hit Ratio</a>" article, or contact [support@gcore.com](mailto:support@gcore.com).

### Check with DevTools in a browser

1\. Open any internet browser (e.g., Google Chrome).

2\. Go to your website.

3\. Right-click and select **Inspect** to open the DevTools (Developer Toolbar).

4\. Select the "Network" tab.

5\. Refresh the page.

6\. You will get a list of all files retrieved from your website.

7\. Find any file (e.g., JPEG, PNG, IMG, CSS, etc.) integrated with the CDN and select it.

8\. On the "Headers" tab on the right, you will see the configured headers. Analyze them using the description of the important headings below.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin/13249609604753.png" alt="Headers tab" width="80%">

### Check caching HTTP headers

There are several HTTP header parameters that help analyze the state of the cache:

| HTTP header with parameters             | Explanation                                                                                                                                                                                                                                                                                           |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CACHE: HIT                              | The file has been delivered from the CDN. This parameter indicates that caching is working correctly.                                                                                                                                                                                                     |
| CACHE: MISS                             | The file has been delivered from your origin server. Try to reload the page and clear the browser cache. If the value remains, it indicates something went wrong, and the file is not delivered from the cache.                                                                                           |
| X-ID: ab-cd-d123                          | The file has been delivered from the Gcore CDN server with the identifier ab-cd-d123.                                                                                                                                                                                                                     |
| X-Cached-Since: 2023-02-23T14:33:07+00:00 | The time when the file was cached in the CDN server in UTC.       |                                                                                                                                                                                                                                       