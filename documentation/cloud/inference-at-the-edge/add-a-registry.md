---
title: create-and-configure-a-registry
displayName: Create and configure a registry
order: 20
published: true
pageTitle: Add and configure a registry | Gcore
pageDescription: Learn how to set up a registry with your AI model in the Customer Portal
---
# Add and configure a registry

If you want to deploy a custom AI model on Gcore inference nodes, you need to provide information about the registry where your model is stored. This is necessary to ensure that we access and retrieve your model during the deployment process.  

You can set up a registry <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">during AI model deployment</a> or separately on the **Registries** page. The last approach is described in the following sections. 

## Add a registry 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**. 

2\. Click **Registries**. 

3\. Click **Add registry**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/add-a-registry/registry-list.png" alt="Registries page with highlighted Add registry button" width="80%">

4\. Give your registry a name.  


<alert-element type="tip" title="Tip">
 
A registry name should consist of lowercase Latin characters, which can be separated by dashes.
 
</alert-element> 

5\. Provide the link to the location where your AI model is stored. We’ll use this URL to retrieve the model during deployment.  

6\. Specify the username you use to access the storage location of your AI model. 

7\. Enter a password required to access the model. 

8\. Click **Add**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/add-a-registry/configure-registry.png" alt="Add registry dialog with registry configuration options" width="80%">

You’ve successfully configured a registry.  