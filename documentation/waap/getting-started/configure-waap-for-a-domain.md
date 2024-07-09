---
title: configure-waap-for-a-domain
displayName: Configure WAAP for a domain
published: true
order: 10
pageTitle: Set up Gcore WAAP for your domain | Gcore
pageDescription: Learn how to itegrate your domain with our WAAP and configure initial settings.
---
# Configure WAAP for a domain

Web Application and API Protection (WAAP) is a single SaaS tool that combines all aspects of website security and traffic management, including Layer 7 DDoS protection, and web application security.  

To secure your application with WAAP, you need to create a Gcore CDN resource for your domain, enable WAAP protection in the resource settings, and then verify that everything works as expected and you don’t block legitimate traffic. The following steps will guide you through this process and help you configure WAAP according to your requirements.

<alert-element type="info" title="Info">
 
After you enable WAAP, all traffic will be diverted to our network, and it may cause a temporary disruption for your users. We recommend setting up a WAAP during a low-traffic period to minimize the impact. 

</alert-element>

## Step 1. Create a CDN resource  

To secure your web application or APIs with Gcore WAAP, it’s necessary to create a CDN resource associated with your website’s origin.  

If you don’t have Gcore CDN configured, follow the instructions from this guide: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource" target="_blank">Create a CDN resource</a>. To add an SSL certificate, check out the <a href="https://gcore.com/docs/cdn/ssl-certificates/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">Add an SSL certificate to deliver content over HTTPS</a> guide. 

<alert-element type="info" title="Info">
 
Update your domain’s DNS records so they point to our network. This is necessary to allow all traffic to pass through WAAP.

</alert-element>

## Step 2: Enable WAAP in resource settings 

Once your CDN resource is set up, you can activate WAAP protection for it. Follow instructions from the <a href="" target="_blank">Protect CDN resources with WAAP</a> guide.  

Consider that it might take up to 30 minutes for the HTTP traffic to start passing through our WAAP after the activation. 

## Step 3: Use WAAP in monitor mode 

After you enable WAAP, it will be automatically set to the <a href="https://gcore.com/docs/waap/getting-started/waap-modes#monitor-mode" target="_blank">monitor mode</a>. In this mode, all default WAF rules are enabled. We’ll inspect all incoming requests but won’t take any action. It's best to use monitor mode for several days before enabling the <a href="https://gcore.com/docs/waap/getting-started/waap-modes#protect-mode" target="_blank">protect mode</a> to make sure that all security settings work correctly. 

Completing this step is important because it allows you to analyze requests and test the WAAP behavior before you fully activate it. 

## Step 4: View your domain’s traffic 

While keeping WAAP in monitor mode, you can view all logged requests and check the corresponding actions that the WAAP will take once you put it in the protect mode.  

Go through the <a href="https://gcore.com/docs/waap/analytics" target="_blank">analytics pages</a> to detect common traffic patterns and understand if the current configuration requires any adjustments.  

For instance, you can find information about incoming web requests on the WAF page in the Requests table: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. 

3\. In the sidebar click **Analytics** > **WAF**. 

4\. Review the information under **Requests**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/waf-requests.png" alt="Analytics page in the Customer Portal showing Requests table">

5\. You can also filter requests to get more granular information about your traffic:  

* **Traffic types**: View requests based on the rule that triggered the request. 

* **Policy – Blocked** or **Policy – Allowed**: View requests that triggered our predefined rules. 

* Select **Custom Rule – Blocked** or **Custom Rule – Allowed**: View requests that triggered custom rules created by your account users. 

<alert-element type="info" title="Info">
 
**Policy - Blocked** and **Custom Rule - Blocked** are the default filters automatically displayed for a table.  
 
</alert-element>

To view more information about a request, click the request ID and inspect the **Request Details** page.

<img src="https://assets.gcore.pro/docs/waap/getting-started/request-details.png" alt="Request details section open from the Analytics page">

The screenshot above depicts a request that was blocked because of the **SQL injection** rule. It blocks requests if there is evidence that the request contains malicious SQL code. You can read more about SQL injection and WAF’s top threats in our <a href="https://gcore.com/docs/waap/waf-policies/waf-and-owasp-top-threats#configure-policy-rules" target="_blank">dedicated guide</a>. 

## Step 5: Test your WAAP configuration 

To achieve the desired WAAP behavior, we recommend that you navigate through your website as both a user and administrator.  

Navigating the website will generate entries in the **Requests** table. You can use this information to determine if you need to create IP allowlist rules or custom WAF rules for some requests and let them access your website’s content. 

Specifically, review requests that relate to: 

* **Your origin IP**: IP address assigned to your device. 
* **Your office IP**: IP address assigned to your device within your office's network. 
* **Your workstation IP**: IP address assigned to a workstation or specific computer in a network. 

If you notice that WAAP will block such requests in the protect mode, you need to update your settings to prevent such a situation. You can find detailed instructions on how to update your settings in the following step.  

Check out the <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">allow and block IP addresses</a> guide for more information. 

## Step 6: Allow admins, bots, and CMS 

Before the WAAP is in protection mode, you need to ensure that critical IP addresses, content management systems (CMS), and common automated services are allowed to make successful requests.  

Check <a href="https://gcore.com/docs/waap/waf-policies" target="_blank">predefined WAF policies</a> for a full list of security rulesets and their detailed overview. 

### Allow admin IP addresses

If your domain doesn’t use a CMS, we highly recommend allow listing the site administrator's IP address: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. 

3\. In the sidebar, click **Firewall**. 

4\. In the Allowed IPs section, click **Add IP/IP Range**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/firewall-add-rules.png" alt="Firewall page in the Customer Portal">

5\. Enter any admin user's public IP address. 

6\. Click **Save**. 

Repeat these steps if needed. 

### Allow CMS 

If you use content management systems, such as WordPress, allow traffic for CMS admins:  

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. 

3\. In the sidebar, click **WAF**. 

4\. On the **Policies** page, find CMS protection, and then allow traffic for a desired content management system by enabling a toggle next to it.

<img src="https://assets.gcore.pro/docs/waap/getting-started/cms-protection.png" alt="WAAP policies page with the highlighted CMS protection policy">

<alert-element type="tip" title="Tip">
 
The **WordPress WAF Ruleset** is enabled by default. 
 
</alert-element>

### Allow common automated services 

Follow these steps to allow crawlers, scanners, monitoring bots, and similar tools to access your website:  

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. 

3\. In the sidebar, click **WAAP**. 

4\. On the **Policies** page, click the **Common automated services** to expand the section and enable the desired bot.

<img src="https://assets.gcore.pro/docs/waap/getting-started/common-automated-services.png" alt="WAAP policies page with the highlighted common automated bots policy">

There are a few trusted bots in this section that are allowed by default, which is why we recommend reviewing this list before enabling the protect mode.

## Step 6: Enable protect mode 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. 

3\. In the sidebar, click **WAAP**. 

4\. In the upper-right corner of the screen next to WAF mode, select **Protect**. The WAF will begin to inspect and act upon incoming requests.

<img src="https://assets.gcore.pro/docs/waap/getting-started/protect-mode.png" alt="Domains page in the Customer Portal">