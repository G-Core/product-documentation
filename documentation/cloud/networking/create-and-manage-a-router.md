---
title: create-and-manage-a-router
displayName: Router
published: true
order: 30
toc:
    --1--Router creation: "router-creation"
    --1--Managing routers: "managing-routers"
pageTitle: Add a router | Gcore
pageDescription: Learn how to create and manage a router in the cloud to dynamically exchange routes between networks.
---
# Create and manage a router

**Cloud Router** enables you to dynamically exchange routes between networks. 

The list of routers is located inside the project, section Networking → Routers 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/1._______________.png" alt="1._______________.png">

## Router creation

There are two ways to create a router: 

**1\. Manually from the routers section** 

Go to the project, section Networking → Routers and click on Create router. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/2.______________________.png" alt="2.______________________.png">

In the appeared window configure a new router: 

1.1. Select the network and subnet to configure routing. If necessary, you can add multiple subnets by clicking on Add subnet. For more information about creating and configuring a network and subnet, see the article <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">Networking</a>. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/3._________.png" alt="3._________.png">

1.2. Activate the Enable SNAT selector if you need access to the external network. 

A separate public IP address is announced for a router with access to an external network. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/4._SNAT.png" alt="4._SNAT.png">

1.3. In the Static routes section, you can specify the routing scheme 

Specify the destination prefix and the address of the next hop. To add the next route, click the Add route button. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/5.______.png" alt="5.______.png">

1.4. Enter a name for the router and click Create router. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/6.______________.png" alt="6.______________.png">

**2\. Automatically after creating a network** 

After creating a network, a new router is being automatically created in the cloud to allow further routing of traffic.  

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/7.____________.png" alt="7.____________.png">

For more information about creating and configuring a network and subnet, see the article <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">Networking</a>.

For automatically created routers, you can make the same settings as for manually created routers. 

## Managing routers

To manage routers, open the list of routers: inside the project, section Networking → Routers 

To make changes with an existing router, click the selector on the right from the selected router and select the Overview option. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/8._Overview.png" alt="8._Overview.png">

In the appearing window, you can find general information about the router: the router ID, whether there is a SNAT for accessing the external network, and the creation date. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/9._ID_SNAT_Time.png" alt="9._ID_SNAT_Time.png">

In the Subnets section, you can manage the list of subnets added to the router: add new subnets and delete old ones. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/10._Subnet_______.png" alt="10._Subnet_______.png">

To edit routes, go to the Static routes tab and click Edit static routes. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/11._Edit_static_routes.png" alt="11._Edit_static_routes.png">

To add a new route, click Add Route and specify the destination prefix and address of the nexthop, or delete an unnecessary route by clicking the Delete button on the right of the route. 

<img src="https://assets.gcore.pro/docs/cloud/networking/create-and-manage-a-router/12._Add_and_delete_route.png" alt="12._Add_and_delete_route.png">

To save settings, click Save static routes.