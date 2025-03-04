---
title: manage-apps
displayName: Manage FastEdge apps
published: true
order: 30
toc:
   --1--Stop or start an application: "stop-or-start-an-application"
   --1--View and enable logging: "view-and-enable-logging"
   --1--Add and update parameters: "add-and-update-parameters"
pageTitle: A guide on managing FastEdge applications | Gcore
pageDescription: Learn how to manage FastEdge CDN and HTTP applications.
---
# Manage FastEdge apps

You can view and manage your HTTP and CDN applications on the application management page:

<img src="https://assets.gcore.pro/docs/fastedge/manage-apps/app-management-page-annotated.png" alt="FastEdge applications page" width="80%">

* **Actions**: Perform quick actions, such as stopping or starting an application, editing its configuration, or deleting the application from the Customer Portal.

* **Template name**: If the application was created from a template, check the template and its configuration.

* **Metrics**: Check response statuses for requests to the FastEdge servers and analyze runtime duration data.

* **Logs**: View and enable application logs.

* **Parameters**: Update or add application parameters.

To open the application management page:

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a> , navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**.

2\. On the **Applications** page, click the three-dot icon next to the application you want to configure. 

3\. Select **Manage**.

<img src="https://assets.gcore.pro/docs/fastedge/manage-apps/manage-apps-menu.png" alt="FastEdge applications page" width="80%">

4\. Check and update your application’s configuration as required.  

## Stop or start an application 

You can change the running state of your application and decide if you want to have it running and processing requests, or stopped. The latter might be useful if you need to update the application’s configuration or want to upload a new version of the application's binary file. 

An application can be stopped for the following reasons: 

* You manually stopped it, as described in the following instructions. You can restart the application at any time. 

* Payment for the product was unsuccessful. In this case, the application cannot be reactivated until payment is completed. 

To manually stop or activate the application: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a> , navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Applications** page, click the three-dot icon next to the application you want to configure.

3\. Select **Manage**.

4\. Click **Actions** and choose the relevant one: **Stop** or **Start**.

<img src="https://assets.gcore.pro/docs/fastedge/manage-apps/stop-app.png" alt="FastEdge applications page" width="80%">

The application status will be changed respectively.

## View and enable logging

If you want to record logs for your FastEdge application, make sure that you have the **Enable logging toggle** enabled.

<img src="https://assets.gcore.pro/docs/fastedge/manage-apps/view-logging.png" alt="FastEdge appl page with logging tab open" width="80%">

By default, FastEdge applications don't generate logs. After you turn on the Enable logging toggle, the application will record logs for 30 minutes. You can monitor the remaining logging time by checking the countdown next to the toggle.

After 30 minutes, logging will stop, and the application will revert to its default no-logging state. To start logging, enable the toggle again.

You can filter log data according to the following criteria:

* **Timestamp**. Choose the date and time when the logs have been recorded. By default, the table displays data for the past hour.

* **Client IP address**. View logs collected for a particular IP.

* **Edge name**. Seach within the **Logs** column.

## Add and update parameters

On the **Parameters** tab, you can update or enhance the functionality of your application by adding or modifying HTTP response headers and environment variables. 

For example, the following screenshots illustrate the configuration for a geo-location application. Environment variables are set based on the geo-IP of the client making the request. With this configuration, users will view different versions of a website based on their location.

<img src="https://assets.gcore.pro/docs/fastedge/manage-apps/app-params-sample.png" alt="FastEdge applications page" width="80%">

<alert-element type="tip" title="Tip">
By using <a href="https://g-core.github.io/FastEdge-sdk-js/reference/fastedge-env/" target="_blank">FastEdge SDK</a>, you can configure these variables according to your use cases.
</alert-element>
