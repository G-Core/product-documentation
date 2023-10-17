---
title: manage-a-cdn-resource-with-terraform
displayName: Terraform
published: true
order: 20
toc:
   --1--What is Terraform?: "what-is-terraform"
   --1--Install and configure Terraform: "install-terraform-and-integrate-it-with-our-cdn"
   --1--Manage CDN: "manage-the-cdn-infrastructure-via-terraform"
   --2--Create a CDN resource: "create-a-new-cdn-resource"
   --2--Configure options: "configure-cdn-resource-options"
   --2--Add an SSL certificate: "add-an-ssl-certificate"
   --2--Create a rule: "create-a-rule"
pageTitle: Managing CDN Resources with Terraform | Gcore
pageDescription: A detailed guide on how to create a CDN resource and configure needed settings via Terraform.
---
# Manage a CDN resource with Terraform

## What is Terraform? 

Terraform is a declarative command-line utility used to manage the infrastructure of Terraform partner providers. With this tool, you can manage our CDN service. 

To work with Terraform, you create a configuration file where you specify the changes you want to make to your CDN service — for example, to create a new CDN resource or to add an SSL certificate. Then you run the Terraform command to make changes. The utility reads the configuration file and sends necessary API requests. As a result, the required CDN settings are applied. 

## Install Terraform and integrate it with our CDN 

1\. Download the appropriate Terraform package for your OS from the <a href="https://terraform.io/downloads" target="_blank">official Terraform website</a>.  

2\. Create a new folder and name it just as the downloaded package. 

3\. Unzip the Terraform archive into the new folder. 

4\. Add the directory of the unzipped Terraform archive to the PATH environment variable. 

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
gcore_cdn_api = "https://api.gcore.com/docs/cdn"  
} 
</code-block>

Where:

- <span style="color:#FF5913">0.3.44</span> is the latest version of the Terraform provider indicated on the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest" target="_blank">page</a>;
- <span style="color:#FF5913">251$d33611b35f26d8</span> is a permanent API token generated according to <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">the guide</a>.


7\. Open the command-line interface, access the "Terraform" folder and run the command: 

```
terraform init
```

This command will install Terraform and download a set of modules to work with our CDN. The following response will appear:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1734.png" alt="response " width="80%">

This response means Terraform was successfully downloaded and installed, you can start working with it. 

## Manage the CDN infrastructure via Terraform

If you have already worked with Terraform, you can use the abridged guide on how to manage the Gcore CDN infrastructure: 

1\. Copy the required code from the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs" target="_blank">Resources section in the Terraform documentation</a> and paste it to the *main.tf* file. 

2\. Add your values to the code. 

3\. Run the ```terraform plan``` command — it will show what changes you are going to make to the CDN settings. 

4\. Run the ```terraform apply``` command to make changes to the CDN. 

You can also use our step-by-step guides below.  

### Create a new CDN resource

This guide will help you to create a CDN resource and integrate it with your websites (content sources). 

1\. Open the *main.tf* file where you configured the Gcore provider for Terraform. 

2\. At this step, you will write the code that creates an origin group — the CDN resource will pull content from those origins. An origin group has three features: 

- **You choose which origin will be active and which origin will be backup**. An active origin is accessed whenever the CDN requests content. A backup origin is accessed only when active origins return 4xx or 5xx error. A group must have at least one active origin.   
- **You can enable or disable the "Use next upstream" option**. It defines the order in which the CDN will access remaining origins if the first origin returns a 4xx or 5xx error. If this option is on, the CDN will access active origins one by one, and then request backup origins. If it is off, the CDN will ignore remaining active origins and will immediately request a backup origin. 
- **You can create a group from a single origin.** It must consist of an active origin. The "Use next upstream" option should be disabled. 

Copy the code below to the file. Replace the hints in the brackets with your values and remove the brackets.   

<code-block>
resource "gcore_cdn_origingroup" "<span style="color:#FF5913">make up Terraform name of the origin group; you can use any name, it will be linked to the origin in the Terraform system</span>" {  
 name = "<span style="color:#FF5913">make up a name of the origin group that will be displayed in the Gcore Control panel</span>"
</code-block>

If you want to enable the "Use next upstream" option, add the string below: 

```
use_next = true 
```

If you want to disable the "Use next upstream" option, add the string below: 

```
use_next = false 
```

To add an active origin, enter the code below. Specify your website domain and remove the brackets. 

<code-block>
origin {          
source  = "<span style="color:#FF5913">domain of your origin website</span>"   
enabled = true      
} 
</code-block>

To add a backup origin, enter the code below. Specify your website domain and remove the brackets. 

