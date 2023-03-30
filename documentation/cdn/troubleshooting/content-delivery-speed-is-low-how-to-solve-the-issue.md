---
title: content-delivery-speed-is-low-how-to-solve-the-issue
displayName: Low content delivery speed
published: true
order: 30
toc:
   --1--Check the delivery speed from a CDN-resource and an origin server.: "check-the-delivery-speed-from-a-cdn-resource-and-an-origin-server"
   --1--Check CDN-resource's settings.: "cdn-resource-s-settings-checking"
   --1--Diagnostic information for technical support.: "diagnostic-information-for-technical-support"
---
If you experience issues with site or application performance, follow the steps below: 

1.  Revise your origin to find errors or misconfigurations that may affect the content delivery speed.  Contact your hosting provider or server administrator for help in the case analysis. 

Check the delivery speed from a CDN-resource and an origin server 
------------------------------------------------------------------

1\. Measure the content delivery speed from both a CDN-resource and an origin server using:

*   DevTools (F12->Network tab->F5).  
    

*   wget –S + static file URL.

wget -S [testsupport.gcdn.co/files/test.jpg](http://testsupport.gcdn.co/files/test.jpg)  
\--2019-12-10 13:29:17-- [http://testsupport.gcdn.co/files/test.jpg](http://testsupport.gcdn.co/files/test.jpg)  
Resolving [testsupport.gcdn.co](http://testsupport.gcdn.co/) ([testsupport.gcdn.co](http://testsupport.gcdn.co/))... 92.223.97.97  
Connecting to [testsupport.gcdn.co](http://testsupport.gcdn.co/) ([testsupport.gcdn.co](http://testsupport.gcdn.co/))|92.223.97.97|:80... connected.  
HTTP request sent, awaiting response...  
HTTP/1.1 200 OK  
Server: nginx  
Date: Tue, 10 Dec 2019 08:29:17 GMT  
Content-Type: image/jpeg  
Content-Length: 290  
Connection: keep-alive  
Last-Modified: Fri, 06 Dec 2019 10:12:14 GMT  
ETag: "5dea297e-122"  
Set-Cookie: 48c62c809b061c360cc201975b7fa802  
Cache: MISS  
X-ID: fr5-up-gc22  
Accept-Ranges: bytes  
Syntax error in Set-Cookie: 48c62c809b061c360cc201975b7fa802 at position 32.  
Length: 290 \[image/jpeg\]  
Saving to: 'test.jpg'  
  
test.jpg 100%\[=================================================>\] 290 --.-KB/s in 0s  
  
2019-12-10 13:29:18 (5,38 MB/s) - 'test.jpg' saved [290/290](https://wiki.gcore.lu/pages/createpage.action?spaceKey=monitoring&title=290%2F290&linkCreation=true&fromPageId=71286196)

*   online-services. Consider network settings and location which are chosen for the speed test. 

2\. Compare the delivery speed from CDN and the origin server. 

3\. If the analysis confirmed issues with content delivery speed from CDN, [revise CDN-resource's settings.](#cdn-resource-s-settings-checking)

CDN-resource's settings checking 
---------------------------------

1\. Make sure that you don’t use a VPN or proxy.   
VPN affects the CDN Geo-balancing and you may receive content from a not optimal edge with lower speed. 

2\. Make sure that content is being cached.   
The cache rate is presented by Cache Hit Ratio [report](https://support.gcore.com/hc/en-us/articles/115004917425). If you noticed that the cache rate is low, use our [instructions](https://support.gcore.com/hc/en-us/articles/360013291637) to analyze and solve this issue.  

3\. If an issue with content delivery speed occurs with large files, we recommend you to use [Large files delivery optimization](https://www.gcore.com/support/articles/115001975929/) and consider content compression on [CDN](https://www.gcore.com/support/articles/360006563858/) or the origin server. 

Diagnostic information for technical support
--------------------------------------------

If you revised your CDN resource's settings but are still unsatisfied with the download speed, contact [Technical Support](mailto:support@gcore.com) (support@gcore.com) and provide the following information:

*   File URL
*   Follow the link [http://iam.gcdn.co/info](http://iam.gcdn.co/info), copy all information from the page or save a screenshot. 
*   Follow the try speed test link, click on the Start button, save the result, and add it to the ticket. 

<img src="https://support.gcore.com/hc/article_attachments/360011396498/iam.png" alt="iam.png">

*   Wget –S output for the URL from your CDN-resource.
*   Open a file or a web-page and save a [HAR file.](https://toolbox.googleapps.com/apps/har_analyzer/?lang=en)