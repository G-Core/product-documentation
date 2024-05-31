---
title: configure-nfs-csi-driver-for-kubernetes
displayName: Configure NFS CSI driver for Kubernetes
published: true
order: 20
pageTitle: Configure NFS CSI driver for Managed Kubernetes | Gcore
pageDescription: Learn how to connect a Managed Kubernetes cluster to the NFS Container Storage Interface (CSI) driver and manage NFS volumes as persistent volumes. 
---
# Configure NFS CSI driver for Managed Kubernetes 

Data stored in a Kubernetes container’s file system is temporary and not intended for long-term retention. When you replace or terminate a container, all information within it is deleted and can’t be restored. 

To prevent data loss, you can connect your Managed Kubernetes cluster to the NFS Container Storage Interface (CSI) driver. This driver connects <a href="https://gcore.com/docs/cloud/kubernetes/about-gcore-kubernetes" target="_blank">Kubernetes</a> and <a href="https://gcore.com/docs/cloud/file-shares/about-file-shares" target="_blank">Gcore File Shares</a>, allowing Kubernetes clusters to dynamically provision, attach, and manage NFS volumes as <a href="https://gcore.com/docs/cloud/kubernetes/storage/create-a-pvc-and-bind-it-to-a-pod" target="_blank">persistent volumes</a>. 

## Provision clusters with persistent NFS volumes

Kubernetes integration with the NFS driver is enabled by default, and the driver is installed in each cluster. 

<alert-element type="info" title="Info">

To provision persistent NFS volumes, ensure that a Managed Kubernetes cluster and File Share are created in the same project and connected to the same network and subnetwork.

</alert-element>

### Step 1. Create a Managed Kubernetes cluster

Create a cluster by following the instructions from our guide: <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster" target="_blank">Create a Managed Kubernetes cluster</a>. 

If you already have a Kubernetes cluster created, proceed to the next step.

### Step 2. Create a File Share

Create a File Share in the same project and region as your Kubernetes cluster: 

1\. In the Gcore Customer Portal, navigate to **Storage** > **File Shares**.

2\. Click **Create File Share**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/storage/add-file-share.png" alt="File Shares page with a highlighted button to create file share" width="80%">

3\. Configure File Share settings:

- **Basic settings**: Enter the name of the File Share and specify its size and protocol.

- **File Share network settings**: Select the private network and subnetwork that you will use for file sharing. Ensure that they match those selected in your Kubernetes cluster.

- **Access**: Click the **Add rule** button and specify the IP addresses of machines that should have access to the File Share, along with their access modes.

- (optional) **Add tags**: Add metadata to your File Share. 

The File Share should be set up within a few minutes.

### Step 3. Validate persistent NFS volume configuration

Run the following command to retrieve information about the storage classes configured in your Kubernetes cluster: 

```
kubectl get storageclass 
```

If everything’s set up correctly, the `gcore-nfs storage` class should be listed among other storage classes. 
