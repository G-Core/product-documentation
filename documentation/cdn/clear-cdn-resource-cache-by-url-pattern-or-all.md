---
title: clear-cdn-resource-cache-by-url-pattern-or-all
displayName: Purge
published: true
order: 80
toc:
   --1--About Purge: "about-purge"
   --1--Configure in the Control Panel: "configure-the-purge-option"
   --2--Purge by URL: "purge-by-url"
   --2--Purge all: "purge-all"
   --2--Purge by pattern: "purge-by-pattern"
   --1--Configure via API: "configure-purge-via-api"
pageTitle: Understanding of the Purge option for cache clearance | Gcore
pageDescription: A guide on how to clear the cache in one of three ways—for the whole CDN resource, by pattern, or by URL.
---
# Clear CDN resource cache by URL, pattern or all 

## About Purge 

<a href="https://cdn.gcore.com/purge" target="_blank">Purge</a> is an option that allows clearing the CDN resource cache. Using Purge is helpful if you update the content on your origin and don’t want to wait until the content is updated on CDN servers naturally because it takes time. After Purge is applied, the outdated CDN server’s cache will disappear. Additionally, the option assists if your end-users receive incorrect content of your website data from CDN servers.

We provide three options for cache clearing:

1. **Purge by URL (recommended)** to remove content that belongs to a particular URL from the cache without impacting other cached items.
2. **Purge all** to remove all data from the cache.  
3. **Purge by pattern** to remove content selectively by specifying path patterns with the operator that can replace any number of symbols.  

There are two ways to clear the cache: via API (use the <a href="https://api.gcore.com/docs/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post" target="_blank">API documentation</a> to get more information about the request) and in the Control Panel.

## Configure the Purge option

1\. Go to the <a href="https://cdn.gcore.com/purge" target="_blank">Purge</a> section.

A new page opens. Do the remaining steps there.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339545400209.png" alt="Configure the Purge option" width="80%">

2\. Select the CDN resource from the dropdown menu to which the content to purge belongs.

3\. Select the purging type and follow the appropriate instructions below (by URL, all, or by pattern) to manage purge.

4\. Click the **Purge** button.

### Purge by URL

**Note**: You can make two purge requests for a resource per minute. One purge request is limited to 100 URLs. It means you can remove only 200 files from the cache in a minute.

In the text area, specify one or more content URLs to purge, entering one URL per line. Make sure to follow the URL requirements. Links must:

- Start with a slash (/).
- Not include a protocol, domain name, or wildcard (*).
- Include query strings if the CDN resource cache is configured to consider the query string.

For example, to purge the file ```https://www.example.com/pictures/icon.jpg?size=small```, specify the following: */pictures/icon.jpg?size=small*.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339546960145.png" alt="Purge by URL" width="80%">

We recommend using other types of Purge in the following cases:

- **If your origin contains a Vary HTTP response header**. When you use Purge by URL, it will delete only one version of the file.
- **If Large file delivery optimization is enabled**. When you update several files in origin without clearing the CDN cache, Purge by URL will delete only the first slice (with bytes=0…).

The configuration of Purge by URL also depends on the settings in the Ignore Query string option:

- If the value is "Ignore All", don’t specify parameters in the Purge request.
- If the value is "Ignore All Except", only files with the parameters listed in the option will be cached as different objects. Files with other parameters will be cached as one object. In this case, specify the listed parameters in any order in the Purge request. Other parameters shouldn’t be specified.
- If the value is "Ignore Only", files with the parameters listed in the option will be cached as one object. Files with other parameters will be cached as different objects. In this case, specify other parameters (if any) besides the ones listed in any order in the Purge request.

### Purge all

**Note**: You can make one purge request for a resource per minute.

To purge all files from the cache, select the "Purge All" option and click the **Purge** button.

<img src="https://assets.gcore.pro/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all/14339549617041.png" alt="Purge all" width="80%">

Please note that purging all files from the cache will cause a significant load on your server as CDN servers will pull all files from the origin. Therefore, if you have a large amount of content, we recommend using Purge by URL or pattern.

### Purge by pattern

**Note**: You can make one purge request for a resource per minute. One purge request is limited to 10 patterns.

To purge files by pattern, specify the path to the file you want to purge or a path pattern without a domain name in the input line. Use the * operator, which replaces any number of symbols in your path (you can use several * operators in one request). A path must start with the / or the * symbols and each path must be on a separate line. 

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
<td style="text-align: left"><b>1. Purge the selected file</b><br><br>Specify a file path without a domain name.<br> As a result, all files at <i>cdn.site/static/image.jpg</i><br>will be purged,<br> including files with query string <i>.jpg?VERSION</i><br><br>If you want to purge only a selected file with a query string, specify it in the file path: <i>/static/image.jpg?VERSION</i></td>
<td style="text-align: left">cdn.site/static/image.jpg</td>
<td style="text-align: left">/static/image.jpg</td>
</tr>
<tr>
<td style="text-align: left"><b>2. Purge the group of files from one folder</b><br><br>Input pattern without a domain name and <i>*</i> operator: <i>/statiс/*</i> </td>
<td style="text-align: left">cdn.site/static</td>
<td style="text-align: left">/statiс/*</td>
</tr>
<tr>
<td style="text-align: left"><b>3. Purge the group of files with a certain type</b><br><br>Input the <i>*</i> operator and the file name extension <i>.jpg</i><br>As a result, all the jpg files will be purged,<br> including files with the query string <i>.jpg?VERSION</i></td>
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

## Configure Purge via API

We will explain in detail how to do "Purge by URL" via API calls. Examples of other Purge types (all and by pattern) can be found in the <a href="https://api.gcore.com/docs/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post" target="_blank">API documentation</a>. 

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