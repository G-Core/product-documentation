---
title: add-an-origin-group
displayName: Origin group
published: true
order: 60
toc:
   --1--Origin groups: "what-is-the-origin-groups-feature"
   --1--Step 1. Add a new origin group: "step-1-add-a-new-origin-group"
   --1--Step 2. Enter the origin group name: "step-2-enter-the-origin-group-name"
   --1--Step 3. Configure the origin group: "step-3-configure-the-origin-group"
   --1--Step 4. Save changes: "step-4-save-changes"
   --1--Step 5. Connect the origin group to the CDN resource: "step-5-connect-the-origin-group-to-the-cdn-resource"
pageTitle: Guide to adding an origin group to CDN | Gcore
pageDescription: A detailed guide on how to add an origin group to your CDN resource, covering group configuration, origin authentication, and binding process.
---
# Add an origin group to a CDN resource

This guide will explain the origin groups feature and show you how to configure and add an origin group to your CDN resource.

## What is the origin groups feature?

Origin groups is a feature that allows you to specify sources for a CDN resource. One origin group can consist of a single site/private bucket or of multiple sites. 

Specifying several sites increases fault tolerance. If one origin fails, another can function as a backup. You can specify a group and set the logic of interaction between origins.

For example, if you make both origins in the group active, requests between them will be distributed 50:50. If you make one source the backup, then that source will respond only when the primary source gives an error 5xx. 

## Step 1. Add a new origin group

You can do this in several ways: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files#step-1-start-creation" target="_blank">during CDN resource creation</a>, in the settings of an existing resource, or on the **Origin groups** page. 

<tabset-element>

### In resource settings

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN**. You’ll be directed to the **CDN resources** page. 

2\. Find the resource where you want to add a new origin group and click the CNAME to open its settings.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/cdn-resource-name-no-waap.png" alt="Resource name highlighted" width="80%">

3\. Scroll down to the **Origin pull protocol** section.

4\. Click **Add group** and proceed with the configuration as described in Step 2. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/add-group-resource-settings.png" alt="Choose a new origin group in resource settings" width="80%">

### On the Origin groups page 

If you add a group from the **Origin groups** page, the created group won’t be automatically added to a CDN resource. You’ll need to <a href="" target="_blank">manually add a group to the resource</a>. 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN** > **Origin groups**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/origin-groups-page.png" alt="Choose a new origin group in resource settings" width="80%">

2\. Click **Add origin group** and proceed with the configuration as described in Step 2. 

</tabset-element>

## Step 2. Enter the origin group name

Enter a unique name of a group. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/origin-group-name.png" alt="Choose a new origin group in resource settings" width="80%">

## Step 3. Configure the origin group

You can choose AWS signature V4 origin authentication or select none for the public origins without authentication. 

### With S3 authentication

If you want to use AWS signature authentication, choose your storage type and proceed with the relevant instructions. 

<tabset-element>

#### Amazon S3 storage 

1\. Specify your access key ID. In your Amazon personal account, it's called "AWS access key ID". For details on how to find your key ID, check the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">official Amazon guide</a>.  

2\. Specify your secret access key. In your Amazon account, it's called "AWS secret access key". For details on how to find your access key, check the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">official Amazon guide</a>. 

3\. Choose your AWS region—the location of a server where your storage is hosted. 

4\. Enter your S3 bucket name. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/aws-authentication.png" alt="Amazon S3 authentication for a new origin" width="80%">

#### Other storage

1\. Specify a hostname—a name that's assigned to a storage server within a network and is used instead of an IP address. 

2\. Specify your access key ID.  

3\. Specify your secret access key.  

4\. Specify a region—location ID of a server where your storage is hosted.  

5\. Enter your S3 bucket name. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/other-authentication.png" alt="Amazon S3 authentication for a new origin" width="80%">

</tabset-element>

### With no authentication

1\. In the origin source field, enter the origin IP or its domain name without `http` or `https://`. The CDN will pull content from this source. 

   <img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/no-auth-origin-source.png" alt="Amazon S3 authentication for a new origin" width="80%">

2\. (Optional) If your source uses ports other than 80 or 443, disable the **Use default port** toggle and enter the port on the right. 

