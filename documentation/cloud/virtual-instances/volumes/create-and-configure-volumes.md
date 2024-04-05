---
title: create-and-configure-volumes
displayName: Create and configure
order: 20
published: true
toc:
   --1--Create a volume: "create-a-volume"
   --1--Attach volumes to an instance: "attach-volumes-to-an-existing-instance"
   --1--Manage volumes: "manage-volumes"
   --2--Rename a volume: "rename-a-volume"
   --2--Detach a volume: "detach-a-volume-from-an-instance"
   --2--Resize a volume: "resize-a-volume"
   --2--Change volume type: "change-volume-type"
   --2--Take volume snapshot: "take-a-volume-snapshot"
   --2--Revert volume: "revert-volume-to-the-latest-snapshot"
   --2--Create image from a volume: "create-image-from-a-bootable-volume"
   --2--Delete volume: "delete-volume"

pageTitle: Create and configure volumes | Gcore
pageDescription: Create and configure volumes for cloud storage. Choose from High IOPS SSD, Standard, Cold, Ultra, and SSD Low-Latency types.
---
# Create and configure a volume

You can view, create, and manage volumes in the Gcore Customer Portal on the **Volumes** page.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/volumes-page-annotated.png" alt="Volumes page with numbered UI elements" width="80%">

1\. **Volumes**: view all volumes created in a project.

2\. **Instance**: check if a volume is attached to an instance.

3\. **IOPS limit/burst**: check the maximum number of read and write operations a volume can handle in a second and when a burst traffic occurs. 

4\. **MBps limit/burst**: check the bandwidth limit for a volume and a max bandwidth when a burst traffic occurs.

5\. **Without attachments**: view all volumes that aren’t attached to any instance.

In the following sections, you’ll find information on how to create and manage volumes. For a general overview of volumes and available volume types, check out our <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes" target="_blank">dedicated guide</a>. 

## Create a volume

You can create volumes in several ways: <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">when creating a virtual instance</a>, from the **Volumes** page, or from a snapshot. The last two approaches are described in the following sections. 

<alert-element type="info" title="Info">
 
You can use a volume only in the same region where an instance is created.
 
</alert-element>

<tabset-element>

### From the Volumes page

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click **Create volume**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-volume.png" alt="Volumes page with numbered storage and create volume tabs" width="80%">

3\. A new **Add volume** page will open. Here you can customize volume settings.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/new-volume-volumes-page.png" alt="Dialog with options for configuring new volume" width="75%">

