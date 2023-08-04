---
title: install-and-set-up-the-nginx-ingress-controller
displayName: Install nginx Controller
order: 30
published: true
toc:
pageTitle: Install nginx Controller| Gcore
pageDescription: Learn how to install nginx Ingress Controller to effectively manage network traffic within a cluster.
---
# Install nginx Ingress Controller

When you install the nginx Ingress Controller, our system automatically creates a <a href="https://gcore.com/cloud/load-balancers" target="_blank">load balancer</a>. This load balancer acts as an entry point for incoming traffic. When traffic arrives, the load balancer forwards it to the Ingress Controller. The Ingress Controller is responsible for routing the traffic to the appropriate services within your Kubernetes cluster based on the rules defined in the Ingress manifests.

1\. Run the kubectl command to create a namespace:

```
kubectl create namespace ingress-nginx
```

2\. Run the command to add the helm repository for the nginx Controller:

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```

3\. Run the command to update the helm repository data:

```
helm repo update
```

4\. Run the command to install the Controller:

```
helm install ingress-nginx ingress-nginx/ingress-nginx  \
--namespace ingress \
--set controller.ingressClassResource.name=nginx
```

You have installed the nginx Ingress Controller. It will now automatically create a load balancer on your behalf.

5\. Use this command to get the IP address:

```
watch kubectl -n ingress get svc
```
Wait until the `<pending> state` of the `EXTERNAL-IP` column changes to the IP address.

The load balancer will be shown in your control panel in the **Load Balancers** section. The traffic will reach the nginx Ingress Controller via this balancer.
