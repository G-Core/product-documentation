---
title: difference-between-virtual-floating-and-reserved-ip-addresses
displayName: Difference between virtual, floating, and reserved IP addresses
published: true
order: 40
toc:
---
 

|           | \nVirtual IP (VIP)\n                                                                                                                                                                                                                                  | Floating IP                                                                                                                                                                                                                                             | \nReserved IP\n                                                                        |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Use cases | \n• Assign to several instances at once to create a fault-tolerant infrastructure (if the main machine is not available the VIP will go to the backup one, and it will respond to requests).\n• Make it a second address for the network interface.\n | • Rapidly organize access from the Internet to an instance created only in a private subnet (that is, it has no public network interface). After assigning a floating IP to the machine it will be possible to connect to it from the external network. | \n• Assign to an instance or a load balancer at any time.\n• Convert to a VIP.\n \n \n |
| Subnet    | Public or private                                                                                                                                                                                                                                     | Private                                                                                                                                                                                                                                                 | \nPublic or private\n                                                                  |


Read more about IP of each type in the articles:

[Floating IP: what it is, what it is used for, how to get it and assign to instance](https://gcorelabs.com/support/articles/360013333757/)  
[Virtual IP (VIP): what it is, what it is used for, how to get it and assign to instance](https://gcorelabs.com/support/articles/4405866963345/)  
[Reserved IP: what it is, what it is used for, how to get it and assign to instance or balancer](https://gcorelabs.com/support/articles/4405927368721/)
