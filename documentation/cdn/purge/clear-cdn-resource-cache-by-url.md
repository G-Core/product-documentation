---
title: clear-cdn-resource-cache-by-url
displayName: By URL
published: true
order: 10
toc:
   --1--About Purge by URL: "about-purge-by-url"
   --1--Features: "features"
   --2--Limitations: "limitations"
   --2--URL requirements: "url-requirements"
   --2--Quotas: "quotas"
   --1--Configure: "configure-purge-by-url"
   --2--via the control panel: "via-the-control-panel"
   --2--via API: "via-api"
---
  
  
  
  
  
  
  

About Purge by URL
------------------

"Purge by URL" allows you to delete content that belongs to a particular URL from the cache without impacting other cached items.

Purge by URL can be set using the control panel or API.

Features
--------

1. When the same content is served over HTTP and HTTPS, both versions are deleted with a single purge by URL.

2\. When purging a compressed or optimized image, the original image and its variants are deleted with a single purge by URL. Supported formats are .br, .gzip, .webp, and .avif.

3. Query strings are supported on Purge by URL.

In the resource settings, if **Ignore query string** is disabled, you must append the query strings to the URL path when purging a particular item.

If **Ignore query string** is [enabled](https://gcore.com/support/articles/115002223049/), then whether to include query strings depends on the value set for the option:

*   **Ignore all.** Query strings do not need to be included in the purge request.
*   **Ignore all except.** Include in the purge request the parameters listed, and exclude those that are not.
*   **Ignore only.** Exclude from the purge request the parameters listed, and include those that are not.

**Note:** The order of the query string parameters does not matter. For example, _/pictures/icon.jpg?a=small&b=large_ and _/pictures/icon.jpg?b=large&a=small_ are considered the same.

### Limitations

1. When the origin server serves variations of content based on the HTTP _Vary_ header, only one variant is deleted with the URL purge method. Solutions:

*   If you have a subscription to a paid plan, you can [request](mailto:support@gcore.com) that your CDN resource be set to ignore the _Vary_ header.
*   You can use [other methods](https://gcore.com/support/articles/214532065/) to completely clear the content from the cache.

2. When content is cached in chunks (which happens when [Large Files Delivery Optimization](https://gcore.com/support/articles/115001975929/) is enabled), only the first chunk is deleted with the URL purge method. Solution:

*   You can use [other methods](https://gcore.com/support/articles/214532065/) to completely clear the content from the cache.

### URL requirements

The URLs that you specify must meet the following requirements:

*   They must start with a slash (/).
*   They must not include a protocol, domain name, or wildcard (\*).
*   They must include query strings if the CDN resource cache is configured to consider query strings (see General notes for more information).

For example, to purge the content at https://www.example.com/pictures/icon.jpg?size=small_,_ you would specify the following: _/pictures/icon.jpg?size=small._

### Quotas

The following are the default quotas for Purge by URL:

*   Maximum number of purge requests: 2 per minute
*   Maximum number of URLs that can be purged: 100 per request

**Note:** If you are on an Enterprise plan, contact our [support team](mailto:support@gcore.com) to increase these quotas.

Configure Purge by URL
----------------------

### Via the control panel

**Note:** Before proceeding with these steps, contact our [support team](mailto:support@gcore.com) to enable the URL purge option in the control panel.

To purge via the control panel:

1. Go to the **CDN**, then click **Purge**.

<img src="https://support.gcore.com/hc/article_attachments/11762143842705" alt="image1.png">

2. On the **Purge** page, do the following:

a. Select the CDN resource from the dropdown menu to which the content to purge belongs.

b. Click the radio button next to Purge by URL.

c. In the text area, specify one or more content URLs to purge, entering one URL per line. Make sure to follow the [URL requirements](#url-requirements).

<img src="https://support.gcore.com/hc/article_attachments/11762168816657" alt="image2.png">

3. Click **Purge**, and the contents will be immediately removed from the CDN cache.

<img src="https://support.gcore.com/hc/article_attachments/11762143900305" alt="image3.png">

### Via API

|                   |                                                                                                                                                                                                                                                                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Method            | POST                                                                                                                                                                                                                                                                                                                            |
| URL               | https://api\.gcore\.com/cdn/resources/\{\{resource\_id\}\}/purge                                                                                                                                                                                                                                                                |
| URL parameter     | \resource\_idID of the CDN resource that the content to purge belongs to                                                                                                                                                                                                                                                      |
| Header            | Bearer \{\{access\_token\}\}application/json                                                                                                                                                                                                                                                                                    |
| Payload           | \\{\  \\"urls\\": \[    \\"/example1\.jpg\\",    \\"/img/example2\.png\\",    \\"/style\.css?ver=2\.0\\"  \]\}\                                                                                                                                                                                                           |
| Request parameter | \urls\(required, string\) An array of one or more content URLs to purge                                                                                                                                                                                                                                                       |
| Response          | \201 CreatedReturns an array of the purged URLs\400 Bad RequestThe URL purge via API is not enabled for your account\400 Bad RequestThe user has exceeded the URL quota\401 UnauthorizedThe user does not have the correct authentication credentials\429 Too many requests\The user has exceeded the request quota |


To get started, [generate an access token](https://apidocs.gcore.com/account) that you can use to access the API and make authenticated requests. You can use a REST tool like cURL or Postman to send the requests. For this documentation, we used Postman.

**Note:** Before proceeding with these steps, contact our [support team](mailto:support@gcore.com) to enable sending purge by URL requests via API.

To send a purge by URL request:

1. In Postman, open a new request tab, then do the following:

a. Set the request method to _POST._

b. Enter the resource URL in the request URL field. Replace **{{resource\_id}}** with your actual value.

<img src="https://support.gcore.com/hc/article_attachments/11762143895441" alt="image4.png">

2. Go to the **Authorization** tab and do the following:

a. Select _Bearer Token_ from the **Type** dropdown.

b. Copy the generated access token and paste it into the **Token** field.

<img src="https://support.gcore.com/hc/article_attachments/11762143944849" alt="image5.png">

3. Go to the **Body** tab and do the following:

a. Select _raw_ as the data type.

b. Select _JSON_ from the format dropdown.

c. Enter the payload in the text area. Replace the sample values indicated by {{ }} with your actual values.

<img src="https://support.gcore.com/hc/article_attachments/11762143945233" alt="image6.png">

4. Click **Send**.

If the purge is successful, you will receive an HTTP 201 and a response message that contains a list of purged URLs.

<img src="https://support.gcore.com/hc/article_attachments/11762168939921" alt="image7.png">

If an error occurs with the request, the API will return a status code and a body that contains a description of what caused the error. Here is an example:

<img src="https://support.gcore.com/hc/article_attachments/11762168948241" alt="image8.png">
