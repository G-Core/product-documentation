---
title: configure-a-placement-group
displayName: Configure
order: 20
published: true
toc:
   --1--Create a group: "create-a-placement-group"
   --1--Create an instance included in a placement group: "create-an-instance-included-in-a-placement-group"
   --1--Add a previously created instance to a group: "add-a-previously-created-instance-to-a-group"
   --1--Move an instance from one group to another: "move-an-instance-from-one-group-to-another"
pageTitle: Configure a placement group | Gcore
pageDescription: Configure a placement group to control whether virtual machines share a physical server or they are deployed on different ones.
---
# Configure a placement group

## Create a placement group

In the "Placement Groups" section, create a new group. Give it a name and select a policy — affinity or anti-affinity — and click Create Placement Group.

<expandable-element title="Types of placement groups">

You can place your virtual machine in one of three types of groups:

- **Affinity** groups assemble virtual machines on the same hardware. Machines launched in one affinity group will exchange data faster because they are located on the same server.

- **Anti-affinity** groups work the opposite way: All virtual machines in this group will be separated across different physical hardware. This increases fault tolerance of a cluster: Even if something happens to one server, machines on the other(s) will remain available.

- **Soft anti-affinity** groups encourage, but don't strictly enforce, the separation of virtual machines. Unlike a strict anti-affinity policy, where machines may never be placed together, soft anti-affinity allows placement on the same hardware when it is necessary due to factors like resource constraints or high demand. It is suitable for users who want to use the anti-affinity policy by default while also avoiding machine creation failures if an unused host was not found.

</expandable-element>

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-6.png" alt="Additional options">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-6.png)

## Create an instance included in a placement group

When creating an instance, in the "Additional options" section, move the "Add to placement group" slider and select a group or create a new one — the machine will be a member of it.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-8.png" alt="Placement Group" width="509" height="502">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-8.png)

## Add a previously created instance to a group

In the instance menu, open the "Placement Group" tab. Select the previously created group where you want to add the instance to, or create a new one. Click "Add".

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-9.png" alt="Placement Group">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-9.png)

## Move an instance from one group to another

In the instance menu, open the "Placement Group" tab. Remove a machine from one group and add it to another —you can add it to a new one or to a previously created one.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-10.png" alt="Placement Group">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-10.png)[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-11.png" alt="Placement Group">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-11.png)