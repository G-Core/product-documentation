---
title: clients-add-edit-and-delete
displayName: Clients add, edit and delete
published: true
order: 50
toc:
   --1--Create an account: "create-an-account"
   --1--Edit an account: "edit-an-account"
   --2--Settings tab: "settings-tab"
   --2--Users tab: "users-tab"
   --1--Delete an account: "delete-an-account"
   --1--Log in as Reseller, Seller, or Client: "log-in-as-reseller-seller--or-client"
---

# Clients add, edit and delete

In the "Clients" section, you can add, view, edit, and delete clients. A client is not allowed to self-register. Only users with "Reseller" or "Seller" rights can create client accounts.

Create an account
-----------------

To create a new client account, go to the "Clients" tab and click the "Add new client" button in the upper-right corner. 

<img src="https://reseller.support.gcore.com/hc/article_attachments/360008643137/_______add_new.png" alt="_______add_new.png">

In the next window, add information about a client and select the services that will be available for them.

<img src="https://reseller.support.gcore.com/hc/article_attachments/360008715998/________________.png" alt="________________.png">

In the field on the left, enter information about a new client: e-mail, first and last name, company, name in your system, sign-in password; select "Seller" from the list to sort clients by the "Seller" attribute in the "Clients" tab and the language for automatic emails in the "Lang" field: "en" — for emails in English, "ru" — for emails in Russian.

 <img src="https://reseller.support.gcore.com/hc/article_attachments/360007147117/______________________.png" alt="______________________.png" width="631" height="567">

In the field on the right, toggle on the services that you want to make available for the client. By default, the [global service visibility](https://reseller.support.gcore.com/hc/en-us/articles/360006648777) settings are inherited.  

<img src="https://reseller.support.gcore.com/hc/article_attachments/360008643957/_______.png" alt="_______.png">**Important!** If you want to customize service visibility and override settings of the [global service visibility](https://reseller.support.gcore.com/hc/en-us/articles/360006648777) in the "Services" section, switch on and off a service toggle as required. Be aware that further changes in the global service visibility settings will not affect the client's custom service visibility. To learn more about it, click [here](https://reseller.support.gcore.com/hc/en-us/articles/360006648797). 

You can reconfigure customized service visibility in the [client settings](#edit-an-account) after creating an account.

! Enabling a service in the "Services" section **creates a tab of a given service** in the client settings and the client control panel, **but does not activate the service**. To activate a service, go to its settings, check "Activate Service" and set the service status. To learn how to set up a service, refer to [our guide on CDN configuration](https://reseller.support.gcore.com/hc/en-us/articles/360002555578).

<img src="https://reseller.support.gcore.com/hc/article_attachments/360008719238/__________________.png" alt="__________________.png">

Edit an account
---------------

After creating a client account, you can [set up their services](https://reseller.support.gcore.com/hc/en-us/articles/360006648797), edit personal data and manage rights of users of that account.

For set-up guides, refer to the "[General](https://reseller.gcorelabs.com/hc/en/sections/115001595929-General)" section. To edit the personal data and manage user rights, click the wrench icon next to client account in the "Clients" section.  

<img src="https://reseller.support.gcore.com/hc/article_attachments/360005260518/blobid0__2_.png" alt="blobid0__2_.png">

### **"Settings" tab**

On this tab, you can change a client's email address (Company email) and company name (Company).  In the "Seller" drop-down list, select "Seller" for every client to facilitate the search. 

The "Client status" field is a system one. Currently it includes only a trial status and is not editable. 

Check the "Test Account" checkbox to hide a client from the all-clients list on the "Clients" tab (it works when the "Hide test clients" filter is applied).

In the "Custom ID" field, you can set or change your own customer ID. You can enter letters, numbers and special characters. Your clients can see the Custom ID value with an API request, but they will not be allowed to edit it. 

<img src="https://reseller.support.gcore.com/hc/article_attachments/360005158937/settings.png" alt="settings.png">

Here you can also customize [service visibility](https://reseller.support.gcore.com/hc/en-us/articles/360006648797) for a client.

<img src="https://reseller.support.gcore.com/hc/article_attachments/360007036418/en8.png" alt="en8.png">

### **"Users" tab**

On this tab, you can edit personal data and manage user rights. [You can invite new users](https://gcorelabs.com/support/articles/115000573489/) only via the client control panel.

You can edit a client's name, email, language of automatic emails (Russian or English) and user type.<img src="https://reseller.support.gcore.com/hc/article_attachments/360004222258/Screenshot_31.png" alt="Screenshot_31.png">

User types: 

*   _Administrators_ have full rights (including deleting other users) 
*   _Engineers_ have rights to make any changes to service settings and account, except for editing company data and inviting new users 
*   _Purge and Prefetch only_ users have rights to view statistics, resource settings, purge cache and prefetch files to CDN cache. There is a user type who is authorized to purge cache and prefetch files to CDN cache only by sending API requests.
*   _Users_ can only view statistics, service settings, and change only their personal data (name, email, password).

Delete an account 
------------------

A client can send a request to delete the account from the "Profile" menu in the control panel.

<img src="https://reseller.support.gcore.com/hc/article_attachments/6570300938257/image_1609.png" alt="image_1609.png">

When a client clicks "Got it, request the deletion", all services of his/her account will be stopped, and the deletion request appears in the control panel. 

You can also receive emails about status updates of deletion requests. We describe how to do it in the "[Branding](https://reseller.gcorelabs.com/hc/en-us/articles/115005733445-Branding#h_01G8DZSV28N5XYAZ744RHJC05Z)" article.

When you receive a deletion request, you have 10 days to contact the client and convince him/her not to quit. After 10 days the account will be deleted automatically. 

To process the request manually, open the "Clients" section in the control panel and find the client. Click the "Edit client" icon and go to the "Delete client" tab. A page with deletion information opens.

<img src="https://reseller.support.gcore.com/hc/article_attachments/7783042329361/mceclip0.png" alt="mceclip0.png">

On the left you'll see information about a current request status. On the right you will find the history of all the client's deletion requests. Below there are two buttons used to manage requests.

"Cancel the deletion request" cancels the deletion request. When you press this button, the window for notes will appear — you can add a comment here. It will be saved in the history of all the client's deletion requests and will relate to the canceled request. 

"Delete account" deletes the account. When you press this button, the confirmation window will appear. Press "Yes, delete account" to destroy the account. 

You can delete an account even if a client hasn't sent a request — for example, to destroy abandoned or test accounts. The workflow will be the same: go to the "Delete client" tab, click "Delete account" and confirm deletion.

Log in as Reseller, Seller, or Client
-------------------------------------

In the "Clients" and "Sellers" section, you can choose the role that you want to use to log in to a client account:     

<img src="https://reseller.support.gcore.com/hc/article_attachments/360010443217/_______________.png" alt="_______________.png">

The "Log in as Reseller using client's credentials" arrow allows you to log in to a client account as a "Reseller".  

 <img src="https://reseller.support.gcore.com/hc/article_attachments/360010443197/____________.png" alt="____________.png">

The "Log in using client's credentials" arrow allows you to log in to a client account as a client.

   <img src="https://reseller.support.gcore.com/hc/article_attachments/360010526998/__________.png" alt="__________.png">

The "Log in using another user's credentials" arrow allows you to log in to a client account as a "Seller". 

<img src="https://reseller.support.gcore.com/hc/article_attachments/360010527038/__________.png" alt="__________.png">

**Important!  Currently, users with «Reseller», «Seller» or «Client» roles share the same UI and available operations in the client control panel.**  

We are working on granting more rights for "Resellers" and "Sellers" for an account management.