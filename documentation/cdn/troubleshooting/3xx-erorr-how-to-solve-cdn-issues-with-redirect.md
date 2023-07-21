---
title: 3xx-erorr-how-to-solve-cdn-issues-with-redirect
displayName: 3xx codes
published: true
order: 50
toc:
   --1--Origin Pull Protocol: "origin-pull-protocol"
   --1--Change Host Header: "change-host-header"
pageTitle: Solving 3xx Issues | Gcore  
pageDescription: Changing the origin pull protocol or host header to solve redirecting issues. 
---
# 3xx erorr: how to solve CDN issues with redirect

If you request content from CDN and receive a redirect (301 or 302 HTTP codes) to the Origin source, check the following CDN resource's settings. 

## Origin Pull Protocol 

Choose an origin pull protocol that matches redirect settings on your origin. 

- Choose HTTPS if your origin redirects HTTP requests to HTTPS. 
- Choose HTTP if your origin redirects HTTPS requests to HTTP. 

## Change Host Header

Usually, the Host Header matches the Origin Source’s domain. Specify the correct Host Header or configure the processing of already specified Host Header on the origin source.

If your Origin redirects requests to another domain put this end-domain as Origin of the CDN-resource. 

For example, if requests to _domain.com_ are redirected to _www.domain.com_, put _www.domain.com_ as the Origin source. 

Go to the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Reports</a> tab to track the amount of 3xx codes.

To receive more details about user’s requests to CDN-resources you may use the Raw logs. This is the paid feature. The Raw log receiving setup flow and the description of logs’ fields are specified here. If you want to activate this feature, contact your account manager or send a request to the [technical support](mailto:support@gcore.com).