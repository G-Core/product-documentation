---
title: create-and-configure-a-reserved-ip-address
displayName: Reserved IP address
order: 20
published: true
toc:
   --1--What a reserved IP is used for: "what-a-reserved-ip-is-used-for"
   --1--How does it work: "how-does-it-work"
   --1--Billing: "how-it-is-charged"
   --1--Reserve: "reserve-an-ip-address"
   --1--Assign a reserved IP to a VM: "assign-a-reserved-ip-to-a-vm"
   --1--Detach from a Virtual Machine: "detach-a-reserved-ip-from-a-vm"   
   --1--Assign to a Load Balancer: "assign-a-reserved-ip-to-a-load-balancer"
   --1--Find a resource with reserved IP: "find-a-resource-with-reserved-ip"
   --1--Delete a reserved IP: "delete-a-reserved-ip"
pageTitle: Reserved IP address | Gcore
pageDescription: Create and configure a reserved IP address to assign to Virtual Machines or Load Balancers. Learn how to reserve, assign, detach, and delete a reserved IP.
---
# Create and configure a reserved IP address

A reserved IP is a dedicated IP address that you can assign to a <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">Virtual Machine</a> or a <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">Load Balancer</a> at any time.

## What a reserved IP is used for

Since you know the IP address in advance, you can pre-configure your services for it—for example, create a DNS record for this IP or configure the server to connect to it.

A reserved IP can also be used as a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">virtual IP address</a>.

## How does it work

After you create a reserved IP, this address becomes yours inside our system. No one can use it except you.

## How it is charged

The monthly price for the IP is displayed in the order window. You pay only for the time from creating an IP to deleting it. 

For example, if you had reserved an IP and then deleted it after an hour, you will be charged only for an hour of use. The price remains the same whether the IP address is assigned to a Virtual Machine or not.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/create-reserved-ip-dialog.png" alt="How it is charged" width="80%">

## Reserve an IP address

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/networks-page.png" alt="Networks page in the Customer Portal" width="80%">

2\. Open the **Reserved IPs** page.

3\. Click **Reserve new IP**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/reserved-ips-page.png" alt="Reserved IPs page in the Customer Portal" width="80%">

4\. Select the IP type:

 * Public (for external network). A public IP address can be created immediately.
 * Private (for internal network). If you selected this option, choose the network and subnetwork in which the address will be created.

<alert-element type="info" title="Info">
 
A reserved private IP can only be used in the specified subnetwork. To order a specific address, enable the **Set IP address** toggle and enter the IP that belongs to that subnetwork.
 
</alert-element>

5\. (Optional) If you want to use IPv6 addresses, turn on the <b>Enable IPv6 dual-stack</b> toggle.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/create-reserved-ip-dialog.png" alt="Reserved IPs page in the Customer Portal" width="80%">

6\. Click **Create**. 

## Assign a reserved IP to a VM

<tabset-element>

### During VM creation

For instructions on how to add a Reserved IP when creating a Virtual Machine, refer to the <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance#step-5-add-network-interfaces" target="_blank">VM creation</a> guide. 

### After VM creation

1\. In the Virtual Machine settings, open the **Networking** tab. 

If the machine is already connected to the target subnetwork, detach it first before assigning a new IP. This will remove the old IP.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/detach-subnetwork.png" alt="Detach subnetwork" width="80%">

2\. Add a new interface (public or private) and enable the **Use reserved IP** toggle. 

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/add-reserved-ip-vm.png" alt="Assign after Virtual Machine creation" width="80%">

3\. Select the reserved IP and click **Save Changes**. 

The IP will be assigned to the Virtual Machine.

</tabset-element>

<alert-element type="info" title="Info"> 

If you add a public interface after creating a Virtual Machine, you may need to configure it manually on some operating systems. The OS cannot automatically detect and apply the new interface settings, especially for BMs. If your VM has an IPv6 address, it will be configured automatically without additional setup.

</alert-element>

## Detach a reserved IP from a VM

Detach the subnetwork to which the reserved IP is assigned. This address will be detached from the Virtual Machine automatically.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/detach-subnetwork.png" alt="Detach from the Virtual Machine">

## Assign a reserved IP to a Load Balancer

You can assign the reserved IP only during the Load Balancer creation. 

For instructions on how to add a Reserved IP when creating a Load Balancer, refer to the <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#step-4-configure-network" target="_blank">Load Balancer creation</a> guide. 

## Find a resource with reserved IP

If a reserved IP address is attached to a particular resource, you'll see this information on the **Reserved IPs** page, in the **Status** column:

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/attached-to-instance.png" alt="Reserved IPs page in the Customer Portal" width="80%">

You click the resource name to view and update its settings.

## Delete a reserved IP

If the reserved IP is attached to the Virtual Machine or Load Balancer, you need to detach it first. Otherwise, you won't be able to delete the IP.

To delete a reserved IP address:

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/networks-page.png" alt="Networks page in the Customer Portal" width="80%">

2\. Open the **Reserved IPs** page.

3\. Click a three-dot icon next to the IP you want to delete.

4\. Select **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/delete-reserved-ip.png" alt="Delete a reserved IP button" width="80%">
