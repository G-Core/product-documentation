---
title: configure-sso-via-saml
displayName: Configure SSO
published: true
order: 40
toc:
   --1--Configuring SSO in the Admin Panel: "configuring-sso-in-the-admin-panel"
   --1--Data for the identity provider: "data-for-the-identity-provider"
   --1--Authorization in the client's control panel: "authorization-via-sso-in-the-clients-control-panel"
   --1--Authorization in the Admin panel: "authorization-via-sso-in-the-admin-panel"
---
# Configure Single Sign-On (SSO) via SAML

You can give clients the ability to authorize using SSO (Single Sign-On) — a single sign-on technology with which a user can log in to a personal account using a corporate account.

To implement the technology, our systems use the SAML 2.0 XML protocol which is an open standard for the secure exchange of authentication and authorization data between the corporate identity provider (IdP) and the service provider (SP) of Gcore.

## Configuring SSO in the Admin Panel

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/authorization-sso-10.png" alt="SSO in the Admin Panel">

To allow your users to log in using SSO, in the admin panel:

1\. Go to the "Authorization" tab.

2\. In the "Login options" section, activate the "SSO Login" authorization method.

3\. In the "Provider" section, enter your provider information.

<table>
<thead>
<tr>
<td><b>Field</b></td>
<td><b>Description</b></td>
</tr>
</thead>
<tbody>
<tr>
<td><b>Name</b</td>
<td>Your identity provider name. You can specify any name, the data from this field will be displayed only in the Admin Panel and do not affect the SSO settings.</td>
</tr>
<tr>
<td><b>Entity ID</b></td>
<td>Unique URL for the connection to the identity provider. Provided by the IdP.</td>
</tr>
<tr>
<td><b>Domains</b></td>
<td>The list of domain names will be used to redirect to the identity provider page for authorization via SSO.</td>
</tr>
<tr>
<td><b>SAML metadata</b></td>
<td>XML file with the identity provider metadata. Provided by the IdP.</td>
</tr>
</tbody>
</table>

Activate "Force redirect to the Identity provider" if desired. If this option is enabled the user only has to enter a username and password to log in. If it is disabled the user has to enter the corporate domain additionally.

4\. Using the checkboxes at the bottom, select the type of account for entering using the SSO — client’s one, administrator’s one, or both.

## Data for the identity provider

After entering the identity provider information on the Gcore side, enter the Gcore information in the identity provider settings. All necessary metadata is available by link: https://api.gcore.com/iam/auth/saml2/metadata.

If you use a self-signed SSL certificate, you must enable the use of such certificates in the settings of the identity provider.

## Authorization via SSO in the client's control panel

1\. Click "Sign in with SAML SSO".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/sign-in-with-sso-20.png" alt="Sign in with SAML SSO" width="50%">

2\. This step will appear if you have not activated the "Force redirect to the Identity provider" option. If you have done, it will not appear.

Enter the corporate domain for which SSO authorization is connected and click "Sign in with SAML SSO".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/welcome-sso-page-30.png" alt="SSO authorization " width="50%">

3\. Enter your username and password and log in.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/login-pass-40.png" alt=" log in" width="50%">

## Authorization via SSO in the Admin panel 

1\. Click "Sign in with SAML SSO".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/sign-in-50.png" alt="Sign in with SAML SSO" width="50%">

2\. This step will appear if you have not activated the "Force redirect to the Identity provider" option. If you have done, it will not appear.

Enter the corporate domain for which SSO authorization is connected and click "Sign in".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/sign-in-60.png" alt=" SSO authorization" width="50%">

3\. Enter your username and password and log in.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-sso-via-saml/login-password-70.png" alt="log in" width="50%">
