---
title: add-the-access-control-allow-origin-header-to-the-browser-response
displayName: Activate CORS
published: true
order: 20
toc:
   --1--What is CORS, and how it works: "what-is-cors-and-how-does-it-work"
   --1--What is the feature used for?: "what-is-the-cors-header-support-feature-used-for"
   --1--Configure: "configure-the-cors-header-support-feature"
   --2--in the resource settings: "configure-cors-in-the-resource-settings"
   --2--over the rule creation: "configure-cors-over-the-rule-creation"
   --2--on an origin server: "configure-cors-on-the-origin-server"
   --1--Check: "check-cors"
   --2--through cURL: "check-cors-through-curl"
   --2--in a browser: "check-cors-with-devtools-in-a-browser"
---

What is CORS, and how does it work?
-----------------------------------

CORS (Cross-Origin Resource Sharing) is a mechanism that uses the HTTP header "Access-Control-Allow-Origin" to allow or deny end-user browsers from accessing a domain other than the one from which the browser sent the request.

For example, if a user visits the website _http://site-a.com_ and requests an image, but the image is hosted on another server and has the path _http://cdn.site-b.com/image.jpg_, the user's browser sends a request to the server _http://cdn.site-b.com/_:

GET /image.jpg HTTP/1.1  
Host: cdn.site-b.com  
User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3pre) Gecko/20081130 Minefield/3.1b3pre  
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8  
Accept-Language: en-us,en;q=0.5  
Accept-Encoding: gzip,deflate  
Accept-Charset: ISO-8859-1,utf-8;q=0.7,\*;q=0.7  
Connection: keep-alive  
Referer: http://site-a.com/examples/access-control/test.html  
Origin: http://site-a.com

The most significant header in the response is "Origin," which tells the server that the request was sent from _http://site-a.com_. The _http://cdn.site-b.com_ server checks the "Origin" header and decides whether to accept or deny the request.

*   If the _http://cdn.site-b.com_ server is configured for cross-platformed requests, it will add the CORS header with the allowing value (e.g., _Access-Control-Allow-Origin: \*_) to the response. In this case, the requested image will be displayed at _http://site-a.com_.
*   If the _http://cdn.site-b.com_ server isn’t configured for cross-platformed requests, the response will have no "Access-Control-Allow-Origin" header or won't have permission for _http://site-a.com_, and the requested image will not be displayed.

What is the CORS header support feature used for?
-------------------------------------------------

Gcore has the CORS header support feature, which allows the CDN to add the "Access-Control-Allow-Origin" header to a response to a browser.

