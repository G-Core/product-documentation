---
title: upload-an-image-to-the-storage
displayName: Upload
published: true
order: 10
toc:
   --1--Image requirements: "image-requirements"
   --1--Upload: "upload-an-image"
pageTitle: Upload an image | Gcore
pageDescription: Learn how to upload images for virtual machines to Cloud storage.
---
# Upload an image to the storage

## Image requirements

1. **Format**. The image should be in one of the following formats:
- raw
- vhd
- vhdx
- vmdk
- vdi
- ploop
- qcow2
- aki
- ari
- ami

2. **VirtIO drivers**. If you are uploading an image that was previously downloaded from another cloud, the image should already have VirtIO drivers installed. However, if you have built your own image, please make sure to install and configure the VirtIO SCSI drivers.

3. **`cloud-init`**. If you are uploading an image that was previously downloaded from another cloud, the image should already have the `cloud-init` package installed. However, if you have built your own image, please make sure to install and configure the `cloud-init` package accordingly.

## Upload an image

1\. In the **Cloud** menu, select the desired project and region.

2\. Go to the **Images** tab and then proceed to **Import via URL**.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/3-menu.png" alt="Images tab ">

3\. Enter the image name and specify the URL from where the image will be downloaded.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/2-image-settings.png" alt="Upload an Image" width="300" height="225">

4. Turn on the **Show advanced options** toggle to access additional settings.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/1-advanced-settings.png" alt="Show advanced options " width="300" height="436">

Additional settings include:

- **Instance quick start**: If this option is on, the instances will be deployed faster with this image mounted. However, please note that you cannot delete this image if there are active instances created from this image.

Standard start vs quick start:

<table>
   <tr>
      <td>Start type</td>
      <td>Standard</td>
      <td>Quick</td>
   </tr>
   <tr>
      <td>Technology</td>
      <td>RBD Copy-On-Write</td>
      <td>RBD Copy-On-Write</td>
   </tr>
   <tr>
      <td>Image data</td>
      <td>All data is copied to a separate volume</td>
      <td>Image data is NOT copied when reading or writing new information, i.e. all changes and updates are applied directly to the original image</td>
   </tr>
   <tr>
      <td>Format</td>
      <td>qcow2</td>
      <td>raw</td>
   </tr>
   <tr>
      <td>Resource usage</td>
      <td>Resource-intensive</td>
      <td>Less resources used</td>
   </tr>
   <tr>
      <td>Image deletion</td>
      <td>The image can be deleted without affecting an instance operation</td>
      <td>The image can be deleted only when there are NO active instances created from this image</td>
   </tr>
</table>

- **Permission to use an SSH key in instances** (for Linux images): We recommend using SSH-key authorization for security reasons.

- **Image will be used for bare metal instances** Turn on this toggle, if you want to use the image for bare metal servers. This ensures that necessary properties are added to the image for the use in a bare metal environment, as the deep looping process for physical servers is different from that of virtual servers.

- **Operating system installed on the image**. Choose between Linux or Windows.

- **Type of firmware with which to boot the guest.** Select either BIOS or UEFI. For bare metal servers, UEFI is recommended for proper functionality. For virtual machines, the choice depends on your personal preference.

- **Virtual Chipset type.** Choose between q35 and i440 virtual chipsets based on the OS version, required functionality, and supported virtual devices.

5\. (optional) Add tags to identify images using the "Key" and "Value" principles.

6\. Click the **Next** button. Your image will be uploaded.
