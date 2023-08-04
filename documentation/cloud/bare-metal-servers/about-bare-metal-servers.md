---
title: about-bare-metal-servers
displayName: About bare metal servers
published: true
order: 10
toc:
   --1--What is a bare metal server?: "what-is-a-bare-metal-server"
   --1--How does the service work?: "how-does-bare-metal-work"
   --1--Configurations: "bare-metal-configurations"
   --1--Benefits: "benefits-of-bare-metals"
   --1--Use cases: "use-cases"
   --1--Pricing: "pricing"
   --1--Bare metals vs. virtual machines: "bare-metals-vs-virtual-machines"
   --1--Bare metals vs. dedicated servers in Hosting: "bare-metals-vs-dedicated-servers-in-hosting"
pageTitle: Bare metal servers | Gcore
pageDescription: Explore bare metal servers for gaming, HPC, and big data. High performance, fault-tolerance, data security. Compare virtual machines & bare metal.
---
# About bare metal servers

## What is a bare metal server?

A bare metal server is a form of cloud service in which the user rents a physical machine from a provider. This machine is dedicated to the user and not shared with any other tenants.

You can rent one or multiple bare metals in one of <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">15+ locations</a>. You can find all the locations on <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">our website</a>.

## How does bare metal work?

When you rent a bare metal server, we allocate the entire physical machine exclusively for you, set up networking configuration (you can configure simple public access or make your own private network landscape with other cloud services), and install the operating system (you can choose existing OS images or use your own ISO file).

You have 100% access to the computing and networking power of the machine because the server environment is fully isolated.

There are several options to manage a bare metal server:

*   Gcore control panel
*   API. To learn more, see <a href="https://api.gcore.com/docs/cloud" target="_blank">our API documentation</a>
*   Terraform. To learn more, see <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/baremetal" target="_blank">our official Terraform provider documentation for bare metal servers</a>

## Bare metal configurations

We offer three types of in-stock configurations:

*  **Basic single**. These servers are core servers typically equipped with 2236/2336 or similar CPUs, suitable for lightweight applications or micro-containers.
*  **High-frequency**. These servers are single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.
*  **Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores and are optimized for multithreading.

If you want a custom configuration, contact our [Sales team](mailto:sales@gcore.com). They will help you find the best solution for your needs.

You set up your bare metal with the OS of your choice. By default, we offer various ones: Ubuntu, CentOS, Debian, and Windows. You can use a pre-set OS image or upload your own.

Our bare metals are deployed with LACP-aggregated network ports by default. This improves server availability and traffic throughput. Moreover, you can assign both public and private interfaces to your machine. It lets you connect your bare metals and virtual machines into single private networks.

## Benefits of bare metals

Bare metal servers have the following benefits:

*   **High performance.** Get direct access to the physical components of your server and use 100% of its resources.
*   **Fault-tolerance.** Minimize your server downtime with power backup and redundant network interfaces. Firstly, if the primary power supply goes down, your server will keep working because the backup supply will start providing power. Secondly, if a network port fails, your server will still be online because the traffic will be automatically routed to the second port.
*   **Your data security.** Leverage single-tenant access to the hardware to avoid unwelcome intruders. Since we dedicate an entire physical server to you, only you or your authorized users with access rights can connect to it.
*   **Fast deployment time.** Get your server ready within 10-15 minutes after purchasing it.
*   **Easy management.** Create, rebuild, and control your bare metals via the <a href="https://cloud.gcore.com" target="_blank">Gcore control panel</a>, <a href="https://api.gcore.com/docs/cloud" target="_blank">API</a>, or <a href="https://registry.terraform.io/providers/G-Core/gcore" target="_blank">Terraform provider</a>.
*   **Scalability.** Scale your resources up or down on demand. Whenever you need extra resources, you can easily create new virtual machines and bare metals and connect them to existing ones. Once your workload decreases, you can delete the added resources and stop paying for them.
*   **Hybrid landscape.** Bring virtual machines and bare metals together into single networks.
*   **Gcore integration.** Integrate bare metals with other Gcore services, such as <a href="https://gcore.com/cdn" target="_blank">CDN</a>, <a href="https://gcore.com/streaming-platform" target="_blank">Streaming Platform</a>, or  <a href="https://gcore.com/ddos-protection" target="_blank">DDoS Protection</a>.

