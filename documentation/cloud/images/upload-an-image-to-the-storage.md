---
title: upload-an-image-to-the-storage
displayName: Upload
published: true
order: 10
toc:
   --1--Image requirements: "image-requirements"
   --1--Upload: "upload-an-image"
pageTitle: Upload an image | Gcore
pageDescription: Learn how to upload images for Virtual Machines to Cloud storage.
---
# Upload an image to the storage

You can upload images to the cloud storage by following a few simple steps, ensuring the correct formats and settings are in place for a successful upload and easy management.

## Image requirements

Before uploading an image to the storage, check that it meets the required format, driver, and package requirements.

### Supported formats  

The uploaded image must be in one of the following formats:

<table>
   <tr>
      <td>raw</td>
      <td>Uncompressed image format</td>
   </tr>
   <tr>
      <td>vhd / vhdx</td>
      <td>Microsoft Hyper-V formats</td>
   </tr>
   <tr>
      <td>vdi</td>
      <td>VirtualBox disk image</td>
   </tr>
   <tr>
      <td>ploop</td>
      <td>Parallels storage format</td>
   </tr>
   <tr>
      <td>qcow2</td>
      <td>QEMU copy-on-write format</td>
   </tr>
   <tr>
      <td>aki / ari / ami</td>
      <td>Amazon Machine Image formats</td>
   </tr>
</table>

### VirtIO drivers  

If you upload an image previously downloaded from another cloud, the image should already have VirtIO drivers installed. However, if you have built your own image, please install and configure the VirtIO SCSI drivers.

### cloud-init  

If you upload an image previously downloaded from another cloud, the image should already have the `cloud-init` package installed. However, if you have built your own image, please install and configure the `cloud-init` package accordingly.

## Upload an image

1. In the **Cloud** menu, select the desired project and region.

2. Go to the **Images** tab and then proceed to **Import via URL**.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/click-import-via-url.png" alt="Gcore Customer Portal - Import an image via URL in the Images section" width="800">

3. Select the Resource type:
   - Virtual Instances
   - Bare Metal
   - Virtual GPU Clusters
   - Baremetal GPU Clusters

4. Enter the image name and specify the URL from where the image will be downloaded.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/enter-url-of-your-image.png" alt="Enter the image name and URL for uploading" width="800">

5. Choose the architecture of the image based on the processor type where it will run: select x86 for traditional CISC processors like Intel or AMD, or ARM for RISC-based processors such as ARM CPUs.

6. If **VM quick start** toggle is on, the Virtual Machines will be deployed faster with this image mounted. However, please note that you cannot delete this image if there are active Virtual Machines created from this image.

**Standard start vs quick start:**

<table>
   <tr>
      <td>Start type</td>
      <td>Standard</td>
      <td>Quick</td>
   </tr>
   <tr>
      <td>Technology</td>
      <td>RBD copy-on-write</td>
      <td>RBD copy-on-write</td>
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
      <td>The image can be deleted without affecting a Virtual Machine's operation</td>
      <td>The image can be deleted only when there are NO active Virtual Machines created from this image</td>
   </tr>
</table>

7. Specify the permission level for SSH key usage in instances created from this image. You can choose **Allow** to make SSH key usage optional, **Deny** to prohibit SSH key usage entirely, or **Required** to mandate SSH key usage for secure instance access. We recommend using SSH-key authorization for security reasons. 

8. Select the OS pre-installed on the image, like Linux or Windows Server, to suit your deployment needs and ensure smooth operation.

9. Select firmware type. For Bare Metal servers, UEFI is recommended for proper functionality. For Virtual Machines, the choice depends on your personal preference. The firmware type is determined by the selected product. Virtual Instances and GPU virtual clusters support both UEFI and BIOS, while Bare Metal servers and GPU baremetal clusters are restricted to UEFI for compatibility. Choose UEFI for modern systems or BIOS for legacy setups.

10. Choose the virtual chipset type between q35 and i440 virtual chipsets based on the OS version, required functionality, and supported virtual devices.

11. Add tags (optional) to identify images using the "Key" and "Value" principles. Enable this option to add metadata tags to your image, helping you efficiently organize and identify resources.

12. Click the **Upload** button. Your image will be uploaded.

<img src="https://assets.gcore.pro/docs/cloud/images/upload-an-image-to-the-storage/click-upload.png" alt="Click the Upload button to finalize image import" width="800">
