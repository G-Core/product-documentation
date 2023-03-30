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
---
   
   
       
        •    
        •    
        •  
        •  

What is Terraform? 
-------------------

Terraform is a declarative command-line utility used to manage the infrastructure of Terraform partner providers. With this tool, you can manage our CDN service. 

To work with Terraform, you create a configuration file where you specify the changes you want to make to your CDN service — for example, to create a new CDN resource or to add an SSL certificate. Then you run the Terraform command to make changes. The utility reads the configuration file and sends necessary API requests. As a result, the required CDN settings are applied. 

Install Terraform and integrate it with our CDN 
------------------------------------------------

1\. Download the appropriate Terraform package for your OS from the [official Terraform website](https://www.terraform.io/downloads).  

2\. Create a new folder and name it just as the downloaded package. 

3\. Unzip the Terraform archive into the new folder. 

4\. Add the directory of the unzipped Terraform archive to the PATH environment variable. 

5\. Create a configuration file in the Terraform folder and name it _main.tf_.  

6\. Copy the code below and paste it to the _main.tf_ file.  

terraform {  
  required\_version = ">=0.13.0"   
  required\_providers {   
    gcore = {  
      source = "G-Core/gcore"  
      version = "**(the latest version of the Terraform provider indicated on [the page](https://registry.terraform.io/providers/G-Core/gcorelabs/latest))**"  
   }   
  }   
}   
provider gcore {   
permanent\_api\_token = "**(permanent API token generated according to [the guide](https://www.gcore.com/support/articles/360018625617/))**" gcore\_cdn\_api = " [https://api.gcore.com](https://api.gcorelabs.com/)"  
} 

  
7\. Replace the hints in brackets with your values and remove the brackets. This is how you will integrate Terraform with our CDN. 

For example, your values:  

*   _0.3.44_ is the latest version of Gcore provider in Terraform,
*   _$251d33611b35f26d8_ is the permanent API token. 

 Then the code in the file will look as follows: 

terraform {   
  required\_version = ">=0.13.0"    
  required\_providers {    
    gcore = {   
      source = "G-Core/gcore"   
      version = "0.3.44"    
   }   
  }   
}   
provider gcore {   
permanent\_api\_token = "251$d33611b35f26d8"    
gcore\_cdn\_api = "[https://apidocs.gcore.com/cdn](https://api.gcorelabs.com/)"   
} 

8\. Open the command-line interface, access the "Terraform" folder and run the command: 

 terraform init

This command will install Terraform and download a set of modules to work with our CDN. The following response will appear:

<img src="https://support.gcore.com/hc/article_attachments/7049757339537/image_1734.png" alt="image_1734.png">

This response means Terraform was successfully downloaded and installed, you can start working with it. 

Manage the CDN infrastructure via Terraform
-------------------------------------------

If you have already worked with Terraform, you can use the abridged guide on how to manage the Gcore CDN infrastructure: 

1\. Copy the required code from the [Resources section in the Terraform documentation](https://registry.terraform.io/providers/G-Core/gcorelabs/latest/docs) and paste it to the _main.tf_ file. 

2\. Add your values to the code. 

3\. Run the _terraform plan_ command — it will show what changes you are going to make to the CDN settings. 

4\. Run the _terraform apply_ command to make changes to the CDN. 

You can also use our step-by-step guides below.  

### Create a new CDN resource

This guide will help you to create a CDN resource and integrate it with your websites (content sources). 

1\. Open the _main.tf_ file where you configured the Gcore provider for Terraform. 

2\. At this step, you will write the code that creates an origin group — the CDN resource will pull content from those origins. An origin group has three features: 

*   **You choose which origin will be active and which origin will be backup**. An active origin is accessed whenever the CDN requests content. A backup origin is accessed only when active origins return 4xx or 5xx error. A group must have at least one active origin.   
*   **You can enable or disable the "Use next upstream" option**. It defines the order in which the CDN will access remaining origins if the first origin returns a 4xx or 5xx error. If this option is on, the CDN will access active origins one by one, and then request backup origins. If it is off, the CDN will ignore remaining active origins and will immediately request a backup origin. 
*   **You can create a group from a single origin.** It must consist of an active origin. The "Use next upstream" option should be disabled. 

Copy the code below to the file. Replace the hints in the brackets with your values and remove the brackets.   

resource "gcore\_cdn\_origingroup" "**(make up Terraform name of the origin group; you can use any name, it will be linked to the origin in the Terraform system)**" {  
 name = "**(make up a name of the origin group that will be displayed in the Gcore control panel)**"

If you want to enable the "Use next upstream" option, add the string below: 

use\_next = true 

If you want to disable the "Use next upstream" option, add the string below: 

use\_next = false 

To add an active origin, enter the code below. Specify your website domain and remove the brackets. 

origin {          
source  = "**(domain of your origin website)"**   
enabled = true      
} 

To add a backup origin, enter the code below. Specify your website domain and remove the brackets. 

origin {   
 source  = "**(domain of your origin website)"**   
 enabled = true   
 backup = true   
} 

Add as many origins as you need. The maximum number is ten. 

Add another curly bracket to a new string below. 

} 

Here is an example. Let's say you want to create an origin group with the following parameters: 

*   _example\_terraform_ — name of the origin group that will be displayed in Terraform, 
*   _example group_ — the name of the origin group that will be displayed in the Gcore control panel, 
*   the "Use next upstream" option is disabled, 
*   _one.com_ and _two.com_ — the active origins, 
*   _three.com_ — the backup origin. 

Then the code in the configuration file will look as follows: 

resource "gcore\_cdn\_origingroup" "example\_terraform" {   
  name     = "example group"    
  use\_next = false   
  origin {       
  source  = "one.com"   
  enabled = true     
}   
  origin {       
  source  = "two.com"   
  enabled = true     
}   
  origin {   
  source  = "three.com"   
  enabled = true   
  backup  = true   
}   
} 

3\. At this step, you will write the code that adds a CDN resource to your origin group. Continue to enter the code below in the same configuration file. 

Copy the code below, replace the hints in the brackets with your values, and remove the brackets.   

resource "gcore\_cdn\_resource" "**(Terraform name for your resource)**" {     
cname               = "**(custom domain like cdn.\[your site's domain\]; for example, if your site is example.com, enter cdn.example.com)**"   
origin\_group = gcore\_cdn\_origingroup.**(Terraform name for your origin group that will be requested for content)**.id 

If you want to configure the CDN so that it will access an origin on a protocol of a user's request — HTTP or HTTPS — add the string below:   

origin\_protocol     = "MATCH" 

If you want the CDN to be able to use only HTTP, add the string: 

origin\_protocol     = "HTTP" 

If you want the CDN to be able to use only HTTPS, add the string: 

origin\_protocol     = "HTTPS" 

If you want to deliver different types of content from two separate custom domains, add the string below: 

secondary\_hostnames = \["(**additional custom domain)**"\] 

If you want to deliver different types of content from more than two separate custom domains, add the string below: 

secondary\_hostnames = \["(**additional custom domain 1)**","**(additional custom domain 2, continue adding up to 10 domains in quotation marks and separating them by commas)**"\] 

In the end, add a curly bracket to a new string below.

} 

Here is an example. Let's say you want to create a CDN resource with the following parameters: 

*   _cdn\_example\_com_ — name of the resource that will be displayed in Terraform,  
*   _сdn.one.com_ — custom domain of the CDN resource that will be displayed in the file paths and in the control panel,  
*   _example\_terraform_ — name of the origin group that will be displayed in Terraform, 
*   _HTTPS_ — protocol that will be used by the CDN to access an origin,  
*   _cdn.two.com_ and _cdn.three.com_ — additional custom domains.  

Then the code in the configuration file will look as follows:  

resource "gcore\_cdn\_resource" "cdn\_example\_com" {   
cname = "сdn.one.com"   
origin\_group = gcore\_cdn\_origingroup.example\_terraform.id   
origin\_protocol = "HTTPS"   
secondary\_hostnames = \["cdn.two.com ","cdn.three.com"\]   
} 

4\. At Step 2 and 3, you entered the code that has created an origin group and a CDN resource. Below is an example of how your code may look in your configuration file:

<img src="https://support.gcore.com/hc/article_attachments/7046920387345/image_1706.png" alt="image_1706.png">

Make sure all data is correct and save the changes.  

5\. Access the "Terraform" folder in command-line interface and run the _terraform plan_ command — it will show what changes Terraform is going to make. If the code in the configuration file contains an error, the output will give a brief description of it. 

6\. Run the _terraform apply_ command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

Congratulations! The origin group and CDN resource have been created! Then the CDN resource requires configuring a custom domain and changing the file paths so that they contain the custom domain instead of the origin domain. Use the guide below. 

1\. Log in to your Gcore account, go to the "CDN" tab and click the custom domain of the resource created in Terraform.

<img src="https://support.gcore.com/hc/article_attachments/7047885775889/image_1629.png" alt="image_1629.png">

2\. On the page that opens, click "Setup guide". 

<img src="https://support.gcore.com/hc/article_attachments/7047928183313/image_1631.png" alt="image_1631.png">

3\. Copy the domain name such as _\*.gcdn.co._ from the sliding panel.

<img src="https://support.gcore.com/hc/article_attachments/7047935415441/image_1633.png" alt="image_1633.png">

4\. Go to the settings of your DNS provider and create a CNAME record for the custom domain. For the value of the CNAME record, paste the value copied at the previous step.  

Here is an example. Let's say your custom domain is _cdn.example.com_ and at Step 3 you copied the _cl-sdf34f.gcdn.co_ domain. So, in the personal account of your DNS provider, you need to create a CNAME record for _cdn.example.com_ with _cl-sdf34f.gcdn.co._ as its value. 

5\. Change the file paths so that they contain the custom domain instead of origin domain. For example, if your origin is _example.com_, and the custom domain is _cdn.example.com_, replace in the file paths _example.com_ with _cdn.example.com._ If the source website is built on a CMS, you can change the file paths using special plugins you can find on the Internet. If the site is not built on a CMS, we recommend writing a script to replace domain name in the paths. 

Congratulations! The setup is complete! You have created and integrated your CDN resource.  

### Configure CDN resource options 

When you create a CDN resource via Terraform, it automatically adds the following options with default values: 

*   browser\_cache\_settings — [Browser Caching](https://www.gcore.com/support/articles/360003527817/), 
*   cors — [CORS header support](https://www.gcore.com/support/articles/115004862185/), 
*   edge\_cache\_settings — [CDN Caching](https://www.gcore.com/support/articles/360003525737/), 
*   gzip\_on — [GZip Compression](https://www.gcore.com/support/articles/360006563858/), 
*   host\_header — [Change Host Header](https://www.gcore.com/support/articles/360003612697/), 
*   ignore\_query\_string — [Ignore Query String (Ignore All)](https://www.gcore.com/support/articles/115002223049/), 
*   query\_params\_blacklist — Ignore Query String (Ignore All Except), 
*   query\_params\_whitelist — Ignore Query String (Ignore Only), 
*   redirect\_http\_to\_https — [Enable HTTPS](https://www.gcore.com/support/articles/360001893317/), 
*   rewrite — [Rewrite (request redirection)](https://www.gcore.com/support/articles/115005353949/), 
*   sni — [Change SNI hostname](https://www.gcore.com/support/articles/360017569777/), 
*   static\_request\_headers — [Response headers](https://www.gcore.com/support/articles/115002515005/), 
*   tls\_versions — Supported TLS versions, 
*   webp — [WebP Compression](https://www.gcore.com/support/articles/4417800051729/), 
*   websockets  — [WebSockets](https://www.gcore.com/support/articles/4411311465873/). 

We constantly add new options. The up-to-date list is always available in the [Terraform documentation for the Gcore provider](https://registry.terraform.io/providers/G-Core/gcorelabs/latest/docs/resources/gcore_cdn_resource%23optional). 

If a CDN resource was created via Terraform, you can change its options via Terraform. To do this, use the guide below. 

1\. Open the _main.tf_ file. 

2\. The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the "[Create a new CDN resource"](#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used for the creation of the resource only to identify a resource that should be changed. 

3\. Add the following string before the last curly bracket:  

options { 

4\. Open the [Terraform documentation for the Gcore provider](https://registry.terraform.io/providers/G-Core/gcorelabs/latest/docs/resources/gcore_cdn_resource%23optional) and find the required option. Follow the guide from the Terraform documentation, to enter the required option values. 

5\. Be aware to add a curly bracket to a new string below: 

} 

Here is an example. You want to set up CDN Caching and find this option in the Terraform documentation — edge\_cache\_settings. You need to set up CDN Caching with these settings:  

*   _345600 seconds (4 days)_ is the caching time for responses with 200, 206, 301, and 302 codes, 
*   _1000 seconds_ is the caching time for responses with a 403 code, 
*   _50 seconds_ is the caching time for responses with a 404 code.  

According to the guide, you need to add the necessary settings below the _options {_ string. 

  edge\_cache\_settings {    custom\_values = {       "403" = "1000s"      "404" = "50s" }    enabled = true   value = "345600s" } }

6\. The configuration file now contains the code that creates a CDN resource with your option values. An example of the file:

<img src="https://support.gcore.com/hc/article_attachments/7048212376721/image_1707-2.png" alt="image_1707-2.png">

Save the changes in the configuration file.  

7\. Access the "Terraform" folder in the command-line interface and run the _terraform plan_ command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it. 

8\. Run the _terraform apply_ command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

### Add an SSL certificate 

If a CDN resource was created via Terraform, you can add an SSL certificate via Terraform. To do this, use the guide below. 

1\. Open the _main.tf_ file. 

2_._ The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used for the creation of the resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for issuing an SSL certificate. 

Add the code below before the following string: _resource "gcore\_cdn\_resource" "(name of your resource in Terraform)" {_ . Replace the hints in the brackets with your values and remove the brackets. 

resource "gcore\_cdn\_sslcert" "**(make up Terraform name for your certificate; you can use any name, it will be linked to the certificate inside the Terraform system)**" {   
name = "**(make up a certificate name that will be displayed in the Gcore control panel; it should not match the names of other SSL certificates in the same account)**"   
cert = " **(specify a public key of your certificate, including the BEGIN CERTIFICATE----- and-----END CERTIFICATE---- strings)**"   
private\_key =" **(specify a private key of your SSL certificate, including the -----BEGIN RSA PRIVATE KEY----- and -----END RSA PRIVATE KEY----- string)**"   
}

4\. Add the code below after the _secondary\_hostnames_ string, if any (if not, after _origin\_protocol)_. Replace the hints in the brackets with your values and remove the brackets. 

ssl\_enabled = true   
ssl\_data = gcore\_cdn\_sslcert.**(Terraform name of the certificate)**.id 

Here is an example of adding a certificate. Let's suppose your values are as follows: 

*   _example\_cert_ — the name of the certificate that will be displayed in Terraform, 
*   _example\_certificate —_ the name of the certificate that will be displayed in the control panel, 
*   _\-----BEGIN CERTIFICATE-----MIIDkjCCAnqgAwIBAgIgTfqoZeTGCEvm...T7XH8IlQY0SGq2FSZKJAlrfX+UOpIMWQcOwcuDB97DXl5Bjs+QEXO203GW0C-----END CERTIFICATE-----_ — the public key of the certificate,
*   _\-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAzzj54zBOWxBIJRFMBtG...xyf2T9RZYRpIVbkatg977nXryEZC8Sp8U76c3Oww==-----END RSA PRIVATE KEY----_\- — the private key of the certificate.

To add such a certificate, you have inserted the necessary strings into the configuration file. The file is supposed to look as follows:

<img src="https://support.gcore.com/hc/article_attachments/7048391625745/image_1709-2.png" alt="image_1709-2.png">

5\. Save the changes in the configuration file. 

6\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the _terraform plan_ command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

7\. Run the _terraform apply_ command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 

### Create a rule 

If a CDN resource was created via Terraform, you can [add a rule](https://gcorelabs.com/support/articles/115005383865/) to it via Terraform. To do this, use the guide below.  

1\. Open the _main.tf_ file. 

2_._ The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used to create a resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for creating a rule to the configuration file. 

Add the code below to a new string. Replace the hints in the brackets with your values and remove the brackets.  

resource "gcore\_cdn\_rule" "**(make up Terraform name for the rule; you can use any name, it will be linked to the rule inside the Terraform system)**" {   
  resource\_id = gcore\_cdn\_resource.**(Terraform name of the CDN resource for which you are adding the rule)**.id   
  name = **"(make up a name for the rule that will be displayed in the Gcore control panel)"**   
  rule = "**(specify path to the files for which you are adding the rule; the path should always start with "^/" or "/")**"   
  rule\_type   = 0 

4\. If you want to add options to the rule, paste the code below. Replace the hints in the brackets with your values and remove the brackets. 

options {   
**(code to configure the necessary options; for set-up guides, refer to the [Terraform documentation for the Gcore provider](https://registry.terraform.io/providers/G-Core/gcorelabs/latest/docs/resources/gcore_cdn_rule%23nested-schema-for-options), an example of configuration can be found in the [Configure CDN resource options](#configure-cdn-resource-options) section)**   
} 

If you don't need options, do not add the _options_ code segment. 

5\. Be aware to add a curly bracket to a new string below. 

} 

Here is an example of a configuration file. Let's say you want to add a rule with the following characteristics: 

*   _example\_rule_ — the name of the rule for Terraform, 
*   _cdn\_example\_com_ — the name of the CDN resource in Terraform,  
*   _PNG images —_ the name of the rule for the control panel_._ 
*   _/folder/images/\*.png —_ the path to the files. 
*   The "WebP Compression" option with a final quality of 66 is required. 

The final code in the configuration file will look as follows:

<img src="https://support.gcore.com/hc/article_attachments/7049290958865/image_1712-2.png" alt="image_1712-2.png">

6\. Save the changes in the configuration file. 

7\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the _terraform plan_ command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

8\. Run the _terraform apply_ command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes".