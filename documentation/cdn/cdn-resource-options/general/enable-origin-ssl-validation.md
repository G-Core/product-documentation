---
title: enable-origin-ssl-validation
displayName: Enable SSL Validation
published: true
order: 20
toc:
   --1--What is it for: "what-is-this-option-for"
   --1--How does it work: "how-does-it-work"
   --1--Enable via API: "enable-ssl-validation-via-api"
---
 

## What is this option for?

Note: This option is only accessible via [API](https://apidocs.gcore.com/iam).  

In the Origin Pull Protocol option, you are to set the protocol which CDN servers will use to pull content from an origin server: HTTP, HTTPS or HTTP and HTTPS. It allows you to control whether the connection between the CDN and the origin server is encrypted or not. 

If you choose the HTTPS protocol, CDN servers will send a request for the content via HTTPS protocol, such a content transfer process is encrypted, but still do not save the connection from the attack called [Man In The Middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). 

This is because the CDN servers by default do not check whether the SSL certificate on the origin is valid and certified by a Certificate Authority and whether the answered server is the client's server.  

To increase the connection security level, activate the Origin SSL Validation option.  

With the active origin validation option, the CDN server will ensure the validity of your origin certificate before completing any connection. This includes ensuring the identity of your server with your signing CA. 

## How does it work?


1\. You set the part of the public key of the X.509 certificate in the system (using an API request) in the PEM format. The other part of the key you will store on your origin server. The certificates you added will receive a unique ID. We will store all the certificate information on CDN servers. At any moment, you can get a request for the certificate information or change their names.  

2\. When a user sends a request for the content for the first time, a CDN server sends a request to access protected information on the origin server. 

3\. The origin server presents its X.509 certificate to the CDN server. 

4\. The CDN server verifies the origin server’s certificate by validating the digital signature of the server’s public key using CA’s public key stored in the CDN system. 

5\. If the last step is successful, the CDN server sends its certificate to the origin server. 

6\. The origin server verifies the CDN server's certificate using the same approach.  

7\. If successful, the origin server gives access to the protected information to the CDN server. 

8\. CDN server sends the content to the user browser.

## Enable SSL validation via API

1\. Upload the certificate using the "<a href="https://apidocs.gcore.com/cdn#tag/CA-certificates/operation/ca_certitifactes-add" target="_blank">Add Trusted CA Certificate</a>" documentation.

2\. Link the certificate to the CDN resource using the *proxy_ssl_ca* and *proxy_ssl_data* keys according to the "<a href="https://apidocs.gcore.com/cdn#tag/Resources/operation/change_cdn_resource" target="_blank">Change CDN Resource</a>" documentation.

3\. Set the *proxy_ssl_enabled* key to the true value for your resource according to the "<a href="https://apidocs.gcore.com/cdn#tag/Resources/operation/change_cdn_resource" target="_blank">Change CDN Resource</a>" documentation.