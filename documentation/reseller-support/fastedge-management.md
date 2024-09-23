---
title: fastedge-management
displayName: FastEdge management
published: true
order: 45
toc:
    --1--Manage FastEdge applications: "manage-fastedge-applications"
    --2--Filter table data: "filter-data-in-the-applications-table"
    --2--Configure columns: "configure-columns-in-the-applications-table"
    --2--Stop or activate an application: "stop-or-activate-an-application"
    --2--Upgrade a binary version: "upgrade-a-binary-version"
    --2--Delete an application: "delete-an-application"
    --1--Manage application templates: "manage-application-templates"
    --2--Filter table data: "filter-data-in-the-templates-table"
    --2--Configure columns: "configure-columns-in-the-templates-table"
    --2--Share or unshare a template: "share-or-unshare-a-template"
    --2--Delete a template: "delete-a-template"
---
# FastEdge management

In the Gcore Admin Panel, you can manage two types of FastEdge applications and their corresponding templates: 

* **HTTP applications**: Manage your cloud applications deployed on edge servers across the global Gcore CDN network. 

* **CDN applications**: Manage FastEdge applications integrated with Gcore CDN infrastructure to extend the CDN functionality.  

## Manage FastEdge applications

The **HTTP Applications** and **CDN Applications** pages contain information about all FastEdge apps created and used by your customers.  

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/http-apps-page.png" alt="HTTP Applications page" width="80%">

<alert-element type="tip" title="Tip">
 
You can save the preferred filters and columns displayed in the applications and templates tables. For instructions on how to configure and save presets, check out the <a href="https://gcore.com/docs/reseller-support/new-admin-panel-interface#search-presets" target="_blank">Search presets</a> section.
 
</alert-element>

### Filter data in the applications table

You can filter application data based on the following criteria: 

* **Client ID**. A unique identifier for the customer account where the application was created. 

* **Status**. The current state of the application: 

 * **Active**: the application is up and running 

 * **Disabled**: the application is stopped 

* **Template ID**. A unique identifier for the template used to create the application. If this column is empty, it indicates that the application was created without a template. 

* **Binary ID**. A unique identifier for the binary file from which the application was created. Useful for distinguishing different versions of an app built from the same template.

* **Plan**: The subscription plan according to which the application is billed. This is typically determined by the customer’s plan. 

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/app-filters.png" alt="List of table filters" width="80%">

To filter information in the table: 

1\. Click **Add filter**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/add-filter.png" alt="Add filter button highlighted" width="80%">

2\. Specify the required criteria. For example, set the application status to **Active**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/filter-sample-active.png" alt="Table filter set to active status" width="80%">

3\. Click **Apply filter**. 

The table results will be updated accordingly, and you’ll see the list of all currently running applications. 

Click **Reset all** to switch back to the default view. 

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/reset-all.png" alt="Reset all link highlighted" width="80%">

### Configure columns in the applications table 

The applications table displays the following information about FastEdge apps: 

* **ID**: A unique identifier for the application. This information can be useful for diagnostic purposes and troubleshooting. If you encounter issues with a specific app and require assistance from our support team, we recommend providing the app ID in your support request. 

* **Name**: The application name specified in the Customer Portal during application creation. 

* **Upgradable**: If the column shows **Outdated**, this means that the application was created from a template and is using an old version of the binary. In this case, it’s best to <a href="https://gcore.com/docs/reseller-support/fastedge-management#upgrade-a-binary-version" target="_blank">update the application</a> to the newest version.  

* **URL** (HTTP applications only): Link to the deployed HTTP application. 

* **Reseller**: The ID of a reseller account where the application was created. 

* **Description**: If your customer provided a description when creating the application in the Customer Portal, the description will appear in this column.  

### Stop or activate an application

1\. Open the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. Find the application that you want to manage and click the three-dot icon next to it. 

3\. Select the required action: **Stop** or **Start**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/stop-app.png" alt="Application settings menu with stop button highlighted" width="80%">

