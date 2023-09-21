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
   --1--Assign to an instance: "assign-a-reserved-ip-to-an-instance-and-detach-it-from-the-machine"
   --1--Assign to a load balancer: "assign-a-reserved-ip-to-a-load-balancer-and-detach-it"
   --1--Determine which server the reserved IP is assigned to: "determine-which-server-the-specific-reserved-ip-is-assigned-to"
   --1--Delete: "delete-a-reserved-ip-address"
pageTitle: Reserved IP address| Gcore
pageDescription: Create and configure a reserved IP address to assign to instances or load balancers. Learn how to reserve, assign, detach, and delete a reserved IP.
---
# Create and configure a reserved IP address

Reserved IP is an IP that you reserved for yourself and can be assigned to an <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">instance</a> or <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">a load balancer</a> at any time.

## What it is used for

Since you know the IP of the future equipment, you can pre-configure your services for it — for example, create a DNS record for this IP or configure the server to connect to it.

Also, a reserved IP can be used as a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">virtual IP address</a> .

## How it works

After you created a reserved IP, this address becomes yours inside our system. No one can use it except you.

## How it is charged

The IP price per month is displayed in the order window. You pay only for the time from creating an IP to deleting it: for example, if you had reserved an IP and then deleted it after an hour, you will be charged only for an hour of use. The price doesn’t depend on whether the address is assigned to the instance or not.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-17.png" alt="How it is charged" width="380" height="168">

## Reserve an IP address

Open the tab "Reserved IPs" in the "Networking" section.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip0.png" alt="mceclip0.png">

Click the "Reserve new IP" button

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip1.png" alt="mceclip1.png">

Select the IP type — public (for external network) or private (for internal network). A public one can be created immediately. For private, select the network and subnet in which the address will be created. Please note: reserved private IP can only be used in the specified subnet. If you wish, you can order a specific address by entering it in the "IP address" section (it must belong to the subnet). Then click "Create".

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-20.png" alt="Select the IP type " width="367" height="164">

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-21.png" alt="Select the IP type " width="359" height="334">
</media-gallery>

## Assign a reserved IP to an instance and detach it from the machine

### Assign during instance creation

When creating an instance, in the "Network settings" section click the arrow next to the network you want to assign an IP to. Then move the "Use reserved IP" slider and select the desired IP from the list. Save the settings and this address will be assigned to the instance.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-22.png" alt="Assign during instance creation" width="417" height="152">
   
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-23.png" alt="Assign during instance creation" width="411" height="156">
   
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-24.png" alt="Assign during instance creation" width="415" height="263">
</media-gallery>

### Assign after instance creation

Go to the instance menu and open the "Networking" section.

If the machine has already been added to the subnet you want to assign an IP to, disable that subnet. This will remove the old IP.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-25.png" alt="Assign after instance creation">

Add a new interface (public or private) and move the "Use reserved IP" slider. Then select the desired IP and click "Save Changes". The IP will be assigned to the instance.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-26.png" alt="Assign after instance creation">

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-27.png" alt="Assign after instance creation">
   
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-28.png" alt="Assign after instance creation">
</media-gallery>

### Detach from the instance

Detach the subnet the reserved IP is assigned to. This address will be detached from the instance automatically.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-29.png" alt="Detach from the instance">

## Assign a reserved IP to a load balancer and how to detach it

You can assign the reserved IP only during the balancer creation. In the "Network" section, select the network (public or private) to which you want to bind the address, move the "Use reserved IP" slider, and select the required IP. It will be assigned to the balancer.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-30.png" alt="Assign a reserved IP to a load balancer and how to detach it" width="441" height="102">
   
<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/image-31.png" alt="Assign a reserved IP to a load balancer and how to detach it" width="438" height="216">
</media-gallery>

## Determine which server the specific reserved IP is assigned to

Open the "Networking" → "Reserved IPs" section. In the "Status" column, you will see what equipment the IP is assigned to. Click the orange text "Instance" or "Load Balancer" to go to the menu of this equipment.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip2.png" alt="mceclip2.png">

## Delete a reserved IP address

Detach it from the instance or load balancer. Then go to the "Networking" → "Reserved IPs" section, click the selector next to the IP and select "Delete". The address will be deleted and no longer charged.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address/mceclip3.png" alt="mceclip3.png">
