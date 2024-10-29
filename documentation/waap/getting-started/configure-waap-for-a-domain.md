---
title: configure-waap-for-a-domain
displayName: Configure WAAP for a domain
published: true
order: 10
toc:
   --1--Step 1. Create a CDN resource: "step-1-create-a-cdn-resource"
   --1--Step 2. Enable WAAP in resource settings: "step-2-enable-waap-in-cdn-resource-settings"
   --1--Step 3. Use WAAP in monitor mode: "step-3-use-waap-in-monitor-mode"
   --1--Step 4. View your domain’s traffic: "step-4-view-your-domain-traffic"
   --1--Step 5. Test your WAAP configuration: "step-5-test-your-waap-configuration"
   --1--Step 6. Allow admins, bots, and CMS: "step-6-allow-admins-bots-and-cms"  
   --1--Step 7. Configure your APIs: "step-7-configure-your-apis"
   --1--Step 8. Enable protect mode: "step-8-enable-protect-mode"
pageTitle: Set up Gcore WAAP for your domain | Gcore
pageDescription: Learn how to integrate your domain with our WAAP and configure the initial settings.
---
# Configure WAAP for a domain

Web Application and API Protection (WAAP) is a single SaaS tool that combines all aspects of website security and traffic management, including Layer 7 DDoS protection, and web application security.  

<alert-element type="info" title="Info">

WAAP is currently in beta mode. To join the beta, contact the [Gcore support team](mailto:support@gcore.com).
 
</alert-element>

To secure your application with WAAP, you need to create a Gcore CDN resource for your domain, enable WAAP protection in the resource settings, and then verify that everything works as expected and you don’t block legitimate traffic. The following steps will guide you through this process and help you configure WAAP according to your requirements.

<alert-element type="tip" title="Tip">
 
After you enable WAAP, all traffic will be diverted to our network, and it may cause a temporary disruption for your users. We recommend setting up Gcore WAAP during a low-traffic period to minimize the impact. 

</alert-element>

## Step 1. Create a CDN resource  

To secure your web application and APIs with Gcore WAAP, it’s necessary to create a CDN resource associated with your website’s origin.  

If you don’t have Gcore CDN configured, follow the instructions from this guide: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource" target="_blank">Create a CDN resource</a>. To add an SSL certificate, check out the <a href="https://gcore.com/docs/cdn/ssl-certificates/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">Add an SSL certificate to deliver content over HTTPS</a> guide. 

<alert-element type="info" title="Info">
 
Update your domain’s DNS records so they point to our network. This is necessary to allow all traffic to pass through WAAP.

</alert-element>

## Step 2: Enable WAAP in CDN resource settings 

Once your CDN resource is set up, you can activate WAAP protection for it. Refer to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/cdn-security/protect-cdn-resources-with-basic-waf" target="_blank">Protect CDN resources with Gcore WAAP</a> guide for detailed instructions.

## Step 3: Use WAAP in monitor mode 

After you enable WAAP, it will be automatically set to the <a href="https://gcore.com/docs/waap/getting-started/waap-modes#monitor-mode" target="_blank">monitor mode</a>. In this mode, we’ll inspect all incoming requests but won’t take any action. It's best to use monitor mode for several days before enabling the <a href="https://gcore.com/docs/waap/getting-started/waap-modes#protect-mode" target="_blank">protect mode</a> to make sure that all security settings work correctly. 

Completing this step is important because it allows you to analyze requests and test the WAAP behavior before you fully activate it. 

<alert-element type="warning" title="Warning">
 
In monitor mode, all traffic is allowed to your domain, regardless of configured security rules and policy groups. This mode is only recommended for testing WAAP settings.
 
</alert-element>

## Step 4: View your domain traffic 

While keeping WAAP in monitor mode, you can view all logged requests and check the corresponding actions that the WAAP will take once you put it in the protect mode.  

Go through the <a href="https://gcore.com/docs/waap/analytics" target="_blank">analytics pages</a> to detect common traffic patterns and understand if the current configuration requires any adjustments.  

For instance, you can find information about incoming web requests on the **WAAP** analytics page in the **Requests** table: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **Analytics** > **WAAP**. 

4\. Review the information under **Requests**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/waap-requests-table.png" alt="Analytics page in the Customer Portal showing Requests table">

5\. You can also filter requests to get more granular information about your traffic:  

