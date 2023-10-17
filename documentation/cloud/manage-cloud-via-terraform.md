---
title: manage-cloud-via-terraform
displayName: Terraform
published: true
order: 130
toc:
   --1--What is Terraform?: "what-is-terraform"
   --1--Install and configure Terraform: "install-terraform-and-integrate-it-with-our-cloud"
   --1--Manage Cloud resources: "manage-cloud-resources-via-terraform"
   --2--Create a bare metal server: "create-a-bare-metal-server"
   --2--Create an instance: "create-an-instance"
   --2--Create a Kubernetes cluster: "create-a-kubernetes-cluster"
   --2--Create a Kubernetes pool: "create-a-kubernetes-pool"
   --2--Create a load balancer: "create-a-load-balancer"
   --2--Create a network and subnetwork: "create-a-network-and-subnetwork"
   --2--Create a server group: "create-a-server-group"
   --2--Create a snapshot: "create-a-snapshot"
   --2--Create a volume: "create-a-volume"
   --2--Reserve an IP address: "reserve-an-ip-address"
pageTitle: Manage Cloud via Terraform | Gcore
pageDescription: Learn how to manage your cloud resources using Terraform. Follow the guide to install Terraform and create VMs, K8s clusters, load balancers, and more.
---
# Manage Cloud via Terraform

## What is Terraform?

Terraform is a declarative command-line utility used to manage the infrastructure of Terraform partner providers. With this tool, you can manage our Cloud service.

To work with Terraform, you create a configuration file where you specify the changes you want to make to your Cloud resources, for example, to create an instance or a Kubernetes cluster. Then you run the Terraform command to make changes. The utility reads the configuration file and sends the necessary API requests. The required Cloud settings are then applied.

## Install Terraform and integrate it with our Cloud

1\. Download a Terraform package suitable for your OS from the <a href="https://terraform.io/downloads" target="_blank">official Terraform website</a>.

2\. Create a new folder and name it the same as the downloaded package.

3\. Unzip the Terraform archive in the new folder.

4\. Add the directory of the unzipped Terraform archive to the PATH environment variable.

5\. Create a configuration file in the Terraform folder and name it **main.tf**.

6\. Find out the latest version of the Terraform provider on <a href="https://registry.terraform.io/providers/G-Core/gcore/latest" target="_blank">the page</a> and generate a permanent API token using <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">the guide</a>, if you don’t have one yet.

7\. Add the following code to main.tf:

<code-block>
terraform {
  required_version = ">=0.13.0"
  required_providers {
    gcore = {
      source = "G-Core/gcore"
      version = "<span style="color:#FF5913">0.3.55</span>"
   }
  }
}
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">123$61b8e1e7a68c</span>"
}
</code-block>

Enter your values instead:

- <span style="color:#FF5913">0.3.55</span>—the Terraform provider version  
- <span style="color:#FF5913">123$61b8e1e7a68c</span>—the permanent API token

8\. Open the command line, access the Terraform folder and run the following command:

```
terraform init
```

You’ll get the output:

<img src="https://assets.gcore.pro/docs/cloud/manage-cloud-via-terraform/12966689446417.png" alt="output" width="80%">

This means Terraform has been successfully downloaded and installed, and you can start working with it.

## Manage Cloud resources via Terraform

If you have already worked with Terraform, you can use this abridged guide on how to manage Gcore Cloud resources:

1\. Go to the Terraform documentation, click **Resources**, and copy the necessary code to main.tf.

2\. Customize values in the code.

3\. Run the following command to preview the expected changes:

```
terraform plan
```

4\. Run the following command to apply these changes:

```
terraform apply
```

You can also use our step-by-step guides below.

### Create a bare metal server

1\. Open the **main.tf** file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_baremetal" "<span style="color:#FF5913">bm</span>" {
  name       = "<span style="color:#FF5913">baremetal_example</span>"
  flavor_id  = "<span style="color:#FF5913">bm1-infrastructure-small</span>"
  interface {
      type = "<span style="color:#FF5913">external</span>"
              <span style="color:#FF5913">is_parent = "true"</span>
  }
}
</code-block>

3\. Configure your bare metal server.

* Specify "flavor_id".

* Configure “interface”.
  
  Select the interface "type": "external", "subnet", "any_subnet", or "reserved_fixed_ip".  
    - If you select "subnet", specify the "network_ID" and "subnetwork_ID".  
    - If you select "anu_subnet", specify the "network_ID".  
    - If you select "reserved_fixed_ip", specify the "port_id".
  
  (optional) Add <span style="color:#FF5913">is_parent = "true"</span> to ensure the interface cannot be detached and is always connected first.
  
  (optional) Specify "order" to set the order in which interfaces will be attached.

* (optional) Specify "app_config" to set parameters for the application template from the marketplace.

* (optional) Specify the "image_id" or "apptemplate_id".

* (optional) Specify the "keypair_name".

* (optional) Specify the "name" of the server.

* (optional) Specify the "region_id" and "region_name".

* (optional) Specify the "project_id" and "project_name".

* (optional) Specify the "metadata_map": "key" and "value".

* (optional) Specify "username" and/or "password".

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the changes:

```
terraform plan
```

If the code contains an error, the output will show it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter "yes".

### Create an instance

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}  
resource "gcore_reservedfixedip" "<span style="color:#FF5913">fixed_ip</span>" {
  type             = "ip_address"
  network_id       = "<span style="color:#FF5913">faf6507b-1ff1-4ebf-b540-befd5c09fe06</span>"
  fixed_ip_address = "<span style="color:#FF5913">192.168.13.6</span>"
  is_vip           = <span style="color:#FF5913">false</span>
}
resource "gcore_volume" "first_volume" {
  name       = "<span style="color:#FF5913">boot volume</span>"
  type_name  = "<span style="color:#FF5913">ssd_hiiops</span>"
  size       = <span style="color:#FF5913">10</span>
  image_id   = "<span style="color:#FF5913">6dc4e061-6fab-41f3-91a3-0ba848fb32d9</span>"
}
resource "gcore_floatingip" "<span style="color:#FF5913">fip</span>" {
  fixed_ip_address = <span style="color:#FF5913">gcore_reservedfixedip.fixed_ip.fixed_ip_address</span>
  port_id          = <span style="color:#FF5913">gcore_reservedfixedip.fixed_ip.port_id</span>
}
resource "gcore_instance" "<span style="color:#FF5913">v</span>" {
  name       = "<span style="color:#FF5913">hello</span>"
  flavor_id  = "<span style="color:#FF5913">g1-standard-1-2</span>"
  volume {
    source     = "existing-volume"
    volume_id  = <span style="color:#FF5913">gcore_volume.first_volume.id</span>
    boot_index = <span style="color:#FF5913">0</span>
  }
  interface {
    type            = "<span style="color:#FF5913">reserved_fixed_ip</span>"
    port_id         = <span style="color:#FF5913">gcore_reservedfixedip.fixed_ip.port_id</span>
    fip_source      = "<span style="color:#FF5913">existing</span>"
    existing_fip_id = <span style="color:#FF5913">gcore_floatingip.fip.id</span>
    security_groups = <span style="color:#FF5913">["ada84751-fcca-4491-9249-2dfceb321616"]</span>
  }
}
</code-block>

3\. Configure resources required for the instance: [a reserved IP address](https://gcore.com/docs/cloud/manage-cloud-via-terraform#reserve-an-ip-address), [network](https://gcore.com/docs/cloud/manage-cloud-via-terraform#create-a-network-and-subnetwork), [subnetwork](https://gcore.com/docs/cloud/manage-cloud-via-terraform#create-a-network-and-subnetwork), [volume](https://gcore.com/docs/cloud/manage-cloud-via-terraform#create-a-volume).

4\. Configure the instance.

* Specify "flavor_id".

* Select the interface "type": "external", "subnet", "any_subnet", or "reserved_fixed_ip".     
  - If you select "subnet", specify the "network_ID" and "subnetwork_ID".  
  - If you select "anu_subnet", specify the "network_ID".  
  - If you select "reserved_fixed_ip", specify the "port_id".
  - (optional) Add is_parent = "true" to ensure the interface cannot be detached and is always connected first.
  - (optional) Specify order to set the order in which interfaces will be attached.

* Configure "volume".

  - Specify "source = existing-volume" and the "volume_id". Optionally, you can specify the size of the existing volume in GB.
  - (optional) Specify the "boot_index". If "boot_index = 0", the volume cannot be detached.
  - (optional) Specify the "type_name": "standard", "ssd_hiiops", "cold", or "ultra".

* (optional) Add "allow_app_ports = true" to allow application ports for instances created from marketplace templates.

* (optional) Specify "configuration" to set parameters for the application template from the marketplace: "key" and "value".

* (optional) Specify the "keypair_name".

* (optional) Specify the "metadata_map": "key" and "value".

* (optional) Specify the "name" of the instance.

* (optional) Specify "username" and "password".

* (optional) Specify the "region_id" and "region_name".

* (optional) Specify the "project_id" and "project_name".

* (optional) Specify the "security_group" to add firewalls.

5\. Save changes in the file.

6\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will describe it.

7\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter "yes".

### Create a Kubernetes cluster

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_k8s" "v" {
  name          = "<span style="color:#FF5913">kluster_example</span>"
  fixed_network = "<span style="color:#FF5913">6bf878c1-1ce4-47c3-a39b-6b5f1d79bf25</span>"
  fixed_subnet  = "<span style="color:#FF5913">dc3a3ea9-86ae-47ad-a8e8-79df0ce04839</span>"
  pool {
    name               = "<span style="color:#FF5913">pool_example</span>"
    flavor_id          = "<span style="color:#FF5913">g1-standard-1-2</span>"
    min_node_count     = <span style="color:#FF5913">1</span>
    max_node_count     = <span style="color:#FF5913">2</span>
    node_count         = <span style="color:#FF5913">1</span>
    docker_volume_size = <span style="color:#FF5913">2</span>
  }
}
</code-block>

