---
title: create-and-manage-a-subnetwork
displayName: Subnetwork
published: true
order: 20
toc:
   --1--Subnetwork creation: "subnetwork-creation"
   --1--Network routing: "network-routing"
   --1--Setting the IP range: "setting-the-ip-range"
   --1--Subnetwork management: "managing-subnets"
pageTitle: Add a subnetwork | Gcore
pageDescription: Learn how to create and manage a subnetwork in the cloud to transfer information between cloud resources and establish an Internet connection.
---
# Create and manage a subnetwork

A subnetwork is a range of IP addresses in a cloud network. Addresses from this range will be assigned to machines in the cloud.  

## Subnetwork creation

There are two ways to create a subnet in the network: 

1. Inside the project, in the section Networking → Networks → Click on the name of the network where you want to create a subnet → Create a subnet.

<media-gallery>
 <img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830562453009.png" alt="Networks ">

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830595601169.png" alt="network">
</media-gallery>

2. While creating an instance, in the Network settings section, select the Private interface type, select or create a network, and click Add a new subnetwork.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830600498321.png" alt="Network settings section">

## Setting the IP range

While creating a subnet (with any method), you need to specify the address range in the CIDR format in the drop-down window.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830635124369.png" alt="creating a subne">

The subnet size is set using the classless addressing (CIDR) method. Only private IPv4 addresses can be used in subnets. 

Acceptable CIDR ranges: 
*   10.0.0.0 - 10.255.255.255 
*   172.16.0.0 - 172.31.255.255 
*   192.168.0.0 - 192.168.255.255 
Valid subnet mask range: 16-24. 

## Network routing

A routed network is a private network that is already connected to a router with a public interface. All virtual servers in such networks can access the Internet through the router and accept incoming connections. 

By default, a subnet in the cloud is created with Internet access (**routable**). 

If you need to restrict machines from external connections, you need to enable the non-routable Subnetwork option while creating a subnet. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830607341457.png" alt="Network routing">

## Managing subnets

You can see the list of subnets in the created **network** in the section Networking → Networks. 

**Editing a name** 
    
To rename a subnet, click the selector on the right from the selected subnet and select **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830661431953.png" alt="Editing a name ">

In the drop-down window, you can change the name of the created subnet.

**Deleting a subnet**
    
To delete a subnet, click the selector on the right from the selected subnet and click **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/13830702718097.png" alt="Deleting a subnet">
