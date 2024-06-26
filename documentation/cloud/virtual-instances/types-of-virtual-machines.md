---
title: types-of-virtual-machines
displayName: Types of Virtual Machines
order: 5
published: true
toc:
    --1--Standard: "standard"
    --1--GPU: "gpu"
    --1--CPU: "cpu"
    --1--Memory: "memory"
    --1--High-frequency: "high-frequency"
    --1--Basic VM: "basic-vm"
    --1--SGX-enabled: "sgx-enabled"
    --1--TPM: "tpm"
pageTitle: Types of Virtual Machines | Gcore
pageDescription: Discover the available types of Gcore Virtual Machines, their technical specifications, and use cases.
---
# Types of Virtual Machines

Gcore Virtual Machines (VMs) offer a flexible, powerful, and scalable solution for hosting applications and services. Designed to meet a wide range of computing needs, our VMs ensure optimal performance, reliability, and security for your applications.

We provide multiple types of Virtual Machines suitable to different workflows and computing tasks:
 
* **Standard**: Suitable for a wide range of basic workloads that require predictable compute performance.

* **CPU**: Best suited for CPU-intensive tasks that require predictable computing performance, such as batch processing of large data sets and video encoding.

* **Memory**: Ideal for tasks and projects that require intensive memory usage, such as databases.

* **GPU**: Virtual Machines with GPUs process certain types of tasks more efficiently than CPUs and are used for workloads that require the resources of graphics accelerators. These machines have dedicated graphics cards and are ideal for complex computations such as CAD, AI/ML, or rendering.

* **Basic VM**: Machines that work with partial core use and are designed to run applications that don’t require high performance. 

* **High-frequency**: Best fit for applications that require single-threaded performance.

* **SGX-based VMs**: Virtual Machines that support Intel SGX technology and are suitable for storing critical, sensitive data by applying confidential computing.

* **VMs with a Trusted Platform Module (TPM)**: Suitable for a diverse array of secure workloads that demand robust hardware-based security features.

Check out the following sections for a detailed overview of these VM types and applicable use cases. 

## Standard

These Virtual Machines are designed for a wide range of tasks that require predictable performance. They balance compute, memory, and networking resources and can be used as the default choice for most workloads. 

**Use cases**

Applications that use these resources in equal proportions, such as web servers and code repositories.

<tabset-element>

### A1

Machines equipped with the industry’s first cloud-native, **128-core ARM Ampere Altra Max Family** processors. 

Based on 64-bit ARM architecture that’s optimized for cloud workloads, these VMs deliver predictable high performance to meet the demands of modern data centers and scalable cloud applications.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>a1-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>a1-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>a1-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>a1-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>a1-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>a1-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>a1-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>a1-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>a1-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>a1-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>                                
</thead>
</table> 

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>a1w-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>a1w-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>a1w-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>a1w-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>a1w-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>a1w-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>a1w-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>a1w-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>a1w-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>a1w-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>                                
</thead>
</table> 

### G1 

Machines equipped with newer generations of CPU:

* **Intel® Xeon® E Family (E-2288G)**: targeted at entry-level and medium applications, these VMs balance performance, cost-effectiveness, and power efficiency. Suitable for operations that don’t require high computing resources or memory-extensive tasks. 

* **2nd Gen Intel® Xeon® Scalable Processors**: optimized for demanding workloads, such as high-performance computing, advanced analytics, and artificial intelligence. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g1-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g1-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>g1-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>g1-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>                                
</thead>
</table> 

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1w-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1w-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1w-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g1w-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g1w-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1w-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1w-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1w-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>g1w-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>g1w-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>                                
</thead>
</table> 

### G2

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g2-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g2-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g2-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>g2-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>g2-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>  
    <tr>
   <td>g2-standard-32-128</td>
   <td>32</td>
   <td>128</td>
    </tr>                                    
</thead>
</table> 

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2w-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2w-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2w-standard-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g2w-standard-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g2w-standard-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2w-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2w-standard-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g2w-standard-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>     
    <tr>
   <td>g2w-standard-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>     
    <tr>
   <td>g2w-standard-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>                                   
