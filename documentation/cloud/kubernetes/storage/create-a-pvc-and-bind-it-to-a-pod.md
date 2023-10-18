---
title: create-a-pvc-and-bind-it-to-a-pod
displayName: Create a PVC and bind it to a pod
published: true
toc:
   --1--What are PV and PVC?: "what-are-pv-and-pvc"
   --1--Create a PVC: "create-a-pvc"
   --1--Bind a PVC to a pod: "bind-your-pvc-to-a-pod"
pageTitle: Understand and manage PVC | Gcore
pageDescription: Learn how to create a Persistent Volume Claim (PVC) for different disk types in Kubernetes to request storage and bind it to a pod.
---
# Create a PVC and bind to a pod
  
## What are PV and PVC?

A PV (PersistentVolume) in Kubernetes is a resource used to store data. It is attached to pods but has a separate lifecycle, specified by its reclaim policy. This policy determines if a PV will continue to exist or will be deleted when a pod attached to it gets destroyed.

A PV represents a piece of available storage. To use a PV, a user needs to create a PersistentVolumeClaim (PVC,) which is a request for storage. Kubernetes passes this request to a storage class, which creates PVs automatically in response to the PVC.

## Create a PVC

Before you create a PVC, you need to create a storage class with the required disk type. Gcore provides the following disk types:

<table>
   <tr>
      <td>Volume type</td>
      <td>Features</td>
   </tr>
   <tr>
      <td>standard</td>
      <td> Standard

Network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB.) The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.
      </td>
   </tr>
   <tr>
      <td>ssd_hiiops</td>
      <td> High IOPS SSD

High-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB.) The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.
      </td>
   </tr>
   <tr>
      <td>ssd_lowlatency</td>
      <td>SSD Low Latency

SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.
      </td>
</table>

To proceed with a PVC, follow the steps:

1. Make sure the required disk type is available in your region. To do so, go to the **Kubernetes** tab, select the required region and click **Create new cluster**. Click the **Volume type** field and check which options are available on the drop-down list. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/storage/create-a-pvc-and-bind-it-to-a-pod/1-available-volumes.jpg" alt="Create new cluster">

If you create a storage class with a volume type that is not available in your region, the PV won’t work.

2. Create a YAML file to create a storage class with the required disk type:

<code-block>
apiVersion: storage.k8s.io/v1  
kind: StorageClass  
metadata:  
  name: <span style="color:#FF5913">csi-sc-cinderplugin-hiiops</span>  
  annotations:  
    storageclass.kubernetes.io/is-default-class: "false"  
provisioner: cinder.csi.gcorelabs.com  
parameters:  
  type: <span style="color:#FF5913">ssd_hiiops</span>  
allowVolumeExpansion: true
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">`csi-sc-cinderplugin-hiiops`</span>: Storage class name  
- <span style="color:#FF5913">`ssd_hiiops`</span>: Disk type (`standard`, `ssd_hiiops`, or `ssd_lowlatency`)

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

You will get this output:

```
storageclass/<the name of the created storage class> created
```

3\. Create a YAML file to configure a PVC:

<code-block>
apiVersion: v1  
kind: PersistentVolumeClaim  
metadata:  
  name: <span style="color:#FF5913">block-pvc</span>  
spec:  
  storageClassName: <span style="color:#FF5913">csi-sc-cinderplugin-hiiops</span>  
  accessModes:  
    - ReadWriteOnce  
  resources:  
    requests:  
      storage: <span style="color:#FF5913">1Gi</span>
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">`block-pvc`</span>: PVC name  
- <span style="color:#FF5913">`csi-sc-cinderplugin-hiiops`</span>: Name of the created storage class  
- <span style="color:#FF5913">`1Gi`</span>: Storage size

4\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

You will get this output:

```
persistentvolumeclaim/<the name of the created PVC> created
```

This means you have successfully created a PVC with a storage class of the required disk type. To connect the PVC to your pods, refer to the section below.

## Bind your PVC to a pod

1\. Create a YAML file to bind the created storage class to your pod.

<code-block>
apiVersion: v1  
kind: Pod  
metadata:  
  name: <span style="color:#FF5913">mypod</span>
spec:  
  containers:  
    - name: <span style="color:#FF5913">myfrontend</span>
      image: nginx  
      volumeMounts:  
        - mountPath: <span style="color:#FF5913">"/var/www/html"</span>
          name: <span style="color:#FF5913">mypd</span>
  volumes:  
    - name: <span style="color:#FF5913">mypd</span>
      persistentVolumeClaim:  
        claimName: <span style="color:#FF5913">block-pvc</span>
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">`mypod`</span>: Pod name  
- <span style="color:#FF5913">`myfrontend`</span>: Container name  
- <span style="color:#FF5913">`"/var/www/html"`</span>: Destination inside the pod where to mount the storage class  
- <span style="color:#FF5913">`mypd`</span>: Storage class name  
- <span style="color:#FF5913">`block-pvc`</span>: Created PVC name

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

3\. You will get this output:

```
pod/<the pod name> created
```

This means you have successfully connected the PVC to your pod, and its containers can now access the storage.
