---
title: configure-a-10-gbps-network-card
displayName: 10 Gbps network card
order: 31
published: true
toc:
   --1--For Ubuntu/Debian: "configure-a-10-gbps-interface-for-ubuntu-debian-servers"
   --1--For CentOS: "configure-a-10-gbps-interface-for-centos"
pageTitle: Configure a 10 Gbps network card | Gcore
pageDescription: Learn how to configure a 10 Gbps network card on your Ubuntu, Debian, or CentOS server with this step-by-step guide.
---
# Configure a 10 Gbps network card

Each dedicated server has multiple network cards connected to separate network switches. By default, the installed OS is configured to use a 1 Gbps network card. To use a faster 10 Gbps network card, you should configure the 10 Gbps interface manually.

If you want to avoid failover, we recommend using Link Aggregation Control Protocol (LACP).

**Please note**: This guide is for experienced users. Consult your system administrator if you have any difficulties.

## Configure a 10 Gbps interface for Ubuntu/Debian servers

1\. Install the necessary tools: **ethtool**, **net-tools**, and **nano**. Instead of <a href="https://help.ubuntu.com/community/Nano" target="_blank">nano</a>, you can use a text editor of your choice.

```
apt-get install ethtool net-tools nano
```

2\. Check the active interfaces of your server: ```ip```

You will get the similar output where ‘```eth0```’ is the required interface.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12987773655057.png" alt="output " width="80%">

If you are using an older version of Linux, and the ‘**ip’** command is not found, you can try using the ‘```ifconfig```’ command instead. 

3\. Check the settings of the interface:

```
ethtool eth0
```

You will get the similar output:

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12987901207825.png" alt="output " width="60%">

The "Supported link modes" field will list ‘```1000baseT/Full```’, which means the interface supports a maximum speed of 1 Gbps.  

You need to find an interface that would mention ‘```10000baseT/Full```’, which means that the interface supports a speed of 10 Gbps. 

4\. Check other interfaces, including inactive ones:

```
ip link show
```

The output will include the name of each interface and its state (up or down).

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12988067861649.png" alt="output " width="80%">  
If you are using an older version of Linux,and the ‘**ip link show’** command is not found, you can try using the ‘```ifconfig```’ command instead.

5\. Activate inactive interfaces: 

```
ip link set eth1 up  
ip link set eth2 up
```

This will activate the ```eth1``` and ```eth2``` interfaces. If you are using an older version of Linux,and the ‘```ip link set eth1 up```’ command is not found, you can try using the ‘```ifconfig eth1 up```’ command instead.

You can verify that the interface is up by using the following command to view the status of the interface: ```ip```

​​If the interface is up, you will see the line **state UP** in the output. If the interface is down, you will see the line **state DOWN**.

If you are using an older version of Linux, and the ‘```ip```’ command is not found, you can try using the ‘```ifconfig```’ command instead.

6\. Run the following command for each interface until you find the one that supports 10 Gbps.

```
ethtool eth1  
ethtool eth2
```

You will get the similar output:

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12988155718033.png" alt="output " width="60%">

Make sure that **"Link detected**" is "**yes**" and "**Speed**" is "**10000Mb/s**" (10 Gbps).

7\. Change the active interface from 1 Gbps to 10 Gbps in the network configuration file. To edit this file, you can use a text editor of your choice, such as nano. For example: 

```
nano /etc/netplan/*.yaml
```

If you are using an older version of Linux, and the ‘**nano /etc/netplan/\*.yaml’** command is not found, you can try using the ‘```nano /etc/network/interfaces```’ command instead.

In the network configuration file, find every line where **eth0** is mentioned and change it to **eth2**. Note that the **lo** interface doesn't require any changes. 

8\. Save the changes to the file and exit the text editor. You will need to reboot the server for the changes to take effect.

9\. After the reboot, you can use the **ethtool** command to verify that the active interface is set to 10 Gbps.

If you fail to connect, it may indicate that something went wrong. You can use <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/log-in-to-ipmi" target="_blank">IPMI</a> to recover your server or try <a href="https://gcore.com/docs/hosting/virtual-servers/manage/operating-system/install-a-linux-os-from-a-template" target="_blank">reinstalling the OS</a>.

## Configure a 10 Gbps interface for CentOS

1\. Install the necessary tools: **ethtool**, **net-tools**, and **nano**. Instead of **nano**, you can use a text editor of your choice.

```
yum install ethtool net-tools nano
```

2\. Check the active interfaces of your server by running the command: ```ip```

You will get the similar output where **eno1** is the required interface.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12988893619089.png" alt="output " width="80%">

If you are using an older version of Linux, and the ‘**ip’** command is not found, you can try using the ‘```ifconfig```’ command instead.

3\. Check the settings of the interface:

```
ethtool eno1
```

You will get the similar output:

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12988723926417.png" alt="output ">

The **Supported link modes** field will list ‘```1000baseT/Full```’, which means the interface supports a maximum speed of 1 Gbps.  

You need to find an interface that would mention ‘**10000baseT/Full’**, which means that the interface supports a speed of 10 Gbps.

4\. Check other interfaces, including inactive ones:

```
ip link show
```

The output will include the name of each interface and its state (up or down).

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12989145294481.png" alt="output " width="80%">

If you are using an older version of Linux, and the ‘**ip link show’** command is not found, you can try using the ‘```ifconfig```’ command instead.

5\. Activate inactive interfaces: 

```
ip link set eno2 up
```

This will activate the **eno2** interface. If you are using an older version of Linux, and the ‘```ip link set eno2 up```’ command is not found, you can try using the ‘```ifconfig eno2 up```’ command instead.

You can verify that the interface is up by using the following command to view the status of the interface: ```ip```

​​If the interface is up, you will see the line **state UP** in the output. If the interface is down, you will see the line **state DOWN**.

If you are using an older version of Linux, and the ‘```ip```’ command is not found, you can try using the ‘```ifconfig```’ command instead. 

6\. Run the following command for each interface until you find the one that supports 10 Gbps. 

```
ethtool eno2
```

You will get the output:

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/configure-a-10-gbps-network-card/12989201201041.png" alt="output ">  

Make sure that **"Link detected**" is "**yes**" and "**Speed**" is "**10000Mb/s**" (10 Gbps).

7\. Move network settings to the 10 Gbps configuration file (ifcfg-eno2) and disable 1 Gbps (ifcfg-eno1) if you don't need it.

To edit the configuration file, you can use a text editor of your choice, such as nano. For example: 

```
nano /etc/sysconfig/network-scripts/ifcfg-eno1  
nano /etc/sysconfig/network-scripts/ifcfg-eno2
```

8\. Save the changes to the file and exit the text editor. You will need to reboot the server for the changes to take effect.

9\. After the reboot, you can use the ‘**ethtool’** command to verify that the active interface is set to 10 Gbps.

If you fail to connect, it may indicate that something went wrong. You can use <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/log-in-to-ipmi" target="_blank">IPMI</a> to recover your server or try <a href="https://gcore.com/docs/hosting/virtual-servers/manage/operating-system/install-a-linux-os-from-a-template" target="_blank">reinstalling the OS</a>.