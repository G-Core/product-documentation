---
title: create-and-configure-a-load-balancer
displayName: Create Load Balancer
published: true
order: 10
toc:
   --1--1. Initiate: "step-1-initiate-load-balancer-creation"
   --1--2. Set region: "step-2-set-the-region"
   --1--3. Configure computing: "step-3-set-computing-configuration"
   --1--4. Configure network: "step-4-configure-network"
   --1--5. Configure listeners: "step-5-configure-listeners"
   --2--Listener: "listener"
   --2--Pool: "pool"
   --2--Virtual Machine: "virtual-machine"
   --2--Health Сheck: "health-check"
   --2--Timeouts: "timeouts"
   --1--6. Enter name: "step-6-enter-the-name"
   --1--7. (Optional) Enable Logging: "step-7-optional-enable-logging"
   --1--8. (Optional) Add tags: "step-8-optional-add-tags"
   --1--9. Finalize: "step-9-finalize-creation"
   --1--10. Check firewall: "step-10-configure-firewall"
pageTitle: How to Create and Configure a Load Balancer | Gcore
pageDescription: Learn how to create and configure a Load Balancer to distribute incoming requests across VMs, improving the fault tolerance of your infrastructure.
customUrl: /cloud/networking/create-and-configure-a-load-balancer
---
# Create and configure a Load Balancer

A Load Balancer is a tool used to sort incoming requests across your Virtual Machines to improve your infrastructure's fault tolerance.

## Step 1. Initiate Load Balancer creation

Go to your project, navigate to the "Load Balancers" in the "Networking" section and click **Create Load Balancer**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-1-lb.png" alt="Initiate the process of Load Balancer creation" width="80%">

The new page opens. Perform the remaining steps there. 

## Step 2. Set the region 

Select a region for balancing. 

<alert-element type="warning" title="Warning">

You can balance traffic only within a single data center.

</alert-element>

## Step 3. Set computing configuration

Select a suitable computing configuration for your Load Balancer: GiB and vCPU. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-2-lb.png" alt="Select type" width="75%">

## Step 4. Configure network

Select a network, public or private, and enable additional features:

- Reserved IP and IPv6 dual-stack for the public network.
- Floating IP, reserved IP and IPv6 dual-stack for the private network.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-3-lb.png" alt="Select public or private network option" width="70%">

## Step 5. Configure listeners 

### Listener

Add listeners that will check for connection requests using the protocol and port that you specify. You can add multiple listeners to a Load Balancer. 

To configure a listener: 

1\. In the **Listeners** section, click **Add listener**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/add-listener.png" alt="Add listener" width="65%">

2\. Enter the listener’s name.  

3\. Select the required protocol: TCP, UDP, HTTP, Terminated HTTPS, and Prometheus. You can configure multiple TLS certificates for Terminated HTTPS and Prometheus.  

4\. Specify a port that the Load Balancer will listen on for incoming traffic. You can keep a default port for some protocols or specify the needed port from 1 to 65535. 

5\. (Optional) To identify the origin of the user's IP address connecting to a web server via a load balancer, enable the **Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests** toggle. 

6\. If you select Terminated HTTPS and Prometheus protocols, you can configure TLS certificates. Follow instructions from our <a href="https://gcore.com/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer" target="_blank">dedicated guide</a>. 

7\. Set the connection limit - a maximum number of simultaneous connections that can be handled by this listener.  

8\. (Optional) Add allowed CIDR ranges to define which IP addresses can access your content. All IP addresses that don’t belong to the specified range will be denied access. 

9\. (Optional) For HTTP-based listeners, you can configure basic user authentication to protect your resource from unauthorized access. Click **Add users** to enable the authentication:

* **Enter username**: specify a username. 

