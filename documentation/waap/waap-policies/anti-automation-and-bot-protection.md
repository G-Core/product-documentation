---
title: anti-automation-and-bot-protection
displayName: Anti-automation and bot protection
published: true
order: 50
toc:
   --1--Configure policy group: "configure-policy-group"
   --2--Traffic anomaly: "traffic-anomaly"
   --2--Automated clients: "automated-clients"
   --2--Headless browsers: "headless-browsers"
   --2--Anti-scraping: "anti-scraping"
pageTitle: Set up Anti-automation and bot protection WAAP policy group for your domain | Gcore
pageDescription: Learn how to enable and customize Anti-automation and bot protection policy.
---
# Anti-automation and bot protection

WAAP uses <a href="https://gcore.com/docs/waap/waap-policies/behavioral-waf" target="_blank">behavioral WAF</a> to block non-human traffic from accessing your application, including scanners, bots, and other automated tools.  

To protect your site from malicious attacks, we use <a href="https://gcore.com/docs/waap/frequently-asked-questions/javascript-injection" target="_blank">JavaScript injection</a>. This method ensures that we get all necessary information to block automated traffic from reaching your origin server. Meanwhile, all known bots, such as search engines, can still access your app.  

<alert-element type="info" title="Info">
 
This policy group is available in the <a href="https://gcore.com/docs/waap/billing#pro" target="_blank">Pro</a> and <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise</a> plans.
 
</alert-element> 

## Configure policy group

Our WAAP includes a pre-defined anti-automation & bot protection policy group to protect your site from automated traffic. You can review the policy group and enable or disable its policies in the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. On the **Policies** page that opens, click **Anti-automation and bot protection** to expand the section and adjust the policies. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/anti-automation-bot-protection/anti-automation.png" alt="WAAP policies page with the highlighted Anti-automation and bot protection policy">

<alert-element type="info" title="Info">

Only the **Traffic anomaly** policy is enabled by default. To activate other policies, turn on the toggles near those policies. 

</alert-element>

### Traffic anomaly 

Challenge or block requests when the user or device doesn’t maintain cookies or execute JavaScript correctly. If this happens, users are presented with either CAPTCHA or JavaScript validation screen.  

### Automated clients 

Challenge or block requests from automated sessions. Automated clients are usually bots looking to hack, spam, spy, or generally compromise your website. Activating this policy will detect these requests and force human interaction. 

You can review a list of known bots and allow or block their activity within the <a href="https://gcore.com/docs/waap/waap-policies/common-automated-services" target="_blank">common automated services</a> policy group. Learn more about enabling and troubleshooting bot protection in <a href="https://gcore.com/docs/waap/troubleshooting/enable-troubleshoot-bot-protection" target="_blank">our dedicated guide</a>. 

### Headless browsers 

Challenge or block requests from users or devices that use automation tools to launch browsers. Headless browsers are sometimes used to perform DDoS attacks on websites, increase advertisement impressions, or automate websites in unintended ways. Activate this policy to protect your site from these attacks. 

### Anti-scraping 

Challenge or block requests when a user or device uses an automation tool with rapid and aggressive scraping practices.  

In certain cases, you may want to disable this policy. For example, if you have a travel website with aggregated data and want to allow partners to extract and display information on their own sites. 