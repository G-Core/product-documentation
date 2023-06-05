---
title: create-a-pvc-and-bind-it-to-a-pod
displayName: Create a PVC and bind it to a pod
published: true
toc:
   --1--What are PV and PVC?: "what-are-pv-and-pvc"
   --1--Create a PVC: "create-a-pvc"
   --2--To connect to ‘standard’ disk-type storage: "create-a-pvc-to-connect-to-a-standard-disk-type-storage-class"
   --2--To connect to ‘ultra’, ‘cold’, or ‘ssd_hiiops’ disk-type storage: "create-a-pvc-to-connect-to-ultra-cold-ssd-hiiops-disk-type-storage"
   --1--Bind a PVC to a pod: "bind-your-pvc-to-a-pod"
---
# Create a PVC and bind to a pod
  
## What are PV and PVC?

A PV (Persistent Volume) in Kubernetes is a resource used to store data. It is attached to pods but have a separate lifecycle, specified by its Reclaim Policy. This policy determines if a PV will continue to exist or will be deleted when a pod attached to it gets destroyed.

A PV represents a piece of available storage. To use a PV, a user needs to create a persistent volume claim (PVC), which is a request for storage. Kubernetes passes this request to a storage class, which creates PVs automatically in response to the PVC.

## Create a PVC

There are four storage classes based on the disk type: standard, ultra, cold, and ssd\_hiiops. The standard disk-type storage class exists by default, so you simply need to create a default PVC. For any other disk type, you first have to create a storage class with the required disk type and then create a PVC.

### Create a PVC to connect to a standard disk-type storage class

1\. Create a YAML file to configure a PVC:

<code-block>
apiVersion: v1  
kind: PersistentVolumeClaim  
metadata:  
  name: <span style="color:#FF5913">block-pvc</span>  
spec:  
  accessModes:  
    - ReadWriteOnce  
  resources:  
    requests:  
      storage: <span style="color:#FF5913">1Gi</span>
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">block-pvc</span>—the PVC name  
- <span style="color:#FF5913">1Gi</span>—the required storage size

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the YAML file>.yaml
```

You will get the output:

```
persistentvolumeclaim/<the name of the created PVC> created
```

It means you have created a PVC with a standard disk-type storage class. To connect the PVC to your pods, refer to the [Bind a PVC to a pod](bind-your-pvc-to-a-pod) section.

### Create a PVC to connect to ultra/cold/ssd_hiiops disk-type storage

You can check the available disk types in different regions in the <a href="https://cloud.gcore.com/cloud/projects/list" target="_blank">Gcore Control panel</a> or via <a href="https://apidocs.gcore.com/cloud" target="_blank">an API request</a>.

1\. Create a YAML file to configure a storage class with the required disk type:

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

- <span style="color:#FF5913">csi-sc-cinderplugin-hiiops</span>—the storage class name  
- <span style="color:#FF5913">ssd_hiiops</span>—the required disk type

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

You will get the output:

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

- <span style="color:#FF5913">block-pvc</span>—your PVC name  
- <span style="color:#FF5913">csi-sc-cinderplugin-hiiops</span>—the name of the created storage class  
- <span style="color:#FF5913">1Gi</span>— the required storage size

4\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

You will get the output:

```
persistentvolumeclaim/<the name of the created PVC> created
```

It means you have created a PVC with a storage class of the required disk type. To connect the PVC to your pods, refer to the section below.

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

- <span style="color:#FF5913">mypod</span>—the pod name  
- <span style="color:#FF5913">myfrontend</span>—the container name  
- <span style="color:#FF5913">"/var/www/html"</span>—the destination inside the pod where to mount the storage class  
- <span style="color:#FF5913">mypd</span>—the storage class name  
- <span style="color:#FF5913">block-pvc</span>—the created PVC name

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML file>.yaml
```

3\. You will get the output:

```
pod/<the pod name> created
```

It means you have connected the PVC to your pod, and now its containers can access the storage.