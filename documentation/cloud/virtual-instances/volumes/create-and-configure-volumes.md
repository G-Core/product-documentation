---
title: create-and-configure-volumes
displayName: Create and configure
order: 20
published: true
toc:
   --1--Create a volume: "create-a-volume"
   --1--Attach volumes to a Virtual Machine: "attach-volumes-to-an-existing-virtual-machine"
   --1--Manage volumes: "manage-volumes"
   --2--Rename a volume: "rename-a-volume"
   --2--Detach a volume: "detach-a-volume-from-a-virtual machine"
   --2--Resize a volume: "resize-a-volume"
   --2--Change volume type: "change-volume-type"
   --2--Take volume snapshot: "take-a-volume-snapshot"
   --2--Revert volume: "revert-volume-to-the-latest-snapshot"
   --2--Create an image from a volume: "create-an-image-from-a-bootable-volume"
   --2--Delete volume: "delete-volume"

pageTitle: Create and configure volumes | Gcore
pageDescription: Create and configure volumes for cloud storage. Choose from High IOPS SSD, Standard, Cold, Ultra, and SSD Low-Latency types.
---
# Create and configure a volume

You can view, create, and manage volumes in the Gcore Customer Portal on the **Volumes** page. Here's how to navigate the page:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/volumes-page-annotated.png" alt="Volumes page with numbered UI elements" width="80%">

1\. **Volumes**: View all volumes created in a project.

2\. **Instance**: Check if a volume is attached to a Virtual Machine.

3\. **IOPS limit/burst**: Check the maximum number of read and write operations a volume can handle in a second and when a burst traffic occurs. 

4\. **MBps limit/burst**: Check the bandwidth limit for a volume and a max bandwidth when a burst traffic occurs.

5\. **Without attachments**: View all volumes that aren’t attached to a Virtual Machine.

In the following sections, you’ll find information on how to create and manage volumes. For a general overview of volumes and available volume types, check out our <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes" target="_blank">dedicated guide</a>. 

## Create a volume

You can create volumes in several ways: <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">when creating a Virtual Machine</a>, from the **Volumes** page, or from a snapshot. The latter two approaches are described in the following sections. 

<alert-element type="info" title="Info">
 
You can only use a volume in the same region where a Virtual Machine is created.
 
</alert-element>

<tabset-element>

### From the Volumes page

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click **Create volume**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-volume.png" alt="Volumes page with numbered storage and create volume tabs" width="80%">

3\. A new **Add volume** page will open. Here you can customize volume settings.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/new-volume-volumes-page.png" alt="Dialog with options for configuring new volume" width="75%">

