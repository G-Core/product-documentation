---
title: specify-an-origin-and-the-origin-pull-protocol
displayName: Specify an origin
published: true
order: 10
toc:
   --1--Origin Pull protocol: "origin-pull-protocol"
   --1--Pull content from: "pull-content-from"
pageTitle: Understanding CDN Origin Pull Protocol & Origins | Gcore
pageDescription: Learn to correctly set up your CDN Origin Pull Protocol and define origins to avoid redirects or delivery failures.
---
# Specify an origin and the origin pull protocol
  
## Origin Pull protocol 

Use the Origin Pull Protocol option to set the protocol which CDN servers will use to pull content from an origin server: HTTP, HTTPS or HTTP and HTTPS.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol/13339352573201.png" alt="Origin Pull protocol " width="50%">

Select the Origin pull protocol, depending on which protocol the origin server uses to send the content.  

1. **HTTP** - if the content on the origin server is available only via HTTP (port 80) or there is a redirect from HTTPS to HTTP on the origin server. 
2. **HTTPS** - if the content on the origin server is available only via HTTPS (port 443) or here is a redirect from HTTP to HTTPS on the origin server. 
3. **HTTP and HTTPS** - if the content on the origin server is available via both HTTPS and HTTP. It means that a CDN server will use the protocol depending on the client’s request:
    - Files are cached on a CDN server for both protocols. There will be two versions of the file in the cache: one for HTTP, and the other for HTTPS.
    - When the user sends a request to ```https://cdn.example.com/image.jpg```, a CDN server delivers content from the origin through HTTPS (443 port).
    - When the user sends a request to ```http://cdn.example.com/image.jpg```, a CDN server delivers content from the origin through HTTP (80 port).

To show the logic of the Origin Pull Protocol option and what will happen if an incorrect value is set, consider an example:

Your origin server only delivers content through HTTPS (port 443), but in the Origin Pull Protocol option HTTP protocol (80 port) is specified.

Depending on whether a redirection is configured on the origin server or not, the client will receive or not receive content.

1\. **Origin redirects from HTTP to HTTPS**

1.  A user requests content from a CDN at http://cdn.example.com/image.jpg.
2.  The CDN pulls from an origin source at **http**://example.com/image.jpg.
3.  The origin redirects to **https**://example.com/image.jpg.

Conclusion: the user gets the content from the origin, not from the CDN. Choose the HTTPS value to have your content delivered through a CDN. 

2\. **Origin does not redirect from HTTP to HTTPS** 

1.  A user requests content from a CDN at http://cdn.example.com/image.jpg.
2.  The CDN pulls from an origin source at **http**://example.com/image.jpg.

Conclusion: the origin cannot provide any content because it can take content only at **https**://example.com/image.jpg. Choose the HTTPS value to have your content delivered through a CDN. 

## Pull Content from 

Here you can specify an origin that CDN uses to pull the content from. 

The origin can be the IP address or your site domain. 

If you want to change the current origin, click **Edit the group**.

You can also add an origin group by clicking **Add group**.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol/13339453926417.png" alt="Add group" width="50%">

**Note**: When you add an origin group from the resource settings, it is not automatically assigned to the resource. It should be manually selected from the list.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol/13339542285201.png" alt="manually selected from the list" width="50%">

Read more about <a href="https://gcore.com/docs/cdn/add-an-origin-group" target="_blank">how to edit and add origin groups</a>.