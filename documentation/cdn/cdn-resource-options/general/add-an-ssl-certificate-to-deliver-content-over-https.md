---
title: add-an-ssl-certificate-to-deliver-content-over-https
displayName: SSL certificates
published: true
order: 40
toc:
   --1--What is an SSL certificate?: "what-is-an-ssl-certificate"
   --1--Your own SSL certificate: "your-own-ssl-certificate"
   --2--Add during resource creation: "add-an-ssl-certificate-during-resource-creation"
   --2--Add on the SSL certificates page: "add-an-ssl-certificate-on-the-ssl-certificates-page"
   --2--How to insert data correctly: "how-to-insert-an-ssl-certificate-and-a-key-correctly"
   --2--Attach to a CDN resource: "attach-an-ssl-certificate-to-a-resource"
   --2--Renew: "renew-an-ssl-certificate"
   --2--Expiration notifications: "ssl-certificates-expiration-notifications"
   --2--Delete: "delete-an-ssl-certificate"
   --1--Let's Encrypt certificate: "2-let-s-encrypt-certificate"
   --2--Activate: "activate-a-let-s-encrypt-certificate"
   --2--Revoke: "revoke-a-let-s-encrypt-certificate"
   --2--Restrictions and features of the option: "restrictions-and-features-of-the-option"
   --1--request a new one: ""
---


What is an SSL certificate?
---------------------------

An SSL certificate is a unique digital signature for your website that provides a secure connection between a client and a server. It is essential when sensitive information is being transferred, and financial transactions are being carried out.

In Gcore, two types of SSL certificates are available:

**1) Your own SSL certificate.** You can re-issue a certificate for your domain from a third-party company and add its data to the control panel. 

**2) Free Let's Encrypt certificate.** You can issue a free Let's Encrypt certificate for your custom domain. All data will be added automatically. 

Your own SSL certificate
------------------------

