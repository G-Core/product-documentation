---
title: content-delivery-speed-is-low-how-to-solve-the-issue
displayName: Low content delivery speed
published: true
order: 30
toc:
   --1--Check the delivery speed from a CDN-resource and an origin server.: "check-the-delivery-speed-from-a-cdn-resource-and-an-origin-server"
   --1--Check CDN-resource's settings: "cdn-resources-settings-checking"
   --1--Diagnostic information for technical support: "diagnostic-information-for-technical-support"
pageTitle: Optimizing CDN Content Delivery Speed | Gcore
pageDescription: Boost your CDN content delivery speed with this detailed guide.
---
# Content delivery speed is low: how to solve the issue

Revise your origin to find errors or misconfigurations that may affect the content delivery speed.  Contact your hosting provider or server administrator for help in the case analysis. 

## Check the delivery speed from a CDN-resource and an origin server 

1\. Measure the content delivery speed from both a CDN-resource and an origin server using:

- DevTools (F12->Network tab->F5).
- Online-services. Consider network settings and location which are chosen for the speed test.   
- wget –S + static file URL.

```
wget -S testsupport.cdn.com/files/test.jpg  
--2019-12-10 13:29:17-- http://testsupport.cdn.com/files/test.jpg  
Resolving testsupport.cdn.com... 92.223.97.97  
Connecting to testsupport.cdn.com|92.223.97.97|:80... connected.  
HTTP request sent, awaiting response...  
HTTP/1.1 200 OK  
Server: nginx  
Date: Tue, 10 Dec 2019 08:29:17 GMT  
Content-Type: image/jpeg  
Content-Length: 290  
Connection: keep-alive  
Last-Modified: Fri, 06 Dec 2019 10:12:14 GMT  
ETag: "5dea297e-122"  
Set-Cookie: 48c62c809b061c360cc201975b7fa802  
Cache: MISS  
X-ID: fr5-up-gc22  
Accept-Ranges: bytes  
Syntax error in Set-Cookie: 48c62c809b061c360cc201975b7fa802 at position 32.  
Length: 290 [image/jpeg]  
Saving to: 'test.jpg'  
  
test.jpg 100%[=================================================>\] 290 --.-KB/s in 0s  
  
2019-12-10 13:29:18 (5,38 MB/s) - 'test.jpg' saved [290/290]
```

2\. Compare the delivery speed from CDN and the origin server. 

3\. If the analysis confirmed issues with content delivery speed from CDN, [revise CDN-resource's settings](https://gcore.com/docs/cdn/troubleshooting/content-delivery-speed-is-low-how-to-solve-the-issue#cdn-resources-settings-checking).

## CDN-resource's settings checking 

1\. Make sure that you don’t use a VPN or proxy.   
VPN affects the CDN Geobalancing and you may receive content from a not optimal edge with lower speed. 

2\. Make sure that content is being cached. The cache rate is presented by <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Cache Hit Ratio report</a>. If you noticed that the cache rate is low, use our <a href="https://gcore.com/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue" target="_blank">instructions</a> to analyze and solve this issue.  

3\. If an issue with content delivery speed occurs with large files, we recommend you to use <a href="https://gcore.com/docs/cdn/cdn-resource-options/optimize-large-file-delivery" target="_blank">Large files delivery optimization</a> and consider content <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression" target="_blank">compression on CDN</a> or the origin server. 

## Diagnostic information for technical support

If you revised your CDN resource's settings but are still unsatisfied with the download speed, contact [technical Support](mailto:support@gcore.com) and provide the following information:

- File URL
- Follow the link ```http://iam.gcdn.co/info```, copy all information from the page or save a screenshot. 
- Follow the try speed test link, click on the Start button, save the result, and add it to the ticket. 

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-delivery-speed-is-low-how-to-solve-the-issue/iam.png" alt="Diagnostic information for technical support" width="50%">

- Wget –S output for the URL from your CDN-resource.
- Open a file or a web-page and save a <a href="https://toolbox.googleapps.com/apps/har_analyzer/?lang=en"target="_blank">HAR file</a>.