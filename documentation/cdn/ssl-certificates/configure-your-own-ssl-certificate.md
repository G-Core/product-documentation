---
title: configure-your-own-ssl-certificate
displayName: Own SSL certificate
published: true
order: 20
toc:
   --1--Upload a certificate: "how-to-upload-an-ssl-certificate-to-your-account"
   --2--Insert data correctly: "how-to-insert-an-ssl-chain-and-a-key-correctly"
   --1--Attach: "how-to-attach-the-ssl-certificate-to-the-cdn-resource"
   --2--During resource creation: "method-1-add-ssl-certificate-during-cdn-resource-creation"
   --2--For an existing resource: "method-2-add-ssl-certificate-for-an-existing-cdn-resource"
   --1--SSL management: "certificate-management"
   --2--Overview: "ssl-certificates-overview"
   --2--Renewal: "renew-an-ssl-certificate"
   --2--Notifications: "ssl-certificate-expiration-notifications"
   --2--Deletion: "delete-an-ssl-certificate"
pageTitle: Adding Your Own SSL Certificates | Gcore
pageDescription: Learn how to add and attach your certificate to the CDN resource.
---
# Configure your own SSL certificate

**Note**: Your SSL certificate should be issued for the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain of your CDN resource</a>, e.g., *cdn.example.com*. You can use a wildcard certificate, which allows you to protect all subdomains (_*.example.com_).

## How to upload an SSL certificate to your account

1\. Go to <a href="https://cdn.gcore.com/ssl/" target="_blank">SSL certificates</a> and click **Add SSL certificate**. 

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-1.png" alt="SSL certificates">

A new page will open.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/ssl-certificate-data.png" alt="new page will open" width="70%">

2\. Enter the following details of the certificate that you purchased from the Certificate Authority:

- The SSL certificate name, which can be found in the control panel 
- Certificate chain (personal certificate, intermediate CA, root CA) in the <a href="https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail" target="_blank">PEM format</a> 
- Private key

For help inserting the certificate chain and key contents, <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-insert-an-ssl-chain-and-a-key-correctly" target="_blank">explore our guide</a>.

3\. Uncheck the box if the certificate is not signed by the trusted CA.

4\. Click **Create SSL Certificate**.

That’s it. The certificate will be added to the list of certificates in the <a href="https://cdn.gcore.com/ssl/" target="_blank">SSL Certificates</a> section. 

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-3.png" alt="Create SSL Certificate">

**Note**: Attach the entry to the related CDN resource after uploading your SSL certificate data. 

### How to insert an SSL chain and a key correctly

1\. Open the certificate file in PEM format (.pem, .crt, or .cer) using a text editor like Notepad.

2\. Copy and paste the certificate chain in this order: personal certificate, intermediate CA, root CA.

3\. All the contents of the certificate must be inserted into the **Certificate** field, including the tags ```-----BEGIN CERTIFICATE-----``` and ```-----END CERTIFICATE-----```.

4\. The certificate chain must be inserted without blank lines. Here's an example of how it should look:

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-4.png" alt="certificate chain" width="80%">

5\. Add a new line at the end of the certificate chain.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-5.png" alt="new line at the end of the certificate chain" width="80%">

6\. Open the private key file (.key) using a text editor.

7\. Copy and paste all of its contents into the **Private key** field, including the tags ```-----BEGIN RSA PRIVATE KEY-----``` and ```-----END RSA PRIVATE KEY-----```.

## How to attach the SSL certificate to the CDN resource

You can attach the SSL certificate to your CDN resource either:

- During CDN resource creation
- To an existing CDN resource

### Method 1: Add SSL certificate during CDN resource creation

1\. Follow steps 1–3 of the guide <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Create a CDN resource for static assets only</a> until the “Custom domain” field is filled in.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-6.png" alt="Create a CDN resource" width="80%">

2\. In the **Custom domain** section, enter your desired custom domain name—e.g., *cdn.example.com*—for your CDN resource.

3\. In the **SSL** section, turn on the toggle for **Enable HTTPS** and select **Add or select your own SSL certificate**.

4\. If you’ve already <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-upload-an-ssl-certificate-to-your-account" target="_blank">uploaded the SSL certificate to your account</a>, select the certificate from the list and continue the CDN resource creation.

5\. Continue with the creation of your CDN resource.


<expandable-element title="If you haven’t uploaded the SSL certificate">

