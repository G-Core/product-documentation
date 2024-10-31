---
title: deploy-ai-model
displayName: Deploy Hugging Face models
order: 20
published: true
toc: 
  --1--Step 1. Set up a Hugging Face Space: "step-1-set-up-a-hugging-face-space"
  --1--Step 2. Deploy a Hugging Face model: "step-2-deploy-the-hugging-face-model-on-edge-inference"
  --1--Step 3. Interact with the model: "step-3-interact-with-the-model"
pageTitle: Deploy Hugging Face AI models on the Gcore platform | Gcore
pageDescription: "Learn how to set up Hugging Face Spaces and run AI models on the Gcore edge inference nodes"
---
# Deploy Hugging Face models on edge inference nodes

Deploy Hugging Face AI models on <a href="https://gcore.com/docs/cloud/inference-at-the-edge" target="_blank">Gcore edge inference nodes</a> to easily set up, manage, and ensure real-time delivery of your AI-powered solutions.

Whether you're working on natural language processing, computer vision, or other AI tasks, using edge inference significantly improves response times and scalability of your workloads.

## Step 1. Set up a Hugging Face Space

1\. In the <a href="https://huggingface.co/models" target="_blank">Hugging Face models catalog</a>, select the model you want to deploy for your edge inference solution. 

2\. Navigate to the corresponding space where the model is used. For example, for the model Pixtral-12B-2409, select any of the associated spaces.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/deploy-hugging-face-models/huggingface-spaces-example.png" alt="Spaces section in Hugging Face" width="80%">

3\. Copy the Docker image link and startup command according to the instructions from the <a href="https://huggingface.co/docs/hub/en/spaces-run-with-docker" target="_blank">official Hugging Face guide</a>. 

## Step 2. Deploy the Hugging Face model on edge inference

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, click **Inference at the Edge**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/iae-landing-page.png" alt="Overview page with options to create custom models or from catalog" width="80%">

2\. Click **Deploy custom model**. 

3\. Configure the model image: 

  * In the **Model image URL (docker tag)** field, enter the following link: `registry.hf.space/ethux-mistral-pixtral-demo:latest`. 

  * Enable the **Set startup command** toggle and add the executable command `python app.py`.

  <img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/deploy-hugging-face-models/huggingface-model-settings.png" alt="Configurations for a public Hugging Face AI model" width="80%">

4\. Set the **Container port** to 7860.  

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/deploy-hugging-face-models/huggingface-port-settings.png" alt="Container port settings for a public Hugging Face AI model" width="80%">

5\. Configure the pod: 

  * Processor type: GPU-optimized 

  * Flavor: 1x L40S / 16 vCPU / 232GiB RAM 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/deploy-hugging-face-models/huggingface-pod-settings.png" alt="Pod settings for a public Hugging Face AI model" width="80%">

6\. In the **Routing placement** field, choose any available region for optimal performance.  

7\. Enter a name for your deployment.

8\. Click **Deploy**. 

## Step 3: Interact with the model

Once the model is up and running, you’ll get a link to the endpoint. You can interact with the model via this endpoint to test and use your deployed inference model at the edge. 