</thead>
</table> 

### G0

Machines powered with **Intel Xeon E3-E5 Family** processors. Designed for a wide range of workloads and reliable performance.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g0-standard-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g0-standard-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g0-standard-4-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g0-standard-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>                                 
</thead>
</table>

</tabset-element>

## GPU

Production-grade instances designed for AI and compute-intensive workloads.

**Use cases**

Artificial Intelligence and Machine Learning, Computer-Aided Design (CAD), rendering.

<tabset-element>

### G1

Machines powered with the **2nd Generation Intel Xeon Scalable Processors** and **Nvidia Graphic Cards**. Nvidia GPUs enable parallel processing of multiple matrix operations and calculations. As a result, GPUs complete AI training tasks much faster than traditional CPUs.

Well-suited for compute-intensive workloads, including dynamic programming algorithms, video rendering, and scientific simulations.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-gpu-4-16-1</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1-gpu-8-32-1</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1-gpu-8-32-2</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1-gpu-16-64-4</td>
   <td>16</td>
   <td>64</td>
    </tr>   
    <tr>
   <td>g1-gpu-32-128-4</td>
   <td>32</td>
   <td>128</td>
    </tr>                                     
</thead>
</table>

#### Windows-based VMs 

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1w-gpu-4-16-1</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1w-gpu-8-32-1</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1w-gpu-8-32-2</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1w-gpu-16-64-4</td>
   <td>16</td>
   <td>64</td>
    </tr>   
    <tr>
   <td>g1w-gpu-32-128-4</td>
   <td>32</td>
   <td>128</td>
    </tr>                                     
</thead>
</table>

### G2 

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-gpu-4-16-a2-1</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2-gpu-8-32-a2-1</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g2-gpu-8-32-a2-2</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>    
   <td>g2-gpu-16-64-a2-4</td>
   <td>16</td>
   <td>64</td>
    </tr>   
    <tr>
   <td>g2-gpu-32-128-a2-4</td>
   <td>32</td>
   <td>128</td>
    </tr>                                     
</thead>
</table>

### GPU-G1

Machines equipped with the **Intel® Xeon® E Family (E-2288G)** processor. 

Targeted at entry-level and medium applications, these VMs offer a balance of performance, cost-effectiveness, and power efficiency. Suitable for operations that don’t require high computing resources or memory-extensive tasks.  

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-gpuhf-4-16-1</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1-gpuhf-8-32-1</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1-gpuhf-8-32-2</td>
   <td>8</td>
   <td>32</td>
    </tr>
    <tr>    
   <td>g1-gpuhf-16-64-4</td>
   <td>16</td>
   <td>64</td>
    </tr>   
    <tr>
   <td>g1-gpuhf-32-128-4</td>
   <td>32</td>
   <td>128</td>
    </tr>                                     
</thead>
</table>

</tabset-element>

## CPU

Production-grade machines that are designed for high workloads with intensive CPU usage.

**Use cases**

Big data packet processing, video coding, huge builds.

<tabset-element>

### G1

Machines powered with the **2nd Gen Intel® Xeon® Scalable Processors**. 

Optimized for demanding workloads like high-performance computing, advanced analytics, and artificial intelligence.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-cpu-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1-cpu-4-4</td>
   <td>4</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1-cpu-8-8</td>
   <td>8</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g1-cpu-16-16</td>
   <td>16</td>
   <td>16</td>
    </tr>   
    <tr>
   <td>g1-cpu-32-32</td>
   <td>32</td>
   <td>32</td>
    </tr>                                     
</thead>
</table>

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1w-cpu-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1w-cpu-4-4</td>
   <td>4</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1w-cpu-8-8</td>
   <td>8</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g1w-cpu-16-16</td>
   <td>16</td>
   <td>16</td>
    </tr>   
    <tr>
   <td>g1w-cpu-32-32</td>
   <td>32</td>
   <td>32</td>
    </tr>                                     
</thead>
</table>

