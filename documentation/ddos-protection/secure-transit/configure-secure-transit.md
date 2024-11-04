---
title: configure-secure-transit
displayName: Configure infrastructure for Secure Transit
published: true
order: 10
toc:
   --1--How does it work?: "how-does-ddos-protection-work"
   --1--Advanced protection modes: "advanced-protection-modes"
   --1--DDoS attack statistics: ddos-attack-statistics
   --1--Pricing: "pricing"
pageTitle: About DDoS Protection | Gcore
pageDescription: Learn how DDoS Protection safeguards your servers, explore use cases for different protection modes and select the best option for your needs.
---
# Configure your infrastructure for Secure Transit 

Secure Transit protects your on-premise, hybrid, and cloud-hosted networks from DDoS attacks and maximizes network performance by accelerating traffic.  

This feature is available to every Gcore customer using the <a href="https://gcore.com/ddos-protection" target="_blank">DDoS protection</a> product. To start using Secure Transit, adjust your network settings as described in the following steps. 

All you need to do is make sure that your network settings are properly configured. The following steps will help you to do so. 

## Step 1. Provide information about your network infrastructure  

To correctly configure the DDoS protection for your site, we need to get the information about your network setup and traffic patterns. Complete and send us the DDoS protection questionnaire as explained in the following guide: <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection" target="_blank">Activate DDoS protection</a>.

## Step 2. Verify your router compatibility 

To ensure secure and efficient transmission of data packets through our anycast tunnels, the routers at your tunnel endpoints must support the following specifications: 

* Support anycast tunneling to efficiently route traffic from Gcore’s  network to your origin. 
* Allow configuration of multiple tunnels per internet service provider (ISP). 
* Support maximum segment size (MSS) clamping to prevent fragmentation of larger packets and optimize data transmission through the tunnel. 

## Step 3. Verify IRR entries

<alert-element type="info" title="Info">
 
If you are using an IP address provided by Gcore, you can skip this step. 
 
</alert-element>

Your <a href="https://irr.net/" target="_blank">Internet Routing Registry</a> (IRR) entries must match the corresponding origin <a href="https://en.wikipedia.org/wiki/Autonomous_system_(Internet)" target="_blank">autonomous system numbers (ASNs)</a>. This is necessary for establishing accurate and secure traffic routing. 

To verify the authenticity of your IP address prefixes, use the Resource Public Key Infrastructure (RPKI). It’s a security framework that links route prefixes to an autonomous system via cryptographic verification, which validates that the routing infomation is correct before it’s passed to your routers.  

To check your prefixes, use any available RPKI validation tool or portal available through your service provider. 

## Step 4. Set maximum segment size (MSS) 

When sending your original data packets across the network, we encapsulate those packets with additional headers. These headers increase the overall size of each data packet, so you need to add extra space when configuring the maximum transmission unit (MTU) and maximum segment size (MSS) values for your network. 

Recommended MSS clamping settings:

* **GRE tunnels for off-ramp traffic**. The TCP maximum segment size (MSS) is 1432 bytes. 

* **Clear the "Do Not Fragment" bit**. If can’t set the MSS to less than 1500 bytes, you can clear the "Don’t fragment" (DF) flag in the IP header. When this option is enabled, packets larger than 1500 bytes will be fragmented and reassembled after decapsulation. In most environments, it won’t have significant impact on traffic throughput. 

## Step 5. Adjust MSS values for a router 

This configuration depends on the actual provider of your router. Here are the instructions for some common network providers: 

* <a href="https://www.cisco.com/en/US/docs/ios-xml/ios/ipapp/command/ip_tcp_adjust-mss_through_ip_wccp_web-cache_accelerated.html#GUID-68044D35-A53E-42C1-A7AB-9236333DA8C4" target="_blank">Cisco</a>
* <a href="https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/tcp-mss-edit-system.html" target="_blank">Juniper</a> 

## Step 6. Configure tunnels 

Configure the tunnels on the Gcore side and your router side to connect to your origin infrastructure. Refer to the <a href="https://gcore.com/docs/ddos-protection/gre-tunneling/set-a-gre-tunnel-with-gcore" target="_blank">Set a GRE tunnel with Gcore</a> guide for details.

## Step 7. Advertise prefixes 

After we check and process your <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection#ddos-questionnaire" target="_blank">DDoS questionnaire</a>, we'll announce your prefixes through the Gcore network using Border Gateway Protocol (BGP). Once it’s done, all incoming traffic will be routed through Secure Transit for DDoS protection and then forwarded to your infrastructure. 

