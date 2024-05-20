---
title: about-our-ai-infrastructure
displayName: GPU Cloud
order: 10
published: true
toc:
   --1--AI GPU infrastructure: "ai-gpu-infrastructure"
   --1--AI IPU infrastructure: "ai-ipu-infrastructure"
   --1--Server specifications and performance: "server-specifications-and-performance"
   --2--Bow-2000 specifications: "bow-2000-specifications"
   --2--M2000 specifications: "m2000-specifications"
   --1--Tools our AI Infrastructure supports: "tools-our-ai-infrastructure-supports"
pageTitle: About our AI Infrastructure | Gcore
pageDescription: Explore our AI Infrastructure. Graphcore servers, top performance, diverse tools supported. Easy deployment, per-minute billing.
---
# GPU Cloud infrastructure

Gcore GPU Cloud infrastructure services provide high-performance compute clusters designed for machine learning tasks.

## AI GPU infrastructure

You can train your ML models with the latest <a href="https://www.nvidia.com/en-us/data-center/data-center-gpus/" taget="_blank">NVIDIA GPUs</a>. We offer a wide range of Bare Metal servers and Virtual Machines powered by NVIDIA A100, H100, and L40S GPUs. 

You can choose between multiple configurations and reservation plans that would best fit your computing requirements. 

<table>
  <tr>
    <th style="width:20%">Specification</th>
    <th style="width:40%">Characteristics</th>
    <th style="width:20%">Use case</th>
    <th style="width:20%">Performance</th>
  </tr>
  <tr>
   <td style="text-align: left">H100 with Infiniband</td>
   <td style="text-align: left">

- 8x Nvidia H100 80GB
- 2 Intel Xeon 8480+
- 2TB RAM 
- 2x 960GB 
- 8x3.84 TB NVMe 
- 3.2 Tbit/s Infiniband
- 2x100Gbit/s Ethernet 
   </td>
   <td style="text-align: left">
- Optimized for distributed training of Large Language Models.
   </td>
   <td style="text-align: left">Ultimate performance for compute-intensive tasks that require a significant exchange of data by the network.</td> 
  </tr>
  <tr>
   <td style="text-align: left">A100 with Infiniband</td>
   <td style="text-align: left">
- 8x Nvidia A100 80GB
- 2 Intel Xeon 8468 
- 2 TB RAM 
- 2x 960GB SSD 
- 8x3.84 TB NVMe 
- 800Gbit/s Infiniband 
   </td>
   <td style="text-align: left">
- Specifically crafted for AI and HPC tasks. 
- Boasts fourth-generation Tensor Cores and the Transformer Engine.
   </td>
   <td style="text-align: left">Well-balanced in performance and price.</td>
  </tr>
  <tr>
   <td style="text-align: left">A100 without Infiniband</td>
   <td style="text-align: left">
- 8x Nvidia A100 80GB
- 2 Intel Xeon 8468 
- 2 TB RAM 
- 2x 960GB SSD
- 8x3.84 TB NVMe
- 2x100Gbit/s Ethernet
   </td>
   <td style="text-align: left">
- Training and fine-tuning of models on single nodes.
- Inference for large models.
- Multi-user HPC cluster.
   </td>
   <td style="text-align: left">The best solution for inference models that require more than 48GB vRAM.</td>
  </tr>
  <tr>
   <td style="text-align: left">L40</td>
   <td style="text-align: left">
- 8x Nvidia L40S
- 2x Intel Xeon 8468
- 2TB RAM 
- 4x7.68TB NVMe SSD 
- 2x25Gbit/s Ethernet
   </td>
   <td style="text-align: left">
- Model inference.
- Fine-tuning for small and medium-size models.
   </td>
   <td style="text-align: left">The best solution for inference models that require less than 48GB vRAM.</td>
  </tr>
</table>

Check out the pricing at our official website: <a href="https://gcore.com/cloud/ai-gpu" target="_blank">AI GPU Cloud infrastructure</a>.

## AI IPU infrastructure

Our <a href="https://graphcore.ai/" target="_blank">Graphcore</a> infrastructure consists of three entities:

- **Poplar server** manages all the other servers in the cluster. You have full access to this server via SSH and can work with it directly to manage the infrastructure and run your model.

- **M2000 or Bow-2000 server** (different types are available in different regions) is used for calculations made while training your model. You don’t have access to it, and this server receives commands from the Poplar server.

- **vIPU controller** (virtual Intelligence Processing Unit) is a service which configures M2000/Bow-2000 servers of your AI infrastructure to form a cluster. It's involved while the cluster is being created and while you’re changing its configuration (e.g. resizing partitions). You have access to vIPU controller via API and can rebuild the cluster if needed.

For datasets storage, you can use Poplar server disk space, external S3 storage, or <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a>.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/about-our-ai-infrastructure/image__10_.png" alt="AI Infrastructure scheme" width="80%">

## Server specifications and performance

We provide two types of Graphcore servers: M2000 and Bow-2000. M2000 is a second-generation machine and Bow-2000 is a third-generation one. 

### Bow-2000 specifications

<table>
<thead>
  <tr>
    <th><strong>Specification</strong></th>
    <th><strong>Characteristics</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td style="text-align: left">IPU processors</td>
   <td style="text-align: left">
   
- 4x Bow IPU processors (IPU frequency 1.85 GHz)
- 5,888 IPU-Cores™ with independent code execution on 35,328 worker threads
    </td>
    </tr>
    <tr>
   <td style="text-align: left">AI compute</td>
   <td style="text-align: left">
- 1.394 petaFLOPS AI (FP16.16) compute
- 0.349 petaFLOPS FP32 compute
    </td>
    </tr>
    <tr>
   <td style="text-align: left">Memory</td>
   <td style="text-align: left">
