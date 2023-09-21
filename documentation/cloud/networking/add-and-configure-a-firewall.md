---
title: add-and-configure-a-firewall
displayName: Firewall
published: true
order: 60
toc:
   --1--Create a firewall: "create-a-firewall"
   --1--Use the default firewall: "use-the-default-firewall"
   --2--Add, change and delete rules: "add-change-and-delete-rules"
   --2--Assign to an instance and detach from it: "assign-to-an-instance-and-detach-from-it"
   --2--Delete: "delete-a-firewall"
pageTitle: Add a firewall | Gcore
pageDescription: Learn how to add and configure a firewall to protect your servers from network threats.
---
# Add and configure a firewall

A firewall is a network security device used to protect servers from network threats. The firewall monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules. You can set rules for all connections except port 25 for outbound traffic as it is blocked by default.

If you use a load balancer and your instance is in a pool, configure its firewall by opening ports for receiving and transmitting data to the load balancer. For more information, refer to our guide <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">"Create and configure a load balancer"</a>.

## Create a firewall

If you don’t create your custom firewall, the default firewall will be used.

1\. Open a window to create a firewall. You can do in two ways:

*   In the Cloud menu, go to **Networking** → **Firewalls** → **Create firewall**.  

 <img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257548714001.png" alt="Firewalls " width="580" height="271">  
    
*   When you’re creating a virtual machine, find the **Firewall settings** section, select **Add a Firewall**. 

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

5\. (optional) Apply a firewall to an instance by selecting it in the **Apply to Instance** drop-down list.

6\. (optional) Add tags by switching on the **Add tags** toggle in the **Additional options** section and specifying headers and tags. 

7\. Click **Create firewall**.

## Use the default firewall

If you don't specify which firewall to apply to your instance, the default firewall will be applied.

The default firewall allows the following traffic:

*   Incoming connections over protocols: SSH (port 22), UDP (port 3389), ICMP (all ports), TCP (port 3389).
*   All outgoing connections.

## Manage a firewall

### Add, change and delete rules

1\. Go to the **Networking** tab → **Firewalls.**

2\. Find the required firewall, click the ⋯ menu on the right and select **Rules**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13257832035729.png" alt="Firewalls">

### Assign to an instance and detach from it

1\. Go to the **Networking** tab → **Firewalls.**

2\. Find the required firewall, click the ⋯ menu on the right and select **Instances**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13258087088401.png" alt="Firewalls">

### Delete a firewall

1\. Go to the **Networking** tab → **Firewalls.**

2\. Find the required firewall, click the ⋯ menu on the right and select **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/networking/add-and-configure-a-firewall/13258132640145.png" alt="Delete a firewall">
