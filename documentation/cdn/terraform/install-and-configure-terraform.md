---
title: install-and-configure-terraform
displayName: Install and integrate with CDN
published: true
order: 20
toc:
pageTitle: A guide on how to install Terraform and integrate it with Gcore CDN  | Gcore
pageDescription: Learn how to install and configure Terraform.
---
# Install Terraform and integrate it with Gcore CDN

The following instructions will help you set up Terraform and use it to create and manage CDN resources. 

1\. Download the appropriate Terraform package for your OS from the <a href="https://terraform.io/downloads" target="_blank">official Terraform website</a>.  

2\. Create a new folder and name it just as the downloaded package. 

3\. Unzip the Terraform archive into the new folder. 

4\. Add the directory of the unzipped Terraform archive to the `PATH` environment variable. 

5\. Create a configuration file in the Terraform folder and name it *main.tf*.  

6\. Copy the code below and paste it to the *main.tf* file.  

<code-block>
terraform {  
  required_version = ">=0.13.0"   
  required_providers {   
    gcore = {  
      source = "G-Core/gcore"  
      version = "<span style="color:#FF5913">0.3.44</span>"  
   }   
  }   
}   
provider gcore {   
permanent_api_token = "<span style="color:#FF5913">251$d33611b35f26d8</span>"  
} 
</code-block>

Where:

- <span style="color:#FF5913">0.3.44</span> is the latest version of the Terraform provider indicated on the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest" target="_blank">Terraform registry page</a>.
- <span style="color:#FF5913">251$d33611b35f26d8</span> is a permanent API token generated according to <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">Managing API tokens</a> guide.


7\. Open the command-line interface, navigate to the **Terraform** folder, and run the following command: 

```
terraform init
```

This command will install Terraform and download a set of modules to work with our CDN. The following response will appear:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1734.png" alt="response " width="80%">

This response means Terraform was successfully downloaded and installed, you can start working with it. 