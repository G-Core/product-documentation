---
title: add-a-registry
displayName: Add a registry
published: true
order: 
toc:
  --1-- Step 1. Initialize a new registry addition: "step-1-initialize-a-new-registry-addition"
  --1-- Step 2. Enter registry configuration: "step-2-enter-registry-configuration"
  --1-- Step 3. Finalize registry addition: "step-3-finalize-registry-addition"
pageTitle: Add a registry | Gcore
pageDescription: 
---
# Add a container image registry

Everywhere Inference supports custom private and public registries in addition to Gcore ones, so you can manage your model images with any service you like.

## Step 1. Initialize a new registry addition

You can initialize a new registry by following these two steps.

1\. In the Gcore Customer Portal, navigate to **Everywhere Inference** > **Registries**.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/container-image-registries/add-a-registry/add-a-registry-1.png" alt="Add a registry">

2\. Click **Add registry** in the top right of the screen.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/container-image-registries/add-a-registry/add-a-registry-2.png" alt="Add a registry">

This will open the Add registry dialog, where you can add the authentication credentials for the registry you want to add.

## Step 2. Enter registry configuration

Enter the registry’s name, URL, username, and password.

<alert-element type="tip" title="Tip">
The URL for the Huggingface registry is “<https://registry.hf.space>”. You can create an access token in the <a href="https://huggingface.co/settings/tokens">Huggingface settings</a>. Use “username” as the Image registry username and the access token as the Image registry password.
</alert-element>

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/container-image-registries/add-a-registry/add-a-registry-3.png" alt="Add a registry">

## Step 3. Finalize registry addition

After you enter all registry details, click **Add**. Your new registry’s name should appear in the list of registries.

You can now select the registry for a custom AI model deployment. To learn how to deploy a custom AI model, read [our guide](https://gcore.com/docs/edge-ai/everywhere-inference/ai-models/deploy-an-ai-model).
