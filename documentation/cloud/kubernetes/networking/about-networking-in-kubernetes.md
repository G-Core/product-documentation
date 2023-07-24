---
title: about-networking-in-kubernetes
displayName: Overview
order: 5
published: true
toc:
   --2--Service: "what-is-a-service"
   --2--Ingress: "what-is-ingress"
   --2--Ingress Controllers: "what-is-an-ingress-controller"
pageTitle: Networking in Kubernetes | Gcore
pageDescription: Learn about Kubernetes networking essentials—Services, Ingress, and Ingress Controllers—to effectively manage network traffic within a cluster.
---
# About networking in Kubernetes

To effectively manage network traffic within a cluster, it is important to have a clear understanding of Services, Ingress, and Ingress Controllers. 

### What is a Service?

A Service in Kubernetes is an abstraction used to expose an application running on a set of pods. A Service provides access to those pods through a single IP address. Pods can die, be recreated, and change their internal IP addresses, but they can still be accessed through the same service IP address. A Service distributes the incoming traffic to all pods within it.

### What is Ingress?

Ingress is a Kubernetes object represented as a set of rules used to route external traffic (ingress) across services inside a cluster. For example, you can map the "/login" route to a specific service in your cluster. So, when a user requests "yourwebsite.com/login", the traffic will be redirected to the service that is responsible for user logins.

To route external traffic to your application, you need three components:

1. Pods with containers that run your application.
2. A Service that routes traffic to pods.
3. Ingress that routes traffic from external networks to service(s).

To fulfill ingress, you need an Ingress Controller.

### What is an Ingress Controller?

An Ingress Controller is a Kubernetes tool that reads ingress objects and creates a map of services in a cluster.
