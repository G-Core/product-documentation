---
title: ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers
displayName: Ignore Set Cookie or Query string
published: true
order: 40
toc:
   --1--Ignore Query string: "query-string-setting"
   --1--Ignore Set-Cookie: "set-cookie-setting"

---
  
  
  

The _Ignore Query String_ option determines how the CDN will cache URLs that have query parameters. Query parameters are optional pairs of key and value separated by an equal sign (=) and joined by an ampersand (&), that appear at the end of a URL following a question mark (?). For example:

http://cdn.example.com/photo.jpeg?id=6&color=blue

## Query string setting

This option is disabled by default. To enable it via the control panel:

1\. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/12414969223185" alt="CDN_resource.png">

2\. In the navigation panel, under the **Cache** section, click **Query string**.

<img src="https://support.gcore.com/hc/article_attachments/12420789740177" alt="Query_String_option.png">

The enabled option has 3 modes:

*   **Ignore All**. Selected by default. Files with different query parameters are cached as objects with the same key, regardless of the parameter value.
    
    <img src="https://support.gcore.com/hc/article_attachments/12415341115665" alt="Ignore_All_option.png" width="522" height="176">
    
    For example, the following files will be cached as objects with a single cache key because all parameters will be ignored:
    
    _http://cdn.example.com/photo.jpeg?id=6&color=blue_  
    _http://cdn.example.com/photo.jpeg?id=1&color=blue_
    

*   **Ignore All Except**. Files with the specified query parameters are cached as objects with different keys; files with other parameters are cached as objects with the same key.
    
    In the **Parameter** field, enter each parameter on a separate line.
    
    <img src="https://support.gcore.com/hc/article_attachments/12415729590801" alt="Ignore_All_Except.png" width="523" height="269">
    
    For example, you specified _id_ in the Parameter field. The following files will be cached as objects with different keys because the values of the _id_ parameter are different, and the value of the _color_ parameter will be ignored.
    
    _http://cdn.example.com/photo.jpeg?id=6&color=blue_  
    _http://cdn.example.com/photo.jpeg?id=1&color=blue_
    
    For example, you specified _color_ in the Parameter field. The following files will be cached as objects with the same keys because the values of the _color_ parameter are the same, and the _id_ parameter will be ignored.
    
    _http://cdn.example.com/photo.jpeg?id=6&color=blue_  
    _http://cdn.example.com/photo.jpeg?id=1&color=blue_
    

*   **Ignore only**. Files with the specified query parameters are cached as objects with the same key, files with other parameters are cached as objects with different keys.
    
    In the **Parameter** field, enter each parameter on a separate line.
    
    <img src="https://support.gcore.com/hc/article_attachments/12415745809041" alt="Ignore_Only.png" width="524" height="270">
    
    For example, you specified _id_ in the Parameter field. The following files will be cached as objects with the same keys because the values of the _id_ parameter will be ignored, and the values of the _color_ parameters are the same.
    
    _http://cdn.example.com/photo.jpeg?id=6&color=blue_  
    _http://cdn.example.com/photo.jpeg?id=1&color=blue_
    
    For example, you specified _color_ in the Parameter field. The following files will be cached as objects with different keys because the values of the _color_ parameter will be ignored, and the values of the _id_ parameters are different.
    
    _http://cdn.example.com/photo.jpeg?id=6&color=blue_  
    _http://cdn.example.com/photo.jpeg?id=1&color=blue_

## Set-Cookie setting

A CDN defines a file with the Set-Cookies header as a unique one. As a result, each user’s request goes to the origin. This option defines whether we will cache files with the Set-Cookies header as one file or as different ones. In most cases, it is not effective to have copies of the same file with different cookies on the server.

Enable Ignore Set-Cookie option and files with cookies will be cached like one object. Go to CDN Resources, choose a CDN Resource and press Settings, open Advanced Settings and check Ignore Set-Cookies.

<img src="https://support.gcore.com/hc/article_attachments/115011406629/Screenshot-2018-1-1_G-Core_Labs___________CDN-___________________8_.png" alt="Screenshot-2018-1-1_G-Core_Labs___________CDN-___________________8_.png">