---
title: enable-troubleshoot-bot-protection
displayName: Enable and troubleshoot bot protection 
published: true
order: 10
pageTitle: Enable and troubleshoot bot protection | Gcore
pageDescription: Learn how to enable and troubleshoot bot protection for your domain.
---
# Enable and troubleshoot bot protection

Hackers use bots to scan a web application's front-end environment and exploit vulnerabilities for access and control. 

Gcore <a href="https://gcore.com/docs/waap/waap-policies/anti-automation-and-bot-protection" target="_blank">anti-automation and bot protection</a> detects, prevents, and blocks unauthorized vulnerability scans from directly reaching your application. This feature denies hackers the ability to map your site and plan malicious activities.  

Our bot mitigation solution uses the following methods to prevent attackers from accessing your application: 

* **User-Agent detection**. Requests with invalid (known to be malicious) or missing User-Agent strings will be blocked. 

* **Analysis of traffic sources**. Requests from hosting services, TOR exit nodes, proxy, or VPN networks will be required to pass a Handshake (JavaScript validation). 

* **Behavioral analysis**. Requests with unusual user behavior will be challenged or blocked. 

* **Headless browsers and automated clients**. Requests from headless browsers <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules/predefined-tags" target="_blank">will be tagged</a> by our security cloud (behavioral engine) and will have to pass a Handshake (JavaScript validation). 

## View and enable common automated services

WAAP allows known bots and services listed in the common automated services policy group. To view the policy group and enable or disable bots:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/analytics/domains-waap-page.png" alt="Domains page in the Customer Portal" width="80%">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page. 

3\. Click **Common automated services** to expand the section and adjust the policies.  

4\. Review the list of accepted bots and adjust the list as needed. 

<alert-element type="info" title="Info">
 
If you want to add a new bot to the list, contact [Gcore support team](mailto:support@gcore.com) and provide the details. We’ll consider adding that bot in the future.  
 
</alert-element>

## Enable the “Let's Encrypt” policy  

Let's Encrypt is a free, automated, and open certificate authority that provides server-side SSL certificates. Use the following instructions to enable the **Let's Encrypt** policy that will validate requests to create or renew SSL certificates: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/analytics/domains-waap-page.png" alt="Domains page in the Customer Portal" width="80%">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page. 

3\. Click **Common automated services** to expand the policy group.  

4\. Find the **Let's Encrypt** policy and enable the toggle next to it. 

5\. If a renewal is successful, you'll see the confirmation message "Congratulations, all renewals succeeded." If a renewal is not successful, you'll get an error message informing you that renewal attempts have failed. 

## Troubleshoot common automated services  

If you notice that a known crawler or bot is not working or is blocking you, check the following troubleshooting recommendations. 

### Verify that the bot is allowed in the policy group 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. On the **Policies** page that opens, click **Common automated services** to expand the policy group.  

3\. Find the needed bot and make sure that it’s enabled.

### Check security actions enforced on a request 

If the bot is enabled in the **Common automated services** policy group, review the security action. 

When WAAP challenges or blocks bots' requests to your domain, a block response page will be displayed. This page contains a reference ID, which can be used to check the security actions enforced on the request.

If you don't see a reference ID, then you can open each security event until you find a user agent that matches the bot. 

Check the <a href="https://gcore.com/docs/waap/troubleshooting/troubleshoot-blocked-users" target="_blank">Troubleshooting blocked users</a> for detailed instructions on how to inspect and fix such issues. 