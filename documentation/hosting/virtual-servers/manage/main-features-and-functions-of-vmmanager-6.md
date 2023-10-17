---
title: main-features-and-functions-of-vmmanager-6
displayName: VMmanager 6
published: true
order: 5
toc:
--1--What is VMmanager 6?: "what-is-vmmanager-6"
--1--Available actions: "what-can-you-do-with-vmmanager-6"
--1--Key features: "key-features-of-vmmanager-6"
--1--Navigation: "navigation-in-the-vmmanager-6"
pageTitle: Features and functions of VMmanager 6 | Gcore
pageDescription: Explore the features of VMmanager 6 to efficiently manage virtual servers. Perform key actions like OS reinstallation, script running, and more.
---
# Features and functions of VMmanager 6

## What is VMmanager 6?

VMmanager 6 is a control panel with a user-friendly interface that enables users to manage their virtual private servers efficiently.

## What can you do with VMmanager 6?

Here are some key actions you can perform via VMmanager6:

- Start/stop your server. 

**Note**: In VMmanager 6, it is not possible to fully shut down a server due to billing restrictions. If you attempt to turn it off, the server will automatically be turned on again shortly.

- Restart your server.

- Reinstall an OS. 

**Note**: In VMmanager 6, you can reinstall your OS using scripts.

- Start/stop the recovery mode. To read more about the recovery mode, refer to the "<a href="https://gcore.com/docs/hosting/virtual-servers/manage/main-features-and-functions-of-vmmanager-6#key-features-of-vmmanager-6">Key features</a>" section below.

- Mount an ISO image.

**Note**: In VMmanager 6, you can upload an ISO image only using a URL. It will mount to your server immediately and initiate an automatic reboot.

- Change the password for your server.

- Manage disks, including backup disks.

- Connect to the server desktop via VNC. 

**Note**: In VMmanager 6, VNC is only available to use via VMmanager.

- Run a script. For more information about scripts, refer to the "<a href="https://gcore.com/docs/hosting/virtual-servers/manage/main-features-and-functions-of-vmmanager-6#key-features-of-vmmanager-6">Key features</a>" section below. 

- See the statistics of your server.

- Add notes to a virtual machine.

## Key Features of VMmanager 6

Here are some of the distinctive features that set VMmanager 6 apart from alternative options:

1. **Password**. For improved security, the password for the VMmanager 6 panel is sent only once in the server activation email after buying your first server in a location. The passwords for all later servers will remain the same as the one provided in that initial email.

2. **Faster deployment time**. In VMmanager 6, servers are created in 2–5 minutes.

3. **Recovery mode**. For VM maintenance, diagnostics, and troubleshooting, you can use a special operating system called SystemRescueCD. To use it, you typically need to create a bootable media (e.g., CD, USB drive) using the provided ISO image. You can then boot your computer from the media to access the SystemRescueCD environment. For more information, refer to the <a href="https://system-rescue-cd.org/manual" target="_blank">SystemRescueCD official documentation</a>.

4. **Scripts**. In VMmanager 6, you can use scripts to set up virtual machines automatically: install software applications, modify configuration files, and perform other operations. You can use the default scripts or create your own. On a Linux OS, you can run Shell scripts written in bash, and on a Windows OS, you can run Powershell scripts.

5. **Automatic configuration of additional IP addresses**. In previous VMmanager iterations, you had to manually configure additional IP addresses, but with VMmanager 6 there’s no need to do so.

6. **Private VNC**. In VMmanager 6, the connection over VNC is accessible only from VMmanager.

7. **IPv6 subnet**. When creating a server, you will be allocated an IPv6 subnet from which you can select your own IP.

## Navigation in the VMmanager 6

The VMmanager's UI simplifies navigation to essential options. 

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/vmmanager-6/1-navigation.jpg" alt="Navigation in the VMmanager 6"> 

In the screenshot above, we've labeled the following numbers for reference:

1 – **Virtual machines**: View server info: name, ID, characteristics, current load, domain, OS, cluster type and uptime

2 – **Virtual networks**: Not available

3 – **Scripts**: View the default scripts and create your custom ones

4 – **VNC**: Connect to your server via VNC

5 – **VM parameters**: View information, statistics, IP addresses, interfaces, logs, tasks, VNC settings

6 – **Menu**: Stop, restart, reinstall an OS, start or stop the recovery mode, mount an ISO image, connect to your server via VNC, change the password, run scripts, add notes
