---
title: troubleshoot-a-server-that-is-not-responding-to-ping-requests
displayName: Server is not responding to ping requests
published: true
toc:
---

1. If you can't reach your IP address from China, make sure the IP address is not blocked by the Great Firewall. Use the following services:


*   [PingChinaz](\"http://ping.chinaz.com/\") - shows a connectivity status only in China
*   [ping.pe](\"http://ping.pe/\") - shows a worldwide connectivity status, including China



Please note that due to the Chinese network restrictions, we cannot guarantee the proper functioning of our service in China. The Great Firewall randomly blocks IP addresses, but you may solve this issue by purchasing [additional IP addresses](\"https://support.gcorelabs.com/hc/en-us/articles/115004930545-Additional-IPs-\").


2. Check your network settings.


If you installed your OS from an ISO, set up the network configuration. Otherwise, an IP address won’t be available. To find the required settings, open the control panel, choose your server and click **IP addresses**.


![\"Rectangle_1200-2.png\"](\"https://support.gcore.com/hc/article_attachments/13169768953873\")


Check the IP address, the network mask and the default gateway.


3. If you can’t ping an additional IP address, make sure that [you have configured](\"https://support.gcorelabs.com/hc/en-us/articles/360000233358-How-to-configure-additional-IPs-\") it on your server. To configure an additional IP address, reinstall your OS.