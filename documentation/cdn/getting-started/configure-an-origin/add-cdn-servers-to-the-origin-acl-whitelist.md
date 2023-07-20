---
title: add-cdn-servers-to-the-origin-acl-whitelist
displayName: Add CDN servers to ACL
published: true
order: 10
toc:
   --1--Whitelist CDN by HTTP headers: "whitelist-via-http-headers"
   --1--Whitelist CDN by IP addresses: "whitelist-via-ip-addresses"
pageTitle: Whitelisting CDN Servers for Origin Access | Gcore
pageDescription: A comprehensive guide on whitelisting CDN servers via HTTP headers or IP addresses to ensure uninterrupted content delivery.
---
# Add CDN servers to the origin ACL whitelist
  
If you have restrictions on your origin, there are two ways to whitelist the CDN servers:

- via HTTP headers (recommended)
- via CDN servers' IP addresses

## Whitelist via HTTP headers

Use the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin" target="_blank">Add Request Headers</a> option to set up a custom header.

We recommend this method as it does not require any further update once it is set up. In contrast, the list of IP addresses must be regularly updated.

## Whitelist via IP addresses

To get the IP addresses of the CDN servers, use this API request:

```
curl -i -X GET https://api.gcore.com/cdn/public-ip-list
```

**Note**: We are continually expanding our network, so the list of servers is constantly changing. If you fail to add the IP address of your new server to the whitelist, users will not be able to access content from that edge server.

We recommend that you write a script that automatically updates your ACL. New IP addresses are added to our list 30-60 minutes prior to launching a new server.