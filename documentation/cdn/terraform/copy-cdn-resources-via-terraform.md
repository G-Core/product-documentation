---
title: copy-cdn-resources-via-terraform
displayName: Copy CDN resources
published: true
order: 30
toc:
pageTitle: A guide on how to copy a CDN resource via Terraform | Gcore
pageDescription: Learn how to use Terraform to copy an existing CDN resource.
---
# Copy CDN resources via Terraform 

Terraform simplifies the duplication of CDN configurations across environments, ensuring consistency and reliability. By managing environment-specific variables and using workspaces, you can maintain identical setups across your staging and production environments.

<alert-element type="tip" title="Tip">
 
To proceed with the following steps, you need to have <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token#create-a-permanent-api-token" target="_blank">API keys</a> configured. 
 
</alert-element>

## Step 1: Define variables

One of the key benefits of Terraform is its ability to manage configurations through variables, making it easier to handle environment-specific settings. 

Create a *variables.tf* file to define parameters that change between environments, such as API URL, token, or CDN resource names. 

<code-block>

// variables.tf
 
variable "api_token" {
  description = "API token for access to your Gcore account"
  type        = string
  sensitive   = true
}
 
variable "api_endpoint" {
  description = "Gcore API url"
  type        = string
}
 
variable "cdn_resource_cname" {
  description = "Name of the CDN resource"
  type        = string
}

</code-block>

## Step 2: Configure environment variables 

Create **.tfvars* file for each environment to set the variable values. For example, for preproduction:

<code-block>

// preprod.tfvars
 
api_token          = "your-preprod-api-token"
api_endpoint       = "https://api.preprod.world"
cdn_resource_cname = "preprod.example.com"

</code-block>

And for production:

<code-block>

// production.tfvars
 
api_token          = "your-production-api-token"
api_endpoint       = "https://api.gcore.com"
cdn_resource_cname = "prod.example.com"

</code-block>

## Step 3: Write configurarion for copying resources 

Add the following Terraform configuration to the *main.tf*:

<code-block>

// main.tf
 
terraform {
  required_providers {
    gcore = {
      source  = "G-Core/gcore"
      version = ">= 0.8.20"
    }
  }
}
 
provider "gcore" {
  permanent_api_token = var.api_token
  api_endpoint = var.api_endpoint
}
 
 
resource "gcore_cdn_resource" "example" {
  cname  = var.cdn_resource_cname
  origin = "example.com"
}

</code-block>

## Step 4: Use Terraform workspaces

Terraform workspaces allow you to manage multiple environments using the same configuration. 

Initialize Terraform and create workspaces for preproduction and production: 

<code-block>

terraform init
 
terraform workspace new preprod
terraform workspace new production

</code-block>

## Step 5: Apply the configuration 

Switch to the staging workspace and apply the configuration:

<code-block>

terraform workspace select staging
terraform apply -var-file=preprod.tfvars

</code-block>

Then switch to the production workspace and apply the configuration there as well: 

<code-block>

terraform workspace select production
terraform apply -var-file=production.tfvars

</code-block>

By using Terraform workspaces and variable files, you can apply the same configuration to different environments with a few commands.