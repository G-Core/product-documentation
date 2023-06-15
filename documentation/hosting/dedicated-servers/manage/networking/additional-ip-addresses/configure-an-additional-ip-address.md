---
title: configure-an-additional-ip-address
displayName: Configure
order: 21
published: true
toc:
    --1--For Debian/Ubuntu: "configure-an-additional-ip-address-on-debian-ubuntu"
    --1--For CentOS: "configure-an-additional-ip-address-on-centos"
    --1--For Windows 2012: "configure-an-additional-ip-address-on-windows-server-2012"
---
# Configure an additional IP address

An additional IP address becomes available only after you configure it.

This guide will help you to configure IP addresses manually. If you want to configure it automatically, reinstall the operating system of your server.

## Configure an additional IP address on Debian/Ubuntu

1\. Open the network configuration file in **/etc/network/interfaces**.

2\. Add the following lines to the file:

```
auto eth0:N  
iface eth0:N inet static  
                address Х. Х. Х. Х  
                netmask 255.255.255.255
```

Replace:
- ```N``` with the serial number of the interface (0 for the first one, 1 for the second, etc.), 
- ```Х.Х.Х.Х``` with the IP address you want to add, 
- ```255.255.255.255``` with the net mask. You can find it in your Control Panel. Go to the **Dedicated servers** tab, choose the server you need, and click the IP addresses button.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/additional-ip-addresses/configure-an-additional-ip-address/13640001933073.png" alt="" width="70%">

If you need to add an IPv6 address, add the following:

```
iface eth0:N inet6 static  
    address 2х01:Х:X:X::X
```
3\. Save the file.

4\. Reboot the server or run the "**service network restart**" command.

## Configure an additional IP address on CentOS

1\. Create the ```ifcfg-eth0:N``` file in the **/etc/sysconfig/network-scripts/** directory.

2\. Add the following lines to the file:

```
DEVICE=eth0:N  
ONBOOT=yes  
BOOTPROTO=static  
IPADDR=X.X.X.X  
NETMASK=255.255.255.255
```

Replace:
- ```N``` with the serial number of the interface (0 for the first one, 1 for the second, etc.), 
- ```Х.Х.Х.Х``` with the IP address you want to add, 
- ```255.255.255.255``` with the netmask. You can find it in your Control Panel. Go to the **Dedicated servers** tab, choose the server you need, and click the IP addresses button.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/additional-ip-addresses/configure-an-additional-ip-address/13640001933073.png" alt="" width="70%">

If you need to add an IPv6 address, add the following:

```
IPV6ADDR_SECONDARIES="2х01:Х:X:X::X/64"
```

Replace ```2х01:Х:X:X::X/64``` with the IP address you want to add.

3\. Save the file.

4\. Reboot the server or run the "**service network restart**" command.

## Configure an additional IP address on Windows Server 2012

1\. Run the server via RDP.

2\. Click **Start** and find **Server Manager**.

3\. In the Server Manager window, click **Local Server.**

4\. In the Server Configuration page, right-click the connection you want to configure and select **Properties**.

5\. Choose IP Version: for IPv4, select **Internet Protocol Version 4 (TCP/IPv4)**, and for IPv6, select **Internet Protocol Version 6 (TCP/IPv6)**.

6\. Click **Advanced** and then select **Add** to specify the IP address and the subnet mask.

7\. Click **Ok** to save the changes, and then click **Close**.