---
title: about-logging-as-a-service
displayName: Overview
order: 10
published: true
toc:
   --1--What is Logging?: "what-is-logging"
   --1--How does it work?: ""
   --1--How it may be useful: "how-logging-can-be-useful"
   --1--Use cases: "use-cases"
   --1--How we store logs: "how-we-store-logs"
   --1--Logging restrictions: "logging-restrictions"
   --1--Compatibility of our LaaS and log shippers: "compatibility-of-our-laas-and-log-shippers"
---
  
 [](#)  
  
  
  

What is Logging?  
------------------

Logging (also known as LaaS, logging as a service) is a service used to collect and store logs from virtual machines and baremetal servers. It doesn't matter whether you use a Gcore server or your own: Logging will collate logs from any devices. You can work with logs via OpenSearch Dashboards.

How does Logging work? 
-----------------------

1.  We allocate storage space for your logs.  
2.  You install a log shipper on your servers — the tool collects logs and forwards them to our storage. For example, you can install [Fluent Bit](https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit) or [Filebeat](https://www.elastic.co/beats/filebeat) log shipper.
3.  You configure the log shipper by specifying which services' logs need to be exported to the storage. If you haven’t worked with a log shipper before, you can use our guides: [Configure Fluent Bit](https://support.gcore.com/hc/en-us/articles/6173162093201), [Configure Filebeat](https://support.gcore.com/hc/en-us/articles/6171869217937). 
4.  Logs from your machine are automatically exported to the storage.  
5.  You work with the logs of your resources via OpenSearch Dashboards that we provide. 

How Logging can be useful 
--------------------------

Logging collects logs from different services into one dashboard. To find the cause of an error or to collect data for analytics, you do not have to manually open logs of each service or machine — all data is available in OpenSearch Dashboards. You can apply filters to see the required logs.  

Logs are still available even if their source is destroyed — for example, a server is broken, or a Kubernetes pod is deleted. By opening the Logging tab, you can see what happened to a machine before the breakdown or to an object before the deletion.  

Use cases  
-----------

With Logging, you can see how the system has changed. Below are four cases when the service may be useful.  

**Quicker detection and resolution of errors in a cluster.** You enter an error message into the OpenSearch Dashboards search bar, identify when and which server experienced an issue, and fix it.  

**Investigation of security incidents.** For example, if data on your server was stolen last month, you can find logs from that time period, see which account signed in to the storage, and detect the culprit.  

**Server connectivity check.** You open logs of two servers for the same time interval and see whether all the data has reached an end-user.  

**Data speed measurement**. You open logs and compare the time when one server sent the data with the time when another one received it.  

How we store logs  
-------------------

Logs from your machines are exported to Kafka servers, which then send them to OpenSearch servers for permanent storage. You read the logs from the OpenSearch servers via OpenSearch Dashboards.

We use Kafka servers as a buffer for better reliability. Even if an OpenSearch server fails to receive logs, they will be saved in Kafka and sent to OpenSearch as soon as possible. We have built such a system to ensure the safety of your data. 

Logging restrictions
--------------------

Please note that Logging has several restrictions that ensure that the logging system runs effectively.  

1.  Incoming traffic to Kafka: <10 Mb/sec
2.  Overall incoming traffic: ~900Gb/day
3.  Retention period in OpenSearch: 45 days
4.  Maximum fields in a JSON log: 225 fields 
5.  Maximum message size: 1 MB
6.  Message format: text/JSON

Compatibility of our LaaS and log shippers
------------------------------------------

The table below shows what log shippers are compatible with different operating systems in our Cloud. 

| OS\\ Log shipper | Fluent Bit | Filebeat | Promtail | Logstash | Syslog |
|------------------|------------|----------|----------|----------|--------|
| Ubuntu 20.04     |  -         |  +       |  -       |  +       |  -     |
| Ubuntu 22.04     |  -         |  +       |  -       |  +       |  -     |
| CentOS 7         |  +         |  +       |  -       |  +       |  -     |
| CentOS 8 Stream  |  -         |  +       |  -       |  +       |  -     |
| CentOS 9 Stream  | -          | +        | -        | +        | -      |
