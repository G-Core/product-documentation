---
title: install-and-configure-logstash
displayName: Logstash
published: true
toc:
   --1--Install Logstash: "install-logstash"
   --1--Configure Logstash: "configure-logstash"
pageTitle: Install and Configure Logstash | Gcore
pageDescription: Easily install and configure Logstash, a log shipping tool, to collect and send logs to Gcore's logging servers.
---
# Install and configure Logstash

Logstash is an open-source data collection and processing tool. It’s used to collect, parse, enrich, and transform log data from various sources, including log files, event streams, and databases.

## Install Logstash

You can download Logstash from the <a href="https://www.elastic.co/logstash" target="_blank">official Elastic website</a>. 

## Configure Logstash

A standard Logstash configuration consists of three sections: `input`, `filter`, and `output`. The `input` and `filter` sections depend on the sources of logs.

To send logs to Gcore LaaS (Logging as a Service), you need to configure Logstash with Kafka output and enable the <a href="https://github.com/logstash-plugins/logstash-integration-kafka" target="_blank">Kafka Integration Plugin</a> in your Logstash installation.

1\. Configure Logstash with Kafka output by adding the following data to the `logstash.conf` file:

<code-block>
output {
        kafka {
          codec => json
          topic_id => <span style="color:#FF5913">"yourlogin.yourtopic"</span>
          bootstrap_servers => <span style="color:#FF5913">"endpoint"</span>
          sasl_mechanism => "SCRAM-SHA-512"
          security_protocol => "SASL_SSL"
          sasl_jaas_config => "org.apache.kafka.common.security.scram.ScramLoginModule required username=<span style="color:#FF5913">'yourlogin'</span>password=<span style="color:#FF5913">'yourpassword'</span>; "
          key_serializer => "org.apache.kafka.common.serialization.StringSerializer"
          value_serializer => "org.apache.kafka.common.serialization.StringSerializer"
        }
    }
</code-block>

Customize the highlighted values:

- <span style="color:#FF5913">yourlogin.yourtopic</span>: Your username and topic name separated with a dot (.)
- <span style="color:#FF5913">endpoint</span>: Kafka endpoint
- <span style="color:#FF5913">yourlogin.yourtopic</span>: Your login
- <span style="color:#FF5913">yourpassword</span>: Your password

<alert-element type="tip" title="Tip">
 
You can find your username, password, login, and topic name information in the Gcore Customer Portal on the **Logging** page. Learn more about logging configuration in the <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">Configure Logging and view your logs</a> guide.
 
</alert-element>

For more settings, check out <a href="https://www.elastic.co/guide/en/logstash/current/plugins-outputs-kafka.html" target="_blank">Kafka output plugin</a> documentation. 

<expandable-element title="Descriptions of the “output” parameters">

- **topic_id**: ID of a Kafka topic to which Logstash will publish messages.
- **bootstrap_servers**: A comma-separated list of Kafka broker addresses.
- **sasl.mechanism**: Authentication mechanism that helps to verify a username and password entered to sign in your logs storage.  
- **security_protocol**: Security protocol used to encrypt your data and protect it from theft.  
- **sasl_jaas_config**: JAAS configuration that's required for SASL authentication.   
- **key_serializer**: Serialization format used to convert keys of messages sent to Kafka.
- **value_serializer**: Serialization method applied to the content of messages before they are transmitted to Kafka.

</expandable-element> 

2\. Save the changes in the Logstash configuration file.

3\. Restart Logstash. It will start sending logs to your Gcore logging storage. 
