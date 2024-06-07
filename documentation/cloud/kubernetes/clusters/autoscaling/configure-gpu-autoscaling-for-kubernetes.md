---
title: configure-gpu-autoscaling-for-kubernetes
displayName: Configure GPU autoscaling for Kubernetes
order: 40
published: true
toc:
   --1--Step 1. Create a Kubernetes cluster: "step-1-create-a-kubernetes-cluster"
   --1--Step 2. Verify your Kubernetes configuration: "step-2-verify-your-kubernetes-configuration"
   --1--Step 3. Install GPU Operator: "step-3-install-gpu-operator"
   --1--Step 4. Verify GPU allocation: "step-4-verify-gpu-allocation"
   --1--Step 5. Run test CUDA pod: "step-5-run-test-cuda-pod"
   --1--Step 6. Install KEDA: "step-6-install-keda"
   --1--Step 7. Install kube-prometheus stack: "step-7-install-kube-prometheus-stack"
   --1--Step 8. Create Autoscaling configuration: "step-8-create-autoscaling-configuration"
   --1--Step 9. Check the results: "step-9-check-the-results"   
pageTitle: Configure GPU Autoscaling for Managed Kubernetes | Gcore
pageDescription: Learn how to set up KEDA with Managed Kubernetes for GPU scaling.
---
# Configure GPU autoscaling for Kubernetes

If you manage GPU-intensive workloads with fluctuating traffic in a Kubernetes cluster, you can configure the Kubernetes Event-Driven Autoscaling (KEDA) component to automatically scale your GPU resources based on real-time demand. With such a setup, you’ll ensure optimal performance and cost efficiency of your application. 

## Step 1. Create a Kubernetes cluster

Add a new Managed Kubernetes cluster with the Bare Metal worker pool: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Kubernetes**. 

2\. Click **Create Cluster**. 

3\. Select a region—the location of the data center where your cluster will be deployed.  

4\. Select the Kubernetes cluster version: v.1.28.6 or higher. 

5\. Configure Bare Metal pools: 

* **Pool name**: Enter a unique and descriptive name for your resource pool. 

* **Minimum nodes** and **Maximum nodes**: specify how many nodes can be allocated to the pool during traffic fluctuations. The maximum number of pods must be greater than the minimum, allowing the system to scale up in response to increased demand. 

* **Type**: Choose **Bare Metal instances**. 

* **Infrastructure**: select the needed GPU-optimized flavor. You need to add at least one node with GPU support to the worker pool. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/gpu-autoscaling/configure-pools.png" alt="Pools configuration section on the Create Kubrnetes cluster page.jpg">

6\. (Optional) Add labels to include additional information about your nodes. You can also specify taints, which are special conditions that define which Kubernetes pods can run on these nodes.  

7\. Disable the **Autohealing nodes** toggle. 

8\. (Optional) Enable the **Public IPv4 address** option to assign public IPv4 addresses to cluster nodes. 

9\. If you need to add more pools, click **Add pool** and configure it according to the previous steps.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/gpu-autoscaling/configure-toggles.png" alt="A list of toggles with configurations for steps 6-9" width="80%">

10\. Continue configuring the cluster by following the instructions from <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster#step-5-select-the-cni-provider" target="_blank">Step 5: Select the CNI provider<a> in the <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster" target="_blank">Create a Kubernetes cluster</a> guide.  

## Step 2. Verify your Kubernetes configuration 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Kubernetes**. 

2\. Find the cluster you’ve created in the previous step and click its name to open it. 

3\. Check the pool status—it should be **Running**. If you see **Scaling up**, wait until all resources are allocated and the cluster ready to use.  

4\. Download the .config file by clicking **Kubernetes config** in the top-right corner of the screen.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/gpu-autoscaling/kubernetes-config.png" alt="Kubernetes cluster overview page" width="80%">

5\. Export Kubernetes configuration locally:  

<code-block>

export KUBECONFIG=/path/to/your/k8sConfig.yml 

</code-block>

6\. Verify that the created node is ready and correctly configured: 

<code-block>

kubectl get nodes 

</code-block>

Here’s an example of the expected result: 

<code-block>

NAME                STATUS   ROLES    AGE     VERSION 
ed-b16-82-160-248   Ready    <none>   3h26m   v1.28.6 

</code-block>

## Step 3. Install GPU Operator 

