---
title: create-a-container
displayName: Create a container
published: true
order: 10
toc:
   --1--Step 1. Add a container image: "step-1-add-a-container-image"
   --1--Step 2. Specify port: "step-2-specify-port"
   --1--Step 3. Choose container configuration: "step-3-choose-container-configuration"
   --1--Step 4. Configure autoscaling: "step-4-configure-autoscaling"
   --1--Step 5. Specify container lifetime: "step-5-specify-container-lifetime"
   --1--Step 6 (optional). Add variables: "step-6-optional-add-environment-variables"
   --1--Step 7 (optional). Configure API keys: "step-7-optional-configure-authentication-via-API"
   --1--Step 8. Finalize configuration: "step-8-finalize-container-configuration"  
pageTitle: Create Containers in the Customer Portal | Gcore
pageDescription: A comprehensive step-by-step guide on how to create containers in the Customer Portal.
---
# Create a container

Deploy and run your containerized application in the Cloud, without managing any underlying infrastructure.  

## Step 1. Add a container image

<alert-element type="tip" title="Tip">
 
If you don’t have sufficient resources to a create a Container, request <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">quota increase</a>. 
 
</alert-element>

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Container as a Service**. 

2\. Click **Create container**.

<img src="https://assets.gcore.pro/docs/cloud/caas/caas-page.png" alt="CaaS page in the Customer Portal" width="80%">

3\. In the **Container image** section, select the image type: **public** or **private**. The difference between them is that a private image is secured with credentials. 

4\. Enter your image URL. For example, nginx:latest. For a private image, enter the URL in the format `https://registry.mysite.com`. 

5\. (Optional) Specify registry credentials. If you selected private image in the previous step, enter credentials for accessing that image. If you’ve already added createntials to the Customer Portal, choose them from the Credentials dropdown.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/add-container-image.png" alt="Container image settings" width="80%">

If you have no saved credentials, add them as follows: 

 * **Image registry name**: Registry name that will be displayed in the Credentials dropdown. 
 * **Image registry URL**: Link to the location where your application is stored. 
 * **Image registry username**: Username you use to access the storage location of your application. 
 * **Image registry password**: Password you use to access the storage location of your application.  

To save the new credentials, click **Create credentials**. 

(Optional) Set startup command. Enable the toggle if you want to execure a specific command when your container is initiated.  

## Step 2. Specify port  

In the **Port** section, specify the port for connection to your container. 

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/specify-port.png" alt="Container port" width="80%">

<alert-element type="info" title="Info">
 
Currently, we support only one port for the container. If you need to add additional data, create a separate container. 
 
</alert-element>

## Step 3. Choose container configuration 

Select the required MB of memory and mCPU (up to 2260 mCPU and 4096 MB). This configuration will be used for the deployed Kubernetes pod, where your container will be placed after creation.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/container-configuration.png" alt="Container configuration" width="80%">

## Step 4. Configure autoscaling 

In the **Limits of autoscaling section**, enter the range for the number of nodes you want to maintain under Minimum pods and Maximum pods.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/autoscaling-limits.png" alt="Container autoscaling limits" width="80%">

To ensure more efficient use of computational resources and consistent model performance, define scaling thresholds for CPU, RAM, GPU, GPU RAM, and HTTP requests resource utilization. 

Click **Add trigger** to view and modify current thresholds: 

* The minimum setting is 1% of the resource capacity. Only **HTTP requests** trigger can scale pods to and from 0. 

* The maximum setting is 100% of the resource capacity. 

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/autoscaling-thresholds.png" alt="Container autoscaling thresholds" width="80%">

By default, the autoscaling parameters are set to 80% but you can enter any percentage within the specified range.  

You can combine any triggers or use a single one. 

<alert-element type="warning" title="Warning">
 
When setting up HTTP scaling, use small values with caution as it might affect the scale window—the time (in seconds) it takes to aggregate HTTP request rates for making scaling decisions. Low scaling value might cause unexpected scale triggers. 
 
</alert-element>

## Step 5. Specify container lifetime 

Enter the number of seconds after which a pod will be deleted when there are no requests to your pod. For example, if you enter 600, the pod will be deleted in 600 seconds—equal to ten minutes.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/container-lifetime.png" alt="Container lifetime settings" width="80%">

<alert-element type="tip" title="Tip">

If you specify 0, the container will take approximately one minute to scale down. 
 
</alert-element>

## Step 6 (optional). Add environment variables 

(Optional) If you want to add metadata to your container, create variables in a form of key-value pairs. These variables will only be used in the environment of the created container.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/variables.png" alt="Enviroment variables settings" width="80%">

## Step 7 (optional). Configure authentication via API 

To protect your container endpoints from unauthorized access, enable the API Key authentication feature. Either select an existing API key or create a new one.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/api-key.png" alt="API keys settings" width="80%">

## Step 8. Finalize container configuration 

Specify the container name (this will be displayed in the Customer Portal) and additional information if needed.

<img src="https://assets.gcore.pro/docs/cloud/caas/add-a-container/container-details.png" alt="Container details settings" width="80%">

In the top-right corner of the screen, click **Create container**. After a few minutes, the initial setup will be finished and the container will be launched. 