4\. Specify how many GiB of disk space you need. If it exceeds your current limit, [send a request for quota increase](https://gcore.com/docs/cloud/getting-started/request-a-quota-increase#how-to-send-a-request).

5\. Select [volume type](https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes#available-volume-types). Faster volume types are designed for latency-sensitive transactional operations and storing critical data. Slower volumes are more suitable for archived or non-critical data and for less frequent operations.

6\. (Optional) Attach the volume to an instance. Consider that a volume can only be used in the same region where an instance is created.

7\. Enter volume name. You can use Latin letters, numbers, underscores, spaces, and dots. The name should be between 3 and 63 characters long.

<alert-element type="tip" title="Tip">
 
When you add volumes via Customer Portal or API, you don’t have to keep volume names consistent in the operating system (like sda, sdb, or sdc). We recommend using Universally Unique Identifiers (UUID) instead of names for OS operations.
 
</alert-element>

8\. (Optional) To add metadata to a volume, specify tags as key-value pairs.

9\. Click **Save**. 

The created volume will appear in the **Volumes** section.

### From a volume snapshot

If you need to quickly duplicate or back up information on your instance or provision new resources from pre-existing data, you can create a volume from a snapshot of an existing volume. 

To create a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Snapshots**.

2\. Find the snapshot you want to create volume from and click on the three-dot icon to open snapshot settings. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/new-volume-snapshot.png" alt="Snapshots tab with expanded settings menu" width="80%">

3\. Click **Create volume**.

4\. Select the instance to which you want to attach a new volume.

5\. Click **Create**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-volume-from-snapshot.png" alt="Create volume dialog with options to select instance and add volume name" width="80%">

The volume will appear on the **Volumes** page.

</tabset-element> 

## Attach volumes to an existing instance

If a volume is attached to an instance, you’ll see the instance name on the **Volumes** page in the **Instance** column. Otherwise, you’ll see the "Attach to instance" link. You can attach more than one volume to an instance. However, these volumes can only be used in the same region where the instance is created.

You can attach volumes to an instance either from the **Volumes** page or from the instance settings.

<tabset-element>

### From the Volumes page

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Find the volume that you want to attach and click **Attach to instance**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume.png" alt="Volumes page with annotated attach to instance link" width="80%">

3\. Select the instance from the **Choose instance to attach to** dropdown.

4\. (Optional) Add an attachment tag.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume-to-instance.png" alt="Attach volume dialog with options to select instance and add a tag" width="75%">

5\. Click **Attach volume**.

Your volume is added to the selected instance.

### From instance settings

1\. In the Customer Portal, navigate to **Cloud** > **Virtual instances**.

2\. Find the instance you want to update and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/cloud-instances.png" alt="Virtual instances tab with two created instances" width="80%">

3\. Open the **Volumes** tab.

4\. Click **Add volume**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume-instance-settings.png" alt="Volumes tab with Add volume button highlighted" width="80%">

5\. Click **Use existing** to attach an existing volume to an instance. 

You can also create a new volume here—click **Create new** and configure the settings as described in the [Create a volume](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#create-a-volume) section. 

6\. Select a volume that you want to attach to the instance.

7\. (Optional). Add an attachment tag.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/add-volume-to-instance.png" alt="Add volume menu with options to add instance and tags" width="75%">

8\. Click **Add volume**.

You’ve successfully attached a volume to the instance. 

</tabset-element>

## Manage volumes

The options for managing volumes differ depending on the volume you want to modify: boot or a regular one. 

If you have a large number of volumes, you can also search for volumes by name or UUID values to find the one you need. 

### Rename a volume

You can rename both a boot and regular volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to rename.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Select **Rename**.

4\. Enter a new name.

5\. Select **Save** to apply the changes. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/rename-volume.png" alt="Rename volume dialog" width="80%">

Your volume has been renamed. 

### Detach a volume from an instance

You can only detach regular volumes. The boot volume cannot be detached from an instance as long as the instance exists. If you want to detach a boot volume, you need to delete the instance first.

To detach a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to detach.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-attached.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Choose the instance from which you want to detach a volume.

4\. Select **Confirm**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/detach-volume-dialog.png" alt="Dialog asking to select an instance to detach the volume from" width="80%">

You’ve detached a volume from the instance. 

<alert-element type="warning" title="Warning">
 
Detaching a volume will not cancel your payment unless you delete the volume. You can also add a detached volume to any instance at any time.

</alert-element>

### Resize a volume

You can resize both a boot and a regular volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to resize.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. In the **Resize volume** dialog that opens, you can see your current volume size in GB. Enter the new volume size. 

4\. Click **Resize volume** to apply the changes.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/resize-volume.png" alt="Dialog asking for a new volume size" width="80%">

You’ve increased your volume size. 

<alert-element type="warning" title="Warning">

If you have snapshots for this volume, after you increase the size, you won’t be able to [revert from the last snapshot](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#revert-volume-from-snapshot). You can only create a new volume from this volume’s snapshot.

</alert-element>

### Change volume type

This option is available for regular volumes of High IOPS and Standard types. You can’t change the type of boot volume. However, you can create a new volume from a volume snapshot with the required type.

<alert-element type="info" title="Info">

Before proceeding with the following instructions, make sure that a volume is detached from an instance. Otherwise, the **Retype** button won’t appear in your settings list.

</alert-element>

To retype a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to retype.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Retype**.

4\. Select the desired volume type and then click **Retype** to apply the updates.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/retype-volume.png" alt="Dialog asking to select a new volume type" width="80%">

You’ve successfully changed a volume type. 

If you have multiple volumes attached to one instance, you can use the `rsync` and `cp` utilities to migrate data between volumes within an operating system.

### Take a volume snapshot

You can create a volume snapshot and use it later for backup and further recovery, as well as for deploying new instances from snapshots of boot volumes. 

To take a snapshot:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the needed volume.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Take snapshot**.

4\. Enter snapshot name.

5\. Click **Take snapshot**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/take-snapshot.png" alt="Dialog asking to add a snapshot name" width="80%">

The snapshot will appear on the **Snapshots** page, along with the other created snapshots.

### Revert volume to the latest snapshot

In case of an accidental data loss, data corruption, or for a similar reason, you might need to restore a volume to its previous state. If you [made a snapshot of that volume](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#take-volume-snapshot), you can roll your volume back to the state when that snapshot was taken. 

<alert-element type="info" title="Info">

Before proceeding with the following instructions, make sure that a volume is [detached from an instance](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#detach-a-volume-from-an-instance) and that you have the volume’s snapshot. Otherwise, you’ll get an error when trying to revert a volume to its previous state. 

</alert-element>

To revert a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to revert.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Revert to the latest snapshot**.

4\. Click **Revert**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/revert-volume.png" alt="Dialog asking to confirm volume reverting" width="80%">

<alert-element type="info" title="Info">

After resizing a volume, reversion is unavailable because the latest snapshot is taken for the old size. You can only create a new volume. For the new size, create a new snapshot.

</alert-element>

### Create image from a bootable volume

You can create an image from a boot volume and use that image to create a new instance. 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume from which you want to create an image.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-boot.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Select **Create image**.

4\. Specify the image name.

5\. Select architecture.

6\. Click **Create image**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-image.png" alt="Dialog to select image and and architecture" width="80%">

Within several minutes, the image will be created and available in the Images section.

### Delete volume

You can delete a regular volume that’s not attached to an instance. The boot volume can only be deleted together with the instance.

To delete a volume: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to remove.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Delete**.

4\. Confirm your action by typing “Delete” in the text field.

5\. Click **Delete volume.**

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/delete-volume.png" alt="Dialog asking to confirm volume deletion" width="80%">

The volume is removed from the Customer Portal. 

<alert-element type="tip" title="Tip">
 
You can also use the **Actions** dropdown to delete multiple volumes at once. For this option to be active, you must have at least one regular volume that is not attached to any instance.
 
</alert-element>

