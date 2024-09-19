---
title: manage-load-balancers
displayName: Manage Load Balancers
published: true
order: 15
toc:
   --1--Load Balancer statuses: "statuses-of-a-load-balancer-and-its-components"
   --1--Load Balancer settings: "load-balancer-settings"
   --2--Flavor: "flavor"
   --2--Monitoring: "monitoring"
   --2--Listeners: "listeners"
   --3--Pool settings: "pool-settings"
   --3--L7 policies: "l7-policies"
   --3--Listener statistics: "listener-statistics"
   --2--Configuration: "configuration"
   --2--Logging: "logging"
   --2--Custom tags: "custom-tags"
   --1--Initiate a failover: "initiate-a-failover" 
   --1--Rename a Load Balancer: "rename-a-load-balancer" 
   --1--Edit tags: "edit-tags" 
   --1--Delete a Load Balancer: "delete-a-load-balancer"                                    
pageTitle: Configure a Load Balancer | Gcore
pageDescription: Learn how to configure a Load Balancer to distribute incoming requests across VMs, improving the fault tolerance of your infrastructure.
---
# Manage Load Balancers

After you create a Load Balancer, it will appear on the **Load Balancers** page in the Customer Portal. To access the page: 

1\. Navigate to **Cloud** > **Networking**. 

2\. Open the **Load Balancers** page. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/load-balancers-page.png" alt="Load Balancers page in the Customer Portal" width="80%">

On this page, you can find all the necessary information about the created resource: 

* **Name**: The name and brief summary of its configuration. 
* **IP Address**: Address assigned to the Load Balancer. 
* **Listeners**: The number of configured listening ports that define how incoming network traffic is received and distributed. 
* **Region**: The geographical location of a data center where the Load Balancer is deployed. 
* **Tags**: <a href="https://gcore.com/docs/cloud/networking/load-balancers/manage-load-balancers#custom-tags" target="_blank">Metadata</a> used to label and categorize Load Balancer within a cloud environment. 
* **Created**: The date and time when it was deployed. 
* **Operating status**, **Provisioning status**: Check the <a href="https://gcore.com/docs/cloud/networking/load-balancers/manage-load-balancers#statuses-of-a-load-balancer-and-its-components" target="_blank">statuses of Load Balancer and its components</a> for a detailed overview of each one. 

You can explore these settings in more detail, monitor Load Balancer's performance and health metrics, and adjust configurations as needed. Refer to the following sections for instructions. 

<alert-element type="tip" title="Tip">
 
When managing a significant number of Load Balancers, use the **Search by name** feature to find the exact one you need. 

</alert-element>

## Statuses of a Load Balancer and its components

A Load Balancer and its components (listener, pool, and pool member) can have two types of statuses:  

* **Operating status**: The current observed operational state of a resource. The status reflects whether the resource is functioning as expected or if there are any issues with its operation.  

* **Provisioning status**: The lifecycle stage of a resource, from creation through any changes to potential deletion. 

The **operating** status of a resource can change to: 

* **Online**: It’s operating normally, and all pool members are healthy. 
* **Draining**: Pool members are no longer accepting new connections. 
* **Offline**: Load Balancer isn’t accepting new connections. 
* **Degraded**: One or more pool members are in an error state.  
* **Error**: This status indicates that the Load Balancer has failed, one or more pool members are failing health checks, or all pool members are in an error state. 
* **No_monitor**: No health monitor is configured for a resource. Thus, its status is unknown. 

During the resource’s lifetime, its **provisioning** status can signal the following: 

* **Active**: It’s been successfully created.  
* **Deleted**: It’s been successfully deleted. 
* **Updating**: It’s currently being updated. 
* **Deleting**: It’s currently being deleted.  
* **Error**: The system failed to create a balancer. If an error occurs during the update or deletion of a balancer, <a href="https://gcore.com/docs/cloud/networking/load-balancers/manage-load-balancers#initiate-a-failover" target="_blank">initiate a failover</a>. Load Balancers that fail to be created will be automatically deleted.

<alert-element type="info" title="Info">
 
Updating the name, description, or tags of a Load Balancer won't cause any connection interruptions or downtime.
 
</alert-element>

## Load Balancer settings

You can inspect the configuration details of a created Load Balancer, view and copy its routing scheme, add and remove listeners, or enable logging on the **Overview** page. To open the page:

1\. Navigate to **Cloud** > **Networking**. 

