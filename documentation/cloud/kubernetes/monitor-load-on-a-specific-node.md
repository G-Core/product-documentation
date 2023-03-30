---
title: monitor-load-on-a-specific-node
displayName: Monitor load on a specific node
published: true
toc:
   --1--Navigate to monitoring: "navigate-to-monitoring"
   --1--Metrics: "metrics"
---
  

Each node is a virtual machine. You can monitor its load and performance through 6 metrics.

Navigate to monitoring
----------------------

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://support.gcore.com/hc/article_attachments/13348768823569" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click the required pool to expand the menu, and the click the required node.

<img src="https://support.gcore.com/hc/article_attachments/13348772802833" alt="Screenshot_2023-02-27_at_15_1.jpg">

3\. In the new window, switch to the **Monitoring** tab.  
The buttons to the right above the graphs regulate the presentation of statistics. The left button sets the period to be shown, and the right button sets the frequency at which data will be updated on the screen.

<img src="https://support.gcore.com/hc/article_attachments/13348867859473" alt="Screenshot_2023-02-04_at_14.28_4-2.png" width="554" height="254">

Note: the Monitoring feature shows the average value per minute for metrics that are measured in seconds (e.g., the number of bytes per second). The system calculates the volume of traffic/operations per minute and then divides it by 60.

Metrics
-------

You can monitor the state of a virtual machine using 6 metrics:

1\. The **CPU Utilization** metric measures the load on the machine's CPU as a percentage. For example, if all cores are at 90% usage, the value displayed will be 90%.

2\. The **RAM Utilization** refers to the amount of RAM being utilized by the instance to perform tasks. It is measured as a percentage, with 100% indicating full utilization of RAM.

The RAM Utilization value inside the system might appear to be lower than what is shown in Monitoring, which is normal. Monitoring takes into account cache RAM as a part of its statistics. Cache RAM is unused RAM that the machine borrows and uses to improve application performance. If an application needs more RAM, the system immediately retrieves it from cache.

3\. The **Network BPS ingress** is the speed of incoming traffic, measured in bytes per second.

4\. The **Network BPS egress** is the speed of outgoing traffic, measured in bytes per second.

5\. The **Network PPS ingress** is the speed of incoming traffic, measured in packets per second.

6\. The **Network PPS egress** is the speed of outgoing traffic measured in packets per second.