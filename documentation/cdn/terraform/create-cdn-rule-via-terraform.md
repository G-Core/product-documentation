---
title: create-cdn-rule-via-terraform
displayName: Create a CDN rule via Terraform
published: true
order: 30
pageTitle: A guide on how to create a CDN rule with Terraform | Gcore
pageDescription: Learn how to add a new CDN rule to the resource and configure the needed settings via Terraform.
---
# Create a CDN rule via Terraform

If a CDN resource was created via Terraform, you can <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files" target="_blank">add a rule</a> to it via Terraform. To do this, use the following instructions.  

1\. Open the *main.tf* file. 

2\. The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](https://gcore.com/docs/cdn/terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used to create a resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for creating a rule to the configuration file. 

Add the code below to a new string. Replace the hints in the brackets with your values and remove the brackets.  

<code-block>
resource "gcore_cdn_rule" "<span style="color:#FF5913">make up Terraform name for the rule; you can use any name, it will be linked to the rule inside the Terraform system</span>" {   
  resource_id = gcore_cdn_resource.<span style="color:#FF5913">Terraform name of the CDN resource for which you are adding the rule</span>.id   
  name = "<span style="color:#FF5913">make up a name for the rule that will be displayed in the Gcore Customer Portal</span>"   
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
- <span style="color:#FF5913">PNG images</span> — the name of the rule from the Gcore Customer Portal. 
- <span style="color:#FF5913">/folder/images/*.png</span> — the path to the files. 
- The "WebP Compression" option with a final quality of 66 is required. 

The final code in the configuration file will look as follows:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1712-2.png" alt="configuration file" width="80%">

6\. Save the changes in the configuration file. 

7\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

8\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes".

