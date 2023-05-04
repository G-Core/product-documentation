---
title: branding
displayName: Branding
published: false
toc:
   --1--Base control panel domain: "base-control-panel-domain"
   --1--Colors and logo: "colors-and-logo"
   --2--Logo at the sign-in page: "logo-at-the-sign-in-page"
   --2--Header logo: "header-logo"
   --2--Header color: "header-color"
   --2--Header text color: "header-text-color"
   --2--Favicon: "favicon"
   --2--Brand color: "brand-color"
   --1--Customer Support Tools: "customer-support-tools"
   --2--Support phone number: "support-phone-number"
   --2--Support email address: "support-email-address"
   --2--Email for deletion requests: "email-for-deletion-requests"
   --2--Link to agreement: "link-to-user-agreement"
   --2--Link to website: "link-to-company-website"
   --2--Show API documentation: "show-api-documentation"
   --2--Show Status Page: "show-status-page"
   --2--Show tickets: "show-tickets"
   --2--Show online chat: "show-online-chat"
   --2--Show Сreate new account: "show-create-new-account"
   --1--SMTP Provider Settings: "smtp-provider-settings"
---

# Branding

Branding is a tool for service positioning that allows you to use your trademark, corporate identity, symbols and contact info when reselling our products. Your company branding will be displayed in the client control panels instead of the G-Core Labs one.  

To set up branding, go to the "Branding" section in the admin control panel.

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409934290449/1.png" alt="1.png" width="218" height="286">](https://reseller.gcorelabs.com/hc/article_attachments/4409934290449/1.png)

Base control panel domain
-------------------------

Enter the top level domain into the "Base control panel domain" field. It will be used to generate the service subdomains.

For example, if you specify "mycompany.com" , your services will be available at "auth.mycompany.com", "cdn.mycompany.com", "accounts.mycompany.com".

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409934290705/2.jpg" alt="2.jpg">](https://reseller.gcorelabs.com/hc/article_attachments/4409934290705/2.jpg)

**Important!** To avoid issues with the control panel, we don't recommend making changes in the field.

