---
title: configure-lets-encypt-certificate
displayName: Let's Encrypt certificate
published: true
order: 30
toc:
   --1--Attach: "attach-a-lets-encrypt-certificate"
   --2--Duration resource creation: "during-resource-creation"
   --2--For created resource: "for-created-resource"
   --2--Notes: "notes-regarding-issuing"
   --1--Revoke: "revoke-a-lets-encrypt-certificate"
   --1--Restrictions: "restrictions-and-features-of-the-option"
pageTitle: Adding Let's Encrypt Certificates | Gcore
pageDescription: Learn how to issue Let's Encrypt certificate to the CDN resource.
---
# Configure Let's Encrypt certificate

If you do not have your own SSL certificate, you can activate the free Let's Encrypt certificate in your account. Let's Encrypt certificates can only be issued for resources with a <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain name</a>.

## Attach a Let's Encrypt certificate

### During resource creation

On the **Set up initial configuration** step, navigate to the **SSL** section, and turn on the toggle for **Enable HTTPS**. Then, select **Get free Let's Encrypt certificate**. 

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-1.png" alt="During resource creation" width="70%">

The certificate issuance may take up to 30 minutes after the resource is created. During this time, please do not:

- disable the HTTPS option,
- select another certificate,
- interrupt the issuance of the current certificate.

### For created resource

1\. Go to CDN and select the **CDN** resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-2.png" alt="CDN resource" width="80%">

2\. In the navigation panel, under the **General** section, click **SSL**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-3.png" alt="General section" width="80%">

3\. In the **SSL** section, turn on the toggle for **Enable HTTPS**, select **Get free Let's Encrypt certificate**, and click on **Save changes**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-4.png" alt="SSL section" width="80%">

### Notes regarding issuing

- The time it takes to issue a certificate varies depending on when the CDN resource was created. If you are requesting a certificate for a recently created resource, it may take up to 30 minutes as the configuration has not yet been fully propagated to all CDN servers. However, if the resource's configuration has already been fully propagated, issuing a Let's Encrypt certificate will only take a few minutes.
- Let's Encrypt requires placing a temporary file at the URL ```http://<CNAME>/.well-known/acme-challenge/<TOKEN>``` and making HTTP requests to this file. Before adding a Let's Encrypt certificate, make sure that your CDN resource does not have any rules that block these requests. Examples of such rules include:
    - __A rule with /*__. This rule will catch any strings and override the hidden rule that is necessary to obtain a certificate.
    - __A rule with ((?!(jpeg|gif|png|pdf|jpg|css|js|woff|woff2|ttf)).)*$__. This rule will catch all non-static files.

You can check your resource rules using the service <a href="https://regex101.com/r/6BCT9Z/1" target="_blank">regex</a>. If you find a rule that blocks Let's Encrypt certificate issuance, delete the rule or change its pattern. The next time Let's Encrypt sends a request, the certificate issuance should be successful.

If an error occurs during certificate issuance, the Enable HTTPS toggle will be disabled and a notification will be sent to your email.

- You can only issue a Let's Encrypt certificate for an existing resource. If the CNAME of the resource in the DNS settings is not pointing to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">value specified in the setup guide</a>, or the source is not available, the certificate will not be issued.
- Only one Let's Encrypt certificate can be issued per resource. If you need to add or remove an additional personal domain for a resource, we will reissue the certificate after making the changes. You will receive a warning that the current certificate will only be valid for 30 minutes and will be automatically replaced.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-5.jpg" alt="Warning">

While the resource is active, the certificate is renewed automatically. An attempt to reissue the certificate will be made 30 days before the expiration of the current certificate. There is only one attempt to reissue the certificate. If the certificate is not reissued, a notification will be sent to your email.

In the event of an unsuccessful attempt to reissue a certificate, the current certificate will remain active for another 30 days. After the certificate's end date, the content will become unavailable via HTTPS.

To avoid interruption of content delivery, please reissue the certificate yourself. To do this, <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-lets-encrypt-certificate#revoke-a-lets-encrypt-certificate" target="_blank">revoke</a> the Let's Encrypt certificate in your account and then .

## Revoke a Let's Encrypt certificate

To revoke a certificate, go to the Resource Settings and click **Revoke Let's Encrypt certificate** in the SSL section.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-6.png" alt="Revoke a Let's Encrypt certificate" width="70%">

**Note**: You can also use an <a href="https://api.gcore.com/docs/cdn#tag/SSL-Certificates" target="_blank">API request</a> to replace the Let's Encrypt certificate with your own certificate without having to revoke it.

## Restrictions and features of the option

- A wildcard domain cannot be issued a certificate
- If a Let's Encrypt certificate is issued, the certificate selector will not be displayed in the resource settings. Personal certificates will become available for selection after <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-lets-encrypt-certificate#revoke-a-lets-encrypt-certificate" target="_blank">revoking Let's Encrypt</a>
- A Let's Encrypt certificate will not be displayed on the SSL Certificates page

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-7.png" alt="Restrictions and features of the option" width="80%">

- A certificate is **only** visible in the settings of the resource for which it is issued.
- Issuing and revoking a Let's Encrypt certificate does not require saving the Resource Settings.
- If you are using DNS Cloudflare, be sure not to set the **CNAME Flattering** option to Flatten all CNAMEs. This will cause Cloudflare to return an A-record instead of a CNAME, which will prevent the issuance of a Let's Encrypt certificate. To successfully issue a Let's Encrypt certificate, set the CNAME Flattering option to **Flatten CNAME at root**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-lets-encypt-certificate/lets-encrypt-8.png" alt="Status" width="80%">