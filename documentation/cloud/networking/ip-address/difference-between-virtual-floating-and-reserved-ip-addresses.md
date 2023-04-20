---
title: difference-between-virtual-floating-and-reserved-ip-addresses
displayName: Difference between virtual, floating, and reserved IP addresses
published: true
order: 40
toc:
---
# Difference between virtual, floating and reserved IP addresses

|           | Virtual IP (VIP)                                                                                                                                                                                                                                  | Floating IP                                                                                                                                                                                                                                             | Reserved IP                                                                        |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Use cases | • Assign to several instances at once to create a fault-tolerant infrastructure. • Make it a secondary address for the network interface | • Rapidly organize access from the Internet to an instance in a private subnet. After assigning a floating IP to the machine it will be possible to connect to it from the external network. | • Assign to an instance or a load balancer at any time. • Convert to a VIP.   |
| Subnet    | Public or private                                                                                                                                                                                                                                     | Private                                                                                                                                                                                                                                                 | Public or private                                                                  |


Read more about IP of each type in the articles:

<a href=“https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address” target="_blank">Create and configure a floating IP address</a> 


 <a href=“https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address” target="_blank">Create and configure a virtual IP address</a> 

<a href=“https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address” target="_blank">Create and configure a reserved IP address</a>