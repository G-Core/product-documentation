---
title: about-volumes
displayName: Overview
order: 10
published: true
toc:
pageTitle: About volumes | Gcore
pageDescription: Learn more about volume types. High IOPS SSD, Standard, Cold, Ultra, and SSD Low-Latency. Choose the cloud storage for various data and workloads.
---
# About volumes

A volume is a file storage which is similar to traditional hard disks (SSD and HDD) but is located in the cloud.

Gcore Cloud uses a software-defined distributed file system to store data. This system comprises a cluster of easily scalable nodes that provide storage, triple data replication, and load distribution. These features ensure that volumes are highly available.

 When you connect to an instance, you may need to store data or manage information. This is where volumes come in - they provide a convenient way to store and manage data within the instance.

 ## Available volume types 
 
* **High IOPS SSD**. This is a high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

Availability: Amsterdam, Frankfurt, London, Luxembourg, Luxembourg-2, Manassas, Paris-2, Singapore

* **Standard**. This is a network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

Availability: all regions

* **Cold**. This is a network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **Ultra**. This is the network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **SSD Low-Latency**. This is an SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

Availability: Amsterdam-2, Frankfurt, Hong Kong, Luxembourg-2, Manassas, Tokyo