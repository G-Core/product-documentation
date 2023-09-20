---
title: add-an-ssl-certificate-to-your-resource
displayName: Add an SSL certificate
published: true
order: 50
toc:
   --1--Add SSL certificate: "add-ssl-certificate-to-your-resource"
   --2--None: "none-choose-protection-with-no-certificate"
   --2--Let's Encrypt: "add-lets-encrypt-certificate"
   --2--Custom: "add-custom-certificate-to-your-resource"
pageTitle: SSL Certificate For Your Protected Resource | Gcore
pageDescription: How to add an SSL certificate for a protected resource.
---
# Add an SSL certificate to your resource

## Add SSL сertificate to your resource

To add an SSL certificate to your domain or subdomains go to the resource Settings and click **Edit** in "SSL Certificate" section.

<img src="https://assets.gcore.pro/docs/web-security/add-an-ssl-certificate-to-your-resource/mceclip0.png" alt="Add SSL сertificate to your resource" width="80%">

You can add Let's Encrypt or Custom certificate, or refuse adding a certificate (None).

### None (choose protection with no certificate)

There is no SSL certificate, the content is delivered via HTTP.

### Add Let's Encrypt certificate

It is a paid option, to activate it, please, contact the [support team](mailto:support@gcore.com). 

If you choose this option we will request an SSL certificate for your domain name and will be regularly renewing it automatically. To obtain the certificate we have to show to the certificate authority that our server controls your domain. One of the ways to do that is an A-record. So for us to have a certificate issued for your domain you have to change an A-record in your DNS settings and point your domain name to the protected IP address. Keep in mind that once the A-record has been changed it takes time for the DNS servers to renew their cache (depends on the TTL setting). If some old records are still circulating the certificate authority might not see that your domain name is pointed to our IP and deny the certificate issue. The disadvantage is that for the time spent on issuing the certificate the website would only be available via HTTP.

Once the SSL certificate is issued we will automatically renew it if you keep the Let's Encrypt option enabled in the Control Panel.

If you decide to stop using Let's Encrypt certificate and switch settings to None, we will stop renewing the certificate but the previously issued one will stay active until its expiration date.

**How to start using Let's Encrypt right away**. To avoid a period when your website will only be available via HTTP use these guideline:

1. Create a resource in the Control panel but don't change the A-record. Issue a Let's Encrypt certificate by yourself.
2. Add this certificate as a Custom one to the Contol panel.
3. Change the A-record in your DNS settings.
4. Wait untill the old DNS records will get removed (keep in mind the TTL value).
5. In the SSL settings change the value from Custom to Let's Encrypt and save the new settings.

Once you change the settings we will issue a new Let's Encrypt certificate for your resource and will regularly renew it.

### Add Custom certificate to your resource

1. Open a certificate file in PEM format in the Notepad app. Certificates of such format usually have .pem, .crt, or .cer extensions.  
2. Copy and paste the certificate chain in the following order: Personal certificate → Intermediate CA → Root CA.  Data in the Certificate field should be inserted, including the tags *- - - - - BEGIN CERTIFICATE - - - - and - - - - - END CERTIFICATE - - - -*. 
3. Certificate chains must be inserted together.  
      
<img src="https://assets.gcore.pro/docs/web-security/add-an-ssl-certificate-to-your-resource/mceclip1.png" alt="Certificate chains must be inserted together" width="80%">

4. There should be an empty string at the end of the certificate chain. 

<img src="https://assets.gcore.pro/docs/web-security/add-an-ssl-certificate-to-your-resource/mceclip2.png" alt="an empty string at the end of the certificate chain" width="80%"> 

5. Open a file with the private key (.key) in the Notepad app. 
6. Copy and paste the key, including the tags *- - - - - BEGIN PRIVATE KEY - - - - and - - - - - END PRIVATE KEY - - - - -*. 
7. Click **Create SSL certificate**. 
8. The certificate will appear in the SSL certificates section. If this certificate is added at the moment of resource creation, the certificate will also be bound to the resource.

Don't forget to update certificates of this type.