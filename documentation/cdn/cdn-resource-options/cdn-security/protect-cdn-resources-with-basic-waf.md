---
title: protect-cdn-resources-with-basic-waf
displayName: Gcore WAAP (Beta)
published: true
order: 10
pageTitle: Protection from cyberthreads with Gcore WAAP | Gcore
pageDescription: A comprehensive guide on how to protect the entire CDN resource or specific urls.
---
# Protect CDN resources with Gcore WAAP

<a href="https://gcore.com/docs/waap/about-waap" target="_blank">Gcore Web Application and API Protection</a> (WAAP) combines all aspects of website security and traffic management, including Layer 7 DDoS protection, web app security, and API protection. 

With built-in security rules, advanced behavioral analytics, and a range of available customization options, Gcore WAAP protects your domains against known vulnerabilities and common exploits. 

## Enable WAAP for a resource

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN** > **CDN resources**.

2\. Next to the resource that you want to protect with WAAP, click the three-dot icon and select **Settings**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/cdn-resources-page.png" alt="CDN resource settings page in the Customer Portal">

3\. Scroll down the page and find the **Security** section. 

4\. Enable the **WAAP** toggle to activate Web Application and API Protection for your CDN resource.

<img src="https://assets.gcore.pro/docs/waap/getting-started/security-section-waap-enabled.png" alt="WAAP toggle">

5\. Click **Save** to apply the changes.  

<alert-element type="warning" title="Warning">

After enabling WAAP in CDN, you need to invalidate the cache. This is necessary to ensure that WAAP settings are properly applied. 
When "Secure Token" and/or "Referrer access policy" CDN options are enabled in conjunction with WAAP, the CDN may block WAAP requests.

These limitations will be removed soon.

</alert-element>

Consider that it might take up to 20 minutes for the HTTP traffic to start passing through our WAAP after the activation. 

### What to do if WAAP blocks content that shouldn’t be blocked? 

Instead of disabling WAAP protection for the whole resource, you can create a rule with an exception: 

1\. In the CDN resource settings, open the **Rules** tab. 

2\. Click **Create rule** > **Create blank rule**. 

3\. Give your rule a name. 

4\. In the **Match criteria** section, specify the URLs or a regular expression of files blocked by WAAP. 

5\. Set the origin pull protocol to **Inherit from resource**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/rule-name-match-options.png" alt="WAAP toggle" width="80%">

6\. In the **Options** section, click **Add option**. 

7\. Find WAAP and then turn it off for the selected URL rule pattern. 

8\. Click **Create rule**. 

Your content should no longer be blocked by WAAP. 
