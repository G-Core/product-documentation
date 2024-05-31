---
title: about-bare-metal-servers
displayName: About Bare Metal servers
published: true
order: 10
toc:
   --1--How does the service work?: "how-does-bare-metal-work"
   --1--Configurations: "bare-metal-configurations"
   --1--Benefits: "benefits-of-bare-metal"
   --1--Use cases: "use-cases"
   --1--Pricing: "pricing"
   --1--Bare metal vs. Virtual Machines: "bare-metal-vs-virtual-machines"
   --1--Bare metal vs. Dedicated Servers in Hosting: "bare-metal-vs-dedicated-servers-in-hosting"
pageTitle: Bare Metal servers | Gcore
pageDescription: Explore Bare Metal servers for gaming, HPC, and big data. High performance, fault-tolerance, data security. Compare Virtual Machines & Bare Metal.
---
# About Bare Metal

Bare Metal is a form of cloud service in which the user rents a physical machine from a provider. This machine is dedicated to the user and not shared with any other tenants.

You can rent one or multiple Bare Metal servers in one of <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">15+ locations</a>. You can find all the locations on <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">our website</a>.

## How does Bare Metal work?

When you rent a Bare Metal server, we allocate the entire physical machine exclusively for you, set up networking configuration (you can configure simple public access or make your own private network landscape with other cloud services), and install the operating system (you can choose existing OS images or use your own ISO file).

You have 100% access to the computing and networking power of the machine because the server environment is fully isolated.

There are several options to manage a Bare Metal server:

*   Gcore Customer Portal
*   API. To learn more, see <a href="https://api.gcore.com/docs/cloud" target="_blank">our API documentation</a>
*   Terraform. To learn more, see <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/baremetal" target="_blank">our official Terraform provider documentation for Bare Metal servers</a>

## Bare Metal configurations

We offer three types of in-stock configurations:

*  **Basic single**. These servers are core servers typically equipped with 2236/2336 or similar CPUs, suitable for lightweight applications or micro-containers.
*  **High-frequency**. These servers are single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.
*  **Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores and are optimized for multithreading.

If you want a custom configuration, contact our [Sales team](mailto:sales@gcore.com). They will help you find the best solution for your needs.

You set up your Bare Metal with the OS of your choice. By default, we offer various ones: Ubuntu, CentOS, Debian, and Windows. You can use a pre-set OS image or upload your own.

Our Bare Metal servers are deployed with LACP-aggregated network ports by default. This improves server availability and traffic throughput. Moreover, you can assign both public and private interfaces to your machine. It lets you connect your Bare Metal servers and Virtual Machines into single private networks.

## Benefits of Bare Metal

Bare Metal servers have the following benefits:

*   **High performance.** Get direct access to the physical components of your server and use 100% of its resources.
*   **Fault-tolerance.** Minimize your server downtime with power backup and redundant network interfaces. Firstly, if the primary power supply goes down, your server will keep working because the backup supply will start providing power. Secondly, if a network port fails, your server will still be online because the traffic will be automatically routed to the second port.
*   **Your data security.** Leverage single-tenant access to the hardware to avoid unwelcome intruders. Since we dedicate an entire physical server to you, only you or your authorized users with access rights can connect to it.
*   **Fast deployment time.** Get your server ready within 10-15 minutes after purchasing it.
*   **Easy management.** Create, rebuild, and control your Bare Metal via the <a href="https://cloud.gcore.com" target="_blank">Gcore Customer Portal</a>, <a href="https://api.gcore.com/docs/cloud" target="_blank">API</a>, or <a href="https://registry.terraform.io/providers/G-Core/gcore" target="_blank">Terraform provider</a>.
*   **Scalability.** Scale your resources up or down on demand. Whenever you need extra resources, you can easily create new Virtual Machines and Bare Metal servers and connect them to existing ones. Once your workload decreases, you can delete the added resources and stop paying for them.
*   **Hybrid landscape.** Bring Virtual Machines and Bare Metal together into single networks.
*   **Gcore integration.** Integrate Bare Metal with other Gcore services, such as <a href="https://gcore.com/cdn" target="_blank">CDN</a>, <a href="https://gcore.com/streaming-platform" target="_blank">Streaming Platform</a>, or  <a href="https://gcore.com/ddos-protection" target="_blank">DDoS Protection</a>.

