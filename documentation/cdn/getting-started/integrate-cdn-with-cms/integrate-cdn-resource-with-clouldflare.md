---
title: integrate-cdn-resource-with-clouldflare
displayName: ClouldFlare
published: true
order: 30
toc:
   --1--CNAME record setup: "cname-record-setup"
   --1--Origin Pull Protocol setup: "origin-pull-protocol-setup"
pageTitle: Integrate CDN with ClouldFlare Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with ClouldFlare CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with ClouldFlare

## CNAME record setup

If you use the CloudFront DNS service, the CloudFront servers function as proxy for all DNS records. The CloudFlare's DDoS protection and CDN services are based on that.

If you want to use Gcore as your CDN provider, disable the proxying in the CloudFlare DNS settings by clicking the cloud icon during the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record creation</a>.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-clouldflare/1574936519330.png" alt="CNAME record setup" width="50%">

## Origin Pull Protocol setup

Due to the differences in our and CloudFlare's infrastructures, if you set HTTPS as your "Origin Pull Protocol", you will likely start getting 502 errors. 

To avoid it, add the <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/set-the-hostname-passed-in-sni-requests-to-the-origin-server" target="_blank">Change SNI Hostname</a> option in the "Security" section or change "Origin Pull Protocol" to HTTP.