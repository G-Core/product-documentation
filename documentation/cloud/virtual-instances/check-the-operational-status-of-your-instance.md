---
title: check-the-operational-status-of-your-instance
displayName: Check the status
order: 20
published: true
toc:
pageTitle: VM status | Gcore
pageDescription: Understand the operational status of your VM - Building, Power on, Power off, Error, and Deleted.
---
# Check the operational status of your instance
You can find the instance statues inside the project, in the "Instances" section, in the "Status" column 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/1.__________.png" alt="1.__________.png">

For instance, in Cloud we have the following statuses: 

*   Building — allocating resources to the VM. 
*   Power on — the VM is running.  
*   Power off - a virtual machine is powered off.  
*   Error — an error occurred when allocating resources. The machine cannot be allocated. 
*   Deleted — the VM was deleted.  

Instance cycles 

1.  After creation, the Instance will have the "Building" status for the first few minutes. At this stage, the machine is allocated computing resources. 
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/2.________.png" alt="2.________.png">
2.  After that, the server will automatically switch to the "Power on" status. This means that the machine is up and running. 
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/3._________.png" alt="3._________.png">
3.  When the power is turned off, the instance switches to the "Power Off" status. 
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/4._________.png" alt="4._________.png">
4.  If you initiate server deletion, all the ongoing operations are aborted and then the VM switches to the "Deleted" status. 
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/5.__________.png" alt="5.__________.png">

If an error occurs when allocating resources, the VM gets the "Error" status. if you get this status, you may contact technical support _support_@gcore.lu.