There are 2 ways to add a certificate: during [resource creation](#add-an-ssl-certificate-during-resource-creation) and on the [SSL Certificates page](#add-an-ssl-certificate-on-the-ssl-certificates-page) of your account.

### Add an SSL certificate during resource creation

To add and bind a personal certificate during [CDN resource creation](https://www.gcore.com/support/articles/213969429/):

1\. In the **Custom domain** section enter your desired domain name.

<img src="https://support.gcore.com/hc/article_attachments/12865716431377" alt="mceclip0.png" width="527" height="146">

2\. In the **SSL** section, turn on the toggle for **Enable HTTPS** and select **Add or select your own SSL certificate**.

<img src="https://support.gcore.com/hc/article_attachments/12452694059025" alt="Create_CDN_resource__SSL_section_.png" width="524" height="300">

3\. Click **Add SSL certificate**.

<img src="https://support.gcore.com/hc/article_attachments/12452850452369" alt="Add_Certificate_button.png" width="523" height="248">

4\. In the pop-up window, enter a certificate name, the certificate in PEM format, and the private key.

For help inserting the certificate and key contents, read [How to insert an SSL certificate and a key correctly](#how-to-insert-an-ssl-certificate-and-a-key-correctly).

<img src="https://support.gcore.com/hc/article_attachments/12453011844113" alt="Add_SSL_pop-up_window.png" width="523" height="673">

5\. Click **Add SSL certificate**.

The certificate will be bound to the resource and added to the list of certificates in the SSL Certificates page.

<img src="https://support.gcore.com/hc/article_attachments/12454318012305" alt="SSL_certificate_page_with_an_entry_attached_to_a_CDN.png">

### Add an SSL certificate on the SSL certificates page

To add a personal certificate without binding to a resource:

1\. Click **SSL certificates** in the side panel of the CDN service and click **Add SSL certificate**.

<img src="https://support.gcore.com/hc/article_attachments/12453744428945" alt="Add_certificate_to_SSL_certificate_page.png">

2\. In the form that appears, enter a certificate name, the SSL certificate in PEM format, and the private key.

For help inserting the certificate and key contents, read [How to insert an SSL certificate and a key correctly](#how-to-insert-an-ssl-certificate-and-a-key-correctly).

<img src="https://support.gcore.com/hc/article_attachments/12453950369937" alt="Create_SSL_certificate.png" width="524" height="511">

3\. Click **Create SSL Certificate**.

The certificate will be displayed in the list of certificates in the SSL Certificates page. The SSL Certificates page contains a table that lists your personal certificates and associated information such as the ID, name, CDN resources connected to the certificate, and expiration date.

<img src="https://support.gcore.com/hc/article_attachments/12454558136465" alt="SSL_certificate_page_with_entry_without_attached_CDN.png">

### How to insert an SSL certificate and a key correctly

1\. Open the certificate file in PEM format (.pem, .crt, or .cer) using a text editor like Notepad.

2\. Copy and paste the certificate chain in this order: Personal certificate, Intermediate CA, Root CA.

3\. All the contents of the certificate must be inserted into the **Certificate** field, including the tags "-----BEGIN CERTIFICATE-----" and "-----END CERTIFICATE-----".

4\. The certificate chain must be inserted together, similar to the following:

<img src="https://support.gcore.com/hc/article_attachments/12474188463505" alt="Insert_certificate_chain_together.png" width="525" height="211">

5\. Make sure to add a new line at the end of the certificate chain.

<img src="https://support.gcore.com/hc/article_attachments/12474236901009" alt="Add_a_new_line_at_the_end_of_the_certificate.png" width="525" height="211">

6\. Open the private key file (.key) using a text editor.

7\. Copy and paste all of its contents into the **Private key** field, including the tags "-----BEGIN RSA PRIVATE KEY-----" and "-----END RSA PRIVATE KEY-----".

8\. Click **Create SSL certificate**.

The certificate will appear in the SSL Certificates page. If it is added during the resource creation process, the certificate will also be bound to the resource.

### Attach an SSL certificate to a resource

A certificate added to the SSL Certificates page can be attached to a CDN resource while [creating](https://gcore.com/support/articles/213969429/) or editing it. To edit an existing resource:

1\. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/12472174727185" alt="CDN_resource.png">

2\. In the navigation panel, under the **General** section, click **SSL**.

<img src="https://support.gcore.com/hc/article_attachments/12472264886801" alt="SSL_option_in_Resource_Settings.png">

3\. In the **SSL** section, turn on the toggle for **Enable HTTPS**, and select **Add or select your own SSL certificate**.

<img src="https://support.gcore.com/hc/article_attachments/12472444490513" alt="Select_SSL_certificate.png" width="524" height="227">

4\. Click the **Select the certificate** dropdown and select the certificate that you want to use.

<img src="https://support.gcore.com/hc/article_attachments/12472462558609" alt="Select_SSL_certificate_dropdown.png" width="524" height="227">

5\. Click **Save changes**.

**Important**: If a Let's Encrypt certificate is enabled for a resource, the certificate selector will not be displayed. To select a personal certificate, you must first [revoke](#revoke-a-let-s-encrypt-certificate) the Let's Encrypt certificate.

### Renew an SSL certificate

There is no way to change the data of an added certificate, so when the certificate is nearing its expiration date, follow these steps:

1\. Go to the **SSL Certificates** page and [add a new certificate](#add-an-ssl-certificate-on-the-ssl-certificates-page).

2\. Go to the settings of the CDN resource you want to configure.

3\. In the **SSL** section, select the new certificate from the dropdown menu.

4\. Click **Save changes** and allow at least 15 minutes for the changes to take effect.

5\. To verify that the SSL certificate has been correctly installed and bound to the resource, enter your CNAME into the browser (e.g., https://example.ru). Click the lock icon in the address bar, navigate to **Connection is secure**, and click **Certificate is valid**.

<img src="https://support.gcore.com/hc/article_attachments/12505093148305" alt="Check_SSL_certificate_in_the_browser.png" width="524" height="204">

Compare the displayed certificate data with the certificate data you just installed. If the settings are match, you can safely [delete](#delete-an-ssl-certificate) the old certificate from the SSL Certificates page.

**Important**: Delete the old certificate only after making sure that your content is being delivered using the new certificate. If you delete the old certificate too soon, content delivery will be interrupted.

### SSL certificates expiration notifications

When your added certificates are about to expire, a notification is displayed in your account, and is sent to the email addresses of the Administrator and Engineer.

Users are notified by email:

*   14 days before the certificate expires
*   7 days before the certificate expires
*   On the day of the certificate's expiration

When you log in to your account, you will see a reminder about the expiration of the certificate.

The **SSL certificates** in the side panel will also be marked with an exclamation point if there are already expired certificates or those that will expire within the next 14 days:

<img src="https://support.gcore.com/hc/article_attachments/12502925405713" alt="SSL_certificates_section_warning_sign.png" width="172" height="164">

In the certificates table, warning signs will also appear next to the certificates that need attention.

*   If the certificate has already expired:  
      
    <img src="https://support.gcore.com/hc/article_attachments/12474790392849" alt="SSL_certificates_warning_sign_-_Expired.png">

*   If the certificate is due to expire in 14 days or less:  
      
    <img src="https://support.gcore.com/hc/article_attachments/12474878887441" alt="SSL_certificates_warning_sign_-_Near_expiration.png">

**Note**: Certificates issued by Let's Encrypt are automatically renewed, so there are no expiration notifications for such certificates.

### Delete an SSL certificate

To delete a certificate, click the three dots icon next to the certificate, then click **Delete**.

<img src="https://support.gcore.com/hc/article_attachments/12472136184849" alt="Delete_SSL_certificate.png">

**Important**: It is not possible to delete certificates that are in use by CDN resources. If you want to delete the certificate, you must first [replace it with another certificate](#renew-an-ssl-certificate) in the CDN Resource Settings.

2\. Let's Encrypt certificate
-----------------------------

If you do not have your own SSL certificate, you can activate the free Let's Encrypt certificate in your account.

### Activate a Let's Encrypt certificate

1\. [Use a custom domain name](https://gcore.com/support/articles/213969769/) for your resource.

2\. In the **SSL** section, turn on the toggle for **Enable HTTPS**, and select **Get free Let's Encrypt certificate**.

<img src="https://support.gcore.com/hc/article_attachments/12476211101713" alt="Activate_Let_s_Encrypt.png" width="523" height="195">

The certificate issuance may take up to 30 minutes. During this time, please do not:

*   disable the HTTPS option,
*   select another certificate,
*   interrupt the issuance of the current certificate.

**Important:**

*   The time it takes to issue a certificate varies depending on when the CDN resource was created. If you are requesting a certificate for a recently created resource, it may take up to 30 minutes as the configuration has not yet been fully propagated to all CDN servers. However, if the resource's configuration has already been fully propagated, issuing a Let's Encrypt certificate will only take a few minutes.

*   Let's Encrypt requires placing a temporary file at the URL _http://<CNAME>/.well-known/acme-challenge/<TOKEN>_ and making HTTP requests to this file. Before adding a Let's Encrypt certificate, make sure that your CDN resource does not have any rules that block these requests. Examples of such rules include:
    
    *   **A rule with /\***. This rule will catch any strings and override the hidden rule that is necessary to obtain a certificate.
    *   **A rule with ((?!(jpeg|gif|png|pdf|jpg|css|js|woff|woff2|ttf)).)\*$**. This rule will catch all non-static files.
    
    You can check your resource rules using the service [https://regex101.com/r/6BCT9Z/1](https://regex101.com/r/6BCT9Z/1). If you find a rule that blocks Let's Encrypt certificate issuance, delete the rule or change its pattern. The next time Let's Encrypt sends a request, the certificate issuance should be successful.
    
    If an error occurs during certificate issuance, the Enable HTTPS toggle will be disabled and a notification will be sent to your email.
    

*   You can only issue a Let's Encrypt certificate for an existing resource. If the CNAME of the resource in the DNS settings is not pointing to the [value specified in the setup guide](https://gcore.com/support/articles/213969769/), or the source is not available, the certificate will not be issued.

*   Only one Let's Encrypt certificate can be issued per resource. If you need to add or remove an additional personal domain for a resource, we will reissue the certificate after making the changes. You will receive a warning that the current certificate will only be valid for 30 minutes and will be automatically replaced.  
    
    <img src="https://support.gcore.com/hc/article_attachments/12476294660369" alt="Reissue_a_certificate_warning.jpg" width="483" height="197">
    
    While the resource is active, the certificate is renewed automatically. An attempt to reissue the certificate will be made 30 days before the expiration of the current certificate. There is only one attempt to reissue the certificate. If the certificate is not reissued, a notification will be sent to your email.
    
    In the event of an unsuccessful attempt to reissue a certificate, the current certificate will remain active for another 30 days. After the certificate's end date, the content will become unavailable via HTTPS.
    
    To avoid interruption of content delivery, please reissue the certificate yourself. To do this, [revoke](#revoke-a-let-s-encrypt-certificate) the Let's Encrypt certificate in your account and then .
    

### Revoke a Let's Encrypt certificate

To revoke a certificate, go to the Resource Settings and click **Revoke Let's Encrypt certificate** in the SSL section.

<img src="https://support.gcore.com/hc/article_attachments/12476569572241" alt="Revoke_Let_s_Encrypt.png" width="520" height="190">

**Important**: You can also use an [API request](https://apidocs.gcore.com/cdn#tag/SSL-Certificates) to replace the Let's Encrypt certificate with your own certificate without having to revoke it.

### Restrictions and features of the option

*   A wildcard domain cannot be issued a certificate.
*   If a Let's Encrypt certificate is issued, the certificate selector will not be displayed in the resource settings. Personal certificates will become available for selection after [revoking](#revoke-a-let-s-encrypt-certificate) Let's Encrypt.
*   A Let's Encrypt certificate will not be displayed on the SSL Certificates page.  
    
    <img src="https://support.gcore.com/hc/article_attachments/12476717472145" alt="SSL_Certificate_page_does_not_contain_Let_s_Encrypt_certificates.png">
    
*   A certificate is **only** visible in the settings of the resource for which it is issued.
*   Issuing and revoking a Let's Encrypt certificate does not require saving the Resource Settings.
*   If you are using DNS Cloudflare, be sure not to set the **CNAME Flattering** option to Flatten all CNAMEs. This will cause Cloudflare to return an A-record instead of a CNAME, which will prevent the issuance of a Let's Encrypt certificate. To successfully issue a Let's Encrypt certificate, set the CNAME Flattering option to **Flatten CNAME at root.**  
    
    <img src="https://support.gcore.com/hc/article_attachments/12503873872017" alt="DNS_Cloudflare_settings.png">