If you haven’t yet added a certificate or want to upload a new one for this resource, click **Add SSL certificate**. Specify your SSL certificate’s data in the pop-up window. <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-insert-an-ssl-chain-and-a-key-correctly" target="_blank">Review our guide</a> for help inserting the certificate and key contents. After pasting the data, сlick **Add SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/ssl-cert-adding.png" alt=" Add SSL certificate" width="70%">

</expandable-element>

### Method 2: Add SSL certificate for an existing CDN resource

1\. Select the resource you want to configure in the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> section.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-8.png" alt="CDN resources section">

2\. In the navigation panel, under the General section, click **SSL** and enable the **Enable HTTPS** switch.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-9.png" alt="General section">

3\. Select **Add or select your own SSL certificate**. If you’ve already <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-upload-an-ssl-certificate-to-your-account" target="_blank">uploaded the SSL certificate to your account</a>, select the certificate from the list and save changes.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-10.png" alt="Add or select your own SSL certificate" width="80%">


<expandable-element title="If you haven’t uploaded the SSL certificate">

If you haven’t yet added a certificate or want to upload a new one for this resource, click **Add SSL certificate**. Specify your SSL certificate’s data in the pop-up window. <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-insert-an-ssl-chain-and-a-key-correctly" target="_blank">Review our guide</a> for help inserting the certificate and key contents. After pasting the data, сlick **Add SSL certificate**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/ssl-cert-adding.png" alt="SSL certificates overview" width="70%">

</expandable-element>

## Certificate management

### SSL certificates overview

The certificate will be displayed in the <a href="https://cdn.gcore.com/ssl/list" target="_blank">SSL certificates</a> section of your control panel. This page contains a table that lists your personal certificates and associated information, such as the ID, name, CDN resources connected to the certificate, and expiration date.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-11.png" alt="Renew an SSL certificate">

### Renew an SSL certificate

There is no way to change a certificate's data once the certificate has been added. When the certificate is nearing its expiration date, follow these steps:

1\. Go to the <a href="https://cdn.gcore.com/ssl/list" target="_blank">SSL Certificates</a> page and <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#how-to-upload-an-ssl-certificate-to-your-account" target="_blank">upload a new certificate</a>.

2\. Go to the settings of the CDN resource you want to configure.

3\. Select the new certificate from the dropdown menu in the SSL section.

4\. Click **Save changes** and allow at least fifteen minutes for the changes to take effect.

5\. To verify that the SSL certificate has been correctly installed and bound to the resource, enter your CNAME into the browser (e.g., ```https://example.com```). Click the lock icon in the address bar, navigate to **Connection is secure**, and click **Certificate is valid**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-12.png" alt="verify that the SSL certificate">

Compare the displayed certificate data with the new certificate data you just added. If the settings match, you can safely <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#delete-an-ssl-certificate" target="_blank">delete the old certificate</a> from the SSL certificates page.

**Note**: Delete the old certificate only after ensuring your content is delivered using the new certificate. If you delete the old certificate too soon, content delivery will be interrupted.

### SSL certificate expiration notifications

When your added certificates are about to expire, a notification is displayed in your account and is sent to the email addresses of the administrator and engineer.
Users are notified by email:

- Fourteen days before the certificate expires
- Seven days before the certificate expires
- On the day of the certificate’s expiration

In addition, when you log in to your account during the fourteen days before certificate expiration or any time after that, you will see a reminder. The <a href="https://cdn.gcore.com/ssl/list" target="_blank">SSL certificates</a> in the side panel will also be marked with an exclamation point if there are expired certificates or certificates that will expire within the next fourteen days.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-13.png" alt="SSL certificates">

In the certificates table, warning signs will appear next to the specific certificates that need attention.

If the certificate has already expired, a red exclamation point will be shown.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-14.png" alt="certificate has already expired">

If the certificate is due to expire in fourteen days or fewer, a yellow warning triangle will be shown.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-15.png" alt="certificate is due to expire">

### Delete an SSL certificate

To delete a certificate, click the three dots next to the certificate, then click **Delete**.

<img src="https://assets.gcore.pro/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate/own-ssl-16.png" alt="Delete an SSL certificate">

**Note**: It is not possible to delete certificates that are currently in use by a CDN resource. If you want to delete such a certificate, you must first unattach it. To do so, open the SSL section in the CDN resource settings and turn off the **Enable HTTPS option**.
