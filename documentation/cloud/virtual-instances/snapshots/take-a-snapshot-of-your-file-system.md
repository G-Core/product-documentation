---
title: take-a-snapshot-of-your-file-system
displayName: Take a snapshot of your file system
order: 10
published: true
toc:
   --1--Create: "create-a-snapshot"
   --1--Manage: "manage-your-snapshots"
---
# Take a snapshot of your file system

**Snapshot** is the state of a system at a particular point in time. The snapshot can be used for backup and further recovery, as well as for deploying new instances from **snapshots of system disks.** 

**Difference between system and regular disk snapshots** 

You can make a snapshot for both system (boot) disks and regular disks. 

**The system disk** is the disk on which the operating system is installed. On this disk, the operating system (OS) stores everything it needs to work.  

**Regular disk -** contains all other information for use, except the operating system.  

## Create a snapshot

There three ways to create a snapshot: from the **Snapshot** menu, from the **Volumes** menu, and from the **Instances** menu.

1.  Create a snapshot from the **Snapshots** menu.

To make a snapshot of the disk, go to the "Snapshots" section inside the project.  

<img src="https://support.gcore.com/hc/article_attachments/360012025238/_______________.png" alt="_______________.png">

In the “Take snapshot” section, select the disk to create the snapshot. **System disks** will have the "\_bootvolume" Postfix -> Enter a name for the snapshot in the “Name” field and click "Create snapshot". 

<img src="https://support.gcore.com/hc/article_attachments/360012025258/_______________________________.png" alt="_______________________________.png">

2. Create a snapshot from the **Volumes** menu.

Inside the project, in the “Volumes” section, select the disk to create a snapshot -> on the selector on the right from the selected volume -> select the "Take snapshot" option 

<img src="https://support.gcore.com/hc/article_attachments/360011939337/______________________.png" alt="______________________.png">

In the drop-down window, enter a name for the snapshot and click “Take snapshot”. 

<img src="https://support.gcore.com/hc/article_attachments/360011939377/_______________________.png" alt="_______________________.png">

3. Create a snapshot from the **Instances** menu

Inside the project, go to the “Instances” section -> select the Instance you want to take a snapshot from -> select the "Overview" option on the selector on the right from the machine. 

<img src="https://support.gcore.com/hc/article_attachments/360011939397/__________.png" alt="__________.png">

Go to the “Volumes” section -> select the disk to create a snapshot -> select the “Take snapshot” option on the selector on the right from the disk 

<img src="https://support.gcore.com/hc/article_attachments/360012025338/_______________________________.png" alt="_______________________________.png">

In the window that opens, enter a name for the snapshot and click “Take snapshot” 

<img src="https://support.gcore.com/hc/article_attachments/360012025358/__________________.png" alt="__________________.png"> 

In the “Snapshots” section, you can view a list of created snapshots from Instance disks 

<img src="https://support.gcore.com/hc/article_attachments/360011939437/__________________.png" alt="__________________.png">

## Manage your snapshots

A list of all created snapshots can be found in the "Snapshots" section, inside the project. 

 <img src="https://support.gcore.com/hc/article_attachments/360012025378/_____________________________.png" alt="_____________________________.png">

You can select the necessary option on the selector on the right from the snapshot: 

### Create an instance from a snapshot of the system drive

<img src="https://support.gcore.com/hc/article_attachments/360012025398/_________________________________.png" alt="_________________________________.png">
    
### Create a disk from a disk snapshot 

<img src="https://support.gcore.com/hc/article_attachments/360011939457/____________________________________________.png" alt="____________________________________________.png">
    
### Delete a snapshot
    
<img src="https://support.gcore.com/hc/article_attachments/360011939477/_______.png" alt="_______.png">

**Also, you can revert a volume to the latest snapshot**. Open the "Volumes" section, detach the volume from your instance and select the reverting option on the selector.

Please note: if you have just resized the volume you will not be able to use the function because the last snapshot is designed for the old size. You can only create a new volume from it. For the new size volume, you need to create a new snapshot.

<img src="https://support.gcore.com/hc/article_attachments/4402888565521/mceclip1.png" alt="mceclip1.png">