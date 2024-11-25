---
title: modify-cache-key
displayName: Modify cache key
published: true
order: 70
toc:
   --1--Update cache key in CDN resource settings: "update-cache-key-in-CDN-resource-settings"
   --1--Supported variables: "supported-variables"
   --1--Best practices and considerations: "best-practices-and-considerations"
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

* `$request_uri`: The full original request URI. If used with the <a href="https://gcore.com/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin" target="_blank">rewrite feature</a> in conjunction with this option, this variable retains the value of the original URI, not the rewritten one. 
* `$scheme`: The protocol used in the request. 
* `$uri`: The current normalized URI in the request. The value of this variable may change during request processing. For example, it’ll change during internal redirects or when using index files. 
  
## Best practices and considerations

When configuring a cache key, take into account the following aspects to ensure optimal cache behavior: 

* Using both `$uri` and `$request_uri` cache keys simultaneously will result in the cache following the `$request_uri` key—query strings won't be ignored because `$request_uri` includes the query string. 

* The `$scheme` cache key does not work correctly when the Redirect HTTP to HTTPS option is enabled. All requests will be redirected to HTTPS, with no cache under the `$scheme` key. 

* Using the `$uri` cache key overrides the <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers" target="_blank">Ignore query string</a> option. 

* Cache keys restricted or added by administrators can’t be modified by the client. You can only select from the available options or <a href="mailto:support@gcore.com" target="_blank">contact support</a> to request changes to such keys. 

* When you use modified cache keys, prefetch may not cover all possible cache cases. For instance, if your cache key includes both the `$request_method` and `$uri`, prefetching will result in warm-only HEAD requests. GET requests won't be preloaded into the cache. 