---
title: take-a-snapshot-of-your-file-system
displayName: Take a snapshot of your file system
order: 10
published: true
toc:
   --1--Creating a snapshot: "creating-a-snapshot"
   --2--From the "Snapshots" section: "from-the-snapshots--section"
   --2--From the "Volumes" section: "from-the-volumes--section"
   --2--From the Instance: "from-instance"
   --1--Snapshot management: "snapshot-management"
   --2--Creating an Instance from a snapshot of the system drive: "to-create-an-instance-from-a-snapshot-of-the-system-drive"
   --2--Creating a disk from a disk snapshot: "create-a-disk-from-a-disk-snapshot"
   --2--Deleting a snapshot: "delete-a-snapshot"
   --2--Reverting a volume to the latest snapshot: "also-you-can-revert-a-volume-to-the-latest-snapshot--open-the--volumes--section--detach-the-volume-from-your-instance-and-select-the-reverting-option-on-the-selector"
pageTitle: Take a snapshot of your file system | Gcore
pageDescription: Learn how to take a snapshot of your file system to backup your data.
---
# Take a snapshot of your file system

**Snapshot** is the state of a system at a particular point in time. The snapshot can be used for backup and further recovery, as well as for deploying new instances from **snapshots of system disks.** 

**Difference between system and regular disk snapshots** 

You can make a snapshot for both system (boot) disks and regular disks. 

**The system disk** is the disk on which the operating system is installed. On this disk, the operating system (OS) stores everything it needs to work.  

**Regular disk -** contains all other information for use, except the operating system.  

## **Creating a snapshot** 

### **From the** **"Snapshots"** **section** 

To make a snapshot of the disk, go to the "Snapshots" section inside the project.  

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________.png" alt="_______________.png">

In the "Take snapshot" section, select the disk to create the snapshot. **System disks** will have the "_bootvolume" Postfix -> Enter a name for the snapshot in the "Name" field and click "Create snapshot". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________________.png" alt="_______________________________.png">

### **From the "Volumes" section** 

Inside the project, in the "Volumes" section, select the disk to create a snapshot -> on the selector on the right from the selected volume -> select the "Take snapshot" option 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/______________________.png" alt="______________________.png">

In the drop-down window, enter a name for the snapshot and click "Take snapshot". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________.png" alt="_______________________.png">

### **From Instance** 

Inside the project, go to the "Instances" section -> select the Instance you want to take a snapshot from -> select the "Overview" option on the selector on the right from the machine. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________.png" alt="__________.png">

Go to the "Volumes" section -> select the disk to create a snapshot -> select the "Take snapshot" option on the selector on the right from the disk 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______________________________.png" alt="_______________________________.png">

In the window that opens, enter a name for the snapshot and click "Take snapshot" 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________________.png" alt="__________________.png"> 

In the "Snapshots" section, you can view a list of created snapshots from Instance disks 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/__________________.png" alt="__________________.png">

## **Snapshot management** 

A list of all created snapshots can be found in the "Snapshots" section, inside the project. 

 <img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_____________________________.png" alt="_____________________________.png">

You can select the necessary option on the selector on the right from the snapshot: 

### **To create an Instance from a snapshot of the system drive** <img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_________________________________.png" alt="_________________________________.png">
    
### **Create a disk from a disk snapshot** <img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/____________________________________________.png" alt="____________________________________________.png">
    
### **Delete a snapshot**
    
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/_______.png" alt="_______.png">

**Also, you can revert a volume to the latest snapshot**. Open the "Volumes" section, detach the volume from your instance and select the reverting option on the selector.

Please note: if you have just resized the volume you will not be able to use the function because the last snapshot is designed for the old size. You can only create a new volume from it. For the new size volume, you need to create a new snapshot.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system/mceclip1.png" alt="mceclip1.png">