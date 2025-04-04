---
title: about-gcore-kubernetes
displayName: Overview
order: 10
published: true
toc:
pageTitle: Learn to use Gcore Managed Kubernetes | Gcore
pageDescription: Explore Gcore Managed Kubernetes. Powerful features, Bare Metal support, autoscaling, data storage, and high availability for seamless container orchestration.
---
# About Gcore Managed Kubernetes

Kubernetes is a container management system that can be deployed and used on our servers. Features of our Managed Kubernetes service include the following:

- **Bare Metal support**. With Gcore, you can deploy the cluster nodes not only on <a href="https://gcore.com/cloud/compute-resources" target="_blank">Virtual Machines (VMs)</a>, but also directly on our <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">Bare Metal servers</a>. This allows you to improve performance and latency even further and avoid the noisy neighbors of VMs. For more information, refer to <a href="https://gcore.com/docs/cloud/kubernetes/bare-metal-kubernetes" target="_blank">our article</a>.
- **Secure master node management**. You have access to your worker nodes, and our administrators alone manage the master nodes where the control planes are located. We restrict access to master nodes to guarantee security and stability, meaning that nobody unwanted can make changes and we can guarantee the stability of the service.
- **Flexible worker node configuration**. You have complete control over the number of worker nodes in your cluster. Order as many nodes as you need with just one click.  
- **Autoscaling**. The system deploys new nodes and removes unnecessary ones based on real-time resource demands. You just set the minimum and maximum node limits, and the cluster will adapt accordingly. For more information, refer to our <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling product docs</a>
- **Self-healing**. The service constantly monitors the health of your nodes and automatically recovers failed ones if necessary.
- **Data storage**. You can use PersistentVolumeClaims (PVC) with our <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes" target="_blank">volumes</a> to store all your data. For details, check out the <a href="https://gcore.com/docs/cloud/kubernetes/storage/create-a-pvc-and-bind-it-to-a-pod" target="_blank">relevant product docs</a>.
- **Networking**. You can manage the routing of networking traffic for your applications by configuring the Nginx ingress controller. We explain how in <a href="https://gcore.com/docs/cloud/kubernetes/networking/install-and-set-up-the-nginx-ingress-controller" target="_blank">our article</a>.      
- **High availability and SLA**. Our Managed Kubernetes service is built on the Cluster API, providing high availability and a 99.99% SLA guarantee.

## Shared Responsibilities

As the list above shows, the managed Kubernetes service takes care of many, but not all, of the tasks required for running services and apps on Kubernetes. That's why Gcore follows a shared responsibility model.

**Gcore's responsibilities:**

* Managing the control plane.
* Ensuring high availability and SLA's
* Ensuring worker nodes are provisioned successfully and according to your settings.

**Your responsibilities:**

* Managing your SSH keys according to industry best practices.
* Ensuring your services and apps work with your chosen settings and configurations.
