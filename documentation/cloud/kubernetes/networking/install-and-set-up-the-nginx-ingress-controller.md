---
title: install-and-set-up-the-nginx-ingress-controller
displayName: Nginx ingress controller
order: 30
published: true
toc:
   --1--Install the controller: "install-the-nginx-ingress-controller"
   --1--Use the controller: "use-the-nginx-controller"
   --1--View an ingress IP address: "view-an-ingress-ip-address"
---
# Install and set up the Nginx ingress controller

This article will help you install and start using the nginx ingress controller. To learn about Kubernetes services, ingress, and ingress controllers, refer to the article "<a href="https://gcore.com/docs/cloud/kubernetes/networking/set-up-the-gcore-ingress-controller" target="_blank">Set up the Gcore ingress controller</a>".

Once you install the nginx ingress controller, our system automatically creates a <a href="https://gcore.com/cloud/load-balancers/" target="_blank">load balancer</a>. The traffic will go to that load balancer, which will then forward it to the nginx controller. After that, the nginx controller will distribute traffic across services within your cluster according to the rules specified in the ingress manifests.

## Install the nginx ingress controller

1\. Run the kubectl command to create a namespace for the nginx controller.

```
kubectl create namespace ingress-nginx
```

2\. Run the command to add the helm repository for the nginx controller.

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```

3\. Run the command to update the helm repository data.

```
helm repo update
```

4\. Run the command to install the controller.

```
helm install ingress-nginx ingress-nginx/ingress-nginx  \
--namespace ingress-nginx \
--set controller.ingressClassResource.name=nginx \
--set controller.ingressClassResource.controllerValue="example.com/ingress-nginx" \
--set controller.ingressClassResource.enabled=true \
--set controller.ingressClassByName=true \
--set controller.hostNetwork=true
```

You have installed the nginx controller. Now it will automatically create a load balancer on your behalf. The load balancer will be shown in your control panel in the Load Balancers section. The traffic will go to the nginx controller through this balancer. To start using the controller, you need to apply an Ingress manifest.

## Use the nginx controller

1\. Create a YAML file in any text or code editor to create an Ingress object:

<code-block>
apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: <span style="color:#FF5913">hello-world</span>  
spec:  
  ingressClassName: nginx  
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

- <span style="color:#FF5913">hello-world</span> is the name of the Ingress object  
- <span style="color:#FF5913">/about</span> is the URL path  
- <span style="color:#FF5913">hello-world-about</span> is the name of the service that will manage "/about" requests  
- <span style="color:#FF5913">80</span> is the port of the service that will manage "/login" requests  
- <span style="color:#FF5913">/login</span> is the URL path  
- <span style="color:#FF5913">hello-world-login</span> is the name of the service that will manage "/login" requests  
- <span style="color:#FF5913">80</span> is the port of the service that will manage "/login" requests

Make sure to add ```ingressClassName: nginx``` to the spec attributes.

2\. Run the kubectl command from the file directory.

```
kubectl apply -f <name of the created YAML-file>
```

You’ll get the output:

```
Ingress/<name of the created ingress object> created
```

Congratulations! You’ve created and applied an ingress object for the nginx ingress controller.

## View an ingress IP address

If you want to see an IP address of the load balancer through which the traffic comes, view it in your control panel in the Load Balancers section or run the command:

```
kubectl get ingress <ingress name>
```

You’ll get the output:

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/networking/install-and-set-up-the-nginx-ingress-controller/Output.png" alt="" width="80%">

The IP address is written in the ADDRESS column.