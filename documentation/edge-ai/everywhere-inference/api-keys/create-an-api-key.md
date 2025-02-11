---
title: create-an-api-key
displayName: Create an API Key
published: true
order: 1
toc:
  --1-- Step 1. Initialize API Key creation: "step-1-initialize-api-key-creation"
  --1-- Step 2. Configure the API Key: "step-2-configure-the-api-key"
  --1-- Step 3. Finalize the API Key creation: "step-3-finalize-the-api-key-creation"
pageTitle: Create an API Key | Gcore
pageDescription: 
---
# Create an API Key

You can create API Keys to make sure that only authenticated clients can access your AI models.

## Step 1. Initialize API Key creation

To open the Create API Key dialog, you can use this [direct link](https://portal.gcore.com/inference-at-the-edge/api-keys/create) or take the following two steps:

1. Navigate to **Everywhere Inference** > **API Keys** in the Gcore Customer Portal.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/api-keys/create-an-api-key/create-an-api-key-1.png" alt="Create an API Key">

1. Click **Add API Key** in the top right of the screen.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/api-keys/create-an-api-key/create-an-api-key-2.png" alt="Create an API Key">

This will open the Create API Key dialog, where you can configure the new API Key.

## Step 2. Configure the API Key

In the **Create API Key** dialog, you can name and describe the API key and select the instances (e.g., AI model deployments) to which it should grant access.

<alert-element type="tip" title="Tip">
You can select multiple instances for one key, and each instance can have multiple keys. You can also add and remove instances from the API Key or the deployment side later.
</alert-element>

<alert-element type="info" title="Info">
For security reasons, you should set an expiration date for API Keys. The key will expire on the selected date at 00:00 UTC. You can change this setting later.
</alert-element>

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/api-keys/create-an-api-key/create-an-api-key-3.png" alt="Create an API Key">

## Step 3. Finalize the API Key creation

After entering the API Key details, click the **Create** button. The new API key will appear in the list of API Keys.

You can now select the API key for an AI model deployment. To learn how to deploy a custom AI model, read [the guide](https://gcore.com/docs/edge-ai/everywhere-inference/ai-models/deploy-an-ai-model).
