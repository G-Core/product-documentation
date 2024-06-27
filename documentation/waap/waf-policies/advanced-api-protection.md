---
title: advanced-api-protection
displayName: Advanced API protection
published: true
order: 80
pageTitle: Set up Advanced API protection WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize Advanced API protection policy.
---
# Advanced API protection 

The Web Application Firewall (WAF) offers Web Application and API Protection (WAAP) capabilities that allow you to protect both your web apps and APIs simultaneously.  

Our WAF includes a pre-defined Advanced API protection policy with multiple rules, allowing you to securely manage your API traffic and protect against unwanted or abusive usage of APIs. 

## Configure policy rules 

You can review the Advanced API protection policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/advanced-api-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **Advanced API protection** to expand the section and adjust the policy rules. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/advanced-api-protection/advanced-api-protection.png" alt="WAF policies page with the highlighted advanced AIP protection policy">

<alert-element type="info" title="Info">

All advanced API protection rules are disabled by default. To enable a rule, turn on the toggle near that rule. 

</alert-element>

### Auth token protection 

Prevent multiple authentication attempts and block access for users who repeatedly try to use invalid tokens to access the API. 

Before enabling this rule, you need to define your 0Auth token endpoints to ensure they are correctly tagged. For instructions on how to do this, check out our guide Tag Generating Rules. 

### Sensitive data exposure 

Block API responses that contain Personal Identifiable Information (PII) such as phone numbers, SSNs, email addresses, or credit card numbers. 

You can turn off this rule for specific API endpoints by tagging them as needed. In this case, you’ll remain protected against unknown sensitive data leakage, also allowing legitimate known resources to create a response without being interrupted by the WAF.

❗️You can find more information about ignoring sensitive data exposure in our Tag generating rules guide. 

### Invalid API traffic 

Block API requests that don’t conform to a JSON structure. This policy protects your APIs by inspecting the keys and values within the JSON. If they are not properly structured, the request will be blocked. 

### API-level authorization 

There are three levels of API endpoint authorization: 

* **Admin**: Users who can access any endpoint. 

* **Privileged**: Users who can access privileged access endpoints. 

* **Non-privileged**: Users who will be blocked from all access endpoints that are privileged or admin. 

To ensure that only admins and privileged users can access sensitive endpoints, you can create tags that will be applied when the defined header, token, or other identifier is present. ❗️ You can then use the API Discovery feature to control API access based on these tags. 

❗️ For details about API-level authorization, check out the Tag generating rules guide. 

### Non-baselined API requests 

❗️Enable a positive security policy that blocks requests to endpoints that aren’t part of the API baseline—a defined version of your API where all protected endpoints are listed.  

You can also add endpoints to the API baseline if you don’t want to perform a network or API specification file scan.  