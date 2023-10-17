---
title: about-our-ai-infrastructure
displayName: Overview
order: 10
published: true
toc:
   --1--What is AI Infrastructure?: "what-is-ai-infrastructure"
   --1--Server specifications and performance: "server-specifications-and-performance"
   --2--Bow-2000 specifications: "bow-2000-specifications"
   --2--M2000 specifications: "m2000-specifications"
   --2--Performance tests Graphcore M2000 vs NVIDIA DGX A100: "performance-tests-graphcore-m2000-vs-nvidia-dgx-a100"
   --1--Tools our AI Infrastructure supports: "tools-our-ai-infrastructure-supports"
   --1--Deployment time: "deployment-time"
   --1--How to use AI Infrastructure?: "how-to-use-ai-infrastructure"
   --1--How is AI Infrastructure billed?: "how-is-ai-infrastructure-billed"
pageTitle: About our AI Infrastructure | Gcore
pageDescription: Explore our AI Infrastructure. Graphcore servers, top performance, diverse tools supported. Easy deployment, per-minute billing.
---
# About our AI infrastructure

## What is AI Infrastructure?

AI Infrastructure is a cluster of <a href="https://graphcore.ai" target="_blank">Graphcore</a> servers which are designed for ML tasks. These servers have [high specifications](https://gcore.com/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure#server-specifications-and-performance) and are configured for processing a great amount of data in a short time (you can find the results of performance tests in the [Performance tests](https://gcore.com/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure#performance-tests-graphcore-m2000-vs-nvidia-dgx-a100) section).

This infrastructure consists of three entities:

- **Poplar server** — a server that manages all the other servers in the cluster. You have full access to this server via SSH and can work with it directly for managing the AI Infrastructure and running your model.
- **M2000 or Bow-2000 server** (different types are available in different regions) — a Graphcore server which is used for calculations made while training your model. You don’t have access to it, this server receives commands from the Poplar server.
- **vIPU controller** (virtual Intelligence Processing Unit) — a service which configures M2000/Bow-2000 servers of your AI Infrastructure to make them a cluster. It is involved while the cluster is being created and while you’re changing its configuration, e.g. resizing partitions. You have access to vIPU controller via API and can rebuild the cluster if desired.

For datasets storage, you can use Poplar server disk space, external S3 storage, or <a href="https://gcore.com/storage" target="_blank">our S3 storage</a>.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure/image__10_.png" alt="AI Infrastructure scheme" width="80%">

## Server specifications and performance

We provide two types of Graphcore servers: M2000 and Bow-2000. M2000 is a second-generation machine and Bow-2000 is a third-generation one. 

### Bow-2000 specifications

| IPU processors       | 4x Bow IPU processors (IPU frequency 1.85 GHz)5,888 IPU-Cores™ with independent code execution on 35,328 worker threads |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| AI compute           | 1.394 petaFLOPS AI (FP16.16) compute0.349 petaFLOPS FP32 compute                                                        |
| Memory               | Up to ~260 GB memory (3.6 GB In-Processor Memory™ plus up to 256 GB Streaming Memory™)261 TB/s memory bandwidth         |
| StreamingMemory      | 2x DDR4-2400 DIMM DRAMOptions: 2x 64 GB (default SKU in Bow-2000 Founder’s Edition) or 2x 128 GB (contact sales)        |
| IPU-Gateway          | 1x IPU-Gateway chip with integrated Arm Cortex quad-core A-series SoC                                                   |
| Internal SSD         | RoCEv2 NIC (1 PCIe G4 x16 FH¾L slot)Standard QSFP ports                                                                 |
| Mechanical           | 1U 19 inch chassis (Open Compute compliant)40 mm (width) x 728 mm (depth) x 1U (height)Weight: 16.395 kg (36.14 lbs)    |
| Lights-outmanagement | OpenBMC AST2520                                                                                                         |

### M2000 specifications

|     IPU processors    | 4 Colossus GC200 IPU processors (IPU frequency 1.325GHz) 5,888 IPU-Cores™ with independent code execution on 35,328 worker threads                                                                                                                                                                                                                                       |
|:---------------------:|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|       AI compute      | 1 petaFLOPS AI compute 0.25 petaFLOPS FP32 compute                                                                                                                                                                                                                                                                                                                       |
|       IPU-Fabric      | 8x IPU-Links supporting 2Tbps bi-directional bandwidth 8x OSFP ports  Switch-less scalability  Up-to 8 M2000s in directly connected stacked systems  Up-to 16 M2000s in IPU-POD systems  2x IPU-GW-Links (IPU-Link extension over 100GbE)  2 QSFP28 ports  Switch or Switch-less scalability supporting 400Gbp bi-directional bandwidth  Up-to 1024 IPU-M2000s connected |
|      IPU-Gateway      | 1 IPU-Gateway with integrated Arm Cortex quad-core A-series SoC                                                                                                                                                                                                                                                                                                          |
|    Streaming Memory   | 2 DDR4-2400 DIMM DRAM  Options: 2x 64GB (default SKU in IPU-M2000 Founder’s Edition) or 2x 128GB or 2x 256GB (contact sales)                                                                                                                                                                                                                                             |
|      Internal SSD     | 32GB eMMC  1TB M.2 SSD                                                                                                                                                                                                                                                                                                                                                   |
|       Mechanical      | 1U 19inch chassis (Open Compute compliant)  440mm (width) x 728mm (depth) x 1U (height)  Weight: 16.395kg (36.14lbs)                                                                                                                                                                                                                                                     |
| Lights-out management | OpenBMC AST2520  2x1GbE RJ45 management ports                                                                                                                                                                                                                                                                                                                            |

### Performance tests: Graphcore M2000 vs NVIDIA DGX A100

Here are results of <a href="https://graphcore.ai/posts/graphcore-sets-new-ai-performance-standards-with-mk2-ipu-systems" target="_blank">processing of two popular computer vision models on M2000 and NVIDIA DGX A100</a> (another popular solution for machine learning).

<media-gallery>
<img src="https://www.graphcore.ai/hs-fs/hubfs/ResNet%2050%20Training_December%202020.jpg?width=590&amp;name=ResNet%2050%20Training_December%202020.jpg" alt="Performance tests">

<img src="https://www.graphcore.ai/hs-fs/hubfs/ResNet%2050%20Inference_December%202020.jpg?width=591&amp; name=ResNet%2050%20Inference_December%202020.jpg" alt="Performance tests">

<img src="https://www.graphcore.ai/hs-fs/hubfs/ResNeXt%20Training_December%202020.jpg?width=593&amp; name=ResNeXt%20Training_December%202020.jpg" alt="Performance tests">

<img src="https://www.graphcore.ai/hs-fs/hubfs/ResNeXt%20Inference_December%202020.jpg?width=591&amp; name=ResNeXt%20Inference_December%202020.jpg" alt="Performance tests">
</media-gallery>

You can find results of a higher number of comparative tests (12 in total) in the article <a href="https://graphcore.ai/posts/graphcore-sets-new-ai-performance-standards-with-mk2-ipu-systems" target="_blank">Graphcore Sets New Ai Performance Standards With MK2 IPU System</a>. 

## Tools our AI Infrastructure supports

| Tool class                                  | List of tools                                       | Explanation                                                                                                       |
|-------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Framework                                   | TensorFlowKerasPyTorchPaddle PaddleONNXHugging Face | Your model is supposed to use one of these frameworks for correct work                                            |
| Data platforms                              | PostgreSQLHadoopSparkVertika                        | You can set up a connection between our cluster and your data platforms of these types to make them work together |
| Programming languages                       | JavaScriptRSwiftPython                              | Your model is supposed to be written on one of these languages for correct work                                  |
| Resources for receiving and processing data | StormSparkKafkaPySparkMS SQLOracleMongoDB           | You can set up a connection between our cluster and your resources of these types to make them work together      |
| Exploration and visualization tools         | SeabornMatplotlibTensorBoard                        | You can connect our cluster to these tools to visualize your model                                                |

## Deployment time

Deployment time is about 15 minutes. This is the time between the moment you click **Create cluster** and the moment it is created and ready to work.

## How to use AI Infrastructure?

1.  Create a cluster in the Gcore Control panel.
2.  Access a Poplar server via SSH.
3.  Upload a clone of the repository with your model to the Poplar server.
4.  Upload datasets to the Poplar server or connect the S3 storage that hosts your datasets.
5.  Run the model.

## How is AI Infrastructure billed?

The billing is per minute. You pay for the time spent from a cluster creation to its deletion.
