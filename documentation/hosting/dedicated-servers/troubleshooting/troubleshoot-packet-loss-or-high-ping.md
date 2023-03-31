---
title: troubleshoot-packet-loss-or-high-ping
displayName: Packet loss or high ping
published: true
toc:
---

If you ping a server, and some of the packets are lost, or they take too much time to return (more than 110 milliseconds), it indicates a network issue.

Please note that this article is for those whose server is available, despite the network issue. If the server does not return any packets at all, please refer to the guide [for the case when a server does not respond to ping](\"https://support.gcorelabs.com/hc/en-us/articles/360000395297\").

1. If you are using a proxy or VPN, disable it and ping again. If it helps, the problem was caused by an intermediate server. Connect without it or consider changing the VPN/proxy.

2. If you have recently changed network settings, return to the previous settings and ping again. If it helps, continue using the old settings which works better.

To return your network settings to the default parameters, reinstall your OS. Refer to the guides:

[Reinstall your OS from our templates](\"https://support.gcorelabs.com/hc/en-us/articles/115003754285\")  
[Reinstall your OS from an ISO image](\"https://support.gcorelabs.com/hc/en-us/articles/115005444989\")

3. If the steps above are not applicable to you, or they don’t help, [contact our technical support](\"https://support.gcorelabs.com/hc/en-us/articles/115003753885\"). Please provide the following information in your message:


*   Whether you are using a VPN/proxy and whether you have changed the network settings. If so, specify whether disabling the VPN/proxy and returning to old settings helped or not.
*   The IP address of your server.
*   The IP address from which your server is being pinged poorly.
*   The country and city where you are located. If you are a reseller and your client is experiencing a network issue, please specify the country and city of your client.
*   The date and time in UTC+0 when the problem occurred.
*   The output of **ping** and **tracert** (Windows) / **ping** and **traceroute** (Linux) / **mtr** (UNIX system) from the client to the server.
*   The output of **ping** and **tracert** (Windows) / **ping** and **traceroute** (Linux) / **mtr** (UNIX system) from the server to the client.


This data will help us understand what happened and allow us to respond to the issue quickly.