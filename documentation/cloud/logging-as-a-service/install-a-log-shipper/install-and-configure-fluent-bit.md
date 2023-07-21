---
title: install-and-configure-fluent-bit
displayName: Fluent Bit
published: true
toc:
   --1--What is Fluent Bit?: "what-is-fluent-bit"
   --1--Install: "install"
   --1--Configure: "configure"
   --1--No timestamps: "no-timestamps"
pageTitle: Install and configure Fluent Bit| Gcore
pageDescription: Easily install and configure Fluent Bit, a log shipping tool, to collect and send logs to Gcore's Logging servers.
---
# Install and configure Fluent Bit

## What is Fluent Bit?  

Fluent Bit is a log shipping tool. This means that it is a service that collects logs from a device and sends them to an external storage.

In Fluent Bit’s Settings, you specify a source of the logs you need, for example, logs of a specific service, internal storage, TCP port, or OS events. You must indicate a destination for log export—Gcore’s Logging servers. After that, Fluent Bit works automatically: Once a required log is recorded in the system, the log shipper transfers it to our storage, and the log appears on OpenSearch Dashboards.

## Install

Fluent Bit’s <a href="https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit" target="_blank">official documentation</a> provides up-to-date installation guides for different operating systems. <a href="https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit" target="_blank">Open this link</a> and select your OS. Simply follow the steps in the relevant installation manual.

## Configure 

The Fluent Bit configuration file consists of two sections: `INPUT` and `OUTPUT`. `INPUT` determines the source of the logs you need to collect, and `OUTPUT` indicates the destination where they will be sent. Here’s how to set up the configuration file correctly:

1. Open the `fluent-bit.conf` file and add the following data:

<code-block>
[INPUT]  
    Name        <span style="color:#FF5913">tail</span>
    Path        <span style="color:#FF5913">/var/log/syslog</span>
[OUTPUT]   
    name        kafka    
    brokers       <span style="color:#FF5913">laas-example.gcore.com:443</span>  
    topics        <span style="color:#FF5913">yourlogin.yourtopic</span>   
    rdkafka.security.protocol        SASL_SSL    
    rdkafka.sasl.mechanism        SCRAM-SHA-512   
    rdkafka.sasl.username       <span style="color:#FF5913">yourlogin</span>
    rdkafka.sasl.password       <span style="color:#FF5913">yourpassword</span> 
</code-block>

Customize the highlighted values:

- <span style="color:#FF5913">tail</span>: Data source
- <span style="color:#FF5913">/var/log/syslog</span>: File path 
- <span style="color:#FF5913">laas-example.gcore.com:443</span>: Kafka Endpoint on the Logging page
- <span style="color:#FF5913">yourlogin.yourtopic</span>: Your username on the Logging page and your topic name separated with a dot (.)
- <span style="color:#FF5913">yourlogin</span>: Your username on the Logging page
- <span style="color:#FF5913">yourpassword</span>: Your password

For more information on how to add `INPUT` for different log sources, go to the <a href="https://docs.fluentbit.io/manual/pipeline/inputs" target="_blank">"Input" section of the Fluent Bit documentation</a> and click the log source you need. 

For example, if you want to gather logs from a specific file, open the <a href="https://docs.fluentbit.io/manual/pipeline/inputs/tail" target="_blank">guide for Tail</a>. Tail is a utility on UNIX-like systems used to display the tail end of a file. It helps Fluent Bit to read changes in the log file. You need to fill in the `INPUT` so that it corresponds with Tail.

<expandable-element title="Descriptions of the OUTPUT strings">

- **[OUTPUT]**: Type of process (export).  
- **name**: Servers where logs will be delivered (Kafka servers).  
- **brokers**: Server(s) where logs will be exported to.  
- **topics**: Topic(s) where logs will be exported to.  
- **rdkafka.security.protocol**: Security protocol that encrypts data to protect it from theft.  
- **rdkafka.sasl.mechanism**: Authentication mechanism that helps to verify a login and a password entered to sign into your logs storage.  
- **rdkafka.sasl.username**: The username that helps to verify the sender.  
- **rdkafka.sasl.password**: The password that helps to verify the sender.

</expandable-element>

2. Save the changes in the `fluent-bit.conf` file.

3. Restart Fluent Bit, and it will begin sending logs to your Gcore Logging storage.

## No timestamps  

Some services (for example, nginx) transmit timestamps of logs in a non-standard format. In this case, OpenSearch Dashboards will show logs without their date and time. If this happens, copy the string below to the `OUTPUT` section. This will ensure that Fluent Bit forwards date and time in a different format that is suitable for services like nginx.

```
    timestamp_format        iso8601
```