---
title: create-and-configure-a-virtual-ip-vip-address
displayName: Virtual IP address
order: 30
published: true
toc:
   --1--What is it?: "what-is-a-virtual-ip-address"
   --1--Billing: "billing"
   --1--Public IP limits: "public-ip-limits"
   --1--Create a virtual IP: "create-a-virtual-ip-address"
   --1--Use a virtual IP to create a fault-tolerant system: "assign-a-virtual-ip-address-to-multiple-vms"
   --1--Assign a virtual IP address as a secondary address: "assign-a-virtual-ip-address-as-a-secondary-address"
pageTitle: Virtual IP address | Gcore
pageDescription: Create and configure a virtual IP address to assign to multiple Virtual Machines or use as a secondary IP address for a network interface.
---
# Create and configure a virtual IP address

## What is a virtual IP address?

A virtual IP address (VIP)  is an IP address that can be assigned to multiple Virtual Machines or serve as a secondary IP address for a network interface.

## How does it work?

**To use a VIP to create a fault-tolerant system**, you’ll need to install and configure Keepalived, which is a system daemon for Linux. Keepalived uses the Virtual Router Redundancy Protocol (VRRP) to manage the VIP. This protocol allows multiple machines to share a common IP address, and Keepalived uses VRRP to pass the VIP address between the primary machine and the backup machines. When the primary machine fails, the VRRP protocol detects the failure and passes the VIP to one of the backup machines, ensuring that the network service remains available.

**To** **use a VIP as a secondary address** for a network interface, you will reserve a VIP and assign it to a Virtual Machine, first in the settings of our system, then in the settings of the machine. As a result, the VIP becomes the address of the Virtual Machine, working in conjunction with its regular IP address, allowing the machine to receive and transmit data on behalf of both addresses.

## Billing

A VIP is billed from the moment you reserve it until the moment you delete it. For example, if you reserve an IP address and then delete it after an hour, you will be charged only for an hour of use, regardless of whether the address was assigned to the Virtual Machine or not.

The monthly price is displayed in the order window.

## Public IP limits

A Virtual Machine has only one public interface, meaning it receives a Public IP from the public network. It also supports multiple Floating IPs from private networks, but quotas limit the number. In a multi-network setup, each subnet can have one Floating IP. Within a single network, multiple subnets can exist, and each subnet of a single machine (VM/BM) is allowed one Floating IP. 

By default, Bare Metal servers support up to six attached IPs. A dedicated Bare Metal network removes this limit, allowing unlimited IPs per machine. Unlike standard networks, this type of network lacks port security and can be allocated by request.


## Create a virtual IP address

1\. In the Cloud menu, go to **Networking** → **Reserved IPs** and click **Reserve new IP**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12896827624209.png" alt="Screenshot_2023-02-07_at_14.59_1.png">

2\. In the new window, select the type of an IP address depending on the required network interface: public or private.  

If you select **Private**, specify the network and subnetwork. If you want to reserve a specific IP address, turn on the **Set IP address** toggle and choose an IP address from the valid CIDR. Otherwise, you will be assigned a random IP address.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12896898220817.png" alt="Screenshot_2023-02-07_at_15.28.15.png">

3\. Go back to the list of reserved IP addresses, find the required IP address, click **⋯** next to it and select **VIP settings**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12896925225233.png" alt="Screenshot_2023-02-07_at_15.53_1.png">

4\. In the pop-up window, turn on the **Is VIP** toggle and click **Save**.  
You have reserved a virtual IP address. You can now assign it multiple machines to create a fault-tolerant system or to add as a secondary address for your network interface.

## Assign a virtual IP address to multiple VMs

1\. In the Cloud menu, go to **Networking** → **Reserved IPs**, find the required virtual IP address, click **VIP** in the **Status** column.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12946840118161.png" alt="Screenshot_2023-02-13_at_11.27_1.png">

