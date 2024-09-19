---
title: create-and-manage-a-subnetwork
displayName: Subnetwork
published: true
order: 20
toc:
   --1--Create a subnetwork: "create-a-subnetwork"
   --1--Set the IP range: "set-the-ip-range"
   --1--Configure network routing: "configure-network-routing"
   --1--Manage subnetworks: "manage-subnetworks"
pageTitle: Create and manage a subnetwork | Gcore
pageDescription: Learn how to create and manage a subnetwork in the cloud to transfer information between cloud resources and establish an internet connection.
---
# Create and manage a subnetwork

A subnetwork is a range of IP addresses in a cloud network. Addresses from this range will be assigned to Virtual Machines(VMs) in the cloud.  

## Create a subnetwork

There are two ways to create a subnetwork in the network: <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">during the creation of a Gcore Virtual Machine</a> or from the **Networks** page, which is described in the following section.

### Create a subnetwork from the Networks page 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/networks-page.png" alt="Networks page open in the Customer Portal" width=80%>

2\. Find the network where you want to create a subnetwork and click its name to open it. 

3\. Click **Create subnetwork**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/network-settings-create-subnet.png" alt="Network settings section with the highlighted Create a subnetwork button" width=80%>

4\. A new **Create subnetwork** page will open. Here, you can customize subnetwork settings.

5\. Enter the subnetwork name.

6\. Set CIDR between ranges: 10.0.0.0 - 10.255.255.255, 172.16.0.0—172.31.255.255, 192.168.0.0—192.168.255.255. Set the mask between 16 and 24. You can find more information in the [Set the IP range](https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#set-the-ip-range) section.

7\. (optional) Turn on the **Enable DHCP** toggle to assign IP addresses to machines in the subnet automatically.

<alert-element type="warning" title="Warning">
 
For IPv6 networks, you can only enable or disable DHCP when creating a subnetwork. Changing this setting later is only possible via recreating the IPv6 subnetwork.
 
</alert-element>

8\. (optional) Turn on the **Non-routable subnetwork** toggle to block access to the subnet from external networks and other subnets. If you keep the network routable, you can specify the **Gateway IP** address. Otherwise, a random IP address will be assigned.

9\. (optional) Enter server addresses in the "Custom DNS" field to add specific DNS servers.

10\. (optional) Turn on **Add tags** to add metadata to the subnetwork.

11\. Click **Create subnetwork**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/create-subnetwork-annotated.png" alt="Network settings section with the highlighted Create a subnetwork button" width=80%>

## Set the IP range

While creating a subnetwork, specify the address range in the CIDR format.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/create-subnetwork.png" alt="Create a subnetwork dialog" width=80%>

The subnetwork size is set using the classless addressing (CIDR) method. You can use both private IPv6 and IPv4 addresses in subnetworks. 

Acceptable CIDR ranges for IPv4 addresses are as follows:

*   10.0.0.0 - 10.255.255.255 
*   172.16.0.0 - 172.31.255.255 
*   192.168.0.0 - 192.168.255.255
  
The valid subnet mask range is 16-29. 

## Configure network routing

A routed network is a private network that's already connected to a router with a public interface. All Virtual Machines in such networks can access the internet through the router and accept incoming connections. 

By default, a subnetwork in the cloud is created with internet access, which means that it’s  routable. If you need to restrict machines from external connections, you need to enable the **Non-routable subnetwork** option while creating a subnetwork. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/enable-non-routable-subnetwork.png" alt="Create subnetwork dialog" width=80%>

### Set up the default gateway

If your Gcore Virtual Machine or Gcore Bare Metal server has both public and private interfaces, disable the default gateway for all private subnetworks. Otherwise, there will be a conflict with the default gateway on the server, and you won’t be able to connect to the server. 

If you need to configure a gateway in a private subnetwork, ensure that only one of your subnetworks is routable. To do this, check the subnetwork settings and verify that only one subnetwork has the **Enable router gateway** toggle active.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/disable-router-gateway.png" alt="Edit subnetwork dialog" width=80%>

## Manage subnetworks

You can view and manage subnetworks on the **Networking** page of the Gcore Customer Portal. 

### Rename a subnetwork 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/networks-page.png" alt="Networks page open in the Customer Portal" width=80%>

2\. Find the network where you want to rename a subnetwork. Click the network's name to open it. 

3\. Click the three-dot icon next to the subnetwork you want to rename, then click **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/rename-subnetwork.png" alt="Network settings with the highlighted edit button" width=80%>

4\. Update the subnetwork’s name. 

5\. Click **Edit subnetwork** to save the changes. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/edit-subnetwork-menu.png" alt="Subnetwork settings" width=80%>

The subnetwork has been renamed.

### Delete a subnetwork

You can delete a subnetwork that’s not attached to a VM. 

To delete a subnetwork:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/networks-page.png" alt="Networks page open in the Customer Portal" width=80%>

2\. Find the network where you want to delete a subnetwork. Click the network's name to open it. 

3\. Click the three-dot icon next to the subnetwork you want to remove, then click **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/delete-subnetwork.png" alt="Network settings with the highlighted delete button" width=80%>

4\. Confirm your action by clicking **Delete** again.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-subnetwork/confirm-subnetwork-deletion.png" alt="Delete subnetwork confirmation dialog" width=80%> 

The subnetwork has been successfully removed.
