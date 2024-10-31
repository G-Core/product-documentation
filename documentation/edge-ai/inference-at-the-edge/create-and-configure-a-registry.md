---
title: create-and-configure-a-registry
displayName: Create and configure a registry
published: true
order: 40
pageTitle: Add and configure a registry | Gcore
pageDescription: Learn how to set up a registry with your AI model in the Gcore Customer Portal for Gcore Inference at the EDge
---
# Add and configure a registry

If you want to deploy a custom AI model with Gcore Inference at the Edge, you need to provide information about the registry where your model is stored. This is necessary to ensure that we can access and retrieve your model during the deployment process.

You can set up a registry either <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">during AI model deployment</a> or on the **Registries** page. The latter approach is described in this guide.

## Add a registry

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **Registries**.

3\. Click **Add registry**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/add-a-registry/registry-list.png" alt="Registries page with highlighted Add registry button" width="80%">

4\. Give your registry a name consisting of lowercase Latin characters, which can be separated by dashes.

5\. Provide the link to the location where your AI model is stored. We’ll use this URL to retrieve the model during deployment.

6\. Specify the username you use to access the storage location of your AI model.

7\. Enter the password required to access the model.

8\. Click **Add**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/add-a-registry/configure-registry.png" alt="Add registry dialog with registry configuration options" width="80%">

You’ve successfully configured a registry.  

