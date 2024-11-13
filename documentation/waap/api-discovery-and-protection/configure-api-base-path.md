---
title: configure-api-base-path
displayName: 'Manually add endpoints to API base path'
published: true
order: null
toc: 10
pageTitle: 'A guide on how to configure API base path in Gcore WAAP | Gcore'
pageDescription: 'Learn how to manually add endpoints to API base path so they are protected by WAAP.'
---
# Manually add endpoints to the API base path

If your domain uses APIs hosted on the same domain and you don't have enabled <a href="https://gcore.com/docs/waap/api-discovery-and-protection/api-discovery" target="_blank">API Discovery</a>, you can manually add endpoints to the API base path. This will define a communication path for WAAP to expect API requests and protect your endpoints.  

<alert-element type="info" title="Info">
 
This setting doesn't add API endpoints to the allowlist. 
 
</alert-element>

When you enter a path, note that:  

* Paths are recursively allowed. For example, `api/` allows `api/v1/*`, `api/v2/*`, etc. 

* Regex/wildcard input is not accepted. Use `api/` instead of `api/*`.  

* Don't enter the protocol or domain. Use `api/` instead of `https://example.foobar.com/api/`. The domain is automatically added.  

* Paths are not case-sensitive. `API/` and `api/` are interchangeable.  

* To add multiple APIs, you must create separate entries. 

## Add endpoints to the base path

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/api-discovery-and-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page. 

3\. In the sidebar, click **API Discovery** > **Settings**. 

4\. Navigate to the **API base path** section and in the **Host** field, enter a path to your endpoint. 

5\. Click **Add**. The endpoint will appear in the table under the **Host** field.  

## To remove endpoints from the base path

1\. Find the relevant endpoint and click the three-dot icon next to it. 

2\. Select **Delete**.

3\. Confirm your action by clicking **Delete** again. 

After you configure the API base path, CAPTCHA and JavaScript validation will be disabled for added endpoints.  

The <a href="https://gcore.com/docs/waap/ddos-protection" target="_blank">DDoS protection</a>, <a href="https://gcore.com/docs/waap/waap-policies/ip-reputation" target="_blank">IP reputation</a>, and rate limitation features will continue to protect those endpoints. Custom <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">WAAP rules</a> and <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">firewall rules</a> can also impact content delivery via API and potentially block users.
