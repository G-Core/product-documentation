---
title: cdn-dns-1
documentName: CDN & DNS 1
description: description
published: true
---

Heading H1:
# Main Heading 

Heading H2:
## Smaller Heading

Heading H3:
### Another small Heading

Heading H4:
#### Another small Heading

Heading H5:
##### And even that's one 

Heading H6:
###### The smallest heading

Text:

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 

Bold:

**Lorem ipsum**

Italic:

*dolor sit amet*

Italic inside Bold:

**consectetur _adipiscing_ elit**

Italic and Bold:

***sed do eiusmod tempor***

Strikethrough:

 ~~Lorem ipsum dolor sit amet~~

Subscript, superscript: 

<sub>consectetur adipiscing</sub> <sup>eiusmod tempor</sup> 

String Quote: 

> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Phrase Quote:

Lorem ipsum dolor `sit amet`, consectetur adipiscing elit.

Code:

Lorem ipsum dolor sit amet:
```
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.
```

Example of Code with color syntax:

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

Link:

[Lorem ipsum dolor sit amet](https://www.lipsum.com/), consectetur adipiscing elit. 

Anchor:

[Lorem ipsum dolor sit amet](#smaller-heading), consectetur adipiscing elit. 
<!-- Can't check anchor because of preprod-mode. Have to publish the page to know, how it works. -->

Relative link to another aticle in repository: 

[Another atricle in repository](./cdn-dns-2.md) 

Image (MarkDown):
![](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg)

Image (HTML): 
*Also can add picture by HTML*
<picture>
  <img alt="useful seo text" src="https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg">
</picture>
  
Unordered list:
  - consectetur adipiscing elit, 
  - sed do eiusmod tempor incididunt 
  - ut labore et dolore magna aliqua.

Ordered list:
  1. consectetur adipiscing elit, 
  2. sed do eiusmod tempor incididunt 
  3. ut labore et dolore magna aliqua.

Nested list:

1. First list item
   - First nested list item
     - Second nested list item
2. Second list item
   - Second nested list item
   - Third nested list item
     - Fourth nested list 
       - Fifth nested list  

To do task list:
- [x] First list item
- [ ] Second list item
- [ ] Add delight to the experience when all tasks are complete :tada:

Table:
| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cellazazazazazazazaaaaaaaaazaaaaaaaaaaaaaaaaaaaaaaaaa  |
| Content Cell  | Content Cell  |

Tables with wore wide column:
| Command | Description |
| --- | --- |
| *git status* | **List all new or modified files** |
| git diff | ![Image](https://i.ytimg.com/vi/1cDcHq7nQFM/maxresdefault.jpg) |


# Log Viewer (free feature). View and download logs of CDN resources

## What is Log Viewer?

Log Viewer is a free tool designed to view and export logs of CDN resources to your device. With it, you can see and download information about requests to your resources. The service stores the logs  that were recorded for the last 15 days of CDN operation.
![](https://support.gcorelabs.com/hc/article_attachments/5466155185937/image_1330-2.png)

## View logs in your control panel
Log Viewer can show logs collected for a maximum of 6 hours of CDN operation. Moreover, it can only display up to 1000 log entries. If more than 1000 logs have been recorded in six hours, entries after the 1000th will not be shown.

When you open the tab, you can see logs of all CDN resources for the last 6 hours.
![](https://support.gcorelabs.com/hc/article_attachments/5466214437521/image_1331.png)

You can customize a log report:
  - To see logs of a specific CDN resource, enter its [CNAME](https://gcorelabs.com/support/articles/213969769/) or ID.
  - To filter logs, click "Add filter" and set the required parameter: time, user's IP address, HTTP method, status code, data center or cache status.
  - To see logs for another time interval, click the timestamp field and specify your values. You can choose any interval of up to 6 hours for any of the last 15 days.

![](https://support.gcorelabs.com/hc/article_attachments/5466277302801/image_1332.png)

To see more details about a log, hover the mouse over the "i" icon on the right. You will see twelve request parameters.
![](https://support.gcorelabs.com/hc/article_attachments/5466309149073/image_1333-2.png)

**Client IP** — an IP address of the client who sent the request.

**Timestamp** — UTC time of the request.

**Method** — an HTTP request method (GET, POST, DELETE, etc.).

**Request URL** — a URL of the requested page or file.

**Status code** — a status of the response that was returned to the client.

**Refer header** — a URL of the page from which the client opened the requested page. If it was a direct transition, the header will contain a dash.

**Size** — the number of bytes in the response.

**Data center** — a G-Core Labs data center that received the client's request.

**User-Agent** — information about the client's browser and operating system.

**Cache status** — a source of the response: HIT means the response was sent from the CDN resource, MISS means the response was sent from the website.

**Resource ID** — an ID of the requested CDN resource.

**CNAME** — a CNAME of the requested CDN resource.

## Export logs
Log Viewer allows you to download a file with logs collected for a maximum of 24 hours of CDN operation. One file can contain up to 10,000 log entries. If more logs have been collected in 24 hours, entries after the 10,000th will not be written to an export file.

Logs are exported based on the filters that you have applied. To download logs to your PC:
  1. Click the "Export" button on the right side of the page.
  2. Select the time range of logs you want to download: you can keep the current period (selected in filters when viewing), or set a new value.
  3. Choose the export format: CSV or TSV.
  4. Click "Export".

The file will be downloaded to your browser download location.
![](https://support.gcorelabs.com/hc/article_attachments/5466379409297/image_1334.png)

## Manage Log Viewer via the API
You can also view and download logs via the API using requests from our [API documentation](https://apidocs.gcorelabs.com/cdn#tag/CDN-Logs). Below we explain how to create a request.

  1. In a tool for working with an API, add an authorization header.  Choose one of the two headers below, copy it, replace the expression in brackets with your data and remove the brackets.
   - *Authorization: Bearer* **(your [standard authorization token](https://apidocs.gcorelabs.com/account#tag/Account/paths/~1auth~1jwt~1login/post) that is valid for 1 hour; its lifetime can be extended up to 24 hours)**
   - *Authorization: APIKey* **(your permanent authorization token generated in your personal account; it never expires)** 

  2. Set the "GET" request type and specify a path for the required action: 
   - A path to view — https://api.gcorelabs.com/cdn/advanced/v1/logs.
   - A path to export — https://api.gcorelabs.com/cdn/advanced/v1/logs/download.

  3. Add the request parameters to filter the logs for the report. Enter each parameter on a new line. For example:
```
&from=2022-04-27T06:00:00Z    
&to=2022-04-27T12:00:00Z  
&fields=method,path,status,size 
… 
```                   
<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Description</th>
    <th>Example of parameter with value</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>from</td>
    <td><span><b>Condition</b>: this is a required parameter; a request will fail without it.<br><br><b>It sets</b>: the start of the time interval for which logs will be exported.<br><br><b>How to specify</b>: enter the time in ISO 8086 or RFC 3339 format. The time is indicated in UTC.</td>
    <td>&amp;from=2022-04-27T06:00:00Z</td>
  </tr>
  <tr>
    <td>to</td>
    <td><b>Condition</b>: this is a required parameter; a request will fail without it.<br><br><b>It sets</b>: the end of the time interval for which logs will be exported.<br><br><b>How to specify</b>: enter the time in the same format as in the "from" parameter. The interval between the "from" and "to" values should not exceed 6 hours for viewing and 24 hours for exporting.</td>
    <td>&amp;to=2022-04-27T12:00:00Z</td>
  </tr>
  <tr>
    <td>offset</td>
    <td><b>It sets</b>: skipping a certain number of logs from the beginning of the report.<br><br><b>Default value</b>: offset=0.<br><br><b>How to specify</b>: enter the number of entries you want to exclude from the report.<br><br><b>Example</b>: the report contains 100 entries, and you want to see only logs from 11 to 100. Set the "offset" value to 10: the first ten logs will be skipped, and you will see only entries from 11 to 100.</td>
    <td>&amp;offset=10</td>
  </tr>
  <tr>
    <td>limit</td>
    <td><b>It sets:</b> the number of entries in the report.<br><br><b>Default value:</b> 100 for viewing and 1000 for exporting.<br><br><b>Maximum value:</b> 1000 for viewing and 10,000 for exporting.<br><br><b>How to specify:</b> add the number of entries you want to see in the report.<br><br><b>Example:</b> if you set the "limit" value to 200, you will see the first 200 entries of the report.<br><br><b>Specific case</b>: together with the "offset" parameter, "limit" can be used to divide the report into segments of X logs. For example, you have 100 logs, but you need to split them into 10 lists of 10 entries each. To do this, use a combination of the "limit" and "offset" parameters. Send 10 requests with these combinations:<br><br>&amp;limit=10&amp;offset=0<br><br>&amp;limit=20&amp;offset=10<br><br>&amp;limit=30&amp;offset=20<br><br>...<br><br>&amp;limit=100&amp;offset=90</td>
    <td>&amp;limit=100</td>
  </tr>
</tbody>
</table>

  4. Send the created API request.

Let's look at an example of a request. Assuming, we want to view logs with the following parameters:
   - Time range is from 6:00 to 12:00 (UTC) on April 27, 2022.
   - The report should only contain the request method, the request path, the status of the response, the data center and the size of the request.
   - We don't need all the entries in the report; we only want to see logs about GET or POST requests whose responses were smaller than 100 bytes and had 3xx response codes.

We open a tool for working with an API and do as follows:

  1. We specify the request path for log viewing: "https://api.gcorelabs.com/cdn/advanced/v1/logs".
  2. We specify the request method: "GET".
  3. We add the "Authorization" header and its value. We want to log in with a permanent token, so we specify our token "APIKey 7711$eyJ0eXAiOiJKV".
  4. We enter the request parameters:
```
&from=2022-04-27T06:00:00Z
&to=2022-04-27T12:00:00Z
&fields=method,status,size,path,datacenter
&status__gte=300&status__lt=400&method__in=GET,POST&size__lt=100
```
  5. We send the request.

               ![image](https://user-images.githubusercontent.com/106074138/174901415-9f73abcb-8083-4162-be54-b7466dd15cd6.png)

