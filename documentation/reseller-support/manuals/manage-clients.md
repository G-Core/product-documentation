---
title: manage-clients
displayName: Manage clients
published: true
order: 10
toc:
   --1--Create an account: "create-an-account"
   --1--Edit an account: "edit-an-account"
   --2--"Edit client" tab: "edit-client-tab"
   --2--"Services" tab: "services-tab"
   --2--"Users" tab: "users-tab"
   --1--Delete client: "delete-client"
   --1--Log in to a client account: "log-in-to-a-client-account"
---
# Manage clients

In the "Accounts" section, "Clients" subsection, you can add, view, edit, and delete clients. A client is not allowed to self-register. Only users with "Reseller" or "Seller" rights can create client accounts.

## Create an account

To create a new client account, go to the "Clients" subsection and click the "Add new client" button in the upper-right corner. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/add-new-client-10.png" alt="">

In the next window, add information about a client and select the services that will be available for them.

In the field on the left, enter information about a new client: e-mail, first and last name, company, name in your system, sign-in password; select "Seller" from the list to sort clients by the "Seller" attribute in the "Clients" tab and the language for automatic emails in the "Lang" field: "en" — for emails in English.

In the field on the right, toggle on the services that you want to make available for the client. By default, the <a href="https://gcore.com/docs/reseller-support/manuals/configure-global-visibility " target="_blank">global service visibility</a> settings are inherited.  

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/list-of-services-20.png" alt="">

**Important!** If you want to customize service visibility and override settings of the global service visibility in the "Vendor settings" section, the "Services" subsection switch on and off a service toggle as required. Be aware that further changes in the global service visibility settings will not affect the client's custom service visibility. To learn more about it, click <a href="https://gcore.com/docs/reseller-support/manuals/configure-personal-visibility " target="_blank">here</a>. 

You can reconfigure customized service visibility in the client settings after creating an account.

Enabling a service in the "Services" section **creates a tab of a given service** in the client settings and the client control panel, **but does not activate the service**. To activate a service, go to a client settings, check "Activate Service" and set the service status. To learn how to set up a service, refer to our guide on <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN configuration</a>.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/cdn-settings-30.png" alt="">

## Edit an account

After creating a client account, you can set up their services, edit personal data and manage rights of users of that account.

For set-up guides, refer to the following product docs:

- <a href="https://gcore.com/docs/reseller-support/new-admin-panel-interface" target="_blank">New admin panel interface</a>
- <a href="https://gcore.com/docs/reseller-support/getting-started" target="_blank">Getting started</a>
- <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN service management</a>
- <a href="https://gcore.com/docs/reseller-support/storage-service-management" target="_blank">Storage service management</a>
- <a href="https://gcore.com/docs/reseller-support/service-status" target="_blank">Service statuses</a>
- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">API</a>

To edit the personal data and manage user rights, click on the ID of the desired client, or click on the "Edit" button in the "Actions" сolumn. If you click on the "Log in" button you'll log in the client control panel under client's admin user. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-account-40.png" alt="">

### Edit client tab

On this tab, you can change a client's email address (Company email) and company name (Company).  In the "Seller" drop-down list, select "Seller" for every client to facilitate the search. 

The "Client status" field is a system one. Currently, it includes only a trial status and is not editable. 

Check the "Test Account" checkbox to hide a client from the all-clients list on the "Clients" subsection (it works when the "Test Account" filter value is "false").

In the "Custom ID" field, you can set or change your own customer ID. You can enter letters, numbers and special characters. Your clients can see the Custom ID value with an API request, but they will not be allowed to edit it. 

If you click on the "Log in as Admin using client’s credentials" button you'll log in the client control panel under client's admin user.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-client-50.png" alt="">

### Services tab

You can customize <a href="https://gcore.com/docs/reseller-support/manuals/configure-personal-visibility" target="_blank">service visibility</a> for a client.

### Users tab

On this tab, you can edit personal data and manage user rights. You can <a href="https://gcore.com/docs/account-settings/users/add-edit-or-delete-an-invited-user" target="_blank">invite new users</a> only via the client control panel.

You can edit a client's name, email address, language of automatic emails and user type.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-user-60.png" alt="">

<a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">About Users</a>

## Delete client

A client can send a request to delete the account from the "Profile" menu in the control panel.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/delete-account-70.png" alt="">

When a client clicks "Got it, request the deletion", all services of his/her account will be stopped, and the deletion request appears in the control panel. 

You can also receive emails about status updates of deletion requests. We describe how to do it in the "<a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Vendor settings</a>" article.

When you receive a deletion request, you have 10 days to contact the client and convince him/her not to quit. After 10 days the account will be deleted automatically. 

To process the request manually, open the "Delete client" tab.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/confirmation-deletion-80.png" alt="">

On the left you'll see information about a current request status. On the right you will find the history of all the client's deletion requests. Below there are two buttons used to manage requests.

"Cancel the deletion request" cancels the deletion request. When you press this button, the window for notes will appear — you can add a comment here. It will be saved in the history of all the client's deletion requests and will relate to the canceled request. 

"Delete account" deletes the account. When you press this button, the confirmation window will appear. Press "Yes, delete account" to destroy the account. 

You can delete an account even if a client hasn't sent a request — for example, to destroy abandoned or test accounts. 

## Log in to a client account

Open the list of clients, in the "Accounts" section, find the desired client and click on the "Log in" button in the "Actions" сolumn.  You'll log in the client control panel under client's admin user

**Important!**  Currently, users with «Reseller», «Seller» roles share the same UI and available operations in the client control panel.  

We are working on granting more rights for "Resellers" and "Sellers" for an account management.