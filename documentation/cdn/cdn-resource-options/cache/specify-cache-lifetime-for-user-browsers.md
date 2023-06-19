---
title: specify-cache-lifetime-for-user-browsers
displayName: Configure browser caching
published: true
order: 30
toc:
   --1--Origin controlled: "origin-controlled"
   --1--CDN controlled: "cdn-controlled"
---
# Specify cache lifetime for user browsers

You can set up a cache period for the end-users' browser.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/______1.png" alt="" width="70%">

## Origin controlled

Content will be cached due to origin settings. If there are no cache settings on your origin, the content will not be cached.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/___________.png" alt="" width="70%">

## CDN controlled

Content will be cached due to the chosen cache duration. The default value is 4 days.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers/________.png" alt="" width="70%">

The list of HTTP response codes that can be cached in browsers: *200*, *201*, *204*, *206*, *301*, *302*, *303*, *304*, *307*, *308*. Other response codes will not be cached.