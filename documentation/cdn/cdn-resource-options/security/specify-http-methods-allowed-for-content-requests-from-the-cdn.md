---
title: specify-http-methods-allowed-for-content-requests-from-the-cdn
displayName: Specify HTTP methods
published: true
order: 40
toc:
pageTitle: Understanding HTTP Methods Allowed for CDN Requests | Gcore
pageDescription: A guide on how to specify HTTP methods allowed for content requests from CDN.
---
# Specify HTTP methods allowed for content requests from the CDN

You can choose HTTP methods for your CDN content. By default, the following methods are allowed: 

* GET
* HEAD
* POST
* PUT
* PATCH
* DELETE
* OPTIONS

To manage allowed HTTP method:

1\. In the Gcore Customer Portal, navigate to **CDN**. You'll be directed to the **CDN resources** page.

2\. Find the needed resource and click on its CNAME to open the settings.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/specify-http-methods-allowed-for-content-requests-from-the-cdn/cdn-resources-cname.png" alt="CDN resources page with a resource CNAME highlighted" width="80%">

3\. Scroll down to the **HTTP methods** section and click the **Enable HTTP methods** toggle to specify the necessary methods. The other methods you haven't specified will be blocked. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/specify-http-methods-allowed-for-content-requests-from-the-cdn/http-methods-section.png" alt="HTTP methods section in resource settings" width="80%">

The most used methods are GET, HEAD, and POST. Thus, we suggest allowing at least these ones. 

If some methods aren't allowed to the user, that user will get the **405 (Method Not Allowed)** response. If the method isn't supported by your server, the user will get the **501 (Not Implemented)** response.  
