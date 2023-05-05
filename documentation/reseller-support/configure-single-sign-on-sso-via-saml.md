---
title: configure-single-sign-on-sso-via-saml
displayName: Configure Single Sign-On (SSO) via SAML
published: true
toc:
   --1--Configuring SSO in the Admin Panel: "configuring-sso-in-the-admin-panel"
   --1--Data for the identity provider: "data-for-the-identity-provider"
   --1--Authorization via SSO in the client's personal account: "authorization-via-sso-in-the-clients-personal-account"
   --1--Authorization via SSO in the administrator's personal account: "authorization-via-sso-in-the-administrators-personal-account"
---

# Configure Single Sign-On (SSO) via SAML

**To use SSO Login for authorization, contact technical support.**   

You can give clients the ability to authorize using SSO (Single Sign-On) — a single sign-on technology with which a user can log in to a personal account using a corporate account.

To implement the technology, our systems use the SAML 2.0 XML protocol which is an open standard for the secure exchange of authentication and authorization data between the corporate identity provider (IdP) and the service provider (SP) of G-Core Labs.

  
  
  

Configuring SSO in the Admin Panel
----------------------------------

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410538997393/image-0.png" alt="">](https://reseller.gcorelabs.com/hc/article_attachments/4410538997393/image-0.png)To allow your users to log in using SSO, in the admin panel:

1\. Go to the "Authorization" tab.

2\. In the "Login options" section, activate the "SSO Login" authorization method.

3\. In the "Provider" section, enter your provider information.

| Field | Description                                                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Name\n | Your identity provider name. You can specify any name, the data from this field will be displayed only in the Admin Panel and do not affect the SSO settings. |
| Entity ID | Unique URL for the connection to the identity provider. Provided by the IdP.                                                                 |
| Domains | The list of domain names will be used to redirect to the identity provider page for authorization via SSO.                                   |
| SAML metadata | XML file with the identity provider metadata. Provided by the IdP.                                                                           |


Activate "Force redirect to the Identity provider" if desired. If this option is enabled the user only has to enter a username and password to log in. If it is disabled the user has to enter the corporate domain additionally.

4\. Using the checkboxes at the bottom, select the type of account for entering using the SSO — client’s one, administrator’s one, or both.

Data for the identity provider
------------------------------

After entering the identity provider information on the G-Core Labs side, enter the G-Core Labs information in the identity provider settings. All necessary metadata is available by link: [https://api.gcorelabs.com/auth/saml2/metadata](https://api.gcorelabs.com/auth/saml2/metadata).

If you use a self-signed SSL certificate, you must enable the use of such certificates in the settings of the identity provider.

Authorization via SSO in the client's personal account
------------------------------------------------------

1\. Click "Sign in with SAML SSO".

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410538999825/image-7.png" alt="" width="298" height="309">](https://reseller.gcorelabs.com/hc/article_attachments/4410538999825/image-7.png)

2\. This step will appear if you have not activated the "Force redirect to the Identity provider" option. If you have done, it will not appear.

Enter the corporate domain for which SSO authorization is connected and click "Sign in with SAML SSO".

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410532177937/image-8.png" alt="" width="307" height="245">](https://reseller.gcorelabs.com/hc/article_attachments/4410532177937/image-8.png)

3\. Enter your username and password and log in.

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410539000081/image-9.png" alt="" width="334" height="145">](https://reseller.gcorelabs.com/hc/article_attachments/4410539000081/image-9.png)

Authorization via SSO in the administrator's personal account
-------------------------------------------------------------

1\. Click "Sign in with SAML SSO".

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410532177681/image-4.png" alt="" width="311" height="301">](https://reseller.gcorelabs.com/hc/article_attachments/4410532177681/image-4.png)

2\. This step will appear if you have not activated the "Force redirect to the Identity provider" option. If you have done, it will not appear.

Enter the corporate domain for which SSO authorization is connected and click "Sign in".

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410538999569/image-5.png" alt="" width="316" height="221">](https://reseller.gcorelabs.com/hc/article_attachments/4410538999569/image-5.png)

3\. Enter your username and password and log in.

[<img title="" src="https://reseller.support.gcore.com/hc/article_attachments/4410539000081/image-9.png" alt="" width="344" height="149">](https://reseller.gcorelabs.com/hc/article_attachments/4410539000081/image-9.png)
