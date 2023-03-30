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
---
  
  
  
  
  
  
  
  
  
  
  
  

What is Terraform?
------------------

Terraform is a declarative command-line utility used to manage the infrastructure of Terraform partner providers. With this tool, you can manage our Cloud service.

To work with Terraform, you create a configuration file where you specify the changes you want to make to your Cloud resources, for example, to create an instance or a Kubernetes cluster. Then you run the Terraform command to make changes. The utility reads the configuration file and sends the necessary API requests. The required Cloud settings are then applied.

Install Terraform and integrate it with our Cloud
-------------------------------------------------

1. Download a Terraform package suitable for your OS from the [official Terraform website](https://www.terraform.io/downloads).

2. Create a new folder and name it the same as the downloaded package.

3. Unzip the Terraform archive in the new folder.

4. Add the directory of the unzipped Terraform archive to the PATH environment variable.

5. Create a configuration file in the Terraform folder and name it **main.tf**.

6. Find out the latest version of the Terraform provider on [the page](https://registry.terraform.io/providers/G-Core/gcorelabs/latest) and generate a permanent API token using [the guide](https://gcore.com/support/articles/360018625617/), if you don’t have one yet.

7. Add the following code to main.tf:

terraform {
  required\_version = ">=0.13.0"
  required\_providers {
    gcore = {
      source = "G-Core/gcore"
      version = "**0.3.55**"
   }
  }
}
provider gcore {
  permanent\_api\_token = "**123$61b8e1e7a68c**"
}

Enter your values instead:

**0.3.55**—the Terraform provider version  
**123$61b8e1e7a68c**—the permanent API token

8. Open the command line, access the Terraform folder and run the following command:

terraform init

You’ll get the output:

<img src="https://support.gcore.com/hc/article_attachments/12966689446417" alt="1.png" width="700" height="360">

This means Terraform has been successfully downloaded and installed, and you can start working with it.

Manage Cloud resources via Terraform
------------------------------------

If you have already worked with Terraform, you can use this abridged guide on how to manage Gcore Cloud resources:

1. Go to the Terraform documentation, click **Resources**, and copy the necessary code to main.tf.

2. Customize values in the code.

3. Run the following command to preview the expected changes:

terraform plan

4. Run the following command to apply these changes:

terraform apply

You can also use our step-by-step guides below.

### Create a bare metal server

1. Open the **main.tf** file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_baremetal" "**bm**" {
  name       = "**baremetal\_example**"
  flavor\_id  = "**bm1-infrastructure-small**"

  interface {
      type = "**external**"
              **is\_parent = "true"**
}

3\. Configure your bare metal server.

1) Specify “flavor\_id”.

2) Configure “interface”.

*   Select the interface “type”: “external”, “subnet”, “any\_subnet”, or “reserved\_fixed\_ip”.  
      
    If you select "subnet", specify the “network\_ID” and “subnetwork\_ID”.  
    If you select "anu\_subnet", specify the “network\_ID”.  
    If you select “reserved\_fixed\_ip”, specify the “port\_id”.

*   (optional) Add “**is\_parent = "true"**” to ensure the interface cannot be detached and is always connected first.
*   (optional) Specify “order” to set the order in which interfaces will be attached.

3) (optional) Specify “app\_config” to set parameters for the application template from the marketplace.

4) (optional) Specify the “image\_id” or “apptemplate\_id”.

5) (optional) Specify the “keypair\_name”.

6) (optional) Specify the “name” of the server.

7) (optional) Specify the “region\_id” and “region\_name”.

8) (optional) Specify the “project\_id” and “project\_name”.

9) (optional) Specify the “metadata\_map”: “key” and “value”.

10) (optional) Specify “username” and/or “password”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the changes:

terraform plan

If the code contains an error, the output will show it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create an instance

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "2**51$d3361.............1b35f26d8**"
}  
resource "gcore\_reservedfixedip" "**fixed\_ip**" {
  type             = "ip\_address"
  network\_id       = "**faf6507b-1ff1-4ebf-b540-befd5c09fe06**"
  fixed\_ip\_address = "**192.168.13.6**"
  is\_vip           = **false**
}

resource "gcore\_volume" "first\_volume" {
  name       = "**boot volume**"
  type\_name  = "**ssd\_hiiops**"
  size       = **10**
  image\_id   = "**6dc4e061-6fab-41f3-91a3-0ba848fb32d9**"
}

resource "gcore\_floatingip" "**fip**" {
  fixed\_ip\_address = **gcore\_reservedfixedip.fixed\_ip.fixed\_ip\_address**
  port\_id          = **gcore\_reservedfixedip.fixed\_ip.port\_id**
}

