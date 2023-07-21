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

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-6.png" alt="">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-6.png)

## Create an instance included in a placement group

When creating an instance, in the "Additional options" section, move the "Add to placement group" slider and select a group or create a new one — the machine will be a member of it.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-8.png" alt="" width="509" height="502">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-8.png)

## Add a previously created instance to a group

In the instance menu, open the "Placement Group" tab. Select the previously created group where you want to add the instance to, or create a new one. Click "Add".

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-9.png" alt="">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-9.png)

## Move an instance from one group to another

In the instance menu, open the "Placement Group" tab. Remove a machine from one group and add it to another —you can add it to a new one or to a previously created one.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-10.png" alt="">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-10.png)[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-11.png" alt="">](https://assets.gcore.pro/docs/cloud/virtual-instances/placement-groups/configure-a-placement-group/image-11.png)