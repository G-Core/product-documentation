---
title: difference-between-virtual-floating-and-reserved-ip-addresses
displayName: Difference between virtual, floating, and reserved IP addresses
published: true
order: 40
toc:
pageTitle: Types of IP addresses| Gcore
pageDescription: Understand the differences between virtual, floating, and reserved IP addresses.
---
# Difference between virtual, floating and reserved IP addresses

<table>
  <tr>
    <td>Type of an IP address</td>
    <td>Virtual</td>
    <td>Floating</td>
    <td>Reserved</td>
  </tr>
  <tr>
    <td>Use cases</td>
    <td>• Assigning to several instances at once to create a fault-tolerant infrastructure.
    • Using as a secondary address for the network interface</td>
    <td>• Providing access from the Internet to an instance in a private subnet. After assigning a floating IP to the machine, it will be accessible from the external network.</td>
    <td>• Assigning to an instance or a load balancer at any time. 
    • Converting to a VIP.</td>
  </tr>
  <tr>
    <td>Subnet</td>
    <td>Public or private</td>
    <td>Private</td>
    <td>Public or private</td>
  </tr>
</table>

Read more about IP of each type in the articles:

<a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">Create and configure a floating IP address</a> 


 <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">Create and configure a virtual IP address</a> 

<a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">Create and configure a reserved IP address</a>