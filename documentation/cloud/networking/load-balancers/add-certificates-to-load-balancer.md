--- 
title: add-certificates-to-load-balancer
displayName: Add multiple certificates to a Load Balancer
published: true
order: 13
toc:
--1—-How it works: "how-it-works"
--1—-Add multiple certificates: "add-multiple-certificates"
--2—-1. Add certificates to Secret Manager: "1-add-certificates-to-the-secrets-manager"
--2—-2. Add certificates to a listener: "2-add-certificates-to-a-listener"
--1—-Create an encrypted password: "create-an-encrypted-password"
pageTitle: Add multiple TLS certificates to a Load Balancer | Gcore
pageDescription: Learn how to create and configure a load balancer with multiple TLS certificates.
--- 
# Add multiple certificates to a Load Balancer 

You can configure multiple TLS (Transport Layer Security) certificates for a single Load Balancer, which allows you to host several secure websites on a single IP address. 

Instead of configuring separate Load Balancers for each website, you can configure just one Load Balancer and add multiple TLS certificates to it. The Load Balancer will serve the correct certificate based on the requested domain name, and everything will be managed in one place. 

## How it works 

Our listeners support Server Name Indication (SNI) extension to handle multiple TLS certificates. Based on the SNI information provided by the client, the listener selects the appropriate TLS certificate for encrypting the connection. Once the TLS connection is terminated at the listener, the Load Balancer inspects the decrypted traffic and routes it to the proper server. 

Each listener can also be configured with its own TLS certificate, corresponding to a specific hostname or domain. 

## Add multiple certificates

You can add multiple certificates to listeners that use the Terminated HTTPS and Prometheus protocols.

### 1. Add certificates to the Secrets Manager 

To get started, you need to add the required certificates to Gcore Secrets Manager. If you don’t have any certificates created, follow the instructions from this guide: <a href="https://gcore.com/docs/cloud/secrets-manager/upload-a-pkcs12-file" target="_blank">Upload a PKCS12 file</a>. 

### 2. Add certificates to a listener 

After you configure the certificates, you need to add them to the relevant listener. This can be done during Load Balancer creation or in the settings of an existing Load Balancer. 

<tabset-element>

#### During Load Balancer creation 

Create a new Load Balancer <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">according to the instructions</a>. In step 5, configure a new listener as follows: 

1\. Give your listener a name.

2\. Select a protocol with the supported TLS encryption: **Terminated HTTPS** or **Prometheus**. 

3\. Use a default port or specify a custom port from 1 to 65535. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/add-listener-name-port.png" alt="Create a listener dialog" width="80%">

4\. (Optional) To identify the origin of the user's IP address connecting to a web server via a Load balancer, enable the **Add headers X-Forwarded-For, X-Forwarded-Port, X-Forwarded-Proto to requests** toggle.

5\. Choose the default TLS Certificate. It’s the main certificate that will be used when there’s no configured certificate for a domain.  

6\. Select the CNI Certificates stored in the Secret Manager.  

7\. Set the connection limit - a maximum number of simultaneous connections that can be handled by the listener.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/add-listener-headers-cni.png" alt="Create a listener dialog" width="80%">

8\. (Optional) Add allowed CIDR ranges to define which IP addresses can access your content. All IP addresses that don’t belong to the specified range will be denied access. 

9\. (Optional) Configure Basic Authentication for HTTP traffic to protect your resource from unauthorized access. Click **Add user** to specify who can access your resource only by logging in with the following credentials: 

* **Enter username**: specify a username that needs to be entered on the login screen. 

* **Password**: specify a password or provide an encrypted password. 

10\. Click **Create Listener**. 

After you configure the listener, proceed with the rest of the steps described in the <a href="https://gcore.com/docs/cloud/networking/create-and-configure-a-load-balancer" target="_blank">Create a Load Balancer</a> guide to finish the balancer’s creation.  

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/create-listener.png" alt="Create a listener dialog" width="80%">

#### From the Load Balancer settings 

If you already have a Load Balancer and don’t want to create a new one to terminate SSL connections, update the existing Load Balancer as follows: 

1\. In the Gcore Customer Portal, navigate to the **Cloud** page and click **Networking**. 

2\. Open the **Load Balancers** page.

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/load-balancers-page.png" alt="Load Balancers page in Customer Portal" width="80%">

3\. Find the Load Balancer you want to configure and click its name to open it. 

4\. Navigate to the **Listeners** tab and click **Add listener**. 

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/listeners-tab.png" alt="Listener tab in the Load Balancer settings" width="80%">

5\. To configure a new listener, follow the same instructions as in the "Add certificates during Load Balancer creation" step.

</tabset-element>

## Create an encrypted password 

When configuring basic authentication for HTTP traffic, you have the option to specify an encrypted password for a user. 

You can use any preferred encryption method or generate a hashed password using the <a href="https://www.unix.com/man-page/linux/1/mkpasswd/" target="_blank">MKPasswd</a> utility.  

To generate a password hash using a dockerized version of MKPasswd:  

1\. Check the available encryption types:   

```
docker run --rm yardalgedal/mkpasswd -m help 
```

2\. Choose your preferred encryption method and generate the password hash.  For example, to create a password hash using the bcrypt method, run:  

```
docker run --rm yardalgedal/mkpasswd -m bcrypt mypassword 
```

3\. Insert the into the **Encrypted password** field:

<img src="https://assets.gcore.pro/docs/cloud/networking/load-balancers/add-certificates-to-load-balancer/encrypted-password-field.png" alt="Encrypted password in listener settings" width="80%">