---
title: install-and-configure-filebeat
displayName: Filebeat
published: true
toc:
   --1--What is Filebeat?: "what-is-filebeat"
   --1--Install: "install"
   --1--Configure: "configure"
pageTitle: Install and configure Filebeat| Gcore
pageDescription: Easily install and configure Filebeat, a log shipping tool, to collect and send logs to Gcore's Logging servers.
---
# Install and configure Filebeat

## What is Filebeat?  

Filebeat is a log shipping tool. It collects logs from a device and sends them to an external storage.

In Filebeat’s Settings, specify a source of the logs you need, for example, logs of a specific service, internal storage, TCP port, or OS events. Indicate a location for log export—Gcore’s Logging servers. After that, Filebeat works automatically: once a required log is recorded in the system, the log shipper transfers it to our storage, and the log appears on OpenSearch Dashboards. 

## Install

An up-to-date link for Filebeat installation is available on its <a href="https://elastic.co/beats/filebeat" target="_blank">Filebeat official webpage</a>. Open the Filebeat website and click **Download**.

## Configure 

The Filebeat configuration file consists of two sections: `inputs` and `output`. `inputs` determines the source of the logs you need to collect, and `output` indicates the destination where they will be sent. Here’s how to set up the configuration file correctly:

1. Open the `filebeat.yml` file and add the following data:

<code-block>
filebeat.inputs:   
- type: log   
  enabled: true   
  paths:   
   - <span style="color:#FF5913">/var/log/*.log</span>    
output.kafka:   
  hosts: [<span style="color:#FF5913">"laas-example.gcore.com:443"</span>]   
  topic: '<span style="color:#FF5913">yourlogin.yourtopic</span>'  
  sasl.mechanism: SCRAM-SHA-512   
  username: <span style="color:#FF5913">yourlogin</span>   
  password: <span style="color:#FF5913">yourpassword</span>   
  ssl.enabled: true
</code-block>

Customize the highlighted values:
- <span style="color:#FF5913">/var/log/*.log</span>: File(s) path
- <span style="color:#FF5913">laas-example.gcore.com:443</span>: Kafka Endpoint on the Logging page
- <span style="color:#FF5913">yourlogin.yourtopic</span>: Your username on the Logging page and your topic name separated with a dot (.) 
- <span style="color:#FF5913">yourlogin</span>: Your username on the Logging page
- <span style="color:#FF5913">yourpassword</span>: Your password

You can also collect logs from other sources such as TCP, UDP, or syslog. For more details, refer to the <a href="https://elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html" target="_blank">"Configure inputs" section of the Filebeat documentation</a>: Click the log source you need, and configure the `inputs` section following the provided guide.

<expandable-element title="Descriptions of the OUTPUT strings">

- **output.kafka**: Servers for log export (Kafka servers). 
- **hosts**: Address of server(s) where logs will be exported to.  
- **topic**: Topic(s) where logs will be exported to.  
- **sasl.mechanism**: Authentication mechanism that helps to verify a username and password entered to sign into your logs storage.  
- **sasl.username**: Username that helps to verify the sender.  
- **password**: Password that helps to verify the sender.  
- **ssl.enabled**: Security protocol used to encrypt your data and protect it from theft (true).

</expandable-element> 

2. Save the changes in the Filebeat configuration file.

3. Restart Filebeat, and it will begin sending logs to your Gcore Logging storage.  