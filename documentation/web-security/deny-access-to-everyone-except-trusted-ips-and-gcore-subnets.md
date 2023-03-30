---
title: deny-access-to-everyone-except-trusted-ips-and-gcore-subnets
displayName: Deny access
published: true
order: 70
toc:
---
To minimize your website vulnerability, deny access to it for all but Gcore's subnets and your trusted IP addresses.  
  
Network Firewall

Different hosting providers offer different firewalls (often for additional cost) so there is no one-for-all manual. The goal is to limit access for non-Gcore subnets. Contact us via chat or email to [support@gcore.com](mailto:support@gcorelabs.com) to get an up-to-date list of subnets.  
  
Web server

_Don't use this method if you have set the [X-Forwarded-For](https://support.gcorelabs.com/hc/en-us/articles/360000569538-Restoring-Visitor-IPs) header: the requests will be blocked._

Apache

Example lines that should be added to .htaccess file (static trusted IP addresses can also be added):

_order deny, allow_

_deny from all_

_allow from 13x.2xx.xxx.xxx/24_

_allow from 13x.2xx.xxx.xxx/24_

Nginx

Nginx comes with a module called [ngx\_http\_access\_module](https://nginx.org/en/docs/http/ngx_http_access_module.html) to allow or deny access to an IP address. Below are example strings that should be added to your server configuration (static trusted IP addresses can also be added):

_location / {_

_allow 13x.2xx.xxx.xxx/24;_

_allow 13x.2xx.xxx.xxx/24;_

_deny all;_

_}_