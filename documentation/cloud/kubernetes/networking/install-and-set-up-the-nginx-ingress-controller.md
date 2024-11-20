---
title: install-and-set-up-the-nginx-ingress-controller
displayName: Install nginx Controller
order: 30
published: true
toc:
pageTitle: Install nginx Controller| Gcore
pageDescription: Learn how to install nginx Ingress Controller to effectively manage network traffic within a cluster.
---
# Install nginx Ingress Controller

When you install the nginx Ingress Controller, our system automatically creates a <a href="https://gcore.com/cloud/load-balancers" target="_blank">Load Balancer</a>. This Load Balancer acts as an entry point for incoming traffic. When traffic arrives, the Load Balancer forwards it to the Ingress Controller. The Ingress Controller is responsible for routing the traffic to the appropriate services within your Managed Kubernetes cluster based on the rules defined in the Ingress manifests.

## Step 1. Install Helm

Using <a href="https://helm.sh/" target="_blank">Helm</a> package manager simplifies the process of deploying, managing, and scaling applications on Kubernetes. 

The following sections contain instructions for installing Helm on Windows, Ubuntu, and macOS. For more installation options, check out the official <a href="https://helm.sh/docs/intro/install/" target="_blank">installing Helm</a> guide. 

<tabset-element>

### On Linux  

1\. In the Terminal, run the official Helm installation script: 

```
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

This command will download and install the latest version of Helm and place the Helm binary in /usr/local/bin/helm (or another location based on your system's configuration). 

2\. Verify that Helm was installed successfully by checking its version: `helm version`. You should get the installed version of Helm.

### On macOS 

If you have <a href="https://brew.sh/" target="_blank">Homebrew</a> installed, run `brew install helm`. 

Verify installation by running `helm version`.This command should return the Helm version that was installed. 

If you don’t have Brew on your macOS, follow the installation steps for Linux.

### On Windows

1\. Download the latest Helm release from the <a href="https://github.com/helm/helm/releases" target="_blank">Helm GitHub releases</a> page. 

2\. Extract the contents of the downloaded ZIP file to a directory of your choice. For instance, `C:\Program Files\Helm`. 

3\. Add Helm binary to the `PATH`: 

 a. Open the **Start** menu and search for **Environment Variables**. 

 b. Click **Edit** the system environment variables. 

 c. In the **System properties** window, click **Evironment variables**. 

 d. In the **System variables** section, click **New**.  

 e. Provide a variable name and add the full path to the directory where you moved `helm.exe` (e.g., `C:\Program Files\Helm`). 

 f. Click **OK** to save the changes. 

 g. Verify the installation. In the Terminal, run `helm version`. You should get the latest release version downloaded from the GitHub repositoty in step 1. 

</tabset-element>

## Step 2. Create a namespace

Run the following kubectl command to create a namespace:

```
kubectl create namespace ingress-nginx
```

## Step 3. Add helm repository for the nginx Controller

 Run the following command to add the helm repository for the nginx Ingress Controller:

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```

## Step 4. Update helm repository

Update data in the helm repository:

```
helm repo update
```

## Step 5. Install nginx Ingress Controller

Run the following command:

```
helm install ingress-nginx ingress-nginx/ingress-nginx  \
--namespace ingress-nginx \
--set controller.ingressClassResource.name=nginx
```

After the nginx Ingress Controller is installed, it will automatically create a Load Balancer on your behalf.

## Step 6. Get an IP of a Load Balancer

To get the IP address of the created Load Balancer, execute the command below:

```
watch kubectl -n ingress-nginx get svc
```
Wait until the `<pending> state` of the `EXTERNAL-IP` column changes to the IP address.

The Load Balancer will be shown in the Gcore Customer Portal on the **Load Balancers** page. The traffic will reach the nginx Ingress Controller via this balancer.