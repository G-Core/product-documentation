---
title: manage-containers 
displayName: Manage containers
published: true
order: 30
toc:
   --1--Container statuses: "container-statuses"
   --1--Container settings: "container-settings"
   --2--Overview: "overview"
   --2--Image and port: "image-port"
   --2--Container configuration: "container-configuration"
   --2--API key authentication: "api-key-authentication" 
   --2--Settings: "settings"
   --2--Logs: "logs"
   --2--Logging: "logging"
   --2--Delete: "delete"
pageTitle: Manage containers in the Customer Portal | Gcore
pageDescription: A comprehensive step-by-step guide on how to create and manage containers with the new product.
---
# Manage containers

After <a href="https://gcore.com/docs/cloud/caas/manage-containers" target="_blank">creating the container</a>, you can view and update its configuration in the Customer Portal on the <a href="https://portal.gcore.com/cloud/project/510960/region/80/caas/containers" target="_blank">Containers</a> page:

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/containers-page.png" alt="Containers page" width="80%">

Click a container name to open its settings. Alternatively, click the three dot-icon next to it and then select **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/edit-container.png" alt="Edit container menu" width="80%">

## Container statuses

A container can have the following statuses: 

* **Deploying**: The initial setup was successful, and the container works appropriately. 
* **Pending**: The required resources have been successfully created, but the container hasn’t been scheduled to a node yet.
* **Ready**: The container is up and running. 
* **Disabled**: You manually disabled the container in settings. 
* **Error**: There were issues with the image of your container in its initial configuration and as a result, the container didn’t work. 

## Container settings 

To start or stop the container, open the container settings and disable or enable the **Started** toggle accordingly: 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/stop-container.png" alt="Started toggle enabled" width="80%">

### Overview 

The **Overview** tab in container settings features the following details: container status, endpoint, description (if you added one during creation), and date of creation. After you create a container, you can’t change this information. 

### Image & port 

On the **Image & Port** tab, you can add a container startup command, as well as update port and protocol used to connect to the container. You can change these settings at any time.  

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/image-port.png" alt="Image & port tab" width="80%">

### Container configuration

View and adjust the number of MiB of memory, allocated mCPU, as well as autoscaling limits and triggers. For detailed overview of these settings, check out the the relevant steps in the <a href="https://gcore.com/docs/cloud/caas/create-a-container#step-4-configure-autoscaling" target="_blank">Create a container</a> guide. 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/container-configuration.png" alt="Container configuration tab" width="80%">

### API key authentication 

If you want to configure authentication to the container via API or update your API keys, you can do so on this tab.  

Turn on the **Enable API Key authentication** toggle and then add or update keys as needed. 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/api-key-auth.png" alt="API key authentication tab" width="80%">

### Settings 

The **Settings** tab lets you configure <a href="https://gcore.com/docs/cloud/caas/create-a-container#step-6-optional-add-environment-variables" target="_blank">environment variables</a> and set the duration the container will continue running without receiving any requests before it’s automatically deleted. 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/settings.png" alt="Settings tab" width="80%">

## Logs 

View the aggregated log data about requests to all running containers. Note that when you delete a container, logs are also deleted.  

Logs entities are shown in the following format: 

```
Container name_Date_Date  
IP_Method_Endpoint_HTTP type_ Resonse code_Monitoring technology name
```  

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/manage-containers-140.png" alt="Example of the logs" width="70%">

### Logging 

Activate the Logging service to store your logs. To learn how it works and how to configure it, refer to the article about <a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">Logging</a>. 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/logging.png" alt="Logging tab" width="80%">

### Delete

If you no longer need the container, click the **Delete container** button and then confirm your action by typing **Delete**. 

Both the container and its logs will be permanently removed. 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/delete-container.png" alt="Container deletion" width="80%">