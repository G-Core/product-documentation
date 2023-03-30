---
title: 5xx-error-how-to-solve-server-issues
displayName: 5xx codes
published: true
order: 70
toc:
   --1--Check for incidents or maintenances: "check-for-incidents-or-maintenances"
   --1--Check your origin server: "check-your-origin-server"
   --2--Check settings of your CDN-resource: ""
   --2--Incorrect Origin Pull Protocol: "incorrect-origin-pull-protocol"
   --2--Incorrect Host Header: "incorrect-host-header"
---
_**HTTP 5xx codes**_ can be caused by an error on an origin server or CDN edge servers.

  
   

Check for incidents or maintenances
===================================

If you have noticed a significant increase of 5xx codes or received multiple complaints from users, we recommend checking our [Status Page](https://status.gcorelabs.com/#cdn) for incidents or maintenance associated with the following services: 

\- CDN service,

\- other Gcore services (if you use one of them as an origin: Storage, VPS, Dedicated Server, Cloud). 

Check your origin server
========================

Make sure that your origin server is available.

If the origin is not responding, or it is returning an HTTP error, contact your hosting provider or server’s administrator to solve this issue. 

*   **_HTTP 504 error_** usually appears when an origin server fails to respond in time: the CDN edge servers wait for 5 seconds and, if an origin server is not responding, they return a 504 error. Change the settings of your origin to respond in time. 
*   **_If you restrict access to your origin by IP or use DDoS Protection service_**,  make sure that you’ve whitelisted the CDN edge servers. Use an API request below to receive the list of IP: 

curl -i -X GET [https://api.gcore.com/cdn/public-ip-list](https://api.gcore.com/cdn/public-ip-list) [](https://api.gcorelabs.com/cdn/public-ip-list)

**!** We constantly update this list and suggest you two solutions: creating a script to keep the origin whitelist regularly updated or using the HTTP header authorization. Find more about ACL in this [article](https://gcore.com/support/articles/360000208709/). 

Check your CDN resource settings  
==================================

HTTP 5xx errors can be caused by incorrect CDN resource's settings. Check the list of the most common errors below.

Incorrect origin pull protocol 
-------------------------------

Check the origin pull protocol in the resource’s settings and make sure that your origin server uses the same protocol. For more information about this feature, refer the [article](https://gcore.com/support/articles/214493065/).

If you use _Cloudflare_ or _CloudFront_ services as an origin server, select "HTTP" as the origin pull protocol. If your origin only supports HTTPS, or it has a redirect from HTTP to HTTPS, contact our Technical Support ([support@gcore.com](mailto:support@gcore.com)) to add settings. 

Incorrect Host header
---------------------

Check the "Change Host Header" option. Make sure that the option is active, and the value is the same as the Origin Source or match with the host that you have set up on the Origin. For more information about Host Header, refer [here](https://gcore.com/support/articles/360003612697/). 

To track the amount of 5xx errors use the Response codes statistic on the [Report](https://support.gcore.com/hc/en-us/articles/115004917425) tab. 

To receive detailed data about error responses, use our paid feature Raw Logs. Check the [article](https://gcore.com/support/articles/115000511685/) to know more about Raw logs receiving set up and logs’ fields specifications.