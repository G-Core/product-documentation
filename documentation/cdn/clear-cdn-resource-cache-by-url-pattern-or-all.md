---
title: clear-cdn-resource-cache-by-url-pattern-or-all
displayName: Purge
published: true
order: 80
toc:
   --1--Configure in the Customer Portal: "configure-purge-in-the-customer-portal"
   --2--Purge by URL: "purge-by-url"
   --2--Purge all: "purge-all"
   --2--Purge by pattern: "purge-by-pattern"
   --1--Configure via API: "configure-purge-via-api"
   --1--Purge history: "view-purge-history"
pageTitle: How to Clear CDN Resource Cache by URL, Pattern, or All and Check Purge History | Gcore
pageDescription: A guide on how to clear the cache in one of three ways—for the whole CDN resource, by pattern, or by URL.
---
# Clear CDN resource cache by URL, pattern, or all and check Purge history 

<a href="https://cdn.gcore.com/purge/purge-request" target="_blank">Purge</a> is an option that allows clearing the CDN resource cache. Using Purge is helpful if you update the content on your origin and don’t want to wait until the content is updated on CDN servers naturally because it takes time. After Purge is applied, the outdated CDN server’s cache will disappear. Additionally, the option assists if your end-users receive incorrect content of your website data from CDN servers.

We provide three options for cache clearing:

1. **Purge by URL (recommended)** to remove content that belongs to a particular URL from the cache without impacting other cached items.
2. **Purge all** to remove all data from the cache.  
3. **Purge by pattern** to remove content selectively by specifying path patterns with the operator that can replace any number of symbols.  

There are two ways to clear the cache: via API (use the <a href="https://api.gcore.com/docs/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post" target="_blank">API documentation</a> to get more information about the request) and in the Customer Portal.

## Configure Purge in the Customer Portal

1\. Go to the <a href="https://cdn.gcore.com/purge/purge-request" target="_blank">Purge request</a> section.

A new page will open. Perform the remaining steps there.

2\. Select the relevant CDN resource from the dropdown menu.

3\. Select the desired purge type and follow the instructions below (by URL, all, or by pattern).

4\. Click the **Purge** button.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/purge-section-overview.png" alt="Purge section overview" width="80%">

<tabset-element>

### Purge by URL

<alert-element type="warning" title="Warning">

You can make two purge requests per resource per minute. One purge request is limited to 100 URLs. Therefore, you can remove up to 200 files from the cache per minute.

</alert-element>

In the text area, specify one or more content URLs to purge, entering one URL per line. Links must:

- Start with a slash (/).
- Not include a protocol, domain name, or wildcard (*).
- Include query strings if the CDN resource cache is configured to consider the query string.

For example, to purge the file ```https://www.example.com/pictures/icon.jpg?size=small```, specify ```/pictures/icon.jpg?size=small```.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339546960145.png" alt="Purge by URL" width="80%">

We recommend avoiding this method and instead using other types of Purge in the following cases:

- **Your origin contains a Vary HTTP response header**. When you use Purge by URL, it will delete only one version of the file.
- **Large file delivery optimization is enabled**. When you update several files in origin without clearing the CDN cache, Purge by URL will delete only the first slice (with bytes=0…).

The configuration of Purge by URL also depends on the settings in the Ignore Query string option:

- If the value is "Ignore All", don’t specify parameters in the Purge request.
- If the value is "Ignore All Except", only files with the parameters listed in the option will be cached as different objects. Files with other parameters will be cached as one object. In this case, specify the listed parameters in any order in the Purge request. Other parameters shouldn’t be specified.
- If the value is "Ignore Only", files with the parameters listed in the option will be cached as one object. Files with other parameters will be cached as different objects. In this case, specify other parameters (if any) besides the ones listed in any order in the Purge request.

### Purge all

<alert-element type="warning" title="Warning">

You can make one purge request per resource per minute.

</alert-element>

<alert-element type="warning" title="Warning">

Purging all files from the cache will cause a significant load on your server as CDN servers will pull all files from the origin. Therefore, if you have a large amount of content, we recommend using Purge by URL or pattern.

</alert-element>

To purge all files from the cache, select the "Purge All" option and click the **Purge** button.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339549617041.png" alt="Purge all" width="80%">

### Purge by pattern

<alert-element type="warning" title="Warning">

You can make one purge request per resource per minute. One purge request is limited to 10 patterns.

</alert-element>

To purge files by pattern, specify the path to the file you want to purge or a path pattern without a domain name in the input line. Use the * operator, which replaces any number of symbols in your path. You can use several * operators in one request. A path must start with / or * and each path must be on a separate line. 

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339551969425.png" alt="Purge by pattern" width="80%">

If you don’t specify a query string, files with all the possible query string parameters will be purged from the cache according to the path pattern.

Several types of patterns are available:

