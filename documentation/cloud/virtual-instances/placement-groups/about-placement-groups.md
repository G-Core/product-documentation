---
title: about-placement-groups
displayName: Overview
published: true
order: 10
toc:
pageTitle: About placement groups | Gcore
pageDescription: Understand placement groups to control whether virtual machines share a physical server or they are deployed on different ones.
---
# About placement groups

A placement group is a policy that determines whether virtual machines will be hosted on the same physical server or on different ones.

## Types of groups

There are three types of groups:

- **Affinity** groups assemble virtual machines on the same hardware. Machines launched in one affinity group will exchange data faster because they are located on the same server.

- **Anti-affinity** groups work the opposite way: All virtual machines in this group will be separated across different physical hardware. This increases fault tolerance of a cluster: Even if something happens to one server, machines on the other(s) will remain available.

- **Soft anti-affinity** groups encourage, but don't strictly enforce, the separation of virtual machines. Unlike a strict anti-affinity policy, where machines may never be placed together, soft anti-affinity allows placement on the same hardware when it is necessary due to factors like resource constraints or high demand. It is suitable for users who want to use the anti-affinity policy by default while also avoiding machine creation failures if an unused host was not found.

## FAQ

**What happens if you don’t add instances to a placement group?** They will be placed on physical servers randomly—they could end up all on the same server or spread across different ones.

**How many placement groups a machine can belong to at the same time?** A machine can only belong to one group. It is impossible to add a machine to two different groups at once.