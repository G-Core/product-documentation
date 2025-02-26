---
title: create-and-manage-a-router
displayName: Router
published: true
order: 30
toc:
   --1--Create a router: "create-a-router"
   --2--Create a router manually: "create-a-router-manually"
   --2--Router control and route tables: "router-control-and-route-tables"
   --1--Manage routers: "manage-routers"
   --2--Configure subnetworks: "configure-subnetworks"
   --2--Configure static routes: "configure-static-routes"
   --3--Host routes (Layer 2): "host-routes-layer-2"
   --3--Router static routes (Layer 3): "router-static-routes-layer-3"
pageTitle: Add a router | Gcore
pageDescription: Learn how to create and manage a router in the cloud to dynamically exchange routes between networks.
---
# Create and manage a router

Cloud Router enables you to dynamically exchange routes between networks. You can find the list of routers in networking settings, on the **Routers** page.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/routers-page.png" alt="Routers page in the Customer Portal" width="80%">

## Create a router

A router can be created in two ways:  

* Manually on the **Routers** page as documented in the following section. 

* After you create a <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">network</a>, a new router is automatically created in the cloud to enable traffic routing. You can configure automatically created routers using the same settings available for manually created routers. 

### Create a router manually 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Networking**. 

2\. Go to the **Routers** page and click **Create router**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-button.png" alt="Create router button highlighted" width="80%">

3\. Select the network and subnetwork to configure routing. If necessary, you can add multiple subnetworks by clicking on **Add Subnet**. For more information about creating and configuring a network and subnetwork, refer to our <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">Networking</a> guide.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-add-interfaces.png" alt="Create router menu" width="80%">

4\. (Optional) Turn on the **Enable SNAT** toggle if you need access to the external network. A separate public IP address is announced for a router with access to an external network. 

5\. You can specify the routing scheme in the **Static Routes** section. Provide the destination prefix and the address of the next hop. To add the next route, click the **Add Route** button. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-snat-static-routes.png" alt="Create router menu" width="80%">

6\. Give your router a name and save the configuration by clicking **Create Router**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-name.png" alt="Create router menu" width="80%">

### Router control and route tables

Routing is based on route tables, which define the paths that network traffic takes from a VM to other destinations. These destinations can be inside or outside the private network. The tables contain static routes, which consist of a target subnet prefix in CIDR notation and the nexthop's internal IP address (the virtual machine or router handling the traffic).

A router is automatically created when a network is created, but customers can also create and configure routers manually.

By default, all routers have SNAT (Source Network Address Translation) enabled, allowing instances in a private network to access the external network. 

Customers can add subnets to a router and define static routes for controlling traffic flow.

## Manage routers 

To manage routers: 

1\. Open the **Routers** page in the Gcore Customer Portal.  

2\. Click the router name to access its settings. Alternatively, click the three-dot icon next to the router you want to manage and then select **Overview**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/router-name-highlighted.png" alt="Routers page with example router" width="80%">

3\. On the router overview page, you can find general information such as router ID, whether there is a SNAT for accessing the external network, creation dates, and external IPs. Here you can also configure and add new subnetworks as well as update static routes.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/router-settings.png" alt="Routers overview page" width="80%">

### Configure a subnetwork  

In the **Subnets** section, you can manage the list of subnets added to the router, add new subnets, and delete the existing ones. 

When creating a subnetwork, pay attention to the supported CIDR ranges: 

* 10.0.0.0/8 
* 172.16.0.0/12 
* 192.168.0.0/16
* fc00::/7 

<alert-element type="warning" title="Warning">

The specified CIDR ranges must align with the destinations configured in your static routes. 

</alert-element>

We support both IPv4 and IPv6 subnetworks, but there are key differences. IPv4 is fully supported without restrictions. IPv6 has limitations: Floating IPs are not supported, private IPv6 subnets are not publicly routable, and only public IPv6 subnets can access the internet. 

## Configure static routes 

There are two types of static routes: host routes (Layer 2) for internal subnet routing and router static routes (Layer 3) for inter-network traffic control.

### Host routes for subnets (Layer 2)

Host routes operate at Layer 2 without relying on a router, controlling traffic flow within a subnet. They are assigned to instances through DHCP or cloud-init instead of being distributed by a router. DHCP dynamically assigns host routes based on network configurations, while cloud-init configures them automatically at instance startup using predefined settings.

Host routes are automatically assigned to instances within the same subnet and do not require manual configuration. They are not advertised beyond the subnet, ensuring traffic stays internal.

### Router static routes (Layer 3)

Router-level static routes operate at Layer 3 and require a router to forward traffic between networks. These routes are distributed to instances using Router Advertisement. When a router is present, it announces available routes to connected instances.

To configure a static route:

1\. Go to the **Routers** page in the Gcore Customer Portal.

2\. Open the settings of the desired router.

3\. Open the **Static Routes** tab.

4\. Click **Edit Static Routes** → **Add Route**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/configure-static-routes.png" alt="Static routes settings" width="80%">

5\. Enter Destination and Nexthop.

6\. Click **Save Static Routes**.

By default, subnets within the same network can communicate. This is because the default network router automatically unites all subnets within the network, enabling internal communication. However, traffic between different networks requires an explicit static route via a router.