* **Password**: specify a password or choose the **Encrypted password** option to store password as a hash. Check out [create an encrypted password](https://gcore.com/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer#create-an-encrypted-password) for instructions. 

<alert-element type="info" title="Info">
 
A password must contain at least one lowercase character, one uppercase character, at least one number, and a special character. The maximum password length is 128 symbols.
 
</alert-element>

10\. Click **Create Listener**.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/configure-listener.png" alt="Listener configuration" width="55%">

### Pool

Configure a pool—a list of VMs to which the listener will redirect incoming traffic. Click **Add new pool** in the "Listeners" block to start configuring.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-4-pools-lb.png" alt="Add pools" width="55%">

1\. Specify the pool name.

2\. Select the balancing algorithm:          
 
- **Round robin**—requests are distributed across servers within a cluster one by one: the first request is sent to the first server, the second request is sent to the second server, and so on in a circle. 
- **Least Connection**—new requests are sent to a server with the fewest active connections. 
- **Source IP**—a client's IP address is used to determine which server receives the request. 

3\. A protocol will be automatically selected based on the listener's settings: the HTTP listener can communicate with servers via the HTTP protocol.

4\. Select **App Cookie** and fill in the "Cookie" field. <a href="https://code.google.com/p/nginx-sticky-module/)" target="_blank">A special module</a> creates a cookie and then uses it to forward requests to the same server.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-4-pool-conf-lb.png" alt="Pool configuration" width="70%">

### Virtual Machine 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-4-instance-lb.png" alt="Add Virtual Machine" width="65%">

Click **Add Instance** to add Virtual Machines that will participate in the traffic distribution for the configured listener. 

1\. Select Custom IP, Virtual Machine, or Bare Metal and appropriate configurations. 

2\. Specify its port and weight in the distribution. 

### Health Сheck

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-4-instance-conf-lb.png" alt="Configure Health Check" width="65%">

1\. Select the protocol for checking: TCP, Ping, HTTP and appropriate configurations. 

2\. Specify сheck interval (sec)—time between sent requests.

3\. Specify response time (sec)—the time to wait for a response from a server.

4\. Specify unhealthy threshold—the number of failed requests after which traffic will no longer be sent to the Virtual Machine.

5\. Specify healthy thresholds—the number of successful requests after which the Virtual Machine will be considered ready to receive traffic.

### Timeouts

Specify client data, member connect and member data timeouts in msec.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-4-timeouts-lb.png" alt="Configure timeouts" width="65%">

## Step 6. Enter the name

Enter a name for the Load Balancer. It will be displayed in the Customer Portal.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-6-lb.png" alt="Enter Load Banalcer name" width="65%">

## Step 7. (Optional) Enable Logging

The Logging service will be activated to store your logs. To learn how it works and how to configure it, refer to the article about <a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">Logging</a>.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-7-lb.png" alt="Configure Logging" width="65%">

## Step 8. (Optional) Add tags

Create tags for your load balancer by entering "Key" and "Valu."

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/step-8-lb.png" alt="Configure tags" width="65%"> 

## Step 9. Finalize creation

Check the settings and click **Create Load Balancer** on the right. 

## Step 10. Configure firewall

Configure firewalls for Virtual Machines in the pool according to the <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall" target="_blank">separate guide</a>.

Make sure their ports are open for the Load Balancer traffic:

- If a Load Balancer and Virtual Machines are in a **public network,** set a rule to receive and transmit traffic to the balancer's IP address (specified in the menu) in firewalls settings of the VM.
- If a Load Balancer and Virtual Machines are in a **private subnetwork,** set a rule to receive and transmit traffic to the entire private subnetwork or to the balancer's IP address (specified in the menu).
- If a Load Balancer is in a **public network** and Virtual Machine are in a **private subnetwork**, set a rule to receive and transmit traffic to the entire private subnetwork or to the balancer's internal IP address (send a request to the technical support).

In the Load Balancers section, open the created balancer and click **Create** or **Edit** a custom security group (this is the firewall) and edit it: configure the rules for inbound and outbound traffic.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/firewall-lb.png" alt="Create a custom security group also known as a firewall">
