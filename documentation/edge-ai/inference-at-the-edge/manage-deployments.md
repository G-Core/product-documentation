---
title: manage-deployments
displayName: Manage deployments in the Customer Portal 
order: 20
published: true
toc:
  --1--Manage deployments: "manage-deployments"
  --2--Pause deployments: "pause-deployments"
  --2--View deployment details: "view-deployment-details"
  --3--Overview: "overview"
  --3--API key authentication: "api-key-authentication"
  --3--Settings: "settings"
pageTitle: Managing Deployments in the Gcore Customer Portal | Gcore
pageDescription: Learn how to manage Inference at the Edge instances with deployed AI models. Change instance settings, pause instances, or delete them from the Gcore Customer Portal.
---
# Manage deployments in the Customer Portal

After you <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">deploy an AI model</a>, it will appear on the **Deployments** page. There, you can find all the necessary information about the model:

* **Name:** Name of your AI model (you entered it in the Deployment details section).

* **Endpoint:** A URL for the pretrained deployed model.

* **Created:** The date and time when the model was deployed.

* **Deployment status:** An Inference at the Edge instance can have the following statuses:

  - **New**: We’re in the process of allocating resources to a deployment.
  - **Succeeded:** The instance has been successfully deployed.
  - **Active:** The deployment is up and running.
  - **Failed:** An error occurred when allocating resources. Recreate the deployment.
  - **Disabled:** The deployment is currently paused/inactive.

* **Running status:** Maintenance deployment status, showing how many pods are run in the selected regions. Move the cursor over the number of running models and a list of regions will appear.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/deployments-tab.png" alt="Deployments page with two inference instances" width="80%">

## Manage deployments

You can view the configuration details of a deployed AI model, pause the deployment, or delete it from the Gcore Customer Portal. If you have a large number of deployments, you can also use search to find the one that you need.

## Pause deployments

You can temporarily stop the deployment:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **Deployments**.

3\. Find the deployment you want to stop and click the three-dot icon to open the settings menu.

4\. Click **Stop**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/stop-deployment.png" alt="Stop deployment dialog" width="80%">

After stopping, the deployment status will change to “Disabled.” You can run the deployment anytime by clicking the three-dot icon and clicking **Start**.

## View deployment details

To get comprehensive information about your deployment configuration and adjust the settings if needed:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **Deployments**.

3\. Find the required deployment and click the three-dot icon next to it.

4\. Click **Overview**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/overview-deployment.png" alt="Overview deployment dialogs" width="80%">

A new page with a deployment overview will open. Navigate to the corresponding tab to check a particular functionality.

### Overview

This tab contains all the details related to your model's deployment. This includes the number of pods currently running, deployment status, price rate, endpoint, and description (if available).

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/overview-tab.png" alt="Overview tab in the deployment overview" width="80%">

Click **Show map with running replicas** to view the regions where your models have been deployed.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/models-map.png" alt="Map with deployments" width="80%">

### API key authentication

This tab allows you to configure API authentication for your Inference instance. To activate the feature, toggle the **Enable API Key authentication** toggle.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/api-key-auth-tab.png" alt="API keys section with enabled toggle" width="80%">

Choose one of the following options:

* **Select API keys:** Add one or more keys that are already stored in the Gcore Customer Portal by selecting them from the dropdown list.

* **Create new API key:**: Generate a new key.

<alert-element type="tip" title="Tip">

Inference instances have a many-to-many relationship. A single instance can have multiple API keys, and the same API key can be attached to multiple instances.

</alert-element>

To generate a key, select the **Create new API key** link:

1\. In a new dialog that opens, enter the key name to identify the key in the system.

2\. (Optional) Add a description to give more context about the key and its usage.

4\. As a security measure, you can specify the key expiration date. If you don’t want to regenerate the key and want to keep it indefinitely, select **Never expire**.

4\. Click **Create**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/create-api-key.png" alt="Create API key dialog with annotated steps" width="80%">

You can now select the key from the API Keys dropdown and use it for authentication.

### Delete

Here, you can delete a deployment and all its data.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/delete-tab.png" alt="Delete tab in the deployment overview" width="80%">

To delete the deployment:

1\. Click **Delete deployment**.

2\. Confirm your action by typing “Delete” in the text field.

3\. Click **Yes, delete**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/verify-deletion.png" alt="Delete deployment confirmation dialog" width="80%">

The deployed AI model has been successfully deleted.

### Settings

Here, you can change the following settings of the deployment:

* **Pod configuration:** Change the parameters of a Kubernetes pod your model is deployed to.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/pod-configuration.png" alt="Pod configuration section" width="60%">

* **Port:** Change the port inside the container on which the model is listening.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/port.png" alt="Port section" width="60%">

* **Autoscaling:** Increase or decrease the number of maximum and minimum pods during traffic changes.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/autoscaling.png" alt="Autoscaling section" width="60%">

* **Environment variables:** Add metadata.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/env-variables.png" alt="Environment variables section" width="60%">

* **Pod lifetime:** Change the number of MB and vCPU allocated to the Kubernetes pod.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/pod-lifetime.png" alt="Pod lifetime section" width="60%">

## Delete deployment

<alert-element type="warning" title="Warning">

When you delete a deployment, you lose all its data. Deleted deployments can't be restored.

</alert-element>

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **Deployments**.

3\. Find the deployment you want to delete and click the three-dot icon next to the deployment you want to view.

4\. Click **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/manage-deployments/delete-deployment.png" alt="Delete deployment option in the settings" width="80%">

5\. Confirm your action by typing “Delete” in the text field.

6\. Click **Yes, delete**.

The deployed AI model has been successfully deleted. 
