---
title: create-and-manage-a-router
displayName: Router
published: true
order: 30
toc:
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

5\. In the **Static Routes** section, you can specify the routing scheme. Provide the destination prefix and the address of the next hop. To add the next route, click the **Add Route** button. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-snat-static-routes.png" alt="Create router menu" width="80%">

6\. Give your router a name and save the configuration by clicking **Create Router**.

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/create-router-name.png" alt="Create router menu" width="80%">

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

## Configure static routes 

In the **Static Routes** section, you can update the destination and nexthop of your routes, add new ones, or remove static routes from the router. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/configure-static-routes.png" alt="Static routes settings" width="80%">