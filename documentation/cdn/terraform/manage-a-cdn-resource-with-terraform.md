---
title: manage-a-cdn-resource-with-terraform
displayName: Create and manage CDN resources
published: true
order: 20
toc:
   --1--Create a new CDN resource: "create-a-new-cdn-resource"
   --2--Step 1. Open the configuration file: "step-1-open-the-configuration-file"
   --2--Step 2. Create an origin group: "step-2-create-an-origin-group"
   --2--Step 3. Add a resource to an origin group: "step-3-add-a-cdn-resource-to-your-origin-group"
   --2--Step 4. Verify the configuration: "step-4-verify-the-configuration"
   --2--Step 5. Preview your changes: "step-5-preview-your-changes"
   --2--Step 6. Apply the configuration: "step-6-apply-the-configuration"
   --2--Step 7. Configure the resource in the Customer Portal: "step-7-configure-cdn-resource-in-the-customer-portal"
   --1--Configure CDN resource options: "configure-cdn-resource-options"
   --2--Step 1. Update the configuration file: "step-1-open-the-configuration-file"
   --2--Step 2. Provide required options: "step-2-provide-the-required-options-for-gcore-resources"
   --2--Step 3. Add custom values: "step-3-add-custom-values-to-the-configuration"
   --2--Step 4. Verify the updated configuration: "step-4-verify-the-updated-configuration"
   --2--Step 5. Preview the updates: "step-5-preview-the-updates"
   --2--Step 6. Apply the updates: "step-6-apply-the-updates"
pageTitle: Managing CDN Resources with Terraform | Gcore
pageDescription: A detailed guide on how to create a CDN resource and configure needed settings via Terraform.
---
# Create and manage CDN resources with Terraform

If you have already worked with Terraform, you can use the abridged instructions for managing  the Gcore CDN infrastructure: 

1\. Copy the required code from the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs" target="_blank">Resources section in the Terraform documentation</a> and paste it to the *main.tf* file. 

2\. Add your values to the code. 

3\. Run the ```terraform plan``` command — it will show what changes you are going to make to the CDN settings. 

4\. Run the ```terraform apply``` command to make changes to the CDN. 

For detailed guidelines on how to create and manage CDN resources and resource options, check out the following sections.

## Create a new CDN resource

Use the following steps to create a CDN resource and integrate it with your websites (content sources).  

### Step 1. Open the configuration file

Open the *main.tf* file where you <a href="https://gcore.com/docs/cdn/terraform/install-and-configure-terraform" target="_blank">configured the Gcore provider for Terraform</a>.

### Step 2. Create an origin group

At this step, you need to write the code that creates an origin group — the CDN resource will pull content from those origins. An origin group has three features: 

- **You choose which origin will be active and which origin will be backup**. An active origin is accessed whenever the CDN requests content. A backup origin is accessed only when active origins return 4xx or 5xx error. A group must have at least one active origin.   
- **You can enable or disable the "Use next upstream" option**. It defines the order in which the CDN will access remaining origins if the first origin returns a 4xx or 5xx error. If this option is on, the CDN will access active origins one by one, and then request backup origins. If it is off, the CDN will ignore remaining active origins and will immediately request a backup origin. 
- **You can create a group from a single origin.** It must consist of an active origin. The "Use next upstream" option should be disabled. 

To create an origin group via Terraform:

1\. Copy the following code to the *main.tf* file. Replace the information in brackets with your values, and then remove the brackets.   

  <code-block>
  resource "gcore_cdn_origingroup" "<span style="color:#FF5913">make up Terraform name of the origin group; you can use any name, it will be linked to the origin in the Terraform system</span>" {  
   name = "<span style="color:#FF5913">make up a name of the origin group that will be displayed in the Gcore Customer Portal</span>"
  </code-block>

