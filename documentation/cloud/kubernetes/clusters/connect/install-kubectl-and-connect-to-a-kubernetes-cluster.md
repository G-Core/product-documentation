---
title: install-kubectl-and-connect-to-a-kubernetes-cluster
displayName: kubectl
published: true
toc:
   --1--What is kubectl?: "what-is-kubectl"
   --1--For Windows: "install-kubectl-on-windows-and-connect-to-a-cluster"
   --1--For Ubuntu and Linux: "install-kubectl-on-ubuntu-linux-and-connect-to-a-cluster"
   --1--For macOS: "install-kubectl-on-macos-and-connect-to-a-cluster"
pageTitle: Connect to Kubernetes nodes via kubectl | Gcore
pageDescription: Discover how to install kubectl, a command-line tool used to manage Kubernetes clusters and connect to them.
---
# Install kubectl and connect to a Kubernetes cluster
  
## What is kubectl?

Kubectl is a command-line tool which allows you to control Kubernetes clusters. With kubectl, you can create and configure resources, manage pods and perform other operations. 

The utility runs as follows: you enter a command, kubeclt accesses the cluster and sends an API request to it. The cluster executes the command and makes changes. For the latest list of kubectl operations, see the <a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands" target="_blank">kubectl official documentation</a>.

Alternatively, there is a tool with a graphical user interface called "Lens". It lets you manage the cluster not from the command line, but from the application window. You can download it on <a href="https://k8slens.dev" target="_blank">k8slens.dev</a>. The guide below applies only to kubectl.

## Install kubectl on Windows and connect to a cluster

1.  Send a CURL request. For version v1.23.0, use the request below: 
    
    ```
    curl -LO [https://storage.googleapis.com/kubernetes-release/release/v1.23.0/bin/windows/amd64/kubectl.exe](https://storage.googleapis.com/kubernetes-release/release/v1.23.0/bin/windows/amd64/kubectl.exe)
    ```

    Instead of a CURL request, you can use a link to download the installation file. Find the link and CURL request for the latest Kubernetes version in <a href="https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/#install-kubectl-binary-with-curl-on-windows" target="_blank">Kubernetes official documentation</a>.  
    
2.  Add the directory containing the **kubectl.exe** file to the **PATH** variable (so the system can access this file when executing kubectl commands). To do this, first copy the path from the command line (this is the directory where kubectl.exe has been downloaded):  
      
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_28.png" alt="image_28.png"> 

    Then go to Windows Settings → System → About → Advanced System Settings (or right-click This PC, then Properties → Advanced System Settings). In the next dialog, select **Environment Variables** and double-click the **Path** system variable. Paste the path to **kubectl.exe** in the bottom most empty field, and save the changes.  

    <media-gallery>
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_61.png" alt="image_61.png" width="341" height="356">
    
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_62.png" alt="image_62.png" width="418" height="363">
    </media-gallery>

3.  In **C:\\Users\\\[username\]** create the **.kube** directory (to store the cluster configuration file).  

    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_46.png" alt="image_46.png" width="556" height="143">

4.  Download the configuration file.  

    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/13323281147921.png" alt="Screenshot_2023-02-27_at_18.50_1.jpg">

5.  Rename the configuration file to "**config"** (without an extension) and add it to the **.kube** folder. Kubectl can now access it and manage your cluster.  
      
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_45.png" alt="image_45.png" width="548" height="107">  
    
6.  Verify the kubectl configuration. Type the command in the command line:
    
    ```
    kubectl get pod
    ```

    The system is supposed to output either "No resources found in default namespace" (when there are no pods in the cluster), or data of the pods. Either result mean that kubectl is correctly configured and you can access your cluster.

## Install kubectl on Ubuntu, Linux and connect to a cluster

1.  Download the latest version of the kubectl binary file with the CURL request. 

    ```
    curl -LO https://storage.googleapis.com/kubernetes-release/release/\`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt\`/bin/linux/amd64/kubectl 
    ```

2.  Make the kubectl binary file executable.  
    
    ```
    chmod +x ./kubectl
    ```

3.  Move the binary file into the directory from the **PATH** variable.
    
    ```
    sudo mv ./kubectl /usr/local/bin/kubectl
    ```

4.  Create the "**.kube**" directory in your home directory:
    
    ```
    mkdir ~/.kube
    ```

5.  Download the configuration file.  
      
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/13323281147921.png" alt="Screenshot_2023-02-27_at_18.50_1.jpg">  
    
6.  Rename the configuration file to "**config**" (without an extension) and add it to the **.kube** folder. Kubectl can now access it and manage your cluster.  
      
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/image_47.png" alt="image_47.png" width="555" height="342">

7.  Verify kubectl configuration with the command below: 
    
    ```
    kubectl get pod
    ```
    
    The system is supposed to output either "No resources found in default namespace" (when there are no pods in the cluster), or data of the pods. Either result mean that kubectl is correctly configured and you can access your cluster.

## Install kubectl on macOS and connect to a cluster

1.  Download the latest version of the kubectl binary file with the CURL request. 
    
    ```
    curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
    ```

2.  Make the kubectl binary file executable: 

    ```
    chmod +x ./kubectl
    ```

3.  Move the kubectl binary file into the directory from the **PATH** variable. To do this, first check which directories correspond to the variable:
    
    ```
    echo $PATH
    ```

    The system returns a list of directories. Select one of them and move the kubectl file there using the command below:
    
    ```
    sudo mv ./kubectl \[one of the directories that has been returned by the "echo $PATH" command\]
    ```

    For example, for the directory "/usr/local/bin/kubectl" the command looks like this: 
    
    ```
    sudo mv ./kubectl /usr/local/bin/kubectl
    ```

4.  Create the ".**kube**" directory in your home directory: 
    
    ```
    mkdir ~/.kube/config
    ```

5.  Download the configuration file.  
      
    <img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/connect/install-kubectl-and-connect-to-a-kubernetes-cluster/13323281147921.png" alt="Screenshot_2023-02-27_at_18.50_1.jpg">

6.  Rename the configuration file to "**config**" (file should not have an extension) and add it to the **.kube** folder. Kubectl can now access it and manage your cluster.

7.  Verify kubectl configuration with the command below: 
    
    ```
    kubectl get pod
    ```
    
    The system is supposed to output either "No resources found in default namespace" (when there are no pods in the cluster), or data of the pods. Either result mean that kubectl is correctly configured and you can access your cluster.