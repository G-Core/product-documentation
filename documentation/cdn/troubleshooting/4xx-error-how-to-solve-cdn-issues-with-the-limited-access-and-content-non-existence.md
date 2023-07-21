---
title: 4xx-error-how-to-solve-cdn-issues-with-the-limited-access-and-content-non-existence
displayName: 4xx codes
published: true
order: 60
toc:
   --1--Check the content availability on the Origin source: "check-the-content-availability-on-the-origin-source"
   --1--Check your CDN resource's settings: "check-your-cdn-resources-settings"
pageTitle: Solving 4xx Issues | Gcore 
pageDescription: Checking your Origin availability and resource settings.
---
# 4xx error: how to solve CDN issues with the limited access and content non-existence.

4xx errors could be caused by a malfunction on the Origin side or incorrect CDN-resource settings. 

## Check the content availability on the Origin source

Request the content from the origin source and ensure you get an HTTP 200 response code. 

If you use IP Whitelist on the origin or a DDoS protection service, ensure that CDN-edges IPs are whitelisted. Use the API request above to get the list of Public IP 

```
curl -i -X GET https://api.gcore.com/cdn/public-ip-list
```

Since we constantly update the Public IP list, we recommend you run a script for the regular whitelist updating. You can also use HTTP Request Header for the authentication on your origin. You may find out more about the <a href="https://gcore.com/docs/cdn/getting-started/configure-an-origin/add-cdn-servers-to-the-origin-acl-whitelist" target="_blank">Origin ACL</a>.

## Check your CDN resource's settings 

- Ensure that the CDN resource is active. If you have created a new resource, wait until its configuration is applied on CDN-edges. Usually, it takes 15 minutes. 
- Ensure that Origin can respond to the requests from CDN edges by choosing Origin Pull Protocol. You may learn more about this option from the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/specify-an-origin-and-the-origin-pull-protocol" target="_blank">article</a>. 
- Check the Change Host Header option. Make sure that the option is active and the value is the same as the Origin Source or match with the host that you have set up on the Origin. You may find more information about <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Host Header</a>. 
Go to the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Reports</a> tab to track the amount of 4xx errors. 

To receive more details about users’ requests to resources, use the Raw logs option. It is a paid feature The Raw log receiving setup flow and the description of logs’ fields are located <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage" target="_blank">here</a>. If you want to activate this feature, contact your account manager or send a request to technical support ([support@gcore.com](mailto:support@gcore.com)).