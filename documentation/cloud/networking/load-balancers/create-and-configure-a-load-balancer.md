---
title: create-and-configure-a-load-balancer
displayName: Load balancer
published: true
order: 10
toc:
   --1--Create: "create-a-load-balancer"
   --1--Manage: "manage-a-load-balancer"
   --1--Balancer statuses: "load-balancer-statuses"
   --1--Performance analysis: "performance-analysis"
pageTitle: Add a load balancer | Gcore
pageDescription: Learn how to create and configure a load balancer to distribute incoming requests across VMs, improving the fault tolerance of your infrastructure.
customUrl: /cloud/networking/create-and-configure-a-load-balancer
---

# Create and configure a load balancer
 
A **load balancer** is a tool used to sort incoming requests across your virtual machines so to improve the fault tolerance of your infrastructure. 

## **Create a load balancer** 

1\. Go to your project - > **Networking** - > **Load Balancers** - > **Create Load Balancer**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/__________________.png" alt="">

The new window opens. Do the remaining steps in it. 

2\. Select a region for balancing. Please note that you can balance traffic only within a single data center.

3\. Select a network. If you want to use a private network for load balancing, enable the **Use private network** option. For more information, see the article <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">"Create and manage a network"</a>.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/_____________________.png" alt="">

4\. Add one or more listeners. A listener is a process that checks for connection requests using the protocol and port that you configure. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/___________________.png" alt="">

In the drop-down window, specify the listener name, protocol (TCP or HTTP), and port in the range from 1 to 65535.  

We also support the option to add an X-Forwarded-For header to identify an origin of the IP address of the client connecting to a web server via a load balancer. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/mceclip1.png" alt="" width="401" height="334">

5\.  Configure a pool. A pool is a list of virtual machines to which the listener will redirect incoming traffic. 

Click **Add pool** to start configuring.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/_______________.png" alt="">

5\. 1. Specify the pool name.

5\. 2. Select the balancing algorithm:          

**Round robin** — requests are distributed across servers within a cluster one by one: the first request is sent to the first server, the second request is sent to the second server, and so on in a circle. 

**Least Connection** — new requests are sent to a server with the fewest active connections. 

**Source IP** — a client's IP address is used to determine which server receives the request. 

4.3. Select a protocol. The system will offer you an option based on the listener's settings: the HTTP listener can communicate with servers via the HTTP protocol, the TCP listener — via TCP.

4.4. If you need to route the requests for a particular session to the same machine that serviced the first request for that session, select **App Cookie** and fill in the **Cookie** field. <a href="https://code.google.com/p/nginx-sticky-module/)" target="_blank">A special module</a> creates a cookie — which makes each browser unique — and then uses it to forward requests to the same server.  

4.5. Add virtual machines that will participate in the traffic distribution for the configured listener. For adding an instance, you must specify its port and weight in the distribution. 

4.6. In the **Health check** section, select the Protocol for checking: TCP, Ping, HTTP. 

For the HTTP Protocol, select the HTTP method and add the URL path. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/_____________.png" alt="">

Specify the following setting for the protocols: 

*   Check interval (sec) — time between sent requests 
*   Response time (sec) — the time to wait for a response from a server 
*   Unhealthy Threshold — the number of failed requests after which traffic will no longer be sent to the virtual machine 
*   Healthy Thresholds — the number of successful requests after which the virtual machine will be considered ready to receive traffic.

6\. Enter a name for the load balancer and click **Create Load Balancer.**

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/___________________.png" alt="">

7\. Configure firewalls for instances in the pool.

Make sure their ports are open for the load balancer traffic:

*   If a balancer and instances are in a **public network,** set a rule to receive and transmit traffic to the balancer's IP address (specified in the menu) in firewalls settings of the instances.
*   If a balancer and instances are in a **private subnetwork,** set a rule to receive and transmit traffic to the entire private subnetwork or to the balancer's IP address (specified in the menu).
*   If a balancer is in a **public network** and instances are in a **private subnetwork**, set a rule to receive and transmit traffic to the entire private subnetwork or to the balancer's internal IP address (send a request to the technical support).

8\. Set up the balancer's firewall (optionally)

Create a custom security group (this is the firewall) and edit it: configure the rules for inbound and outbound traffic.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/mceclip0.png" alt="">

## **Manage a load balancer**

The list of created balancers is located inside the project - > Networking - > Load balancers

There you can:

*   Configure a balancer (the "Overview" option) 
*   Rename a balancer (the "Edit" option) 
*   Delete a balancer

To do it, select the necessary action on the selector on the right from the balancer.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/____________________.png" alt="">

Go to your project - > Networking - > Load balancers -> select the Overview option on the selector on the right from the chosen balancer.

In the drop-down window, you can edit existing listeners in the load balancer and also add new ones.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/________________________________________.png" alt="">

You can **edit** and **delete** listeners. Select the appropriate option on the selector on the right from the listener. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/____________________________.png" alt="">

In the editor, you can:

*   Change the checking algorithm

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/_______________.png" alt="_______________.png">

*   Parameters of connected instances (including verification address, port, and weight)

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/______________.png" alt="______________.png">

*   Enable and disable instances from the load balancing pool

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/__________________________.png" alt="__________________________.png">

*   Change the parameters in the Health Check section

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/__________________.png" alt="__________________.png">

## **Load Balancer statuses**

| Status (UI) | Status (API)                                                                                                                              | Value                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Healthy     | Online                                                                                                                                    | The balancer is working.All virtual machines in the pool accept requests. |
| Unhealthy   | Draining                                                                                                                                  | A virtual machine from the pool does not accept new requests.                   |
| Degraded    | One or more balancer components have the \"Error\" status.                                                                                |
| Error       | The balancer doesn't work.Virtual machines do not pass check requests.All virtual machines in the pool have the \"Error\" status. |


## Performance analysis

We have tested our load balancers to determine the performance of different flavors. The test results show the throughput - the number of requests per second (rps) a load balancer can handle under a number of simultaneous users’ requests for worker nodes that communicate through the load balancer considering that 95 percent of requests are handled within 1 ms. 

| Flavor          | Throughput | Worker request | Percentile response time |
|-----------------|------------|----------------|--------------------------|
| 1 vCPU - 2 GiB  | 5k         | 1              | 95th percentile is 1 ms  |
| 2 vCPU - 4 GiB  | 5k         | 16             | 95th percentile is 1 ms  |
| 4 vCPU - 8 GiB  | 5k         | 512            | 95th percentile is 1 ms  |
| 8 vCPU - 16 GiB | 5k         | 2048           | 95th percentile is 1 ms  |
