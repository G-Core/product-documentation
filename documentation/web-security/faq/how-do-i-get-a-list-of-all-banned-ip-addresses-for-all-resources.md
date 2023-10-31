---
title: how-do-i-get-a-list-of-all-banned-ip-addresses-for-all-resources
displayName: Get all banned IP addresses for all resources
published: true
order: 140
toc:
pageTitle: FAQ. All banned IP addresses| Gcore
pageDescription: How to get a list of all banned IP addresses for all resources via the API request. 
---
#  How do I get a list of all banned IP addresses for all resources?

You can get a list of all banned IP addresses for all Web Security product resources using an API request:

```
// @name Get protected ip addresses
GET https://api.gcore.com/security/resources
Authorization: Bearer {{token_client}}
Content-Type: application/json

> {%
	let ip_list = [];
	for (let resource of response.body) {
    	for (let item of resource["whitelists"]) {
        	ip_list.push(item["whitelist_data"]);
    	}
	}
	client.log(ip_list);
%}
```