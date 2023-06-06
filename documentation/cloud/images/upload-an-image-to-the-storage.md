---
title: upload-an-image-to-the-storage
displayName: Upload
published: true
order: 10
toc:
   --1--Prepare for uploading: "prepare-images-for-uploading"
   --1--Upload: "upload-an-image"
---
# Upload an image to the storage

## Prepare images for uploading

1. **OS preparation.** High-performance VirtIO SCSI controllers are used for the virtual volumes in Gcore. Please make sure that virtio-scsi block devices are supported by your operating system and that the VirtIO drivers are set up.

2\. **Compatible image format.** Gcore Cloud automatically updates supported source image formats into raw format for fast instance loading, and into qcow2 format for standard instance loading. Here is the list of supported formats:

*   raw
*   vhd
*   vhdx
*   vmdk
*   vdi
*   ploop
*   qcow2
*   aki
*   ari
*   ami

## Upload an image

1. Under the **Cloud** tab, go to **Projects** and select the project name.

<img src="https://support.gcore.com/hc/article_attachments/12397877016977" alt="" width="665" height="299">

2. Select the region where you need this image.

<img src="https://support.gcore.com/hc/article_attachments/12397876992273" alt="" width="666" height="304">

3. Once you have selected the region, click on **Images**, and then proceed to **Import via URL**.

<img src="https://support.gcore.com/hc/article_attachments/12397871888145" alt="" width="666" height="305">

4. Enter the image name and make sure to specify the URL where the image will be downloaded from.

<img src="https://support.gcore.com/hc/article_attachments/12397872071313" alt="" width="300" height="225">

5. Toggle on **Show advanced options** to edit additional information such as Quick instance start, permission to use SSH key, firmware types, and operating system.

<img src="https://support.gcore.com/hc/article_attachments/12397872160785" alt="" width="300" height="436">

**Quick instance start.** If the **Quick instance start** option is enabled, you can deploy instances using your image faster, but you will not be able to delete the image while these instances are running.

The difference between standard and quick start:

*   RBD Copy-On-Write technology (standard start) uses full copying of image data to a volume. The qcow2 format is used. This method is resource-intensive and time-consuming, but it allows for the images loaded to be deleted later without affecting an instance’s operation.
*   RBD Copy-On-Write (quick start) technology prevents copying image data when reading and writing new information to the original data area. The raw format is used. Since data for running an instance is read directly from the image loaded, the instance can be started more quickly.

**Permission to use SSH key in instances.** This option is specified for Linux images. We strongly recommend using SSH-key authorization since this is the most secure option.

**The image will be used for bare metal instances.** This option should be selected if you plan to download the image for use with bare metal servers. The deep looping process for physical servers is slightly different from that of virtual servers. Setting this option is important to ensure that suitable properties are added to the image for use in the appropriate situation.

The operating system is installed on the image. You have the option to choose Linux or Windows.

**Type of firmware with which to boot the guest.** Gives you the option to choose BIOS or UEFI. For bare metal instances, we strongly recommend using UEFI for it to work properly on our servers. For virtual machines, this depends on your personal preference.

**Virtual Chipset type.** You have the option to choose between q35 and i440 virtual chipsets. The setting depends on the version of the operating system, the required functionality, and the supported virtual devices.

**Add tags.** Users can set custom tags according to the "Key" and "Value" principles to identify the images in the list correctly.

6. Click the **Next** button. Your image will be uploaded.