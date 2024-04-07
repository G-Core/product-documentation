---
title: about-volumes
displayName: Overview
order: 10
published: true
toc:
   --1--Boot and regular volumes: "boot-and-regular-volumes"
   --1--Volume types: "available-volume-types"
pageTitle: Volumes and volume types | Gcore
pageDescription: Learn more about volume types: High IOPS SSD, Standard, Cold, Ultra, and SSD Low-Latency. Choose the right cloud storage for your data and workloads.
---
# Volumes

A volume is a file storage that is similar to traditional physical disks (SSD and HDD) but is located in the cloud.

When you create a new instance, you may need to store data or manage information. This is where volumes come in: They provide a convenient way to maintain information within the instance. Volumes are also essential for booting instances as they store an operating system and all files necessary for machine startup.

We use a software-defined distributed file system to store data. This system comprises a cluster of easily scalable nodes that provide storage, triple data replication, and load distribution, ensuring the high availability of volumes in our cloud infrastructure. 

## Boot and regular volumes

Each instance requires a volume to boot from. This volume is called a boot (or system) volume and is created based on an OS distribution image or custom image you’ve used for instance creation.

The boot volume cannot be deleted or detached from an instance as long as the instance exists. However, after you terminate the instance, you can keep the boot volume and its data and then use it to create another instance. 

A regular volume is a general-purpose storage volume used to retain any non-OS data in the cloud. 

<alert-element type="info" title="Info">
 
You can create snapshots both from the boot and regular volumes. For instructions, refer to this guide: <a href="https://gcore.com/docs/cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system" target="_blank">Take a snapshot of your file system</a>. 
 
</alert-element>

 ## Available volume types 

In the Gcore Customer Portal, you can create different types of volumes. For instructions on how to create a volume, check out our <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/create-and-configure-volumes" target="_blank">Create and configure volumes</a> guide.

You can check volume availability for a specific region on our website in the <a href="https://gcore.com/pricing/cloud" target="_blank">Gcore Cloud calculator</a>.

<table>
<thead>
<tr>
<th>Volume</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">High IOPS SSD</td>
<td style="text-align: left">This is a high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GB; 2.5 MB/s per 1 GB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.</td>
</tr>
<tr>
<td style="text-align: left">Standard</td>
<td style="text-align: left">This is a network SSD disk that provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.</td>
</tr>
<tr>
<td style="text-align: left">Cold</td>
<td style="text-align: left">This is a network HDD disk suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.
</td>
</tr>
<tr>
<td style="text-align: left">Ultra</td>
<td style="text-align: left">This is the network block storage option recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.
</td>
</tr>
<tr>
<td style="text-align: left">SSD Low-Latency</td>
<td style="text-align: left">This is an SSD block storage designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.
</td>
</tr>
</tbody>
</table>

For **Cold**, **High IOPS SSD**, and **Standard** volumes:

- Both volume IO (Input/Output) burst and volume throughput burst are supported.

- You get both IO and throughput credits to exceed base limits and ensure optimal performance at peak IOPS and throughput.

- Credits increase IOPS and volume throughput by 10x times for 10 minutes.

For example, your instance has a 3 GB High IOPS SSD volume with base limits of 180 IOPS and 7.5 MB (60 IOPS x 3 GB and 2.5 MB/s x 3 GB). If the IOPS and throughput values ​​exceed these limits, you’ll get renewable resources: (60 IOPS x 3 GB + 2.5 MB/s x 3 GB = 180 IOPS + 7.5 MB) x 10 = 1800 IOPS + 75 MB/s.

Credits are restored after peak usage and load reduction. If the base limits are exceeded again, renewed credits will also be applied.
