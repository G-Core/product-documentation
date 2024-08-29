---
title: manage-containers 
displayName: Manage containers
published: true
order: 30
toc:
   --1--Overview and Port tabs: "overview-and-port-tabs"
   --1--Statuses: "container-statuses"
   --1--Change settings: "change-container-settings"
   --1--Logs: "logs"
   --1--Delete: "Delete-a-container"
pageTitle: Create Containers in the Customer Portal | Gcore
pageDescription: A comprehensive step-by-step guide on how to create and manage containers with the new product.
---
# Manage containers

After creating the container, click its name in the **Containers** tab to open its settings. Alternatively, click the three dots on the right of its row and then click **Edit**. 

In the **Overview** tab, you will see the following details: container status, name of the container image, description (if you added one during creation,) and date of creation. You can’t change this information.  

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/manage-containers-130.png" alt="Overview tab" width="70%">

In the **Port** tab, you will see the specified port and protocol to connect to your container. This information is also unchangeable. 

## Container statuses

A Container can have the following statuses: 

- **Started**: The initial setup was successful and the container works appropriately.  
- **Stopped**: You manually disabled the container in settings.  
- **Failed**: There were issues with the image of your container in its initial configuration and as a result, the container doesn’t work.

To change the container status to “Stopped,” go to the container settings and disable the toggle highlighted on the screenshot below: 

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/manage-containers-120.png" alt="How to stop a container" width="70%">

## Change container settings

Click the container’s name in the **Containers** tab to open its settings. Alternatively, click the three dots on the right of its row and then click **Edit**. You can change the following configurations: 

- mCPU and memory 
- Limits of autoscaling 
- API Key authentication 
- Variables 
- Lifetime 

Don’t forget to click **Save changes**. 

## Logs 

Open container settings and go to the **Logs** tab to view entities with the data about requests to your container.  

**Note**: When you delete a container, logs are also deleted.

Logs entities are shown in the following format: 

```
Container name_Date_Date  
IP_Method_Endpoint_HTTP type_ Resonse code_Monitoring technology name
```  

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/manage-containers-140.png" alt="Example of the logs" width="70%">

## Delete a container

Open container settings, go to the **Delete** tab, and click **Delete container**. Confirm the deletion in the pop-up window that appears.

<img src="https://assets.gcore.pro/docs/cloud/caas/manage-containers/manage-containers-150.png" alt="Container deletion" width="70%">