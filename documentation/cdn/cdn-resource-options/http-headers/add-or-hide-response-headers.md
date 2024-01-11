---
title: add-or-hide-response-headers
displayName: Configure response headers
published: true
order: 30
toc:
   --1--Add headers: "add-response-headers"
   --2--Add multiple header values: "add-multiple-header-values"
   --2--Check headers: "check-headers"
   --1--Hide response headers: "hide-response-headers"
pageTitle: Manage CDN Response Headers Effectively | Gcore
pageDescription: A detailed guide to add, hide or customize CDN response headers, enhancing control over HTTP responses and refining user-end data security and privacy.
---
# Add or hide response headers

## Add response headers

Our "Response headers (add)" option allows you to set custom HTTP headers that CDN servers will include in a response to an end-user. If the same header is already configured on your server, the CDN servers will override its value.

1\. Go to the CDN resource settings.

Do the remaining steps below on the tab that opens.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/image_1659-2.png" alt="Go to the CDN resource settings">

2\. In the "HTTP headers" section, select "Response headers (add)".

3\. Switch on the "Response headers (add)" option. 

**Note**: You can add up to 50 response headers.

4\. Enter the header name in the "Header name" field. 

5\. Enter the header value in the "Value" field that will be sent in the response. 

6\. Check the box if you want to add a header to all responses regardless of their status code. If not, uncheck the box. Then headers will be added only to responses with codes 200, 201, 204, 206, 301, 302, 304, 307 and 308. 

7\. Click "Add header" if you want to add extra headers. Fill in the fields according to Steps 4 and 5. 

8\. Save the changes. 

### Add multiple header values

If you need to add more than one header value, you can do it in two ways. It determines how response headers will look like: 

- If you need to send header values in different strings, enter value of the first header in the "Value" field and press "Enter", then enter a value of the second header and press "Enter", and so on.  

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/image_1660.png" alt="Add multiple header values">
    
In this case, the response header will be transmitted as follows:
    
```
Example: one   
Example: two   
Example: three 
```

- If you need to send header values in one string, fill in the "Value" field with header values separated by commas. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/image_1661.png" alt="header values ">
    
In this case, the response header will be transmitted as follows:
    
```Example: one, two, three``` 
    
You can also combine both ways: enter the values separated by commas and add other values to them separately.
    
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/image_1662.png" alt="header values ">

In this case, the response header will be transmitted as follows:

```
Example: one, two   
Example: three 
```

**Valid characters for fields:**

- "Header name":  Latin letters (A-Z, a-z), numbers (0-9), underscore (_) and hyphen (-),
- "Value": Latin letters (A-Z, a-z), numbers (0-9), a space and the following special characters: `~!@#%^&*()-_=+ /|";:?.><{}[]

**The "Value" field restrictions:**

- Invalid characters: \$'
- It can't start with a special character
- It cannot contain only special characters

### Check headers

1\. <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">Clear the cache</a> of the CDN resource or files for which the header was added.

2\. Run the cURL command using the terminal on your PC or online services:

```
curl -I http://cdn.site.com/images/1.jpg 
HTTP/1.1 200 OK 
Server: nginx/1.11.4 
Date: Wed, 05 Apr 2017 19:27:14 GMT 
Content-Type: image/jpeg 
Content-Length: 62890 
Connection: keep-alive 
Last-Modified: Mon, 03 Oct 2016 22:21:05 GMT
ETag: "f5aa-53dfd5c25d421" 
FILE: Image 
Example: yourvalue 
Cache: HIT 
X-ID: m9-up-e240 
Accept-Ranges: bytes 
```

3\. If the response contains the required header, it means the configuration succeeded.

## Hide response headers

By default, a CDN server passes all HTTP headers it receives from the client’s origin to end users.

To adjust the headers that are being passed:

1\. Go to the resource settings.

2\. Switch on the **Hide response headers option** in the "HTTP headers" section.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/11595287930257.png" alt="Hide response headers option " width="80%">

3\. Set up the option. You can configure it in two modes:

- **Hide all except**. Set the headers that will be kept in the response, and all other headers will be hidden. After enabling, the most popular headers will appear in the field. You can remove some of them from the response or add custom headers to the response. To remove, press the × icon. To add, click on the **HTTP headers** row and choose from the list or enter your own. The new header can contain letters (a-z), numbers (0-9), dashes (-), and underscores (_).

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/11595282619665.png" alt="Hide all except" width="50%">

- **Hide only**. Set the headers that will be hidden from the response, and all other headers will be kept. Click on the **HTTP headers** row and choose from the list or enter custom headers.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers/11595288042385.png" alt="Hide only" width="50%">

Headers to hide that can be chosen in the customer portal: *accept, accept-charset, accept-encoding, accept-language, accept-ranges, age, allow, alternates, authorization, cache-control, content-disposition, content-encoding, content-language, content-location, content-md5, content-range, content-version, derived-from, etag, expect, expires, from, host, if-match, if-modified-since, if-none-match, if-range, if-unmodified-since, last-modified, link, location, max-forwards, mime-version, pragma, proxy-authenticate, proxy-authorization, public, range, referer, retry-after, title, te, trailer, transfer-encoding, upgrade, user-agent, vary, via, warning, www-authenticate, keep-alive*.

**Note**: There are some mandatory headers: *connection, content-length, content-type, server, and date*. These cannot be hidden from responses.

4\. Save changes.