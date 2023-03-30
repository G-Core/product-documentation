---
title: specify-cache-lifetime-for-user-browsers
displayName: Configure browser caching
published: true
order: 30
toc:
---
You can set up a cache period for the end-users' browser.  
  
<img src="https://support.gcore.com/hc/article_attachments/360005246457/______1.png" alt="______1.png">

Origin controlled

Content will be cached due to origin settings. If there are no cache settings on your origin, the content will not be cached.  
  
<img src="https://support.gcore.com/hc/article_attachments/360005246437/___________.png" alt="___________.png">

CDN controlled

Content will be cached due to the chosen cache duration. The default value is 4 days.  
  
<img src="https://support.gcore.com/hc/article_attachments/360005346418/________.png" alt="________.png">

The list of HTTP response codes that can be cached in browsers: 200, 201, 204, 206, 301, 302, 303, 304, 307, 308. Other response codes will not be cached.