---
title: add-ssl-certificate-to-cdn-via-terraform
displayName: Add an SSL certificate via Terraform
published: true
order: 50
toc:
pageTitle: A guide on how to add an SSL certificate via Terraform | Gcore
pageDescription: Learn how to add an SSL certificate to a CDN resource via Terraform.
---
# Add an SSL certificate to a CDN resource via Terraform 

If a CDN resource was created via Terraform, you can add an SSL certificate via Terraform. To do this, use the following steps. 

1\. Open the *main.tf* file. 

2\. The file is supposed to contain the code for the creation of your CDN resource. If it is missing, add the code according to the [Create a new CDN resource](https://gcore.com/docs/cdn/terraform/manage-a-cdn-resource-with-terraform#create-a-new-cdn-resource) section.  

Don't worry, Terraform won't duplicate a resource. Terraform requires the code used for the creation of the resource only to identify a resource that should be changed. 

3\. At this step, you will add the necessary strings for issuing an SSL certificate. 

Add the code below before the following string: ```resource "gcore_cdn_resource" "(name of your resource in Terraform)" {```. Replace the hints in the brackets with your values and remove the brackets. 

<code-block>
resource "gcore_cdn_sslcert" "<span style="color:#FF5913">make up Terraform name for your certificate; you can use any name, it will be linked to the certificate inside the Terraform system</span>" {   
name = "<span style="color:#FF5913">make up a certificate name that will be displayed in the Gcore Customer Portal; it should not match the names of other SSL certificates in the same account</span>"   
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
- <span style="color:#FF5913">example_certificate</span> — the name of the certificate that will be displayed in the Gcore Customer Portal, 
- <span style="color:#FF5913">-----BEGIN CERTIFICATE-----MIIDkjCCAnqgAwIBAgIgTfqoZeTGCEvm...T7XH8IlQY0SGq2FSZKJAlrfX+UOpIMWQcOwcuDB97DXl5Bjs+QEXO203GW0C-----END CERTIFICATE-----</span> — the public key of the certificate,
- <span style="color:#FF5913">-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAzzj54zBOWxBIJRFMBtG...xyf2T9RZYRpIVbkatg977nXryEZC8Sp8U76c3Oww==-----END RSA PRIVATE KEY-----</span> — the private key of the certificate.

To add such a certificate, you have inserted the necessary strings into the configuration file. The file is supposed to look as follows:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/manage-a-cdn-resource-with-terraform/image_1709-2.png" alt="configuration file" width="80%">

5\. Save the changes in the configuration file. 

6\. Access the "Terraform" folder in the command-line interface unless you are already in it, and run the ```terraform plan``` command — it will show what changes Terraform is going to make. If the code contains an error, the output will give a brief description of it.  

7\. Run the ```terraform apply``` command — it will make changes to the CDN. Terraform will ask you to confirm the action — enter "yes". 