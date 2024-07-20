---
title: advanced-cluster-autoscaler-settings
displayName: Advanced settings
published: true
order: 35
toc:
pageTitle: Advanced Cluster Autoscaler settings | Gcore
pageDescription: Learn how to configure advanced Cluster Autoscaler settings in a Kubernetes cluster.
---
# Advanced Cluster Autoscaler settings

You can configure cluster autoscaler settings to automatically adjust the size of your Kubernetes cluster based on the utilization of pods and nodes. This will help you optimize resource usage and maintain stable performance. 

You can adjust advanced settings <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster" target="_blank">during cluster creation</a> or in the settings of an existing cluster. Regardless of where you start, the configuration process remains the same. 

## View and configure advanced settings 

If you’re creating a new cluster, scroll down to the **Advanced settings** section. To configure the existing cluster, open the cluster overview and click the **Advanced settings** tab. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/advanced-cluster-autoscaler-settings/advanced-settings-section.png" alt="Advanced settings section in the cluster settings"  width="80%">

<alert-element type="info" title="Info">
 
If you want to reset the settings, click **Restore Default**. Be cautious when using this option because it will undo any advanced configurations you’ve set up for a cluster. 
 
</alert-element>

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/advanced-cluster-autoscaler-settings/restore-defaults.png" alt="Restore defaults button highlighted"  width="80%">

### Cluster scan interval 

Define how often the autoscaler will reevaluate the cluster to decide whether it needs to scale up (add nodes) or scale down (remove nodes).  

### Cluster expander 

Choose which node group should be scaled up when additional capacity is needed: 

* **random**: a random node group. 

* **most-pods**: a node group that will be able to schedule the highest number of unscheduled pods.  

* **least-waste**: a node group that will leave the least amount of unused CPU and memory resources. 

* **price**: a node group that is the most cost-effective.  

* **priority**: a node group based on a user-defined priority list. 

* **grpc**: use an external gRPC service to pick a node group. 

### Max node provision time 

Specify the maximum time that autoscaler will wait for a newly provisioned node to become fully operational. If the node isn’t ready within the specified time, the autoscaler will consider it failed.  

### New pod scale up delay 

If a new pod can’t be scheduled, this setting defines the time to wait before adding new nodes. 

### Max percentage of unready nodes 

The maximum percentage of nodes in the cluster that can be unready before the autoscaler stops creating new nodes. 

### Allowed count of unready nodes 

The maximum number of unready nodes that can exist before the autoscaler stops adding new nodes. 

### Enable scaledown (optional) 

Allow autoscaler to remove unused nodes in the cluster.  

### Post-addition scale-down delay 

The period during which the autoscaler will not remove any nodes after adding a new node to the cluster, even if they are unused.  

### Post-deletion scale-down delay 

The period during which the autoscaler will not remove any other unused nodes after a node is deleted from the cluster. 

### Failure scale-down delay 

The waiting period before the autoscaler attempts another scale-down operation after a previous attempt fails. 

### Unready node delay 

The waiting period before the autoscaler defines a node that's not fully operational as a candidate for scale-down. 

### Unneeded node delay 

The waiting period before the autoscaler defines a node as unneeded and scheduled for scale-down. 

### Scale-down utilization threshold 

The resource utilization level below which a node is considered unused and eligible for scale-down. 

### Max bulk deletion of empty nodes 

The number of empty nodes the autoscaler can delete at the same time.  

### Expendable pods priority cutoff 

Pods with priorities below this value are considered expendable and may be terminated during scale-down. 

For details on how to configure this setting, check out the <a href="https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/" target="_blank">official Kubernetes documentation</a>. 

### Max graceful termination time 

The maximum time that autoscaler will wait for pods to gracefully terminate before forcefully deleting them when scaling down a node. 

### Ignore Daemonsets utilization 

Ignore the resource utilization of pods managed by a DaemonSet when considering a node for scale-down. 

### Balance similar node groups 

Allow autoscaler to balance the size of node groups, which are similar in terms of instance types, resources, labels, or other characterists.  

### Skip nodes with system pods 

Don't allow scaling down critical system pods.  

### Skip nodes with local storage 

Don't scale down pods that use local storage. Enabling this setting helps to prevent potential data loss. 

### Skip nodes with custom controller pods 

Don't scale down nodes that run pods, which are managed by custom controllers. These custom controllers can be created by users or third-party extensions. 

<alert-element type="tip" title="Tip">
 
You can read more about these settings in the <a href="https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#what-are-the-parameters-to-ca" target="_blank">Kubernetes cluster-autoscaler documentation</a>. 
 
</alert-element>