---
title: about-ingree-controllers
displayName: Overview
order: 5
published: true
toc:
   --2--Service: "what-is-a-service"
   --2--Ingress: "what-is-ingress"
   --2--Ingress controllers: "what-is-an-ingress-controller"
---
# About ingress controllers

To understand the concept of an ingress controller, it is important to have a clear understanding of a service and ingress. 

### What is a service?

A service in Kubernetes is an abstraction used to expose an application running on a set of pods. A service provides access to those pods through a single IP address. Pods can die, be recreated, and change their internal IP addresses, but they can still be accessed through the same service IP address. A service distributes the incoming traffic to all pods within it.

### What is ingress?

Ingress is a Kubernetes object represented as a set of rules used to route external traffic (ingress) across services inside a cluster. For example, you can map the "/login" route to a specific service in your cluster. So, when a user requests "yourwebsite.com/login", the traffic will be redirected to the service that is responsible for user logins.

To route external traffic to your application, you need three components:

1. Pods with containers that run your application.
2. A service that routes traffic to pods.
3. Ingress that routes traffic from external networks to service(s).

To fulfill ingress, you need an ingress controller.

### What is an ingress controller?

An ingress controller is a Kubernetes tool that reads ingress objects and creates a map of services in a cluster.