For more details about the "Base control panel domain" field, refer to [How to set up control panel services URLs](https://reseller.gcorelabs.com/hc/ru/articles/360002574458).

Colors and logo
---------------

###  Logo at the sign-in page

This option configures the logo on the user sign-in page: [https://auth .gcorelabs.com/login/signin](https://auth.gcorelabs.com/login/signin).[  
](https://auth.gcorelabs.com/login/signin)

<img src="https://reseller.support.gcore.com/hc/article_attachments/4984713390865/mceclip0.png" alt="mceclip0.png">

If it is disabled, the sign-in page inherits the logo from the "Header logo" setting.

**Please note** that your image must be: smaller than 4 MB, in SVG (recommended)/PNG/JPG file. We will save the resolution of your image if it doesn't exceed 300 x 90 pixels.

### Header logo

The setting configures the logo in the service column.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4984744199825/mceclip1.png" alt="mceclip1.png">

**Please note that** your image must be: smaller than 4 MB, SVG (recommended)/PNG/JPG file. We will save the size of your image if it doesn't exceed 300 x 90 pixels.

### Header color

The setting is not available at the moment.

### Header text color

The setting configures the color of icons and service names.

### Favicon

This configures the favicon.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4984973986193/mceclip2.png" alt="mceclip2.png">

**Please note** that your image must be: ICO file, 16 x 16 pixels.

### Brand color

This configures the color of hovered menu items and links in the control panel and on the sign-in page.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4985023486353/mceclip3.png" alt="mceclip3.png">

Customer Support Tools
----------------------

Customer support tools include the phone number and email address of technical support, as well as links to the Status Page that informs about incidents and maintenance, the company's website, Knowledge Base and API documentation, tickets and chat with the G-Core Labs technical support.

All tools, except for the chat, are available in the client control panel in the "Help" section.

If the chat option is activated, it is shown as a pop-up widget in the client control panel.

By default, when the "Branding" settings are not activated, the client control panel shows links, email address and phone number of the G-Core Labs technical support.

### <img src="https://reseller.support.gcore.com/hc/article_attachments/4985275009297/mceclip5.png" alt="mceclip5.png">

### Support phone number

This setting allows displaying the phone number of technical support.

If the setting is activated but not configured, clients will see an empty field in their control panels.

If the setting is not activated, the client control panel shows the phone number of the G-Core Labs technical support.

### Support email address

The setting allows displaying the email address of technical support. If it is activated but left unspecified, your clients will see an empty field. If it is not activated, the client control panel will show the email address of the G-Core Labs technical support.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4985337481489/mceclip6.png" alt="mceclip6.png">

### Email for deletion requests

<img src="https://reseller.support.gcore.com/hc/article_attachments/8659196194577/mceclip0.png" alt="mceclip0.png">

Here you can enter an email address to receive notifications about status updates of deletion requests. We will automatically send you emails about three events: a client sends the request, the request is canceled, the account is deleted. 

To receive emails, turn on the "Email for deletion request" toggle and enter your email address into the field. If you want the emails to be sent to multiple email addresses, add them with the "+" button. Don't forget to save the changes at the bottom of the page. 

### Link to User Agreement

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409934294289/11.jpg" alt="11.jpg">](https://reseller.gcorelabs.com/hc/article_attachments/4409934294289/11.jpg)

The setting allows displaying the link to legal documents.

It has two parameters:

*   G-Core Labs link — if you want to use the link to G-Core Labs legal documents.
*   Custom link — if you want to specify a link to your legal documents.

### Link to company website

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409926071313/12.jpg" alt="12.jpg">](https://reseller.gcorelabs.com/hc/article_attachments/4409926071313/12.jpg)

The "Link to website" setting allows displaying the link to your website.

It has two parameters:

*   G-Core Labs link — if you want to use the link to G-Core Labs website.
*   Custom link — if you want to specify a link to your website.

### Show API documentation

The setting allows displaying links to API documentation.

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409934294673/13.jpg" alt="13.jpg">](https://reseller.gcorelabs.com/hc/article_attachments/4409934294673/13.jpg)

It has two parameters:

*   G-Core Labs link — if you want to use the link to the G-Core Labs API documentation.
*   Custom link — if you want to specify a link to your API documentation.

### Show Status Page

[<img src="https://reseller.support.gcore.com/hc/article_attachments/4409934295057/14.jpg" alt="14.jpg">](https://reseller.gcorelabs.com/hc/article_attachments/4409934295057/14.jpg)

The setting allows displaying a link to your Status Page.

It has two parameters:

*   G-Core Labs link — if you want to use the link to the G-Core Labs Status Page.
*   Custom link — if you want to specify a link to your Status Page.

### Show tickets

This setting allows your clients to send requests directly to the G-Core Labs technical support.

Activate the setting so that your clients can contact technical support via the ticket system in their control panel.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4985441822993/mceclip7.png" alt="mceclip7.png">

### Show online chat

The setting allows your clients to contact the G-Core Labs technical support via a chat in their control panel. If the chat option is activated, it is shown as a pop-up widget in the client control panel.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4985648444817/mceclip8.png" alt="mceclip8.png">

### Show Create new account

The setting allows your clients to create additional accounts.

If it is activated, your clients can create additional accounts from their control panels.

<img src="https://reseller.support.gcore.com/hc/article_attachments/4985738776465/mceclip9.png" alt="mceclip9.png">

SMTP Provider Settings 
-----------------------

This setting allows your clients to receive automatic event notifications about the service they use. For example:  

*   the trial period has started, 
*   the trial period will end soon, 
*   a password has been changed, 
*   a new user has been added to the account. 

By default, your clients receive emails sent via a G-Core Labs mail provider from _support@gcorelabs.com_. If it is ok for you, you do not need to configure anything.  

If you want to send automatic emails from another email address, specify your SMTP server and the address from which the emails should be sent. To do this: 

1\. Open "Branding settings" and make sure the "Base control panel domain" field is filled in. If not, emails will not be sent.  
  
<img src="https://reseller.support.gcore.com/hc/article_attachments/6543542362769/image_1553.png" alt="image_1553.png">

2\. Go to the "SMTP Provider Settings" section and enable the "Email for service emails" option.  
  
<img src="https://reseller.support.gcore.com/hc/article_attachments/6543529458705/image_1550.png" alt="image_1550.png">

You will see the page with SMTP settings that need to be configured.

<img src="https://reseller.support.gcore.com/hc/article_attachments/6543532022289/image_1556.png" alt="image_1556.png">

3\. Enter the email address that you want to use to send automatic emails to your clients. It will be displayed in the "From" field in emails.   

4\. Enter the domain of your SMTP server such as _smtp.serveraddress.com_, or specify its IP address.  

5\. Enter the port that your SMTP server uses. Please note: port 25 is commonly abused to send spam, so some ISPs block this port. If so, some clients may not get your emails via port 25. We recommend using port 465 or 587. 

6\. Check the "TLS" box if this security protocol for email encryption is enabled on your SMTP server. 

7\. Enter your username and password of your SMTP server. 

8\. Save the changes.  

To make sure that everything is configured properly, send yourself a test email by clicking the "Send test email" button. The email will be sent to your account's primary email address.
