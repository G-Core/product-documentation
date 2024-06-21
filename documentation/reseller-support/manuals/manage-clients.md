---
title: manage-clients
displayName: Manage customers
published: true
order: 10
toc:
   --1--Create an account: "create-an-account"
   --1--Edit an account: "edit-an-account"
   --2--"Edit account" tab: "edit-account-tab"
   --2--"Products" tab: "products-tab"
   --2--"Users" tab: "users-tab"
   --1--Delete: "delete-account"
   --1--Log in to a customer account: "log-in-to-a-customer-account"
---
# Manage customers

In the "Accounts" section, you can add, view, edit, and delete customers. A customer is not allowed to self-register. Only users with "Reseller" or "Seller" rights can create customer accounts.

## Create an account

To create a new customer account, go to the "Accounts" subsection and click the "Add new account" button in the upper-right corner. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/manage-clients-10.png" alt="Accounts subsection ">

In the next window, add information about a customer and select the products that will be available for them.

In the field on the left, enter information about a new customer: e-mail, first and last name, company, name in your system, sign-in password; select "Seller" from the list to sort customers by the "Seller" attribute in the "Accounts" tab and the language for automatic emails in the "Lang" field: "en" — for emails in English.

In the field on the right, toggle on the products that you want to make available for the customer. By default, the <a href="https://gcore.com/docs/reseller-support/manuals/configure-global-visibility " target="_blank">global product visibility</a> settings are inherited.  

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/manage-clients-20.png" alt="global product visibility settings">

**Important!** If you want to customize product visibility and override settings of the global product visibility in the "Settings" section, the "Products" subsection switch on and off a product toggle as required. Be aware that further changes in the global product visibility settings will not affect the customer's custom product visibility. To learn more about it, click <a href="https://gcore.com/docs/reseller-support/manuals/configure-personal-visibility " target="_blank">here</a>. 

You can reconfigure customized product visibility in the account settings after creating an account.

Enabling a product in the "Products" section **creates a tab of a given product** in the account settings and the customer's Customer Portal, **but does not activate the product**. To activate a product, go to a account settings, check "Activate product" and set the product status. To learn how to set up a product, refer to our guide on <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN configuration</a>.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/cdn-settings-30.png" alt=" CDN configuration">

## Edit an account

After creating a customer account, you can set up their products, edit personal data and manage rights of users of that account.

For set-up guides, refer to the following product docs:

- <a href="https://gcore.com/docs/reseller-support/new-admin-panel-interface" target="_blank">New Admin Portal interface</a>
- <a href="https://gcore.com/docs/reseller-support/getting-started" target="_blank">Getting started</a>
- <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN management</a>
- <a href="https://gcore.com/docs/reseller-support/storage-service-management" target="_blank">Storage management</a>
- <a href="https://gcore.com/docs/reseller-support/service-statuses" target="_blank">Product statuses</a>
- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">API</a>

To edit the personal data and manage user rights, click on the ID of the desired customer, or click on the "Edit" button in the "Actions" сolumn. If you click on the "Log in" button you'll log in the customer's Customer Portal panel under customer's admin user. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-account-40.png" alt="Edit an account">

### Edit account tab

In this section, you can:

1\. Log in to the Customer Portal using the client’s credentials.

2\. Check the “Test Account” checkbox to hide a customer from the all customers list in the Customers subsection. Customer accounts marked as test accounts will not be displayed in the list. If you want to see test accounts, set the filter to “Test account true.”

In the “Settings” section, fields with the information about the customer are included per steps 3–6.

3\. Review the "Account status." It shows the steps of using an account. The customer's status is determined automatically according to the conditions:

- **Preparation**. An account has been created, but the user has not yet used any product.
- **Trial**. An account has at least one product in “Trial” status, but no product in “Active” status.
- **Active**. An account has at least one product in “Active” status.
- **Trial End**. At least one of the product is in the “Deleted,” “Trial End,” or “Paused” status, and no product is in “Active” or “Trial” status.
- **Deleted**. An account is deleted.

**Note**: You can’t edit the "Account status” field.  

4\. Change a customer’s email address (Company email) and company name (Company.) 

5\. Set your Account ID in the “Custom ID” field. You can use letters, numbers, and special characters. Your customers will see the value in the API requests but cannot edit it.

6\. Select “Seller” for every customer in the “Seller” dropdown list, to facilitate the search.

7\. If you change something, don’t forget to save the changes at the top of the page.


<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-clients-tab.png" alt="Edit customer tab" width="80%">

### Services tab

You can customize <a href="https://gcore.com/docs/reseller-support/manuals/configure-personal-visibility" target="_blank">product visibility</a> for a customer.

### Users tab

On this tab, you can edit personal data and manage user rights. You can <a href="https://gcore.com/docs/account-settings/users/about-users/add-edit-or-delete-an-invited-user" target="_blank">invite new users</a> only via the customer's Customer Portal.

You can edit a customer's name, email address, language of automatic emails and user type.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/edit-user-60.png" alt="Users tab">

<a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">About Users</a>

## Delete account

To delete their accounts, customers should navigate to the "Profile" section: 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/go-to-profile.png" alt="Open profile" width="75%">

Then, open the "Account profile" tab, go to the "Delete account" page and click **Delete my account**. 

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/delete-account.png" alt="Delete account" width="85%">

After confirmation all products of their accounts will be stopped, and the deletion request appears in the Customer Portal. 

You can also receive emails about status updates of deletion requests. We describe how to do it in the "<a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Vendor settings</a>" article.

When you receive a deletion request, you have 10 days to contact the customer and convince him/her not to quit. After 10 days the account will be deleted automatically. 

To process the request manually, open the "Delete account" tab.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/manage-clients/confirmation-deletion-80.png" alt="Delete account">

On the left you'll see information about a current request status. On the right you will find the history of all the customer's deletion requests. Below there are two buttons used to manage requests.

"Cancel the deletion request" cancels the deletion request. When you press this button, the window for notes will appear — you can add a comment here. It will be saved in the history of all the customer's deletion requests and will relate to the canceled request. 

"Delete account" deletes the account. When you press this button, the confirmation window will appear. Press "Yes, delete account" to destroy the account. 

You can delete an account even if a customer hasn't sent a request — for example, to destroy abandoned or test accounts. 

## Log in to a customer account

Open the list of customers, in the "Accounts" section, find the desired customer and click on the "Log in" button in the "Actions" сolumn.  You'll log in the customer's Customer Portal under customer's admin user

**Important!**  Currently, users with «Reseller», «Seller» roles share the same UI and available operations in the customer's Customer Portal.  

We are working on granting more rights for "Resellers" and "Sellers" for an account management.