Use Helm package manager to install the GPU Operator that’ll manage your resources. If you don’t have Helm, install it according to the <a href="https://helm.sh/docs/intro/install/" target="_blank">official instructions</a>. 

To install the GPU Operator: 

1\. Add the NVIDIA Helm repository and update it as follows:  

<code-block>

helm repo add nvidia https://helm.ngc.nvidia.com/nvidia && helm repo update

</code-block>

2\. Install the GPU Operator with the required configurations for your Kubernetes version: 

* 1.28.x:   

    <code-block>

    helm install gpu-operator nvidia/gpu-operator --version v23.9.1  --wait \ 
        -n gpu-operator --create-namespace \ 
        --set driver.enabled=false \ 
        --set operator.defaultRuntime=crio \ 
        --set operator.logging.level=debug 
    
    </code-block> 
* 1.29.x: 

    <code-block>

    helm install gpu-operator nvidia/gpu-operator --version v23.9.2  --wait \ 
        -n gpu-operator --create-namespace \ 
        --set driver.enabled=false \ 
        --set operator.defaultRuntime=crio \ 
        --set operator.logging.level=debug 
    
    </code-block>    

## Step 4. Verify GPU allocation 

1\. Verify that GPUs have been correctly allocated. The number of GPU nodes in `nvidia.com/gpu` should comply with the number specified in the Bare Metal flavor. 

<code-block>

Allocatable: 
  cpu:                192 
  ephemeral-storage:  850152999143 
  hugepages-1Gi:      0 
  hugepages-2Mi:      0 
  memory:             2113338172Ki 
  nvidia.com/gpu:     8 
  pods:               110

</code-block>

2\. Check the status of the Kubernetes pods–it should be **READY**. 

<code-block>

kubectl get pods -n gpu-operator 

</code-block>

Here’s an example of the expected result: 

<code-block>

NAME                                                         READY   STATUS      RESTARTS   AGE 
gpu-feature-discovery-f4knk                                  1/1     Running     0          3m9s 
gpu-operator-f7ffcf7f8-sf8m7                                 1/1     Running     0          3m34s 
gpu-operator-node-feature-discovery-gc-7cc7ccfff8-77g45      1/1     Running     0          3m34s 
gpu-operator-node-feature-discovery-master-d8597d549-dnxz5   1/1     Running     0          3m34s 
gpu-operator-node-feature-discovery-worker-rlf6p             1/1     Running     0          3m34s 
nvidia-container-toolkit-daemonset-rl9p2                     1/1     Running     0          3m1s 
nvidia-cuda-validator-78g72                                  0/1     Completed   0          2m32s 
nvidia-dcgm-exporter-nv9bk                                   1/1     Running     0          3m9s 
nvidia-device-plugin-daemonset-4l5fl                         1/1     Running     0          3m9s 
nvidia-mig-manager-rqnsq                                     1/1     Running     0          26s 
nvidia-operator-validator-n9rpz                              1/1     Running     0          3m9s 

</code-block>

## Step 5. Run test CUDA pod

Run a test GPU application to verify that the GPU resources in your Kubernetes cluster are properly configured and accessible. Follow the instructions from the official Nvidia guide: <a href="https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#cuda-vectoradd" target="_blank">Verification: running sample GPU application</a>. 

## Step 6. Install KEDA 

Install and configure the Kubernetes Event-Driven Autoscaling (KEDA) component for your Managed Kubernetes cluster. 

1\. Add the KEDA Helm repository: 

<code-block>
 
helm repo add kedacore https://kedacore.github.io/charts 
 
</code-block> 

2\. Update the repository to include any new Helm charts: 

<code-block>

helm repo update 

</code-block>

3\. Install KEDA into its own namespace: 

<code-block>

helm install keda kedacore/keda --namespace keda --create-namespace 

</code-block>

## Step 7. Install kube-prometheus stack 

To collect and visualize metrics from your Kubernetes cluster, install the <a href="https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack" target="_blank">kube-prometheus-stack</a>that’s integrated with Prometheus and Grafana.  

1\. Add the Prometheus Helm repository:  

<code-block>

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts 

</code-block>

2\. Update the repository: 

<code-block>

helm repo update

</code-block>

3\. Inspect the default values for the kube-stack: 

<code-block>

helm inspect values prometheus-community/kube-prometheus-stack > values.yaml 

