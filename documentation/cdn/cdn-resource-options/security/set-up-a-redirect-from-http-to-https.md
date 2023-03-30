---
title: set-up-a-redirect-from-http-to-https
displayName: Redirect from HTTP to HTTPS
published: true
order: 20
toc:
---
Note: only one redirect option can be enabled on a CDN Resource. 

You can redirect HTTP traffic to HTTPS via API (more info in the [API documentation](https://apidocs.gcore.com/cdn#tag/SSL-Certificates)) or in the control panel. 

To enable the redirect option in the control panel, go to the CDN Resources settings: 

1\. Get a free Let’s Encrypt certificate or add your SSL certificate in the General -> SSL section and save changes. More info in the guide “[Add a SSL certificate to transfer content over HTTPS](https://www.gcore.com/support/articles/213970109/)”.

<img src="https://support.gcore.com/hc/article_attachments/8007486637841/mceclip0.png" alt="mceclip0.png">

2\. Go to the Access -> Redirect HTTP to HTTPS section, enable the option and save changes.

<img src="https://support.gcore.com/hc/article_attachments/8007508254097/mceclip1.png" alt="mceclip1.png">

The error “_You cannot enable redirect HTTP to HTTPS when HTTPS is disabled. Please enable HTTPS and add SSL certificate first_” means that you didn't add a certificate or that the issuing of a Let’s Encrypt certificate for your account wasn’t completed. As usual it takes about 15 minutes.