<code-block>
origin {   
 source  = "<span style="color:#FF5913">domain of your origin website</span>"   
 enabled = true   
 backup = true   
} 
</code-block>

Add as many origins as you need. The maximum number is ten. 

Add another curly bracket to a new string below. 

```
} 
```

Here is an example. Let's say you want to create an origin group with the following parameters: 

- <span style="color:#FF5913">example_terraform</span> — name of the origin group that will be displayed in Terraform, 
- <span style="color:#FF5913">example group</span> — the name of the origin group that will be displayed in the Gcore control panel, 
- the "Use next upstream" option is disabled, 
- <span style="color:#FF5913">one.com</span> and <span style="color:#FF5913">two.com</span> — the active origins, 
-  <span style="color:#FF5913">three.com</span> — the backup origin. 

Then the code in the configuration file will look as follows: 

<code-block>
resource "gcore_cdn_origingroup" "<span style="color:#FF5913">example_terraform</span>" {   
  name     = "<span style="color:#FF5913">example group</span>"    
  use_next = <span style="color:#FF5913">false</span>   
  origin {       
  source  = "<span style="color:#FF5913">one.com</span>"   
  enabled = true     
}   
  origin {       
  source  = "<span style="color:#FF5913">two.com</span>"   
  enabled = true     
}   
  origin {   
  source  = "<span style="color:#FF5913">three.com</span>"   
  enabled = true   
  backup  = true   
}   
} 
</code-block>

3\. At this step, you will write the code that adds a CDN resource to your origin group. Continue to enter the code below in the same configuration file. 

Copy the code below, replace the hints in the brackets with your values, and remove the brackets.   

<code-block>
resource "gcore_cdn_resource" "<span style="color:#FF5913">Terraform name for your resource</span>" {     
cname               = "<span style="color:#FF5913">custom domain like cdn.[your site's domain]; for example, if your site is example.com, enter cdn.example.com</span>"   
origin_group = gcore_cdn_origingroup.<span style="color:#FF5913">Terraform name for your origin group that will be requested for content.id</span>
</code-block> 

If you want to configure the CDN so that it will access an origin on a protocol of a user's request — HTTP or HTTPS — add the string below:   

```
origin_protocol     = "MATCH" 
```

If you want the CDN to be able to use only HTTP, add the string: 

```
origin_protocol     = "HTTP" 
```

If you want the CDN to be able to use only HTTPS, add the string: 

```
origin_protocol     = "HTTPS" 
```

If you want to deliver different types of content from two separate custom domains, add the string below: 