2\. Add the appropriate strings and code snippets to the file:

 * To enable the <a href="https://gcore.com/docs/cdn/add-an-origin-group#use-next-upstream" target="_blank">Use next upstream</a> option: `use_next = true` 

 * To disable the <a href="https://gcore.com/docs/cdn/add-an-origin-group#use-next-upstream" target="_blank">Use next upstream</a> option: `use_next = false` 
  
 * To add an active origin, add the following code. Specify your website domain and remove the brackets. 

  <code-block>
  origin {          
  source  = "<span style="color:#FF5913">domain of your origin website</span>"   
  enabled = true      
  } 
  </code-block>

 * To add a backup origin, add the following code. Specify your website domain and remove the brackets. 

  <code-block>
  origin {   
   source  = "<span style="color:#FF5913">domain of your origin website</span>"   
  enabled = true   
  backup = true   
  } 
  </code-block>

 You can add up to ten origins to a CDN resource.

3\. Add another curly bracket to a new string below.  

  ```
  } 
  ```

Here is an example. Let's say you want to create an origin group with the following parameters: 

- <span style="color:#FF5913">example_terraform</span> — name of the origin group that will be displayed in Terraform
- <span style="color:#FF5913">example group</span> — the name of the origin group that will be displayed in the Gcore Customer Portal
- The **Use next upstream** option is disabled
- <span style="color:#FF5913">one.com</span> and <span style="color:#FF5913">two.com</span> — the active origins
-  <span style="color:#FF5913">three.com</span> — the backup origin

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

### Step 3. Add a CDN resource to your origin group 

At this step, you will write the code that adds a CDN resource to your origin group. Continue to add the following code to the same configuration file. 

1\. Copy the code, replace the information in brackets with your values, and then remove the brackets.   

  <code-block>
  resource "gcore_cdn_resource" "<span style="color:#FF5913">Terraform name for your resource</span>" {     
  cname               = "<span style="color:#FF5913">custom domain like cdn.[your site's domain]; for example, if your site is example.com, enter cdn.example.com</span>"   
  origin_group = gcore_cdn_origingroup.<span style="color:#FF5913">Terraform name for your origin group that will be requested for content.id</span>
  </code-block> 

