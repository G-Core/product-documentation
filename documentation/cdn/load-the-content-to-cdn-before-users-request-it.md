---
title: load-the-content-to-cdn-before-users-request-it
displayName: Prefetch
published: true
order: 90
toc:
---
Use Prefetch to upload the content to CDN cache before users request it. 

1\. On left in the control panel find Prefetch.  
  
<img src="https://support.gcore.com/hc/article_attachments/115003192585/chrome_2017-04-11_19-12-13.png" alt="chrome_2017-04-11_19-12-13.png">  
  
2\. Choose the desired CDN Resource.  
3\. In the field write paths to the files without a domain name that you want to prepopulate to the CDN.

<img src="https://support.gcore.com/hc/article_attachments/115011325785/Screenshot-2018-1-1_G-Core_Labs___________CDN-_________________.png" alt="Screenshot-2018-1-1_G-Core_Labs___________CDN-_________________.png">  
4\. Click on Prefetch.

**Important!** 

*   Prefetch is recommended only for files that **more than 200 MB and less than 5 GB.**
*   If you need to update files stored in the CDN, first [purge](https://support.gcorelabs.com/hc/en-us/articles/214532065-How-to-clear-CDN-cache-) these files and then prefetch.
*   One request for prefetch may content only up to 100 paths to files.
*   There is only 1 request per minute available.