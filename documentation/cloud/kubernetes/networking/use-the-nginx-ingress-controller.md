---
title: use-the-nginx-ingress-controller
displayName: Use nginx Controller
published: true
order: 40
pageTitle: Use nginx Controller| Gcore
pageDescription: Learn how to use nginx Ingress Controller to effectively manage network traffic within a cluster.
---
# Use nginx Ingress Controller

To start using the controller, you need to apply an Ingress manifest.

1\. Create a YAML file to create an Ingress object:

<code-block>
apiVersion: extensions/v1beta1  
kind: Ingress  
metadata:  
  name: <span style="color:#FF5913">hello-world-ingress</span>  
spec:  
  ingressClassName: <span style="color:#FF5913">nginx</span>  
   rules:  
   - http:  
      paths:  
      - path: <span style="color:#FF5913">/</span>  
        backend:  
          serviceName: <span style="color:#FF5913">hello-world-svc</span>  
          servicePort: <span style="color:#FF5913">80</span>
</code-block>

Enter your custom values instead:

- <span style="color:#FF5913">hello-world-ingress</span>: Name of the Ingress object
- <span style="color:#FF5913">nginx</span>: Name of ingressClassResource
- <span style="color:#FF5913">/</span>: Default URL path  
- <span style="color:#FF5913">hello-world-svc</span>: Name of the Service that will manage the requests  
- <span style="color:#FF5913">80</span>: Port of the Service that will manage the requests

2\. Run the kubectl command.

```
kubectl apply -f <name of the created YAML-file>
```

You’ll get the output:

```
Ingress/<name of the created ingress object> created
```

This means you’ve successfully created and applied an Ingress object for the nginx Ingress Controller.