2\. On the **Load Balancers** page, find the balancer you want to configure and click its name to open the settings.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/balancer-overview.png" alt="Load Balancers overview page" width="80%">

The **Overview** page features the following information:

* **Routing scheme**: Visualization of traffic flow as it passes through a Load Balancer. The scheme demonstrates what’s happening as traffic is received (ingress) and sent out (egress) by the balancer. 
* **Type**: Network distribution by a Load Balancer—external (public) or private. 
* **VIPs**: Virtual IP address of a Load Balancer. 
* **Floating IP**: If you added a Floating IP while creating a Load Balancer, it will appear in this column. 
* **Custom security group**: Firewall that defines rules for inbound and outbound traffic. By default, the Load Balancer uses the project's <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall#use-the-default-firewall" target="_blank">default firewall</a> (also known as “security group”). If you want to customize firewall settings, <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall#create-a-firewall" target="_blank">create a custom security group</a>. 

 <alert-element type="info" title="Info">
 
 The firewall offers flexible network configuration, allowing you to control incoming and outgoing traffic.  

 After creating the balancer, update firewall settings and open VM ports so that traffic can easily pass from the balancer and back. 

 </alert-element>

* **Operating status**, **Provisioning status**: Check the <a href="https://gcore.com/docs/cloud/networking/load-balancers/manage-load-balancers#statuses-of-a-load-balancer-and-its-components" target="_blank">statuses of Load Balancer and its components</a> for a detailed overview of each one. 

The Load Balancer settings are organized into tabs, each dedicated to a specific functionality. The following sections provide a detailed description of these settings. 

### Flavor

This tab features a summary of the load balancer's configuration and its resources. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/flavor-tab.png" alt="Flavor tab in Load Balancer settings" width="80%">

* **Flavor**: A name for the specific configuration that defines the combination of vCPU and RAM resources allocated for the Load Balancer. 
* **vCPU**: The number of allocated virtual CPU cores.  
* **RAM**: The amount of allocated RAM, expressed in Gibibytes (GiB). 
* **ID**: A unique identifier of the Load Balancer used for management and tracking within the cloud environment. 
* **Active connections**: The number of current, ongoing connections being handled by the load balancer.  
* **Bytes in**: The total amount of data received by the balancer.  
* **Bytes out**: The total amount of data sent out by the balancer. 
* **Request errors**: The number of errors that occurred during the handling of requests.  
* **Total connections**: The total number of connections that have been made to the Load Balancer. 

### Monitoring 

This tab provides an overview of the Load Balancer's performance metrics that are crucial for tracking its health and performance.  

By checking the metrics, you can understand if the current resources are sufficient or if there's a need to scale up and optimize Load Balancer’s performance.  

Monitoring data is available in hourly and weekly views:  

* Hourly options: 1, 6, or 24 hours 
* Weekly options: 1 or 2 weeks 

You can also specify the auto-refresh cadence: in minutes (1, 5, 15, or 30) or for one hour. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/monitoring-tab.png" alt="Monitoring tab in Load Balancer settings" width="80%">

* **CPU Utilization**, %: The percentage of currently used Load Balancer's CPU. It's a key performance indicator that can help you understand if the Load Balancer is nearing its capacity limits. High CPU usage is typically observed with a large number of connections or high volumes of traffic. 

* **RAM Utilization**, %: The percentage of total available memory currently used by the Load Balancer. High RAM utilization indicates that the Load Balancer is handling a large number of connections or running memory-intensive processes, which is common with terminated HTTPS traffic. Other types of traffic generally consume less RAM.  

* **Network traffic**: The rate of incoming (ingress) and outgoing (egress) network traffic measured in kilobits per second (kbit/s). The metrics can help you understand the network load on the Load Balancer. 

* **Network packets**: Network packets per second (PPS) measure the rate of network packets being received (ingress) and sent out (egress) by the balancer. 

### Listeners 

Listener is a process that checks for connection requests using the configured protocol and port. A listener contains a pool—a list of virtual machines or Bare Metal servers that will receive traffic from the listener. 

Listener configuration: 

* **Name**: Name of the listener. 
* **Protocol**: The network protocol that defines what type of traffic will be handled by the listener.  
* **Port**: The network port that the listener monitors for incoming connections. 
* **Pools**: The number of backend server pools (often called members or backends) that handle the traffic received by the listener.  
**Operating status**: The current operational state of the listener. "Online" means it is functioning and can receive traffic. 
* **Provisioning status**: The status of the configuration process for the listener. "Active" suggests that it has been fully configured and is operational. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listeners-tab.png" alt="Listeners tab in Load Balancer settings" width="80%">

