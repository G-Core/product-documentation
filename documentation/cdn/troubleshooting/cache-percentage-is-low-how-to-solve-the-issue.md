---
title: cache-percentage-is-low-how-to-solve-the-issue
displayName: Low cache hit ratio
published: true
order: 20
toc:
    --1--CDN Caching option: "cdn-cachin-option"
    --1--Query-String and Set-Cookies options: "query-string-and-set-cookies-options"
    --1--LargeFilesDeliveryOptimization: "large-files-delivery-optimization"
---
**_Cached traffic_** is traffic that is delivered from CDN edge’s cache without request to the origin server. 

You may track the Cache Hit Ratio percentage on the [Report](https://www.gcore.com/support/articles/115004917425/) tab. 

Cache Hit Ratio depends on the number of requests and the amount of traffic. If you have noticed that the cache hit ratio is 60% or less: 

1.  Make sure that your website or application is integrated with CDN successfully: the static content is delivered through a custom domain, the custom domain is [set up](https://www.gcore.com/support/articles/213969769/) correctly. 
2.  Make sure that more than 2 days have passed since you have started to use CDN. 
3.  Deliver more content through CDN, if possible. 

If you already set up CDN delivery for all possible static content, but the cache hit ratio remains low, revise the CDN resource’s cache settings: 

CDN Caching option
------------------

<img src="https://support.gcore.com/hc/article_attachments/360011328097/_______________________.png" alt="_______________________.png">

Check if this option is added and activated. If you use this option with Origin controlled parameter, make sure that origin settings are suitable for caching.

CDN caches according to Cache-Control headers from your origin. 

**Important!** Cache-control directives that are not suitable for CDN: 

no-cache,     
no-store,    
private,    
max-age\=0 

Query-String and Set-Cookies options
------------------------------------

<img src="https://support.gcore.com/hc/article_attachments/360011328117/___________________________.png" alt="___________________________.png">

CDN caches content with different query-strings and Set-Cookie headers separately by default. If you have such content on your website or application, we recommend you to use Ignore Query-String and Ignore Set-Cookies options for the CDN-resource. It will help to decrease the number of requests from CDN to the origin server and increase the Cache hit ratio. 

Large Files Delivery Optimization 
----------------------------------

<img src="https://support.gcore.com/hc/article_attachments/360011408218/________________.png" alt="________________.png">

Use the Large Files Delivery Optimization option for the large content caching. You may know more about the option from the [article](https://www.gcore.com/support/articles/115001975929/). 

If you add any parameters (for example, a unique signature for users) to the URL, but not as a query string(http://cdn.example.com/image.jpg?id=1), it requires custom caching keys set up. 

Contact [Technical Support](mailto:support@gcore.com) for manual settings and describe the URL scheme: which parts should be cached and which – should not.