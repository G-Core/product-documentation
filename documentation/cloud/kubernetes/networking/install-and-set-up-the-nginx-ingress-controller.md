---
title: install-and-set-up-the-nginx-ingress-controller
displayName: Nginx ingress controller
order: 30
published: true
toc:
   --1--Install the controller: "install-the-nginx-ingress-controller"
   --2--Use the controller: "use-the-nginx-controller"
   --1--View an ingress IP address: "view-an-ingress-ip-address"
---
# Install and set up the nginx ingress controller

This article will help you install and start using the nginx ingress controller. To learn about Kubernetes services, ingress, and ingress controllers, refer to the article [“Set up the Gcore ingress controller”](https://gcore.com/support/articles/9570322632593/).

Once you install the nginx ingress controller, our system automatically creates a [load balancer](https://gcore.com/cloud/load-balancers/). The traffic will go to that load balancer, which will then forward it to the nginx controller. After that, the nginx controller will distribute traffic across services within your cluster according to the rules specified in the ingress manifests.

Install the nginx ingress controller
------------------------------------

1. Run the kubectl command to create a namespace for the nginx controller.

kubectl create namespace ingress-nginx

2. Run the command to add the helm repository for the nginx controller.

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

3. Run the command to update the helm repository data.

helm repo update

4. Run the command to install the controller.

helm install ingress-nginx ingress-nginx/ingress-nginx  \\  
\--namespace ingress-nginx \\  
\--set controller.ingressClassResource.name=nginx \\  
\--set controller.ingressClassResource.controllerValue="example.com/ingress-nginx" \\  
\--set controller.ingressClassResource.enabled=true \\  
\--set controller.ingressClassByName=true \\  
\--set controller.hostNetwork=true

You have installed the nginx controller. Now it will automatically create a load balancer on your behalf. The load balancer will be shown in your control panel in the Load Balancers section. The traffic will go to the nginx controller through this balancer. To start using the controller, you need to apply an Ingress manifest.

### Use the nginx controller

1. Create a YAML file in any text or code editor to create an Ingress object:

apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: **hello-world**  
spec:  
  ingressClassName: nginx  
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

**hello-world** is the name of the Ingress object  
**/about** is the URL path  
**hello-world-about** is the name of the service that will manage “/about” requests  
**80** is the port of the service that will manage “/login” requests  
**/login** is the URL path  
**hello-world-login** is the name of the service that will manage “/login” requests  
**80** is the port of the service that will manage “/login” requests

Make sure to add “**ingressClassName: nginx**” to the spec attributes.

2. Run the kubectl command from the file directory.

kubectl apply -f <name of the created YAML-file>

You’ll get the output:

Ingress/<name of the created ingress object> created

Congratulations! You’ve created and applied an ingress object for the nginx ingress controller.

View an ingress IP address
--------------------------

If you want to see an IP address of the load balancer through which the traffic comes, view it in your control panel in the Load Balancers section or run the command:

kubectl get ingress <ingress name>

You’ll get the output:

<img src="https://support.gcore.com/hc/article_attachments/9570885113745/Output.png" alt="Output.png">

The IP address is written in the ADDRESS column.