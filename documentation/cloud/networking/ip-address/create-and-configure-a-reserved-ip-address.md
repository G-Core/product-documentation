---
title: create-and-configure-a-reserved-ip-address
displayName: Reserved IP address
order: 20
published: true
toc:
   --1--What it is used for: ""
   --1--How it works: ""
   --1--How it is charged: ""
   --1--How to reserve an IP: ""
   --1--How to assign a reserved IP to an instance and how to detach it from the machine: ""
   --1--Assign during instance creation: ""
   --1--Assign after instance creation: ""
   --1--Detach from the instance: ""
   --1--How to assign a reserved IP to a load balancer and how to detach it: ""
   --1--How to find out the equipment the specific reserved IP is assigned to: ""
   --1--How to delete a reserved IP: ""
---
Reserved IP is an IP that you reserved for yourself and can be assigned to an [instance](https://gcorelabs.com/support/articles/360019378537/) or [load balancer](https://gcorelabs.com/support/articles/360004523578/) at any time.


What it is used for
-------------------

Since you know the IP of the future equipment, you can pre-configure your services for it — for example, create a DNS record for this IP or configure the server to connect to it.

Also, a reserved IP can be used as a [virtual IP](https://gcorelabs.com/support/articles/4405866963345/).

How it works
------------

After you created a reserved IP, this address becomes yours inside our system. No one can use it except you.

How it is charged
-----------------

The IP price per month is displayed in the order window. You pay only for the time from creating an IP to deleting it: for example, if you had reserved an IP and then deleted it after an hour, you will be charged only for an hour of use. The price doesn’t depend on whether the address is assigned to the instance or not.

[<img src="https://support.gcore.com/hc/article_attachments/4405921021457/image-17.png" alt="" width="380" height="168">](https://support.gcorelabs.com/hc/article_attachments/4405921021457/image-17.png)

How to reserve an IP
--------------------

Open the tab "Reserved IPs" in the "Networking" section.

<img src="https://support.gcore.com/hc/article_attachments/5287105533073/mceclip0.png" alt="mceclip0.png">Click the "Reserve new IP" button

<img src="https://support.gcore.com/hc/article_attachments/5287183411857/mceclip1.png" alt="mceclip1.png">Select the IP type — public (for external network) or private (for internal network). A public one can be created immediately. For private, select the network and subnet in which the address will be created. Please note: reserved private IP can only be used in the specified subnet. If you wish, you can order a specific address by entering it in the "IP address" section (it must belong to the subnet). Then click "Create".

[<img src="https://support.gcore.com/hc/article_attachments/4405927362449/image-20.png" alt="" width="367" height="164">](https://support.gcorelabs.com/hc/article_attachments/4405927362449/image-20.png)[<img src="https://support.gcore.com/hc/article_attachments/4405927363089/image-21.png" alt="" width="359" height="334">](https://support.gcorelabs.com/hc/article_attachments/4405927363089/image-21.png)

How to assign a reserved IP to an instance and how to detach it from the machine
--------------------------------------------------------------------------------

### Assign during instance creation

When creating an instance, in the "Network settings" section click the arrow next to the network you want to assign an IP to. Then move the "Use reserved IP" slider and select the desired IP from the list. Save the settings and this address will be assigned to the instance.

[<img src="https://support.gcore.com/hc/article_attachments/4405927362577/image-22.png" alt="" width="417" height="152">](https://support.gcorelabs.com/hc/article_attachments/4405927362577/image-22.png)[<img src="https://support.gcore.com/hc/article_attachments/4405927362961/image-23.png" alt="" width="411" height="156">](https://support.gcorelabs.com/hc/article_attachments/4405927362961/image-23.png)[<img src="https://support.gcore.com/hc/article_attachments/4405927363729/image-24.png" alt="" width="415" height="263">](https://support.gcorelabs.com/hc/article_attachments/4405927363729/image-24.png)

### Assign after instance creation

Go to the instance menu and open the "Networking" section.

If the machine has already been added to the subnet you want to assign an IP to, disable that subnet. This will remove the old IP.

[<img src="https://support.gcore.com/hc/article_attachments/4405927363985/image-25.png" alt="">](https://support.gcorelabs.com/hc/article_attachments/4405927363985/image-25.png)Add a new interface (public or private) and move the "Use reserved IP" slider. Then select the desired IP and click "Save Changes". The IP will be assigned to the instance.

[<img src="https://support.gcore.com/hc/article_attachments/4405927364241/image-26.png" alt="">](https://support.gcorelabs.com/hc/article_attachments/4405927364241/image-26.png)[<img src="https://support.gcore.com/hc/article_attachments/4405921022481/image-27.png" alt="">](https://support.gcorelabs.com/hc/article_attachments/4405921022481/image-27.png)[<img src="https://support.gcore.com/hc/article_attachments/4405927368081/image-28.png" alt="">](https://support.gcorelabs.com/hc/article_attachments/4405927368081/image-28.png)

### Detach from the instance

Detach the subnet the reserved IP is assigned to. This address will be detached from the instance automatically.

[<img src="https://support.gcore.com/hc/article_attachments/4405921023249/image-29.png" alt="">](https://support.gcorelabs.com/hc/article_attachments/4405921023249/image-29.png)

How to assign a reserved IP to a load balancer and how to detach it
-------------------------------------------------------------------

You can assign the reserved IP only during the balancer creation. In the "Network" section, select the network (public or private) to which you want to bind the address, move the "Use reserved IP" slider, and select the required IP. It will be assigned to the balancer.

[<img src="https://support.gcore.com/hc/article_attachments/4405921022993/image-30.png" alt="" width="441" height="102">](https://support.gcorelabs.com/hc/article_attachments/4405921022993/image-30.png)[<img src="https://support.gcore.com/hc/article_attachments/4405927367697/image-31.png" alt="" width="438" height="216">](https://support.gcorelabs.com/hc/article_attachments/4405927367697/image-31.png)

How to find out the equipment the specific reserved IP is assigned to
---------------------------------------------------------------------

Open the "Networking" → "Reserved IPs" section. In the "Status" column, you will see what equipment the IP is assigned to. Click the orange text "Instance" or "Load Balancer" to go to the menu of this equipment.

<img src="https://support.gcore.com/hc/article_attachments/5287346918289/mceclip2.png" alt="mceclip2.png">

How to delete a reserved IP
---------------------------

Detach it from the instance or load balancer. Then go to the "Networking" → "Reserved IPs" section, click the selector next to the IP and select "Delete". The address will be deleted and no longer charged.

<img src="https://support.gcore.com/hc/article_attachments/5287371219089/mceclip3.png" alt="mceclip3.png">
