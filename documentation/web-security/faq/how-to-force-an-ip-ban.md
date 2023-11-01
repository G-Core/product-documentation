---
title: how-to-force-an-ip-ban
displayName: Force an IP ban
published: true
order: 130
toc:
   --1--Force in customer portal: "force-an-ip-ban-in-the-customer-portal"
   --1--Force via API: "force-an-ip-ban-via-api"
pageTitle: FAQ. Force an IP ban | Gcore
pageDescription: How to force an IP ban in the customer portal and via API. 
---
# How to force an IP ban?

You can force an IP or subnet mask ban using a whitelist policy. This allows requests from all IPs or subnets, except specified IPs or subnet masks.

**Note**: To ban all IPs or subnets *except specified values*, select the blacklist option.

You can set an IP ban in two ways: in the customer portal or via the API. 

## Force an IP ban in the customer portal

1\. Go to your <a href="https://control.gcore.com/resources/all" target="_blank">list of resources under protection</a>.

2\. Click three dots on the line of the relevant resource and click **Access Policy**.

<img src="https://assets.gcore.pro/docs/web-security/faq/how-to-force-an-ip-ban/force-ip-ban-10.png" alt="How to open Access Policy settings of the resource under protection" width="80%">

3\. On the page that opens, type the IPs or subnet masks in the “Whitelist” field (click the plus button on the right to add more than one) and save changes. 

<img src="https://assets.gcore.pro/docs/web-security/faq/how-to-force-an-ip-ban/force-ip-ban-20.png" alt="How to force an IP ban" width="80%">

That’s it. The specified IP will be banned for two hours. 

## Force an IP ban via API

Here’s an example of restricting a specific IP using an API request:

```
// @name Get client ddos resource
GET https://api.gcore.com/security/resources/<resource_id>
Authorization: Bearer {{token_client}}
Content-Type: application/json
> {%
	client.global.set("resource", JSON.stringify(response.body.resource));
%}
###
// @name Add whitelist into ddos resources
< {%
	let resource = client.global.get("resource");
	resource = JSON.parse(resource);
	resource["whitelists"] = [{"whitelist_data": "3.3.3.3"}];
	resource = JSON.stringify(resource);
	request.variables.set("resource_whitelist", resource);
%}
PUT https://api.gcore.com/security/resources/<resource_id>
Authorization: Bearer {{token_client}}
Content-Type: application/json
{{resource_whitelist}}
```