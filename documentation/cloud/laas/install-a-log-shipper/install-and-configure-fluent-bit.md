---
title: install-and-configure-fluent-bit
displayName: Fluent Bit
published: true
toc:
   --1--What is Fluent Bit?: "what-is-fluent-bit"
   --1--Install: "install-fluent-bit"
   --1--Configure: "configure-fluent-bit-for-logging"
   --1--What to do if logs have no timestamps: "what-to-do-if-logs-have-no-timestamps"
---
# Install and configure Fluent Bit

## What is Fluent Bit?  

Fluent Bit is a log shipping tool. This is a service that collects logs from a device and sends them to an external storage.  

How does it work? In the Fluent Bit settings, you specify a source of the logs you need — for example, logs of a specific service, internal storage, TCP port, OS events, or other. Besides, you indicate a destination for log export — our Logging servers. After that, Fluent Bit works automatically: once a required log is recorded in the system, the log shipper transfers it to our storage, and the log appears on OpenSearch Dashboards.  

## Install Fluent Bit  

The up-to-date installation guides for different operating systems are in the Fluent Bit official documentation. Open the link below and select your OS. You will find an installation manual that you need to follow. 

<a href="https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit" target="_blank">Fluent Bit Installation</a> 

## Configure Fluent Bit for Logging  

You need to fill in the Fluent Bit configuration file. It consists of two sections: INPUT and OUTPUT. INPUT determines the source of the logs you need to collect, and OUTPUT indicates the destination where to send them. Below we will describe how to write out the file correctly.  

1\. Open the fluent-bit.conf file.

2\. Copy the data below to this file. 

```
[OUTPUT]  
    name        kafka  
    brokers        Kafka Endpoint shown on the Logging page  
    topics        your username generated on the Logging page.your topic name shown on the Logging page   
    rdkafka.security.protocol        SASL_SSL    
    rdkafka.sasl.mechanism        SCRAM-SHA-512   
    rdkafka.sasl.username        your username generated on the Logging page   
    rdkafka.sasl.password        your password generated on the Logging page 
```

3\. Fill out the brackets with your data and remove the brackets.

For example, you have the following data:

- The login is ```ExAmPlElOgIn```.
- The password is ```ExAmPlEPaSsWoRd```.
- The topic name is ```Exampletopic```.
- The Kafka Endpoint on the Logging page in your control panel is ```laas-example.gcore.com:443```.

Then you need to fill in the data as follows: 

```
[OUTPUT]   
    name        kafka    
    brokers        laas-example.gcore.com:443   
    topics        ExAmPlElOgIn.Exampletopic   
    rdkafka.security.protocol        SASL_SSL    
    rdkafka.sasl.mechanism        SCRAM-SHA-512   
    rdkafka.sasl.username        ExAmPlElOgIn    
    rdkafka.sasl.password        ExAmPlEPaSsWoRd 
```

Each string in the OUTPUT section sets a specific configuration of log export:

- [OUTPUT] — type of process, "output" means export.  
- name — type of servers where logs will be delivered (in our case, it is Kafka servers).  
- brokers — address of server(s) where logs will be exported to.  
- topics — name of topic(s) where logs will be exported to.  
- rdkafka.security.protocol — type of security protocol that encrypts data to protect it from theft.  
- rdkafka.sasl.mechanism — authentication mechanism that helps to verify a login and password entered to sign in to your logs storage.  
- rdkafka.sasl.username — your username that helps to verify that it is you who is trying to send data.  
- rdkafka.sasl.password — your password that helps to verify that it is you who is trying to send data.

4\. Add the INPUT section above the OUTPUT section. To fill in the data, go to the <a href="https://docs.fluentbit.io/manual/pipeline/inputs" target="_blank">"Input" section of the Fluent Bit documentation</a>. Click the log source you need and configure everything according to the guide. 

For example, if you want to gather logs from a specific file, open the <a href="https://docs.fluentbit.io/manual/pipeline/inputs/tail" target="_blank">guide for Tail</a>. Tail is a utility on UNIX-like systems used to display the tail end of a file. It helps Fluent Bit to read changes in the log file. You need to fill in the INPUT so that it corresponds with Tail.

```
[INPUT]  
    Name        tail   
    Path        path to your file 
```

If your file path is */var/log/syslog*, the final Fluent Bit configuration will be as follows: 

```
[INPUT]   
    Name        tail   
    Path        /var/log/syslog   
```
```
[OUTPUT]   
    name        kafka    
    brokers        laas-example.gcore.com:443   
    topics        ExAmPlElOgIn.Exampletopic   
    rdkafka.security.protocol        SASL_SSL    
    rdkafka.sasl.mechanism        SCRAM-SHA-512   
    rdkafka.sasl.username        ExAmPlElOgIn    
    rdkafka.sasl.password        ExAmPlEPaSsWoRd 
```

5\. Save the changes in the fluent-bit.conf file.

6\. Restart Fluent Bit, and it will begin sending logs to a Logging storage. 

## What to do if logs have no timestamps  

Some services (for example, Nginx) transmit timestamps of logs in a non-standard format. In this case, OpenSearch Dashboards will show logs without date and time. If this is the case, copy the string below to the OUTPUT section — it will ensure that Fluent Bit forwards date and time in another format suitable for services like Nginx.  

```
    timestamp_format        iso8601
```