## Use cases

Considering the benefits of Bare Metal, they can be the best solution for the following tasks:

*   **Gaming applications** where superior performance and low latency are extremely critical.
*   **High-performance computing (HPC)** that requires a large amount of processing power for CPU-intensive workloads such as machine learning or AI modeling.
*   **Big data analytics** that need optimal computing resources, security, and storage.
*   **Database servers** that can benefit you if you deploy your app on a Virtual Machine and migrate its database to a Bare Metal server.
*   **Containers/virtualization** that are best deployed on dedicated servers and managed via an API.
*   **E-Commerce** websites and applications.
*   Video production/game development **rendering**.

## Pricing

Bare Metal servers are billed per minute. The price depends on the configuration and location.

We offer two billing options:

*   The pay-as-you-go (PAYG) model is best for short-term rental, where you pay for the number of minutes you use the service.
*   A monthly subscription is best for long-term rental, where you regularly pay once a month.

If you're committed to paying 12+ months upfront or buying multiple Bare Metal servers at once, we can offer you a discount. Contact our [Sales team](mailto:sales@gcore.com) for details.

Please note: a Bare Metal server is billed even while it's stopped because all resources are still reserved for you. If you want to stop charges, delete your server.

If you want to test the service, you can activate the Trial Period. It will expire in 14 days, and you'll be switched to the basic PAYG plan.

## Bare Metal vs. Virtual Machines

When evaluating Bare Metal, users still gravitate toward the comparison to Virtual Machines. For most companies, the criteria for choice are application-specific or workload-specific. It's common for a company to use a mix of Bare Metal servers along with virtualized resources across their cloud environment.

Virtual Machines are the more common model of cloud computing because they offer greater resource density, faster provisioning times, and the ability to scale up and down quickly as needs dictate.

But Bare Metal servers are the right fit for a few primary use cases that take advantage of the combination of attributes. These attributes are dedicated resources, greater processing power, and more consistent disk and network I/O performance.

*   Performance-centric app and data workloads: The complete access and control over hardware resources make Bare Metal a good match for workloads such as HPC, big data, and high-performance databases, as well as gaming and finance workloads.
*   Apps with complex security or regulatory requirements: The combination of a global data center footprint with physical resource separation has helped many organizations adopt a cloud while simultaneously meeting complex security and regulatory demands.
*   Large, steady-state workloads: For applications such as ERP, CRM, or SCM that have a relatively stable set of ongoing resource demands, Bare Metal servers can also be a good fit.

## Bare Metal vs. Dedicated Servers in Hosting

The table below shows the key differences between our Bare Metal servers in <a href="https://gcore.com/cloud" target="_blank">Cloud</a> and Dedicated Servers in <a href="https://gcore.com/hosting" target="_blank">Hosting</a>.

 

|                                       | Bare Metals                                                                                                                                                                                                                                            | Dedicated Servers                                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Management                            | Gcore Customer Portal, API, Terraform                                                                                                                                                                                                                    | DCImanager, IPMI, SSH                                                                                |
| Server administration                 | Automated for a user                                                                                                                                                                                                                                   | Done per user                                                                                        |
| Billing                               | Per minute                                                                                                                                                                                                                                             | Fixed amount monthly/daily                                                                           |
| Scalability                           | On-demand within 10–15 minutes for basic configurations                                                                                                                                                                                                | Limited                                                                                              |
| Interaction with other Cloud services | Yes                                                                                                                                                                                                                                                    | No                                                                                                   |
| Interaction with other Gcore services | Yes                                                                                                                                                                                                                                                    | No                                                                                                   |
| Usability                             | Complex infrastructure, intensive workloads, possible traffic spikes, networks between Virtual and Bare Metal servers, interaction with other Cloud services (Load Balancers, Managed Kubernetes), internal virtualization and containers | Small- and medium-sized projects, simple web applications, predictable workloads, low budget |
