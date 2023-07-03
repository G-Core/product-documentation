---
title: cache-percentage-is-low-how-to-solve-the-issue
displayName: Low cache hit ratio
published: true
order: 20
toc:
   --1--CDN Caching option: "cdn-caching-option"
   --1--Query-String and Set-Cookies options: "query-string-and-set-cookies-options"
   --1--Large Files Delivery Optimization: "large-files-delivery-optimization"
---
# Cache percentage is low: how to solve the issue

Cached traffic is traffic that is delivered from CDN edge’s cache without request to the origin server. 

You may track the Cache Hit Ratio percentage on the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Report</a> tab. 

Cache Hit Ratio depends on the number of requests and the amount of traffic. If you have noticed that the cache hit ratio is 60% or less: 

1.  Make sure that your website or application is integrated with CDN successfully: the static content is delivered through a custom domain, the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain is set up</a> correctly. 
2.  Make sure that more than 2 days have passed since you have started to use CDN. 
3.  Deliver more content through CDN, if possible. 

If you already set up CDN delivery for all possible static content, but the cache hit ratio remains low, revise the CDN resource’s cache settings: 

## CDN Caching option

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue/_______________________.png" alt="" width="80%">

Check if this option is added and activated. If you use this option with Origin controlled parameter make sure that origin settings are suitable for caching.

CDN caches according to Cache-Control headers from your origin. 

**Note**: Cache-control directives that are not suitable for CDN:  no-cache, no-store, private, max-age=0 

## Query-String and Set-Cookies options

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue/___________________________.png" alt="" width="80%">

CDN caches content with different query-strings and Set-Cookie headers separately by default If you have such content on your website or application, we recommend you to use Ignore Query-String and Ignore Set-Cookies options for the CDN-resource. It will help to decrease the number of requests from CDN to the origin server and increase the Cache hit ratio. 

## Large Files Delivery Optimization 

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue/________________.png" alt="" width="50%">

Use the Large Files Delivery Optimization option for the large content caching. You may know more about the option from the <a href="https://gcore.com/docs/cdn/cdn-resource-options/optimize-large-file-delivery" target="_blank">article</a>. 

If you add any parameters (for example, a unique signature for users) to the URL, but not as a query string (```http://cdn.example.com/image.jpg?id=1```), it requires custom caching keys set up. 

Contact [technical Support](mailto:support@gcore.com) for manual settings and describe the URL scheme: which parts should be cached and which – should not.