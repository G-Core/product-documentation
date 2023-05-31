---
title: about-server-protection
displayName: Overview
published: true
order: 10
toc:
   --1--How it works: "how-it-works"
   --1--Advanced protection modes: "advanced-protection-modes"
   --1--Pricing: "pricing"
---
# About Server Protection

## How it works

Server Protection is a service that protects your servers and instances from DDoS attacks.

Server Protection (free) is provided for all our equipment by default. In case of an attack, our system blocks the server's IP. So, an attacker cannot continue the attack. The server is not affected, but it becomes unavailable for several hours.

You can order advanced (paid) Server Protection. During an attack, it redirects traffic to the threat mitigation system (TMS), that helps to filter traffic and detect threats. This system recognizes an attack, removes attack traffic, and enables only legitimate traffic that won't impact the server's operation. You can configure the ACL (access control list) for TMS by yourself. The main advantage is that a server's IP is not blocked during an attack, and the server remains available.

Advanced protection can operate in one of two modes: always-on or on-demand.

## Advanced protection modes

With on-demand mode, traffic passes through the TMS only during an attack. The system needs about a minute to identify a threat and redirect traffic to the TMS. During this first minute, a targeted server will receive attack traffic, and then filtered one.

With always-on mode, your traffic passes through the TMS all the time, even when there is no attack. This protection provides immediate response to an attack and guarantees that only legitimate traffic will be sent to your server.


|                                         |  Advanced protection                                                                                                                                         | Basic protection                                                                                                                                                                                  |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| On-demand                           | Always-on                                                                                                                                                        |
| Pricing                             | Paid                                                                                                                                                         | Paid                                                                                                                                                                                              | Free                                                                                                       |
| Attack detection time(maximum)      | 2 minutes                                                                                                                                                  | 5 seconds                                                                                                                                                                                   | 3 minutes                                                                                            |
| Types of attacks to be prevented  | • Common amplification attacks<br><br>• IP spoofing attacks<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish connection (L4)            | • Common amplification attacks<br><br>• IP spoofing attacks<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish a connection (L4)<br><br>• Attacks at the application layer (L5-L7) | • Common amplification attacks• IP spoofing attacks                                                  |
| Protection technology               | 1. Attack is detected.<br><br>2. Traffic is redirected to TMS.<br><br>3. TMS filters the traffic.<br><br>4. TMS sends legitimate traffic to the server.                        | 1. All traffic passes through TMS.<br><br>2. In case of attack, TMS immediately filters the traffic.<br><br>3. TMS sends legitimate traffic to the server.                                              | 1. Attack is detected.<br><br>2. The attacked IP is blocked for a while.                                 |
| When it is suitable for you       | • Your server is rarely attacked• Your server is not attacked at the application layer (L7)<br><br>• Your server doesn't host any critical business applications | • Your server is attacked more than 2-3 times a day• Your server is attacked at the application layer (L7)<br><br>• Your server hosts a critical business application                           | • Your server is hardly ever attacked<br><br>• Your server doesn't host any critical business applications |

## Pricing

 The price of a Server Protection depends on three things:

- OSI layers to be protected. Two options are available: L3-L4 and L3-L7. The first option is cheaper.
- Bandwidth used by the TMS to send traffic to a server**.** Several options are available: 1 Mbit/s, 10 Mbit/s, 100 Mbit/s, 200 Mbit/s, 500 Mbit/s, 1 Gbit/s, 2 Gbit/s,10 Gbit/s. The lower the bandwidth, the cheaper the price. 
- Server location. Prices vary from location to location. Please send a request, and we will advise you the price for Server Protection in a particular data center. 

The price does not depend on a mode you choose. But note that always-on mode is available at L3-L7 layers, and on-demand mode is available only at L3-L4.

We can also offer you a plan with custom terms. Tell us what protection parameters you are interested in, and we will be happy to negotiate a custom proposal for you.

