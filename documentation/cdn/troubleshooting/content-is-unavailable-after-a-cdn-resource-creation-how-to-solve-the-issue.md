---
title: content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue
displayName: Content unavailability
published: true
order: 10
toc:
   --1--Define where the issue is: "define-where-the-issue-is-the-website-or-the-cdn-resource"
   --1--Check the CDN’s settings: "check-the-cdns-settings"
   --2--1. Personal domain (CNAME): "1-check-the-configuration-of-the-personal-domain"
   --2--2. Host header: "2-check-the-host-header-option"
   --2--3. Origin pull protocol: "3-check-the-origin-pull-protocol-option"
   --2--4. SSL certificate: "4-check-the-ssl-option"
   --3--Let’s Encrypt: "free-lets-encrypt-certificate"
   --3--Your SSL: "personal-ssl-certificate"
   --2--5. Cache options: "5-check-the-cache-options"
   --2--6. Purge: "6-check-the-purge-option"
pageTitle: Common CDN Issues | Gcore
pageDescription: What to do if the content is unavailable after integration your site with the CDN resource.
---
# Content is unavailable after a CDN resource creation: how to solve the issue

If content from your site doesn’t load or loads in an inappropriate way after integration with CDN, use this guide to quickly fix common CDN issues.

## Define where the issue is: the website or the CDN resource

Request any file that should be delivered via CDN from the source (your website) and ensure that you get an HTTP 200 response code.

For example:

*   <span style="color:#FF5913">example.com</span> is your website’s domain
*   <span style="color:#FF5913">http</span> is the protocol
*   <span style="color:#FF5913">image.png</span> is the path of the file you want to request to

The request will look as follows:

```
http://example.com/image.png
```

If the file opens correctly (HTTP 200 response code), the issue is not related to the website. In this case, check the CDN options according to the instructions below. If the file load fails (HTTP 4xx or 5xx response codes), the issue is related to the website origin, not to the CDN.

## Check the CDN’s settings

### 1. Check the configuration of the personal domain

If the CNAME record of the personal domain isn’t configured or configured with mistakes, the content will be delivered from the source and not via CDN. To check the CNAME record and set it up correctly:

