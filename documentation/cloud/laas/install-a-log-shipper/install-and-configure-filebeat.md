---
title: install-and-configure-filebeat
displayName: Filebeat
published: true
toc:
   --1--What is Filebeat?: "what-is-filebeat"
   --1--Install: "install-filebeat"
   --1--Configure: "configure-filebeat-for-logging"
---
  
  

What is Filebeat?  
-------------------

Filebeat is a log shipping tool. This is a service that collects logs from a device and sends them to an external storage.  

How does it work? In the Filebeat settings, you specify a source of the logs you need — for example, logs of a specific service, internal storage, TCP port, OS events, or other. Besides, you indicate a location for log export — our Logging servers. After that, Filebeat works automatically: once a required log is recorded in the system, the log shipper transfers it to our storage, and the log appears on OpenSearch Dashboards.  

Install Filebeat  
------------------

An up-to-date link for Filebeat installation is on its official page. Open the Filebeat website and click "Download".  

[Filebeat official webpage](https://www.elastic.co/beats/filebeat) 

Configure Filebeat for Logging  
--------------------------------

You need to fill in the Filebeat configuration file. It consists of two sections: "inputs" and "outputs". The "inputs" section determines a source of the logs that the log shipper collects, and "outputs" shows a destination where to send them. Below we will describe how to write out the file correctly.  

1\. Open the filebeat.yml file.

2\. Copy the data below to this file. 

filebeat.inputs:   
\- type: log   
  enabled: true   
  paths:   
   - **(path to one or several log files)**   
  
output.kafka:   
  hosts: \["**(Kafka Endpoint shown on the Logging page)**"\]   
  topic: **'(****name of your topic shown on the Logging page)****'**   
  sasl.mechanism: SCRAM-SHA-512   
  username: **(your username generated on the Logging page)**   
  password: **(your password generated on the Logging page)**   
  ssl.enabled: **true** 

3\. Fill in the "inputs" section.

If you want to collect logs from a specific file, fill out the brackets with the file path and remove the brackets. If you want to collect logs from multiple files in the same folder, fill out the brackets with a path to one of the files, replace its name with an asterisk, and remove the brackets.

For example, if several of your log files are in the _/var/log/_ directory, the "inputs" configuration should be as follows: 

filebeat.inputs:   
\- type: log   
  enabled: true   
  paths:   
   - /var/log/\*.log 

Logs can also be collected from other sources — for example, you can create an HTTP listener and record all HTTP POST requests. To gather logs not from a specific file, open [the "Configure inputs" section of the Filebeat documentation,](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html) go to the bottom of the page and click the link with the log source you need and configure the "inputs" section according to the guide.  

4\. Fill in the "outputs" section.

Fill out the brackets with your data and remove the brackets. For example, you have the following data:

*   The login is _ExAmPlElOgIn._
*   The password is _ExAmPlEPaSsWoRd._
*   The topic name is _Exampletopic._
*   The Kafka Endpoint on the Logging page in your control panel is _laas-example.gcore.com:443._

Then you need to fill in the "outputs" data as follows:

output.kafka:   
  hosts: \["laas-example.gcore.com:443"\]   
  topic: 'Exampletopic'   
  sasl.mechanism: SCRAM-SHA-512   
  username: ExAmPlElOgIn   
  password: ExAmPlEPaSsWoRd   
  ssl.enabled: true 

And the final configuration will be as follows: 

filebeat.inputs: 
- type: log 
  enabled: true 
  paths: 
   - /var/log/\*.log 

output.kafka: 
  hosts: \["laas-example.gcore.com:443"\] 
  topic: 'ExAmPlElOgIn.Exampletopic' 
  sasl.mechanism: SCRAM-SHA-512 
  username: ExAmPlElOgIn 
  password: ExAmPlEPaSsWoRd 
  ssl.enabled: true

Each string of the "outputs" section sets a specific configuration of log export:

*   output.kafka — type of servers for log export specified after the dot (in this case, Kafka servers).  
*   hosts — address of server(s) where the logs will be exported to.  
*   topic — name of the topic where the logs will be exported to.  
*   sasl.mechanism — authentication mechanism that helps to verify a username and password entered to sign in to your logs storage.  
*   sasl.username — your username that helps to verify that it is you who is trying to send data.  
*   password — your password that helps to verify that it is you who is trying to send data.  
*   ssl.enabled — an indication that a security protocol is enabled to encrypt your data and protect it from theft.  

5\. Save the changes in the Filebeat configuration file.

6\. Restart Filebeat, and it will begin sending logs to the Logging storage.