---
title: upgrade
displayName: Upgrade
published: true
order: 15
toc:
   --1--Implications for cluster APIs: "implications-for-cluster-apis"
   --1--Implications for applications: "implications-for-applications"
   --1--Best practices: "best-practices"
   --1--How to upgrade a cluster: "how-to-upgrade-a-cluster"
   --2--Step 1. Select a cluster: "step-1-select-a-cluster"
   --2--Step 2. Initialize the cluster upgrade: "step-2-initialize-the-cluster-upgrade"
   --2--Step 3. Finalize: "step-3-finalize"
pageTitle: Upgrade a Kubernetes cluster | Gcore
pageDescription: You can perform a Kubernetes cluster version upgrade to get the latest Kubernetes features and make sure that your cluster is secure and stable.
---
# Upgrade a Kubernetes cluster

You can perform a Kubernetes cluster version upgrade to get the latest Kubernetes features and make sure that your cluster is secure and stable.

## [Implications for cluster APIs](#implications-for-cluster-apis)

Kubernetes version upgrades might change the Kubernetes API and features. Please check the official Kubernetes documentation to find the latest changes.

## [Implications for applications](#implications-for-applications)

We use a rolling update approach, where the update procedure terminates the existing worker nodes one by one and creates new worker nodes. While rolling upgrades won’t stop all nodes at once, they can still have performance implications for your users if you don't have any spare capacity.

## Best practices

- Plan upgrades and learn if deprecated APIs are removed in the target version.
- Test your upgrades in a non-production environment before attempting an upgrade in production.
- Use our Kubernetes logging feature to see what’s happening during an upgrade.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-1.png" alt="upgrade">

## How to upgrade a cluster

To upgrade the Kubernetes version of a cluster, perform the following steps:

### Step 1. Select a cluster

Open the **Managed Kubernetes** tab in the **Cloud** section and select a cluster from the list.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-2.png" alt="upgrade">

If a newer version of Kubernetes is available for the cluster, a **Change** link will appear beside the version under **General Info**.

Click the **Change** link to start the update.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-3.png" alt="upgrade">

A pop-up window will open where you can select a new version.

### Step 2. Initialize the cluster upgrade

Select a new version and click the **Change** button.

**Warning:** Downgrade is only supported for one patch version down (e.g., from 1.24.9 to 1.24.8).

**Warning:** Changing your cluster version will take several minutes, during which API access to the cluster may be unstable.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-4.png" alt="upgrade">

Clicking on the **Change** button will open another popup that asks you to confirm the version upgrade. Click on the **Yes, upgrade** button to start the upgrade.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-5.png" alt="upgrade">

When the update starts, both popups will close. You’ll see a loading indicator when the update is in progress.

### Step 3. Finalize

After the update, check that the version under **General Info** matches your selected version.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/upgrade/upgrade-6.png" alt="upgrade">
