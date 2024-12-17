---
title: load-balancers
displayName: Load Balancers
published: true
pageTitle: About Load Balancers | Gcore
pageDescription: A short overview of the Gcore Lead Balancers and their performance test results.
---
# Load Balancers

A Load Balancer is a tool used to sort incoming requests across Virtual Machines and Bare Metal servers to improve your infrastructure's fault tolerance.  

Gcore Load Balancers come with various configuration options to fit different network requirements. We’ve also conducted multiple performance tests on available flavors to help you make an informed decision and select the most effective solution for your infrastructure. 

Our Load Balancers also support long (keepalive) connections through Server-Sent Events (SSE), Long polling, and WebSockets. To keep the connections consistently stable, you need to adjust the data timeout to the appropriate values based on your application's requirements. 

## Performance analysis

We’ve tested our Load Balancers to determine the performance of different flavors.  

For each flavor, we’ve deployed the client in multithreading mode with 36 concurrent threads and 400 connections over the test duration of 30 seconds. 

The results show: 

* **Throughput**: The number of requests per second (RPS) a Load Balancer can handle under a number of simultaneous users’ requests. 

* **Latency**: Response times for both HTTP and HTTPS traffic across different Load Balancer flavors. 

<table>
<tbody>
<tr>
    <th rowspan="2" style="width:30%">Flavor</th>
    <th colspan="2" style="width:35%">HTTP</th>
    <th colspan="2" style="width:35%">HTTPS</th>
  </tr>
  <tr>
    <th>Throughput</th>
    <th>Latency (ms)</th>
    <th>Throughput</th>
    <th>Latency (ms)</th>
  </tr>
  <tr>
    <td>1 vCPU - 2 GiB</td>
    <td>21k</td>
    <td>4</td>
    <td>20k</td>
    <td>20</td>
  </tr>
  <tr>
    <td>2 vCPU - 4 GiB</td>
    <td>45k</td>
    <td>3</td>
    <td>34k</td>
    <td>12</td>
  </tr>
  <tr>
    <td>4 vCPU - 8 GiB</td>
    <td>91k</td>
    <td>5</td>
    <td>51k</td>
    <td>8</td>
  </tr>
  <tr>
    <td>8 vCPU - 16 GiB</td>
    <td>142k</td>
    <td>3</td>
    <td>117k</td>
    <td>4</td>
  </tr>
</tbody>
</table>