## Use cases

Considering the benefits of bare metal servers, they can be the best solution for the following tasks:

*   **Gaming applications** where superior performance and low latency are extremely critical.
*   **High-performance computing (HPC)** that requires a large amount of processing power for CPU-intensive workloads such as machine learning or AI modeling.
*   **Big data analytics** that need optimal computing resources, security, and storage.
*   **Database servers** that can benefit you if you deploy your app on a virtual machine and migrate its database to a bare metal server.
*   **Containers/virtualization** that are best deployed on dedicated servers and managed via an API.
*   **E-Commerce** websites and applications.
*   Video production/game development **rendering**.

## Pricing

Bare metals are billed per minute. The price depends on the configuration and location.

We offer two billing options:

*   The pay-as-you-go (PAYG) model is best for short-term rental, where you pay for the number of minutes you use the service.
*   A monthly subscription is best for long-term rental, where you regularly pay once a month.

If you're committed to paying 12+ months upfront or buying multiple bare metal servers at once, we can offer you a discount. Contact our [Sales team](mailto:sales@gcore.com) for details.

Please note: a bare metal server is billed even while it's stopped because all resources are still reserved for you. If you want to stop charges, delete your server.

If you want to test the service, you can activate the Trial Period. It will expire in 14 days, and you'll be switched to the basic PAYG plan.

## Bare metals vs. virtual machines

When evaluating bare metal servers, users still gravitate toward the comparison to virtual servers. For most companies, the criteria for choice are application-specific or workload-specific. It's common for a company to use a mix of bare metal servers along with virtualized resources across their cloud environment.

Virtual servers are the more common model of cloud computing because they offer greater resource density, faster provisioning times, and the ability to scale up and down quickly as needs dictate.

But bare metal servers are the right fit for a few primary use cases that take advantage of the combination of attributes. These attributes are dedicated resources, greater processing power, and more consistent disk and network I/O performance.

*   Performance-centric app and data workloads: The complete access and control over hardware resources make bare metal a good match for workloads such as HPC, big data, and high-performance databases, as well as gaming and finance workloads.
*   Apps with complex security or regulatory requirements: The combination of a global data center footprint with physical resource separation has helped many organizations adopt a cloud while simultaneously meeting complex security and regulatory demands.
*   Large, steady-state workloads: For applications such as ERP, CRM, or SCM that have a relatively stable set of ongoing resource demands, bare metal servers can also be a good fit.

## Bare metals vs. dedicated servers in Hosting

The table below shows the key differences between our bare metal servers in <a href="https://gcore.com/cloud" target="_blank">Cloud</a> and dedicated servers in <a href="https://gcore.com/hosting" target="_blank">Hosting</a>.

 

|                                       | Bare metals                                                                                                                                                                                                                                            | Dedicated servers                                                                                    |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Management                            | Gcore control panel, API, Terraform                                                                                                                                                                                                                    | DCImanager, IPMI, SSH                                                                                |
| Server administration                 | Automated for a user                                                                                                                                                                                                                                   | Done per user                                                                                        |
| Billing                               | Per minute                                                                                                                                                                                                                                             | Fixed amount monthly/daily                                                                           |
| Scalability                           | On-demand within 10–15 minutes for basic configurations                                                                                                                                                                                                | Limited                                                                                              |
| Interaction with other Cloud services | Yes                                                                                                                                                                                                                                                    | No                                                                                                   |
| Interaction with other Gcore services | Yes                                                                                                                                                                                                                                                    | No                                                                                                   |
| Usability                             | Complex infrastructure, intensive workloads, possible traffic spikes, networks between virtual and bare metal servers, interaction with other Cloud services (load balancers, Kubernetes), internal virtualization and containers | Small- and medium-sized projects, simple web applications, predictable workloads, low budget |