</code-block>
 
4\. Create the values-overrides.yaml file that contains additional configurations for the GPU operator:

<code-block>

serviceMonitorSelectorNilUsesHelmValues: false 

additionalScrapeConfigs: 
/- job_name: gpu-metrics 
  scrape_interval: 1s 
  metrics_path: /metrics 
  scheme: http 
  kubernetes_sd_configs: 
  /- role: endpoints 
    namespaces: 
      names: 
      - gpu-operator 
  relabel_configs: 
  /- source_labels: [__meta_kubernetes_endpoints_name] 
    action: drop 
    regex: .*-node-feature-discovery-master 
  /- source_labels: [__meta_kubernetes_pod_node_name] 
    action: replace 
    target_label: kubernetes_node 

</code-block>    

5\. Install kube-stack with the specified configurations: 

<code-block>

helm install prometheus-community/kube-prometheus-stack \ 
   --create-namespace --namespace prometheus \ 
   --generate-name \ 
   -f values.yaml -f values-overrides.yaml

</code-block>  

## Step 8. Create Autoscaling configuration 

1\. Create a deployment for the test workload and define an autoscaling configuration using KEDA: 

<code-block>

apiVersion: apps/v1
kind: Deployment
metadata:
  name: <span style="color:#FF5913">workload-name</span>
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gpu
  template:
    metadata:
      labels:
        app: gpu
    spec:
      containers:
        - name: <span style="color:#FF5913">workload-name</span>
          image: <span style="color:#FF5913">app-URL</span>
          command: <span style="color:#FF5913">["--argument-1", "-argument-2"]</span>
          args: <span style="color:#FF5913">app-URL</span>
          resources:
            limits:
              nvidia.com/gpu: <span style="color:#FF5913">allocated-number-of-GPUs</span>