### G2

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-cpu-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2-cpu-4-4</td>
   <td>4</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2-cpu-8-8</td>
   <td>8</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g2-cpu-16-16</td>
   <td>16</td>
   <td>16</td>
    </tr>   
    <tr>
   <td>g2-cpu-32-32</td>
   <td>32</td>
   <td>32</td>
    </tr>                                     
</thead>
</table>

### A1

Machines powered with the cloud-native **ARM Ampere Altra Max Family** processor. 

Optimized for cloud workloads, these VMs deliver predictable high performance to meet the demands of modern data centers and scalable cloud applications.

**Use cases**

Applications that take advantage of scale-out and elastic cloud architectures. 

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>a1-cpu-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>
   <td>a1-cpu-4-4</td>
   <td>4</td>
   <td>4</td>
    </tr>
    <tr>
   <td>a1-cpu-8-8</td>
   <td>8</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>a1-cpu-16-16</td>
   <td>16</td>
   <td>16</td>
    </tr>   
    <tr>
   <td>a1-cpu-32-32</td>
   <td>32</td>
   <td>32</td>
    </tr>                                     
</thead>
</table>

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>a1w-cpu-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>
   <td>a1w-cpu-4-4</td>
   <td>4</td>
   <td>4</td>
    </tr>
    <tr>
   <td>a1w-cpu-8-8</td>
   <td>8</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>a1w-cpu-16-16</td>
   <td>16</td>
   <td>16</td>
    </tr>   
    <tr>
   <td>a1w-cpu-32-32</td>
   <td>32</td>
   <td>32</td>
    </tr>                                     
</thead>
</table>

</tabset-element>

## Memory

Production-grade instances designed for workloads that rely heavily on RAM for optimal performance. 

**Use cases**

Databases

<tabset-element>

### G1

Machines powered with the **Intel® Xeon® Ice-Lake 2nd Generation** and **Intel® Xeon® Scalable Processors**. 

Optimized for demanding workloads, such as high-performance computing, advanced analytics, and artificial intelligence.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-memory-2-16</td>
   <td>2</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1-memory-4-32</td>
   <td>4</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1-memory-8-64</td>
   <td>8</td>
   <td>64</td>
    </tr>
    <tr>    
   <td>g1-memory-16-128</td>
   <td>16</td>
   <td>128</td>
    </tr>   
    <tr>
   <td>g1-memory-32-256</td>
   <td>32</td>
   <td>256</td>
    </tr>                                     
</thead>
</table>

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1w-memory-2-16</td>
   <td>2</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g1w-memory-4-32</td>
   <td>4</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g1w-memory-8-64</td>
   <td>8</td>
   <td>64</td>
    </tr>
    <tr>    
   <td>g1w-memory-16-128</td>
   <td>16</td>
   <td>128</td>
    </tr>   
    <tr>
   <td>g1w-memory-32-256</td>
   <td>32</td>
   <td>256</td>
    </tr>                                     
</thead>
</table>

### G2

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-memory-2-16</td>
   <td>2</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2-memory-4-32</td>
   <td>4</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g2-memory-8-64</td>
   <td>8</td>
   <td>64</td>
    </tr>
    <tr>    
   <td>g2-memory-16-128</td>
   <td>16</td>
   <td>128</td>
    </tr>   
    <tr>
   <td>g2-memory-32-256</td>
   <td>32</td>
   <td>256</td>
    </tr>                                     
</thead>
</table>

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2w-memory-2-16</td>
   <td>2</td>
   <td>16</td>
    </tr>
    <tr>
   <td>g2w-memory-4-32</td>
   <td>4</td>
   <td>32</td>
    </tr>
    <tr>
   <td>g2w-memory-8-64</td>
   <td>8</td>
   <td>64</td>
    </tr>
    <tr>    
   <td>g2w-memory-16-128</td>
   <td>16</td>
   <td>128</td>
    </tr>   
    <tr>
   <td>g2w-memory-32-256</td>
   <td>32</td>
   <td>256</td>
    </tr>                                     
</thead>
</table>

### A1

Machines powered with the cloud-native **ARM Ampere Altra Max Family** processor. 

