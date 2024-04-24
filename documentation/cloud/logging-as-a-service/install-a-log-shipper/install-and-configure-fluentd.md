---
title: install-and-configure-fluentd
displayName: Fluentd
published: true
toc:
  --1--Install Fluentd: "install-fluentd"
  --1--Configure Fluentd: "configure-fluentd"
pageTitle: Install and Configure Fluentd | Gcore
pageDescription: Install and configure Fluentd, a log shipping tool, to collect and send logs to Gcore's logging servers.
---
# Install and configure Fluentd

Fluentd is a data collection and processing tool that supports multiple input sources, data formats, and output destinations. This allows you to stream and consolidate logs from different applications into one unified format and send this information to the Gcore Managed Logging.

## Install Fluentd

Download Fluentd from the <a href="https://www.fluentd.org/download" target="_blank">official Fluentd website</a> and install it using your preferred method.

## Configure Fluentd

A standard Fluentd configuration consists of three sections: `input`, `filter`, and `output`. The `input` and `filter` sections depend on the sources of logs.

To send logs to Gcore Managed Logging, configure Fluentd with the <a href="https://github.com/fluent/fluent-plugin-kafka" target="_blank">Kafka Integration Plugin</a> in your Fluentd installation.

1\. Configure Fuentd with Kafka output by adding the following data to the `fluent.conf` file:

<code-block>

\<match pattern>
  @type kafka2

  \# list of seed brokers
  brokers <span style="color:#FF5913">laas-example.gcore.com:443</span>
  username: <span style="color:#FF5913">username</span>
  password: <span style="color:#FF5913">password</span>
  scram_mechanism: "sha512"
  default_topic: namespace_username.topic_name
  sasl_over_ssl: true

  \# buffer settings
  \<buffer>
    @type memory
    ## OPTIONAL PARAMS
    timekey: 30s
    timekey_wait: 10s
    timekey_use_utc: true
    chunk_limit_size: 4MB
    total_limit_size: 64MB
    chunk_full_threshold: "0.9"
    queued_chunks_limit_size: 12
    flush_thread_count: 12
  \</buffer>

  \# data type settings
  \<format>
    @type json
  \</format>
\</match>

</code-block>

2\. Customize the highlighted values:

- <span style="color:#FF5913">brokers</span>: Kafka servers where logs will be exported to.

- <span style="color:#FF5913">username</span>: Your username

- <span style="color:#FF5913">password</span>: Your password

- <span style="color:#FF5913">default_topic</span>: Your username and topic name, separated with a dot (.)

<alert-element type="tip" title="Tip">
 
You can find your username, password, and topic name information in the Gcore Customer Portal on the **Logging** page. Learn more about logging configuration in <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">our dedicated guide</a>.
 
</alert-element>

For more settings, check out the <a href="https://docs.fluentd.org/output/kafka" target="_blank">official Fluentd documentation</a>. 

<expandable-element title="Descriptions of the “output” parameters">

- **brokers**: Kafka servers where Fluentd logs will be sent to.
- **scram_mechanism**: Authentication mechanism that verifies a username and password entered to sign in your logs storage.
- **default_topic**: Kafka topic where logs will be exported to.
- **sasl_over_ssl**: When this parameter is set to “true”, the system will use  SASL for authentication and SSL for secure communication. 

</expandable-element> 

3\. Save the changes in the Fluentd configuration file.

4\. Restart Fluentd. It will start sending logs to the Gcore Managed Logging.