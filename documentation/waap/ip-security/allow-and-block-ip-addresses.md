---
title: allow-and-block-ip-addresses
displayName: Allow and block IP addresses in firewall
published: true
order: 10
toc:
   --1--Add IPs to allowlist or blocklist: "add-ips-to-allowlist-or-blocklist"
   --1--Manage blocked and allowed IPs: "manage-blocked-and-allowed-ips"
pageTitle: Create firewall rules to allow or block IP addresses that can access your domain | Gcore
pageDescription: Learn how to add IP addresses to block and allow lists.
---
# Allow and block IP addresses in firewall

Our firewall is your first line of protection to block or allow specific IP addresses or IP ranges from reaching your domain. Firewall rules contain a single condition—either "block" or "allow" an IP. They are quick to implement and easy to adjust as compared to the custom or advanced WAAP rules.

All rules for allowing or blocking IPs are also displayed on the  **WAAP Rules** page. There, you can also create more robust <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rules</a> to sanction IP addresses. 

<alert-element type="tip" title="Tip">

If you want to add a rule for verified bots and crawlers, check our <a href="https://gcore.com/docs/waap/waap-policies/common-automation-services" target="_blank">common automated services</a> policy group to see if a similar policy already exists. 

Enabling predefined policies gives you immediate protection without further testing and manual adjustments. They are created and optimized to accurately distinguish between legitimate and harmful automated traffic, which reduces the risk of false positives or negatives.

</alert-element>

## Add IPs to allowlist or blocklist 

You can allow and block traffic for both IPv4 and IPv6 addresses. For each address type, you need to create a separate firewall rule:

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/ip-security/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **Firewall**.

<img src="https://assets.gcore.pro/docs/waap/ip-security/policies-page-firewall-tab.png" alt="Policies page in the Customer Portal">

4\. Navigate to the needed section:

* **Allow IPs**: Permit specific IPs or IP ranges to access your domain without any restrictions or security checks.

* **Block IPs**: Deny IPs or IP ranges access to your domain.

<img src="https://assets.gcore.pro/docs/waap/ip-security/firewall-page.png" alt="Firewall page in the Customer Portal">

5\. Click **Add IP/IP Range**. To allow or block traffic for an IP range, enter its first and last IP address. 

You can specify up to 30 networks in a single range. Subnet masks are not supported. 

6\. Enter the IP information and provide a description. To add an IP address range, enter the first address and then the last address in the next field. 

<alert-element type="info" title="Info">
 
You can’t add a subnetwork to the IP or IP range. 
 
</alert-element>

7\. Click **Save** to add the IP to the list.

Depending on the applied action, the traffic from this IP address will be either allowed or blocked on your domain. 

This rule will appear both on the **Firewall** and **WAAP Rules** pages (in the **Custom rules** section). On the **WAAP Rules** page, the rule will be displayed as an If/Then condition.

## Manage blocked and allowed IPs 

You can view, create, and customize rules for blocking IP addresses and ranges on the **Firewall** page. If you have a large number of rules, you can search by rule description to find the one you need. 

Additionally, all blocked and allowed IPs are displayed on the **WAAP Rules** page, where you can temporarily disable or enable them if necessary. 

<alert-element type="warning" title="Warning">

If you disable a firewall rule on the **WAAP Rules** page, it will no longer be visible on the **Firewall** page. Once re-enabled, the rule will appear on the **Firewall** page automatically.

</alert-element>


### Update an IP or IP range 

If the IP address of a trusted client has changed or you’ve detected new threats within the IP range, you can update the IP address or range accordingly.  

Sometimes an IP address may be incorrectly flagged as a threat or become a security risk. In such cases, you can remove the address from the list and apply the necessary security actions. 

To update or remove an IP or IP range:

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/ip-security/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page.

3\. In the sidebar, click **Firewall**.

<img src="https://assets.gcore.pro/docs/waap/ip-security/policies-page-firewall-tab.png" alt="Policies page in the Customer Portal">

4\. Navigate to the needed section with the configured IP address—**Allow IPs** or **Block IPs**. 

5\. Find the IP you want to manage and click the three-dot icon next to it. 

6\. Select the relevant action from the dropdown—**Edit** or **Delete**—and follow the instructions.

<img src="https://assets.gcore.pro/docs/waap/ip-security/edit-delete-ip.png" alt="Domains page in the Customer Portal">

## Delete multiple rules with group actions

You can simultaneously delete multiple rules that allow or block particular IPs or IP ranges. To do so, select checkboxes next to the firewall rules you want to delete and then choose the **Delete** action from the **Actions** dropdown.

<img src="https://assets.gcore.pro/docs/waap/ip-security/actions-dropdown.png" alt="Actions dropdown on the Firewall page">