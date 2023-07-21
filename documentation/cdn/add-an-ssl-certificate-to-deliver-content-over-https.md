---
title: add-an-ssl-certificate-to-deliver-content-over-https
displayName: SSL certificates
published: true
order: 70
toc:
   --1--What is an SSL certificate?: "what-is-an-ssl-certificate"
   --1--1. Your own SSL certificate: "1-your-own-ssl-certificate"
   --2--Add during resource creation: "add-an-ssl-certificate-during-resource-creation"
   --2--Add on the SSL certificates page: "add-an-ssl-certificate-on-the-ssl-certificates-page"
   --2--How to insert data correctly: "how-to-insert-an-ssl-certificate-and-a-key-correctly"
   --2--Attach to a CDN resource: "attach-an-ssl-certificate-to-a-resource"
   --2--Renew: "renew-an-ssl-certificate"
   --2--Expiration notifications: "ssl-certificates-expiration-notifications"
   --2--Delete: "delete-an-ssl-certificate"
   --1--2. Let's Encrypt certificate: "2-lets-encrypt-certificate"
   --2--Activate: "activate-a-lets-encrypt-certificate"
   --2--Revoke: "revoke-a-lets-encrypt-certificate"
   --2--Restrictions and features of the option: "restrictions-and-features-of-the-option"
pageTitle: Adding, Renewing, and Deleting of SSL Certificates | Gcore
pageDescription: Learn how to add your certificate or get a free Let's Encrypt certificate, renew, and delete SSL certificates.
---
# Add an SSL certificate to deliver content over HTTPS

## What is an SSL certificate?

An SSL certificate is a unique digital signature for your website that provides a secure connection between a client and a server. It is essential when sensitive information is being transferred, and financial transactions are being carried out.

In Gcore, two types of SSL certificates are available:

**1. Your own SSL certificate.** You can re-issue a certificate for your domain from a third-party company and add its data to the control panel. 

**2. Free Let's Encrypt certificate.** You can issue a free Let's Encrypt certificate for your custom domain. All data will be added automatically. 

## 1\. Your own SSL certificate

