---
title: configure-logging-and-view-your-logs
displayName: Configure
order: 20
published: true
toc:
---
# Configure Logging and view your logs

1\. Open the Logging tab and click **Set up Logging**.

<img src="https://support.gcore.com/hc/article_attachments/6183008574737/image_1532.png" alt="" width="70%">

2\. Select the region (under the project name) - the location of the data center for deploying log storage.

Note that logging may not be available in certain regions. Usually, our customers choose a region closer to their equipment to ensure logs are quickly sent to storage.

3\. In the "Topics" section, click Create topic, give it a name and click **Save**.

<img src="https://support.gcore.com/hc/article_attachments/14420358788881" width="70%">

4\. Click **Generate credentials** in the upper-right corner. Save them immediately because you won’t be able to see them again after closing the window.

These credentials are used to connect your equipment to the topic for log export.

If you forget your credentials, click **Generate credentials** again for a new pair. Don’t forget to update your login credentials (i.e., your username and password) in the settings of the installed log shippers.

If you use Logging in multiple regions (which you specify at Step 2), a new storage will be created in each region, and you will need to generate unique credentials for each one.

5\. Install and configure a log shipping tool like <a href="https://docs.fluentbit.io/manual/installation/getting-started-with-fluent-bit" target="_blank">install Fluent Bit</a> or <a href="https://www.elastic.co/beats/filebeat" target="_blank">Filebeat</a> on the equipment from which you want to collect logs. You can use our guides <a href="https://gcore.com/docs/cloud/laas/install-a-log-shipper/install-and-configure-fluent-bit" target="_blank">Configure Fluent Bit</a>, <a href="https://gcore.com/docs/cloud/laas/install-a-log-shipper/install-and-configure-filebeat" target="_blank">Configure Filebeat</a>.  

In the log shipper settings, specify which logs to collect and configure log export to our Kafka servers. Provide the topic name, Kafka Endpoint, and credentials generated at Step 4. Please note that the maximum size of a log message is 1 MB in text/JSON format, and the number of fields is limited to 225.

Once the log shipper is set up, your device logs are sent to your Kafka topic. From there, the Kafka servers will automatically transfer them to our OpenSearch servers.

6\. Go to the OpenSearch Dashboards by using the URL specified on the Logging page. 

<img src="https://support.gcore.com/hc/article_attachments/14420497971473" width="70%">

To log in, use the credentials generated at Step 4.

7\. From the home page, click to Manage → Index Patterns.

<img src="https://support.gcore.com/hc/article_attachments/14420742939281" width="70%">

8\. Click **Create an index pattern** at the bottom of the screen. 
 
<img src="https://support.gcore.com/hc/article_attachments/6183292147473/image_1469.png" alt="" width="70%">  

On the OpenSearch server, your logs are linked to your personal index, which has the same name as your topic. At this step, you create an index pattern, which acts as a filter to help OpenSearch Dashboards to display logs with the required index.

9\. In the **index-pattern** field, enter the namespace, name of the topic you created at Step 3 with an asterisk. For example, if your namespace is *namespace1*, and you have created a topic named *e_xampletopic*, enter _namespace1.exampletopic*_ in the field. Finally, click **Next step** to proceed.

<img src="https://support.gcore.com/hc/article_attachments/14420777278097" alt="" width="70%">

10\. Select the date and time format from the dropdown list, and click Create index pattern to make your logs accessible in OpenSearch Dashboards. The pattern is saved, so you don't have to set it up again next time you log in.

<img src="https://support.gcore.com/hc/article_attachments/6183350616209/image_1475.png" alt="" width="70%">

11\. Setup is complete. To view your logs, go to the main menu and select **Discover**.

<img src="https://support.gcore.com/hc/article_attachments/6183388613265/image_1478.png" alt="" width="70%">

The retention period for the logs is 45 days, after that, they will be automatically deleted.