3\. (Optional) If you want to use several sources of content, click **+Add origin** and enter the value. The CDN will determine the origin IPs as separate sources and distribute requests to them according to the round robin algorithm. In other words, the first request will go to the first source, the second request will go to the second source, and so on. 

<expandable-element title="Set up multiple origins">

When you have more than one origin in a group, you can adjust the balance between them. To do so: 

* Select which origins to enable and disable. 

* Select active and backup origins. 

Decide whether to enable the **Use next upstream** option.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/multiple-origins.png" alt="Amazon S3 authentication for a new origin" width="80%">

</expandable-element>

<expandable-element title="Enable or disable an origin">

Each origin has the **On** toggle enabled by default. This means that CDN can pull content from this origin and it has been added to the balance.  

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/enable-origin-toggle.png" alt="Amazon S3 authentication for a new origin" width="80%">

If you want to disable the content origin in the group, disable the toggle so it changes to **Off**. Note that this will only disable the origin in the current group, but the origin will continue to work in other groups.  

CDN requests will stop coming to the disabled origin within fifteen minutes.  

<alert-element type="info" title="Info">
 
You can’t disable the last active origin.
 
</alert-element>

</expandable-element>

<expandable-element title="Activate origin or use it as backup">

All new origins are automatically assigned an **Active** status. The CDN pulls content from such origins. The balancing between them is determined by the round-robin algorithm.  

You can turn the active origin into the backup origin by selecting the **Use origin as a backup** option.  

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/use-origin-as-backup.png" alt="Amazon S3 authentication for a new origin" width="80%">

Backup origins are taken out of balance by default. The CDN requests content from them only if the active origin gives a 5xx response code. 

</expandable-element>

<expandable-element title="Use next upstream">

This option only works if each origin has the same content. When enabled, the CDN will call the following origins on the list if the previous one is unavailable and respond with any 4xx or 5xx series response code. 

Code 400 is an exception. In this case, the CDN won’t redirect requests to another source. If all origins are unavailable, the CDN will show the response of the last one in the list. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/use-next-upstream.png" alt="Amazon S3 authentication for a new origin" width="80%">

At first glance, the interaction between the active/backup origins and the **Use next upstream** option may seem complicated, so to make it easier to understand, let’s look at examples of how it works.

<table>
<thead>
<tr>
<td><b>Case</b></td>
<td><b>How the CDN requests content</b></td>
</tr>
</thead>
<tbody>
<tr>
<td>The "Use next upstream" option is disabled; all origins are active.</td>
<td>If the active origin responds with an error, the CDN will hand it off to the end user.</td>
</tr>
<tr>
<td>The "Use next upstream" option is enabled. One origin is active, and the rest are backups.</td>
<td>If the active origin responds with 4xx and 5xx response codes, the CDN will start requesting content from the other origins, moving down the list.</td>
</tr>
<tr>
<td>The "Use next upstream" option is enabled. All origins are active.</td>
<td>If the first active origin responds with 404, 500, 502, 503, or 504 response codes, the CDN will start requesting content from the other origins, moving down the list.</td>
</tr>
<tr>
<td>The "Use next upstream" option is disabled. One origin is active, and the rest are backups.</td>
<td>If the active origin doesn’t respond within 5 seconds or responds with a 5xx response code, the CDN will request content from the backup origin. If the active origin responds with a 4xx response code, the CDN won’t request the backup origin and will send an error message to the user.</td>
</tr>
</tbody>
</table>

</expandable-element>

## Step 4. Save changes

Click **Add group** to save changes.

## Step 5. Connect the origin group to the CDN resource

<alert-element type="info" title="Info">
 
If you change an origin group for a CDN resource, the Host header will not automatically change. You’ll have to <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header#how-to-manage-the-host-header" target="_blank">update it manually</a>.
 
</alert-element>

To add a created group to the CDN resource: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN**. You’ll be directed to the **CDN resources** page. 

2\. Find the resource where you want to add a new origin group and click the CNAME to open its settings. 

3\. Navigate to the **Origin** section. 

4\. Choose the relevant group from the Origin group dropdown and click **Add group**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/add-group-resource-settings.png" alt="Amazon S3 authentication for a new origin" width="80%">

5\. Click **Save changes**.