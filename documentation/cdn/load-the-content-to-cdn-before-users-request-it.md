---
title: load-the-content-to-cdn-before-users-request-it
displayName: Prefetch
published: true
order: 90
toc:
---
# Load content to the CDN before users request it

Use Prefetch to upload the content to CDN cache before users request it. 

1\. On left in the control panel find Prefetch.  
  
<img src="https://assets.gcore.pro/docs/cdn/load-the-content-to-cdn-before-users-request-it/chrome_2017-04-11_19-12-13.png" alt="">  
  
2\. Choose the desired CDN Resource.

3\. In the field write paths to the files without a domain name that you want to prepopulate to the CDN.

<img src="https://assets.gcore.pro/docs/cdn/load-the-content-to-cdn-before-users-request-it/Screenshot-2018-1-1_G-Core_Labs___________CDN-_________________.png" alt="" width="70%">  

4\. Click on Prefetch.

**Important!** 

 - Prefetch is recommended only for files that **more than 200 MB and less than 5 GB.**
 - If you need to update files stored in the CDN, first <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purge</a> these files and then prefetch.
 - One request for prefetch may content only up to 100 paths to files.
 - There is only 1 request per minute available.

 