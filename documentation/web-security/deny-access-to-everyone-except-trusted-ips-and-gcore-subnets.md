---
title: deny-access-to-everyone-except-trusted-ips-and-gcore-subnets
displayName: Deny access
published: true
order: 70
toc:
   --1--Network Firewall: "network-firewall"
   --1--Web server: "web-server"
   --2--Apache: "apache"
   --2--Nginx: "nginx"
pageTitle: Strict Access Restrictions | Gcore
pageDescription: Learn how to bolster your website's security by denying access to all but trusted IPs and Gcore subnets using Network Firewall or web server configurations.
---
# Deny access to everyone except trusted IPs and Gcore subnets

To minimize your website vulnerability, deny access to it for all but Gcore's subnets and your trusted IP addresses.  
  
## Network Firewall

Different hosting providers offer different firewalls (often for additional cost) so there is no one-for-all manual. The goal is to limit access for non-Gcore subnets. Contact us via chat or email to [support@gcore.com](mailto:support@gcore.com) to get an up-to-date list of subnets.  
  
## Web server

Don't use this method if you have set the <a href="https://gcore.com/docs/web-security/get-an-actual-ip-addresses-of-visitors-from-the-x-forward-for-header" target="_blank">X-Forwarded-For header</a>: the requests will be blocked.

### Apache

Example lines that should be added to **.htaccess** file (static trusted IP addresses can also be added):

```
order deny, allow

deny from all

allow from 13x.2xx.xxx.xxx/24

allow from 13x.2xx.xxx.xxx/24
```

### Nginx

Nginx comes with a module called <a href="https://nginx.org/en/docs/http/ngx_http_access_module.html" target="_blank">ngx_http_access_module</a> to allow or deny access to an IP address. Below are example strings that should be added to your server configuration (static trusted IP addresses can also be added):

```
location / {

allow 13x.2xx.xxx.xxx/24;

allow 13x.2xx.xxx.xxx/24;

deny all;

}
```