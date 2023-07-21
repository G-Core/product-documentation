---
title: create-and-configure-a-floating-ip-address
displayName: Floating IP address
published: true
order: 10
toc:
   --1--What is a floating IP: "what-is-a-floating-ip"
   --1--What is it used for: "what-is-it-used-for"
   --1--How it works: "how-does-it-work"
   --1--Check if your subnet is routable: "check-if-your-subnet-is-routable"
   --1--Reserve: "reserve-a-floating-ip-from-the-menu"
   --1--Assign: "assign-a-floating-IP-to-an-instance"
   --1--Detach: "detach-a-floating-IP-from-an-instance"
   --1--Delete: "delete-a-floating-IP"
pageTitle: Floating IP address| Gcore
pageDescription: Configure a floating IP address for your instance to enable external network access. Learn how to reserve, assign, detach, and delete a floating IP.
---
# Create and configure a floating IP address

## What is a floating IP address?

A Floating IP is a type of public, static IP address that can be assigned to instances within a private subnet. This means that the instances do not have a public network interface. By using a Floating IP, these instances are able to receive incoming connections from the Internet

**Please note**: The private subnet of the instance must be <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#network-routing" target="_blank">routable</a> . Routing can be enabled in the subnet settings.

## What is it used for?

A floating IP allows you to quickly provide access from an external network to an instance that does not have a public network interface. By assigning an address to the instance; you will be able to connect to it.

Another method for providing access is by creating a public interface for the device. However, this can cause conflicts with the private routed interface as both are used for accessing the internet. You would have to configure the routing manually. A Floating IP is a convenient solution if you only need temporary access to an external network or prefer not to deal with routing configuration.

## How does it work?

When you reserve a floating IP and assign it to your instance, the router directs incoming traffic to your device by forwarding packets intended for that IP. Outgoing traffic from your device will then be sent using the floating IP as the source.

## Check if your subnet is routable

1\. Open the **Networking** section, select the required network, and navigate to your equipment's subnet settings. 

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12391415662737.png" alt="floating-ip-01.png">

2\. Click the three dots menu, then select **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12391621674513.png" alt="floating-ip-02.png">

3\. Ensure the **Enable router gateway** slider is enabled, making the subnet routable, and allowing servers within the subnet to access the Internet and receive incoming connections.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12391738930705.png" alt="floating-ip-03.png" width=80%>

## Reserve a floating IP from the menu

A floating IP is assigned by a specific data center, and its address is linked to that location. It can only be assigned to an instance within the exact location.

1\. Select the Region where your machine is located to assign a floating IP and navigate to the **Networking** section.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12391851006353.png" alt="floating-ip-04.png" width=50%>

2\. Open the Floating IPs section. You can create a floating IP without assigning it to a machine by clicking **Create a new Floating IP.**

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392006241425.png" alt="floating-ip-05.png">

3\. Additionally, you can create a floating IP and immediately assign it to a specific instance. To do this, enable the "Assign to existed instance" slider, select the machine and interface, and click **Create a new floating IP.**

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392182782993.png" alt="floating-ip-06.png">

## Reserve a floating IP when creating an instance


When creating an instance, in the "Network settings" section, select the "**Private**" network type. Specify the network and subnet of the interface you want to assign the floating IP. Enable the "**Use floating IP**" slider, click "**Create a new floating IP**", and save the settings using the "**Add Interface**" button.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392462274833.png" alt="floating-ip-07.png" width=80%>

The instance will be created with a private interface and a new floating IP assigned to it.

## Assign a floating IP to an instance

Next to the free IP, click "Assign to instance" or select this option from the selector on the right.  
  
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392603351313.png" alt="floating-ip-08.png">

Select the instance in the pop-up window, and the floating IP's network interface will be assigned. Click **Assign floating IP**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392628635793.png" alt="floating-ip-09.png">

## Detach a floating IP from an instance

You can detach a floating IP address in the "Floating IPs" section or in the instance menu. In the "Floating IP" section, click the selector next to the address and select **Detach from Instance**, and the IP will no longer be assigned to the machine.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392631295505.png" alt="floating-ip-10.png">  

In the instance menu, open the "Networking" tab and select the private interface. Open the selector and click "**Detach Floating IP**". The IP will no longer be assigned to this machine.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392664056465.png" alt="floating-ip-11.png">

## Delete a floating IP

In the "Floating IPs" section, click the selector next to the desired address and select **Delete**. The IP will be removed, and you don't have to pay anymore.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address/12392700821393.png" alt="floating-ip-12.png">
