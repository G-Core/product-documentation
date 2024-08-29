---
title: vendor-settings
displayName: Vendor settings
published: true
order: 30
toc:
   --1--Base control panel domain: "base-control-panel-domain"
   --1--Colors and logo: "colors-and-logo"
   --2--Brand name: "brand-name"
   --2--Languages: "languages"
   --2--Logo at the sign-in page: "logo-at-the-sign-in-page"
   --2--Header logo: "header-logo"
   --2--Header text color: "header-text-color"
   --2--Favicon: "favicon"
   --2--Brand color: "brand-color"
   --1--Customer Support Tools: "customer-support-tools"
   --2--Support phone number: "support-phone-number"
   --2--Support email: "support-email"
   --2--Link to User Agreement: "link-to-user-agreement"
   --2--Link to company website: "link-to-company-website"
   --2--Show API documentation: "show-api-documentation"
   --2--Show Knowledge Base: "show-knowledge-base"
   --2--Show Status Page: "show-status-page"
   --2--Show online chat: "show-online-chat"
   --2--Show Create new account: "show-create-new-account"
   --1--Email alerts: "email-alerts"
   --1--SMTP Provider Settings: "smtp-provider-settings" 
   --1--DNSaaS settings: "dnsaas-settings"
   --1--Services: "services"
---
# Vendor settings

Here you can add your trademark, corporate identity, symbols and contact info when reselling our products. Your company branding will be displayed in the customer's Customer Portal instead of the Gcore one.  

To set up branding, go to the "Branding settings" tab in the "Vendor settings" section.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/vendor-settings-overview.png" alt="Branding settings" width="80%">

## Base control panel domain

Enter the top level domain into the "Base  Customer Portal domain" field. It will be used to generate the product subdomains.

For example, if you specify "mycompany.com", your products will be available at "auth.mycompany.com", "cdn.mycompany.com", "accounts.mycompany.com".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/base-control-panel-domain-20.png" alt="Base Customer Portal domain" width="80%">

<alert-element type="caution" title="Caution">

To avoid issues with the Customer Portal, we don't recommend making changes in the field.

</alert-element>

For more details about the "Base Customer Portal domain" field, refer to <a href="https://gcore.com/docs/reseller-support/manuals/set-up-control-panel-services-urls" target="_blank">How to set up Customer Portal product URLs</a>.

## Colors and logo

### Brand name 

Enter your brand name. It will be displayed in the title tag of the page’s tab, in the “Help” menu > “Website”, on the Welcome page, in the body of email notifications, and in the sender's name. 

### Languages

Configure the languages that will be available for your customers in the Customer Portal.

### Logo at the sign-in page

This option configures the logo on the user sign-in page: https://auth.gcore.com/login/signin

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/logo-sign-in-page-30.png" alt="Logo at the sign-in page" width="50%">

### Header logo

The setting configures the logo in the product column and on the user sign-in page: https://auth.gcore.com/login/signin 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/header-logo-40.png" alt="Header logo">

<alert-element type="warning" title="Warning">

Your image must be: 

- Smaller than 4 MB.
- SVG (recommended)/PNG/JPG file.
- 75 x 40 px resolution.

</alert-element>

### Header text color

The setting configures the color of icons and product names in the navigation menu in the Customer Portal.

### Favicon

This configures the favicon.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/favicon-50.png" alt="Favicon" width="50%">

<alert-element type="warning" title="Warning">

Your image must be: 

- ICO file.
- 16 x 16 px.

</alert-element>  

### Brand color

This configures the color of hovered menu items and links in the Customer Portal and on the sign-in page.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/brand-color-60.png" alt="Brand color" width="50%">

## Customer Support Tools

Customer support tools include the phone number and email address of technical support, as well as links to the Status Page that informs about incidents and maintenance, the company's website, Knowledge Base and API documentation, and chat with the Gcore technical support.

All tools, except for the chat, are available in the customer's Customer Portal in the "Help" section.

If the chat option is activated, it is shown as a pop-up widget in the customer's Customer Portal.

By default, when the "Branding settings" are not activated, the customer's Customer Portal shows links, email address, and phone number of the Gcore technical support.

### Support phone number

This setting allows displaying the phone number of your technical support.

### Support email

The setting allows displaying the email address of your technical support.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/contact-reseller.png" alt="Support email" width="50%">

