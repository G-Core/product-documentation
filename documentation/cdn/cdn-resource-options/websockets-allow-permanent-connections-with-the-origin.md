---
title: websockets-allow-permanent-connections-with-the-origin
displayName: WebSockets
published: true
order: 80
toc:
   --1--What is WebSocket?: "what-is-websocket"
   --1--How it differs from HTTP: "how-is-websocket-different-from-http"
   --1--Manage the feature: "manage-the-websockets-feature"
---
  
  

What is WebSocket?
------------------

WebSocket is a connection protocol based on TCP. It is designed to transfer data between a client (e.g., a browser) and a server over a persistent TCP connection. A persistent connection only needs to be established once, and then data can be transmitted without breaking the connection or making additional requests. Such connections continue until one of the participants terminates it.

WebSocket is suitable for services that require constant data exchange, such as chat rooms, online games, real-time trading platforms, etc. For static or slowly updated data on a website (e.g., in a blog or product catalog), WebSocket connections could be more optimal. To receive updates, the client only needs to reload the page manually.

How is WebSocket different from HTTP?
-------------------------------------

1\. WebSocket protocol is bidirectional, which means that clients and servers can send data to each other anytime during the connection. HTTP protocol is unidirectional, as the server sends data only when it receives the client's request. With WebSocket, you can leave a page with a chat or social network open and receive messages when they are sent. If HTTP were used, you would have to refresh the page every time to see if a message arrived.

2\. WebSocket establishes one connection and keeps it open permanently. HTTP establishes a new connection every time the client makes a request and breaks it after the server responds.

<img src="https://assets.gcore.pro/blog/how-to-speed-up-dynamic-content-delivery-using-cdn/4.png" alt="The difference between content delivery without and with WebSocket">

Manage the WebSockets feature
-----------------------------

By default, the WebSocket feature is enabled for [CDN resources created for the entire site](https://www.gcore.com/support/articles/4410067902737/) and disabled for [CDN resources created for only static assets](https://gcore.com/support/articles/213969429/). You can manage this feature depending on your concerns: disable it for the CDN resources with full integration or enable it for resources with partial integration.

To manage the WebSocket feature:

1\. Go to the [CDN](https://cdn.gcore.com/resources/list) section in the control panel and open the settings of the resource for which you want to manage WebSockets by clicking its custom domain.

<img src="https://support.gcore.com/hc/article_attachments/13167645190929" alt="mceclip0.png">The new page opens. Do the remaining steps on it.

<img src="https://support.gcore.com/hc/article_attachments/13167716346385" alt="mceclip1.png">

2\. Open the "Content" section and click **Websockets**.

3\. Enable or disable the feature.

4\. Save changes.