1\. Go to the Resource settings and look at the Setup guide. If there is the _x steps left_ label, click on it. If there is no label, go to the [next section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#2-check-the-host-header-option).

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image1.png" alt="Resource settings " width="80%">

2\. Click the **Check DNS setup status** button.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image2.png" alt=" DNS setup status" width="80%">

If the CNAME record doesn’t set up, this notification will appear:

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image3.png" alt="notification " width="50%">

If there is a notification, go to step 3. If there isn’t, go to the [next troubleshooting section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#2-check-the-host-header-option).

3\. Open <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> enter the CNAME of your CDN resource from the notification (in the screenshot above, it is *cdn.example.com*), choose from which servers the domain should be checked and press **Search**.

Choose the CNAME tab at the bottom of the page. If the value from the Setup guide appears, it means that you have already configured the CNAME record with the correct value, but the DNS records didn’t update. Repeat step 2 again in 15 minutes. It must show that the record is configured.

If you see the “No records were found” label, add the CNAME record according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record configuration in DNS settings</a>" guide.

4\. Save the changes and wait for the records to update. Usually, it takes 15 minutes. But if you have recently changed the domain's NS servers, it may take up to 24 hours for the DNS records to be updated.

Try to request the content from the CDN once again. If it was a matter of personal domain settings, the issue won’t happen again.

### 2. Check the Host header option

If the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Host header</a> does not match the website source, your website won’t be able to process requests from the CDN, and the content won’t load. To check the Host header and set it up correctly:

1\. Go to the Resource settings and find the Host header option.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image7.png" alt="Resource settings " width="80%">

2\. Copy the value of the Host header.

3\. Run the following command in the terminal or console:

<code-block>
curl -H "Host: <span style="color:#FF5913">example.com</span>" -I <span style="color:#FF5913">http(s)://10.0.0.1/image.png</span>
</code-block>

where:

- <span style="color:#FF5913">example.com</span> is the value of the Host header
- <span style="color:#FF5913">http(s)://10.0.0.1/image.png</span> the http(s) depends on the protocol used by the source, then the IP address of your website source and the path of the file that is delivered via the CDN without the domain.

4\. If you see the response code 2xx, the issue isn’t related to the Host header. Go to the [next troubleshooting section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#3-check-the-origin-pull-protocol-option).

If the response code is 4xx or 5xx, it means that the Host header wasn’t set properly. To fix it:

- If you integrated only one website with the CDN, specify its actual domain name in the Host header option and then <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">clear the CDN cache</a>.
- If you integrated several websites or applications (origin group with several sources) with the CDN, each of them must accept the specified Host header. Manage the sources and <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">clear the CDN cache</a>.

### 3. Check the Origin pull protocol option

If you have chosen the inappropriate <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol" target="_blank">origin pull protocol</a> (HTTP, HTTPS, or both), the CDN resource will request the content from your website with an error or a redirect. To check if the protocol was chosen properly and correct an error:

1\. Find out which protocol your website uses. You can see the type of protocol at the left of the domain name in the browser address bar. If there is a padlock icon:

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image8.png" alt="origin pull protocol" width="50%">

it means that your website works via HTTPS protocol. If you copy the domain name, it will be copied as follows: ```https://example.com```.

If you see the Not secure label:

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image9.png" alt="Not secure label" width="50%">

it means that your website works via HTTP. If you copy the domain, it will be copied as follows: ```http://example.com```.

It is also possible that the content on the origin is available both via HTTP and HTTPS. To check it, open your website using the protocols ```http://example.com``` and ```https://example.com```.

2\. Go to the Resource settings and find the Origin pull protocol option. You will see what protocol is selected.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image10.png" alt="Resource settings" width="80%">

3\. Compare the protocol from step 1 with the value in step 2. If they are the same (e.g., the website works via HTTP and in the Origin pull protocol option HTTP is set), the issue isn’t related to the protocol. Go to the [next troubleshooting section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#4-check-the-ssl-option).

If they are different, go to the next step.

4\. Change the value in the Origin pull protocol option according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol" target="_blank">Origin. Specify origin and origin pull protocol</a> guide. Select the type of protocol that your website uses. Save changes and then <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">clear the CDN cache</a>.

### 4. Check the SSL option

If you enabled the SSL option, but the SSL certificate for your personal domain (e.g., _cdn.example.com_) isn’t added or is added with an error, the content won’t be available via the CDN, or you will see a notification that the connection isn’t secure in the browser.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image11.png" alt="Check the SSL option" width="50%">

To check the SSL configuration and set it up correctly, go to the Resource settings and find the SSL option. Make sure that the **Enable HTTPS** option is enabled.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image12.png" alt="SSL configuration" width="80%">

There are two types of SSL configuration: **Get free Let’s Encrypt certificate** and **Add or select your own SSL certificate**. In both cases, wait about 15–30 minutes after you issue/add the certificate for the updates to register.

The troubleshooting scenario depends on the chosen SSL certificate type.

#### Free Let’s Encrypt certificate

1\. Go back to the [personal domain troubleshooting section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#1-check-the-configuration-of-the-personal-domain) and make sure that the CNAME record for the personal domain of your CDN resource exists. If not, add it. Otherwise, Let’s Encrypt won’t be able to issue a certificate. If so, go to the next step.

2\. Go to the Resource settings and find the Rules section. If there are no rules, go to the next step.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image13.png" alt="Rules section." width="80%">

3\. Make sure that there are no rules denying requests to the personal domain (CNAME) of your CDN resource. Let’s Encrypt sends requests to your personal domain to issue a certificate. If requests are denied, the issue will fail. To determine whether the rule prevents requests, open every rule and look at the **Rule pattern** field. If you see the value

```
/*
```

or

```
((?!(jpeg|gif|png|pdf|jpg|css|js|woff|woff2|ttf)).)\*$
```

this rule denies requests to the personal domain. To fix the certificate issuing, delete the rule or change its pattern. The next time Let’s Encrypt sends a request, the issue will be successful.

#### Personal SSL certificate

1\. Run the following command in the terminal or console:

<code-block>
curl -I <span style="color:#FF5913">https://cdn.example.com/image.png</span>
</code-block>

where:

- <span style="color:#FF5913">cdn.example.com</span> is the personal domain (CNAME)
- <span style="color:#FF5913">image.png</span> is the path of the file that is delivered via the CDN without the domain

If you see the 2xx response code, go to the next step.

If you see the following error in the command output

```
curl: (77) schannel: next InitializeSecurityContext failed: SEC\_E\_UNTRUSTED\_ROOT (0x80090325)
```

it means that the certificate is self-signed. Self-signed certificates are not suitable for content delivery. In this case, issue a new certificate with the Certificate authority (CA) and add it according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">How to add a personal SSL certificate in the SSL certificates section</a>" guide. Then clear the CDN cache and try to request the content again.

2\. Open your website and request any file that is delivered via the CDN. Click the **padlock icon** or the **Not secure** label and choose the certificate. View the following values:

- What domain the certificate is valid for
- Expiration date

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image14.png" alt="certificates ">

If you see that the certificate is issued for the personal domain of your resource (if you see _*.example.com_, it means that you are using a wildcard certificate that provides all your subdomains, including *cdn.example.com*), and the certificate is not expired. Go to the next step.

If not, you need to renew the certificate (if the problem is caused by expiration) or issue a new one for the personal domain of your CDN resource.

3\. Go to the <a href="https://ssllabs.com/ssltest" target="_blank">SSLlabs</a> website, enter the personal domain name in the Hostname field and press the **Submit** button as follows:

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image15.png" alt="SSLlabs" width="80%">

The check will take a few minutes. If you see no chain issues or the rating A+, the error isn’t related to SSL. Go to the [next section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#5-check-the-cache-options).

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image16.png" alt="rating A+" width="80%">

If you see class B or chain issues as follows

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image17.png" alt="Dashboard section" width="80%">

the chain of the SSL certificate is incomplete or added in the wrong way. Go to the <a href="https://cdn.gcore.com/ssl/list" target="_blank">SSL certificates</a> section on the control panel. Delete the wrong certificate and add it again according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">How to add a personal SSL certificate in the SSL certificates section</a>" guide. 

### 5. Check the cache options

If the <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers" target="_blank">cache options</a> were configured with mistakes, you will see a low percentage of cache traffic or content will be loaded slowly.

To check cache options and set them up correctly:

1\. Go to the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Dashboard</a> section and click **Total traffic**.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image18.png" alt="Total traffic" width="50%">

2\. Set the **Cache hit ratio** filter, the CDN resource, and the appropriate date. If you see less than 60% of Cache Hit Ratio traffic, it means that a small amount of content is delivered from the cache.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image19.png" alt="Cache hit ratio" width="80%">

In this case, ensure that you ran the CDN resource more than two days ago. This time is needed to ‘warm up’ the cache. If not, wait two days. Also, you need to have many requests from end-users to cache the requested content. If you have a small number of requests, the cache will be purged in 36 hours, regardless of the settings. Try to increase the amount of traffic. If the problem isn’t solved, go to the next step.

If the percentage of cache traffic is higher than 60% and you don’t experience a slow load time, go to the [next section](https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#6-check-the-purge-option).

3\. Request any file that is delivered via CDN in the browser or console (terminal) and check the values of the *Cache* and *Cache Control* headers. If you see at least one of the following values, it means that there is a problem in the cache settings:

- Cache-Control: max-age=0
- Cache-Control: private
- Cache-Control: no-cache
- Cache: MISS

If you see the values, go to the next step. If not, go to step 5.

4\. Go to the Resource settings and find the CDN caching option. Change the settings according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers" target="_blank">Configure and check CDN caching settings</a>" guide.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image20.png" alt="CDN caching option" width="80%">

5\. Check the Set-Cookie and Query string options. If they are turned off, enable them. When you enable these options, CDN will cache a file with different cookies or query strings as a unique one.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue/image21.png" alt="Set-Cookie and Query string options" width="80%">

### 6. Check the Purge option

There are two signs showing that there is an issue after cache clearing by the <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">Purge</a> option:

- The CDN returns a wrong or outdated file to users’ requests.
- The file from the CDN cache and from the origin are mismatched.

To check the Purge option and fix an error:

1\. Wait 15 minutes after purging until the cache is cleared on all servers.

2\. Run the following two commands in the terminal or console to request the same file from both the source and the CDN:

```
curl -I cdn.example.com/image.png
curl -H "Host: example.com" -I http(s)://10.0.0.1/image.png
```

where:

- *cdn.example.com* is the personal domain of your CDN resource
- *image.png* is the path of the file that is delivered via the CDN
- *http(s)* depends on the protocol used by the source
- *example.com* is the value of the Host header
- *10.0.0.1* is the IP address of your website source

3\. Compare outputs, paying attention to the values of the following headers:

- Content-Length, which is the object size in bytes
- ETag, which is the character set that the CDN compares to know if the file was changed
- X-Cached-Since, which is the time in UTC format

If you see that the **Etag** and **Content-Length** values of the two files don’t match or that the date in the **X-Cached-Since** header is outdated, it means that there is a mistake. In this case, you should go to the next step.

If the values are the same and the date is relevant, purging has been performed correctly.

4\. Try to repeat purging according to the "<a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">Clear CDN resource cache by URL, pattern or all</a>" guide. Pay attention to the path pattern if you select Selective purge. We recommend checking whether the pattern was right by using the <a href="https://regex101.com" target="_blank">regular expressions</a> service. To do this, enter the path pattern for purging on the top line, and in the bottom area, enter the URL of the file. If you see the result “no matches”, there was an error in the path pattern. Correct the path pattern and repeat purging.

If the problem persists after performing troubleshooting according to this guide, contact support via chat or email at [support@gcore.com](mailto:support@gcore.com). You may have an atypical problem that requires assistance from technical specialists. We’ll be happy to help!