### Link to User Agreement

The setting allows displaying the link to your legal documents.

### Link to a company website

The "Link to website" setting allows displaying the link to your website.

### Show API documentation

The setting allows displaying links to your API documentation.

### Show Knowledge Base

The setting allows displaying a link to your Knowledge Base.

### Show Status Page

The setting allows displaying a link to your Status Page.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/links-info.png" alt="Useful links for customers" width="50%">

### Show online chat

The setting allows your customers to contact Gcore technical support via a chat in their Customer Portal. If the chat option is activated, it is shown as a pop-up widget in the customer's Customer Portal.

### Show Create new account

The setting allows your customers to create additional accounts.

If it is activated, your customers can create additional accounts from their Customer Portals.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/create-new-acc-reseller.png" alt="Show Create new account" width="50%">

## Email alerts

This setting allows you to specify email addresses that will receive notifications about your customers' actions: account deletion requests and failed authorization attempts.

**Email for deletion requests.** Here you can enter an email address to receive notifications about status updates of deletion requests. We will automatically send you emails about three events: a customer sends the request, the request is canceled, and the account is deleted. 

**Email for unsuccessful login attempts.** Here you can add an email address to receive notifications about unsuccessful login attempts. This will help you promptly respond to any suspicious activity in the accounts of all admin and Customer Portal users.

To receive emails, turn on the needed toggle and enter your email address into the field. If you want the emails to be sent to multiple email addresses, add them with the "+" button. Don't forget to save the changes.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/email-alerts-settings.png" alt="Email alerts settings" width="75%">

## SMTP Provider Settings 

This setting allows your customers to receive automatic event notifications about the product they use. For example:  

- the trial period has started, 
- the trial period will end soon, 
- a password has been changed, 
- a new user has been added to the account. 

By default, your customers receive emails sent via a Gcore mail provider from support@gcore.com. If it is ok for you, you do not need to configure anything.  

If you want to send automatic emails from another email address, specify your SMTP server and the address from which the emails should be sent. To do this: 

1\. Open "Branding settings" and make sure the "Base Customer Portal domain" field is filled in. If not, emails will not be sent.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/vendor-settings-20.png" alt="Branding settings">

2\. Go to the "SMTP Provider Settings" tab and enable the "Email for service emails" option. You will see the page with SMTP settings that need to be configured.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/vendor-settings-30.png" alt="SMTP settings that need to be configured">

3\. Configure the following settings:

- Enter the email address that you want to use to send automatic emails to your customers. It will be displayed in the "From" field in emails.   
- Enter the domain of your SMTP server such as smtp.serveraddress.com, or specify its IP address.  
- Enter the port that your SMTP server uses. 

<alert-element type="tip" title="Tip">

Port 25 is commonly abused to send spam, so some ISPs block this port. If so, some customers may not get your emails via port 25. We recommend using port 465 or 587. 

</alert-element>

- Check the "TLS" box if this security protocol for email encryption is enabled on your SMTP server. 
- Enter your username and password of your SMTP server. 

4\. Save changes.  

To make sure that everything is configured properly, send yourself a test email by clicking the "Send test email" button. The email will be sent to your account's primary email address.

## DNSaaS settings

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/dnsaas-settings-190.png" alt="DNSaaS settings" width="80%">

If the DNS service is available for your customers, you can set the values of your primary name server, secondary name server, and email address that will be used to generate SOA records.
This information will be displayed in the customer's Customer Portal when they add a domain name for the DNS zone.

By default, we show Gcore primary and secondary name servers and Gcore email address.

## Services

In your Admin Portal it is possible to set which products available to you are also visible to your customers. 

There are two levels of visibility: global (or default) and personal. 

In the settings of <a href="https://gcore.com/docs/reseller-support/manuals/configure-global-visibility" target="_blank">global visibility</a> is set the visibility of products for all your customers.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/vendor-settings-40.png" alt="Global products" width="70%">

In the settings of <a href="https://gcore.com/docs/reseller-support/manuals/configure-personal-visibility" target="_blank">personal visibility</a> you can enable or disable the visibility of products for a particular customer. The visibility statuses of personally configured products will not be available for changes from the global visibility settings. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/vendor-settings/vendor-settings-50.png" alt="Concrete account products" width="70%">
