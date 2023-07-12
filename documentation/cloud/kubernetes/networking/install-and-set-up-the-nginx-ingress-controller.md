---
title: install-and-set-up-the-nginx-ingress-controller
displayName: Nginx ingress controller
order: 30
published: true
toc:
   --1--Install: "install-the-nginx-ingress-controller"
   --1--Use: "use-the-nginx-controller"
   --1--View an ingress IP address: "view-an-ingress-ip-address"
---
# Install and set up the Nginx Ingress Controller

Once you install the Nginx Ingress Controller, our system automatically creates a <a href="https://gcore.com/cloud/load-balancers/" target="_blank">load balancer</a>. The traffic will go to that load balancer, which will then forward it to the Nginx Controller. After that, the Nginx Controller will distribute traffic across services within your cluster according to the rules specified in the ingress manifests.

## Install the Nginx Ingress Controller

1\. Run the kubectl command to create a namespace for the Nginx Controller.

```
kubectl create namespace ingress-nginx
```

2\. Run the command to add the helm repository for the Nginx Controller.

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```

3\. Run the command to update the helm repository data.

```
helm repo update
```

4\. Run the command to install the Controller.

```
helm install ingress-nginx ingress-nginx/ingress-nginx  \
--namespace ingress-nginx \
--set controller.ingressClassResource.name=nginx \
--set controller.ingressClassResource.controllerValue="example.com/ingress-nginx" \
--set controller.ingressClassResource.enabled=true \
--set controller.ingressClassByName=true \
--set controller.hostNetwork=true
```

You have installed the Nginx Controller. Now it will automatically create a load balancer on your behalf. The load balancer will be shown in your control panel in the Load Balancers section. The traffic will go to the nginx controller through this balancer. To start using the controller, you need to apply an Ingress manifest.

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
- <span style="color:#FF5913">hello-world-about</span> is the name of the Service that will manage "/about" requests  
- <span style="color:#FF5913">80</span> is the port of the Service that will manage "/login" requests  
- <span style="color:#FF5913">/login</span> is the URL path  
- <span style="color:#FF5913">hello-world-login</span> is the name of the Service that will manage "/login" requests  
- <span style="color:#FF5913">80</span> is the port of the Service that will manage "/login" requests

Make sure to add ```ingressClassName: nginx``` to the spec attributes.

2\. Run the kubectl command from the file directory.

```
kubectl apply -f <name of the created YAML-file>
```

You’ll get the output:

```
Ingress/<name of the created ingress object> created
```

Congratulations! You’ve created and applied an Ingress object for the Nginx Ingress Controller.

## View an ingress IP address

If you want to see an IP address of the load balancer through which the traffic comes, view it in your control panel in the Load Balancers section or run the command:

```
kubectl get ingress <ingress name>
```

You’ll get the output:

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/networking/install-and-set-up-the-nginx-ingress-controller/Output.png" alt="" width="80%">

The IP address is written in the ADDRESS column.