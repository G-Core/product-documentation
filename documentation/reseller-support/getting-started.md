---
title: getting-started
displayName: Getting started
published: true
order: 20
toc:
    --1--What's next?: "whats-next"
    --1--Inviting Sellers: "inviting-sellers"
    --1--Setting up Customer Portal: "setting-up-customer-portal"
    --1--Creating customer accounts: "creating-customer-accounts"
    --1--Product management: "product-management"
    --1--Useful links: "useful-links"
---
# Getting started

Once we create a reseller account, you'll get an email with the registration confirmation link. Follow the link to set a password. The link will be active for 24 hours. Write to [support@gcore.com](mailto:support@gcore.com) if the link expires or you experience other issues. 

Admin Portal enterance URL is ```https://admin.gcore.top/```.

## What's next?

Reseller is your account admin. Only one user in your organization can be a Reseller. This user can add Sellers, set up account branding and generate Statistics reports in the Admin Portal.

## Inviting Sellers

Seller is an additional user who has access to the Admin Portal. Users with this role can add clients and set up their resources. There are no limits to the number of Sellers for one organization.

You can read on Seller account creating and management in this article.

## Setting up Customer Portal

In the Customer Portal, customers can set up their products, check statistics, and contact technical support. With no additional settings, your customers will be seeing Gcore Customer Portal which has our corporate colors, logo, and is based at https://accounts.gcore.com.

If you are using your own Customer Portal and just need our API documentation to integrate your service with ours, here are the links:

- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">Reseller API documentation</a>
- <a href="https://api.gcore.com/docs/iam" target="_blank">Product API documentation</a>

If you and your customers are going to use the Customer Portal and you would like to change its look, read the following articles:

- <a href="https://gcore.com/docs/reseller-support/manuals/set-up-control-panel-services-urls" target="_blank">How to set up Customer Portal product URLs</a>
- <a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Settings</a>

## Creating customer accounts

After you log into the Admin Portal, you'll be transferred to the "Accounts" section. Here you can create and edit your customers' accounts (customers are unable to register in your Admin Portal on their own). Both Sellers and Reseller can create customer accounts. You can read more on creating customer accounts in <a href="https://gcore.com/docs/reseller-support/manuals/manage-clients" target="_blank">this article</a>.

Along with the Reseller account, we create a customer account with the same email and company name. This account is used for collecting your customers' stats, generating monthly reports (more on it in <a href="https://gcore.com/docs/reseller-support/manuals/generate-monthly-reports" target="_blank">this article</a>), keeping track of your Sellers and Reseller accounts (they are considered the users for that customer). Also, we recommend creating CDN Resources for the Customer Portal products in this account (more on it in <a href="https://gcore.com/docs/reseller-support/manuals/set-up-control-panel-services-urls" target="_blank">this article</a>). This account can't be deleted.

## Product management

All our products are available for reselling: CDN, Web Application Security, Video Streaming, Edge Cloud, Managed DNS, and Storage. When signing the contract, you discuss with your manager what products you want to resell. By default, the selected products will be displayed in the Customer Portal. You can adjust the visibility of products to all customers in the "Setting" section, "Products" subsection of the Admin Portal:

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/getting-started-10.png" alt="Service management">

You can also override the General settings from the "Services" section in the customer settings. Go to the customer settings, open the list of customers, in the "Accounts" section, click on the Account ID of the desired customer, or click on the "Edit" button in the "Actions" сolumn. If you click on the "Log in" button you'll log in the Customer Portal under customer's admin user

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/getting-started-20.png" alt="Clients">

On the "Products" tab, choose products that you want to display in the customer's Customer Portal.

- You can not disable the product whose switch is marked in light gray color because the product is "Active" or "Trial" status.  Click the "Show more" button to change the status to "Trialend" or "Paused" before disabling the product.
- If you enable a product, it will be displayed in the customer's Customer Portal.
- If you disable a product, it will not be displayed in the customer's Customer Portal.

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/client-services-30.jpg" alt="Services">

**Please note**: Displaying a Product in the Customer Portal does not allow the customer to manage it by default. If the product is displayed but not configured (see the product management articles below), the customer will see the product activation request window:

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/welcome-page-40.png" alt="Storage">

When submitting an activation request, Gсore technical support or you — depending on the setting of the "Support email" field in the "<a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Vendor settings</a>" section — will receive an email about the customer's wish to access the product.

Articles on product management:

- <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN product management</a>
- <a href="https://gcore.com/docs/reseller-support/storage-service-management" target="_blank">Storage product management</a>

## Useful links

If you would like to get notifications about planned maintenance activities and incidents, subscribe to our <a href="https://status.gcore.com" target="_blank">Status Page</a>. You can read more about the service and its subscription methods in <a href="https://gcore.com/docs/account-settings/be-aware-of-the-service-status-scheduled-and-emergency-maintenance" target="_blank">this article</a>.

- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">Reseller API documentation</a>
- <a href="https://api.gcore.com/docs/iam" target="_blank">Product API documentation</a>

This knowledge base describes how to manage products as an administrator from the Admin Portal and doesn't include articles on how to set up products as a customer. For the latter, read the articles here: https://gcore.com/docs/. If you have questions, please, send them to [support@gcore.com](mailto:support@gcore.com).