Optimized for cloud workloads, these VMs deliver predictable high performance to meet the demands of modern data centers and scalable cloud applications.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>a1-memory-2-16</td>
   <td>2</td>
   <td>16</td>
    </tr>
    <tr>
   <td>a1-memory-4-32</td>
   <td>4</td>
   <td>32</td>
    </tr>
    <tr>
   <td>a1-memory-8-64</td>
   <td>8</td>
   <td>64</td>
    </tr>
    <tr>    
   <td>a1-memory-16-128</td>
   <td>16</td>
   <td>128</td>
    </tr>   
    <tr>
   <td>a1-memory-32-256</td>
   <td>32</td>
   <td>256</td>
    </tr>                                     
</thead>
</table>

</tabset-element>

## High-frequency

These VMs have a high processor clock speed, starting at 3.7 GHz in the base configuration. Suitable for applications that require single-threaded performance, using a single CPU core for optimized performance and speed.

The configuration with a large amount of memory also allows you to efficiently work with large databases. 

**Use cases**

Financial and probabilistic analytics, automation of computational processes. 

<tabset-element>

### G1

Machines powered with the following processors: 

* **Intel Xeon E Family**: specifically targeted at entry-level and small business servers, offering a balance of performance and cost-effectiveness for these environments.

* **Intel Xeon 2nd Generation Scalable Processors**: optimized for demanding workloads, such as high-performance computing, advanced analytics, and artificial intelligence.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-highfreq-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1-highfreq-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1-highfreq-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g1-highfreq-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>                                   
</thead>
</table>

#### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1w-highfreq-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1w-highfreq-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1w-highfreq-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g1w-highfreq-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>                                   
</thead>
</table>

</tabset-element>

## Basic VM

Shared Virtual Machine with partial core usage. Cost-effective solution featuring Intel Xeon 4314 CPU, ideal for light web servers and microservices. Suitable for operations that don’t require high computing resources or memory-extensive tasks.

**Use cases**

File sharing or storage, backup services, web hosting of small websites, or private VPN deployment.

<tabset-element>

### G1-shared

Powered with **Intel Xeon E3-V5 Family** processors.

### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1s-shared-1-0.5</td>
   <td>1</td>
   <td>0.5</td>
    </tr>
    <tr>
   <td>g1s-shared-1-1</td>
   <td>1</td>
   <td>1</td>
    </tr>
    <tr>
   <td>g1s-shared-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>    
   <td>g1s-shared-2-2</td>
   <td>2</td>
   <td>2</td>
    </tr>
    <tr>    
   <td>g1s-shared-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>                                       
</thead>
</table>

### G2-shared

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2s-shared-1-2-25</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2s-shared-1-2-50</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2s-shared-2-4-50</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>    
   <td>g2s-shared-2-4-80</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>    
   <td>g2s-shared-4-8-80</td>
   <td>4</td>
   <td>8</td>
    </tr> 
    <tr>    
   <td>g2s-shared-4-8-160</td>
   <td>4</td>
   <td>8</td>
    </tr> 
    <tr>    
   <td>g2s-shared-8-16-160</td>
   <td>8</td>
   <td>16</td>
    </tr> 
    <tr>    
   <td>g2s-shared-8-16-320</td>
   <td>8</td>
   <td>16</td>
    </tr>                                                   
</thead>
</table>

</tabset-element>

## SGX-enabled 

Machines designed to build secure enclave-based applications. Allow isolating private areas of your code and data in enclaves to ensure protection against disclosure or modification.

**Use cases**

Application code storage, critical or sensitive data in the cloud.

<tabset-element>

### G1

Powered with the **Intel Xeon E Family Processors + SGX support** (kernel).  

### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g1-sgx-1-2-5</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g1-sgx-2-4-11</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g1-sgx-4-8-22</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g1-sgx-8-16-45</td>
   <td>8</td>
   <td>16</td>
    </tr>                                    
</thead>
</table>

