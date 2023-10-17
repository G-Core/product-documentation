---
title: about-gcore-ddos-protection-with-gre-tunneling-and-bgp-routing
displayName: Overview
published: true
order: 10
toc:
   --1--What is the GRE protocol?: "what-is-the-gre-protocol"
   --1--GRE header and network requirements: "gre-header-and-network-requirements"
   --1--What is the BGP protocol?: "what-is-the-bgp-protocol"
   --1--How do GRE and BGP work together?: "how-do-gre-and-bgp-work-together"
   --1--How does Gcore protect from DDoS attacks using GRE: "how-does-gcore-protect-from-ddos-attacks-using-gre"
   --1--Use cases: "use-cases"
pageTitle: About DDoS Protection with GRE and BGP | Gcore
pageDescription: Protect networks globally against DDoS attacks with Gcore's GRE tunneling & BGP routing. 
---
# About Gcore’s DDoS Protection with GRE Tunneling and BGP Routing

Gcore provides a comprehensive solution designed to protect network infrastructure from DDoS attacks, regardless of their location worldwide. The approach is based on GRE tunneling and BGP routing. In this article, we explore the solution explanation and the key concepts involved.

## What is the GRE protocol?

<a href="https://gcore.com/blog/gre-tunneling-for-server-protection/" target="_blank">Generic Routing Encapsulation</a>, or GRE, is a tunneling protocol that creates a virtual point-to-point connection between two endpoints over an IP network. The endpoints are usually routers or firewalls that are assigned IP addresses when connected with a GRE tunnel. Much like a real-life tunnel, a GRE tunnel acts as a pathway for data to travel from point A to point B.

<img src="https://assets.gcore.pro/docs/ddos-protection/gre-tunneling/overview/1-gre-tunnel.jpg" alt="What is the GRE protocol">

Here’s how it works: The router at the source location encapsulates the data packages: it wraps a GRE packet around the original packet so that the original packet becomes a payload of the GRE packet. The GRE header is added to the packet, indicating the destination and the protocol of the packet inside.

As a GRE packet travels over the Internet, intermediate routers route the packet to its destination. Finally, the packet reaches its destination endpoint and the router decapsulates the GRE header to retrieve the original data.

## GRE header and network requirements

The GRE protocol adds an additional header to data packets, increasing the overall packet size. You should factor in this size increase before establishing a tunnel. 

MTU (maximum transmission unit) refers to the maximum size of a data packet that can be transmitted without fragmentation, while MSS (maximum segment size) refers to the maximum amount of TCP packet payload. When extra GRE bytes are added to the packet size, it can exceed the standard MTU and MSS limits, resulting in packet fragmentation. Fragmentation slows down delivery, increases resource usage, and may lead to packet drops. This can be avoided by reconfiguring MTU and MSS limits to accommodate GRE headers.

## What is the BGP protocol?

BGP, which stands for Border Gateway Protocol, is a routing protocol which provides information about all available data transmission paths between multiple autonomous systems that form the internet.

Imagine the internet as a big interconnected network of cities, where each city is a network or an autonomous system (AS) with its unique address or IP prefix (range of IP addresses.) The roads between the cities are like the network links between different ASs. BGP routers in each city act as the GPS navigation system. They exchange routing information with neighboring cities (ASs) to determine the best routes for data to reach its destination. This routing information includes the available paths (highways/roads) and the associated metrics (e.g., link cost or traffic conditions.) Routing information can change in real-time due to network changes, link failures, or network administrators’ policy adjustments. BGP routers continuously exchange updates with neighboring routers to reflect these changes, ensuring that traffic is directed along the most optimal and reliable paths.

For more information about BGP, please refer to our <a href="https://gcore.com/learning/what-is-bgp/" target="_blank">blog article</a>.

## How do GRE and BGP work together?

When building a GRE tunnel, you have to specify the address of the endpoint located at the other end of the tunnel. But the address specification is bidirectional: the recipient on the other end of the tunnel should also specify your address. This ensures that both endpoints know where to send and receive encapsulated packets. This is when BGP comes into play.

Similarly to the real-world analogy, where GPS can help you understand the exact location of two cities that you want to connect with a tunnel, BGP will provide users with the information about each other. So when they access the BGP table, both of them can see the user on the other end of the tunnel, and they can set a GRE tunnel.

## How does Gcore protect from DDoS attacks using GRE?

You send [us a request](mailto:sales@gcore.com) and share the details of the internal networks you want to protect from DDoS attacks. Gcore configures its incoming filters to allow traffic originating from your internal networks. After BGP routing is configured, Gcore announces your networks on the internet. This means that everyone on the internet can see that your networks are now being routed through Gcore. All traffic to your networks is redirected to Gcore’s scrubbing center. 

Here, the incoming traffic undergoes thorough filtering and analysis to detect and delete any malicious traffic. The legitimate traffic is encapsulated within GRE packets and sent to your network through the GRE tunnel. Your router decapsulates the GRE packets, examines the routing information, and forwards the data packets to the appropriate servers or devices within your network that host the requested services.

## Use cases

If you have multiple routes within your networks, and you want to protect these networks from DDoS attacks, GRE tunneling will help to safeguard your networks and isolate critical infrastructure from the rest of the internet. Our scrubbing center will act as the last intermediate hop, filtering the incoming traffic before it reaches your servers.

To set up a GRE tunnel with the Gcore scrubbing center, please refer to <a href="https://gcore.com/docs/ddos-protection/gre-tunneling/set-a-gre-tunnel-with-gcore" target="_blank">our step-by-step guide</a>.