<alert-element type="info" title="Info">
 
You can't add multiple listeners with the same L4 type and port number. For example, you can create a listener with TCP 80 and UDP 80 but not a listener with TCP 80 and TCP 80.  

It's also not possible to use both TCP 80 and HTTP 80. The reason is that HTTP is an L7 protocol based on L4 TCP, so in this case, it's perceived as TCP 80 + TCP 80. 
 
</alert-element>

#### Pool settings

<alert-element type="tip" title="Tip">
 
For optimized performance, we recommend making batch updates of pool settings. To perform comprehensive simultaneous updates, use the <a href="https://api.gcore.com/docs/cloud#tag/Load-Balancers/operation/LoadBalancerPoolInstanceViewSet.patch" target="_blank">Gcore API</a>.

</alert-element>

A pool is the list of VMs or Bare Metal to which the listener will redirect incoming traffic. Each pool in the listener has the following configuration:

* **Name**: The name of the pool. 

* **Algorithm**: The load-balancing method used to distribute traffic among instances in the pool. Check available algorithms in <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer#pool" target="_blank">pool settings</a>. 

* **Instance count**: The number of Virtual Machines whose traffic is managed by a Load Balancer. 

* **Health Check**: The method used to determine the health of the instances in the pool.  

* **Operating status**: The current operational state of the pool. "Online" indicates that the pool can handle traffic. 

* **Provisioning status**: The status of the configuration process for the pool. "Active" means the pool is fully set up and ready for use. 

* **Protocol**: The network protocol that the pool uses to communicate with instances and members. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listeners-tab-pool.png" alt="Listeners tab with pool settings" width="80%">

Instances:

* **State**: Whether the instance is enabled or disabled within the pool. "Enabled" means that the instance is active and can receive traffic from the Load Balancer. 
* **Type**: The category of the instance. It can be an instance (Virtual Machine), Bare Metal, or any custom IP. 
* **Instance**: Unique identifier of the instance. 
* **Address**: IP address of the instance that’s used by the Load Balancer to forward traffic to this instance. 
* **Port**: The network port on which the instance listens.  
* **Weight**: Distribution of traffic among Virtual Machines or Bare Metal servers in the pool. A weight can be assigned to each VM or Bare Metal to influence how much traffic it should handle compared to other instances. A higher weight means that more traffic will be directed to that particular resource. 

 <img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listeners-tab-instances.png" alt="Listeners tab with instance settings" width="80%">

Health check: 

* **Protocol**: The method used by a Load Balancer to check the health of the pool members. 
* **Check interval**: The frequency of performing health checks. Typically, the optimal time is less than 10 seconds. 
* **Response time**: The maximum time a Load Balancer will wait for a response to a health check. A response time of "5 sec" means that if a server doesn't respond to a ping within 5 seconds, it is considered unresponsive for this health check instance.  
* **Unhealthy thresholds**: This is the number of consecutive failed health checks required before a server is considered unhealthy and removed from the pool for traffic distribution.  
* **Healthy thresholds**: The number of consecutive successful health checks required for a server to be considered healthy and added back to the pool. 

 <img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listeners-tab-health-check.png" alt="Listeners tab with health check settings" width="80%">

Timeouts: 

* **Client Data**: The maximum amount of time a Load Balancer will wait for a client to send data. After that, the connection will be closed.  
* **Member Connect**: The maximum amount of time a Load Balancer will wait to establish a connection with a pool member. If the connection is not established within that timeframe, it’s considered a failed attempt.  
* **Member Data**: The maximum amount of time a Load Balancer will wait for a pool member to send data once a connection has been established. If no data is sent within this timeframe, the connection times out.  

 <img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listeners-tab-timeouts.png" alt="Listeners tab with timeouts settings" width="80%">

#### L7 policies 

L7 policy specifies how to manage and route incoming traffic at the application layer (Layer 7 of the <a href="https://osi-model.com/application-layer/" target="_blank">OSI model</a>).

#### Listener statistics

* **Name**: Name of each listener. 
* **Active connections**: Number of ongoing connections to each listener. 
* **Bytes in**: Total amount of data received by the listener.  
* **Bytes out**: Total amount of data sent from the listener. 
* **Request errors**: Total number of request errors encountered by the listener. 
* **Total connections**: The cumulative number of connections handled by the listener since it was started. 

 <img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/listener-stats.png" alt="Listeners tab with listener statistics" width="80%">

