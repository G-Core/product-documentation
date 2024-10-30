---
title: about-our-ai-infrastructure
displayName: About GPU Cloud
order: 10
published: true
toc:
   --1--AI GPU infrastructure: "ai-gpu-infrastructure"
   --1--Tools our AI Infrastructure supports: "tools-supported-by-gcore-gpu-cloud"
pageTitle: About Gcore GPU Cloud | Gcore
pageDescription: Explore Gcore GPU Cloud for AI. NVIDIA servers, top performance, diverse tool support. Easy deployment, per-minute billing.
---
# GPU Cloud infrastructure

Gcore <a href="https://gcore.com/cloud/ai-gpu" target="_blank">GPU Cloud</a> provides high-performance compute clusters designed for machine learning tasks.

## AI GPU infrastructure

Train your ML models with the latest <a href="https://www.nvidia.com/en-us/data-center/data-center-gpus/" taget="_blank">NVIDIA GPUs</a>. We offer a wide range of Bare Metal servers and Virtual Machines powered by NVIDIA A100, H100, and L40S GPUs. 

Pick the configuration and reservation plan that best fits your computing requirements. 

<table>
  <tr>
    <th style="width:20%">Specification</th>
    <th style="width:35%">Characteristics</th>
    <th style="width:23%">Use case</th>
    <th style="width:22%">Performance</th>
  </tr>
  <tr>
   <td style="text-align: left">H100 with Infiniband</td>
   <td style="text-align: left">
   8x Nvidia H100 80GB <br> 
   2 Intel Xeon 8480+ <br> 
   2TB RAM <br> 
   2x 960GB <br> 
   8x3.84 TB NVMe <br> 
   3.2 Tbit/s Infiniband <br> 
   2x100Gbit/s Ethernet
   </td>
   <td style="text-align: left">
   Optimized for distributed training of Large Language Models.
   </td>
   <td style="text-align: left">Ultimate performance for compute-intensive tasks that require a significant exchange of data by the network.</td> 
  </tr>
  <tr>
   <td style="text-align: left">A100 with Infiniband</td>
   <td style="text-align: left">
   8x Nvidia A100 80GB <br> 
   2 Intel Xeon 8468 <br> 
   2 TB RAM <br> 
   2x 960GB SSD <br> 
   8x3.84 TB NVMe <br> 
   800Gbit/s Infiniband
   </td>
   <td style="text-align: left">
  Distributed training for ML models and a broad range of HPC workloads.
   </td>
   <td style="text-align: left">Well-balanced in performance and price.</td>
  </tr>
  <tr>
   <td style="text-align: left">A100 without Infiniband</td>
   <td style="text-align: left">
   8x Nvidia A100 80GB <br> 
   2 Intel Xeon 8468 <br> 
   2 TB RAM <br> 
   2x 960GB SSD <br> 
   8x3.84 TB NVMe <br> 
   2x100Gbit/s Ethernet
   </td>
   <td style="text-align: left">
     Training and fine-tuning of models on single nodes. <br> 
     <br>Inference for large models.<br> 
     Multi-user HPC cluster.
   </td>
   <td style="text-align: left">The best solution for inference models that require more than 48GB vRAM.</td>
  </tr>
  <tr>
   <td style="text-align: left">L40</td>
   <td style="text-align: left"> 
   8x Nvidia L40S <br> 
   2x Intel Xeon 8468 <br> 
   2TB RAM <br> 
   4x7.68TB NVMe SSD <br> 
   2x25Gbit/s Ethernet
   </td>
   <td style="text-align: left">
   Model inference.<br> 
   <br>Fine-tuning for small and medium-size models.
   </td>
   <td style="text-align: left">The best solution for inference models that require less than 48GB vRAM.</td>
  </tr>
</table>

Explore our competitive pricing on the <a href="https://gcore.com/cloud/ai-gpu" target="_blank">AI GPU Cloud infrastructure pricing page</a>.
                 
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