3\. Configure the cluster.

* Specify “name”.

* Specify the “fixed_network” of the cluster.

* Specify the “fixed_subnet” and make sure the subnet has a router.

* Specify the “keypair”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

* (optional) Add ```auto_healing_enabled = "true"``` to allow automatic recovery of failed nodes.

* (optional) Add ```external_dns_enabled = "true"``` if you want to enable external DNS.

* Configure the pool, a set of cluster nodes with the same specifications.

  - Specify “name”.
  - Specify “flavor_id”.
  - Specify the “min_node_count” for autoscaling.
  - Specify the “max_node_count” for autoscaling.
  - Specify the “node_count”. This is the initial number of nodes to be deployed.
  - (optional) Specify the “docker_volume_size” in GB.
  - (optional) Select “docker_volume_type”: “standard”, “ssd_hiiops”, “cold”, or “ultra”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a Kubernetes pool

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_k8s_pool" "v" {
  cluster_id         = "<span style="color:#FF5913">6bf878c1-1ce4-47c3-a39b-6b5f1d79bf25</span>"
  name               = "<span style="color:#FF5913">pool_example</span>"
  flavor_id          = "<span style="color:#FF5913">g1-standard-1-2</span>"
  min_node_count     = <span style="color:#FF5913">1</span>
  max_node_count     = <span style="color:#FF5913">2</span>
  node_count         = <span style="color:#FF5913">1</span>
  docker_volume_size = <span style="color:#FF5913">2</span>
}
</code-block>

3\. Configure the pool.

* Specify the “cluster_id” within which you want to create the pool.

* Specify the “name” of your pool.

* Specify “flavor_id”.

* Specify the “min_node_count” for autoscaling.

* Specify the “max_node_count” for autoscaling.

* Specify the “node_count”. This is the initial number of nodes to be deployed.

* (optional) Specify the “docker_volume_size” in GB.

* (optional) Select “docker_volume_type”: “standard”, “ssd_hiiops”, “cold”, or “ultra”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a load balancer

This section explains how to create a load balancer with a pool, listener, and member.

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_loadbalancerv2" "<span style="color:#FF5913">lb</span>" {
  <span style="color:#FF5913">project_id = 1</span>
  <span style="color:#FF5913">region_id  = 1</span>
  name       = "<span style="color:#FF5913">lb_example</span>"
  flavor     = "<span style="color:#FF5913">lb1-1-2</span>"
}
resource "gcore_lblistener" "<span style="color:#FF5913">listener</span>" {
  name            = "<span style="color:#FF5913">listener_example</span>"
  protocol        = "<span style="color:#FF5913">TCP</span>"
  protocol_port   = <span style="color:#FF5913">36621</span>
  loadbalancer_id = <span style="color:#FF5913">gcore_loadbalancerv2.lb.id</span>
}
resource "gcore_lbpool" "<span style="color:#FF5913">pl</span>" {
  name            = "<span style="color:#FF5913">test_pool</span>"
  protocol        = "<span style="color:#FF5913">HTTP</span>"
  lb_algorithm    = "<span style="color:#FF5913">LEAST_CONNECTIONS</span>"
  loadbalancer_id = <span style="color:#FF5913">gcore_loadbalancer.lb.id</span>
  listener_id     = <span style="color:#FF5913">gcore_loadbalancer.lb.listener.0.id</span>
  <span style="color:#FF5913">health_monitor {
    type        = "PING"
    delay       = 60
    max_retries = 5
    timeout     = 10
  }</span>
  <span style="color:#FF5913">session_persistence {
    type        = "APP_COOKIE"
    cookie_name = "test_new_cookie"
  }</span>
}
resource "gcore_lbmember" "lbm" {
  pool_id       = <span style="color:#FF5913">gcore_lbpool.pl.id</span>
  address       = "<span style="color:#FF5913">10.10.2.15</span>"
  protocol_port = <span style="color:#FF5913">8081</span>
  weight        = <span style="color:#FF5913">5</span>
}
</code-block>