<code-block>
secondary_hostnames = ["<span style="color:#FF5913">additional custom domain</span>"] 
</code-block>

If you want to deliver different types of content from more than two separate custom domains, add the string below: 

<code-block>
secondary_hostnames = ["<span style="color:#FF5913">additional custom domain 1</span>","<span style="color:#FF5913">additional custom domain 2, continue adding up to 10 domains in quotation marks and separating them by commas</span>"] 
</code-block>

In the end, add a curly bracket to a new string below.

```
} 
```

Here is an example. Let's say you want to create a CDN resource with the following parameters: 

- <span style="color:#FF5913">cdn_example_com</span> — name of the resource that will be displayed in Terraform,  
- <span style="color:#FF5913">сdn.one.com</span> — custom domain of the CDN resource that will be displayed in the file paths and in the control panel,  
- <span style="color:#FF5913">example_terraform</span> — name of the origin group that will be displayed in Terraform, 
- <span style="color:#FF5913">HTTPS</span> — protocol that will be used by the CDN to access an origin,  
- <span style="color:#FF5913">cdn.two.com</span> and <span style="color:#FF5913">cdn.three.com</span> — additional custom domains.  

Then the code in the configuration file will look as follows:  

<code-block>
resource "gcore_cdn_resource" "<span style="color:#FF5913">cdn_example_com</span>" {   
cname = "<span style="color:#FF5913">сdn.one.com</span>"   
origin_group = gcore_cdn_origingroup.<span style="color:#FF5913">example_terraform.id</span>   
origin_protocol = "<span style="color:#FF5913">HTTPS</span>"   
secondary_hostnames = ["<span style="color:#FF5913">cdn.two.com</span>","<span style="color:#FF5913">cdn.three.com</span>"]   
} 
</code-block>

4\. At Step 2 and 3, you entered the code that has created an origin group and a CDN resource. Below is an example of how your code may look in your configuration file:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1706.png" alt="configuration file" width="80%">

Make sure all data is correct and save the changes.  

5\. Access the "Terraform" folder in command-line interface and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code in the configuration file contains an error, the output will give a brief description of it. 

6\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

Congratulations! The origin group and CDN resource have been created! Then the CDN resource requires configuring a custom domain and changing the file paths so that they contain the custom domain instead of the origin domain. Use the guide below. 

1\. Log in to your Gcore account, go to the "CDN" tab and click the custom domain of the resource created in Terraform.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1629.png" alt="CDN tab">

2\. On the page that opens, click "Setup guide". 

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1631.png" alt="Setup guide" width="80%">

3\. Copy the domain name such as _\*.gcdn.co._ from the sliding panel.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1633.png" alt="sliding panel." width="50%">

4\. Go to the settings of your DNS provider and create a CNAME record for the custom domain. For the value of the CNAME record, paste the value copied at the previous step.  

Here is an example. Let's say your custom domain is *cdn.example.com* and at Step 3 you copied the *cl-sdf34f.gcdn.co* domain. So, in the personal account of your DNS provider, you need to create a CNAME record for *cdn.example.com* with *cl-sdf34f.gcdn.co.* as its value. 

5\. Change the file paths so that they contain the custom domain instead of origin domain. For example, if your origin is *example.com*, and the custom domain is *cdn.example.com*, replace in the file paths *example.com* with *cdn.example.com*. If the source website is built on a CMS, you can change the file paths using special plugins you can find on the Internet. If the site is not built on a CMS, we recommend writing a script to replace domain name in the paths. 

Congratulations! The setup is complete! You have created and integrated your CDN resource.  

### Configure CDN resource options 

When you create a CDN resource via Terraform, it automatically adds the following options with default values: 

- browse_cache_settings — <a href="" target="_blank">Browser Caching</a>, 
- cors — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers" target="_blank">CORS header support</a>, 
- edge_cache_settings — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin" target="_blank">CDN Caching</a>, 
- gzip_on — <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression" target="_blank">GZip Compression</a>, 
- host_header — <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Change Host Header</a>, 
- ignore_query_string — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers" target="_blank">Ignore Query String (Ignore All)</a>, 
- query_params_blacklist — Ignore Query String (Ignore All Except), 
- query_params_whitelist — Ignore Query String (Ignore Only), 
- redirect_http_to_https — <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/set-up-a-redirect-from-http-to-https" target="_blank">Enable HTTPS</a>, 
- rewrite — <a href="https://gcore.com/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin" target="_blank">Rewrite</a> (request redirection), 
- sni — <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/set-the-hostname-passed-in-sni-requests-to-the-origin-server" target="_blank">Change SNI hostname</a>, 
- static_request_headers — <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers" target="_blank">Response headers</a>, 
- tls_versions — Supported TLS versions, 
- webp — <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif" target="_blank">WebP Compression</a>, 
- websockets  — <a href="https://gcore.com/docs/cdn/cdn-resource-options/websockets-allow-permanent-connections-with-the-origin" target="_blank">WebSockets</a>. 

We constantly add new options. The up-to-date list is always available in the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cdn_resource#optional" target="_blank">Terraform documentation for the Gcore provider</a>. 

If a CDN resource was created via Terraform, you can change its options via Terraform. To do this, use the guide below. 

1\. Open the *main.tf* file. 

2\. The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the "[Create a new CDN resource"](https://gcore.com/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used for the creation of the resource only to identify a resource that should be changed. 

3\. Add the following string before the last curly bracket:  

```
options { 
```

4\. Open the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cdn_resource" target="_blank">Terraform documentation for the Gcore provider</a> and find the required option. Follow the guide from the Terraform documentation, to enter the required option values. 

5\. Be aware to add a curly bracket to a new string below: 

```
} 
```

Here is an example. You want to set up CDN Caching and find this option in the Terraform documentation — edge_cache_settings. You need to set up CDN Caching with these settings:  

- *345600 seconds (4 days)* is the caching time for responses with 200, 206, 301, and 302 codes, 
- *1000 seconds* is the caching time for responses with a 403 code, 
- *50 seconds* is the caching time for responses with a 404 code.  

According to the guide, you need to add the necessary settings below the ```options {``` string. 

```
edge_cache_settings {    
  custom_values = {       
    "403" = "1000s"      
    "404" = "50s" 
  }    
  enabled = true   
  value = "345600s" 
  } 
```
6\. The configuration file now contains the code that creates a CDN resource with your option values. An example of the file:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1707-2.png" alt="configuration file" width="80%">

Save the changes in the configuration file.  

7\. Access the "Terraform" folder in the command-line interface and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it. 

8\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

### Add an SSL certificate 

If a CDN resource was created via Terraform, you can add an SSL certificate via Terraform. To do this, use the guide below. 

1\. Open the *main.tf* file. 

2_._ The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](https://gcore.com/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used for the creation of the resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for issuing an SSL certificate. 

Add the code below before the following string: ```resource "gcore_cdn_resource" "(name of your resource in Terraform)" {```. Replace the hints in the brackets with your values and remove the brackets. 

<code-block>
resource "gcore_cdn_sslcert" "<span style="color:#FF5913">make up Terraform name for your certificate; you can use any name, it will be linked to the certificate inside the Terraform system</span>" {   
name = "<span style="color:#FF5913">make up a certificate name that will be displayed in the Gcore control panel; it should not match the names of other SSL certificates in the same account</span>"   
cert = "<span style="color:#FF5913">specify a public key of your certificate, including the BEGIN CERTIFICATE----- and-----END CERTIFICATE---- strings</span>"   
private_key ="<span style="color:#FF5913">specify a private key of your SSL certificate, including the -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY----- string</span>"   
}
</code-block>

4\. Add the code below after the *secondary_hostnames* string, if any (if not, after *origin_protocol*). Replace the hints in the brackets with your values and remove the brackets. 

<code-block>
ssl_enabled = true   
ssl_data = gcore_cdn_sslcert.<span style="color:#FF5913">Terraform name of the certificate</span>.id 
</code-block>

Here is an example of adding a certificate. Let's suppose your values are as follows: 

- <span style="color:#FF5913">example_cert</span> — the name of the certificate that will be displayed in Terraform, 
- <span style="color:#FF5913">example_certificate</span> — the name of the certificate that will be displayed in the control panel, 
- <span style="color:#FF5913">-----BEGIN CERTIFICATE-----MIIDkjCCAnqgAwIBAgIgTfqoZeTGCEvm...T7XH8IlQY0SGq2FSZKJAlrfX+UOpIMWQcOwcuDB97DXl5Bjs+QEXO203GW0C-----END CERTIFICATE-----</span> — the public key of the certificate,
- <span style="color:#FF5913">-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAzzj54zBOWxBIJRFMBtG...xyf2T9RZYRpIVbkatg977nXryEZC8Sp8U76c3Oww==-----END RSA PRIVATE KEY-----</span> — the private key of the certificate.

To add such a certificate, you have inserted the necessary strings into the configuration file. The file is supposed to look as follows:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1709-2.png" alt="configuration file" width="80%">

5\. Save the changes in the configuration file. 

6\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

7\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

### Create a rule 

If a CDN resource was created via Terraform, you can <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files" target="_blank">add a rule</a> to it via Terraform. To do this, use the guide below.  

1\. Open the *main.tf* file. 

2\. The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](https://gcore.com/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used to create a resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for creating a rule to the configuration file. 

Add the code below to a new string. Replace the hints in the brackets with your values and remove the brackets.  

<code-block>
resource "gcore_cdn_rule" "<span style="color:#FF5913">make up Terraform name for the rule; you can use any name, it will be linked to the rule inside the Terraform system</span>" {   
  resource_id = gcore_cdn_resource.<span style="color:#FF5913">Terraform name of the CDN resource for which you are adding the rule</span>.id   
  name = "<span style="color:#FF5913">make up a name for the rule that will be displayed in the Gcore control panel</span>"   
  rule = "<span style="color:#FF5913">specify path to the files for which you are adding the rule; the path should always start with "^/" or "/"</span>"   
  rule_type   = 0 
</code-block>

4\. If you want to add options to the rule, paste the code below. Replace the hints in the brackets with your values and remove the brackets. 

<code-block>
options {   
<span style="color:#FF5913">code to configure the necessary options; for set-up guides, refer to the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cdn_rule#nested-schema-for-options" target="_blank">Terraform documentation for the Gcore provider</a>, an example of configuration can be found in the "Configure CDN resource options" section</span>   
} 
</code-block>

If you don't need options, do not add the _options_ code segment. 

5\. Be aware to add a curly bracket to a new string below. 

```
} 
```

Here is an example of a configuration file. Let's say you want to add a rule with the following characteristics: 

- <span style="color:#FF5913">example_rule</span> — the name of the rule for Terraform, 
- <span style="color:#FF5913">cdn_example_com</span> — the name of the CDN resource in Terraform,  
- <span style="color:#FF5913">PNG images</span> — the name of the rule for the Control panel. 
- <span style="color:#FF5913">/folder/images/*.png</span> — the path to the files. 
- The "WebP Compression" option with a final quality of 66 is required. 

The final code in the configuration file will look as follows:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1712-2.png" alt="configuration file" width="80%">

6\. Save the changes in the configuration file. 

7\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

8\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes".