### Configuration 

This tab allows you to change the flavor of your Load Balancer based on the requirements of your workload, expected traffic, the computing resources needed, and others. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/configuration-tab.png" alt="Configuration tab settings" width="80%">

### Logging

Record detailed information about the traffic processed by a Load Balancer. This data is useful for debugging, monitoring, and analyzing the behavior of your applications. 

Our <a href="https://gcore.com/docs/cloud/networking/load-balancers/logging-for-load-balancers" target="_blank">Logging for Load Balancers</a> guide covers all available settings and configuration steps. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/logging-tab.png" alt="Logging tab settings" width="80%">

### Custom tags 

On this tab, you can review and assign metadata to a Load Balancer. 

You can use tags to group multiple resources that belong to the same functionality. For instance, if you have a single project with different services—such as an authentication service, a shop service, and a cart service—each service can have its own Load Balancer. By applying tags, you can easily organize and manage these resources as a group. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/custom-tags-tab.png" alt="Tags tab settings" width="80%">

When you add the “test” custom tag to your Load Balancer, you essentially label that resource with "test:LB". This can help you quickly identify the resource's purpose, environment, owner, or any other characteristic that is relevant to your organization. 

## Initiate a failover 

The failover mechanism automatically detects Load Balancers that have failed or demonstrate degraded performance.  

When you initiate a failover, the traffic is redirected to an alternate Load Balancer within your network infrastructure. The second balancer immediately takes over the duties of the failed one without interrupting the availability of your application. 

To initiate a failover: 

1\. Navigate to **Cloud** > **Networking**. 

2\. Open the **Load Balancers** page. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/load-balancers-page.png" alt="Load Balancers page in the Customer Portal" width="80%">

3\. Find the needed balancer and click its name to open it. 

4\. In the top-right corner of the screen, click **Actions** > **Failover**.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/failover.png" alt="Load Balancers page with initiate failover settings" width="80%">

5\. (Optional) Enable force failover. To failover the primary Load Balancer, click the **Ignore Load Balancer provisioning status** checkbox. After you complete the failover, the traffic will be handled by a standby balancer.

6\. Click **Initiate Failover**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/initiating-failover.png" alt="Initiate failover dialog asking whether to procceed with failover" width="80%">

The failover might take a few minutes to complete. During this time, the Load Balancer provisioning status will change to **Updating**. 

<alert-element type="warning" title="Warning">
 
During failover or resize operations, all current connections will be terminated, causing temporary disconnects. 
 
</alert-element>

## Rename a Load Balancer 

1\. Navigate to **Cloud** > **Networking**. 

2\. Open the **Load Balancers** page. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/load-balancers-page.png" alt="Load Balancers page in the Customer Portal" width="80%">

3\. Find the Load Balancer you want to update and click the three-dot icon next to it.

4\. Select **Rename**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/rename.png" alt="Rename button in the Load Balancer settings" width="80%">

5\. Enter a new name and click **Save** to apply the changes. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/rename-confirmation.png" alt="Rename dialog in the Load Balancer settings" width="80%">

## Edit tags 

To update <a href="https://gcore.com/docs/cloud/networking/load-balancers/manage-load-balancers#custom-tags" target="_blank">metadata</a> assigned to a Load Balancer: 

1\. Navigate to **Cloud** > **Networking**. 

2\. Open the **Load Balancers** page. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/load-balancers-page.png" alt="Load Balancers page in the Customer Portal" width="80%">

3\. Find the Load Balancer you want to update and click its name to open the settings. 

4\. Navigate to the **Tags** tab, where you can view and modify the balancer’s metadata.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/custom-tags-tab.png" alt="Tags tab settings" width="80%">

5\. Update tags as you see fit and click **Save**. 

## Delete a Load Balancer 

1\. Navigate to **Cloud** > **Networking**. 

2\. Open the **Load Balancers** page. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/load-balancers-page.png" alt="Load Balancers page in the Customer Portal" width="80%">

3\. Find the Load Balancer you want to update and click the three-dot icon next to it.

4\. Select **Delete**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/delete-three-dot-icon.png" alt="Delete button in the Load Balancer settings" width="80%">

5\. Click **Delete** to verify your action.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/manage-a-load-balancer/delete-confirmation.png" alt="Delete dialog in the Load Balancer settings" width="80%">

Your Load Balancer has been successfully removed. 
