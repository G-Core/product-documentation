---
title: manage-load-balancers
displayName: Manage load balancer
published: true
order: 15
toc:
   --1--Manage: "manage-a-load-balancer"
   --1--Balancer statuses: "load-balancer-statuses"
   --1--Performance analysis: "performance-analysis"
pageTitle: Configure a Load Balancer | Gcore
pageDescription: Learn how to configure a load balancer to distribute incoming requests across VMs, improving the fault tolerance of your infrastructure.
---
# Manage load balancers

The list of created balancers is located inside the project - > Networking - > Load balancers

There you can:

*   Configure a balancer (the "Overview" option) 
*   Rename a balancer (the "Edit" option) 
*   Delete a balancer

To do it, select the necessary action on the selector on the right from the balancer.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/____________________.png" alt="Interface for managing created Load Balancers">

Go to your project - > Networking - > Load balancers -> select the Overview option on the selector on the right from the chosen balancer.

In the drop-down window, you can edit existing listeners in the load balancer and also add new ones.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/________________________________________.png" alt="Add new Listener">

You can **edit** and **delete** listeners. Select the appropriate option on the selector on the right from the listener. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/____________________________.png" alt="Edit or Delete listeners">

In the editor, you can:

*   Change the checking algorithm

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/_______________.png" alt="_______________.png">

*   Parameters of connected instances (including verification address, port, and weight)

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/______________.png" alt="______________.png">

*   Enable and disable instances from the load balancing pool

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/__________________________.png" alt="__________________________.png">

*   Change the parameters in the Health Check section

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-configure-a-load-balancer/__________________.png" alt="Health Check configuration">

## Load Balancer statuses

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
