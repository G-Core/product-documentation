---
title: get-actual-ip-addresses-of-visitors-from-the-x-forward-for-header
displayName: Set the X-Forward-For header
published: true
order: 80
toc:
   --1--Why use X-Forwarded-For: "why-use-the-x-forwarded-for-header"
   --1--Configure: "configure-the-realip-module-on-your-server"
   --2--Nginx: "nginx"
   --2--Apache: "apache"
pageTitle: X-Forward-For Header Usage | Gcore 
pageDescription: A guide on how to get actual IPs of visitors with the X-Forward-For header.  
---
# Get actual IP addresses of visitors from the X-Forward-For header

## Why use the X-Forwarded-For header

When you enable <a href="https://gcore.com/web-security" target="_blank">Web Application Security</a>, our servers function as a reverse proxy and filter requests to your server. By default, only our IP addresses will be visible in the access logs. If you want to obtain the actual IP addresses of your visitors, you can configure your system to retrieve the addresses from the *X-Forwarded-For* header using the *realip* module.

## Configure the realip module on your server

### Nginx

1\. Use the <a href="https://nginx.org/en/docs/http/ngx_http_realip_module.html" target="_blank">ngx_http_realip_module</a> and add two key directives: *set_real_ip_from* and *real_ip_header*.

- The *set_real_ip_from* directive specifies the trusted subnets.

```
set_real_ip_from 9х.ххх.ххх.х/24;  
set_real_ip_from 1хх.ххх.ххх.0/24;  
set_real_ip_from 9х.ххх.ххх.х/24;  
```

Contact the support team via email at [support@gcore.com](mailto:support@gcore.com) or through chat to get the up-to-date list of subnets.

- The real_ip_header directive indicates that the IP addresses are contained in the X-Forwarded-For header.

```
real_ip_header X-Forwarded-For;
```

2\. (Optional) Add *$http_x_forwarded_for* variable in the log_format directive to display visitors' real IP addresses in access logs.

3\. Restart Nginx.

### Apache

1\. Use the <a href="https://httpd.apache.org/docs/2.4/mod/mod_remoteip.html" target="_blank">mod_remoteip module</a> for configuration and several key directives to the configuration file, with minor differences depending on the OS (RHEL/CentOS or Debian/Ubuntu).

- The following directive specifies that the *remoteip* module should be loaded:

```
# LoadModule remoteip_module modules/mod_remoteip.so ()
```

- The following directive indicates that the IP addresses are contained in the X-Forwarded-For header:

```
# RemoteIPHeader X-Forwarded-For
```

- The following directives indicate that the Gcore nodes are trusted:

```
# RemoteIPTrustedProxy 9х.ххх.ххх.х/24;  
# RemoteIPTrustedProxy 1хх.ххх.ххх.х/24;  
# RemoteIPTrustedProxy 9х.ххх.ххх.х/24;  
```

Contact the support team via email at [support@gcore.com](mailto:support@gcore.com) or through chat to get the up-to-date list of subnets.

2\. Save changes.

3\. Restart Apache.
