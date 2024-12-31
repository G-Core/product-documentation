---
title: specify-tls-versions-allowed-for-content-requests-from-the-cdn
displayName: Specify allowed TLS versions
published: true
order: 60
toc:
pageTitle: Understanding TLS versions Allowed for CDN Requests | Gcore
pageDescription: A guide on how to specify TLS versions allowed for content requests from CDN.
---
# Specify TLS versions allowed for content requests from the CDN

The option specifies a list of allowed SSL/TLS protocol versions. The list cannot be empty.
By default, the option is disabled, and all the protocol versions are allowed.
Possible values (case sensitive):

* SSLv3
* TLSv1
* TLSv1.1
* TLSv1.2
* TLSv1.3

To manage TLS versions option:

1\. In the Gcore Customer Portal, navigate to **CDN**. You'll be directed to the **CDN resources** page.

2\. Find the needed resource and click on its CNAME to open the settings.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/specify-http-methods-allowed-for-content-requests-from-the-cdn/cdn-resources-cname.png" alt="CDN resources page with a resource CNAME highlighted" width="80%">

3\. Scroll down to the **TLS versions** section and click the **Change TLS versions** toggle to specify the necessary versions. The other versions you haven't specified will be blocked. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/choose-tls-versions/screenshot-1.png" alt="TLS versions in resource settings" width="80%">
