---
title: about-gcore-ddos-protection-for-dedicated-servers
displayName: Overview
published: true
order: 10
toc:
   --1--How it works: "how-it-works"
   --1--Advanced protection modes: "advanced-protection-modes"
   --1--Billing: "billing"
pageTitle: DDoS Protection for dedicated servers | Gcore
pageDescription: Discover Gcore DDoS Protection for dedicated servers. Choose between Basic (free) and Advanced (paid) Protection.
---
# About Gcore DDoS Protection for dedicated servers

## How it works
DDoS Protection is a service that protects dedicated servers from DDoS attacks.

Basic (free) Protection is set up on all of our equipment by default. When a server is attacked, the system blocks its IP, so the attacker cannot continue the attack. The server does not suffer, but it becomes unavailable for several hours.

You can order advanced (paid) Protection. It redirects traffic to TMS (threat mitigation system — a system for cleaning traffic and detecting threats) during an attack. This device detects an attack, cleans up the traffic, and sends to the server only data that will not harm it. You can set the ACL (access control list) for TMS. The main advantage is that IP is not blocked during an attack, and the server remains available.

Advanced protection can operate in one of two modes: always-on or on-demand.

## Advanced protection modes

With on-demand, traffic passes through the TMS only during an attack. The system needs about a minute to identify the threat and start redirecting traffic to the TMS. The server will receive "dirty" traffic during that time and cleaned traffic — after.

With always-on, your traffic passes through the TMS all the time, even when there is no attack. With this protection mode, the response to the attack will be instant, and the server will be guaranteed to receive only clean traffic.


|                                                     | Improved protection                                                                                                                                            | Basic protection                                                                                                                                                                                               |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| On-demand                                       | Always-on                                                                                                                                                          |
| Payment                                             | Paid                                                                                                                                                           | Paid                                                                                                                                                                                                           | Free                                                                                               |
| How soon it recognizes an attack (maximum time) | 2 minutes                                                                                                                                                    | 5 second                                                                                                                                                                                                 | 3 minutes                                                                                    |
| What attacks it protects from                       | • Standard amplification attacks<br><br>• Attacks from fake IP addresses<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish a connection (L4) | • Standard amplification attacks<br><br>• Attacks from fake IP addresses<br><br>• Attacks using flows or volumetric attacks (L3)<br><br>• Attacks to establish a connection (L4)<br><br>• Attacks at the application layer (L5-L7) | • Standard amplification attacks<br><br>• Attacks from fake IP addresses                             |
| Protection mechanism                            | 1. Attack detected<br><br>2. Traffic is redirected to TMS<br><br>3. TMS cleans up traffic<br><br>4. TMS sends cleaned traffic to the server                                      | 1. All traffic passes through TMS2. When attacked, TMS immediately cleans up the traffic3. TMS sends cleaned traffic to the server                                                                   | 1. Attack detected<br><br>2. The attacked IP is blocked for a while                              |
| What cases it is suitable for                       | • You are rarely attacked<br><br>• You are not attacked at the application layer (L7)<br><br>• The server does not host a critical business application                    | • You are attacked from 2 to 3 times a day<br><br>• You are attacked at the application layer (L7)<br><br>• The server hosts a critical business application                                                           | • You are practically not attacked• The server does not host a critical business application |

## Billing

 The price of DDoS Protection service depends on three things:

- OSI layers to be protected. Two ranges are available: L3-L4 and L3-L 7, the first option is cheaper.   
- The bandwidth that will be used by TMS to send traffic to the server**.** Several options are available: 1 Mbps, 10 Mbps, 100 Mbps, 200 Mbps, 500 Mbps, 1 Gbps, 2 Gbps, 10 Gbps. The lower the bandwidth is, the cheaper the tariff is.
- The region where the server is located. Prices vary from location to location, please send a request for service, and we will tell you the price of DDoS Protection in a particular data center.

The price does not depend on the choice of on-demand or always-on protection mode but remember: always-on is available at L3-L7 protection layers, and on-demand is available only at L3-L4.

We are also considering the possibility of providing a tariff with individual conditions: describe protection parameters you are interested in, and we will be happy to discuss an individual offer for you.