### G2

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-sgx-1-2-1</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2-sgx-2-4-2</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2-sgx-4-8-4</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g2-sgx-8-16-8</td>
   <td>8</td>
   <td>16</td>
    </tr>  
    <tr>    
   <td>g2-sgx-16-32-16</td>
   <td>16</td>
   <td>32</td>
    </tr>                                                                      
</thead>
</table>

### Windows-based VMs

Windows license is included.

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2w-sgx-1-2-1</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2w-sgx-2-4-2</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2w-sgx-4-8-4</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g2w-sgx-8-16-8</td>
   <td>8</td>
   <td>16</td>
    </tr>  
    <tr>    
   <td>g2w-sgx-16-32-16</td>
   <td>16</td>
   <td>32</td>
    </tr>                                                                      
</thead>
</table>

</tabset-element>

## TPM

Virtual Machines with a **Trusted Platform Module** (TPM) are suitable for a diverse range of workloads that demand robust hardware-based security features.

**Use cases**

* **BitLocker Drive Encryption**: Secure entire disks with TPM-protected encryption keys, preventing unauthorized access even if the system is compromised.

* **Secure boot**: Ensure that the system boots using only software trusted by the manufacturer. TPM provides a secure environment to store cryptographic keys that verify the integrity of the boot process, detecting and preventing unauthorized changes to the boot loader or firmware.

* **Virtual smart cards**: Provide secure authentication without the need for physical hardware.

* **Credential Guard**: Isolate and protect user credentials using virtualization-based security (VBS). 

* **Digital Rights Management (DRM)**: Protect digital content from unauthorized access and distribution with TPM-stored encryption keys.

<tabset-element>

### G2

Machines powered with the following processors:

* **Intel® Xeon® Ice-Lake 3rd Generation**: new processors with built-in acceleration, increased RAM (up to 4 TB RAM expansion per processor), enhanced security (Integrated Intel <a href="https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/software-guard-extensions.html" target="_blank">SGX</a> and <a href="https://www.intel.com/content/www/us/en/products/docs/processors/xeon-accelerated/crypto-acceleration-solution-brief.html" target="_blank">Crypto Acceleration</a> technologies). Suitable for a wide range of applications, including cloud computing, AI/ML workloads, high-performance computing (HPC), virtualization, and enterprise applications.

* **Intel® Xeon® Scalable Processors**: Designed for scalability, performance, and versatility. These processors meet the diverse needs of data center workloads, ranging from entry-level to high-performance computing. Designed for a broader range of applications, including high-performance computing, virtualization, cloud computing, and enterprise workloads.

#### Linux-based VMs

<table>
<thead>
  <tr>
    <th style="width:50%"><strong>VM type</strong></th>
    <th style="width:25%"><strong>vCPU</strong></th>
    <th style="width:25%"><strong>RAM/memory (GB)</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>g2-tpm-1-2</td>
   <td>1</td>
   <td>2</td>
    </tr>
    <tr>
   <td>g2-tpm-2-4</td>
   <td>2</td>
   <td>4</td>
    </tr>
    <tr>
   <td>g2-tpm-2-8</td>
   <td>2</td>
   <td>8</td>
    </tr>
    <tr>
   <td>g2-tpm-4-8</td>
   <td>4</td>
   <td>8</td>
    </tr>
    <tr>    
   <td>g2-tpm-4-16</td>
   <td>4</td>
   <td>16</td>
    </tr>
    <tr>    
   <td>g2-tpm-8-16</td>
   <td>8</td>
   <td>16</td>
    </tr>  
    <tr>    
   <td>g2-tpm-8-32</td>
   <td>8</td>
   <td>32</td>
    </tr>  
    <tr>    
   <td>g2-tpm-16-32</td>
   <td>16</td>
   <td>32</td>
    </tr>  
    <tr>    
   <td>g2-tpm-16-64</td>
   <td>16</td>
   <td>64</td>
    </tr>  
     <tr>    
   <td>g2-tpm-32-64</td>
   <td>32</td>
   <td>64</td>
    </tr>     
     <tr>    
   <td>g2-tpm-32-128</td>
   <td>32</td>
   <td>128</td>
    </tr>                                                   
</thead>
</table>

</tabset-element>