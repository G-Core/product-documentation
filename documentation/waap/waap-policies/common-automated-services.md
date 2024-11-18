---
title: common-automated-services
displayName: Common automated services
published: true
order: 80
pageTitle: Set up Common automated services WAAP policy group for your domain | Gcore
pageDescription: Learn how to enable and customize common automated services policy.
---
# Common automated services

This policy group functions uniquely in WAAP. Instead of challenging or blocking incoming traffic like other policy groups, it’s designed to recognize and allow traffic from legitimate automated services.  

These services include: 

* Common web crawlers like Google and Microsoft bots
* Preview fetch bots like Slack, Facebook, or Twitter
* SEO and monitoring tools
* Other tools like Instant Payment Notification (IPN) requests from PayPal or HiPay 

All these automation services often access your domain to gather some information and are considered beneficial or necessary for normal web activities. Note that some policies are disabled by default, and you need to enable them to permit traffic from the relevant services. 

In some cases, you might want to do the opposite and restrict automation tools from accessing your domain. For instance, you can do so to enforce specific data protection requirements on a domain, protect it from potentially harmful services, or restrict paid content from unauthorized use. In this case, disable particular bots in the Common automated services policy group. 

<alert-element type="info" title="Info">
 
This policy group is available in the <a href="https://gcore.com/docs/waap/billing#pro" target="_blank">Pro</a> and <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise</a> plans.
 
</alert-element> 

## Configure policy group

You can review and enable relevant policies in the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>:

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/domains-waap-page.png" alt="Domains page in the Customer Portal" width="80%">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. On the **Policies** page that opens, click **Common automated services** to expand the section and adjust the policies. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/common-automated-services/common-automated-services.png" alt="Domains page in the Customer Portal" width="80%">

