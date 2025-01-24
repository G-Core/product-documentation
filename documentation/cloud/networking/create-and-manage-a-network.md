---
title: create-and-manage-a-network
displayName: Network
published: true
order: 10
toc:
   --1--Types of networks: "types-of-networks"
   --1--Create and attach networks: "create-and-attach-networks-to-cloud-resources"
   --1--Detach networks: "detach-a-network-from-a-vm-or-bare-etal"
   --1--Manage networks: "manage-networks"
pageTitle: Add a network | Gcore
pageDescription: Learn how to create and manage a network in the cloud to transfer information between cloud resources and establish an Internet connection.
---
# Create and manage a network

A Gcore Cloud network is a virtualized software-defined network that operates in a cloud computing infrastructure. Cloud networks are used to transfer information between cloud resources and provide an internet connection.  

You can attach networks (also known as network interfaces) to <a href="https://gcore.com/docs/cloud/virtual-instances/types-of-virtual-machines" target="_blank">Virtual Machines</a>, <a href="https://gcore.com/docs/cloud/bare-metal-servers/about-bare-metal-servers" target="_blank">Bare Metal</a>, <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">Load Balancers</a>, and <a href="https://gcore.com/docs/cloud/kubernetes/about-gcore-kubernetes" target="_blank">Managed Kubernetes</a> clusters. 

## Types of networks 

For Cloud resources, you can configure the following types of networks: 

* **Private network**: This interface is for local internal connections to the server and doesn't have access to the external network. Resources with private interfaces can only be accessed from the same network. However, you can customize their setup and establish internet connectivity.  
For example, if you add a VM with a private interface to a public Load Balancer, this Virtual Machine will receive requests from the internet. You can configure a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">Floating IP address</a>. 

* **Public network**: This interface grants access to the external network. Instances with that interface will be available from the internet.

* **Dedicated network**: This network type is designed for individual usage, providing an exclusive pool of addresses for each client. It works with Bare Metal servers and supports assigning multiple public IP addresses to a single server, making it ideal for advanced use cases such as virtualization and traffic balancing. These networks rely on dedicated public subnets, and the number of supported public IPs depending on the size of the assigned subnet. Other customisations are available upon request to meet specific needs. 

## Create and attach networks to Cloud resources 

You can attach both public and private networks to Virtual Machines, Bare Metal, Load Balancers, and Managed Kubernetes clusters. 

There are two ways to create and attach a network: during resource creation or by adding a network separately and then attaching it to an existing Cloud resource. 

For a Dedicated network, it must first be configured by the support team before it can be selected or used. This network type allows the assignment of multiple public IP addresses to a single server, with the total number of IPs determined by the size of the assigned subnet. Public IPs in a Dedicated Network must be explicitly assigned to the server to function. Unassigned IPs within the subnet will not be operational.


### Attach a network when creating a new Cloud resource 

For detailed steps on how to attach a network interface for each resource, refer to the relevant guide: 

* <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">Attach network interface to a Virtual Machine</a>  
* <a href="https://gcore.com/docs/cloud/bare-metal-servers/create-a-bare-metal-server" target="_blank">Attach network interface to a Bare Metal</a> 
* <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster#step-6-configure-network-settings" target="_blank">Attach network interface to a Managed Kubernetes cluster</a>  
* <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#step-4-configure-network" target="_blank">Attach network interface to a Load Balancer</a> 

### Create a network from the Networks page  

You can create new network interfaces in the Customer Portal, on the **Networks** page. 

To add a new network: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**.

2\. Click **Create network**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/networking-page.png" alt="Create network page in the Customer Portal" width="80%">

3\. Enter the network name. 

4\. (Optional) If you want to create a network for Bare Metal servers, turn on the **Bare Metal Network (VLAN)** toggle. 

5\. (Optional) Add tags if you want to include metadata. 

6\. Click **Create network**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/create-network-dialog.png" alt="Create network dialog" width="80%">

If you need to configure a private network, you also need to add a subnetwork. To do so, follow instructions from the <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#create-a-subnetwork-from-the-networks-page" target="_blank">creating a subnetwork</a>

### Attach a network interface to an existing VM or Bare Metal 

<alert-element type="info" title="Info">
 
You can’t change network interfaces for created Load Balancers. 
 
</alert-element>

If you’ve already created a cloud resource and want to add more networks to it, you can do so in the resource settings: 

1\. In the Gcore Customer Portal, navigate to **Cloud**. 

2\. Open the relevant page with your resource: **Virtual Instances** or **Bare Metal**. 

3\. Click the resource name to open its settings. 

4\. Go to the **Networks** tab. Here you can view, attach, and detach network interfaces attached to your resource. Here's the network configuration for a Virtual Machine:

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/networking-tab-vm.png" alt="Networking tab in the VM settings" width="80%">

5\. To attach a new interface, click **Add interface**: 

* **Public**: It’s only possible to add one public interface per VM.  Additionally, you can use a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a>. 

* **Private**: Choose a network from the list or create a new one, then <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork" target="_blank">configure a subnetwork</a> according to your requirements.  

6\. (Optional) If your network contains both IPv6 and IPv4 addresses, you can enable IPV6 dual-stack and simultaneously use IPv4 and IPv6 protocols on the same network infrastructure. 

7\. Click **Save Changes**. 

You’ve successfully attached a new network interface to your resource. 

## Detach a network from a VM or Bare Metal 

To remove an interface from your cloud resource, you need to detach all subnetworks within this network interface: 

1\. In the Gcore Customer Portal, navigate to **Cloud**. 

2\. Open the relevant page with your resource: **Virtual Instances** or **Bare Metal**. 

2\. Find the needed resource and click its name to open it. 

3\. Go to the **Networks** tab and find the network you want to detach. To remove an interface from your cloud resource, you first need to detach all existing subnetworks. 

4\. Click the three-dot icon next to each subnetwork within the network and select **Detach subnetwork**.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/detach-subnetwork.png" alt="Network settings with the detach subnetwork option" width="80%">

If you have a connected Floating IP, detach it before removing subnetworks.

5\. Confirm the action by clicking **Detach**.

Repeat this step for all subnetworks within the network. 

## Manage networks 

All your configured network interfaces and their subnetworks appear in the Customer Portal, on the **Networks** page. 

You can view network details, rename or delete a network, and configure its subnetworks. 

### View network details 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**. 

2\. Find the needed network and click its name to open the details page. 

The details page includes comprehensive information about the network, such as network ID, creation date, tags, and other relevant specifications. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/network-details.png" alt="Network details page" width="80%">

Here you can also create and remove <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork" target="_blank">subnetworks</a>. 

### Rename a network  

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**. 

2\. Find the network that you want to rename and click the three-dot icon next to it. 

3\. Select **Rename**.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/rename-network.png" alt="Network settings menu with the rename button highlighted" width="80%">

4\. Enter a new name and click **Save** to apply the changes.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/edit-name-description.png" alt="Edit network name and description dialog" width="80%">

The network has been renamed. 

### Delete a network 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**. 

2\. Find the network that you want to remove and click the three-dot icon next to it. 

3\. Select **Delete**.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/delete-network.png" alt="Network settings menu with the delete button highlighted.png" width="80%">

4\. Click **Delete network** to confirm your action.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-network/verify-deletion.png" alt="Delete network dialog" width="80%">

You’ve successfully removed a network. 
