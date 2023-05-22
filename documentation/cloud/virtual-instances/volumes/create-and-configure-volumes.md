---
title: create-and-configure-volumes
displayName: Create and configure
order: 20
published: true
toc:
   --1--Volume section: "volume-section"
   --1--How to create a volume?: "how-to-create-a-volume"
   --1--Manage volumes: "manage-volumes"
---
# Create and configure volumes

## Volume section

The Volume section displays both disks that were added and those that were not added to instances in the selected location, their name in the system, and the creation date.

<img src="https://support.gcore.com/hc/article_attachments/360009578578/_________________.png" alt="_________________.png">

If a disk is attached to an instance, in the Instance column will be indicated to which machine this volume is added.

To learn more about an Instance, click on its name.

<img src="https://support.gcore.com/hc/article_attachments/360009578618/__________________.png" alt="__________________.png">

If a volume is not attached to an instance, in the Instance column the "Attach to instance" will be displayed.

<img src="https://support.gcore.com/hc/article_attachments/360009484677/____________________.png" alt="____________________.png">

To attach a volume to an instance, click "Attach to instance", in the pop-up window select the instance you need and click Attach volume.

<img src="https://support.gcore.com/hc/article_attachments/360009578798/___________________.png" alt="___________________.png">

## How to create a volume?

You can create volumes while creating an instance or in the Volume section.

To create a volume in the Volume section:

1\. Go to the Volume section and click Create volume.  

<img src="https://support.gcore.com/hc/article_attachments/360009482777/create_volume_2.png" alt="create_volume_2.png" width="653" height="249">

A dialog box will be opened.

<img src="https://support.gcore.com/hc/article_attachments/360009578958/_____________2_____.png" alt="_____________2_____.png" width="502" height="438">

2\. Specify the required volume size in GB.

3\. Depending on the data, select the volume type: faster for critical data and slower for archived data.

<img src="https://support.gcore.com/hc/article_attachments/360011012678/4___________.png" alt="4___________.png" width="480" height="416">

Four volume types are available: 

*   **High IOPS SSD**. The highest-performance network SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GB; 2.5 MB/s per 1 GB).  The IOPS performance limit is 9,000, and the bandwidth limit is 500 MB/s.
*   **Standard**. The high-performance network SSD block storage offers stable and high random IO performance, along with high data reliability (6 IOPS per 1 GB; 0.4 MB/s per 1 GB). The IOPS performance limit is 4,500, and the bandwidth limit is 300 MB/s.
*   **Cold** The lowest-cost HDD block storage designed for less frequently accessed workloads (maximum 500 IOPS and 100 MB/s). The IOPS performance limit is 1,000, and the bandwidth limit is 100 MB/s. Please note that for Cold volumes, we cannot guarantee these values permanently.
*   **Ultra**. The network block storage suitable for non-critical data and less frequently accessed workloads. The IOPS performance limit is 1,000, and the bandwidth limit is 100 MB/s.

For the **High IOPS SSD** and **Standard** volume types, the following functions are supported:

\- Volume IO Burst

\- Volume Throughput Burst

The options provide IO credits and throughput credits. Credits apply when the volume type base limits are exceeded, it ensures optimal volume performance at peak IOPS and throughput.

Credits increase IOPS and volume throughput in 10 times and allow volumes to continuously run at this speed (x10) for 10 minutes. For example, a 3 GB High IOPS SSD volume is attached to your instance.

The base limits of such the volume are: 60 IOPS x 3 GB + 2.5 MB/s x 3 GB = 180 IOPS +7.5 MB.

If IOPS and throughput values ​​exceed these parameters, the following renewable resources will be added: (60 IOPS x 3 GB + 2.5 MB/s x 3 GB = 180 IOPS + 7.5 MB) x 10 = 1800 IOPS + 75 MB/s.

After the peak values and reducing the load to the base level, credits are restored. The more the load decreased after the peak, the faster the credits will recover. If the base limits are exceeded again, renewed credits will be applied. 

4\. To attach the volume to an instance, select it from the pop-up list.

<img src="https://support.gcore.com/hc/article_attachments/360009579358/___________________.png" alt="___________________.png">

! If you don't want to attach the volume to an instance, skip this field.

5\. Enter the name and click Save.

You will see the created volume in the Volume section.

The volume can be created only in the location indicated in the upper-right corner.

**Please, note!** From our side, the volumes are issued in order, but we can't guarantee consistency in the names of volumes in the OS (sda, sdb, sdc ...) while adding Volumes, via UI/API

The sequence of the Volume names is determined on the OS side.

When working with Volumes in the OS, it is better to pay attention to the UUID.

## Manage volumes

You can detach the created volume from the instance, change its size, type, make a snapshot, or delete it by clicking on the three-dot icon next to the necessary volume. Moreover, you can create an image from the boot volumes. 

<img src="https://support.gcore.com/hc/article_attachments/4402889079441/mceclip2.png" alt="mceclip2.png">

Select the necessary action in the menu.

1\. Create an image (from the bootvolume)<img src="https://support.gcore.com/hc/article_attachments/360012500778/______________________EN.png" alt="______________________EN.png">

Enter a name for the image and click on the "Create image" button. Within several minutes, the image will be created and available in the ["Images"](https://support.gcorelabs.com/hc/en-us/articles/360002429818-Images) section.

2\. To detach a volume from an instance:<img src="https://support.gcore.com/hc/article_attachments/360009483457/detach2.png" alt="detach2.png" width="523" height="390">

Select the instance from which you want to detach the selected volume. Click OK to detach the volume.

**Attention!** Detaching a volume will not cancel your payment for it. You can attach a volume to any instance at any time.

3\. Resize volume:

<img src="https://support.gcore.com/hc/article_attachments/360009483477/resize2.png" alt="resize2.png">

The opened window shows the current volume size. Use keyboard input or arrows to set the new volume size. Click Resize volume to save your settings.

4\. Retype volume:

<img src="https://support.gcore.com/hc/article_attachments/360009483517/retype2.png" alt="retype2.png">

Detach a volume from an instance.  Select the necessary volume type. Click Retype to save the settings.

**Important!** Volume conversion is only possible for _High IOPS_ and _Standard_. Conversion to and from the _Cold_ type is not possible.

Moreover, you can migrate data between disks within an OS using "rsync" or "cp" utilities.

5\. Take a snapshot:

<img src="https://support.gcore.com/hc/article_attachments/360009579518/snap2.png" alt="snap2.png">

To take a snapshot, enter its Name and click Take snapshot.

6\. Delete volume:

<img src="https://support.gcore.com/hc/article_attachments/360009483557/delete2.png" alt="delete2.png">

You can only delete a volume that is not attached to an instance. 

To delete a volume that is attached to an instance, firstly click Detach in the menu. Then delete the volume, by clicking on the Delete in the menu.

**Important!** The instance boot volume can only be deleted together with the instance in the instance management section.

7\. Revert volume to the latest snapshot

<img src="https://support.gcore.com/hc/article_attachments/4402881064337/mceclip3.png" alt="mceclip3.png" width="541" height="204">

Detach the volume from your instance and then revert it to the latest snapshot by clicking on the desired option on the selector.

Please note: if you have just resized the volume you will not be able to use the function because the last snapshot is designed for the old size. You can only create a new volume from it. For the new size volume, you need to create a new snapshot.
