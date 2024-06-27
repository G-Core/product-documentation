---
title: anti-automation-and-bot-protection
displayName: Anti-automation and bot protection
published: true
order: 50
pageTitle: Set up Anti-automation and bot protection WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize Anti-automation and bot protection policy.
---
# Anti-automation and bot protection

The Web Application Firewall (WAF) uses <a href="https://gcore.com/docs/waap/waf-policies/behavioral-waf" target="_blank">advanced behavioral analysis</a> to block non-human traffic from accessing your application. Such traffic includes scanners, bots, and other automated tools.  

To protect your site from malicious attacks, we use ❗️ JavaScript injection. This method ensures that we get all the necessary information needed to block automated traffic from reaching your origin server. At the same time, all known bots, such as search engines, can still access your app.  

## Configure policy rules

Our WAF includes a pre-defined Anti-automation & bot protection policy to protect your site from automated traffic. You can review the policy and enable or disable its rules in the Gcore Customer Portal: 

You can review the Advanced API protection policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/anti-automation-bot-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **Anti-automation and bot protection** to expand the section and adjust the policy rules. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/anti-automation-bot-protection/anti-automation.png" alt="WAF policies page with the highlighted Anti-automation and bot protection policy">

<alert-element type="info" title="Info">

Only the **Traffic anomaly** rule is enabled by default. To activate other rules, turn on the toggles near those rules. 

</alert-element>

### Traffic anomaly 

Challenge or block requests when the user or device doesn’t maintain cookies or execute JavaScript correctly. If this happens, users are presented with either CAPTCHA or JavaScript validation screen.  

### Automated clients 

Challenge or block requests from automated sessions. Automated clients are usually bots looking to hack, spam, spy, or generally compromise your website. Activating this rule will detect these types of requests and force human interaction. 

You can review a list of known bots and allow or block their activity within the common automated services ruleset. Learn more about enabling and troubleshooting WAF bot protection in <a href="https://gcore.com/docs/waap/bot-protection/" target="_blank">our dedicated guide</a>. 

### Headless browsers 

Challenge or block requests from users or devices that use automation tools to launch browsers. Headless browsers are sometimes used to perform DDoS attacks on websites, increase advertisement impressions, or automate websites in unintended ways. Activate this rule to protect your site from these types of attacks. 

### Anti-scraping 

Challenge or block requests when a user or device uses an automation tool with rapid and aggressive scraping practices.  

In certain cases, you may want to disable this rule. For example, if you have a travel website with aggregated data and you want to allow your partner sites to extract and display information on their own. 