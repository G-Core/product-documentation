---
title: configure-http-2-on-the-origin
displayName: HTTP/2
published: true
order: 20
toc:
   --1--Server Configuration: "server-configuration"
   --2--Nginx: "for-nginx"
   --2--Apache: "for-apache"
   --1--Benefits: "benefits-of-http2-for-cdn"
pageTitle: Configuring HTTP/2 on Origin Server | Gcore 
pageDescription: Detailed steps to configure HTTP/2 on Nginx and Apache servers and how this protocol improves CDN performance.
---
# Сonfigure HTTP/2 on the origin

Our nodes support HTTP/2. This option is enabled on all servers by default. Thus, if a user's browser supports HTTP/2, a CDN delivers content via this protocol. 

This standard is supported by Google Chrome, Opera, Mozilla Firefox, Internet Explorer 11, Safari, Amazon Silk and Microsoft Edge. However, at present HTTP/2 works in browsers only for https requests, so to use this option, add an SSL certificate to you CDN Resource.

If your server doesn't support HTTP/2 but a client requests CDN content via HTTP/2, a CDN will deliver the content via HTTP/2, other content — via your server protocol. Browsers can speak different protocols to different domains, and they are able to merge the content they receive from those different domains into a single page.

## Server Configuration

We recommend configuring your web server so that the content could be delivered via HTTP/2 in a proper way.  

### For Nginx

**Requirements** 

Version: 1.9.5 or later (if you have an earlier version, please upgrade).

Setup:

Open ```/etc/nginx/nginx.conf``` and replace the line in the "Server" section

```
listen 443 ssl;
```

with

```
listen 443 ssl http2;
```

Save changes and restart Nginx with the command:

```
$ sudo service nginx reload  
```

### For Apache

**Requirements**

Version: 2.4.17 or later (if you have an earlier version, please upgrade).

Setup:

Enable the <a href="https://httpd.apache.org/docs/2.4/mod/mod_http2.html" target="_blank">mod_http2</a> module (it also can be called mod_h2_module).

Add these lines to the configuration file

```
# for a https server  
Protocols h2 http/1.1
```

```
# for a http server  
Protocols h2c http/1.1
```

Restart Apache.  
  
## Benefits of HTTP/2 for CDN

There is no need to create several CNAME records using HTTP/2. One TCP connection is set up and the load goes through it. There will not be any latency due to several simultaneous connections.