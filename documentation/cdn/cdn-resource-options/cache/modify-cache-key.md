---
title: modify-cache-key
displayName: Modify cache key
published: true
order: 70
toc:
   --1--Update cache key in CDN resource settings: "update-cache-key-in-CDN-resource-settings"
   --1--Supported variables: "supported-variables"
pageTitle: Guide to modify a cache key in CDN resource | Gcore
pageDescription: Learn how to customize a cache key in CDN resource settings to improve website performance and speed up content delivery.
---
# Modify cache key
  
A cache key is a unique identifier for each object stored in the cache. It's generated based on specific request attributes like URL, query parameters, headers, or cookies. 

Web servers and proxies like Nginx combine these attributes in cache keys to ensure that the correct version of the content is served to users. Properly configured cache keys also improve your website's performance as they prevent unnecessary server load and speed up content delivery. 

<alert-element type="tip" title="Tip">
 
If you want to modify your cache key via API, refer to our <a href="https://api.gcore.com/docs/cdn#tag/CDN-resources/operation/change_cdn_resource" target="_blank">API documentation</a>.
 
</alert-element>

## Update cache key in CDN resource settings

You can modify the structure of your cache key by adjusting variables that capture essential request information, such as URI or the value of the Host header.

<alert-element type="info" title="Info">
 
Consider that enabling and updating the **Cache key modification** feature can invalidate your current cache and affect the cache hit ratio. Furthermore,  the <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">Purge by pattern</a> functionality won’t work.
 
</alert-element>

To modify the cache key: 

1\. In the Gcore Customer Portal, navigate to CDN. You’ll be directed to the **CDN resources** page. 

2\. Find the resource where you want to modify the cache key and click the CNAME to open its settings.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/modify-cache-key/cdn-resource-name.png" alt="CDN resource" width="80%">

3\. In the **Cache** section, click **Cache key modification**.

4\. Turn on the **Enable cache key modification** toggle and add the relevant <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/modify-cache-key#supported-variables" target="_blank">supported variables</a>, which are listed in the following section. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/modify-cache-key/cache-key-modification-section.png" alt="Cache key modification settings" width="80%">

5\. Click **Save changes** to apply the updates. 

You’ve successfully modified the cache key for your resource. 

## Supported variables

You can use the following variable to modify your resource’s cache key: 

* `$http_host`: The value of the Host header passed in the request header, which comes from the user. 
* `$request_uri`: The full original request URI. If used with the <a href="https://gcore.com/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin" target="_blank">rewrite feature</a> in conjunction with this option, this variable retains the value of the original URI, not the rewritten one. 
* `$scheme`: The protocol used in the request. 
* `$uri`: The current normalized URI in the request. The value of this variable may change during request processing. For example, it’ll change during internal redirects or when using index files. 