There are 2 ways to add a certificate: during [resource creation](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#add-an-ssl-certificate-during-resource-creation) and on the [SSL Certificates page](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#add-an-ssl-certificate-on-the-ssl-certificates-page) of your account.

### Add an SSL certificate during resource creation

To add and bind a personal certificate during <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">CDN resource creation</a>:

1\. In the **Custom domain** section enter your desired domain name.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12865716431377.png" alt="" width="50%">

2\. In the **SSL** section, turn on the toggle for **Enable HTTPS** and select **Add or select your own SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12452694059025.png" alt="" width="50%">

3\. Click **Add SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12452850452369.png" alt="" width="50%">

4\. In the pop-up window, enter a certificate name, the certificate in PEM format, and the private key.

For help inserting the certificate and key contents, read [How to insert an SSL certificate and a key correctly](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#how-to-insert-an-ssl-certificate-and-a-key-correctly).

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12453011844113.png" alt="" width="80%">

5\. Click **Add SSL certificate**.

The certificate will be bound to the resource and added to the list of certificates in the SSL Certificates page.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12454318012305.png" alt="" width="80%">

### Add an SSL certificate on the SSL certificates page

To add a personal certificate without binding to a resource:

1\. Click **SSL certificates** in the side panel of the CDN service and click **Add SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12453744428945.png" alt="" width="80%">

2\. In the form that appears, enter a certificate name, the SSL certificate in PEM format, and the private key.

For help inserting the certificate and key contents, read [How to insert an SSL certificate and a key correctly](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#how-to-insert-an-ssl-certificate-and-a-key-correctly).

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12453950369937.png" alt="" width="80%">

3\. Click **Create SSL Certificate**.

The certificate will be displayed in the list of certificates in the SSL Certificates page. The SSL Certificates page contains a table that lists your personal certificates and associated information such as the ID, name, CDN resources connected to the certificate, and expiration date.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12454558136465.png" alt="" width="80%">

### How to insert an SSL certificate and a key correctly

1\. Open the certificate file in PEM format (.pem, .crt, or .cer) using a text editor like Notepad.

2\. Copy and paste the certificate chain in this order: Personal certificate, Intermediate CA, Root CA.

3\. All the contents of the certificate must be inserted into the **Certificate** field, including the tags ```-----BEGIN CERTIFICATE-----``` and ```-----END CERTIFICATE-----```.

4\. The certificate chain must be inserted together, similar to the following:

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12474188463505.png" alt="" width="50%">

5\. Make sure to add a new line at the end of the certificate chain.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12474236901009.png" alt="" width="50%">

6\. Open the private key file (.key) using a text editor.

7\. Copy and paste all of its contents into the **Private key** field, including the tags ```-----BEGIN RSA PRIVATE KEY-----``` and ```-----END RSA PRIVATE KEY-----```.

8\. Click **Create SSL certificate**.

The certificate will appear in the SSL Certificates page. If it is added during the resource creation process, the certificate will also be bound to the resource.

### Attach an SSL certificate to a resource

A certificate added to the SSL Certificates page can be attached to a CDN resource while <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">creating</a> or editing it. To edit an existing resource:

1\. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12472174727185.png" alt="">

2\. In the navigation panel, under the **General** section, click **SSL**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12472264886801.png" alt="" width="80%">

3\. In the **SSL** section, turn on the toggle for **Enable HTTPS**, and select **Add or select your own SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12472444490513.png" alt="" width="50%">

4\. Click the **Select the certificate** dropdown and select the certificate that you want to use.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12472462558609.png" alt="" width="50%">

5\. Click **Save changes**.

**Important**: If a Let's Encrypt certificate is enabled for a resource, the certificate selector will not be displayed. To select a personal certificate, you must first [revoke](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#revoke-a-lets-encrypt-certificate) the Let's Encrypt certificate.

### Renew an SSL certificate

There is no way to change the data of an added certificate, so when the certificate is nearing its expiration date, follow these steps:

1\. Go to the **SSL Certificates** page and [add a new certificate](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#add-an-ssl-certificate-on-the-ssl-certificates-page).

2\. Go to the settings of the CDN resource you want to configure.

3\. In the **SSL** section, select the new certificate from the dropdown menu.

4\. Click **Save changes** and allow at least 15 minutes for the changes to take effect.

5\. To verify that the SSL certificate has been correctly installed and bound to the resource, enter your CNAME into the browser (e.g., https://example.ru). Click the lock icon in the address bar, navigate to **Connection is secure**, and click **Certificate is valid**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12505093148305.png" alt="" width="50%">

Compare the displayed certificate data with the certificate data you just installed. If the settings are match, you can safely [delete](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#delete-an-ssl-certificate) the old certificate from the SSL Certificates page.

**Note**: Delete the old certificate only after making sure that your content is being delivered using the new certificate. If you delete the old certificate too soon, content delivery will be interrupted.

### SSL certificates expiration notifications

When your added certificates are about to expire, a notification is displayed in your account, and is sent to the email addresses of the Administrator and Engineer.

Users are notified by email:

- 14 days before the certificate expires
- 7 days before the certificate expires
- On the day of the certificate's expiration

When you log in to your account, you will see a reminder about the expiration of the certificate.

The **SSL certificates** in the side panel will also be marked with an exclamation point if there are already expired certificates or those that will expire within the next 14 days:

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12502925405713.png" alt="">

In the certificates table, warning signs will also appear next to the certificates that need attention.

* If the certificate has already expired:  
      
<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12474790392849.png" alt="" width="50%">

* If the certificate is due to expire in 14 days or less:  
      
<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12474878887441.png" alt="" width="50%">

**Note**: Certificates issued by Let's Encrypt are automatically renewed, so there are no expiration notifications for such certificates.

### Delete an SSL certificate

To delete a certificate, click the three dots icon next to the certificate, then click **Delete**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12472136184849.png" alt="" width="80%"> 

**Note**: It is not possible to delete certificates that are in use by CDN resources. If you want to delete the certificate, you must first [replace it with another certificate](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#renew-an-ssl-certificate) in the CDN Resource Settings.

## 2\. Let's Encrypt certificate

If you do not have your own SSL certificate, you can activate the free Let's Encrypt certificate in your account.

### Activate a Let's Encrypt certificate

1\. Use a <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain name</a> for your resource.

2\. In the **SSL** section, turn on the toggle for **Enable HTTPS**, and select **Get free Let's Encrypt certificate**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12476211101713.png" alt="" width="50%">

The certificate issuance may take up to 30 minutes. During this time, please do not:

- disable the HTTPS option,
- select another certificate,
- interrupt the issuance of the current certificate.

**Important:**

* The time it takes to issue a certificate varies depending on when the CDN resource was created. If you are requesting a certificate for a recently created resource, it may take up to 30 minutes as the configuration has not yet been fully propagated to all CDN servers. However, if the resource's configuration has already been fully propagated, issuing a Let's Encrypt certificate will only take a few minutes.

* Let's Encrypt requires placing a temporary file at the URL ```http://<CNAME>/.well-known/acme-challenge/<TOKEN>``` and making HTTP requests to this file. Before adding a Let's Encrypt certificate, make sure that your CDN resource does not have any rules that block these requests. Examples of such rules include:
  - **A rule with /\***. This rule will catch any strings and override the hidden rule that is necessary to obtain a certificate.
  - **A rule with ((?!(jpeg|gif|png|pdf|jpg|css|js|woff|woff2|ttf)).)\*$**. This rule will catch all non-static files.
    
You can check your resource rules using the service <a href="https://regex101.com/r/6BCT9Z/1" target="_blank">regex</a>. If you find a rule that blocks Let's Encrypt certificate issuance, delete the rule or change its pattern. The next time Let's Encrypt sends a request, the certificate issuance should be successful.
    
If an error occurs during certificate issuance, the Enable HTTPS toggle will be disabled and a notification will be sent to your email.
    

- You can only issue a Let's Encrypt certificate for an existing resource. If the CNAME of the resource in the DNS settings is not pointing to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">value specified in the setup guide</a>, or the source is not available, the certificate will not be issued.

- Only one Let's Encrypt certificate can be issued per resource. If you need to add or remove an additional personal domain for a resource, we will reissue the certificate after making the changes. You will receive a warning that the current certificate will only be valid for 30 minutes and will be automatically replaced.  
    
<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12476294660369.png" alt="" width="50%">
    
While the resource is active, the certificate is renewed automatically. An attempt to reissue the certificate will be made 30 days before the expiration of the current certificate. There is only one attempt to reissue the certificate. If the certificate is not reissued, a notification will be sent to your email.
    
In the event of an unsuccessful attempt to reissue a certificate, the current certificate will remain active for another 30 days. After the certificate's end date, the content will become unavailable via HTTPS.
    
To avoid interruption of content delivery, please reissue the certificate yourself. To do this, [revoke](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#revoke-a-lets-encrypt-certificate) the Let's Encrypt certificate in your account and then .
    

### Revoke a Let's Encrypt certificate

To revoke a certificate, go to the Resource Settings and click **Revoke Let's Encrypt certificate** in the SSL section.

<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12476569572241.png" alt="" width="50%">

**Note**: You can also use an <a href="https://api.gcore.com/docs/cdn#tag/SSL-Certificates" target="_blank">API request</a> to replace the Let's Encrypt certificate with your own certificate without having to revoke it.

### Restrictions and features of the option

- A wildcard domain cannot be issued a certificate.
- If a Let's Encrypt certificate is issued, the certificate selector will not be displayed in the resource settings. Personal certificates will become available for selection after [revoking](https://gcore.com/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https#revoke-a-lets-encrypt-certificate) Let's Encrypt.
- A Let's Encrypt certificate will not be displayed on the SSL Certificates page.  
    
<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12476717472145.png" alt="" width="80%">
    
- A certificate is **only** visible in the settings of the resource for which it is issued.
- Issuing and revoking a Let's Encrypt certificate does not require saving the Resource Settings.
- If you are using DNS Cloudflare, be sure not to set the **CNAME Flattering** option to Flatten all CNAMEs. This will cause Cloudflare to return an A-record instead of a CNAME, which will prevent the issuance of a Let's Encrypt certificate. To successfully issue a Let's Encrypt certificate, set the CNAME Flattering option to **Flatten CNAME at root.**  
    
<img src="https://assets.gcore.pro/docs/cdn/add-an-ssl-certificate-to-deliver-content-over-https/12503873872017.png" alt="" width="80%">