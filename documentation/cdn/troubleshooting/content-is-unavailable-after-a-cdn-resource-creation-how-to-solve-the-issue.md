---
title: content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue
displayName: Content unavailability
published: true
order: 10
toc:
   --1--Define where the issue is the origin or the content delivery network (CDN) resource: "define-where-the-issue-is-the-website-or-the-cdn-resource"
   --1--Check the CDN’s settings: "check-the-cdn-s-settings"
   --2--1. Personal domain (CNAME): "1-check-the-configuration-of-the-personal-domain"
   --2--2. Host header: "2-check-the-host-header-option"
   --2--3. Origin pull protocol: "3-check-the-origin-pull-protocol-option"
   --2--4. SSL certificate: "4-check-the-ssl-option"
   --3--Let’s Encrypt: "free-let-s-encrypt-certificate"
   --3--Your SSL: "personal-ssl-certificate"
   --2--5. Cache options: "5-check-the-cache-options"
   --2--6. Purge: "6-check-the-purge-option"
---
  
  
  
  
  
  
  
  
  

If content from your site doesn’t load or loads in an inappropriate way after integration with CDN, use this guide to quickly fix common CDN issues.

Define where the issue is: the website or the CDN resource
----------------------------------------------------------

Request any file that should be delivered via CDN from the source (your website) and ensure that you get an HTTP 200 response code.

For example:

*   _example.com_ is your website’s domain
*   _http_ is the protocol
*   _image.png_ is the path of the file you want to request to

The request will look as follows:

http://example.com/image.png

If the file opens correctly (HTTP 200 response code), the issue is not related to the website. In this case, check the CDN options according to the instructions below. If the file load fails (HTTP 4xx or 5xx response codes), the issue is related to the website origin, not to the CDN.

Check the CDN’s settings
------------------------

### 1. Check the configuration of the personal domain

If the CNAME record of the personal domain isn’t configured or configured with mistakes, the content will be delivered from the source and not via CDN. To check the CNAME record and set it up correctly:

1. Go to the Resource settings and look at the Setup guide. If there is the _x steps left_ label, click on it. If there is no label, go to the [next section](#2-check-the-host-header-option).

<img src="https://support.gcore.com/hc/article_attachments/9581756189713/image1.png" alt="image1.png">

2. Click the **Check DNS setup status** button.

<img src="https://support.gcore.com/hc/article_attachments/9581707286289/image2.png" alt="image2.png">

If the CNAME record doesn’t set up, this notification will appear:

<img src="https://support.gcore.com/hc/article_attachments/9581756237585/image3.png" alt="image3.png">

If there is a notification, go to step 3. If there isn’t, go to the [next troubleshooting section](#2-check-the-host-header-option).

3. Open [Google Admin Toolbox](https://toolbox.googleapps.com/apps/dig/), select the CNAME tab, and enter the CNAME of your CDN resource from the notification (in the screenshot above, it is _cdn.example.com_). Press **Enter**.

<img src="https://support.gcore.com/hc/article_attachments/9581756246801/image4.png" alt="image4.png">

If the TARGET section with the value from the Setup guide appears at the bottom of the page

<img src="https://support.gcore.com/hc/article_attachments/9581756282769/image5.png" alt="image5.png">

it means that you have already configured the CNAME record with the correct value, but the DNS records didn’t update. Repeat step 2 again in 15 minutes. It must show that the record is configured.

If you see the “Record not found!” label

<img src="https://support.gcore.com/hc/article_attachments/9581756291857/image6.png" alt="image6.png">

add the CNAME record according to the [“CNAME record configuration in DNS settings”](https://gcore.com/support/articles/213969769/) guide.

4\. Save the changes and wait for the records to update. Usually, it takes 15 minutes. But if you have recently changed the domain's NS servers, it may take up to 24 hours for the DNS records to be updated.

Try to request the content from the CDN once again. If it was a matter of personal domain settings, the issue won’t happen again.

### 2. Check the Host header option

If the [Host header](https://gcore.com/support/articles/360003612697/) does not match the website source, your website won’t be able to process requests from the CDN, and the content won’t load. To check the Host header and set it up correctly:

1. Go to the Resource settings and find the Host header option.

<img src="https://support.gcore.com/hc/article_attachments/9581707399697/image7.png" alt="image7.png">

2. Copy the value of the Host header.

3. Run the following command in the terminal or console:

curl -H "Host: example.com" -I http(s)://10.0.0.1/image.png

where:

*   _example.com_ is the value of the Host header
*   _http(s)_ depends on the protocol used by the source
*   _10.0.0.1_ is the IP address of your website source
*   _image.png_ is the path of the file that is delivered via the CDN without the domain

4. If you see the response code 2xx, the issue isn’t related to the Host header. Go to the [next troubleshooting section](#3-check-the-origin-pull-protocol-option).

If the response code is 4xx or 5xx, it means that the Host header wasn’t set properly. To fix it:

*   If you integrated only one website with the CDN, specify its actual domain name in the Host header option and then [clear the CDN cache](https://gcore.com/support/articles/214532065/).
*   If you integrated several websites or applications (origin group with several sources) with the CDN, each of them must accept the specified Host header. Manage the sources and [clear the CDN cache](https://gcore.com/support/articles/214532065/).

### 3. Check the Origin pull protocol option

If you have chosen the inappropriate [origin pull protocol](https://gcore.com/support/articles/214493065/) (HTTP, HTTPS, or both), the CDN resource will request the content from your website with an error or a redirect. To check if the protocol was chosen properly and correct an error:

1. Find out which protocol your website uses. You can see the type of protocol at the left of the domain name in the browser address bar. If there is a padlock icon:

<img src="https://support.gcore.com/hc/article_attachments/9581756338961/image8.png" alt="image8.png">

it means that your website works via HTTPS protocol. If you copy the domain name, it will be copied as follows: _https://example.com_.

If you see the Not secure label:

<img src="https://support.gcore.com/hc/article_attachments/9581756365201/image9.png" alt="image9.png">

it means that your website works via HTTP. If you copy the domain, it will be copied as follows: [http://example.com](http://example.com/).

It is also possible that the content on the origin is available both via HTTP and HTTPS. To check it, open your website using the protocols [http://example.com](http://example.com/) and [https://example.com](https://example.com/).

2. Go to the Resource settings and find the Origin pull protocol option. You will see what protocol is selected.

<img src="https://support.gcore.com/hc/article_attachments/9581707441041/image10.png" alt="image10.png">

3. Compare the protocol from step 1 with the value in step 2. If they are the same (e.g., the website works via HTTP and in the Origin pull protocol option HTTP is set), the issue isn’t related to the protocol. Go to the [next troubleshooting section](#4-check-the-ssl-option).

If they are different, go to the next step.

4. Change the value in the Origin pull protocol option according to the [“Origin. Specify origin and origin pull protocol”](https://gcore.com/support/articles/214493065/) guide. Select the type of protocol that your website uses. Save changes and then [clear the CDN cache](https://gcore.com/support/articles/214532065/).

### 4. Check the SSL option

If you enabled the SSL option, but the SSL certificate for your personal domain (e.g., _cdn.example.com_) isn’t added or is added with an error, the content won’t be available via the CDN, or you will see a notification that the connection isn’t secure in the browser.

<img src="https://support.gcore.com/hc/article_attachments/9581707474065/image11.png" alt="image11.png">

To check the SSL configuration and set it up correctly, go to the Resource settings and find the SSL option. Make sure that the **Enable HTTPS** option is enabled.

<img src="https://support.gcore.com/hc/article_attachments/9581756421393/image12.png" alt="image12.png">

There are two types of SSL configuration: **Get free Let’s Encrypt certificate** and **Add or select your own SSL certificate**. In both cases, wait about 15–30 minutes after you issue/add the certificate for the updates to register.

The troubleshooting scenario depends on the chosen SSL certificate type.

#### **Free Let’s Encrypt certificate**

1. Go back to the [personal domain troubleshooting section](#1-check-the-configuration-of-the-personal-domain) and make sure that the CNAME record for the personal domain of your CDN resource exists. If not, add it. Otherwise, Let’s Encrypt won’t be able to issue a certificate. If so, go to the next step.

2. Go to the Resource settings and find the Rules section. If there are no rules, go to the next step.

<img src="https://support.gcore.com/hc/article_attachments/9581756437009/image13.png" alt="image13.png">

3. Make sure that there are no rules denying requests to the personal domain (CNAME) of your CDN resource. Let’s Encrypt sends requests to your personal domain to issue a certificate. If requests are denied, the issue will fail. To determine whether the rule prevents requests, open every rule and look at the **Rule pattern** field. If you see the value

/\*

or

((?!(jpeg|gif|png|pdf|jpg|css|js|woff|woff2|ttf)).)\*$

this rule denies requests to the personal domain. To fix the certificate issuing, delete the rule or change its pattern. The next time Let’s Encrypt sends a request, the issue will be successful.

#### **Personal SSL certificate**

1. Run the following command in the terminal or console:

curl -I https://cdn.example.com/image.png

where:

*   _cdn.example.com_ is the personal domain (CNAME)
*   _image.png_ is the path of the file that is delivered via the CDN without the domain

If you see the 2xx response code, go to the next step.

If you see the following error in the command output

curl: (77) schannel: next InitializeSecurityContext failed: SEC\_E\_UNTRUSTED\_ROOT (0x80090325)

it means that the certificate is self-signed. Self-signed certificates are not suitable for content delivery. In this case, issue a new certificate with the Certificate authority (CA) and add it according to the [“How to add a personal SSL certificate in the SSL certificates section”](https://gcore.com/support/articles/213970109/) guide. Then clear the CDN cache and try to request the content again.

2. Open your website and request any file that is delivered via the CDN. Click the **padlock icon** or the **Not secure** label and choose the certificate. View the following values:

*   What domain the certificate is valid for
*   Expiration date

<img src="https://support.gcore.com/hc/article_attachments/9581707528977/image14.png" alt="image14.png">

If you see that the certificate is issued for the personal domain of your resource (if you see _\*.example.com_, it means that you are using a wildcard certificate that provides all your subdomains, including _cdn.example.com_), and the certificate is not expired. Go to the next step.

If not, you need to renew the certificate (if the problem is caused by expiration) or issue a new one for the personal domain of your CDN resource.

3. Go to the [SSLlabs](https://www.ssllabs.com/ssltest/) website, enter the personal domain name in the Hostname field and press the **Submit** button as follows:

<img src="https://support.gcore.com/hc/article_attachments/9581756461073/image15.png" alt="image15.png">

The check will take a few minutes. If you see no chain issues or the rating A+, the error isn’t related to SSL. Go to the [next section](#5-check-the-cache-options).

<img src="https://support.gcore.com/hc/article_attachments/9581707559825/image16.png" alt="image16.png">

If you see class B or chain issues as follows

<img src="https://support.gcore.com/hc/article_attachments/9581707577105/image17.png" alt="image17.png">

the chain of the SSL certificate is incomplete or added in the wrong way. Go to the [SSL certificates](https://cdn.gcore.com/ssl/list) section on the control panel. Delete the wrong certificate and add it again according to the [“How to add a personal SSL certificate in the SSL certificates section”](https://gcore.com/support/articles/213970109/) guide. 

### 5. Check the cache options

If the [cache options](https://gcore.com/support/articles/360003525737/) were configured with mistakes, you will see a low percentage of cache traffic or content will be loaded slowly.

To check cache options and set them up correctly:

1. Go to the [Dashboard](https://accounts.gcore.com/reports/dashboard) section and click **Total traffic**.

<img src="https://support.gcore.com/hc/article_attachments/9581707593105/image18.png" alt="image18.png">

2. Set the **Cache hit ratio** filter, the CDN resource, and the appropriate date. If you see less than 60% of Cache Hit Ratio traffic, it means that a small amount of content is delivered from the cache.

<img src="https://support.gcore.com/hc/article_attachments/9581756539665/image19.png" alt="image19.png">

In this case, ensure that you ran the CDN resource more than two days ago. This time is needed to ‘warm up’ the cache. If not, wait two days. Also, you need to have many requests from end-users to cache the requested content. If you have a small number of requests, the cache will be purged in 36 hours, regardless of the settings. Try to increase the amount of traffic. If the problem isn’t solved, go to the next step.

If the percentage of cache traffic is higher than 60% and you don’t experience a slow load time, go to the [next section](#6-check-the-purge-option).

3. Request any file that is delivered via CDN in the browser or console (terminal) and check the values of the _Cache_ and _Cache Control_ headers. If you see at least one of the following values, it means that there is a problem in the cache settings:

*   Cache-Control: max-age=0
*   Cache-Control: private
*   Cache-Control: no-cache
*   Cache: MISS

If you see the values, go to the next step. If not, go to step 5.

4. Go to the Resource settings and find the CDN caching option. Change the settings according to the [“Configure and check CDN caching settings”](https://gcore.com/support/articles/360003525737/) guide.

<img src="https://support.gcore.com/hc/article_attachments/9581707647377/image20.png" alt="image20.png">

5. Check the Set-Cookie and Query string options. If they are turned off, enable them. When you enable these options, CDN will cache a file with different cookies or query strings as a unique one.

<img src="https://support.gcore.com/hc/article_attachments/9581756582033/image21.png" alt="image21.png">

### 6. Check the Purge option

There are two signs showing that there is an issue after cache clearing by the [Purge](https://gcore.com/support/articles/214532065/) option:

*   The CDN returns a wrong or outdated file to users’ requests.
*   The file from the CDN cache and from the origin are mismatched.

To check the Purge option and fix an error:

1. Wait 15 minutes after purging until the cache is cleared on all servers.

2. Run the following two commands in the terminal or console to request the same file from both the source and the CDN:

curl -I cdn.example.com/image.png
curl -H "Host: example.com" -I http(s)://10.0.0.1/image.png

where:

*   _cdn.example.com_ is the personal domain of your CDN resource
*   _image.png_ is the path of the file that is delivered via the CDN
*   _http(s)_ depends on the protocol used by the source
*   _example.com_ is the value of the Host header
*   _10.0.0.1_ is the IP address of your website source

3. Compare outputs, paying attention to the values of the following headers:

*   Content-Length, which is the object size in bytes
*   ETag, which is the character set that the CDN compares to know if the file was changed
*   X-Cached-Since, which is the time in UTC format

If you see that the **Etag** and **Content-Length** values of the two files don’t match or that the date in the **X-Cached-Since** header is outdated, it means that there is a mistake. In this case, you should go to the next step.

If the values are the same and the date is relevant, purging has been performed correctly.

4. Try to repeat purging according to the [“Purge: purge some or all assets from CDN resource cache”](https://gcore.com/support/articles/214532065/) guide. Pay attention to the path pattern if you select Selective purge. We recommend checking whether the pattern was right by using the [regular expressions](https://regex101.com/) service. To do this, enter the path pattern for purging on the top line, and in the bottom area, enter the URL of the file. If you see the result “no matches”, there was an error in the path pattern. Correct the path pattern and repeat purging.

If the problem persists after performing troubleshooting according to this guide, contact support via chat or email at [support@gcore.com](mailto:support@gcore.com). You may have an atypical problem that requires assistance from technical specialists. We’ll be happy to help!