- Up to ~260 GB memory (3.6 GB In-Processor Memory™ plus up to 256 GB Streaming Memory™)
- 261 TB/s memory bandwidth
    </td>
    </tr>
    <tr>
   <td style="text-align: left">Streaming Memory</td>
   <td style="text-align: left">
- 2x DDR4-2400 DIMM 
- DRAM options: 2x 64 GB (default SKU in Bow-2000 Founder’s Edition) or 2x 128 GB (contact sales)
    </td>
    </tr>
     <tr>
   <td style="text-align: left">IPU-Gateway</td>
   <td style="text-align: left">
- 1x IPU-Gateway chip with integrated Arm Cortex quad-core A-series SoC
    </td>
    </tr>
      <tr>
   <td style="text-align: left">Internal SSD</td>
   <td style="text-align: left">
- RoCEv2 NIC (1 PCIe G4 x16 FH¾L slot)
- Standard QSFP ports
    </td>
    </tr>
    <tr>
   <td style="text-align: left">Mechanical</td>
   <td style="text-align: left">
- 1U 19 inch chassis (Open Compute compliant)
- 40 mm (width) x 728 mm (depth) x 1U (height)
- Weight: 16.395 kg (36.14 lbs)
    </td>
    </tr>
        <tr>
   <td style="text-align: left">Lights-outmanagement</td>
   <td style="text-align: left">
- OpenBMC AST2520
    </td>
    </tr>
</thead>
</table>         

### M2000 specifications

<table>
<thead>
  <tr>
    <th><strong>Specification</strong></th>
    <th><strong>Characteristics</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td style="text-align: left">IPU processors</td>
   <td style="text-align: left">

- 4 Colossus GC200 IPU processors (IPU frequency 1.325GHz) 
- 5,888 IPU-Cores™ with independent code execution on 35,328 worker threads
    </td>
    </tr>
    <tr>
   <td style="text-align: left">AI compute</td>
   <td style="text-align: left">
- 1 petaFLOPS AI compute 
- 0.25 petaFLOPS FP32 compute
    </td>
    </tr>
    <tr>
   <td style="text-align: left">IPU-Fabric</td>
   <td style="text-align: left">
- 8x IPU-Links supporting 2Tbps bi-directional bandwidth
- 8x OSFP ports
- Switch-less scalability
- Up to 8 M2000s in directly connected stacked systems
- Up to 16 M2000s in IPU-POD systems
- 2x IPU-GW-Links (IPU-Link extension over 100GbE)
- 2 QSFP28 ports
- Switch or switch-less scalability supporting 400Gbps bi-directional bandwidth
- Up to 1024 IPU-M2000s connected
    </td>
    </tr>
    <tr>
   <td style="text-align: left">IPU-Gateway</td>
   <td style="text-align: left">
- 1 IPU-Gateway with integrated Arm Cortex quad-core A-series SoC
    </td>
    </tr>
     <tr>
   <td style="text-align: left">Streaming Memory</td>
   <td style="text-align: left">
- 2 DDR4-2400 DIMM DRAM 
- DRAM options: 2x 64GB (default SKU in IPU-M2000 Founder’s Edition) or 2x 128GB or 2x 256GB (contact sales)
    </td>
    </tr>
      <tr>
   <td style="text-align: left">Internal SSD</td>
   <td style="text-align: left">
- 32GB eMMC 1TB M.2 SSD
    </td>
    </tr>
    <tr>
   <td style="text-align: left">Mechanical</td>
   <td style="text-align: left">
- 1U 19 inch chassis (Open Compute compliant)
- 440mm (width) x 728mm (depth) x 1U (height)
- Weight: 16.395kg (36.14lbs)
    </td>
    </tr>
        <tr>
   <td style="text-align: left">Lights-out management</td>
   <td style="text-align: left">
- OpenBMC AST2520 
- 2x1GbE RJ45 management ports
    </td>
    </tr>
</thead>
</table>                                                                                                                              

## Tools supported by Gcore GPU Cloud

<table>
  <thead>
    <tr>
      <th style="text-align: left"><strong>Tool class</strong></th>
      <th style="text-align: left"><strong>List of tools</strong></th>
      <th style="text-align: left"><strong>Explanation</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Framework</td>
      <td style="text-align: left">TensorFlow, Keras, PyTorch, Paddle Paddle, ONNX, Hugging Face</td>
      <td style="text-align: left">Your model is supposed to use one of these frameworks for correct work.</td>
    </tr>
    <tr>
      <td style="text-align: left">Data platforms</td>
      <td style="text-align: left">PostgreSQL, Hadoop, Spark, Vertika</td>
      <td style="text-align: left">You can set up a connection between our cluster and your data platforms of these types to make them work together.</td>
    </tr>
    <tr>
      <td style="text-align: left">Programming languages</td>
      <td style="text-align: left">JavaScript, R, Swift, Python</td>
      <td style="text-align: left">Your model is supposed to be written in one of these languages for correct work.</td>
    </tr>
    <tr>
      <td style="text-align: left">Resources for receiving and processing data</td>
      <td style="text-align: left">Storm, Spark, Kafka, PySpark, MS SQL, Oracle, MongoDB</td>
      <td style="text-align: left">You can set up a connection between our cluster and your resources of these types to make them work together.</td>
    </tr>
    <tr>
      <td style="text-align: left">Exploration and visualization tools</td>
      <td style="text-align: left">Seaborn, Matplotlib, TensorBoard</td>
      <td style="text-align: left">You can connect our cluster to these tools to visualize your model.</td>
    </tr>
  </tbody>
</table> 