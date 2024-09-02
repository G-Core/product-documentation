---
title: api-discovery
displayName: API discovery
published: true
order: 20
pageTitle: Learn about Gcore API discovery | Gcore
pageDescription: Learn about Gcore API discovery measures.
---
# API discovery

API Discovery allows you to manage and protect REST API endpoints associated with your domain, including legacy and shadow APIs.  

This feature scans your domain's traffic and presents a compiled list of APIs for your validation so you can decide which endpoints require WAAP protection. You can also add endpoints manually or import them in a Swagger file. 

<alert-element type="info" title="Info">
 
The API Discovery feature is included in the <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise</a> package. 

</alert-element>

## Overview 

API Discovery covers both public and private REST APIs. Public APIs are available to anyone, while private APIs are only accessible to authorized users.  

<alert-element type="tip" title="Tip">
 
If API Discovery isn't available in your plan and you can't automatically map APIs with API Baseline, use the <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-base-path" target="_blank">API base path</a> feature. It lets you manually add API paths that belong to your domain and should be protected by WAAP.
 
</alert-element>

To access the feature: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/api-discovery-and-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page. 

3\. In the sidebar, click **API Discovery**.

You can protect and manage APIs on the following pages: 

* **API Baseline**: Contains all API endpoints protected by WAAP. On this page you can add, edit, and view your APIs. 

* **Potential APIs**: Endpoints that have been auto-detected by the system and require verification. This is where you can reject or approve endpoints as valid APIs. 

* **Scan History**: A list of all endpoints that have been discovered by the system or detected in the uploaded Swagger file. Here you can view detailed scan results. 

* **Settings**: A page with available configuration and customization options where you can set up scan settings, configure <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-base-path" target="_blank">API base URL</a>, and upload a Swagger file. 

The functionality on these pages is described in more detail in the following sections. 

## Statuses of scanned endpoints 

Each API endpoint can have a specific status. This status reflects the results of a system scan or Swagger file check: 

* **Potential**: The endpoint has been added to the system through a network scan and is awaiting to be marked as a confirmed API or not an API. If you confirm the endpoint, it’ll appear on the **API Baseline** page along with other APIs and will automatically get the **Confirmed** status.  

* **Confirmed**: The endpoint is a valid API and should be protected by WAAP. If you manually add the endpoint in the <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-base-path" target="_blank">API base path</a>, it’ll automatically get this status. You can change the status at any time. 

* **Not an API**: The potential endpoint is not a valid API and doesn’t require protection. You can manually assign this status to endpoints that were falsely detected during a network scan. 

* **Delisted**: The endpoint was originally detected in the Swagger file, but it’s subsequently missing after a later Swagger scan. 

## API Baseline 

All your protected API endpoints are listed on this page. Here, you can do the following: 

* Manually add endpoints that should be protected by WAAP 

* Group endpoint using tags to manage access to your APIs 

### Add endpoints to API Baseline 

If you manually add APIs on the **API Baseline** page, they will automatically get the confirmed status. You can change the status at any time. 

To add a new API endpoint: 

1\. In the top-right corner of the screen, click **Add an API**. This will open up a menu with the required settings on the right side of the page. 

2\. Configure your APIs as follows: 

 * **Scheme**: Choose the relevant scheme – HTTP or HTTPS. 
 * **Method**: Provide the relevant API method. 
 * **Endpoint**: Enter a full path to the endpoint. 
 * **Version** (optional): To maintain API efficiently and consistently, you can establish an API versioning to keep track of API changes, relevant fixes, or deprecations.  
 * **API group** (optional): Organize endpoints into related groups. 
 * **Tags**: Configure access to your endpoints. Add reserved tags to set up advanced API protection.

3\. Click **Add** to save the changes. 

### Group endpoints based on tags 

You can categorize endpoints by marking them with reserved tags and then create custom rules to specifically protect those tagged endpoints.  

For example, you can mark certain APIs with the **Indicate API Privileged User** or **Indicate API Admin User** tags to make those paths accessible only to privileged or admin users. Refer to our <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-access-with-reserved-tags" target="_blank">configure API access with reserved tags</a> guide for instructions. 

### View endpoints 

To inspect existing APIs in more detail or modify endpoint status, API groups, or associated tags: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**. 

2\. Find the domain where you want to configure APIs and click the domain name to open it. 

3\. In the sidebar menu, click **API Discovery**. You’ll be directed to the **API Baseline** page. 

4\. Find the endpoint you want to inspect and click the three-dot icon next to it. 

5\. Select **View details**. 

6\. On the page that opens, you can check additional information about your existing endpoint or change endpoint status, API groups, and tags.

7\. If you made any changes, click **Save** to apply them. Otherwise, close the menu. 

### Edit endpoints

If you want to update the actual endpoint path, you can do it as follows: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**. 

2\. Find the domain where you want to modify APIs and click the domain name to open it. 

3\. In the sidebar menu, click **API Discovery**. You’ll be directed to the **API Baseline** page. 

4\. Find the endpoint you want to edit and click the three-dot icon next to it. 

5\. Enter a new or updated path. 

When editing a path, you can use curly braces to signify query string parameters. For example, `/api/v1/stacks/{stack_id}/sites/{site_id}`. 

## Potential APIs 

When the API Discovery feature performs a network scan, all detected endpoints appear on this page. Here, you can manage their status and determine whether or not they are confirmed APIs. 

### Verify detected endpoints

After you identify the endpoint as a confirmed API, it will be moved to the API Baseline page. All rejected APIs will be removed from the system.

## Scan history 

This page lists all endpoints identified by the system: 

* Via automated network scan. The default scan frequency is set to 24 hours, but you can adjust it on the **Settings** page.  

* From the uploaded Swagger file (if you added it to the Settings page).

The scan history also displays information about the scan time, analyzed source, and whether a scan was successful or resulted in errors. You’ll see information about the scan process and any related errors in the **Message** column. 

## Settings

On this page, you can choose the preferred ways of detecting potential API endpoints, configure network scan intervals, and manually add APIs to the base path.

### Configure base path 

For guidelines on how to configure API base path in Gcore WAAP, check out the <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-base-path" target="_blank">Manually add endpoints to API base path</a> guide. 

### Specify API specification files 

One of the ways to add APIs to API Discovery feature is to parse an uploaded JSON or YAML Swagger file. Detected API endpoints will appear on thewa page with the **Confirmed** status. 

Uploading a Swagger file can significantly reduce the work needed for categorizing of potential APIs, as this will automatically classify most of the endpoints that comprise the API Baseline. 

This is how you can do it: 

1\. On the **Settings** page, navigate to the **API specifications file** section. 

2\. Choose the preferred method for adding APIs: 

 * **Path**: Provide a URL to the Swagger file
 * **Upload**: Import locally stored Swagger file

3\. Click **Start Swagger scan**. This will trigger a scan of the listed paths or files for APIs.  
Once the scan is complete, potential endpoints will be added to the **API Baseline** page.     

## Set up scan settings 

In this section, you can choose how the system will detect your APIs: 

* **Network scans**. When this toggle is enabled, API Discovery will automatically scan your site's URLs and detect new potential API endpoints. 

* **API specification scans**. When this toggle is enabled, API Discovery will scan your uploaded API Specification file or specified API paths to see if any new endpoints were added or if any existing endpoints were removed (delisted).

You can customize scan intervals by selecting the relevant option from the **Scan every** dropdown. 