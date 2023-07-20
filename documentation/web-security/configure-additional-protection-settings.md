---
title: configure-additional-protection-settings
displayName: Configure protection settings
published: true
order: 40
toc:
   --1--Change your IP: "change-your-ip"
   --1--Check your DNS records: "check-your-dns-records"
   --1--Check your HTML code: "check-your-html-code"
   --1--Set IP access policy: "set-ip-access-policy"
   --1--Configure your mail service: "configure-your-mail-service"
   --1--Restore users' IP addresses: "restore-users-ip-addresses"
   --1--Reduce server load: "reduce-server-load"
   --1--IPv6: "ipv6"
pageTitle: Additional Protection Settings | Gcore
pageDescription: IP change, check DNS records and other ways to increase protection for your resource.
---
# Configure additional protection settings

Good website protection requires a layered approach. We described the main settings in the "<a href="https://gcore.com/docs/web-security/create-and-configure-a-protected-resource" target="_blank">Create and configure resource under protection</a>" article. Implement additional protective measures to minimize the website vulnerability.

## Change your IP

An attacker can get your real IP using DNS History and attack it directly. Get a new IP and put it in the "Original IP" field in the Control panel. Don't mention/publish the IP anywhere else.

## Check your DNS records

If you have subdomains or other records that point to the real IP, change them to another IP.

## Check your HTML code

Ensure that your HTML code doesn't have references to your real IP.

## Set IP access policy

Limit access to your server for all but our subnets and some trusted IPs. We mention ways to set the limits in the "<a href="https://gcore.com/docs/web-security/deny-access-to-everyone-except-trusted-ips-and-gcore-subnets" target="_blank">Deny access to everyone except trusted IPs and Gcore subnets</a>" article.

## Configure your mail service

Configure a separate email server. If you are running your mail server on the same server as your website, an attacker can find your origin server IP.

## Restore users' IP addresses

<a href="https://gcore.com/docs/web-security/get-an-actual-ip-addresses-of-visitors-from-the-x-forward-for-header" target="_blank">Configure the X-Forwarded-For HTTP header</a> to restore real visitors' IP addresses. Otherwise, you will see requests only from our subnets.

## Reduce server load

Move the static assets (images, video, css, JavaScript) to a subdomain and use <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">CDN</a> to deliver them. It reduces server load and bandwidth. 

## IPv6

By default, we protect only IPv4 addresses, so if your website is also available via IPv6 we recommend removing the A record for IPv6 address from your DNS settings or adding protection for it. The IPv6 protection can be added by request. For details, reach us via chat or email to [support@gcore.com](mailto:support@gcore.com).