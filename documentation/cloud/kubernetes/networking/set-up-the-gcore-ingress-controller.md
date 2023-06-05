---
title: set-up-the-gcore-ingress-controller
displayName: Gcore ingress controller
order: 20
published: true
toc:
   --1--What is an ingress controller: "what-is-an-ingress-controller"
   --2--What is a service?: "what-is-a-service"
   --2--What is ingress?: "what-is-ingress"
   --2--What is an ingress controller?: "what-is-an-ingress-controller"
   --1--Features of the Gcore ingress controller: "features-of-the-gcore-ingress-controller"
   --1--Create a service: "create-a-service"
   --1--Use the Gcore ingress controller: "use-the-gcore-ingress-controller"
   --1--View an ingress IP address: "view-an-ingress-ip-address"
---
# Set up the Gcore ingress controller
  
## What is an ingress controller?

To understand what an ingress controller is, you need to understand the following two entities: service and ingress. We’ll explain in sequence what service, ingress, and ingress controller are.

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

An ingress controller is a Kubernetes tool that reads ingress objects and creates a map of services in a cluster. This article will tell you how to use the Gcore ingress controller. If you prefer to use the Nginx ingress controller, refer to the article "<a href="https://gcore.com/docs/cloud/kubernetes/networking/install-and-set-up-the-nginx-ingress-controller" target="_blank">Install and set up the Nginx ingress controller</a>".

## Features of the Gcore ingress controller

Gcore provides an out-of-the-box ingress controller. Once you apply an ingress manifest, the controller creates a <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">Gcore load balancer</a> automatically. A load balancer is created for every single ingress object. A load balancer will serve as an entry point for all incoming traffic and then deliver it to pods based on rules specified in services and ingress objects.

So, if you have an application running in a Kubernetes cluster, you first need to provide access to its pods by creating a service and then provide access from the Internet by creating an ingress object.

## Create a service

1\. Create a YAML file in any text or code editor:

<code-block>
apiVersion: v1  
kind: Service  
metadata:  
  name: <span style="color:#FF5913">service-grafana</span>  
spec:  
  ports:  
  - port: <span style="color:#FF5913">80</span>  
    protocol: <span style="color:#FF5913">TCP</span>  
    targetPort: <span style="color:#FF5913">3000</span>  
  selector:  
    app: <span style="color:#FF5913">grafana</span>
</code-block>

Enter your custom values instead:


- <span style="color:#FF5913">service-grafana</span>—service name  
- <span style="color:#FF5913">80</span>—service port  
- <span style="color:#FF5913">TCP</span>—protocol which pods listen on  
- <span style="color:#FF5913">3000</span>—pod port  
- <span style="color:#FF5913">grafana</span>—application name

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML-file>
```

You’ll get the output:

```
service/<service name> created
```

Congratulations! You’ve created a service of the default ClusterIP type. For more information about other types of Kubernetes services, refer to the <a href="https://kubernetes.io/docs/concepts/services-networking/service/" target="_blank">official Kubernetes documentation</a>.

## Use the Gcore ingress controller

A Gcore ingress controller is pre-installed by default, so you only need to create an ingress object.

1\. Create a YAML file in any text or code editor:

<code-block>
apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: <span style="color:#FF5913">hello-world</span>  
spec:  
rules:  
  - http:  
    paths:  
    - path: <span style="color:#FF5913">/about</span>  
      backend:  
        serviceName: <span style="color:#FF5913">hello-world-about</span>  
        servicePort: <span style="color:#FF5913">80</span>  
    - path: <span style="color:#FF5913">/login</span>  
      backend:  
        serviceName: <span style="color:#FF5913">hello-world-login</span>  
        servicePort: <span style="color:#FF5913">80</span>
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">hello-world</span>—the name of the ingress object  
- <span style="color:#FF5913">/about</span>—URL path  
- <span style="color:#FF5913">hello-world-about</span>—the name of the service that will manage "/about" requests  
- <span style="color:#FF5913">80</span>—the port of the service that will manage "/login" requests
-  <span style="color:#FF5913">/login</span>—URL path  
- <span style="color:#FF5913">hello-world-login</span>—the name of the service that will manage "/login" requests  
- <span style="color:#FF5913">80</span>—the port of the service that will manage "/login" requests

2\. Run the kubectl command from the file directory:

```
kubectl apply -f <name of the created YAML-file>
```

You’ll get the output:

```
Ingress/<name of the created ingress object> created
```

Congratulations! You’ve created and applied an ingress object for the Gcore ingress controller. Now it will automatically create a Gcore load balancer on your behalf. It will be shown in your Control panel in the <a href="https://cloud.gcore.com/cloud/project/248631/networking/load_balancers" target="_blank">Load Balancers</a> section.

## View an ingress IP address

If you want to see an IP address of the load balancer through which the traffic comes, view it in the <a href="https://cloud.gcore.com/cloud/project/248631/networking/load_balancers" target="_blank">Control panel</a> or run the command:

```
kubectl get ingress <ingress name>
```

You’ll get the output:

<img src="https://support.gcore.com/hc/article_attachments/9569813559569/Output.png" alt="" width="70%">

The IP address is written in the ADDRESS column.