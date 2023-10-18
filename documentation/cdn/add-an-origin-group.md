---
title: add-an-origin-group
displayName: Origin group
published: true
order: 60
toc:
   --1--Origin groups: "what-is-the-origin-groups-feature"
   --1--Step 1. Add a new origin group: "step-1-add-a-new-origin-group"
   --1--Step 2. Enter the origin group name: "step-2-enter-the-origin-group-name"
   --1--Step 3. Select the type of origin authentication: "step-3-select-the-type-of-origin-authentication"
   --1--Step 4. Configure the origin group: "step-4-configure-the-origin-group"
   --1--Step 5. Save changes: "step-5-save-changes"
   --1--Step 6. Bind the origin group to the CDN resource: "step-6-bind-the-origin-group-to-the-cdn-resource"
   --1--If change the origin group, will the Host header change?: "if-you-change-the-origins-group-will-the-host-header-change"
pageTitle: Guide to Adding an Origin Group to CDN | Gcore
pageDescription: A detailed guide on how to add an origin group to your CDN resource, covering group configuration, origin authentication, and binding process.
---
# Add an origin group

This guide will explain the origin groups feature and show you how to configure and add an origin group to your CDN resource.

## What is the origin groups feature?

Origin groups is a feature that allows you to specify sources for a CDN resource. One origin group can consist of a single site/private bucket or of multiple sites. 

Specifying several sites increases fault tolerance. If one origin fails, another can function as a backup. You can specify a group and set the logic of interaction between origins.

For example, if you make both origins in the group active, requests between them will be distributed 50:50. If you make one source the backup, then that source will respond only when the primary source gives an error 5xx. 


## Step 1. Add a new origin group

You can do this in two ways: in the CDN resource settings or in the "origin groups" section.

<expandable-element title="Option 1. CDN resources">

Open the settings of the desired CDN resource.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960872583313.png" alt="Add a new origin group" width="80%">

Find the "Origin pull protocol" option in the Origin section, and click **Add group**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3515.png" alt="Origin section" width="80%">

Continue to <a href="https://gcore.com/docs/cdn/add-an-origin-group#step-2-enter-the-origin-group-name">Step 2</a>. 

**Note**: The created origin group won’t automatically bind to the CDN resource. Follow the instructions untill the end. 

</expandable-element>

<expandable-element title="Option 2. Origin groups">

Open the "Origin groups" section and click **Add origin group**.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3518.png" alt="Origins groups section" width="80%">

**Note**: The created origin group will appear in the general list of origin groups. It won’t automatically bind to the CDN resource.

</expandable-element>

A pop-up window for group configuration and adding will appear. Perform steps 2–5, regardless of the option chosen above. 

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3519.png" alt="Add origins group" width="80%">

## Step 2. Enter the origin group name

Enter the origin group name into the field. After step 5, the origin group that was created will appear in the list of origins groups and the CDN resource settings.

## Step 3. Select the type of origin authentication

There are two types of origin authentication: None and AWS signature V4. Choose None if your origin from where CDN servers will request content is public, i.e., available to all users on the internet. Choose AWS signature V4 if you want to use a private S3 bucket as an origin.

## Step 4. Configure the origin group

<expandable-element title="Type 1. None">

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3520.png" alt="Configure the origin group" width="50%">

1\. In the "Origin source" field, enter the origin IP or its domain name without "http" or "https://". The CDN will pull content from this source.


2\. (Optional) If your source uses ports other than 80 or 443, disable the **Use default port** toggle and enter the port on the right.

3\. (Optional) If you want to use several sources of content, click **+Add origin** and enter the value. The CDN will determine the origin IPs as separate sources and distribute requests to them according to the round robin algorithm. In other words, the first request will go to the first source, the second request will go to the second source, and so on.

When you have more than one origin in a group, you can adjust the balance between them. To do so:

- Select which origins to enable and disable.
- Select active and backup origins.
- Decide whether to enable the "Use next upstream" option.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3521.png" alt="Use several sources of content" width="80%">

**Enable/disable origin**. By default, the slider next to each origin is in the On position. ‘On’ means that the CDN can pull content from this origin; it has been added to the balance. If you want to disable the content origin in the group, move the slider to Off. You’ll only disable the origin in the current group, but it will continue to work in other groups. CDN requests will stop coming to the disabled origin within fifteen minutes.

**Note**: You can’t disable the last active origin.

**Active/backup origin**. All new origins are automatically assigned an "Active" status. The CDN pulls content from such origins. The balancing between them is determined by the round-robin algorithm. You can turn the active origin into the backup origin by selecting the "Use origin as a backup" option. Backup origins are taken out of balance by default. The CDN requests content from them only if the active origin gives a 5xx response code.

**Use next upstream**. This option only works if each origin contains the same content. When enabled, the CDN will call the following origins on the list if the previous one is unavailable and responds with any 4xx or 5xx series response code, except 400. Code 400 is an exception. In this case, the CDN won’t redirect requests to another source. If all origins are unavailable, the CDN will show the response of the last one in the list.

At first glance, the interaction between the active/backup origins and the "Use next upstream" option may seem complicated, so to make it easier to understand, let’s look at examples of how it works.

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

<expandable-element title="Type 2. AWS signature V4">

Read about this type of origin in our article about <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin" target="_blank">using a private bucket as an origin</a>.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/image3522.png" alt="Using a private bucket as an origin" width="80%">

1\. Select the type of S3 storage: Amazon or Other.

2\. Specify the required authentication data. It depends on the type of storage selected in the previous step.

- For Amazon storage: Access Key ID, Secret access key, and AWS region
- For Other: Hostname, Access Key ID, Secret access key, and Region

3\. Enter the **Bucket name**.

**Note**: If you selected **Amazon S3 storage** in step #1, go to the next step. If you selected **Other**, go to the resource settings and open the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Host header</a> option in the "HTTP headers" section. Specify the URL of your storage Hostname (the URL depends on your S3 provider) in the following format:

- For Gcore S3 storage: ```s-ed1.cloud.gcore.lu```
- For most other storages: ```s3.{region-code}.{storage hostname}```

Don’t forget to save the changes.

</expandable-element>

## Step 5. Save changes

Click **Add group** to save changes.

## Step 6. Bind the origin group to the CDN resource

To bind a created group to the CDN resource, open the required CDN resource settings, and go to the Origin section. Then, click the **ᐯ** symbol, and select the created group from the drop-down list. Next, click **Save changes**.

## If you change the origins group, will the Host header change?

No. If you switch the CDN resource from one origins group to another, the Host header won’t automatically change. You’ll have to do it manually.