3\. Configure the load balancer.

* Specify the “name” of your load balancer.

* Specify “flavor”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

* (optional) Specify the “vip_port_id” or “vip_network_id”.

* (optional) Specify the “vip_subnet_id”.

4\. Configure the listener.

* Specify “name”.

* Select “protocol”: “HTTP”, “HTTPS”, “TCP”, “UDP”, or “TERMINATED_HTTPS”. If you select “TERMINATED_HTTPS”, specify the “secret_id”.

* Specify the “protocol_port”.

* Specify the “loadbalancer_id”.

* (optional) Add ```insert_x_forward = "true"``` to identify an original IP address of a client connecting to a web server via a load

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

5\. Configure the pool.

* Specify “name”.

* Select “protocol”: “HTTP”, “HTTPS”, “TCP”, or “UDP”.

* Select “lb_algorithm”: “ROUND_ROBIN”, “LEAST_CONNECTIONS”, “SOURCE_IP”, or  “SOURCE_IP_PORT”.

* (optional) Add “health_monitor”.

  *   Select “type”: “HTTP”, “HTTPS”, “PING”, “TCP”, “TLS-HELLO”, or “UPD-CONNECT”.
  *   Specify the “delay” in seconds to set the time between sending probe requests to pool members.
  *   Specify the “max_tertires” to set the number of successful probes required to switch a member to the ONLINE state.
  *   Specify the “timeout” in seconds to set the maximum time to connect.
  *   (optional) Select “http_method”: “CONNECT”, “DELETE”, “GET”, “HEAD”, “OPTIONS”, “PATCH”, “POST”, “PUT”, or “TRACE”.
  *   (optional) Specify the “max_retrieve_down” to set the threshold of failures required to switch a member to the ERROR state.
  *   (optional) Specify “expected_codes”
  *   (optional) Specify the “url_path”

* (optional) Specify the “listener_id”.

* (optional) Specify the “loadbalancer_id”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

* (optional) Add “session_persistence”.

  *   Select “type”: “APP_COOKIE”, “HTTP_COOKIE”  
      If you select “APP_COOKIE” or “HTTP_COOKIE”, specify the “cookie_name”.  
      If you select “SOURCE_IP”, specify the “persistence_granularity” (for UDP ports only).
  *   (optional) Specify the “persistence_timeout”.

6\. Configure the member.

* Specify the IP “address”.

* Specify the “pool_id”.

* Specify the “protocol_port”.

* Specify the “instance_id” or “subnet_id”.

* (optional) Specify member “weight” from 0 to 256.

7\. Save changes in the file.

8\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

9\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a network and subnetwork

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_network" "<span style="color:#FF5913">network</span>" {
  name       = "<span style="color:#FF5913">network_example</span>"
  <span style="color:#FF5913">mtu        = 1450</span>
  <span style="color:#FF5913">type       = "vlan"</span>
}
</code-block>

3\. Configure the network.

* Specify “name”.

* (optional) Add ```create_router = "false"``` to remove the external router from the network. Otherwise, the external router will be added by default.

* (optional) Add ```type = "vlan"```. Otherwise, a “vxlan” network will be created by default.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. If you don’t need a subnetwork, skip to Step 6. To create a subnetwork, add the code below and customize the highlighted values:

<code-block>
resource "gcore_subnet" "<span style="color:#FF5913">subnet</span>" {
  name            = "<span style="color:#FF5913">subnet_example</span>"
  cidr            = "<span style="color:#FF5913">192.168.10.0/24</span>"
  network_id      = <span style="color:#FF5913">gcore_network.network.id</span>
}
</code-block>

