---
title: inference-at-the-edge
displayName: Inference at the Edge
order: 105
published: true
toc:
   --1--What is Inference at the Edge?: "what-is-inference-at-the-edge"
   --1--Getting started: "getting-started"
   --1—-How Inference at the Edge works: "how-inference-at-the-edge-works"
   --1--Use cases: "use-cases"
   --1--Key benefits: "key-benefits"
   --1--Supported features: "supported-features"
pageTitle: About Inference at the Edge | Gcore
pageDescription: Explore our Inference at the Edge infrastructure. Deploy custom AI models or select AI models from our model catalog.
---
# About Inference at the Edge

The development of machine learning involves two main stages: training and inference.  

In the first stage, an AI model is trained on big data, like an array of images, to recognize and label objects. This results in a pre-trained model.  

The second stage is model inference, where the model is used to make predictions from real user requests. For this stage, it’s crucial that the AI model can respond promptly to users regardless of network delays, latency, and distance from data centers. 

The <a href="https://gcore.com/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure" target="_blank">Gcore GPU Cloud</a> product is designed for creating and training models. For inference, Gcore has introduced a new product—Inference at the Edge.  

## What is Inference at the Edge? 

Inference at the Edge enables customers to deploy pre-trained AI models on edge inference nodes. This technology uses anycast endpoints to direct end users’ queries to the nearest running model, ensuring low latency and optimizing response times to enhance user experience. 

The main idea behind Inference at the Edge is to bring pre-trained models as close as possible to end users. This enables ultra-fast response times, automated through a single endpoint, relieving you of managing, scaling, and monitoring the underlying infrastructure.   

## Getting started 

For instructions on how to deploy AI models with the global intelligence pipeline, check out the <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">Deploy a model</a> guide. 

<alert-element type="info" title="Info">
 
Inference at the Edge is currently in beta testing. To enable the product for your account, contact <a href="mailto:support@gcore.com" target="_blank">our technical support</a> or your account manager. 
 
</alert-element>

## How Inference at the Edge works 

Inference at the Edge combines two technologies:  

1\. **Edge Network** for low latency by anycast balancing and smart routing. 

2\. **Serverless flexible GPU infrastructure** for quick initiation, integration, and deployment. 

We provide you with an endpoint that can be integrated with your applications. When your users access this endpoint, their requests are delivered to the nearest Edge nodes. This is achieved through the use of a Smart Routing technology, which redirects requests to the nearest inference region where the pre-trained model is deployed.  

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/about-inference-at-the-edge/smart-routing-diagram.png" alt="Diagram depicting Smart Routing technology" width="60%">

We also use <a href="https://gcore.com/docs/dns/dns-failover/about-dns-failover" target="_blank">Healthchecks</a> to monitor the availability of pods. If a pod in Amsterdam is experiencing downtime, the request will be automatically sent to the next geographically close inference region, such as Amsterdam-2. 

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/about-inference-at-the-edge/smart-routing-map.png" alt="<Map depicting Smart Routing across locations" width="60%">

## Use cases 

Inference at the Edge is a versatile solution for businesses that require low latency or real-time model responses. 

* **Fintech and banking**. Prompt anti-fraud detection and real-time credit scoring. 

* **Healthcare**. Making medical prescriptions based on data from wearable sensors and analyzing medical data 

* **Gaming**. Automatic opponent selection in competitive games, map generation, and maintaining an open world.  

* **Media**. Content analysis and automated transcribing and translating of interviews. 

* **ISP and internet services**. AI-based traffic analysis and DDoS protection. 

* **Industrial**. Real-time defect detection and fast feedback. 

## Key benefits  

* **Low latency**. Over 160 Edge nodes worldwide enable faster request transfer to the closest Inference at the Edge POD, providing low latency for users who send requests to your model. 

* **High performance**. Fast model inference using the latest GPU hardware is built for handling the most demanding workloads. 

* **Cost efficiency**. Payments are based solely on the runtime of the containers, which automatically scale in and out based on the number of user requests. 

* **Easy control**. Global AI infrastructure is configured in a few clicks in the Customer Portal or by API requests.

## Supported features 

* Custom model deployment 

* Various flavors (vGPU/vCPU/RAM) and storage 

* DDoS & Bot protection 

* API keys  

* Marketplace for models (coming soon)

* REST API & Terraform (coming soon)

* RAG support (coming soon)