The application status will be changed respectively and the changes will be also reflected in the Customer Portal, where your customers can also stop or start the application. 

### Upgrade a binary version 

Sometimes, you might see the **Outdated** status in the **Upgradeable** column. This status is only relevant to applications created from templates, and it means that the template has been updated.  

If this happens, we recommend upgrading the application binary to the newest template version to get the latest improvements and security fixes: 

1\. Open the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. Find the application that you want to update and click the three-dot icon next to it. 

3\. Click **Upgrade binary version**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/upgrade-app.png" alt="Application settings menu with upgrade button highlighted" width="80%">

Your application’s binary has been upgraded to the latest version.

### Delete an application

<alert-element type="info" title="Info">
 
To delete a FastEdge CDN application, first disconnect it from the CDN resource. You won’t be able to proceed with the deletion until this step is completed.
 
</alert-element>

If you delete a FastEdge application, it will be permanently removed from the Customer Portal.  

To delete an application: 

1\. Open the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. Find the application that you want to remove and click the three-dot icon next to it. 

3\. Click **Delete**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/delete-app.png" alt="Application settings menu with delete button highlighted" width="80%">

4\. Confirm your action by clicking **Yes, delete**. 

The application has been successfully removed. 

## Manage application templates 

On the **Templates** pages, you can view and manage all templates created by your customers in the Customer Portal. 

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/cdn-templates-page.png" alt="CDN Templates page" width="80%">

## Filter data in the templates table

You can filter the templates based on the following criteria: 

* **Client ID**. A unique identifier for the customer account where the template was created. 

* **Group ID**. A unique identifier for the default group that’s associated with a single reseller and includes all customers created by that reseller. You can create and manage groups via <a href="https://api.gcore.com/docs/fastedge#tag/Groups" target="_blank">API</a>. 

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/cdn-templates-filter.png" alt="List of table filters" width="80%">

To filter templates in the table: 

1\. Click **Add filter**.

2\. Specify the required criteria. For instance, enter the ID of a particular client to view all their templates.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/filter-sample-active.png" alt="Table filter set to active status" width="80%">

3\. Click **Apply filter**. 

The table results will be updated accordingly. 

### Configure columns in the templates table 

The templates table displays the following information: 

* **ID**: A unique identifier for the template.  

* **Name**: A template name specified in the Customer Portal. 

* **Reseller**: A unique identifier for the reseller that created the template.  

* **Group ID**: A unique identifier for the group that includes all reseller’s customers. 

* **Description**: If your customer provided a desciption when creating the template in the Customer Portal, the description will appear in this column. 

* **Instructions**: Guidelines for using the template (if those were provided in the Customer Portal). 

### Share or unshare a template 

Sharing a template makes it accessible to all your customers in the Customer Portal. They will be able to view it in the templates list and create FastEdge applications from this template. 

To use the template sharing options: 

1\. Open the relevant template page, either under the **HTTP Applications** or **CDN Applications**. 

2\. Find the needed template and click the three-dot icon next to it. 

3\. Click **Share template** or **Unshare template**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/share-template.png" alt="Template settings menu with unshare button highlighted" width="80%">

Shared templates have the group ID specified in the table. If the **Group ID** column is empty, this means that the template isn’t shared with your customers, and they can’t see it in the Customer Portal. 

### Delete a template

If you delete a template, it will be removed from the Customer Portal and you won’t be able to restore it back. You’ll need to upload the template again. 

To delete a template: 

1\. Open the relevant template page, either under the **HTTP Applications** or **CDN Applications**. 

2\. Find the template that you want to remove and click the three-dot icon next to it. 

3\. Click **Delete template**.

<img src="https://assets.gcore.pro/docs/reseller-support/fastedge-management/delete-template.png" alt="Template settings menu with delete button highlighted" width="80%">

4\. Confirm your action by clicking **Yes, delete**. 

The template has been successfully removed. 