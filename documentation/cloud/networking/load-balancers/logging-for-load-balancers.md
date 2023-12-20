---
title: logging-for-load-balancers
displayName: Logging
published: true
order: 20
toc:
   --1--Configure: "configure-managed-logging-for-a-load-balancer"
   --1--Test results: "throughput-test-results"
pageTitle: Load Balancer Logging for Seamless Cloud Resource Monitoring | Gcore
pageDescription: Learn to enable logging on your load balancer and explore guaranteed throughput results across various regions with Gcore Managed Logging.
---
# Managed Logging for Load Balancers

Gcore Managed Logging collects and stores logs from various Cloud resources, including Load Balancers. This guide explains the process of configuring Managed Logging for an existing load balancer and highlights the guaranteed throughput between different load balancer regions and Managed Logging regions.

To create a new Load Balancer, refer to <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">our product documentation</a>.

## Configure Managed Logging for a Load Balancer

1\. In the **Cloud** menu, select **Networking** and then **Load Balancers**. Click the Load Balancer for which you want to configure logging.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-load-balancer-10.png" alt="Create Load Balancer" width="85%">

2\. Go to the **Logs** tab and enable the **Enable Logging** toggle.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-load-balancer-20.png" alt="Enable Logging" width="70%">

3\. For **Destination region**, select the region for log export. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/logging-for-load-balancers/logging-load-balancer-30.png" alt="Condigure logging">

4\. Add a topic: select an existing one from the list or create a new one. For a new topic, specify the name and the retention period. 

5\. Click **Save changes**. 

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
