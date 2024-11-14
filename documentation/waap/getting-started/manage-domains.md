---
title: manage-domains-protected-with-waap
displayName: Manage domains protected with WAAP
published: true
order: 30
toc:
   --1--Disable WAAP protection: "disable-waap-protection-for-a-domain"
   --1--Delete a domain from WAAP: "delete-a-domain-from-waap"
   --1--Suspend a CDN resource: "suspend-a-cdn-resource-with-waap-protection"
   --1--Delete a CDN resource: "delete-a-cdn-resource-with-waap-protection"
pageTitle: A guide on how to manage domains in Gcore WAAP and CDN | Gcore
pageDescription: Learn how to manage, delete, and deactivate domains in Gcore WAAP and CDN settings.
---
# Manage domains protected with WAAP

After you <a href="https://gcore.com/docs/waap/getting-started/configure-waap-for-a-domain#step-2-enable-waap-in-cdn-resource-settings" target="_blank">activate WAAP for your domain in CDN</a>, it will appear on the **Domains** page in the Gcore Customer Portal. Here, you can view all domains and their statuses, navigate to the CDN settings, and delete inactive domains. 

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-waap-page.png" alt="Domains page in the Customer Portal">

A domain in WAAP can have the following statuses:  

* **Monitor mode**: WAAP monitors all traffic to the domain but doesn't enforce any actions on requests. 

* **Protect mode**: WAAP enforces all configured security settings for the domain. 

* **Inactive**: The domain isn’t protected because WAAP is disabled. You can always <a href="https://gcore.com/docs/waap/getting-started/configure-waap-for-a-domain#step-2-enable-waap-in-cdn-resource-settings" target="_blank">enable WAAP</a> for inactive domains in the CDN resource settings. Note that inactive domains are still billable.  

## Disable WAAP protection for a domain

<alert-element type="info" title="Info">
 
Inactive domains still incur charges as we retain all configured settings and data. If you want to discontinue billing for WAAP protection, delete a domain. 
 
</alert-element>

To disable WAAP protection for a domain:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN** > **CDN resources**. 

2\. Next to the resource that you want to protect with WAAP, click the three-dot icon and select **Settings**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/cdn-resources-page.png" alt="CDN resource settings page in the Customer Portal">

3\. Navigate to the relevant section: 

* If you enabled WAAP in the resource settings, scroll down the page to the **Security** section and disable the **WAAP** toggle. 

* If you enabled WAAP for a particular rule, open the **Rules** tab, find the relevant rule, and disable the **WAAP** toggle in the **Options** section. 

4\. Save the changes. Note that deactivating a domain can take up to 20 minutes as this step ensures that all changes are correctly and consistently applied across our system.

After you deactivate WAAP protection for your domain, all traffic from the CDN will go directly to the origin with no security checks. The domain status on the Domains page in WAAP will change to **inactive**. All WAAP settings and configured rules will remain intact and can be modified. However, it’ll take no effect while WAAP is disabled.  

To activate WAAP protection again, <a href="https://gcore.com/docs/waap/getting-started/configure-waap-for-a-domain#step-2-enable-waap-in-cdn-resource-settings" target="_blank">enable the WAAP toggle</a> in the CDN settings. 

<alert-element type="warning" title="Warning">
 
If you disable WAAP protection for a CDN resource and later re-enable it, WAAP mode will be set to **monitor**. If you had the protect mode before deactivating a domain, you need to enable it again. 
 
</alert-element>

## Delete a domain from WAAP 

You can’t delete a domain that has enabled WAAP protection. To delete the domain, disable WAAP in CDN resource settings first. The domain status in WAAP should change to inactive. 

To delete an inactive domain: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Click the three-dot icon next to the domain that you want to remove. 

3\. Select **Delete**. 

4\. Confirm your action by clicking **Yes, delete**. 

You’ve successfully removed your domain from WAAP. 

## Suspend a CDN resource with WAAP protection 

If you suspend a CDN resource with enabled WAAP, the status of your WAAP-protected domain will change to **inactive**. All web requests will go directly to the origin, bypassing both CDN and WAAP. 

<alert-element type="info" title="Info">
 
Inactive domains still incur charges as we retain all configured settings and data. If you want to discontinue billing for WAAP protection, delete a domain. 
 
</alert-element>

A <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/suspend-a-cdn-resource-automatically-or-manually" target="_blank">suspended resource</a> will be automatically deleted in 90 days. During this period, we’ll keep your WAAP settings intact, and you’ll be able to activate CDN and WAAP again. 

## Delete a CDN resource with WAAP protection 

If you delete a CDN resource that has enabled WAAP protection, your domain and all relevant settings will automatically removed from WAAP. 

For instructions on how to delete a CDN resource, check our <a href="https://gcore.com/docs/cdn/about-cdn-resources-interface-how-it-is-arranged#delete-a-resource" target="_blank">dedicated guide</a>. 
