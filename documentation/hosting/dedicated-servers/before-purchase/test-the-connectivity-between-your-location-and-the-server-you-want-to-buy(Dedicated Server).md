---
title: test-the-connectivity-between-your-location-and-the-server-you-want-to-buy
displayName: Test network performance
order: 10
published: true
toc:
---

If you wish to test connectivity between your IP and one of our static nodes, you can use our [Looking Glass](\"http://lg.gcorelabs.com/\"). How to test connectivity:


1. Choose a location in the drop-down list


![\"______________2019-01-31___23.49.31.png\"](\"https://support.gcore.com/hc/article_attachments/360001814338/______________2019-01-31___23.49.31.png\")


2. Choose Internet protocol version IPv4 or IPv6


3. Choose a command for testing.


![\"______________2019-01-31___23.52.35.png\"](\"https://support.gcore.com/hc/article_attachments/360001814378/______________2019-01-31___23.52.35.png\")


*

    **ping** – shows time which needs to transfer data packet from your IP address to the server;
 
*

    **traceroute** – transfers data packet from the server to your IP address and shows information about all transitional routers which data packet passes through when it goes to the destination node;
    
*

    **route for all** – shows two best bgp-routes for each location;
    
*

    **route for** **(bgpmap)** – shows information about which AS (autonomous systems) the data packet have to pass for achieve destination network.


4. Write your IPv4 or IPv6 address and start the test.


Please, note the platform takes some time to process your request as it depends on what location you chose.


In the results of your request you can see information about providers, owners of the IP-addresses and ASes.


![\"______________2019-01-31___23.44.28.png\"](\"https://support.gcore.com/hc/article_attachments/360001731397/______________2019-01-31___23.44.28.png\")