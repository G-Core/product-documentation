--- 
title: manage-deployments 
displayName: Manage deployments in the Customer Portal 
order: 30 
published: true 
toc: 
--1--Manage deployments: "manage-deployments" 
--2--Pause deployments: "pause-deployments" 
--2--View deployment details: "view-deployment-details" 
--3--Overview: "overview" 
--3--API key authentication: "api-key-authentication" 
--3--Settings: "settings" 
pageTitle: Managing Deployments in the Customer Portal | Gcore 
pageDescription: Learn how to manage Inference at the Edge instances with deployed AI models. Change instance settings, pause instances, or delete them from the Customer Portal. 
--- 
# Manage deployments in the Customer Portal 

After you <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">deploy an AI model</a>, it will appear on the **Deployments** page. There, you can find all the necessary information about the model:  

* **Name**: name of your AI model (you entered it in the Deployment details section). 

* **Endpoint**: a URL for a pre-trained deployed model. 

* **Created**: the date and time when a model was deployed. 

* **Deployment status**: an Inference instance can have the following statuses: 

    - **New**: we’re allocating resources to an instance.
    - **Active**: the instance is up and running. 
    - **Failed**: an error occurred when allocating resources. You need to recreate the instance.  
    - **Succeeded**: the instance has been successfully deployed.
    - **Disabled**: the instance is currently paused. 

* **Running status**: maintenance deployment status, which shows how many pods are run in the selected regions. If you move the cursor over the amount of running models, a list of regions will appear. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/deployments-tab.png" alt="Deployments page with two inference instances" width="80%">

## Manage deployments 

You can view the configuration details of a deployed AI model, pause the deployment, or delete it from the Customer Portal. If you have a large number of deployments, you can also use search to find the one that you need. 

## Pause deployments

You can temporarily stop the deployment: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **AI infrastructure**. 

2\. Open the **Inference at the Edge** page and click **Deployments**.  

3\. Find the deployment you want to stop and click the three-dot icon to open the settings menu. 

4\. Click **Stop**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/stop-deployment.png" alt="Stop deployment dialog" width="80%">

After stopping, the deployment status will change to “Disabled.” You can run the deployment anytime by clicking the three-dot icon and clicking **Start**.  

## View deployment details 

To get comprehensive information about your deployment configuration and adjust the settings if needed: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **AI infrastructure**. 

2\. Open the **Inference at the Edge** page and click **Deployments**.  

3\. Find the needed deployment and click the three-dot icon next to the deployment you want to view. 

4\. Click **Overview**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/overview-deployment.png" alt="Overview deployment dialogs" width="80%">

A new page with deployment overview will open. Navigate to the corresponding tab to check a particular functionality.   

### Overview  

On this tab, you can find all the details related to the deployment of your model. This includes the number of pods that are currently running, deployment status, price rate, endpoint, and the description (if available). 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/overview-tab.png" alt="Overview tab in the deployment overview" width="80%">

You can click **Show map with running replicas** to view the regions where your models have been deployed. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/models-map.png" alt="Map with deployments" width="80%">

### API key authentication 

On this tab, you can configure API authentication for your Inference instance. To activate the feature, **turn on the Enable API Key authentication** toggle.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/api-key-auth-tab.png" alt="API keys section with enabled toggle" width="80%">

You can choose one of the following options: 

* **Select API keys**: add one or more keys that are already stored in the Gcore Customer Portal by selecting them from the dropdown list. 

* **Create new API key**: generate a new key. 

<alert-element type="tip" title="Tip">
 
Inference instances have many-to-many relationship. A single instance can have multiple API keys, and the same API key can be attached to multiple instances. 
 
</alert-element>

To generate a key, select the **Create new API key** link: 

1\. In a new dialog that opens, enter the key name to identify the key in the system.

2\. (Optional) Add a description to give more context about the key and its usage. 

4\. As a security measure, you can specify the key expiration date. If you don’t want to regenerate the key and keep it indefinitely, select **Never expire**.  

4\. Click **Create**. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/create-api-key.png" alt="Create API key dialog with annotated steps" width="80%">

You can now select the key from the API Keys dropdown and use it for authentication. 

### Delete 

On this tab, you can remove the deployment and all its data. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/delete-tab.png" alt="Delete tab in the deployment overview" width="80%">

To delete the deployment: 

1\. Click **Delete deployment**. 

2\. Confirm your action by typing “Delete” in the text field. 

3\. Click **Yes, delete**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/verify-deletion.png" alt="Delete deployment confirmation dialog" width="80%">

The deployed AI model has been successfully removed. 

### Settings 

On this tab, you can change the following settings of the deployment: 

* **Pod configuration**: change the parameters of a Kubernetes pod your model is deployed to.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/pod-configuration.png" alt="Pod configuration section" width="60%">

* **Port**: change the pore inside the container that the model is listening on.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/port.png" alt="Port section" width="60%">

* **Autoscaling**: increase or decrease the number of maximum and minimum pods during traffic changes.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/autoscaling.png" alt="Autoscaling section" width="60%">

* **Environment variables**: add metadata.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/env-variables.png" alt="Environment variables section" width="60%">

* **Pod lifetime**: change the number of MB and vCPU allocated to the Kubernetes pod.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/pod-lifetime.png" alt="Pod lifetime section" width="60%">

## Delete deployment 

<alert-element type="warning" title="Warning">
 
When you delete a deployment, you lose all its data. Deleted deployments can't be restored. 
 
</alert-element>

1\. In the Gcore Customer Portal, navigate to **Cloud** > **AI infrastructure**. 

2\. Open the **Inference at the Edge** page and click **Deployments**. 

3\. Find the deployment you want to delete and click the three-dot icon next to the deployment you want to view. 

4\. Click **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/delete-deployment.png" alt="Delete deployment option in the settings" width="80%">

5\. Confirm your action by typing “Delete” in the text field. 

6\. Click **Yes, delete**. 

The deployed AI model has been successfully removed. 