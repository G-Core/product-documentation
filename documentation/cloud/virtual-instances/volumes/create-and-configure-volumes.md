---
title: create-and-configure-volumes
displayName: Create and configure
order: 20
published: true
toc:
   --1--Volumes section: "volumes-section"
   --1--Create: "create-a-volume"
   --1--Manage: "manage-your-volumes"
pageTitle: Create a volume | Gcore
pageDescription: Create and configure volumes for cloud storage. Choose from High IOPS SSD, Standard, Cold, Ultra, and SSD Low-Latency types.
---
# Create and configure volumes

## Volumes section

The **Volumes** section displays both disks that were added and those that were not added to instances in the selected location, their system name, and creation date.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/_________________.png" alt="_________________.png">

If a disk is attached to an instance, you will see the instance in the **Instance** column. Click on its name for more info.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/__________________.png" alt="__________________.png">

If a volume is not attached to an instance, you will see "Attach to instance" in the **Instance** column.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/____________________.png" alt="____________________.png">

Click **Attach to instance** to attach a volume to an instance. In the pop-up window, select the instance and click **Attach volume**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/___________________.png" alt="___________________.png">

## Create a volume

You can create volumes while creating an instance or in the **Volumes** section.

To create a volume in the **Volumes** section:

1\. Go to the **Volumes** section and click **Create volume**.  

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create_volume_2.png" alt="create_volume_2.png" width="653" height="249">

2\. In the next dialog box, set the volume size in GB and select its type: faster for critical data and slower for archived data.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/_____________2_____.png" alt="_____________2_____.png" width="502" height="438">

Five types of volumes are available:

* **High IOPS SSD**. This is a high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

Availability: Amsterdam, Frankfurt, London, Luxembourg, Luxembourg-2, Manassas, Paris-2, Singapore

* **Standard**. This is a network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

Availability: all regions

* **Cold**. This is a network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **Ultra**. This is the network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **SSD Low-Latency**. This is an SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

Availability: Amsterdam-2, Frankfurt, Hong Kong, Luxembourg-2, Manassas, Tokyo

For **High IOPS SSD** and **Standard** volumes:

- Volume IO Burst and Volume Throughput Burst are supported.

- IO credits and throughput credits are provided to exceed base limits and ensures optimal performance at peak IOPS and throughput.

- Credits increase IOPS and volume throughput by 10x times for 10 minutes.

For example, your instance has a 3 GB High IOPS SSD volume with base limits of 180 IOPS and 7.5 MB (60 IOPS x 3 GB and 2.5 MB/s x 3 GB). If the IOPS and throughput values ​​exceed these limits, renewable resources are added: (60 IOPS x 3 GB + 2.5 MB/s x 3 GB = 180 IOPS + 7.5 MB) x 10 = 1800 IOPS + 75 MB/s.

Credits are restored after peak usage and load reduction. If the base limits are exceeded again, renewed credits will be applied. 

3\. (If you don't want to attach the volume to an instance, skip this step). Select the instance from the list.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/___________________.png" alt="___________________.png">

4\. Enter the volume name and click **Save**.

The created volume will appear in the **Volumes** section.

The volume can be created only in the location indicated in the upper-right corner.

**Note:** Volume names may not be consistent in OS (e.g., sda, sdb, sdc...) when adding via UI/API. UUID is recommended for OS operations.! If you don't want to attach the volume to an instance, skip this field.

## Manage your volumes

By simply clicking on the three-dot icon next to the desired volume, you can detach it from the instance, change its size or type, take a snapshot, or delete it. Additionally, it's possible to create an image from the boot volumes, expanding the flexibility and control over your storage resources.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/mceclip2.png" alt="mceclip2.png">

1\. Create an image (from the bootvolume).

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/______________________EN.png" alt="______________________EN.png">

Enter a name for the image and click on **Create image**. Within several minutes, the image will be created and available in the **Images** section.

2\. Detach a volume from an instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/detach2.png" alt="detach2.png" width="523" height="390">

Select the instance from which you want to detach the selected volume. Click OK to detach the volume.

**Attention!** Detaching a volume will not cancel your payment for it. You can attach a volume to any instance at any time.

3\. Resize volume:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/resize2.png" alt="resize2.png">

The opened window shows the current volume size. Use keyboard input or arrows to set the new volume size. Click Resize volume to save your settings.

4\. Retype volume:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/retype2.png" alt="retype2.png">

Detach a volume from an instance.  Select the necessary volume type. Click Retype to save the settings.

**Note:** Conversion is only possible for High IOPS and Standard. 

Moreover, you can migrate data between disks within an OS using "rsync" or "cp" utilities.

5\. To take a snapshot, enter its name and click **Take snapshot**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/snap2.png" alt="snap2.png">

6\. Delete volume:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/delete2.png" alt="delete2.png">

You can only delete a volume that is not attached to an instance. 

To delete a volume that is attached to an instance, click **Detach** and then **Delete**.

**Note:** The instance boot volume can only be deleted together with the instance in the instance management section.

7\. Revert volume to the latest snapshot

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/mceclip3.png" alt="mceclip3.png" width="541" height="204">

Detach the volume from your instance and revert to the latest snapshot.

**Note:**  After resizing a volume, reversion is unavailable because the latest snapshot is taken for the old size. You can only create a new volume. For the new size, create a new snapshot.