resource "gcore\_instance" "**v**" {
  name       = "**hello**"
  flavor\_id  = "**g1-standard-1-2**"

  volume {
    source     = "existing-volume"
    volume\_id  = **gcore\_volume.first\_volume.id**
    boot\_index = **0**
  }

  interface {
    type            = "**reserved\_fixed\_ip**"
    port\_id         = **gcore\_reservedfixedip.fixed\_ip.port\_id**
    fip\_source      = "**existing**"
    existing\_fip\_id = **gcore\_floatingip.fip.id**
    security\_groups = **\["ada84751-fcca-4491-9249-2dfceb321616"\]**
  }
}

3. Configure resources required for the instance: [a reserved IP address](#reserve-an-ip-address), [network](#create-a-network-and-subnetwork), [subnetwork](#create-a-network-and-subnetwork), [volume](#create-a-volume).

4. Configure the instance.

1) Specify “flavor\_id”.

2) Configure “interface”.

*   Select the interface “type”: “external”, “subnet”, “any\_subnet”, or “reserved\_fixed\_ip”.  
      
    If you select "subnet", specify the “network\_ID” and “subnetwork\_ID”.  
    If you select "anu\_subnet", specify the “network\_ID”.  
    If you select “reserved\_fixed\_ip”, specify the “port\_id”.
*   (optional) Add “**is\_parent = “true”**” to ensure the interface cannot be detached and is always connected first.
*   (optional) Specify “order” to set the order in which interfaces will be attached.

3) Configure “volume”.

*   Specify “source = “existing-volume” and the "volume\_id". Optionally, you can specify the “size” of the existing volume in GB.
*   (optional) Specify the “boot\_index”. If “boot\_index = 0”, the volume cannot be detached.
*   (optional) Specify the “type\_name”: “standard”, “ssd\_hiiops”, “cold”, or “ultra”.

4) (optional) Add “allow\_app\_ports = true” to allow application ports for instances created from marketplace templates.

5) (optional) Specify “configuration” to set parameters for the application template from the marketplace: “key” and “value”.

6) (optional) Specify the “keypair\_name”.

7) (optional) Specify the “metadata\_map”: “key” and “value”.

8) (optional) Specify the “name” of the instance.

9) (optional) Specify “username” and “password”.

10) (optional) Specify the “region\_id” and “region\_name”.

11) (optional) Specify the “project\_id” and “project\_name”.

12) (optional) Specify the “security\_group” to add firewalls.

5. Save changes in the file.

6. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will describe it.

7. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a Kubernetes cluster

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_k8s" "v" {
  name          = "**kluster\_example**"
  fixed\_network = "**6bf878c1-1ce4-47c3-a39b-6b5f1d79bf25**"
  fixed\_subnet  = "**dc3a3ea9-86ae-47ad-a8e8-79df0ce04839**"
  pool {
    name               = "**pool\_example**"
    flavor\_id          = "**g1-standard-1-2**"
    min\_node\_count     = **1**
    max\_node\_count     = **2**
    node\_count         = **1**
    docker\_volume\_size = **2**
  }
}

3. Configure the cluster.

1) Specify “name”.

2) Specify the “fixed\_network” of the cluster.

3) Specify the “fixed\_subnet” and make sure the subnet has a router.

4) Specify the “keypair”.

5) (optional) Specify the “region\_id” and “region\_name”.

6) (optional) Specify the “project\_id” and “project\_name”.

7) (optional) Add “auto\_healing\_enabled = “true”” to allow automatic recovery of failed nodes.

8) (optional) Add “external\_dns\_enabled = “true”” if you want to enable external DNS.

9) Configure the pool, a set of cluster nodes with the same specifications.

*   Specify “name”.
*   Specify “flavor\_id”.
*   Specify the “min\_node\_count” for autoscaling.
*   Specify the “max\_node\_count” for autoscaling.
*   Specify the “node\_count”. This is the initial number of nodes to be deployed.
*   (optional) Specify the “docker\_volume\_size” in GB.
*   (optional) Select “docker\_volume\_type”: “standard”, “ssd\_hiiops”, “cold”, or “ultra”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a Kubernetes pool

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_k8s\_pool" "**v**" {
  cluster\_id         = "**6bf878c1-1ce4-47c3-a39b-6b5f1d79bf25**"
  name               = "**pool\_example**"
  flavor\_id          = "**g1-standard-1-2**"
  min\_node\_count     = **1**
  max\_node\_count     = **2**
  node\_count         = **1**
  docker\_volume\_size = **2**
}

3. Configure the pool.

1) Specify the “cluster\_id” within which you want to create the pool.

2) Specify the “name” of your pool.

3) Specify “flavor\_id”.

4) Specify the “min\_node\_count” for autoscaling.

5) Specify the “max\_node\_count” for autoscaling.

6) Specify the “node\_count”. This is the initial number of nodes to be deployed.

7) (optional) Specify the “docker\_volume\_size” in GB.

