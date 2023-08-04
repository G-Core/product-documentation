---
title: about-logging-as-a-service
displayName: Overview
order: 10
published: true
toc:
   --1--What is Logging?: "what-is-logging"
   --1--Advantages: "advantages"
   --1--Use cases: "use-cases"
   --1--Log storage: "log-storage"
   --1--Restrictions: "restrictions"
pageTitle: Logging as a service| Gcore
pageDescription: Discover Logging for both VMs and bare metal servers. Troubleshoot errors, analyze security incidents and other data using OpenSearch Dashboards.
---
# About Managed Logging as a service

## What is Managed Logging?  

Managed Logging, also known as LaaS (logging-as-a-service,) is a service that collects and stores logs from both virtual machines and bare metal servers. Whether you are using Gcore’s infrastructure or your own server, logging can collect logs from any system. You can work with Logging via OpenSearch Dashboards.

## How Logging works

1. Install and configure any log shipper that supports Kafka. You can use <a href="https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit" target="_blank">Fluent Bit</a>, <a href="https://elastic.co/beats/filebeat" target="_blank">Filebeat</a>, or any other log source that can export logs to Kafka, such as a Python application with configured Kafka logger output.
2. Access the logs via OpenSearch Dashboards.

## Advantages

Logging compiles logs from different services into one system. To find the cause of an error or to collect data for analytics, you do not have to manually open logs of each service or machine; all data is readily available in OpenSearch Dashboards. You can customize the view or use filters for your needs. 

Logs are still available even if their source is destroyed—for example, a server is down or a Kubernetes pod is deleted. By opening the Logging tab, you can see what happened to a machine before its failure or to an object before its deletion.  

## Use cases  

The use cases of Logging include:  

1. **Error detection and troubleshooting**. Enter an error message into the OpenSearch Dashboards search bar, identify when and which server experienced an issue, and be empowered to fix it.  

2. **Investigation of security incidents**. By monitoring and analyzing logs, you can detect suspicious activities, unauthorized access attempts, or other potential security breaches.  
 
3. **Server connectivity check**. Open logs of two servers for the same time interval and see whether all data has reached an end user.  

4. **Data speed measurement**. Open logs and compare the time when one server sent the data with the time when another one received it.

## Log storage 

Logs from your machines are exported to Kafka servers, which then send them to OpenSearch servers for permanent storage. You can access and read the logs from the OpenSearch servers through OpenSearch Dashboards.

We use Kafka servers as a buffer for better reliability. Even if an OpenSearch server fails to receive logs, they will be saved in Kafka and sent to OpenSearch as soon as possible. This system also ensures the security of your data. 

## Restrictions

Please note that Logging has several restrictions that ensure that the Logging system runs effectively.  

1. Message format: text/JSON
2. Maximum fields in a JSON log: 225 fields 
3. Maximum message size: 1 MB