* **Traffic types**: View requests based on the rule that triggered the request. 

* **Policy – Blocked** or **Policy – Allowed**: View requests that triggered our predefined policy groups. 

* Select **Custom Rule – Blocked** or **Custom Rule – Allowed**: View requests that triggered custom rules created by your account users. 

<alert-element type="info" title="Info">
 
**Policy - Blocked** and **Custom Rule - Blocked** are the default filters automatically displayed for the table.  
 
</alert-element>

To view more information about a request, click the request ID and inspect the <a href="https://gcore.com/docs/waap/analytics#request-details" target="_blank">Request Details</a> page.

<img src="https://assets.gcore.pro/docs/waap/getting-started/request-details-overview.png" alt="Request details section open from the Analytics page">

The screenshot above depicts a request that was blocked because of the <a href="https://gcore.com/docs/waap/waap-policies/waf-and-owasp-top-threats#sql_injection" target="_blank">SQL injection</a> policy. It blocks requests if there is evidence that the request contains malicious SQL code.

## Step 5: Test your WAAP configuration 

To achieve the desired WAAP behavior, we recommend that you navigate through your website as both a user and administrator.  

Navigating the website will generate entries in the <a href="https://gcore.com/docs/waap/analytics#requests-table" target="_blank">Requests</a> table. You can use this information to determine if you need to create <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">Firewall rules</a> or <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom WAAP rules</a> for some requests and let them access your website’s content. 

Specifically, review requests that relate to: 

* **Your origin IP**: IP address assigned to your device. 
* **Your office IP**: IP address assigned to your device within your office's network. 
* **Your workstation IP**: IP address assigned to a workstation or specific computer in a network. 

If you notice that WAAP will block such requests in the protect mode, you need to update your settings to prevent such a situation. You can find detailed instructions on how to update your settings in the following step.  

Check out the <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">allow and block IP addresses</a> guide for more information. 

## Step 6: Allow admins, bots, and CMS 

Before the WAAP is in protection mode, you need to ensure that critical IP addresses, content management systems (CMS), and common automated services are allowed to make successful requests.  

Check the <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policy groups</a> for a full list of security policies and their detailed overview. 

### Allow admin IP addresses

If your domain doesn’t use a CMS, we highly recommend allowlisting the site administrator's IP address: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **Firewall**. 

4\. In the **Allowed IPs** section, click **Add IP/IP Range**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/firewall-add-rules.png" alt="Firewall page in the Customer Portal">

5\. Enter any admin user's public IP address. 

6\. Click **Save**. 

Repeat these steps if needed. 

### Allow CMS 

If you use content management systems, such as WordPress, allow traffic for CMS admins:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **WAAP**. 

4\. On the **Policies** page, find CMS protection, and then allow traffic for a desired content management system by enabling a toggle next to it.

<img src="https://assets.gcore.pro/docs/waap/getting-started/cms-protection.png" alt="WAAP policies page with the highlighted CMS protection policy">

<alert-element type="tip" title="Tip">
 
The **WordPress WAF ruleset** policy is enabled by default. 
 
</alert-element>

### Allow common automated services 

Follow these steps to allow crawlers, scanners, monitoring bots, and similar tools to access your website:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. Click the **Common automated services** to expand the section and enable the desired bot.

<img src="https://assets.gcore.pro/docs/waap/getting-started/automated-services.png" alt="WAAP policies page with the highlighted common automated bots policy">

The <a href="https://gcore.com/docs/waap/waap-policies/common-automated-services" target="_blank">common automated services</a> policy group allows a few trusted bots by default, which is why we recommend reviewing this list before enabling the protect mode.

## Step 7: Configure your APIs

If you plan to serve JSON requests through an API on your domain, you can disable the JavaScript injection and CAPTCHA functionalities for specified API endpoints.

You can <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-base-path" target="_blank">manually add endpoints to API base path</a> or <a href="https://gcore.com/docs/waap/api-discovery-and-protection/api-discovery" target="_blank">configure the API Discovery feature</a> to automatically detect and protect your APIs.

## Step 8: Enable protect mode 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **WAAP**. 

4\. In the upper-right corner of the screen next to WAAP mode, select **Protect**. The WAAP will begin to inspect and act upon incoming requests.

<img src="https://assets.gcore.pro/docs/waap/getting-started/protect-mode.png" alt="Domains page in the Customer Portal">
