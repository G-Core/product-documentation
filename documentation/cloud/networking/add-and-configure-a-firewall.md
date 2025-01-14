---
title: add-and-configure-a-firewall
displayName: Firewall
published: true
order: 60
toc:
   --1--Create a firewall: "create-a-firewall"
   --1--Use the default firewall: "use-the-default-firewall"
   --2--Add, change and delete rules: "add-change-and-delete-rules"
   --2--Assign to a Virtual Machine and detach from it: "assign-to-a-virtual-machine-and-detach-from-it"
   --2--Delete: "delete-a-firewall"
pageTitle: Add a firewall | Gcore
pageDescription: Learn how to add and configure a firewall to protect your servers from network threats.
---
# Add and configure a firewall

A firewall is a network security device used to protect servers from network threats. The firewall monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. You can set rules for all connections except port 25 for outbound traffic as it is blocked by default.

If you use a Load Balancer and your Virtual Machine is in a pool, configure its firewall by opening ports for receiving and transmitting data to the Load Balancer. For more information, refer to our guide <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">"Create and configure a Load Balancer"</a>.

## Create a firewall

If you don’t create your custom firewall, the default firewall will be used.

1\. Open a window to create a firewall. You can do in two ways:

*   In the Cloud menu, go to **Networking** > **Firewalls** > **Create firewall**.  

 <img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257548714001.png" alt="Firewalls " width="580" height="271">  
    
*   When you’re creating a Virtual Machine, find the **Firewall settings** section, select **Add a Firewall**. 

2\. Give your firewall a name. 

3\. Set **Inbound rules** which would define the allowed incoming traffic.  
Click **New rule** and select one of the template rules or choose **Custom** to apply custom settings.

*   Template rules (All TCP/all UDP/SSH/HTTP/HTTPS/MySQL/DNS UPD/DNS TCP/postgreSQL): template rules come with pre-configured protocols and ports for typical connections 
*   Custom rule: if you select a custom rule, specify the protocol and port manually. 

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257703188369.png" alt="Inbound rule" width="569" height="166">

For **Sources**, set a specific IP address range in the CIDR format. Otherwise, the rule will be applied to all IP addresses. 

4\. Set the **Outbound rules** which would define the allowed outgoing traffic.

Please note that by default, outbound traffic over port 25 (TCP/UDP) is restricted, while all other outbound ports are open.

Click **New rule** and select one of the template rules or choose **Custom** to apply custom settings.

*   Template rules (All TCP/all UDP/SSH/HTTP/HTTPS/MySQL/DNS UPD/DNS TCP/postgreSQL): template rules come with pre-configured protocols and ports for typical connections 
*   Custom rule: If you select a custom rule, specify the protocol and port manually.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257703188369.png" alt="Custom rule" width="569" height="166">

For **Sources**, set a specific IP address range in the CIDR format. Otherwise, the rule will be applied to all IP addresses. 

5\. (optional) Apply a firewall to a Virtual Machine by selecting it in the **Apply to Instance** drop-down list.

6\. (optional) Add tags by switching on the **Add tags** toggle in the **Additional options** section and specifying headers and tags. 

7\. Click **Create firewall**.

## Use the default firewall

If you don't specify which firewall to apply to your Virtual Machine, the default firewall will be applied.

The default firewall contains inbound rules, which allow the following traffic for IPv6 as for IPv4 addresses: 

* SSH connections over TCP protocol on port 22 

* Remote Desktop Protocol (RDP) connections over TCP and UDP protocols on port 3389.   

* Internet Control Message Protocol (ICMP) is allowed. 

All outgoing connections are allowed.  

## Manage a firewall

### Add, change and delete rules

1\. Go to the **Networking** tab > **Firewalls**.

2\. Find the required firewall, click the ⋯ menu on the right and select **Rules**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257832035729.png" alt="Firewalls">

### Assign to a Virtual Machine and detach from it

1\. Go to the **Networking** tab > **Firewalls**.

2\. Find the required firewall, click the ⋯ menu on the right and select **Instances**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13258087088401.png" alt="Firewalls">

### Delete a firewall

<alert-element type="warning" title="Warning">
 
You can’t delete a default firewall. 
 
</alert-element>

1\. Go to the **Networking** tab > **Firewalls**.

2\. Find the required firewall, click the ⋯ menu on the right and select **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13258132640145.png" alt="Delete a firewall">


## Firewall feature not supported for Bare Metal servers

Please note that the Firewall feature is not supported for Bare Metal servers. Unlike Virtual Machines or other cloud services that can easily integrate with cloud-native firewalls, Bare Metal servers operate directly on physical hardware and are not subject to the same level of firewall management.

For network security, Bare Metal servers can use the following alternatives:
*   You can manually configure network security using solutions like **iptables** or **nftables** (recommended) to protect your server at the network level. Other similar solutions can also be used to set up necessary firewall rules based on your security needs.

```
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -P INPUT DROP
```

*   For an additional layer of protection, opt for [Gcore DDoS Protection]([url](https://gcore.com/ddos-protection)) to keep your server available during attacks. DDoS Protection redirects traffic to the Threat Mitigation System (TMS), which performs filtering and threat detection, preventing service disruptions with its always-on mode.

For more information, please [reach out to our support team]([url](https://gcore.com/contact-us)) for tailored DDoS Protection plans.
