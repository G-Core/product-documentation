---
title: logging-for-load-balancers
displayName: Logging
published: true
order: 20
toc:
   --1--1. Open settings: "step-1-open-load-balancers-settings"
   --1--2. Enable Logging: "step-2-enable-logging"
   --1--3. Configure Logging: "step-3-configure-logging-settings"
   --1--Test results: "throughput-test-results"
pageTitle: Load Balancer Logging for Seamless Cloud Resource Monitoring | Gcore
pageDescription: Learn to enable logging on your load balancer and explore guaranteed throughput results across various regions with Gcore Managed Logging.
---
# Logging for Load Balancers

Gcore Logging collects and stores logs from various Cloud resources, including Load Balancers. This guide outlines configuring Logging for an existing Load Balancer and highlights the guaranteed throughput between different Load Balancer regions and Logging regions.

To create a new Load Balancer, refer to <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">our product documentation</a>.

## Step 1. Open Load Balancers settings

In the **Cloud** menu, select **Networking** and then **Load Balancers**. Click the Load Balancer name for which you want to configure Logging.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-load-balancer-10.png" alt="Create Load Balancer" width="85%">

## Step 2. Enable Logging

Go to the **Logs** tab and turn on the **Enable Logging** toggle.


<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-load-balancer-20.png" alt="Enable Logging" width="70%">

## Step 3. Configure Logging settings 

1\. Create a namespace for your topics. 

<alert-element type="warning" title="Warning">

This setting is available **if you have not activated** <a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">Logging</a> for your project in the selected destination region.

</alert-element>

<expandable-element title="What is a namespace">

Previously, when activating Logging, you could see a non-human-readable string, e.g., ```cbc25c71af8d4f7ca6cbbcdc5a4d68fe.your-topic``` as a *namespace* that is used as prefixed for topics. To make this process more user-friendly, we created the possibility of making human-readable namespaces, e.g., ```namespace123.your-topic```.

<alert-element type="caution" title="Caution">

You can only create a namespace for a new project where the default value is not set up.

</alert-element>

</expandable-element>

To create a namespace, input the namespace name according to the following restrictions:

- Lowercase Latin letters and digits can be used
- Underscore and spaces are prohibited
- Length is between 2–32
- The name should be unique for the destination region. If it’s already used, the system will suggest inputting another name. 

Click **Create**.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-namespace.png" alt="Configure logging" width="70%">


2\. Add a topic. Select an existing one from the list or create a new one. For a new topic, specify the name and the retention period. 

3\. Click **Save changes**.

Your Load Balancer will start sending logs to the topic.

## Throughput test results 

Below are the test results that demonstrate the throughput for various region pairs (measured in K RPS,) where “source” is the region of a load balancer and “destination” is the location of the Managed Logging servers. 

<table>
<tr>
<td><b>Source</b></td>
<td><b>Destination</b></td>
<td><b>Measured log delivery throughput, K RPS</b></td>
</tr>
<thead>
</thead>
<tbody>
<tr>
<td>Amsterdam</td>
<td>Luxembourg</td>
<td>9.6</td>
</tr>
<tr>
<td>Amsterdam-2</td>
<td>Luxembourg</td>
<td>14.4</td>
</tr>
<tr>
<td>Darmstadt</td>
<td>Luxembourg</td>
<td>16.8</td>
</tr>
<tr>
<td>Frankfurt</td>
<td>Luxembourg</td>
<td>8</td>
</tr>
<tr>
<td>Japan</td>
<td>Luxembourg</td>
<td>1.6</td>
</tr>
<tr>
<td>Istanbul</td>
<td>Luxembourg</td>
<td>8.8</td>
</tr>
<tr>
<td>London</td>
<td>Luxembourg</td>
<td>17.6</td>
</tr>
<tr>
<td>Luxembourg-2</td>
<td>Luxembourg</td>
<td>12</td>
</tr>
<tr>
<td>Warsaw</td>
<td>Luxembourg</td>
<td>11.2</td>
</tr>
<tr>
<td>Chicago</td>
<td>Manassas</td>
<td>8</td>
</tr>
<tr>
<td>Manassas</td>
<td>Manassas</td>
<td>15.2</td>
</tr>
<tr>
<td>Santa Clara</td>
<td>Manassas</td>
<td>7.2</td>
</tr>
</tbody>
</table>
