---
title: difference-between-virtual-floating-and-reserved-ip-addresses
displayName: Difference between virtual, floating, and reserved IP addresses
published: true
order: 40
toc:
pageTitle: Types of IP addresses | Gcore
pageDescription: Understand the differences between virtual, floating, and reserved IP addresses.
---
# Difference between virtual, floating, and reserved IP addresses

Cloud IP addresses serve different purposes based on their type. Virtual, floating, and reserved IPs provide flexibility for high availability, external access, and network management. The table below outlines their key differences and use cases.

<table border="1">
    <thead>
        <tr>
            <th>Type of an IP address</th>
            <th>Use cases</th>
            <th>Intended for</th>
            <th>Subnet</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Virtual IP</td>
            <td>
                • Assign to multiple Virtual Machines for fault tolerance<br>
                • Use as a secondary address for a network interface<br>
                • Automatically assigned as a Virtual IP for Load Balancers<br>
                • A virtual IP is a subtype of a Reserved IP
            </td>
            <td>Virtual Machines</td>
            <td>Public or private</td>
        </tr>
        <tr>
            <td>Floating IP</td>
            <td>
                • Provide public access to a Virtual Machine in a private subnet via DNAT<br>
                • Assign to any Virtual Machine, Bare Metal server, or Load Balancer
            </td>
            <td>Private ports of Virtual Machines, Bare Metal servers, and Load Balancers</td>
            <td>Public (mapped via DNAT)</td>
        </tr>
        <tr>
            <td>Reserved IP</td>
            <td>
                • Pre-allocate an IP for future use<br>
                • Assign to any Virtual Machine, Bare Metal server, or Load Balancer at any time<br>
                • Can be converted into a Virtual IP if needed
            </td>
            <td>Virtual Machines, Bare Metal servers, and Load Balancers</td>
            <td>Public or private</td>
        </tr>
    </tbody>
</table>

## Cloud IPs

All IP addresses on the Cloud platform are native and correspond to the exact physical location where the server is deployed. This results in low latency, optimized routing, and improved performance for cloud services.

When a public IP is assigned, it comes from a shared regional pool and remains static for the lifetime of the network interface. However, if the interface is deleted and re-created, the public IP is released back into the pool and replaced with a new one.


Read more about each IP type in the following articles:

<a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">Create and configure a floating IP address</a> 

<a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">Create and configure a virtual IP address</a> 

<a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">Create and configure a reserved IP address</a>
