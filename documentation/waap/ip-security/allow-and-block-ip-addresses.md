---
title: allow-and-block-ip-addresses
displayName: Allow and block IP addresses
published: true
order: 10
pageTitle: Create firewall rules to allow or block IP addresses that can access your domain | Gcore
pageDescription: Learn how to add IP addresses to block and allow lists.
---
# Allow and block IP addresses

The IP Address Firewall is your first line of protection to block or allow specific IP addresses or IP ranges.  

You can also create more robust <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rules</a> to sanction IP addresses. If you want to add a rule for verified bots and crawlers, check our common automated services <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policy</a> to see if the similar policy already exists. 

## Add IPs to allowlist or blocklist 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/ip-security/domains-list.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. 

3\. Open the **Firewall** page.

<img src="https://assets.gcore.pro/docs/waap/ip-security/firewall-page.png" alt="Firewall page in the Customer Portal">

4\. Navigate to the needed section—**Allow IPs** or **Block IPs**—and click **Add IP/IP Range**. 

5\. Enter the IP information and provide a description. To add an IP address range, enter the first address and then the last address in the next field. 

<alert-element type="info" title="Info">
 
You can’t add a subnetwork to the IP or IP range. 
 
</alert-element>

6\. Click **Save** to add IP to the list.

Depending on the applied action, the traffic from this IP address will be either allowed or blocked on your domain. 

This rule will appear both on the **Firewall** and **WAAP Rules** pages (in the **Custom rules** section). On the **WAAP Rules** page, the rule will be displayed as an if/then condition.

## Manage blocked and allowed IPs 

<alert-element type="tip" title="Tip">
 
You can add and manage all block and allow IP rules on the **Firewall** page. Additionally, these rules are displayed on the **WAAP Rules** page, where you can temporarily disable or enable them if necessary. 
 
</alert-element>

If the IP address of a trusted client has changed or you’ve detected new threats within the IP range, you can update the IP address or range accordingly.  

Sometimes an IP address may be incorrectly flagged as a threat or become a security risk. In such cases, you can remove the address from the list and apply the necessary security actions. 

To update or remove an IP or IP range:

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/ip-security/domains-list.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it. 

3\. Open the **Firewall** page.

4\. Navigate to the needed section—**Allow IPs** or **Block IPs**. 

5\. Find the IP you want to manage and click the three-dot icon next to it. 

6\. Select the relevant action from the dropdown—**Edit** or **Delete**—and follow the instructions.

<img src="https://assets.gcore.pro/docs/waap/ip-security/edit-delete-ip.png" alt="Domains page in the Customer Portal">