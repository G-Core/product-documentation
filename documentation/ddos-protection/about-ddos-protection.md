---
title: about-ddos-protection
displayName: Overview
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
# About DDoS Protection

## How does DDoS Protection work?

DDoS Protection is a service that safeguards your servers and instances from DDoS attacks.

We offer free default DDoS Protection for all our equipment. In the event of an attack, our system blocks the server's IP address, preventing the attacker from continuing their malicious activity. The server is not affected, but it becomes unavailable for several hours.

For advanced DDoS Protection, you can opt for our paid service. During an attack, it redirects traffic to the threat mitigation system (TMS) for traffic filtering and threat detection. The TMS recognizes an attack, removes malicious traffic, and allows only legitimate traffic that won't disrupt the server's operation. You can configure the TMS access control list (ACL) according to your preferences. The main advantage is that a server's IP remains unblocked and available during an attack.

Advanced protection offers two modes: always-on or on-demand.

## Advanced protection modes

With an on-demand mode, traffic passes through the TMS only during an attack. The system needs about a minute to identify a threat and redirect traffic to the TMS. During this first minute, a targeted server will receive attack traffic and then filtered traffic.

With an always-on mode, your traffic passes through the TMS, even when there is no attack. This protection immediately responds to an attack and guarantees that only legitimate traffic will be sent to your server.

<table>
   <tr>
      <td> </td>
      <td>On-demand (Advanced protection)</td>
      <td>Always-on (Advanced protection)</td>
      <td>Basic protection</td>
   </tr>
   <tr>
      <td>Pricing model</td>
      <td>Paid</td>
      <td>Paid</td>
      <td>Free</td>
   </tr>
   <tr>
      <td>Maximum time to recognize an attack</td>
      <td>2 minutes</td>
      <td>5 seconds</td>
      <td>3 minutes</td>
   </tr>
   <tr>
      <td>Attacks it protects from</td>
      <td>• Common amplification attacks<br><br>• IP spoofing attacks<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish connection (L4)</td>
      <td>• Common amplification attacks<br><br>• IP spoofing attacks<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish a connection (L4)<br><br>• Attacks at the application layer (L5-L7)</td>
      <td>• Common amplification attacks<br><br>• IP spoofing attacks</td>
   </tr>
   <tr>
      <td>Protection technology</td>
      <td>1. The attack is detected.<br><br>2. Traffic is redirected to TMS.<br><br>3. TMS filters the traffic.<br><br>4. TMS sends legitimate traffic to the server.</td>
      <td>1. All traffic passes through TMS.<br><br>2. In case of an attack, TMS immediately filters the traffic.<br><br>3. TMS sends legitimate traffic to the server.</td>
      <td>1. Attack is detected.<br><br>2. The attacked IP is blocked for a while.</td>
   </tr>
   <tr>
      <td>Use cases</td>
      <td>• Your server is rarely attacked• Your server is not attacked at the application layer (L7)<br><br>• Your server doesn't host any critical business applications</td>
      <td>• Your server is attacked more than 2-3 times a day• Your server is attacked at the application layer (L7)<br><br>• Your server hosts a critical business application</td>
      <td>• Your server is hardly ever attacked<br><br>• Your server doesn't host any critical business applications</td>
   </tr>
</table>

## DDoS attack statistics

With the real-time DDoS attack statistics feature, you can access a live dashboard that provides a comprehensive overview of ongoing attacks on your protected resources.

You can filter statistics by specific data centers, time intervals, and attack metrics such as bits per second (bps) and packets per second (pps.)

<img src="https://assets.gcore.pro/docs/ddos-protection/ddos-attack-statistics.png" alt="DDoS attack statistics">

## Pricing

 The price for DDoS Protection depends on three factors:

- **OSI layers**. Two options are available: L3-L4 and L3-L7. The first option is cheaper.
- **TMS bandwidth**. The pricing varies based on the TMS's bandwidth to send traffic to your server. Several options are available: 1 Mbit/s, 10 Mbit/s, 100 Mbit/s, 200 Mbit/s, 500 Mbit/s, 1 Gbit/s, 2 Gbit/s,10 Gbit/s. The lower the bandwidth, the lower the price. 
- **Server location**. Prices vary from location to location. Please send a request, and we will advise you on the price for DDoS Protection in a particular data center.

The price does not depend on the mode you choose. But note that always-on mode is available at L3-L7 layers, and on-demand mode is available only at L3-L4.

We can also offer you a plan with custom terms. Let us know what protection parameters you are interested in, and we will be happy to negotiate a custom proposal for you.

