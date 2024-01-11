---
title: about-function-as-a-service
displayName: Function as a Service
published: true
order: 10
toc:
   --1--What is FaaS?: "what-is-faas"
   --1--How it works: "how-it-works"
   --1--Use cases: "use-cases"
   --1--Features: "features-of-gcore-faas"
   --1--Billing: "billing"
pageTitle: Function as a Service | Gcore
pageDescription: Learn about Function-as-a-Service (FaaS) and its benefits. Explore Gcore FaaS features and runtime environments.
---
# About Function as a Service
  
## What is FaaS?

Function-as-a-Service (FaaS) is a cloud service that lets users run code without dealing with the underlying infrastructure. A FaaS provider saves the code to their cloud resources and runs it when requested.

FaaS is based on serverless computing, in which you can use computing resources such as CPU and memory without actually renting servers on a cloud. You don’t have to choose an operating system, configure networking, patch dependencies, or scale capacity up and down. The necessary number of resources is allocated to you automatically as they are needed.

## How it works

1\. You write the code of the app or app component that you want to run automatically via FaaS.

2\. In your Gcore <a href="https://cloud.gcore.com/cloud" target="_blank">Control panel</a> or in an API request, you create a function and insert your code into it.

3\. Our system deploys a Kubernetes pod exclusively for this function. You don’t have to worry about the pod or other infrastructure resources. We create, manage, and monitor it for you.

4\. Once the pod for your function is ready, you’ll see the function in the list. It is shown with its HTTP endpoint, which is the address of the function.

5\. When you or your users request this endpoint, the system automatically invokes the pod, and it runs the function. As a result, you will get the desired code output.

Under the hood, pods with functions are operated by Kubernetes. When you send your code to us, Kubernetes saves it and assigns a pod for it. You can set the minimum and maximum number of pods.

If the minimum number of pods is 0, the zero-scaler comes into play. It monitors requests for a given function. If the function is not requested, the controller keeps resources at zero; the pod consumes 0 mCPU and 0 GB RAM. When the controller receives a request, it triggers the associated pod and allocates the computing resources required for the function to be executed. It takes around three seconds for a pod to start and the function to become active. It starts consuming resources and processing requests. If more requests come than the pod can handle, the system deploys additional pods until it reaches the maximum limit. After the last request is executed, the function remains active for the timeout period. By default, it is 60 seconds. You can also set a custom value. If no other requests come during this period, the system brings the resources back to 0, switches the function to standby mode, and stops charging you.

If the minimum number of pods is more than 0, the auto-scaler takes control. It keeps this minimum number of pods constantly running. They consume resources 24/7, even if the function is not requested. You are also billed 24/7 according to your pod configuration. When the first request comes, the pod(s) doesn’t need extra time for the cold start. The request is processed immediately. When the auto-scaler receives more requests than the minimum number of pods can handle, it’ll scale the pods up to adjust to the increased workload. After the timeout period, the auto-scaler destroys only additional pods, keeping the minimum number.

## Use cases

FaaS is the best solution to:

- **Save costs on deploying a simple application.** If your web app has a few visitors a day, and your server stands idle from time to time, you can switch to FaaS. You’ll pay only when your application is requested.
- **Expand the functionality of your application.** You can organize your application as a set of independently deployable services—microservices—integrated via HTTP API or Webhooks and run by FaaS.
- **Change individual components of your application.** Functions allow the code of independent app components to be changed on the fly without stopping the app.
- **Reduce time-to-market.** FaaS allows you to focus only on your application code without spending time on infrastructure management, so you can release your product as quickly as possible.
- **Adjust resources to traffic surges on the fly.** If you have frequent traffic surges, functions will help to automatically allocate the required number of computing resources.

## Features of Gcore FaaS

Our FaaS supports several runtime environments:

- C# (6.0, 7.0)
- Java (11, 17, 21)
- Node.js (18, 19, 20)
- Python (3.8, 3.9, 3.10)
- Go (1.20, 1.21)

You can find available runtimes and locations on <a href="https://gcore.com/cloud/faas" target="_blank">our website</a> and the Gcore <a href="https://cloud.gcore.com/cloud" target="_blank">Control panel</a>.

You can manage your functions via the Gcore <a href="https://cloud.gcore.com/cloud" target="_blank">Control panel</a> and <a href="https://api.gcore.com/docs/cloud" target="_blank">REST API</a>.

You can set the pod lifetime, the limit of additional pods, and environmental variables.

All data in our Cloud is protected from unauthorized access and modifications according to the PCI DSS and ISO 27001 certification. DDoS protection is available by default. We also protect all your data from loss using three-factor SAN replication and disaster recovery.
