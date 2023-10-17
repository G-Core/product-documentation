---
title: configure-file-shares
displayName: Configure
published: true
order: 20
pageTitle: Configure File Shares | Gcore
pageDescription: Learn how to configure Gcore File Shares, mount them to virtual machines and bare metal services, and change their size.
---
# Configure File Shares

**Please note**: Before you proceed with configuration, make sure you have enough quotas to create a file share. To increase quotas, send us a request according to <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">our guide</a>. The quotas for Files Shares are located on the **Storage** tab and include **File Share count** and **File Share size** (GiB) as shown below.

<img src="https://assets.gcore.pro/docs/cloud/file-shares/1.png" width=60% alt="Storage tab ">

## Configure file shares for Linux VMs and Bare Metal

**Step 0 (for bare metal servers only)**: Make sure the network that you want to use for sharing supports bare metal servers because they require a dedicated VLAN. Otherwise, create a new dedicated VLAN by switching the **Bare Metal Network** toggle when creating a new network.

<img src="https://assets.gcore.pro/docs/cloud/file-shares/2-1.png" width=60% alt="Bare Metal Network toggle">

**Please note**: To change the network interface of an existing bare metal server, you need to do so manually in the OS settings. 

**Step 1: Create a file share.**

1. In the **Cloud** menu, go to the **Storage** tab, select **File Shares** and click **Create File Share**.

<img src="https://assets.gcore.pro/docs/cloud/file-shares/3-1.png" width=60% alt="File Shares">

2. A new page will open. In **Basic settings**, enter the name of the file share, specify its size and protocol.

3. In the **File Share network settings**, select the private network and subnetwork that you will use for file sharing. 

4. In **Access**, click **Add rule** and specify the IP addresses of the machines that should have access to the file share and their access modes.

5. (optional) Add tags.

**Step 2: Connect to your server.**

Connect to your server via the <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">Control panel</a> or <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">SSH</a> and install the NFS client to enable your system to access the file share.

- For Ubuntu and Debian, use the following command: 
```
sudo apt -y install nfs-common
```
- For CentOS, use the following command:
```
sudo yum install nfs-utils
```

**Step 3: Mount the file share**.

1. Choose or create a file directory where you will mount the shared files.

2. Copy the mount command from your personal account. Go to the **Overview** tab of the required file share and copy the command from the field in the **File Share mount** section, as shown below.

<img src="https://assets.gcore.pro/docs/cloud/file-shares/4-1.jpg" alt="Mount the file share">

Run the command:

```
mount 0.0.0.0:/shares/share-d54589b8-132f-4de4-ae99-af5c6cdfdb9c /mount/path
```

Replace `/mount/path` with the path to the local file directory where you want to mount the file share.

Now you can access the content of the remote file share in the specified directory.

## Change size and unmount a file share

**Please note**: If you want to change the size of the file share, you first need to unmount it and then mount it again. 

To unmount a file share, use the following command:
```
umount -lf /your/share
```
To resize your file share, go to the **Overview** tab and click **Resize** as shown below. 

<img src="https://assets.gcore.pro/docs/cloud/file-shares/5-1.png" alt="Overview tab">
 

