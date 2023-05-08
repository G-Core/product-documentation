---
title: troubleshoot-a-server-that-is-not-responding-to-ping-requests
displayName: Server that is not responding to ping requests
published: true
order: 10
toc:
---
# Troubleshoot a server that is not responding to ping requests

1\. If you can't reach your IP address from China, make sure the IP address is not blocked by the Great Firewall. Use the following services:

- <a href="http://ping.chinaz.com/" target="_blank">PingChinaz</a> - the tool shows a connectivity status only in China
- <a href="http://ping.pe/" target="_blank">ping.pe</a> - the tool shows a worldwide connectivity status, including China

Please note that due to the Chinese network restrictions, we cannot guarantee the proper functioning of our service in China. The Great Firewall randomly blocks IP addresses, but you may solve this issue by purchasing <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/networking/additional-ip-addreses/buy-an-additional-ip-address" target="_blank">additional IP addresses</a>.

2\. Check your network settings.

If you have installed your OS from an ISO, you need to set up the network configuration. Otherwise, an IP address won’t be available. To find the required settings, open the control panel, choose your server and click **IP addresses**.

<img src="https://support.gcore.com/hc/article_attachments/13169671371153" alt="" width="70%">

Check the IP address, the network mask and the default gateway.

3\. If you can’t ping an additional IP address, make sure that <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/networking/additional-ip-addreses/configure-an-additional-ip-address" target="_blank">you have configured</a> it on your server. To configure an additional IP address, reinstall your OS.