It can be used for several purposes, such as protecting content from use at third-party sites or in third-party applications and preventing errors (such as _XMLHttpRequest cannot load http://domain.ru_ and _No “Access-Control-Allow-Origin” header is present on the requested resource_ that can appear when web fonts are loaded in Firefox or Internet Explorer from the CDN servers.

Configure the CORS header support feature
-----------------------------------------

There are three methods to configure CORS header supports: in the resource settings, over the rule creation, and on the origin server.

### Configure CORS in the resource settings

If you want to apply the configuration to all files sent over the CDN, use the resource settings method:

1\. Go to the [CDN](https://cdn.gcore.com/resources/list) section in the control panel and click the custom domain of the resource for which you want to configure CORS to open the resource settings.

<img src="https://support.gcore.com/hc/article_attachments/13198726101521" alt="mceclip0.png">

The new page opens. Do the remaining steps on it.

<img src="https://support.gcore.com/hc/article_attachments/13198779606929" alt="mceclip1.png">

2\. Go to the "HTTP headers" section and click **CORS header support**.

3\. Enable the feature.

4\. Configure one of the three available options:

| Option                                            | \nHow it works\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \n*, for all domains\n                            | \nContent will be uploaded for requests from any domain. The highlighted line will be added to the response header.\nHTTP/1.1 200 OKDate: Mon, 01 Dec 2020 00:23:53 GMTServer: Apache/2.0.61 Access-Control-Allow-Origin: *Keep-Alive: timeout=2, max=100Connection: Keep-AliveTransfer-Encoding: chunkedContent-Type: application/xml\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \n\"$http_origin\" if an origin is listed below\n | \nSpecify the domain name from which requests are allowed in the field, e.g., site-a.com.  \nNote: You can specify up to 20 domains.\nContent will be uploaded only for requests from the domains specified in the field. When the CDN servers receive a request, they check the value of the \"Origin\" header to determine which site the request came from.\n\nIf it matches any of the domains specified in the feature, the content will be uploaded, and the response will contain the highlighted line:\n\nHTTP/1.1 200 OKDate: Mon, 01 Dec 2008 00:23:53 GMTServer: Apache/2.0.61 Access-Control-Allow-Origin: https://site-a.comKeep-Alive: timeout=2, max=100Connection: Keep-AliveTransfer-Encoding: chunkedContent-Type: application/xml\n\nIf it doesn't match, the \"Access-Control-Allow-Origin\" header will not be added to a response, and the content will not be uploaded.\n\n |
| \n\"$http_origin\", for all domains\n \n          | \nNote: This option is similar to the first one, but you can use it if the \"*\" parameter is unsuitable for certain filters configured on a server.\nContent will be uploaded for requests from any domain, and the domain from which the request was sent will be added to the \"Access-Control-Allow-Origin\" header in the response. For example, if a user requests content from http://site-b.com, the response will look as follows:\nHTTP/1.1 200 OKDate: Mon, 01 Dec 2008 00:23:53 GMTServer: Apache/2.0.61 Access-Control-Allow-Origin: https://site-b.comKeep-Alive: timeout=2, max=100Connection: Keep-AliveTransfer-Encoding: chunkedContent-Type: application/xml\n                                                                                                                                                                                                                  |


5\. Optionally, check the "Always add the header to the response from CDN regardless of the response code" box to add the "Access-Control-Allow-Origin" header to responses with any status code, even for those when content is not available. If you leave the box unchecked, the header will be added only to responses with specific status codes.

6\. Save changes.

### Configure CORS over the rule creation

If you want to apply the configuration only to particular files, use the "Rules" method:

1\. Go to the [CDN](https://cdn.gcore.com/resources/list) section in the control panel and click the custom domain of the resource for which you want to configure CORS to open the resource settings.

<img src="https://support.gcore.com/hc/article_attachments/13198726101521" alt="mceclip0.png">

2\. Open the "Rules" section, click **Create rule** and select **Create blank rule** from the list.

<img src="https://support.gcore.com/hc/article_attachments/13199698120465" alt="mceclip5.png">

A new page opens. Do the remaining steps in it. 

3\. Specify the settings (rule name and path to files you want to apply the rule) according to the "[Create a rule manually](https://www.gcore.com/support/articles/115005383865/#h_01GHVMZTWQKBATF8S9H9C9DVA0)" guide.

4\. Click **Add option**, select "CORS header support", and close the list.

<img src="https://support.gcore.com/hc/article_attachments/13199806046737" alt="mceclip6.png">

5\. Configure the option. If you enable the option, the Access-Control-Allow-Origin header will be added. If you add an option but leave it disabled, the Access-Control-Allow-Origin header will not be added.

6\. Click **Create rule** to save the changes.

### Configure CORS on the Origin Server

We have provided an example of how to set up CORS for Apache and Nginx web servers.

**Apache Configuration**:

\# ----------------------------------------------------------------------   
\# CORS-enabled images (@crossorigin)   
\# ----------------------------------------------------------------------   
\# Send CORS headers if browsers request them; enabled by default for images.   
\# developer.mozilla.org/en/CORS\_Enabled\_Image   
\# blog.chromium.org/2011/07/using-cross-domain-images-in-webgl-and.html   
\# hacks.mozilla.org/2011/11/using-cors-to-load-webgl-textures-from-cross-domain-images/   
\# wiki.mozilla.org/Security/Reviews/crossoriginAttribute   
<IfModule mod\_setenvif.c>   
<IfModule mod\_headers.c>   
\# mod\_headers, y u no match by Content-Type?!   
<FilesMatch "\\.(gif|png|jpe?g|svg|svgz|ico|webp)$">   
SetEnvIf Origin ":" IS\_CORS   
Header set Access-Control-Allow-Origin "\*" env=IS\_CORS   
</FilesMatch>   
</IfModule>   
</IfModule>   
\# ----------------------------------------------------------------------   
\# Webfont access   
\# ----------------------------------------------------------------------   
\# Allow access from all domains for webfonts.   
\# Alternatively you could only whitelist your # subdomains like "subdomain.example.com".   
<IfModule mod\_headers.c>   
<FilesMatch "\\.(ttf|ttc|otf|eot|woff|woff2|font.css|css|js)$">   
Header set Access-Control-Allow-Origin "\*"   
</FilesMatch>   
</IfModule>

**Nginx configuration:**

location ~ \\.(ttf|ttc|otf|eot|woff|woff2|font.css|css|js)$ {   
add\_header Access-Control-Allow-Origin "\*";   
}

Check CORS
----------

Clear the cache of the CDN resource or files for which CORS was enabled according to the "[Purge CDN cache by URL](https://www.gcore.com/support/articles/11762165947665/)" guide, and use one of the methods below.

### Check CORS through cURL

1\. Open the terminal on macOS or command prompt (cmd) on Windows.

2\. Run the following command:

curl -I http://cdn.testdomain.com/assets/image.jpg

where _http://cdn.testdomain.com/assets/image.jpg_ is a link to your file delivered via CDN.

3\. In the output, check whether the "Access-Control-Allow-Origin" header is present. If you see the Access-Control-Allow-Origin header in the response, the configuration was successful.

HTTP/1.1 200 OK   
Server: nginx/1.13.1   
Date: Fri, 24 Feb 2023 12:54:24 GMT   
Content-Type: image/jpeg   
Content-Length: 124024   
Connection: keep-alive   
X-Image-Generated: 29   
X-Image-Meta: 1024x768   
X-Image-Read: 71   
Expires: Fr, 10 March 2023 12:51:43 GMT   
Cache-Control: max-age=15552000   
**Access-Control-Allow-Origin: \***   
Last-Modified: Sun, 29 Jan 2023 12:00:00 GMT   
Cache-Control: max-age=315360000, public   
Cache: HIT   
X-Cached-Since: 2022-12-09T12:51:43+00:00   
X-ID: m9-up-e245 

### Check CORS with DevTools in a Browser

1\. Open any internet browser (for example, Google Chrome).

2\. Go to your website.

3\. Right-click and select Inspect to open the DevTools (Developer Toolbar).

4\. Select the "Network" tab.

5\. Refresh the page.

6\. You will get a list of all files retrieved from your website.

7\. Find any file (e.g., JPEG, PNG, IMG, CSS, etc.) integrated with the CDN and select it.

8\. On the "Headers" tab on the right, you will see the headers configured on your server. If you see the Access-Control-Allow-Origin header, the configuration was successful.

<img src="https://support.gcore.com/hc/article_attachments/13200288365969" alt="mceclip7.png">
