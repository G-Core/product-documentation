---
title: get-an-actual-ip-addresses-of-visitors-from-the x-forward-for-header
displayName: Set the X-Forward-For header
published: true
order: 80
toc:
   --1--Why use X-Forwarded-For: "why-use-the-x-forwarded-for-header"
   --1--Configure: "configure-the-realip-module-on-your-server"
   --2--Nginx: "nginx"
   --2--Apache: "apache"
---
  
:  
    •  
    •

Why use the X-Forwarded-For header
----------------------------------

When you enable [Web Application Security](https://www.gcore.com/web-security), our servers function as a reverse proxy and filter requests to your server. By default, only our IP addresses will be visible in the access logs. If you want to obtain the actual IP addresses of your visitors, you can configure your system to retrieve the addresses from the _X-Forwarded-For_ header using the _realip_ module.

Configure the realip module on your server
------------------------------------------

### Nginx

1\. Use the [ngx\_http\_realip\_module](http://nginx.org/en/docs/http/ngx_http_realip_module.html) and add two key directives: _set\_real\_ip\_from_ and _real\_ip\_header_.

*   The _set\_real\_ip\_from_ directive specifies the trusted subnets.

set\_real\_ip\_from 9х.ххх.ххх.х/24;  
set\_real\_ip\_from 1хх.ххх.ххх.0/24;  
set\_real\_ip\_from 9х.ххх.ххх.х/24;  

Contact the support team via email at [support@gcore.com](mailto:support@gcore.com) or through chat to get the up-to-date list of subnets.

*   The real\_ip\_header directive indicates that the IP addresses are contained in the X-Forwarded-For header.

real\_ip\_header X-Forwarded-For;

2\. (Optional) Add _$http\_x\_forwarded\_for_ variable in the log\_format directive to display visitors' real IP addresses in access logs.

3\. Restart Nginx.

### Apache

1\. Use the [mod\_remoteip module](https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html) for configuration and several key directives to the configuration file, with minor differences depending on the OS (RHEL/CentOS or Debian/Ubuntu).

*   The following directive specifies that the _remoteip_ module should be loaded:

\# LoadModule remoteip\_module modules/mod\_remoteip.so ()

*   The following directive indicates that the IP addresses are contained in the X-Forwarded-For header:

\# RemoteIPHeader X-Forwarded-For

*   The following directives indicate that the Gcore nodes are trusted:

\# RemoteIPTrustedProxy 9х.ххх.ххх.х/24;  
\# RemoteIPTrustedProxy 1хх.ххх.ххх.х/24;  
\# RemoteIPTrustedProxy 9х.ххх.ххх.х/24;  

Contact the support team via email at [support@gcore.com](mailto:support@gcore.com) or through chat to get the up-to-date list of subnets.

2\. Save changes.

3\. Restart Apache.