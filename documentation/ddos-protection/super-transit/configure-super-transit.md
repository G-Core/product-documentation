---
title: configure-super-transit
displayName: Configure infrastructure for Super Transit
published: true
order: 10
toc:
pageTitle: Set up infrastructure for Super Transit | Gcore
pageDescription: Learn how to prepare and configure your network infrastructure to use the Super Transit feature effectively.
---
# Configure your infrastructure for Super Transit

Super Transit protects on-premises, hybrid, and cloud-based networks from DDoS attacks while optimizing network performance by accelerating traffic delivery. This feature is available to all <a href="https://gcore.com/ddos-protection">Gcore DDoS Protection</a> customers.

To enable Super Transit, follow the configuration steps outlined below.

## Step 1. Provide information about your network infrastructure

To properly configure DDoS protection and traffic routing, we need details about your network setup and traffic patterns. Complete and submit the DDoS Protection questionnaire as described in our guide on <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection">activating DDoS protection</a>.

## Step 2. Verify router compatibility

For Super Transit to function optimally, the routers at your tunnel endpoints must meet the following specifications:
* **Support anycast tunneling** to efficiently route traffic from Gcore’s  network to your origin
* **Allow configuration of multiple tunnels** per internet service provider (ISP)
* **Support maximum segment size (MSS) clamping** to prevent fragmentation of larger packets and optimize data transmission through the tunnel

## Step 3. Verify IRR entries

<alert-element type="info" title="Info">
If you are using an IP address provided by Gcore, you can skip this step.
</alert-element>

Your <a href="https://irr.net/" target="_blank">Internet Routing Registry</a> (IRR) entries must match the corresponding origin <a href="https://en.wikipedia.org/wiki/Autonomous_system_(Internet)" target="_blank">autonomous system numbers (ASNs)</a>. This ensures accurate and secure traffic routing.

To verify the authenticity of your IP address prefixes, use Resource Public Key Infrastructure (RPKI), a security framework that cryptographically links route prefixes to an autonomous system. This validation ensures routing information integrity before passing data to your routers.

To check your prefixes, use any RPKI validation tool or a validation portal provided by your ISP.

## Step 4. Set maximum segment size (MSS)

Since Super Transit encapsulates original data packets with additional headers, these headers increase packet size. To prevent fragmentation, adjust the Maximum Transmission Unit (MTU) and Maximum Segment Size (MSS) settings accordingly.

Recommended MSS clamping settings:
- **GRE tunnels handling off-ramp traffic:** Set TCP MSS to 1432 bytes.
- **Clearing the "Don’t Fragment" (DF) bit:** If you cannot set MSS below 1500 bytes, clearing the DF flag in the IP header allows larger packets to be fragmented and reassembled after decapsulation. In most environments, this does not significantly impact traffic throughput.

## Step 5. Adjust MSS values for a router

This configuration depends on the actual provider of your router. Here are the instructions for some common network providers:
* <a href="https://www.cisco.com/en/US/docs/ios-xml/ios/ipapp/command/ip_tcp_adjust-mss_through_ip_wccp_web-cache_accelerated.html#GUID-68044D35-A53E-42C1-A7AB-9236333DA8C4" target="_blank">Cisco</a>
* <a href="https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/tcp-mss-edit-system.html" target="_blank">Juniper</a>

## Step 6. Configure tunnels

To establish a secure connection between Gcore’s network and your infrastructure, configure tunnels on both the Gcore side and your router. Follow the instructions in the <a href="https://gcore.com/docs/ddos-protection/gre-tunneling/set-a-gre-tunnel-with-gcore">Set Up a GRE Tunnel with Gcore</a> guide.

## Step 7. Advertise prefixes

After submitting your <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection#ddos-questionnaire">DDoS Protection Questionnaire</a>, we will process and announce your prefixes through the Gcore network using Border Gateway Protocol (BGP). Once completed, all incoming traffic will be routed through Super Transit for DDoS protection before reaching your infrastructure.
