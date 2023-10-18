---
title: install-an-os-from-iso-in-vmmanager-6
displayName: Install an OS from ISO in VMmanager 6
published: true
order: 32
toc:
pageTitle: Install an OS from ISO in VMmanager 6| Gcore
pageDescription: Learn how to install an OS from an ISO image for a virtual server in VMManager 6.
---
# Install OS from ISO on in VMmanager 6

An ISO image is a disk file image that contains an exact copy of the data and file structure from a specific optical disc such as a CD, DVD or Blu-ray. Files in an ISO image may include operating systems, programs, games, or any other data that can be written to an optical disc. This guide will describe how an ISO image can be mounted to your virtual server.

## ISO requirements

Before uploading the ISO file, please make sure it meets the relevant requirements:

- The maximum image size: ~8 GB (8192 MB),
- Only 1 ISO image can be uploaded.

## ISO restrictions 

If you are installing an OS on a VM from an ISO image, then you should be aware that the following actions will not be available to you:

- root password editing;
- creating new ISO images;
- running scripts in your VM (while the ISO image is being loaded).

## Install an OS from an ISO image

1. Open the control panel. 

Select **Virtual private servers**, click selected server and go **To panel** (if you’re using the old interface).

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-iso-image/1-to-panel-old-interface.png" alt="Virtual private servers">

If you’re using the new interface, please select **Products/Services** section, then choose **Virtual private servers** and click to **To Panel**.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-iso-image/2-to-panel-new-interface.png" alt="To Panel">

2. In the VMmanager panel, select the three-dot menu and then select the **Mount ISO-image**. 

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-iso-image/3-mount-iso.png" alt="Mount ISO-image">

3. Enter the link to the file you want to upload to the current directory, where the ISO image is available. The image can be available via HTTP(S) or FTP. Optionally, you can specify tags for the connected OS if this VM needs to run scripts. The script will run on the VM if at least one of its tags matches the OS tag. 

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-iso-image/4-url-tags.png" width=70% alt="upload">

4. Select **Download and connect**.

Now you can use the server with the operating system that you installed from an ISO image. To connect to your server via VNC, you can refer to <a href="https://gcore.com/docs/hosting/virtual-servers/manage/connect/connect-to-a-virtual-server-via-vnc" target="_blank">our PD article</a>. 