---
title: check-the-operational-status-of-your-instance
displayName: Check the status
order: 20
published: true
toc:
pageTitle: VM status | Gcore
pageDescription: Understand the operational status of your Virtual Machine - Building, Power on, Power off, Error, and Deleted.
---
# Check the operational status of your Virtual Machine

You can find Virtual Machine (VM) statuses inside a project on the **Virtual Instances** page. Check **the Status column**:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/check-the-operational-status-of-your-instance/vm-status-column.png" alt="VM status column with the Power on status displayed" width="80%">

Each Virtual Machine can have the following statuses: 

*   **Building**: After creation, the Virtual Machine will have the **Building** status for the first few minutes. At this stage, the machine is allocated computing resources. 

*   **Power on**: The Virtual Machine is up and running. The VM status automatically changes to **Power on** once all resources are allocated after its creation.

*   **Power off**: The Virtual Machine is powered off.  

*   **Error**: An error occurred when allocating resources. The machine cannot be allocated. 

*   **Deleted**: Virtual Machine was deleted. If you initiate server deletion, all ongoing operations will be terminated, and the VM will switch to the **Deleted** status. 

<alert-element type="tip" title="Tip">
 
If an error occurs when allocating resources or your Virtual Machine gets the **Error** status, you can contact [Gcore support](mailto:support@gcore.com) for assistance.
 
</alert-element>