8) (optional) Select “docker\_volume\_type”: “standard”, “ssd\_hiiops”, “cold”, or “ultra”.

9) (optional) Specify the “region\_id” and “region\_name”.

10) (optional) Specify the “project\_id” and “project\_name”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a load balancer

This section explains how to create a load balancer with a pool, listener, and member.

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_loadbalancerv2" "**lb**" {
  **project\_id = 1**
  **region\_id  = 1**
  name       = "**lb\_example**"
  flavor     = "**lb1-1-2**"
}

resource "gcore\_lblistener" "**listener**" {
  name            = "**listener\_example**"
  protocol        = "**TCP**"
  protocol\_port   = **36621**
  loadbalancer\_id = **gcore\_loadbalancerv2.lb.id**
}

resource "gcore\_lbpool" "**pl**" {
  name            = "**test\_pool**"
  protocol        = "**HTTP**"
  lb\_algorithm    = "**LEAST\_CONNECTIONS**"
  loadbalancer\_id = **gcore\_loadbalancer.lb.id**
  listener\_id     = **gcore\_loadbalancer.lb.listener.0.id**
  **health\_monitor {
    type        = "PING"
    delay       = 60
    max\_retries = 5
    timeout     = 10
  }
  session\_persistence {
    type        = "APP\_COOKIE"
    cookie\_name = "test\_new\_cookie"
  }**
}

resource "gcore\_lbmember" "lbm" {
  pool\_id       = **gcore\_lbpool.pl.id**
  address       = "**10.10.2.15**"
  protocol\_port = **8081**
  **weight        = 5**
}

3. Configure the load balancer.

1) Specify the “name” of your load balancer.

2) Specify “flavor”.

3) (optional) Specify the “region\_id” and “region\_name”.

4) (optional) Specify the “project\_id” and “project\_name”.

5) (optional) Specify the “vip\_port\_id” or “vip\_network\_id”.

6) (optional) Specify the “vip\_subnet\_id”.

4. Configure the listener.

1) Specify “name”.

2) Select “protocol”: “HTTP”, “HTTPS”, “TCP”, “UDP”, or “TERMINATED\_HTTPS”. If you select “TERMINATED\_HTTPS”, specify the “secret\_id”.

3) Specify the “protocol\_port”.

4) Specify the “loadbalancer\_id”.

5) (optional) Add “insert\_x\_forward = “true”” to identify an original IP address of a client connecting to a web server via a load

6) (optional) Specify the “region\_id” and “region\_name”.

7) (optional) Specify the “project\_id” and “project\_name”.

5. Configure the pool.

1) Specify “name”.

2) Select “protocol”: “HTTP”, “HTTPS”, “TCP”, or “UDP”.

3) Select “lb\_algorithm”: “ROUND\_ROBIN”, “LEAST\_CONNECTIONS”, “SOURCE\_IP”, or  “SOURCE\_IP\_PORT”.

4) (optional) Add “health\_monitor”.

*   Select “type”: “HTTP”, “HTTPS”, “PING”, “TCP”, “TLS-HELLO”, or “UPD-CONNECT”.
*   Specify the “delay” in seconds to set the time between sending probe requests to pool members.
*   Specify the “max\_tertires” to set the number of successful probes required to switch a member to the ONLINE state.
*   Specify the “timeout” in seconds to set the maximum time to connect.
*   (optional) Select “http\_method”: “CONNECT”, “DELETE”, “GET”, “HEAD”, “OPTIONS”, “PATCH”, “POST”, “PUT”, or “TRACE”.
*   (optional) Specify the “max\_retrieve\_down” to set the threshold of failures required to switch a member to the ERROR state.
*   (optional) Specify “expected\_codes”
*   (optional) Specify the “url\_path”

5) (optional) Specify the “listener\_id”.

6) (optional) Specify the “loadbalancer\_id”.

7) (optional) Specify the “region\_id” and “region\_name”.

8) (optional) Specify the “project\_id” and “project\_name”.

9) (optional) Add “session\_persistence”.

*   Select “type”: “APP\_COOKIE”, “HTTP\_COOKIE”  
    If you select “APP\_COOKIE” or “HTTP\_COOKIE”, specify the “cookie\_name”.  
    If you select “SOURCE\_IP”, specify the “persistence\_granularity” (for UDP ports only).
*   (optional) Specify the “persistence\_timeout”.

6. Configure the member.

1) Specify the IP “address”.

2) Specify the “pool\_id”.

3) Specify the “protocol\_port”.

4) Specify the “instance\_id” or “subnet\_id”.

5) (optional) Specify member “weight” from 0 to 256.

7. Save changes in the file.

8. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

9. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a network and subnetwork

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_network" "**network**" {
  name       = "**network\_example**"
  **mtu        = 1450
  type       = "vlan"**
}

3. Configure the network.

1) Specify “name”.