<table>
<thead>
<tr>
<td><b>Type and explanation</b></td>
<td><b>Purge target</b></td>
<td><b>Purge pattern</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><b>1. Purge the selected file</b><br><br>Specify a file path without a domain name.<br> As a result, all files at cdn.site/static/image.jpg<br>will be purged, including files with query string <i>.jpg?VERSION</i><br><br>If you only want to purge a selected file with a query string, specify it in the file path: /static/image.jpg?VERSION</td>
<td style="text-align: left">cdn.site/static/image.jpg</td>
<td style="text-align: left">/static/image.jpg</td>
</tr>
<tr>
<td style="text-align: left"><b>2. Purge the group of files from one folder</b><br><br>Input pattern without a domain name and * operator: /statiс/* </td>
<td style="text-align: left">cdn.site/static</td>
<td style="text-align: left">/statiс/*</td>
</tr>
<tr>
<td style="text-align: left"><b>3. Purge the group of files with a certain type</b><br><br>Input the * operator and the file name extension .jpg<br>As a result, all the jpg files will be purged, including files with the query string <i>.jpg?VERSION</i></td>
<td style="text-align: left">cdn.site/*.jpg</td>
<td style="text-align: left">*.jpg</td>
</tr>
<tr>
<td style="text-align: left"><b>4. Purge the group of files having a common folder in the path</b><br><br>Input path pattern without a domain name and use the <i>*</i> operator twice</td>
<td style="text-align: left">cdn.site/*/static/*</td>
<td style="text-align: left">*/static/*</td>
</tr>
<tr>
<td style="text-align: left"><b>5. Purge the group of files with a certain type having a common folder in the path</b><br><br>Input path pattern with the <i>*</i> operator</td>
<td style="text-align: left">cdn.site/*/static/*.jpg</td>
<td style="text-align: left">*/static/*.jpg</td>
</tr>
</tbody>
</table>

</tabset-element>

## Configure Purge via API

We will explain in detail how to do "Purge by URL" via API calls. Examples of other Purge types (all and by pattern) can be found in the <a href="https://api.gcore.com/docs/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post" target="_blank">API documentation</a>. 

<expandable-element title="API request details">

<table>
<tbody>
<tr>
<td style="text-align: left">Method</td>
<td style="text-align: left">POST</td>
</tr>
<tr>
<td style="text-align: left">URL</td>
<td style="text-align: left">https://api.gcore.com/cdn/resources/{{resource_id}}/purge</td>
</tr>
<tr>
<td style="text-align: left">URL parameter</td>
<td style="text-align: left">resource_id<br />ID of the CDN resource that the content to purge belongs to</td>
</tr>
<tr>
<td style="text-align: left">Header</td>
<td style="text-align: left">Bearer {{access_token}}<br />application/json</td>
</tr>
<tr>
<td style="text-align: left">Payload</td>
<td style="text-align: left">
<p>1. Purge by URL:</p>
<p>{ <br /> "urls": [ <br /> "/example1.jpg", <br /> "/img/example2.png", <br /> "/style.css?ver=2.0" <br /> ] <br />}</p>
<p>2.&nbsp;Purge all:</p>

<p>{</p>
<p>"paths": [ ]<br />}</p>

<p>3. Purge by pattern:</p>

<p>{<br />"paths": [<br />"/images/*"<br />]<br />}</p>
</td>
</tr>
<tr>
<td style="text-align: left">Request parameter </td>
<td style="text-align: left">
<p>paths</p>
<p>1. Purge by URL:</p>
<p>(required, string) An array of one or more content URLs to purge</p>
<p>2. Purge all:</p>
<p>An empty array.</p>
<p>3. Purge by pattern:</p>
<p>(required, string) An array of one or more content patterns started with * or / symbols.</p>
</td>
</tr>
<tr>
<td style="text-align: left">Response</td>
<td style="text-align: left">
<p><strong>201 Created<br /></strong>Returns an array of the purged URLs</p>
<p><strong>400 Bad Request<br /></strong>The user has exceeded the URL quota</p>
<p><strong>401 Unauthorized<br /></strong>The user does not have the correct authentication credentials</p>
<p><strong>429 Too many requests<br /></strong>The user has exceeded the request quota</p>
</td>
</tr>
</tbody>
</table>

</expandable-element>

To access the API and make authenticated requests, <a href="https://api.gcore.com/docs/account" target="_blank">generate an access token</a>. You can use a REST tool like cURL or Postman to send the requests. For this guide, we used Postman.

To send a purge by URL request:

1\. In Postman, open a new request tab, then do the following:

a. Set the request method to *POST*.

b. Enter the resource URL in the request URL field. Replace **{{resource_id}}** with your actual value.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339834314641.png" alt="New request tab in Postman" width="80%">

2\. Go to the **Authorization** tab and do the following:

a. Select *Bearer Token* from the **Type** dropdown.

b. Copy the generated access token and paste it into the **Token** field.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339852303249.png" alt="Authorization" width="80%">

3\. Go to the Body tab and do the following:

a. Select *raw* as the data type.

b. Select *JSON* from the format dropdown.

c. Enter the payload in the text area. Replace the sample values indicated by {{ }} with your actual values.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339837932177.png" alt="Body tab" width="80%">

4\. Click Send.

If the purge is successful, you will receive an HTTP 201 and a response message that contains a list of purged URLs.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339892700945.png" alt="purge is successful" width="80%">

If an error occurs with the request, the API will return a status code and a body that contains a description of what caused the error. Here is an example: 

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339878706961.png" alt="error occurs" width="80%">

## View Purge history

<alert-element type="info" title="Info">

This feature is currently in beta.

</alert-element>

“Purge history” is the section where you can check the status of your purge requests. 

**Note:** We've been keeping a history of purge requests for only one month. 

To view the history, navigate to the <a href="https://cdn.gcore.com/purge/purge-history" target="_blank">Purge history</a> page. The page will display all existing requests.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/purge-history.png" alt="Purge history section" width="80%">

You can use filters to display individual reports: 

- **Search by CNAME.** Specify the CNAME of the desired CDN resource.
- **Type.** Select the needed type of Purge (Purge by URL, Purge all, or Purge by pattern).
- **Status.** Select the desired status (In progress, Success, Failed).
- **Date.** Set the time period for the queries to be displayed (up to one month).

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/purge-history-overview.png" alt="Purge history section explanation" width="80%">
