---
title: set-a-gre-tunnel-with-gcore
displayName: Set a GRE tunnel
published: true
order: 20
toc:
pageTitle: Set a GRE tunnel | Gcore
pageDescription: Discover how to set up a GRE tunnel with Gcore on Cisco routers, set MTU and MSS limits, and implement BGP policies for robust DDoS protection.
---
# Set a GRE tunnel with Gcore

The configuration pieces in the guide below are specific to Cisco routers. For information on configuring GRE tunnels and BGP sessions on other devices, refer to the respective documentation provided by the manufacturer.

**Step 1: Check the network availability between two routers that will participate in the tunnel**. Both routers must have routable interfaces connected to the internet, and their routes must be mutually visible and reachable. To verify the connectivity, run either of the following commands on a router platform:

```
show ip route
```

or 

```
show route
```

These commands will display the routing table of the router, showing the IP addresses of their interfaces that will be used as tunnel sources.

**Step 2: Configure a GRE tunnel.** Follow these steps and use the configuration snippets below as a guideline.

1. Set the tunnel ID:

```
interface Tunnel10
```

2. Set the tunnel IP address and subnet mask:

```
ip address 10.20.30.1 255.255.255.0
```

3. Specify the source and destination IP addresses.

```
tunnel source 40.0.0.1
tunnel destination 50.0.0.1
```

The user on the other end of the tunnel sets the similar configuration:

```
interface Tunnel 10
  	ip address 10.20.30.2 255.255.255.0
  	tunnel source 50.0.0.1
  	tunnel destination 40.0.0.1
```

When you configure both ends of the tunnel with matching parameters, the GRE tunnel between two routers will be established.

**Step 3: Set the MTU and MSS limits.** Tunneling adds an extra header to the original IP packet, resulting in overhead. If you don’t adjust MTU and MSS limits, it may lead to packet delivery issues. Set the following MTU and MSS limits:

```
interface Tunnel10
  ip mtu 1476
  ip tcp adjust-mss 1436
```
<expandable-element title="Why these values?">

The standard MTU size allowed on the internet is 1500 bytes. When using GRE, typically an additional 24 bytes are added to the packet, consisting of 20 bytes of additional an outer IP header and 4 bytes of GRE itself. This means we must reduce the maximum allowed packet size over our GRE tunnel to 1476 bytes. Since we do not use any encryption in our example, no more headers are considered. If there was encryption, there would be 4 more bytes, but this is out of the scope of this article.

For TCP, the maximum segment size (MSS) value is 40 bytes less than the MTU size, as the TCP header is 40 bytes. Thus, the MSS value must be explicitly specified in the configuration. In our case, the MSS value must be 1436 bytes (1476 [the GRE MTU size] - 40 = 1436).

</expandable-element>

**Step 4: Configure BGP.** Open a BGP peering session, configure your BGP neighbor by specifying their IP address and number of remote AS, set BGP policies that will determine the best path for routing, and advertise network prefixes.

For example, imagine Side A (AS 10) and Side B (AS 20) on the two ends of the tunnel. Side A provides DDoS protection, so it accepts specific routes from clients, denies the default for the routing security purposes, and does not advertise anything. On the other hand, Side B advertises only its own routes.

Let’s start with the Side A configuration. 

1. Define the neighbor routes:

```
ip prefix DEFAULT_ROUTE seq permit 5 0.0.0.0/0

ip prefix CLIENT_ROUTES seq 5 permit 50.50.1.0/24
ip prefix CLIENT_ROUTES seq 10 permit 50.50.2.0/24
```

Prefix-list lines are responsible for defining routes.

2. Define the inbound route policy: 

```
route-map SIDE_A_POLICY_INBOUND deny 10
  match ip address prefix-list DEFAULT_ROUTE
route-map SIDE_A_POLICY_INBOUND permit 20
  match ip address prefix-list CLIENT_ROUTES
```

The `SIDE_A_POLICY_INBOUND` route policy processes incoming routes. The first line denies the default route, while the second line permits the client routes.

3. Define the outbound route policy:

```
route-map SIDE_A_POLICY_OUTBOUND deny 10
```

The `SIDE_A_POLICY_OUTBOUND` route policy denies all routes coming out of the router.

The route policy configuration on Side B will be similar:

```
ip prefix DEFAULT_ROUTE seq permit 5 0.0.0.0/0

ip prefix CLIENT_ROUTES seq 5 permit 50.50.1.0/24
ip prefix CLIENT_ROUTES seq 10 permit 50.50.2.0/24

route-map SIDE_B_POLICY_OUTBOUND deny 10
  match ip address prefix-list DEFAULT_ROUTE
route-map SIDE_B_POLICY_OUTBOUND permit 20
  match ip address prefix-list CLIENT_ROUTES

route-map SIDE_A_POLICY_INBOUND deny 10
```

The `SIDE_B_POLICY_INBOUND` and `SIDE_B_POLICY_OUTBOUND` route policies describe the routes coming in and going out of the Side B’s router, respectively. Side B doesn’t accept any routes from Side A, and advertises its own routes to Side A without the default route.

The BGP configuration on both ends of the GRE tunnel should be as follows:

Side A:

```
router bgp 10
  neighbor 10.20.30.2 remote-as 20
  neighbor 10.20.30.2 description SIDE_B_ROUTER
  neighbor 10.20.30.2 route-map SIDE_A_POLICY_INBOUND in
  neighbor 10.20.30.2 route-map SIDE_A_POLICY_OUTBOUND out
```

Side B:

```
router bgp 20
  neighbor 10.20.30.1 remote-as 10
  neighbor 10.20.30.1 description SIDE_A_ROUTER
  neighbor 10.20.30.1 route-map SIDE_B_POLICY_INBOUND in
  neighbor 10.20.30.1 route-map SIDE_B_POLICY_OUTBOUND out
```

The configuration lines provided above enable you to establish BGP sessions with Gcore over GRE tunnels to protect your applications and servers from DDoS attacks and other types of malicious traffic.