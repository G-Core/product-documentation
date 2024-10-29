---
title: advanced-api-protection
displayName: Advanced API protection
published: true
order: 90
toc:
   --1--Configure policy group: "configure-policy-group"
   --2--Auth token protection: "auth-token-protection"
   --2--Sensitive data exposure: "sensitive-data-exposure"
   --2--Invalid API traffic: "invalid-api-traffic"
   --2--API-level authorization: "api-level-authorization"
   --2--Non-baselined API requests: "non-baselined-api-requests"      
pageTitle: Set up Advanced API protection WAAP policy for your domain | Gcore
pageDescription: Learn how to enable and customize Advanced API protection policy.
---
# Advanced API protection 

Our WAAP includes a pre-defined Advanced API protection policy group with multiple policies, allowing you to securely manage your API traffic and protect against unwanted or abusive usage of APIs. 

<alert-element type="info" title="Info">
 
This policy group is available in the <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise plan</a>.
 
</alert-element> 

## Configure policy group 

Before you enable the Advanced API protection policies, you need to <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-access-with-reserved-tags" target="_blank">configure access to APIs by using reserved tags</a>. Without this configuration, the policies will not affect your API traffic. 

You can review the Advanced API protection policy group and enable or disable its policies in the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. On the **Policies** page that opens, click **Advanced API protection** to expand the section and adjust the policies. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/advanced-api-protection/advanced-api-protection.png" alt="WAAP policies page with the highlighted advanced AIP protection policy">

<alert-element type="info" title="Info">

All advanced API protection policies are disabled by default. To enable a policy, turn on the toggle near that policy. 

</alert-element>

### Auth token protection 

Prevent multiple authentication attempts and block access for users who repeatedly try to use invalid tokens to access the API. 

Before enabling this policy, you need to define your 0Auth token endpoints to ensure they are correctly tagged. Learn  instructions on how to do this, check out the <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">Tag generating rules</a> guide. 

### Sensitive data exposure 

Block API responses that contain personally identifiable information (PII) such as phone numbers, SSNs, email addresses, or credit card numbers. 

You can turn off this policy for specific API endpoints by tagging them as needed. In this case, you’ll remain protected against unknown sensitive data leakage, while allowing legitimate known resources to create a response without being interrupted by the WAAP.

### Invalid API traffic 

Block API requests that don’t conform to a JSON structure. This policy protects your APIs by inspecting the keys and values within the JSON. If they are not properly structured, the request will be blocked. 

### API-level authorization 

There are three levels of API endpoint authorization: 

* **Admin**: Users who can access any endpoint. 

* **Privileged**: Users who can access privileged access endpoints. 

* **Non-privileged**: Users who will be blocked from all access endpoints that are privileged or admin. 

To ensure only admins and privileged users can access sensitive endpoints, you can create tags that will be applied when the defined header, token, or other identifier is present. You can then use the <a href="https://gcore.com/docs/waap/api-discovery-and-protection/api-discovery" target="_blank">API Discovery</a> feature and create <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-access-with-reserved-tags" target="_blank">WAAP rules</a> to control API access based on these tags. 

### Non-baselined API requests 

Enable a positive security policy that blocks requests to endpoints that aren’t part of the API baseline—a defined version of your API where all protected endpoints are listed. 

You can also add endpoints to the <a href="https://gcore.com/docs/waap/api-discovery-and-protection/api-discovery#api-baseline" target="_blank">API baseline</a> if you don’t want to perform a network or API specification file scan.