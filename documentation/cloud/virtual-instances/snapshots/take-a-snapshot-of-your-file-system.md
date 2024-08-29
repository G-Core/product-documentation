---
title: take-a-snapshot-of-your-file-system
displayName: Take a snapshot of your file system
order: 10
published: true
toc:
   --1--Create a snapshot: "create-a-snapshot"
   --2--From the Snapshots page: "from-the-snapshots-page"
   --2--From the Volumes page: "from-the-volumes-page"
   --2--From the Virtual Machine: "from-virtual-machine"
   --1--Snapshot management: "snapshot-management"
   --2--Create a VM from a snapshot of the system volume: "create-a-vm-from-a-snapshot-of-the-system-volume"
   --2--Delete a snapshot: "delete-a-snapshot"
   --2--Reverte a volume to the latest snapshot: "also-you-can-revert-a-volume-to-the-latest-snapshot--open-the--volumes--section--detach-the-volume-from-your-vm-and-select-the-reverting-option-on-the-selector"
pageTitle: Take a snapshot of your file system | Gcore
pageDescription: Learn how to take a snapshot of your file system to backup your data.
---
# Take a snapshot of your file system

**Snapshot** is the state of a system at a particular point in time. The snapshot can be used for backup and further recovery, as well as for deploying new Virtual Machines from **snapshots of system volume.** 

**Difference between system and regular volume snapshots** 

You can make snapshots for both system (boot) volumes and regular volumes. 

**The system volume** is the volume which the operating system is installed. On this volume, the operating system (OS) stores everything it needs to work.  

**Regular volume** contains all other information for use, except the operating system.  

## Create a snapshot

### From the Snapshots page 

To make a snapshot of the volume, go to the "Snapshots" section inside the project.  

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________.png" alt="_______________.png">

In the "Take snapshot" section, select the volume to create the snapshot. **System volumes** will have the "_bootvolume" Postfix -> Enter a name for the snapshot in the "Name" field and click "Create snapshot". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________________.png" alt="_______________________________.png">

### From the Volumes page
Inside the project, in the "Volumes" section, select the volume to create a snapshot -> on the selector on the right from the selected volume -> select the "Take snapshot" option 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/______________________.png" alt="______________________.png">

In the drop-down window, enter a name for the snapshot and click "Take snapshot". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________.png" alt="_______________________.png">

### From the Virtual Machine

1\. Open the project and go to the **Instances** page and select the Virtual Machine you want to take a snapshot from.

2\. Click the three-dot icon and select **Overview**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________.png" alt="__________.png">

3\. Go to the **Volumes** tab and select the volume to create a snapshot.

4\. Click **Take snapshot**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________________.png" alt="_______________________________.png">

5\/ In the window that opens, enter a name for the snapshot and click **Take snapshot**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________________.png" alt="__________________.png"> 

6\. In the "Snapshots" section, you can view a list of created snapshots from VM volumes.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________________.png" alt="__________________.png">

## Snapshot management

A list of all created snapshots can be found in the "Snapshots" section, inside the project. 

 <img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_____________________________.png" alt="_____________________________.png">

You can select the necessary option on the selector on the right from the snapshot: 

### Create a VM from a snapshot of the system volume

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_________________________________.png" alt="_________________________________.png">
    
    
### Delete a snapshot
    
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______.png" alt="_______.png">

**Also, you can revert a volume to the latest snapshot**. Open the "Volumes" section, detach the volume from your Virtual Machine and select the reverting option on the selector.

Please note: if you have just resized the volume you will not be able to use the function because the last snapshot is designed for the old size. You can only create a new volume from it. For the new size volume, you need to create a new snapshot.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/mceclip1.png" alt="mceclip1.png">