2\. Add the appropriate strings and code snippets to the file:

 * To configure the CDN so that it will access an origin on a protocol of a user's request — HTTP or HTTPS: ` origin_protocol     = "MATCH"`

 * Enable CDN to use only HTTP: `origin_protocol     = "HTTP"`

 * Enable CDN to use only HTTPS: `origin_protocol     = "HTTPS"`

 * To deliver different types of content from two separate custom domains: 

  <code-block>
  secondary_hostnames = ["<span style="color:#FF5913">additional custom domain</span>"] 
  </code-block>

 *  To deliver different types of content from more than two separate custom domains: 

  <code-block>
  secondary_hostnames = ["<span style="color:#FF5913">additional custom domain 1</span>","<span style="color:#FF5913">additional custom domain 2, continue adding up to 10 domains in quotation marks and separating them by commas</span>"] 
  </code-block>

3\. At the end, add a curly bracket to a new string below.

  ```
  } 
  ```

Here is an example. Let's say you want to create a CDN resource with the following parameters: 

- <span style="color:#FF5913">cdn_example_com</span> — name of the resource that will be displayed in Terraform
- <span style="color:#FF5913">сdn.one.com</span> — custom domain of the CDN resource that will be displayed in the file paths and in the Gcore Customer Portal
- <span style="color:#FF5913">example_terraform</span> — name of the origin group that will be displayed in Terraform
- <span style="color:#FF5913">HTTPS</span> — protocol that will be used by the CDN to access an origin
- <span style="color:#FF5913">cdn.two.com</span> and <span style="color:#FF5913">cdn.three.com</span> — additional custom domains

Then the code in the configuration file will look as follows:  

<code-block>
resource "gcore_cdn_resource" "<span style="color:#FF5913">cdn_example_com</span>" {   
cname = "<span style="color:#FF5913">сdn.one.com</span>"   
origin_group = gcore_cdn_origingroup.<span style="color:#FF5913">example_terraform.id</span>   
origin_protocol = "<span style="color:#FF5913">HTTPS</span>"   
secondary_hostnames = ["<span style="color:#FF5913">cdn.two.com</span>","<span style="color:#FF5913">cdn.three.com</span>"]   
} 
</code-block>

### Step 4. Verify the configuration

At Step 2 and Step 3, you entered the code that has created an origin group and a CDN resource. Below is an example of how your code may look in your configuration file:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1706.png" alt="configuration file" width="80%">

Make sure all data is correct and save the changes.  

### Step 5. Preview your changes

Open the "Terraform" folder in command-line interface and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code in the configuration file contains an error, the output will give a brief description of it. 

### Step 6. Apply the configuration

Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

Congratulations! The origin group and CDN resource have been created! 

Now you need to configure a custom domain for the CDN resource and change the file paths so that they contain the custom domain instead of the origin domain. Use the following section for detailed instructions.

### Step 7. Configure CDN resource in the Customer Portal

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

## Configure CDN resource options 

When you create a CDN resource via Terraform, it automatically adds the following options with default values: 

- browse_cache_settings — <a href="" target="_blank">Browser Caching</a>
- cors — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers" target="_blank">CORS header support</a>
- edge_cache_settings — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin" target="_blank">CDN Caching</a>
- gzip_on — <a href="https://gcore.com/docs/cdn/cdn-resource-options/compression/configure-gzip-and-brotli-compression" target="_blank">GZip Compression</a>
- host_header — <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Change Host Header</a>
- ignore_query_string — <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers" target="_blank">Ignore Query String (Ignore All)</a>
- query_params_blacklist — Ignore Query String (Ignore All Except)
- query_params_whitelist — Ignore Query String (Ignore Only)
- redirect_http_to_https — <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/set-up-a-redirect-from-http-to-https" target="_blank">Enable HTTPS</a>
- rewrite — <a href="https://gcore.com/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin" target="_blank">Rewrite</a> (request redirection)
- sni — <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/set-the-hostname-passed-in-sni-requests-to-the-origin-server" target="_blank">Change SNI hostname</a>
- static_request_headers — <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers" target="_blank">Response headers</a>
- tls_versions — Supported TLS versions
- webp — <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif" target="_blank">WebP Compression</a>
- websockets  — <a href="https://gcore.com/docs/cdn/cdn-resource-options/websockets-allow-permanent-connections-with-the-origin" target="_blank">WebSockets</a>

We constantly add new options. The up-to-date list is always available in the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cdn_resource#optional" target="_blank">Terraform documentation for the Gcore provider</a>. 

If a CDN resource was created via Terraform, you can change its options via Terraform. To do this, use the following steps. 

### Step 1. Update the configuration file 

Open the *main.tf* file. It's supposed to contain the code for the creation of your CDN resource.   

<alert-element type="tip" title="Tip">
 
If the *main.tf* file is missing, add the code according to the [Create a new CDN resource](https://gcore.com/docs/cdn/terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section. Don't worry, Terraform won't duplicate a resource. It requires the code used for the creation of the resource only to identify a resource that should be changed. 
 
</alert-element>

Add the following string before the last curly bracket:  

```
options { 
```

### Step 2. Provide the required options for Gcore resources

Open the <a href="https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cdn_resource" target="_blank">Terraform documentation for the Gcore provider</a> and find the required option. Follow the guide from the Terraform documentation to enter the required option values. 

### Step 3. Add custom values to the configuration

Add a curly bracket to a new string below: 

```
} 
```

Here is an example. You want to set up CDN Caching and find this option in the Terraform documentation — edge_cache_settings. You need to set up CDN Caching with these settings:  

- *345600 seconds (4 days)* is the caching time for responses with 200, 206, 301, and 302 codes
- *1000 seconds* is the caching time for responses with a 403 code
- *50 seconds* is the caching time for responses with a 404 code

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

### Step 4. Verify the updated configuration

The configuration file now contains the code that creates a CDN resource with your option values. Here's an example of the file:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1707-2.png" alt="configuration file" width="80%">

Double-check and save the changes in the configuration file.

### Step 5. Preview the updates

Access the "Terraform" folder in the command-line interface and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it. 

### Step 6. Apply the updates

Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes".