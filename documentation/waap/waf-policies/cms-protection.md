---
title: cms-protection
displayName: CMS protection
published: true
order: 60
toc:
   --1--Allow admin access to a domain: "allow-adminaaccess-to-your-domain"
   --1--Configure policy rules: "configure-policy-rules"
   --2--Allowlist a static IP address: "allowlist-a-static-ip-address"
pageTitle: Set up CMS protection WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize CMS protection policy.
---
# CMS protection

Content Management Systems (CMS) typically send information to your website, and this activity can appear malicious through its automated nature.  

Gcore’s Web Application Firewall (WAF) can distinguish between traffic coming from your CMS administrators and potentially harmful requests. This ensures that administrative activities remain unblocked and your application stays protected.  

The CMS protection policy contains specific rules that detect when a user is logged in to a supported CMS, and it automatically adds the user's session to allowlist. We also keep a library of known malicious attacks, which allows us to block exploits that have attacked users in the past. 

## Allow admin access to your domain 

In some cases, administrative sections of a CMS-based website may be blocked. For example, for WordPress, the WAF may label a change made to the `/wp-admin` section of a CMS-based site as malicious behavior like Cross-Site Scripting or SQL injection.  

As a result, the WAF will block admins from making any page edits. You can prevent this issue in two ways: [enable the needed rules](https://gcore.com/docs/waap/waf-policies/cms-protection#configure-policy-rules) in the CMS protection policy or [allowlist your static IP address](https://gcore.com/docs/waap/waf-policies/cms-protection#allowlist-a-static-ip-address). 

## Configure policy rules 

You can review the policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/anti-automation-bot-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **CMS protection** to expand the section and adjust the policy rules. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/cms-protection/cms-protection.png" alt="WAF policies page with the highlighted CMS protection policy">

<alert-element type="info" title="Info">

Most of the CMS protection rules allow traffic. Only the WordPress WAF ruleset rule will block the traffic to your website. 

</alert-element>

If you don’t see your CMS, you can allow admin access by adding your IP address to the allowlist. Contact our [Support team](mailto:support@gcore.com) for assistance.

<table>
<thead>
<tr>
<td style="text-align: left">Rule</td>
<td style="text-align: left">Description</td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">WordPress WAF ruleset</td>
<td style="text-align: left">Block requests that are potentially a WordPress exploit.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in WordPress admins</td>
<td style="text-align: left">Allow requests from logged-in WordPress admins.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in MODX admins</td>
<td style="text-align: left">Allow requests from logged-in MODX admins.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in Drupal admins</td>
<td style="text-align: left">Allow requests from logged-in Drupal admins.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in Joomla admins</td>
<td style="text-align: left">Allow requests from logged-in Joomla admins.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in allowlist Magento admins</td>
<td style="text-align: left">Allow requests from logged-in Magento admins.</td>
</tr>
<tr>
<td style="text-align: left">Requests from origin's IP</td>
<td style="text-align: left">Allow requests from the origin's IP address for updates. </td>
</tr>
<tr>
<td style="text-align: left">Logged-in Umbraco admins</td>
<td style="text-align: left">Allow requests from logged-in Umbraco admins.</td>
</tr>
<tr>
<td style="text-align: left">Logged-in PimCore admins</td>
<td style="text-align: left">Allow requests from logged-in PimCore admins.</td>
</tr>
</tbody>
</table>

If you enable a particular rule for your CMS, the admin CMS session will be allowlisted when that admin user logs in to the site. 

<alert-element type="info" title="Tip">

We recommend disabling rules for Content Management Systems that you don’t use. 

</alert-element>

### Allowlist a static IP address 

If you don’t see your CMS in the list of rules under the CMS policy, you can allow admin access to your site as follows: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/anti-automation-bot-protection/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it.  

3\. In the left-side navigation menu, click **Firewall**. 

4\. In the Allowed IPs section, click **Add IP/IP Range**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/cms-protection/firewall-page.png" alt="Firewall page with the allow and block IP lists">

5\. Enter your public IP address so that all traffic from your IP will be allowed and won’t be blocked by the WAF for any type of request. 

6\. (Optional). Add a description. 

7\. Click **Save** to apply the changes.