2) (optional) Add “create\_router = “false”” to remove the external router from the network. Otherwise, the external router will be added by default.

3) (optional) Add “type = “vlan””. Otherwise, a “vxlan” network will be created by default.

4) (optional) Specify the “region\_id” and “region\_name”.

5) (optional) Specify the “project\_id” and “project\_name”.

4. If you don’t need a subnetwork, skip to Step 6. To create a subnetwork, add the code below and customize the highlighted values:

resource "gcore\_subnet" "**subnet**" {
  name            = "**subnet\_example**"
  cidr            = "**192.168.10.0/24**"
  network\_id      = **gcore\_network.network.id**
}

5. Configure the subnetwork.

1) Specify the “name” of the subnetwork.

2) Specify the “cidr”.  

*   Select the IP address from the ranges: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, and 192.168.0.0–192.168.255.255.
*   Select the subnet mask from 16 to 24.

3) Specify the “network\_id” within which you want to create the subnet.

4) (optional) Add “connect\_to\_network\_router = “true”” if you want your subnetwork to be accessible for public networks through an external router. If not, add “connect\_to\_network\_router = “false””. The default value is “true”.

5) (optional) Add the “gateway\_ip” of an external router, if any.

6) (optional) Specify “dns\_nameservers”.

7) (optional) Add “host\_routes”.

*   Specify the “destination”, the CIDR of the target subnetwork.
*   Specify the “nexthop”, the IPv4 address to forward traffic to if its destination IP matches the “destination” CIDR.

8) (optional) Add “enable\_dhcp = false” to disable DHCP. Otherwise, DHCP will be enabled by default.

9) (optional) Specify the “region\_id” and “region\_name”.

10) (optional) Specify the “project\_id” and “project\_name”.

6. Save changes in the file.

7. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

8. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a server group

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_servergroup" "**default**" {
  name       = "**server\_group\_example**"
  policy     = "**affinity**"
  region\_id  = **1**
  project\_id = **1**
}

3. Configure the server group.

1) Specify “name”.

2) Select the “policy”: use “**affinity**” to run your servers on one physical server or “**anti-affinity**” to run your servers on different physical servers.

3) (optional) Specify the “region\_id” and “region\_name”.

4) (optional) Specify the “project\_id” and “project\_name”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a snapshot

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_snapshot" "**snapshot**" {
  project\_id  = **1**
  region\_id   = **1**
  name        = "**snapshot\_example**"
  volume\_id   = "**28e9edcb-1593-41fe-971b-da729c6ec301**"
}

3. Configure the snapshot.

1) Specify “name”.

2) Specify the “volume\_id”.

3) (optional) Add a “description”.

4) (optional) Specify the “region\_id” and “region\_name”.

5) (optional) Specify the “project\_id” and “project\_name”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will describe it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Create a volume

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_volume" "**volume**" {
  name       = "**volume\_example**"
  type\_name  = "**standard**"
  size       = **1**
}

3. Configure the volume.

1) Specify “name”.

2) Specify the “snapshot\_id” or “image\_id”.

3) (optional) Specify the “size” of your volume in GB.

4) (optional) Select the “type\_name”: “standard”, “ssd\_hiiops”, “cold”, or “ultra”.

5) (optional) Specify the “region\_id” and “region\_name”.

6) (optional) Specify the “project\_id” and “project\_name”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will show it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.

### Reserve an IP address

1. Open the main.tf file where you configured the Gcore provider for Terraform.

2. Copy the code below to the file and customize the highlighted values:

provider gcore {
  permanent\_api\_token = "**251$d3361.............1b35f26d8**"
}

resource "gcore\_reservedfixedip" "**fixed\_ip**" {
  project\_id = **1**
  region\_id  = **1**
  type       = "**external**"
  is\_vip     = **false**
}

3. Configure the reserved IP address.

1) Specify the “type": “subnet”, “any\_subnet”, “external”, or “ip\_address”.

2) Specify if you want to use the reserved IP address as a virtual IP (VIP) address (“is\_vip = true”) or not (“is\_vip = false”). For more details, refer to this article: [Virtual IP (VIP): what it is, how to get it and assign to instance](https://gcore.com/support/articles/4405866963345/).

3) (optional) Add “allowed\_access\_pairs” to assign one VIP to multiple machines. Specify the “ip\_address” and “mac\_address”.

4) (optional) Specify the “network\_id” and/or “subnet\_id” to attach the IP address to a specific network or subnetwork.

5) (optional) Specify the “region\_id” and “region\_name”.

6) (optional) Specify the “project\_id” and “project\_name”.

4. Save changes in the file.

5. Run the following command from the Terraform directory to preview the expected changes:

terraform plan

If the code contains an error, the output will describe it.

6. Run the following command to apply the changes:

terraform apply

Terraform will ask you to confirm the action. Enter “yes”.