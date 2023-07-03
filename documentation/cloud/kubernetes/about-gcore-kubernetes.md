---
title: about-gcore-kubernetes
displayName: Overview
order: 10
published: true
toc:
---
# About Gcore Kubernetes

Kubernetes is a container management system that can be deployed and used on our servers. Features of our Kubernetes:

*   Cluster nodes are our <a href="https://gcore.com/cloud/compute-resources" target="_blank">virtual machines</a>.

*   Kubernetes-supported versions are 1.24, 1.25, 1.26, and 1.27. If a new version is released, you can upgrade to it without losing data by clicking just one button in your personal account.   
  
*   Support for bare-metal nodes, which helps improve performance and reduces latency even further.  
    
*   You have access to worker nodes, and only our administrators manage the master nodes where the Control planes are located. We restrict access to master nodes so that no one can make changes from the outside, and we can guarantee the stability of the service.  

*   You configure the number of worker nodes. Order as many nodes as you need.     
*   Autoscaling is available — the system will deploy new nodes and remove unnecessary ones depending on how much resources are required at the moment. You only need to specify the limits: how many minimum and maximum nodes can be in the cluster.     

*   Auto-healing is available — a function that automatically recovers failed nodes. It checks the status of the cluster nodes; if a non-working one is found, it initiates a replacement. 

*   PersistentVolumeClaim works with our <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes" target="_blank">volumes</a>  —- all data is stored on them. 
    
*   Ingress works via our <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">load balancers</a>.  
    
*   The implementation is based on Cluster API with high availability and service SLA.