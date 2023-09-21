---
title: ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers
displayName: Ignore Set Cookie or Query string
published: true
order: 40
toc:
   --1--Ignore Query string: "query-string-setting"
   --1--Ignore Set-Cookie: "set-cookie-setting"
pageTitle: Manage CDN caching with Query String and Set-Cookie | Gcore
pageDescription: A detailed guide on managing CDN caching by ignoring query strings or Set-Cookie parameters.
---
# Ignore the Set Cookie or Query string parameters when caching content on CDN servers

## Query string setting

The "Ignore Query String" option determines how the CDN will cache URLs that have query parameters. Query parameters are optional pairs of key and value separated by an equal sign (=) and joined by an ampersand (&), that appear at the end of a URL following a question mark (?). For example:

```
http://cdn.example.com/photo.jpeg?id=6&color=blue
```

This option is disabled by default. To enable it via the Control panel:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/12414969223185.png" alt="CDN resource ">

2\. In the navigation panel, under the "Cache" section, click **Query string**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/12420789740177.png" alt="Cache" width="80%">

The enabled option has 3 modes:

- **Ignore All**. Selected by default. Files with different query parameters are cached as objects with the same key, regardless of the parameter value.
    
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/12415341115665.png" alt="Ignore All" width="50%">
    
For example, the following files will be cached as objects with a single cache key because all parameters will be ignored:
    
```
http://cdn.example.com/photo.jpeg?id=6&color=blue  
http://cdn.example.com/photo.jpeg?id=1&color=blue
```
    
- **Ignore All Except**. Files with the specified query parameters are cached as objects with different keys; files with other parameters are cached as objects with the same key.

In the **Parameter** field, enter each parameter on a separate line.
    
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/12415729590801.png" alt=" Parameter field," width="50%">
    
For example, you specified *id* in the Parameter field. The following files will be cached as objects with different keys because the values of the *id* parameter are different, and the value of the *color* parameter will be ignored.

```    
http://cdn.example.com/photo.jpeg?id=6&color=blue  
http://cdn.example.com/photo.jpeg?id=1&color=blue
```

For example, you specified *color* in the Parameter field. The following files will be cached as objects with the same keys because the values of the *color* parameter are the same, and the *id* parameter will be ignored.
    
```
http://cdn.example.com/photo.jpeg?id=6&color=blue  
http://cdn.example.com/photo.jpeg?id=1&color=blue
```
    
- **Ignore only**. Files with the specified query parameters are cached as objects with the same key, files with other parameters are cached as objects with different keys.
    
In the **Parameter** field, enter each parameter on a separate line.
    
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/12415745809041.png" alt=" Parameter field" width="50%">
    
For example, you specified *id* in the Parameter field. The following files will be cached as objects with the same keys because the values of the *id* parameter will be ignored, and the values of the *color* parameters are the same.
    
```
http://cdn.example.com/photo.jpeg?id=6&color=blue  
http://cdn.example.com/photo.jpeg?id=1&color=blue
```
    
For example, you specified *color* in the Parameter field. The following files will be cached as objects with different keys because the values of the *color* parameter will be ignored, and the values of the *id* parameters are different.
    
```
http://cdn.example.com/photo.jpeg?id=6&color=blue  
http://cdn.example.com/photo.jpeg?id=1&color=blue
```

## Set-Cookie setting

A CDN defines a file with the Set-Cookies header as a unique one. As a result, each user’s request goes to the origin. This option defines whether we will cache files with the Set-Cookies header as one file or as different ones. In most cases, it is not effective to have copies of the same file with different cookies on the server.

Enable Ignore Set-Cookie option and files with cookies will be cached like one object. Go to CDN Resources, choose a CDN Resource and press Settings, open Advanced Settings and check Ignore Set-Cookies.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers/Screenshot-2018-1-1_G-Core_Labs___________CDN-___________________8_.png" alt="Set-Cookie setting">