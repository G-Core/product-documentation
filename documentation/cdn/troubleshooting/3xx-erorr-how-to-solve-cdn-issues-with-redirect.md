---
title: 3xx-erorr-how-to-solve-cdn-issues-with-redirect
displayName: 3xx codes
published: true
order: 50
toc:
---
If you request content from CDN and receive a redirect (301 or 302 HTTP codes) to the Origin source, check the following CDN resource's settings. 

Origin Pull Protocol 

Choose an origin pull protocol that matches redirect settings on your origin. 

*   Choose HTTPS if your origin redirects HTTP requests to HTTPS. 
*   Choose HTTP if your origin redirects HTTPS requests to HTTP. 

Change Host Header

Usually, the Host Header matches the Origin Source’s domain. Specify the correct Host Header or configure the processing of already specified Host Header on the origin source.

If your Origin redirects requests to another domain put this end-domain as Origin of the CDN-resource. 

For example, if requests to _**domain.com**_ are redirected to _**www**__**.domain.com**_, put **_www.domain.com_** as the Origin source. 

Go to the [Reports](https://gcore.com/support/articles/115004917425/) tab to track the amount of 3xx codes.

To receive more details about user’s requests to CDN-resources you may use the Raw logs. This is the paid feature. The Raw log receiving setup flow and the description of logs’ fields are specified here. If you want to activate this feature, contact your account manager or send a request to the Technical Support (support@gcore.com).