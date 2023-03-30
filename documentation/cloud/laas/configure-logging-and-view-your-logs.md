---
title: configure-logging-and-view-your-logs
displayName: Configure
order: 20
published: true
toc:
---
1\. Open the Logging tab and click "Set up Logging".

<img style="margin: 0px 0 0px 0px;" src="https://support.gcore.com/hc/article_attachments/6183008574737/image_1532.png" alt="image_1532.png">

The Logging page will open, do Steps 2, 3, 4 and 7 in it. The screenshot below highlights the sections and buttons that you need to interact with at these steps.

<img src="https://support.gcore.com/hc/article_attachments/6183246831633/image_1545.png" alt="image_1545.png">

2\. Select the region — this is the city of the data center where we will deploy the storage for logs.

Note that logging may be unavailable in some regions. Usually, our customers choose a region closer to their equipment so that logs can be sent to the storage as quickly as possible.

3\. Click **Create topic** in the upper-right corner, give your topic a name and confirm.  

A topic is a logical storage unit where logs are collected. You can think of it as a folder on your PC. Logs will be collected into a topic in the same way that you add files to a folder.

4\. Click **Generate credentials** in the upper-right corner. 

You will receive a login and password for the storage. You will use these to connect your equipment to the topic for log export. Be sure to save the credentials to your PC immediately because you won’t be able to see them again after closing the window. 

If you forget your username and password, click **Generate credentials** again, and a new pair will be generated. The previous credentials will become invalid. 

If you use Logging in multiple regions (which you specify at Step 2), a new storage will be created in each of them, and you will need to generate other credentials to connect to each of them. Your login will the same for all storages, but the passwords will be different. For example, if you use Logging in six regions, you will have one login and six passwords.

5\. Install a log shipping tool on the equipment from which you want to collect logs.

For example, you can [install Fluent Bit](https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit) or [Filebeat](https://www.elastic.co/beats/filebeat).  

6\. In the log shipper settings, specify which logs you need to collect, and configure the log export to our Kafka servers: specify the topic name, Kafka Endpoint, as well as the credentials generated at Step 4.  

Please note that the maximum size of a log message is 1 MB in text/JSON format, and the number of fields is limited to 225.

If you use Fluent Bit or Filebeat, you can configure it with our instructions: [Configure Fluent Bit](https://support.gcore.com/hc/en-us/articles/6173162093201), [Configure Filebeat](https://support.gcore.com/hc/en-us/articles/6171869217937).  

After setting up a log shipper, the logs of your device will be sent to your Kafka topic. Kafka servers will then automatically transfer them to our OpenSearch servers.   

Please note that the total amount of data that can be sent to the logging system should not exceed 900 Gb per day and the incoming traffic to Kafka servers should not exceed 10 Mb/sec.

7\. Go to the OpenSearch Dashboards URL specified on the Logging page.  

8\. Click **Create an index pattern** at the bottom of the screen. 

On the OpenSearch server, your logs are linked to your personal index, which has the same name as your topic. At this step, you create an index pattern, which acts as a filter to help OpenSearch Dashboards to display logs with the required index.

<img src="https://support.gcore.com/hc/article_attachments/6183292147473/image_1469.png" alt="image_1469.png">  

9\. In the **index-pattern** field, enter the namespace, name of the topic you created at Step 3 with an asterisk. For example, if your namespace is _namespace1,_ and you have created a topic named e_xampletopic_, enter _namespace1.exampletopic\*_ in the field. Then click **Next step**.

<img src="https://support.gcore.com/hc/article_attachments/6183355949713/image_1472.png" alt="image_1472.png">

10\. In the dropdown list, select the format used to indicate date and time in your logs, and then click **Create index pattern**.  

An index pattern will be created, and your logs will be available in OpenSearch Dashboards. The index pattern will be saved, and the next time you log into OpenSearch Dashboards, you will not need to configure them again.

<img src="https://support.gcore.com/hc/article_attachments/6183350616209/image_1475.png" alt="image_1475.png">

11\. The setup is finished. In the main menu, select **Discover** to see your logs.

Please note that logs will be stored in OpenSearch for 45 days. After 45 days, logs will be automatically deleted.

<img src="https://support.gcore.com/hc/article_attachments/6183388613265/image_1478.png" alt="image_1478.png">