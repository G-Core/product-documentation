---
title: cms-protection
displayName: CMS protection
published: true
order:
pageTitle: Set up CMS protection WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize CMS protection policy.
---
# CMS protection

Content Management Systems (CMS) typically send information to your website, and this activity can appear malicious through its automated nature.  

Gcore’s Web Application Firewall (WAF) can distinguish between traffic coming from your CMS administrators and potentially harmful requests. This ensures that administrative activities remain unblocked and your application stays protected.  

The CMS protection policy contains specific rules that detect when a user is logged in to a supported CMS, and it automatically adds the user's session to allowlist. We also keep a library of known malicious attacks, which allows us to block exploits that have attacked users in the past. 

## Allow admin access to your domain 

In some cases, administrative sections of a CMS-based website may be blocked. For example, for WordPress, the WAF may label a change made to the `/wp-admin` section of a CMS-based site as malicious behavior like Cross-Site Scripting or SQL injection.  

❗️ As a result, the WAF will block admins from making any page edits. You can prevent this issue in two ways: enable the needed rules in the CMS protection policy or allowlist your static IP address. 

## Configure policy rules 

You can review the policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **CMS protection** to expand the section and adjust the policy rules. 

<alert-element type="info" title="Info">

Most of the CMS protection rules allow traffic. Only the WordPress WAF ruleset rule will block the traffic to your website. 

</alert-element>

❗️If you don’t see your CMS, you can allow admin access by adding your IP address to the allowlist. Contact our [Support team](mailto:support@gcore.com) for assistance.

