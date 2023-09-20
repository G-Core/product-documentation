---
title: load-the-content-to-cdn-before-users-request-it
displayName: Prefetch
published: true
order: 90
toc:
pageTitle: Using Prefetch to prepopulate CDN cache | Gcore
pageDescription: A step-by-step guide on how to use Prefetch to upload content to CDN cache before user requests.
---
# Load content to the CDN before users request it

Use Prefetch to upload the content to CDN cache before users request it. 

1\. Go to the <a href="https://cdn.gcore.com/" target="_blank">CDN</a> section on left in the control panel find **Prefetch**.  
  
2\. Choose the desired CDN Resource.

3\. In the field write paths to the files without a domain name, e.g. ```path/file1.jpg```, that you want to prepopulate to the CDN.

<img src="https://assets.gcore.pro/docs/cdn/load-the-content-to-cdn-before-users-request-it/prefetch-hint.png" alt="Prefetch" width="80%">  

4\. Click on **Prefetch**.

**Important!** 

 - Prefetch is recommended only for files that **more than 200 MB and less than 5 GB.**
 - If you need to update files stored in the CDN, first <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purge</a> these files and then prefetch.
 - One request for prefetch may content only up to 100 paths to files.
 - There is only 1 request per minute available.