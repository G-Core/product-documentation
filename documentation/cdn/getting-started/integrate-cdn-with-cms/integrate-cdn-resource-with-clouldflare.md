---
title: integrate-cdn-resource-with-clouldflare
displayName: ClouldFlare
published: true
order: 30
toc:
    --1-CNAME record setup: "cname-record-setup"
    --1--Origin Pull Protocol setup: "origin-pull-protocol-setup"
---
CNAME record setup
------------------

If you use the CloudFront DNS service, the CloudFront servers function as proxy for all DNS records. The CloudFlare's DDoS protection and CDN services are based on that.

If you want to use Gcore as your CDN provider, disable the proxying in the CloudFlare DNS settings by clicking the cloud icon during the [CNAME record creation.](https://www.gcore.com/support/articles/213969769/)

<img src="https://support.gcore.com/hc/article_attachments/360004882677/1574936519330.png" alt="1574936519330.png">

Origin Pull Protocol setup
--------------------------

Due to the differences in our and CloudFlare's infrastructures, if you set HTTPS as your "Origin Pull Protocol", you will likely start getting 502 errors. 

To avoid it, add the [Change SNI Hostname](https://www.gcore.com/support/articles/360017569777/) option in the Security section or change "Origin Pull Protocol" to HTTP.