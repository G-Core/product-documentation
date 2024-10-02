---
title: create-and-configure-a-reserved-ip-address
displayName: Reserved IP address
order: 20
published: true
toc:
   --1--What it is used for: "what-it-is-used-for"
   --1--How it works: "how-it-works"
   --1--Billing: "how-it-is-charged"
   --1--Reserve: "reserve-an-ip-address"
   --1--Assign to a Virtual Machine: "assign-a-reserved-ip-to-a-vm-and-detach-it-from-the-machine"
   --1--Assign to a Load Balancer: "assign-a-reserved-ip-to-a-load-balancer-and-detach-it"
   --1--Determine which server the reserved IP is assigned to: "determine-which-server-the-specific-reserved-ip-is-assigned-to"
   --1--Delete a reserved IP: "delete-a-reserved-ip"
pageTitle: Reserved IP address| Gcore
pageDescription: Create and configure a reserved IP address to assign to Virtual Machines or Load Balancers. Learn how to reserve, assign, detach, and delete a reserved IP.
---
# Create and configure a reserved IP address

Reserved IP is an IP that you reserved for yourself and can be assigned to an <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">Virtual Machine</a> or <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">a Load Balancer</a> at any time.

## What it is used for

Since you know the IP of the future equipment, you can pre-configure your services for it — for example, create a DNS record for this IP or configure the server to connect to it.

A reserved IP can also be used as a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">virtual IP address</a>.

## How it works

After you created a reserved IP, this address becomes yours inside our system. No one can use it except you.

## How it is charged

The IP price per month is displayed in the order window. You pay only for the time from creating an IP to deleting it. 

For example, if you had reserved an IP and then deleted it after an hour, you will be charged only for an hour of use. The price doesn’t depend on whether the address is assigned to the Virtual Machine or not.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-17.png" alt="How it is charged" width="380" height="168">

## Reserve an IP address

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/networks-page.png" alt="Networks page in the Customer Portal" width="80%">

2\. Open the **Reserved IPs** page.

3\. Click **Reserve new IP**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/reserved-ips-page.png" alt="Reserved IPs page in the Customer Portal" width="80%">

4\. Select the IP type:

 * Public (for external network). A public IP address one can be created immediately.
 * Private (for internal network). If you selected this option, choose the network and subnetwork in which the address will be created.

<alert-element type="info" title="Info">
 
A reserved private IP can only be used in the specified subnetwork. To order a specific address, enable the **Set IP address** toggle and enter the IP that belongs to that subnetwork.
 
</alert-element>

5\. (Optional) If you want to use IPv6 addresses, turn on the <b>Enable IPv6 dual-stack</b> toggle.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/reserve-ip-dialog.png" alt="Reserved IPs page in the Customer Portal" width="80%">

6\. Click **Create**. 

## Assign a reserved IP to a VM and detach it from the machine

<tabset-element>

### Assign during VM creation

For instructions on how to add a Reserved IP when creating a Virual Machine, refer to the <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">VM creation</a> guide. 

### Assign after VM creation

1\. In the Virtual Machine settings, open the **Networking** tab. 

If the machine has already been added to the subnetwork you want to assign an IP to, disable that subnetwork. This will remove the old IP.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/detach-subnetwork.png" alt="Detach subnetwork" width="80%">

2\. Add a new interface (public or private) and enable the **Use reserved IP** toggle. 

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/add-reserved-ip-vm.png" alt="Assign after Virtual Machine creation" width="80%">

3\. Select the desired IP and click **Save Changes**. 

The IP will be assigned to the Virtual Machine.

</tabset-element>

## Detach a reserved IP from the VM

Detach the subnetwork the reserved IP is assigned to. This address will be detached from the Virtual Machine automatically.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-29.png" alt="Detach from the Virtual Machine">

## Assign and detach a reserved IP from a Load Balancer

You can assign the reserved IP only during the Load Balancer creation. 

For instructions on how to add a Reserved IP when creating a Load Balancer, refer to the <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#step-4-configure-network" target="_blank">Load Balancer creation</a> guide. 

## Determine which server the specific reserved IP is assigned to

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **Cloud** > **Networking**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/networks-page.png" alt="Networks page in the Customer Portal" width="80%">

2\. Open the **Reserved IPs** page. In the **Status** column, you will see what resource the IP is assigned to. 

3\. Click the resource name to view and update its settings.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip2.png" alt="mceclip2.png">

## Delete a reserved IP

Detach it from the Virtual Machine or Load Balancer. Then go to the "Networking" → "Reserved IPs" section, click the selector next to the IP and select "Delete". The address will be deleted and no longer charged.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip3.png" alt="mceclip3.png">