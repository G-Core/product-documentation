---
title: how-do-i-renew-my-ssl-certificate
displayName: Renew SSL certificates
published: true
order: 150
toc:
pageTitle: FAQ. Renew SSL certificates attached to your resources under protection | Gcore
pageDescription: How to renew an SSL certificate depending on its type—Let's Encrypt or Custom. 
---
# How do I renew my SSL certificate?

Depending on the type of SSL certificate selected for the resource under protection, there are two options for renewing certificates.

1. If you have **Let's Encrypt**, it will be renewed automatically.

2. If you have a **Custom** certificate, you must reissue it yourself via the certificate authority, delete the current certificate in your resource settings, and add the reissued certificate in the Customer portal according to the <a href="https://gcore.com/docs/web-security/add-an-ssl-certificate-to-your-resource#add-custom-certificate-to-your-resource" target="_blank">Add Custom certificate</a> to your resource guide. You can also add a reissued custom certificate via the API request: 

```
// @name Get client ddos resource
GET {{base_ddos}}/resources/<resource_id>
Authorization: Bearer {{token_client}}
Content-Type: application/json

> {%
	client.global.set("resource", JSON.stringify(response.body.resource));
%}

###

// @name Update custom SSL certificate for the ddos resource
< {%
	let resource = client.global.get("resource");
	resource = JSON.parse(resource);
	resource["service_ssl_crt"] = "-----BEGIN CERTIFICATE-----\n<certificate_data>\n-----END CERTIFICATE-----";
	resource["service_ssl_key"] = "-----BEGIN PRIVATE KEY-----\n<private_key_data>\n-----END PRIVATE KEY-----";
	resource = JSON.stringify(resource);
	request.variables.set("resource_custom_cert", resource);
%}
PUT {{base_ddos}}/resources/<resource_id>
Authorization: Bearer {{token_client}}
Content-Type: application/json

{{resource_custom_cert}}
```

**Note**: We do not automatically notify you of SSL certificate expiry dates, so you should monitor the expiry date yourself.

