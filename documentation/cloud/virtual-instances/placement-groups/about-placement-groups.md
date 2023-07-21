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
Placement groups are a setting that determines whether virtual machines will be hosted on the same physical server or on different ones.

**Types of groups.** There are affinity and anti-affinity ones. An affinity group assembles equipment on one hypervisor — the machines included in it will be launched on the same physical server. Anti-affinity works the opposite way: all machines in this group will be launched on different physical servers.

**What it is used for.** Each group has its own advantages. Machines launched in one affinity group will exchange data faster because they are located on the same server. Anti-affinity group increases fault tolerance of a cluster: even if something happens to one server, machines on the other will remain available.

**What happens if you don't add instances to a placement** **group.** They will be placed on physical servers randomly — may get on the same one or on different ones.

**How many placement groups a machine can belong to at the same time**. Only to one group — it is impossible to add it to two groups at once, even if these groups are of different types (affinity and anti-affinity).