---
title: create-and-manage-a-subnetwork
displayName: Subnetwork
published: true
order: 20
toc:
   --1--Subnetwork creation: "subnetwork-creation"
   --1--Subnetwork management: "managing-subnets"
---
# Create and manage a subnetwork

**A subnetwork** is a range of IP addresses in a cloud network. Addresses from this range will be assigned to machines in the cloud.  

## ubnetwork creation

There are two ways to create a subnet in the network: 

1\. Inside the project, in the section Networking → Networks → Click on the name of the network where you want to create a subnet → Create a subnet.

<media-gallery>
 <img src="https://support.gcore.com/hc/article_attachments/13830562453009" alt="_________________________________.png">

<img src="https://support.gcore.com/hc/article_attachments/13830595601169" alt="_______________.png">
<media-gallery>

2\. While creating an instance, in the Network settings section, select the Private interface type, select or create a network, and click Add a new subnetwork.

<img src="https://support.gcore.com/hc/article_attachments/13830600498321" alt="_____________________.png">

While creating a subnet (with any method), you need to specify the address range in the CIDR format in the drop-down window.

<img src="https://support.gcore.com/hc/article_attachments/13830635124369" alt="_________________.png">

The subnet size is set using the classless addressing (CIDR) method. Only private IPv4 addresses can be used in subnets. 

Acceptable CIDR ranges: 
*   10.0.0.0 - 10.255.255.255 
*   172.16.0.0 - 172.31.255.255 
*   192.168.0.0 - 192.168.255.255 
Valid subnet mask range: 16-24. 

A routed network is a private network that is already connected to a router with a public interface. All virtual servers in such networks can access the Internet through the router and accept incoming connections. 

By default, a subnet in the cloud is created with Internet access (**routable**). 

If you need to restrict machines from external connections, you need to enable the non-routable Subnetwork option while creating a subnet. 

<img src="https://support.gcore.com/hc/article_attachments/13830607341457" alt="__________________________.png">

## Managing subnets

You can see the list of subnets in the created **network** in the section Networking → Networks. 

**Editing a name** 
    
To rename a subnet, click the selector on the right from the selected subnet and select **Edit**.

<img src="https://support.gcore.com/hc/article_attachments/13830661431953" alt="____________.png">

In the drop-down window, you can change the name of the created subnet.

 **Deleting a subnet** 
    

To delete a subnet, click the selector on the right from the selected subnet and click **Delete**.

<img src="https://support.gcore.com/hc/article_attachments/13830702718097" alt="________________.png">