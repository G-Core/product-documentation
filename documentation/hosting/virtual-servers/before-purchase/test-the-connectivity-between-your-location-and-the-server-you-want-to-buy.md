---
title: test-the-connectivity-between-your-location-and-the-server-you-want-to-buy
displayName: Test network performance
published: true
order: 20
toc:
pageTitle: Test the connectivity | Gcore
pageDescription: Learn how to test the connectivity between your location and the desired server before purchase using the Looking Glass tool.
---
# Test the connectivity between your location and the server you want to buy


To test the connectivity between your IP address and one of our static nodes, you can use our <a href="https://lg.gcore.lu" target="_blank">Looking Glass</a> tool.

1\. In the **Nodes**, choose the location of the server from the drop-down list.

2\. In **Protocols**, select a version of Internet protocol: IPv4 or IPv6.

3\. In **Command**, select a command for testing:

- "**ping**" shows the time needed to transfer a data packet from your IP address to the server.
- "**traceroute**" transfers a data packet from the server to your IP address and shows information about all transitional routers the data packet passes through to reach the destination node.
- "**show route for all**" shows two best BGP routes for each location.
- "**show route for (bgpmap)**" shows information about autonomous systems (AS) the data packet has to pass to reach the destination network.

4\. Enter your IPv4 or IPv6 address and start the test.

Please note the tool may take some time to process your request, depending on the location you chose.

In the results of your request, you can see information about providers, owners of the IP addresses, and ASes.