/---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: gpu-dcgmproftester-deployment-scaledobject
spec:
  scaleTargetRef:
    name: <span style="color:#FF5913">workload-name</span>
  minReplicaCount: <span style="color:#FF5913">number-of-replicas</span>
  maxReplicaCount: <span style="color:#FF5913">number-of-replicas</span>
  triggers:
  /- type: prometheus
    metadata:
      serverAddress: http://prometheus-operated.prometheus:9090
      metricName: <span style="color:#FF5913">metrics-name</span>
      threshold: "<span style="color:#FF5913">threshold-number</span>"
      query: sum(avg_over_time(DCGM_FI_DEV_GPU_UTIL{pod=~"<span style="color:#FF5913">workload-name</span>.*"}[30s])) # <- HPA will divide it for number of replicas due to AVG strategy

</code-block>

<alert-element type="tip" title="Tip">
 
This autoscaling configuration is based on the `DCGM_FI_DEV_GPU_UTIL` metrics (GPU utilization). However, you can use any of available metric from <a href="https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html" target="_blank">DCGM exporter</a>. 
 
</alert-element>

Customize the highlighted values: 

* <span style="color:#FF5913">workload-name</span>: enter a unique name that identifies your workload. Make sure that you use the same value in all name fields.  

* span style="color:#FF5913">app-URL</span>: specify the location of your application. For example, a Docker image.  

* span style="color:#FF5913">allocated-number-of-GPUs</span>: specify how many GPUs you need. For example, 8. 

* span style="color:#FF5913">["/usr/bin/sample-command"]</span>: Enter the command your container should run at startup. 

* span style="color:#FF5913">["--argument-1", "-argument-2"]</span>: Provide any arguments that should be passed to the command.  

* span style="color:#FF5913">number-of-replicas</span>: Provide the minimum and maximum number of workload copies the system will create during traffic fluctuation. 

* span style="color:#FF5913">metrics-name</span>: Enter a unique-phrase-that-distinguishes-your-metrics 

* span style="color:#FF5913">threshold-number</span>: If the number is reached, the system creates a new workload. For instance, “60”. 

## Step 9. Check the results 

After an application with the GPU workload is deployed, Keda creates a Horizontal Pod Autoscaler (HPA) for this workload and injects the value of GPU utilization from Prometheus as an external metric. 

To get real-time information about the HPA, run: 

<code-block>

k get hpa -w 

</code-block>

You should get an output like this:  

<code-block>

NAME                                                  REFERENCE                                  TARGETS              MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-gpu-dcgmproftester-deployment-scaledobject   Deployment/gpu-dcgmproftester-deployment   <unknown>/60 (avg)   1         16        0          0s
keda-hpa-gpu-dcgmproftester-deployment-scaledobject   Deployment/gpu-dcgmproftester-deployment   0/60 (avg)           1         16        1          16s
keda-hpa-gpu-dcgmproftester-deployment-scaledobject   Deployment/gpu-dcgmproftester-deployment   23/60 (avg)          1         16        1          76s
....
keda-hpa-gpu-dcgmproftester-deployment-scaledobject   Deployment/gpu-dcgmproftester-deployment   67750m/60 (avg)      1         16        8          10m

</code-block>

Because there are 8 GPUs per server, the system has spun up eight pods. 

After scaling by the number of GPUs, you’ll notice that there are some pending pods created by the HPA. The autoscaler will trigger the addition of new nodes because the cluster is out of free GPUs. 

To fetch the events, run:

<code-block>

k get events -w

</code-block>

You should get an output like this: 

<code-block>

....
0s          Warning   FailedScheduling      pod/gpu-dcgmproftester-deployment-9f866ff47-dnzns                             0/1 nodes are available: 1 Insufficient nvidia.com/gpu. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod..
 
....
kube-system    69s         Normal    ScaledUpGroup         configmap/cluster-autoscaler-status                                           Scale-up: setting group MachineDeployment/76-320426/gpu-autoscale-h100-h100-machine-deployment size to 2 instead of 1 (max: 2)
kube-system    69s         Normal    ScaledUpGroup         configmap/cluster-autoscaler-status                                           Scale-up: group MachineDeployment/76-320426/gpu-autoscale-h100-h100-machine-deployment size set to 2 instead of 1 (max: 2)

</code-block>

Wait until the node is provisioned, which might take up to 20-25 minutes.  

Check out all pods within your cluster: 

<code-block>

k get pods 

</code-block>
 
Here’s an example output: 

<code-block>

NAME                                            READY   STATUS    RESTARTS   AGE
apiserver-bridge-j7jk6                          1/1     Running   0          141m
gpu-dcgmproftester-deployment-9f866ff47-57zmg   1/1     Running   0          11m
gpu-dcgmproftester-deployment-9f866ff47-5wxxb   1/1     Running   0          15m
gpu-dcgmproftester-deployment-9f866ff47-8gkm8   1/1     Running   0          14m
gpu-dcgmproftester-deployment-9f866ff47-9t4bv   1/1     Running   0          7m57s
gpu-dcgmproftester-deployment-9f866ff47-dnzns   0/1     Pending   0          6m57s
gpu-dcgmproftester-deployment-9f866ff47-fb5cs   0/1     Pending   0          6m57s
gpu-dcgmproftester-deployment-9f866ff47-qthzr   1/1     Running   0          10m
gpu-dcgmproftester-deployment-9f866ff47-rxm2c   1/1     Running   0          17m
gpu-dcgmproftester-deployment-9f866ff47-tc8pq   1/1     Running   0          8m58s
gpu-dcgmproftester-deployment-9f866ff47-zbt8d   1/1     Running   0          12m

</code-block>

8 pods are running (there are 8 GPUs per server), and several pods have a Pending status as they wait for the provisioning of a new node. 

After the new node is provisioned, the system will create new pods. In the end, you’ll have the number of pods you’ve specified in the `maxReplicaCount` in Step 8. 

<alert-element type="info" title="Info">

After provisioning nodes, it might take up to five minutes for the Nvidia GPU resources to be distributed and managed in the Kubernetes cluster.

</alert-element>

To retrieve the list of nodes and related information, run:

<code-block>

k get nodes

</code-block>  

Here’s the sample output:  

<code-block>

NAME                STATUS   ROLES    AGE    VERSION
ed-b16-78-161-160   Ready    <none>   166m   v1.28.6
ed-b16-78-161-169   Ready    <none>   12m    v1.28.6

</code-block>

Double-check the HPA status:  

<code-block>

k get hpa 

</code-block>

You should see something like this: 

<code-block>

NAME                                                  REFERENCE                                  TARGETS           MINPODS   MAXPODS   REPLICAS   AGE
keda-hpa-gpu-dcgmproftester-deployment-scaledobject   Deployment/gpu-dcgmproftester-deployment   71463m/60 (avg)   1         16        16         41m

</code-block>
