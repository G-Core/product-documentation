---
title: activate-link-aggregation
displayName: Activate Link Aggregation
published: true
toc:
 --1--Setup example for Ubuntu 14.04: "setup-example-for-ubuntu-14-04"
 --1--Configure LACP on the server: "configure-lasp-on-the-server"
pageTitle: Activate Link Aggregation | Gcore
pageDescription: Learn how to activate Link Aggregation (LACP) to boost server performance and enhance fault tolerance.
---
# Activate Link Aggregation

Bonding is the technology of aggregating several parallel channels in Ethernet network. The feature helps to balance server loading and increase fault tolerance. 

We set up channel aggregation using the standard LACP protocol. It is paid feature, take a look at prices <a href="https://gcore.com/hosting/miscellaneous" target="_blank">at the LACP tab</a>.

To get bonding order the service Port Channel from the Control Panel, prepare your server and then contact us via ticket to set it up. 

<img class="WACImage SCXW53247752" src="https://assets.gcore.pro/docs/hosting/other-services/link-aggreagtion/activate-link-aggregation/blobid1.png" alt="Port Channel from the Control Panel">

## Server Setup

## Setup example for Ubuntu 14.04

Install ifenslave package **before contacting us**:

```
# apt-get install ifenslave​
```

Add "bonding" to **/etc/modules** file.

Run modprobe load bonding immediately:

```
# modprobe bonding
```

Make sure it's loaded, you should see something like "bonding 147456 0":

```
# lsmod | grep bonding  
bonding 147456 0
```

## Configure LACP on the server

After LACP is ready from our side you need to configure it on the server.

Stop network services:

```
# stop networking
```

Edit network interfaces settings:

```
# vim /etc/network/interfaces
```

using the following example (replace em1 and em2 to your network interface names):

```
auto em1  
iface em1 inet manual  
bond-master bond0  
bond-primary em1  
  
auto em2  
iface em2 inet manual  
bond-master bond0  
  
auto bond0  
iface bond0 inet static  
 address 92.223.103.25  
 gateway 92.223.103.1  
 netmask 255.255.255.0  
  
bond-mode 4  
bond-miimon 100  
bond-lacp-rate 1  
bond-slaves em1 em2
```

Changes will apply after you do the following:

```
# start networking
```

If there is no network connection in the bonding, reboot your server. 

You can check the bond0 status:

```
# cat /proc/net/bonding/bond0
```

Output example:

```
Ethernet Channel Bonding Driver: v3.1.1 (September 26, 2006)

Bonding Mode: IEEE 802.3ad Dynamic link aggregation
Transmit Hash Policy: layer2 (0)
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

802.3ad info
LACP rate: fast
Active Aggregator Info:
Aggregator ID: 1
Number of ports: 2
Actor Key: 17
Partner Key: 1
Partner Mac Address: 00:77:54:71:a8:6f

Slave Interface: eth0
MII Status: up
Link Failure Count: 0
Permanent HW addr: 00:99:97:60:9d:48
Aggregator ID: 1

Slave Interface: eth1
MII Status: up
Link Failure Count: 0
Permanent HW addr: 00:00:85:60:9d:49
Aggregator ID: 1​
```

Please refer to <a href="https://help.ubuntu.com/community/UbuntuBonding" target="_blank">official Ubuntu manual</a> (search for "LACP").
