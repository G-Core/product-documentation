---
title: inference-at-the-edge
displayName: Inference at the Edge
order: 105
published: true
toc:
   --1--What is Inference at the Edge?: "what-is-inference-at-the-edge"
   --1--Getting started: "getting-started"
   --1--How Inference at the Edge works: "how-inference-at-the-edge-works"
   --1--Use cases: "use-cases"
   --1--Key benefits: "key-benefits"
   --1--Supported features: "supported-features"
pageTitle: About Inference at the Edge | Gcore
pageDescription: Explore Gcore Inference at the Edge infrastructure. Deploy custom AI models or select from our model catalog.
---
# About Inference at the Edge

The development of machine learning involves two main stages: training and inference.  

In the first stage, an AI model is trained on big data, like an array of images, to recognize and label objects. This results in a pre-trained model.  

The second stage is model inference, where the model is used to make predictions from real user requests. For this stage, it’s crucial that the AI model can respond promptly to users regardless of network delays, latency, and distance from data centers. 

<a href="https://gcore.com/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure" target="_blank">Gcore GPU Cloud</a> is designed for creating and training models. For inference, we offer Gcore Inference at the Edge.  

## What is Gcore Inference at the Edge? 

Gcore Inference at the Edge allows customers to deploy pre-trained AI models on edge PoPs. By bringing AI models closer to end users, the technology ensures ultra-fast response times and optimized performance.

Using Anycast endpoints, end users' queries are directed to the nearest running model, resulting in low latency and an enhanced user experience. This setup is automated through a single endpoint, relieving you of the need to manage, scale, and monitor the underlying infrastructure.

## Getting started 

For instructions on how to deploy AI models with the global intelligence pipeline, check out our guide on <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">deploying a model</a>. 

<alert-element type="info" title="Info">
 
Inference at the Edge is currently in beta mode. To join the beta, contact <a href="mailto:support@gcore.com" target="_blank">Gcore technical support</a> or your account manager. 
 
</alert-element>

## How Inference at the Edge works 

Inference at the Edge combines two technologies:  

1\. **Edge Network:** Provides low latency via Anycast balancing and smart routing.

2\. **Serverless flexible GPU infrastructure:** Enables quick initiation, integration, and deployment.

We provide you with an endpoint that can be seamlessly integrated into your applications. When users access this endpoint, their requests are delivered to the nearest Edge nodes. This is achieved through Smart Routing technology, which redirects requests to the closest inference region where the pre-trained model is deployed.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/about-inference-at-the-edge/smart-routing-diagram.png" alt="Diagram depicting Smart Routing technology" width="60%">

We also use <a href="https://gcore.com/docs/dns/dns-failover/about-dns-failover" target="_blank">Healthchecks</a> to monitor the availability of pods. If the Amsterdam-1 pod is experiencing downtime, the request will be automatically sent to the geographically closest inference region, such as Amsterdam-2. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/about-inference-at-the-edge/smart-routing-map.png" alt="<Map depicting Smart Routing across locations" width="60%">

## Use cases 

Inference at the Edge is a versatile solution for businesses requiring low-latency or real-time model responses. It caters to various industries, including:

**Fintech and banking:** Enables prompt anti-fraud detection and real-time credit scoring.

**Healthcare:** Facilitates medical prescriptions based on data from wearable sensors and the analysis of medical data.

**Gaming:** Supports automatic opponent selection in competitive games, map generation, and maintaining open worlds.

**Media:** Provides content analysis, automated transcribing, and translating of interviews.

**ISP and internet services:** Offers AI-based traffic analysis and DDoS protection.

**Industrial and manufacturing:** Ensures real-time defect detection and fast feedback.

## Key benefits  

Inference at the Edge offers several key benefits:

**Low latency:** With over 180 points of presence worldwide, requests are transferred quickly to the nearest Inference at the Edge pod, ensuring low latency for users.

**High performance:** Utilizing the latest, purpose-built NVIDIA GPU hardware, Inference at the Edge delivers fast model inference capable of handling the most demanding workloads.

**Cost efficiency:** Payments are based solely on the runtime of the containers, which automatically scale in and out based on the number of user requests to keep your operations cost-effective.

**Easy control:** Gcore's global AI infrastructure can be configured with just a few clicks in the Gcore Customer Portal or via API requests, simplifying management and control.

## Supported features 

* Custom model deployment 

* Various flavors (vGPU/vCPU/RAM) and storage 

* DDoS and bot protection 

* API keys  

* Marketplace for models (coming soon)

* REST API & Terraform (coming soon)

* RAG support (coming soon)
