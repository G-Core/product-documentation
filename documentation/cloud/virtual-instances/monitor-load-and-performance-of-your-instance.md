---
title: monitor-load-and-performance-of-your-instance
displayName: Monitor
published: true
order: 60
toc:
pageTitle: Monitor load of a VM | Gcore
pageDescription: Monitor your virtual machine with essential metrics. Check CPU and RAM utilization, track network traffic, and manage performance effectively.
---
# Monitor load on a specific node

Monitoring is a tab where you can monitor the load and performance of an instance using ten metrics.

To open the tab, select the required instance and click "Monitoring".

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip1.png" alt="mceclip1.png">

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip0.png" alt="mceclip0.png">
</media-gallery>

Buttons above the graphs control the display of statistics: the left one sets up what period to show, the right one — how often the data will be updated on the screen.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip2.png" alt="mceclip2.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip2.png)

Please note: as a second metric (for example, the number of bytes per second), Monitoring displays the average value for one minute. The system collects the volume of traffic/operations for a minute and divides it by 60.

1\. CPU Utilization is the load on the machine's CPU, measured as a percentage.  
For example, if all cores are 90% loaded, you will see a value of 90%.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip3.png" alt="mceclip3.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip3.png)

CPU Utilization can exceed 100%. This means that the instance used more physical resources than provided for by the tariff at a particular moment. This usually happens during the creation of the instance. This is normal and does not affect payment.

2\. RAM Utilization is the amount of RAM that the instance uses to perform tasks.  
Measured in percentages, 100% means a full load of RAM.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip4.png" alt="mceclip4.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip4.png)

Inside the system, you can see the RAM Utilization value that is less than in the Monitoring. This is normal: our Monitoring includes cache RAM in the statistics. This is unused RAM that the machine borrows and uses to make applications run smoother and faster. If some application needs more RAM, the system immediately brings it back from the cache.

3\. Network BPS ingress is the speed of incoming traffic measured in bytes per second.

4\. Network BPS egress is the speed of outgoing traffic measured in bytes per second.  

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip5.png" alt="mceclip5.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip5.png)

5\. Network PPS ingress is the speed of incoming traffic measured in packets per second.

6\. Network PPS egress is the speed of outgoing traffic measured in packets per second.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip6.png" alt="mceclip6.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip6.png)

7\. sda/Disk IOPS read is the speed of reading information from the disk measured in the number of read operations per second.

8\. sda/Disk IOPS write is the speed of writing information to the disk measured in the number of write operations per second.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip7.png" alt="mceclip7.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip7.png)

9\. sda/Disk BPS read is the speed of reading information from the disk measured in the number of transmitted bytes per second.

10\. sda/Disk BPS write is the speed of writing information to the disk measured in the number of transmitted bytes per second.

[<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip8.png" alt="mceclip8.png">](https://assets.gcore.pro/docs/cloud/virtual-instances/monitor-load-and-performance-of-your-instance/mceclip8.png)