5\. Configure the subnetwork.

* Specify the “name” of the subnetwork.

* Specify the “cidr”.  

  - Select the IP address from the ranges: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, and 192.168.0.0–192.168.255.255.
  - Select the subnet mask from 16 to 24.

* Specify the “network_id” within which you want to create the subnet.

* (optional) Add ```connect_to_network_router = "true"``` if you want your subnetwork to be accessible for public networks through an external router. If not, add ```connect_to_network_router = "false"```. The default value is “true”.

* (optional) Add the “gateway_ip” of an external router, if any.

* (optional) Specify “dns_nameservers”.

* (optional) Add “host_routes”.

  - Specify the “destination”, the CIDR of the target subnetwork.
  - Specify the “nexthop”, the IPv4 address to forward traffic to if its destination IP matches the “destination” CIDR.

* (optional) Add “enable_dhcp = false” to disable DHCP. Otherwise, DHCP will be enabled by default.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

6\. Save changes in the file.

7\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

8\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a server group

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_servergroup" "<span style="color:#FF5913">default</span>" {
  name       = "<span style="color:#FF5913">server_group_example</span>"
  policy     = "<span style="color:#FF5913">affinity</span>"
  region_id  = <span style="color:#FF5913">1</span>
  project_id = <span style="color:#FF5913">1</span>
}
</code-block>

3\. Configure the server group.

* Specify “name”.

* Select the ```policy: use "affinity"``` to run your servers on one physical server or "anti-affinity" to run your servers on different physical servers.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a snapshot

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_snapshot" "<span style="color:#FF5913">snapshot</span>" {
  project_id  = <span style="color:#FF5913">1</span>
  region_id   = <span style="color:#FF5913">1</span>
  name        = "<span style="color:#FF5913">snapshot_example</span>"
  volume_id   = "<span style="color:#FF5913">28e9edcb-1593-41fe-971b-da729c6ec301</span>"
}
</code-block>

3\. Configure the snapshot.

* Specify “name”.

* Specify the “volume_id”.

* (optional) Add a “description”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will describe it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Create a volume

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_volume" "<span style="color:#FF5913">volume</span>" {
  name       = "<span style="color:#FF5913">volume_example</span>"
  type_name  = "<span style="color:#FF5913">standard</span>"
  size       = <span style="color:#FF5913">1</span>
}
</code-block>

3\. Configure the volume.

* Specify “name”.

* Specify the “snapshot_id” or “image_id”.

* (optional) Specify the “size” of your volume in GB.

* (optional) Select the “type_name”: “standard”, “ssd_hiiops”, “cold”, or “ultra”.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will show it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.

### Reserve an IP address

1\. Open the main.tf file where you configured the Gcore provider for Terraform.

2\. Copy the code below to the file and customize the highlighted values:

<code-block>
provider gcore {
  permanent_api_token = "<span style="color:#FF5913">251$d3361.............1b35f26d8</span>"
}
resource "gcore_reservedfixedip" "<span style="color:#FF5913">fixed_ip</span>" {
  project_id       = <span style="color:#FF5913">1</span>
  region_id  = <span style="color:#FF5913">1</span>
  type       = "<span style="color:#FF5913">external</span>"
  is_vip       = <span style="color:#FF5913">false</span>
}
</code-block>

3\. Configure the reserved IP address.

* Specify the “type": “subnet”, “any_subnet”, “external”, or “ip_address”.

* Specify if you want to use the reserved IP address as a virtual IP (VIP) address (“is_vip = true”) or not (“is_vip = false”). For more details, refer to this article: <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address" target="_blank">Create and configure a virtual IP address</a>.

* (optional) Add “allowe_access_pairs” to assign one VIP to multiple machines. Specify the “ip_address” and “mac_address”.

* (optional) Specify the “network_id” and/or “subnet_id” to attach the IP address to a specific network or subnetwork.

* (optional) Specify the “region_id” and “region_name”.

* (optional) Specify the “project_id” and “project_name”.

4\. Save changes in the file.

5\. Run the following command from the Terraform directory to preview the expected changes:

```
terraform plan
```

If the code contains an error, the output will describe it.

6\. Run the following command to apply the changes:

```
terraform apply
```

Terraform will ask you to confirm the action. Enter “yes”.