2\. In the pop-up window, add the required Virtual Machines, specify their ports and click **Save**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12897006107153.png" alt="Screenshot_2023-02-08_at_17.11.42.png">

3\. Install and configure Keepalived on your Virtual Machines using <a href="https://keepalived.readthedocs.io/en/latest/installing_keepalived.html" target="_blank">the official Keepalived documentation</a>.

4\. Change the Keepalived configuration file to set the "MASTER" machine and "BACKUP" machines. Additionally, set the priority to determine the order in which the VIP will be transferred between devices. If the master server fails, the IP address will be transferred to the backup machine with the highest priority. If the second machine fails, the VIP will be transferred to the backup machine with the second-highest priority.

5\. Run Keepalived on your Virtual Machine and add it to the autostart list. 

You have configured the VIP for your machines. The fault-tolerant system is now operational.

## Assign a virtual IP address as a secondary address

1\. In the Cloud menu, go to **Networking** → **Reserved IPs**, find the required virtual IP address, click **VIP** in the **Status** column.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12946840118161.png" alt="Screenshot_2023-02-13_at_11.27_1.png">

2\. In the pop-up window, add the required Virtual Machine, specify its port and click **Save**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12897006107153.png" alt="Screenshot_2023-02-08_at_17.11.42.png">

Now you have to configure the VIP in the Virtual Machine settings. Below are two guides for Windows and non-Windows VMs.

## Configure a virtual IP address for non-Windows Virtual Machines

1\. Connect to your Virtual Machine.

2\. Run the following command as an administrator:

```
ip addr add [VIP]/[mask] dev [interface name]
```

where:  
\- **\[VIP\]** is the virtual IP address that you want to add to the interface.  
\- **\[mask\]** is the subnet mask associated with the virtual IP address. You can find it in the **Networking** tab of your Virtual Machine.  
\- **\[interface name\]** is the name of the network interface where the IP address will be added. To find the name, run the command:  

```
ip addr  
```

The interface name will appear on the left below the loopback interface.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12946900210833.png" alt="Screenshot_2023-02-08_at_13.30_1.png">

For example, to add the virtual IP address _192.168.1.200_ with a subnet mask of _24_ to the _eth0_ interface, you would use the following command:

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12946938150161.png" alt="Screenshot_2023-02-08_at_14.04.13.png">

Note: **the command assigns the VIP to your machine until it restarts**. After rebooting, run the command to assign the VIP again. To permanently assign a VIP to a Virtual Machine, refer to the official documentation of your OS to add the IP address to the system network settings.

The VIP has been configured. To verify it, <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">connect to your Virtual Machine via SSH</a> using your VIP. If the connection fails, there may be an error in the IP assignment command or the IP address may not have been added inside your system. Repeat the Steps again.

### Configure a virtual IP address for Windows Virtual Machines

1\. Open the **Control Panel**.  
2\. Go to the **Network and Sharing Center**.  
3\. Right-click the active network connection that you want to add the virtual IP address to and select **Properties**.  
4\. Select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12946990237457.png" alt="18.png">

5\. Click **Use the following IP address** option and enter the virtual IP address, subnet mask, and default gateway in the appropriate fields. To find these parameters, run the following command:

```
ipconfig  
```

You will see the output:

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12947005842961.png" alt="16.png">

Go back to the **Control Panel**, make sure the values are correct and click **Advanced ....**

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/12947053843345.png" alt="19.png">

6\. In the **IP Settings** tab, find the **IP addresses** section and click **Add ....**

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/20.png" alt="20.png" width="344" height="420">

7\. In the next window, enter your VIP and the subnet mask from the command line. Then click **Add**.

<img src="https://assets.gcore.pro/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address/21.png" alt="21.png" width="344" height="419">

8\. Click **OK**.

The VIP has been configured. To verify it, <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">connect to your Virtual Machine via SSH</a> using your VIP. If the connection fails, there may be an error in the IP assignment command or the IP address may not have been added inside your system. Repeat the Steps.
