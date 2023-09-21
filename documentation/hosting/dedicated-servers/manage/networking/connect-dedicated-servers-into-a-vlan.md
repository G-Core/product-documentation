---
title: connect-dedicated-servers-into-a-vlan
displayName: VLAN
order: 21
published: true
toc:
--1--VLAN initiation: "vlan-initiation"
--1--Adding new members: "adding-new-members"
pageTitle: Create a VLAN | Gcore
pageDescription: Learn how to set up a Virtual Local Area Network (VLAN) between your dedicated servers using DCI Manager with this step-by-step guide. 
---
# Connect dedicated servers into a VLAN

VLAN - virtual local network that allows working in an internal network regardless of physical server locations.

In order to set up VLAN between your servers, you should use DCI Manager.

## VLAN initiation

1\. Go to DCI manager and choose VLAN section.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid0.png" alt="VLAN section.">

2\. Click **Add** button to create a new VLAN.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid1.png" alt="new VLAN">

3\. Type a name for VLAN. For example, MyVLAN. Click ОК. 

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid5.png" alt="Type a name for VLAN">

## Adding new members

You should add members to realize an interaction by virtual local network. VLAN can be set up only for servers that belong to one account. 

1\. Highlight a created VLAN and go to VLAN Members section. 

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid6.png" alt="VLAN Members section.">

2\. Click **Add**. 

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid7.png" alt="Add">

3\. Choose a server you need to add in a drop-down list. 

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid8.png" alt="Choose a server you need to add in a drop-down list.">

4\. In a Port section choose an interface of the server and click **OK**. 

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/networking/connect-dedicated-servers-into-a-vlan/blobid9.png" alt=" Port section">

After that VLAN is ready to use. A number of servers that can be added to VLAN is unlimited.