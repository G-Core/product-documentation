---
title: getting-started
displayName: Getting started
published: true
order: 20
toc:
    --1--What's next?: "whats-next"
    --1--Inviting Sellers: "inviting-sellers"
    --1-Setting up client control panel: "setting-up-client-control-panel"
    --1--Creating client accounts: "creating-client-accounts"
    --1--Service management: "service-management"
    --1--Useful links: "useful-links"
---
# Getting started

Once we create a reseller account you'll get an email with the registration confirmation link. Follow the link to set a password. The link will be active for 24 hours. Write to [support@gcore.com](mailto:support@gcore.com) if the link expires or you experience other issues. 

Admin control panel enterance URL is ```https://admin.gcore.top/```.

## What's next?

Reseller is your account admin. Only one user in your organization can be a Reseller. This user can add Sellers, set up account branding and generate Statistics reports in the admin control panel.

## Inviting Sellers

Seller is an additional user who has access to the admin control panel. Users with this role can add clients and set up their resources. There are no limits to the number of Sellers for one organization.

You can read on Seller account creating and management in this article.

## Setting up client control panel

In the client control panel, clients can set up their services, check statistics and contact technical support. With no additional settings, your clients will be seeing Gcore clients' control panel which has our corporate colors, logo and is based at https://accounts.gcore.com.

If you are using your own control panel and just need our API documentation to integrate your service with ours, here are the links:

- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">Reseller API documentation</a>
- <a href="https://api.gcore.com/docs/docs/iam" target="_blank">Services API documentation</a>

If you and your clients are going to use the client control panel and you would like to change its look, read the following articles:

- <a href="https://gcore.com/docs/reseller-support/manuals/set-up-control-panel-services-urls" target="_blank">How to set up control panel services URLs</a>
- <a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Vendor settings</a>

## Creating client accounts

After you log into the admin control panel you'll be transferred to the "Accounts" section. Here you can create and edit your clients' accounts (clients are unable to register in your control panel on their own). Both Sellers and Reseller can create client accounts. You can read more on creating client accounts in <a href="https://gcore.com/docs/reseller-support/manuals/manage-clients" target="_blank">this article</a>.

Along with the Reseller account, we create a client account with the same email and company name. This account is used for collecting your clients' stats, generating monthly reports (more on it in <a href="https://gcore.com/docs/reseller-support/manuals/generate-monthly-reports" target="_blank">this article</a>), keeping track of your Sellers and Reseller accounts (they are considered the users for that client). Also, we recommend creating CDN Resources for the client control panel services in this account (more on it in <a href="https://gcore.com/docs/reseller-support/manuals/set-up-control-panel-services-urls" target="_blank">this article</a>). This account can't be deleted.

## Service management

All our services are available for reselling: CDN, Web Protection, Streaming, Cloud, DNS, and Storage. When signing the contract, you discuss with your manager what services you want to resell. By default, the selected services will be displayed in the client's control panel. You can adjust the visibility of products to all customers in the "Vendor setting" section, "Services" subsection of the admin panel:

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/services-10.png" alt="">

You can also override the General settings from the "Services" section in the client settings. Go to the client settings, open the list of clients, in the "Accounts" section, click on the ID of the desired client, or click on the "Edit" button in the "Actions" сolumn. If you click on the "Log in" button you'll log in the client control panel under client's admin user

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/client-editing-20.png" alt="">

On the "Services" tab, choose services that you want to display in the client's control panel.

- You can not disable the service whose switch is marked in light gray color because the service is "Active" or "Trial" status.  Click the "Show more" button to change the status to "Trialend" or "Paused" before disabling the service.
- If you enable a service, it will be displayed in the client's control panel.
- If you disable a service, it will not be displayed in the client's control panel.

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/client-services-30.jpg" alt="">

**Please note**: Displaying a service in the control panel does not allow the client to manage it by default. If the service is displayed but not configured (see the service management articles below), the customer will see the service activation request window:

<img src="https://assets.gcore.pro/docs/reseller-support/getting-started/welcome-page-40.png" alt="">

When submitting an activation request, Gсore technical support or you — depending on the setting of the "Support email" field in the "<a href="https://gcore.com/docs/reseller-support/manuals/vendor-settings" target="_blank">Vendor settings</a>" section — will receive an email about the client's wish to access the service.

Articles on service management:

- <a href="https://gcore.com/docs/reseller-support/cdn-service-management" target="_blank">CDN service management</a>
- <a href="https://gcore.com/docs/reseller-support/storage-service-management" target="_blank">Storage service management</a>

## Useful links

If you would like to get notifications about planned maintenance activities and incidents, subscribe to our <a href="https://status.gcore.com/" target="_blank">Status Page</a>. You can read more about the service and its subscription methods in <a href="https://gcore.com/docs/account-settings/be-aware-of-the-service-status-scheduled-and-emergency-maintenance" target="_blank">this article</a>.

- <a href="https://gcore.com/docs/reseller-support/api" target="_blank">Reseller API documentation</a>
- <a href="https://api.gcore.com/docs/docs/iam" target="_blank">Services API documentation</a>

This knowledge base describes how to manage services as an administrator from the admin control panel and doesn't include articles on how to set up services as a client. For the latter, read the articles here: https://gcore.com/docs/. If you have questions, please, send them to [support@gcore.com](mailto:support@gcore.com).