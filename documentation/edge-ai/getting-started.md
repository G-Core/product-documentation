---
title: getting-started
displayName: Getting started
published: true
order: 1
toc: 
pageTitle: Getting started with Edge AI| Gcore
pageDescription: Learn how to get started with Gcore Edge AI services.
---
# Getting started

The development of machine learning involves two main stages: training and inference.

In the first stage, an AI model is trained on big data, like an image catalog, to recognize and label objects. This results in a trained model.

**If you want to train AI models**, check out or guide on [creating an AI cluster](https://gcore.com/docs/edge-ai/ai-infrastructure/create-an-ai-cluster) to set up an AI cluster with the [Gcore GPU Cloud](https://gcore.com/cloud/ai-gpu) via the Gcore Customer Portal.

<alert-element type="tip" title="Tip">
Check out <a href="https://api.gcore.com/docs/cloud#tag/GPU-Cloud">our API docs</a> if you want to control your GPU resources programmatically.
</alert-element>

The second stage of AI is [model inference](https://gcore.com/learning/what-is-ai-inference/), where the model makes predictions based on user requests. In this stage, it’s crucial that the AI model can respond promptly to users regardless of network delays, latency, and distance from data centers.

**If you need inference** for open-source models or models you trained yourself, [our guide on deploying AI models](https://gcore.com/docs/edge-ai/everywhere-inference/ai-models/deploy-an-ai-model) explains how to set up [Everywhere Inference](https://gcore.com/everywhere-inference) via the Gcore Customer Portal.

<alert-element type="tip" title="Tip">
Check out <a href="https://api.gcore.com/docs/cloud#tag/Inference-Instances">our API docs</a> if you want to control your inference resources programmatically.
</alert-element>
