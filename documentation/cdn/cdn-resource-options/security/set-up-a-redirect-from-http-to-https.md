---
title: set-up-a-redirect-from-http-to-https
displayName: Redirect from HTTP to HTTPS
published: true
order: 20
toc:
---
# Set up a redirect from HTTP to HTTPS

**Note**: only one redirect option can be enabled on a CDN Resource. 

You can redirect HTTP traffic to HTTPS via API (more info in the <a href="https://apidocs.gcore.com/cdn#tag/SSL-Certificates" target="_blank">API documentation</a>) or in the control panel. 

To enable the redirect option in the control panel, go to the CDN Resources settings: 

1\. Get a free Let’s Encrypt certificate or add your SSL certificate in the General -> SSL section and save changes. More info in the guide "<a href="https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">Add an SSL certificate to deliver content over HTTPS</a>".

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/set-up-a-redirect-from-http-to-https/mceclip0.png" alt="" width="80%">

2\. Go to the "Access" section, enable the "Redirect HTTP to HTTPS" option and save changes.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/set-up-a-redirect-from-http-to-https/mceclip1.png" alt="" width="80%">

The error "*You cannot enable redirect HTTP to HTTPS when HTTPS is disabled. Please enable HTTPS and add SSL certificate first*" means that you didn't add a certificate or that the issuing of a Let’s Encrypt certificate for your account wasn’t completed. As usual it takes about 15 minutes.