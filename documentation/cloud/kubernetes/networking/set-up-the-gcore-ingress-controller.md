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
  
  
  
  
  
  
  

What is an ingress controller?
------------------------------

To understand what an ingress controller is, you need to understand the following two entities: service and ingress. We’ll explain in sequence what service, ingress, and ingress controller are.

### What is a service?

A service in Kubernetes is an abstraction used to expose an application running on a set of pods. A service provides access to those pods through a single IP address. Pods can die, be recreated, and change their internal IP addresses, but they can still be accessed through the same service IP address. A service distributes the incoming traffic to all pods within it.

### What is ingress?

Ingress is a Kubernetes object represented as a set of rules used to route external traffic (ingress) across services inside a cluster. For example, you can map the “/login” route to a specific service in your cluster. So, when a user requests “yourwebsite.com/login”, the traffic will be redirected to the service that is responsible for user logins.

To route external traffic to your application, you need three components:

1.  Pods with containers that run your application.
2.  A service that routes traffic to pods.
3.  Ingress that routes traffic from external networks to service(s).

To fulfill ingress, you need an ingress controller.

### What is an ingress controller?

An ingress controller is a Kubernetes tool that reads ingress objects and creates a map of services in a cluster. This article will tell you how to use the Gcore ingress controller. If you prefer to use the Nginx ingress controller, refer to the article [“Set up the nginx ingress controller”](https://support.gcore.com/hc/en-us/articles/9570888308881).

Features of the Gcore ingress controller
----------------------------------------

Gcore provides an out-of-the-box ingress controller. Once you apply an ingress manifest, the controller creates a [Gcore load balancer](https://gcore.com/support/articles/360004523578/) automatically. A load balancer is created for every single ingress object. A load balancer will serve as an entry point for all incoming traffic and then deliver it to pods based on rules specified in services and ingress objects.

So, if you have an application running in a Kubernetes cluster, you first need to provide access to its pods by creating a service and then provide access from the Internet by creating an ingress object.

Create a service
----------------

1. Create a YAML file in any text or code editor:

apiVersion: v1  
kind: Service  
metadata:  
  name: **service-grafana**  
spec:  
  ports:  
  - port: **80**  
    protocol: **TCP**  
    targetPort: **3000**  
  selector:  
    app: **grafana**

Enter your custom values instead:

**service-grafana**—service name  
**80**—service port  
**TCP**—protocol which pods listen on  
**3000**—pod port  
**grafana**—application name

2. Run the kubectl command from the file directory:

kubectl apply -f <name of the created YAML-file>

You’ll get the output:

service/<service name> created

Congratulations! You’ve created a service of the default ClusterIP type. For more information about other types of Kubernetes services, refer to the [official Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/service/).

Use the Gcore ingress controller
--------------------------------

A Gcore ingress controller is pre-installed by default, so you only need to create an ingress object.

1. Create a YAML file in any text or code editor:

apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: **hello-world**  
spec:  
rules:  
  - http:  
    paths:  
    - path: **/about**  
      backend:  
        serviceName: **hello-world-about**  
        servicePort: **80**  
    - path: **/login**  
      backend:  
        serviceName: **hello-world-login**  
        servicePort: **80**

Enter your custom values instead:

**hello-world**—the name of the ingress object  
**/about**—URL path  
**hello-world-about**—the name of the service that will manage “/about” requests  
**80**—the port of the service that will manage “/login” requests**  
/login**—URL path  
**hello-world-login**—the name of the service that will manage “/login” requests  
**80**—the port of the service that will manage “/login” requests

2. Run the kubectl command from the file directory:

kubectl apply -f <name of the created YAML-file>

You’ll get the output:

Ingress/<name of the created ingress object> created

Congratulations! You’ve created and applied an ingress object for the Gcore ingress controller. Now it will automatically create a Gcore load balancer on your behalf. It will be shown in your control panel in the [Load Balancers](https://cloud.gcore.com/cloud/project/248631/networking/load_balancers) section.

View an ingress IP address
--------------------------

If you want to see an IP address of the load balancer through which the traffic comes, view it in the [control panel](https://cloud.gcore.com/cloud/project/248631/networking/load_balancers) or run the command:

kubectl get ingress <ingress name>

You’ll get the output:

<img src="https://support.gcore.com/hc/article_attachments/9569813559569/Output.png" alt="Output.png">

The IP address is written in the ADDRESS column.