4\. Specify how many GB of disk space you need. If it exceeds your current limit, [send a request for quota increase](https://gcore.com/docs/cloud/getting-started/request-a-quota-increase#how-to-send-a-request).

5\. Select the [volume type](https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes#available-volume-types). Faster volume types are designed for latency-sensitive transactional operations and storing critical data. Slower volumes are more suitable for archived or non-critical data and for less frequent operations.

6\. (Optional) Attach the volume to a Virtual Machine. A volume can only be used in the same region where a VM is created.

7\. Create a name for the volume. You can use Latin letters, numbers, underscores, spaces, and dots. The name should be between 3 and 63 characters long.

<alert-element type="tip" title="Tip">
 
When you add volumes via the Gcore Customer Portal or API, you don’t have to keep volume names consistent in the operating system (like sda, sdb, or sdc). We recommend using Universally Unique Identifiers (UUID) instead of names for OS operations.
 
</alert-element>

8\. (Optional) To add metadata to a volume, specify tags as key-value pairs.

9\. Click **Save**. 

Your volume will appear on the **Volumes** page.

### From a volume snapshot

If you need to quickly duplicate or back up information on your Virtual Machine or provision new resources from pre-existing data, you can create a volume from a snapshot of an existing volume. 

To create a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Snapshots**.

2\. Find the snapshot you want to create volume from and click on the three-dot icon to open snapshot settings. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/new-volume-snapshot.png" alt="Snapshots tab with expanded settings menu" width="80%">

3\. Click **Create volume**.

4\. Select the Virtual Machine to which you want to attach a new volume.

5\. Click **Create**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-volume-from-snapshot.png" alt="Create volume dialog with options to select Virtual Machine and add volume name" width="80%">

The volume will appear on the **Volumes** page.

</tabset-element> 

## Attach volumes to an existing Virtual Machine

If a volume is attached to a Virtual Machine, you'll see the VM name on the **Volumes** page in the **Instance** column. Otherwise, you’ll see the "Attach to instance" link. You can attach more than one volume to a Virtual Machine. However, volumes can only be used in the same region where the VM is created.

You can attach volumes to a Virtual Machine either from the **Volumes** page or from the VM settings.

<tabset-element>

### From the Volumes page

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Find the volume that you want to attach and click **Attach to instance**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume.png" alt="Volumes page with annotated attach to Virtual Machine link" width="80%">

3\. Select the Virtual Machine from the **Choose instance to attach to** dropdown.

4\. (Optional) Add an attachment tag.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume-to-instance.png" alt="Attach volume dialog with options to select Virtual Machine and add a tag" width="75%">

5\. Click **Attach volume**.

You’ve successfully attached a volume to the Virtual Machine. 

### From Virtual Machine settings

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Virtual instances**.

2\. Find the Virtual Machine you want to update and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/cloud-instances.png" alt="Virtual Machines tab with two created instances" width="80%">

3\. Open the **Volumes** tab.

4\. Click **Add volume**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/attach-volume-instance-settings.png" alt="Volumes tab with Add volume button highlighted" width="80%">

5\. Click **Use existing** to attach an existing volume to an Virtual Machine. 

You can also create a new volume here. Click **Create new** and configure the settings as described under the [Create a volume](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#create-a-volume) section. 

6\. Select the volume that you want to attach to the Virtual Machine.

7\. (Optional). Add an attachment tag.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/add-volume-to-instance.png" alt="Add volume menu with options to add Virtual Machine and tags" width="75%">

8\. Click **Add volume**.

You’ve successfully attached a volume to the Virtual Machine. 

</tabset-element>

## Manage volumes

The options for managing volumes differ depending on the volume you want to modify: boot or regular. 

If you have a large number of volumes, you can also search for volumes by name or UUID values to find the one you need. 

### Rename a volume

You can rename both boot and regular volumes:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to rename.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Rename**.

4\. Enter a new name.

5\. Select **Save** to apply the changes. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/rename-volume.png" alt="Rename volume dialog" width="80%">

Your volume has been renamed. 

### Detach a volume from a Virtual Machine

You can only detach regular volumes. The boot volume cannot be detached from an Virtual Machine as long as the VM exists. If you want to detach a boot volume, you need to delete the VM first.

To detach a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to detach.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-attached.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Choose the Virtual Machine from which you want to detach a volume.

4\. Select **Confirm**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/detach-volume-dialog.png" alt="Dialog asking to select a VM to detach the volume from" width="80%">

You’ve detached a volume from the Virtual Machine. 

<alert-element type="warning" title="Warning">
 
Detaching a volume will not cancel your payment unless you delete the volume. You can also add a detached volume to any Virtual Machine at any time.

</alert-element>

### Resize a volume

You can resize both boot and regular volumes:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to resize.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. In the **Resize volume** dialog that opens, you can see your current volume size in GB. Enter the new volume size. 

4\. Click **Resize volume** to apply the changes.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/resize-volume.png" alt="Dialog asking for a new volume size" width="80%">

You’ve changed your volume size. 

<alert-element type="warning" title="Warning">

If you have snapshots for this volume, after you increase the size, you won’t be able to [revert from the last snapshot](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#revert-volume-from-snapshot). You can only create a new volume from this volume’s snapshot.

</alert-element>

### Change volume type

This option is available for regular volumes of High IOPS and Standard types. You can’t change the type of boot volume. However, you can create a new volume from a volume snapshot with the required type.

<alert-element type="info" title="Info">

Before proceeding with the following instructions, make sure that a volume is detached from a Virtual Machine. Otherwise, the **Retype** button won’t appear in your settings list.

</alert-element>

To retype a volume:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to retype.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Retype**.

4\. Select the desired volume type and then click **Retype** to apply the updates.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/retype-volume.png" alt="Dialog asking to select a new volume type" width="80%">

You’ve successfully changed the volume type. 

If you have multiple volumes attached to one Virtual Machine, you can use the `rsync` and `cp` utilities to migrate data between volumes within an operating system.

### Take a volume snapshot

You can create a volume snapshot and use it later for backup, further recovery, and deploying new Virtual Machines from snapshots of boot volumes. 

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

In case of an accidental data loss or data corruption, you might need to restore a volume to its previous state. If you [made a snapshot of that volume](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#take-volume-snapshot), you can roll your volume back to the state when that snapshot was taken. 

<alert-element type="info" title="Info">

Before proceeding with the following instructions, make sure that the volume is [detached from an instance](https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes#detach-a-volume-from-an-instance) and that you have the volume’s snapshot. Otherwise, you’ll get an error when trying to revert the volume to its previous state. 

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

### Create an image from a bootable volume

You can create an image from a boot volume and use that image to create a new Virtual Machine. 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume from which you want to create an image.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-boot.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Select **Create image**.

4\. Specify the image name.

5\. Select architecture.

6\. Click **Create image**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/create-image.png" alt="Dialog to select image and and architecture" width="80%">

Within a few minutes, the image will be created and available on the **Images** page.

### Delete volume

You can delete a regular volume that’s not attached to a Virtual Machine. Boot volumes can only be deleted together with the VM.

To delete a volume: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Storage**.

2\. Click the three-dot icon next to the volume you want to remove.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/three-dot-menu-regular.png" alt="Volumes tab with expanded settings menu" width="80%">

3\. Click **Delete**.

4\. Confirm your action by typing “Delete” in the text field.

5\. Click **Delete volume.**

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/volumes/create-and-configure-volumes/delete-volume.png" alt="Dialog asking to confirm volume deletion" width="80%">

The volume has been removed from the Gcore Customer Portal. 

<alert-element type="tip" title="Tip">
 
You can also use the **Actions** dropdown to delete multiple volumes at once. For this option to be active, you must have at least one regular volume that is not attached to any Virtual Machine.
 
</alert-element>

