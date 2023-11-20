---
title: use-a-private-bucket-as-an-origin
displayName: Private origin
published: true
order: 11
toc:
   --1--Overview: "overview"
   --1--Authentication data: "authentication-data"
   --2--Amazon: "amazon-aws-storage"
   --2--Gcore: "gcore-s3-storage"
   --1--Configure: "configure-a-private-bucket-as-an-origin"
   --2--in the control panel: "configure-a-private-origin-in-the-control-panel"
   --2--via the API: "configure-a-private-origin-via-the-api"
pageTitle: Understanding Private Bucket as an Origin | Gcore
pageDescription: A step-by-step guide on how to use a private S3 bucket as an origin for your CDN resource.
---
# Use a private bucket as an origin

## Overview

We have introduced a feature that allows the use of a private bucket inside S3-compatible storage (such as Amazon or others) as a <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol#pull-content-from" target="_blank">CDN resource origin</a>. To grant CDN servers access to content stored in the private bucket, you must specify authentication data (Access Key ID, Secret access key, Hostname, Region). Otherwise, they won’t be able to access the content.

## Authentication data

You can access the necessary authentication data in the personal S3 storage account.

### Amazon AWS storage

You can find the Access Key ID and Secret access key according to the "<a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">AWS Account and Access Keys</a>" guide. 

### Gcore S3 storage

You can find the Hostname and Region in the "Details" section under the <a href="https://storage.gcore.com/storage/list" target="_blank">Storages</a> tab.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/15353064572561.png" alt="Gcore S3 storage">

**Note**: We don’t store the Access Key ID and Secret access key for S3 storage. It is your responsibility to save them after creating the storage.  If you forget them, click **Generate new keys** under the "Details" section. 

## Configure a private bucket as an origin

### Configure a private origin in the control panel

There are two options for configuring a private bucket as an origin:

1. Create an origin group during the CDN resource creation process;
2. Add a group in the "Origins groups" tab and specify this group in the CDN resource setting.

The instructions below are relevant to the first option. The process for the second option is slightly different. 

To configure a private origin: 

1\. Go to the <a href="https://cdn.gcore.com/resources/create/wizard" target="_blank">CDN resource creation page</a>, select "Accelerate and protect only static assets", and click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/image_1460.png" alt="CDN resource creation page" width="50%">

A new page will open. Complete the remaining steps of the manual in the "Origin" section on this page.

2\. Select the **Specify content origin** option.

3\. Select **AWS signature V4** in the "Type of origin authentication" field.

4\. Select the type of S3 storage: **Amazon** or **Other**.

5\. Specify the needed authentication data. It depends on the type of storage selected in the previous step.

  - **For Amazon storage**: Access Key ID, Secret access key, and AWS region
  - **For Other**: Hostname (there's a bucket at the beginning), Access Key ID, Secret access key, and Region

**Note**: To determine the region of your Gcore S3 storage, use the <a href="https://gcore.com/docs/storage/manage-s3-storage/s3-service-urls-and-default-region-names" target="_blank">S3 service URLs and default region names</a> guide.

More information about where to find the keys can be found in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage" target="_blank">Authentication data</a>" section.

6\. Enter the **Bucket name**.

In the example below, we use the private bucket ```test-private``` in S3 Gcore storage with the endpoint (service URL) ```s-ed1.cloud.gcore.lu```. Configure an origin group as follows:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/private-bucket-conf.png" alt="Origin section" width="70%">


7\. Continue the CDN resource creation according to the "<a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Create CDN resource for only static files</a>" guide.

8\. Go to the resource settings and open the Host header option in the "HTTP headers" section. Specify the URL of your storage Hostname (the URL depends on your S3 provider) in the following format: 

- For Gcore S3 storage: ```{bucket-name}.s-ed1.cloud.gcore.lu```
- For most other storages (including Amazon): ```{bucket-name}.s3.{region-code}.{storage-hostname}```

**Note**: The bucket in the "Host header" is very important to specify for the security of the storage data outside the bucket.

Click **Save changes**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/image-3719.png" alt="Save changes">

### Configure a private origin via the API 

Next, we will explain in detail how to specify Private origin via API calls. 


<table>
<tr>
<td>Method</td>
<td>POST</td>
</tr>
<tr>
<td>Header</td>
<td>Bearer <b>{{access_token}}<br><br>
application/json</b></td>
</tr>
<tr>
<td>Payload</td>
<td>
<pre>
{
"name": "YourOriginGroup",
"useNext": true,
"auth_type": "awsSignatureV4",
"auth": {
"s3_type": "amazon",
"s3_access_key_id": "EXAMPLEFODNN7EXAMPLE",
"s3_secret_access_key":
"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
"s3_bucket_name": "bucket_name",
"s3_region": "us-east-2"
 }
}
</pre>
</td>
</tr>
<tr>
<td>Request parameter</td>
<td>For more information, see Gcore’s <a href="https://api.gcore.com/docs/cdn?_gl=1*1vtlv8c*_ga*ODE2MjQ4NzgwLjE2NjY2MDkxMzk.*_ga_Y79HRL8RPR*MTY4NDI0MDAyMC43MjYuMS4xNjg0MjQzNDMyLjYwLjAuMA..#tag/Origins/operation/create_origin_group" target="_blank">API documentation</a></td>
</tr>
<tr>
<td>Response</td>
<td>	
<b>201 Successful<br><br>
400 Request for creation origin group is failed<br><br>
403 Group creation is forbidden</b>
</td>
</tr>
</table>

To access the API and make authenticated requests, <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">generate an access token</a>. You can use a REST tool like cURL or Postman to send the requests. For this guide, we used Postman.

To specify private origin by URL request:

1\. In Postman, open a new request tab.

a. Set the request method to **POST**.

b. Enter the API URL in the request URL field.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/15353579849745.png" alt=" API URL " width="80%">

2\. Go to the **Auth** tab.

a. Select **Bearer Token** from the "Type dropdown".

b. Copy the generated access token and paste it into the "Token" field.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/15353599876753.png" alt="Token" width="80%">

3\. Go to the **Body** tab.

a. Select **raw** as the data type.

b. Select **JSON** from the format dropdown.

c. Enter the payload in the text area. Replace the sample values indicated by ```{{ }}``` with your actual values.

4\. Click **Send**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/15353638607505.png" alt="Send" width="80%">