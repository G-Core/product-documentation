---
title: request-quota-increase
displayName: Request quota increase
published: true
order: 
toc:
  --1-- Step 1. Initialize a quota request: "step-1-initialize-a-quota-request"
  --1-- Step 2. Update the account quotas: "step-2-update-the-account-quotas"
  --2-- Deployment example: "deployment-example"
  --1-- Step 3. Send the quota increase request: "step-3-send-the-quota-increase-request"
  --1-- Step 4. Finalize the quota increase request: "step-4-finalize-the-quota-increase-request"
pageTitle: Request quota increase | Gcore
pageDescription: 
---
# Request account quota increase

You can only deploy AI models if they fit within your quota. Since a new Gcore account has a zero quota, you must request an increase before deploying models.

## Step 1. Initialize a quota request

To create a new quota request, click this [direct link](https://portal.gcore.com/inference-at-the-edge/quotas/viewer) or take the following steps:

Navigate to **Everywhere Inference** > **Quotas** in the Gcore Customer Portal. This will open the **Account Quotas** dialog, where you can view and modify your Everywhere Inference quotas.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/quotas/request-quota-increase/request-quota-increase-1.png" alt="Request quota increase">

## Step 2. Update the account quotas

The Account Quotas dialog shows an overview of the currently configured quotas, which you can use to update for new requests.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/quotas/request-quota-increase/request-quota-increase-2.png" alt="Request quota increase">

### Deployment example

Let’s look at the following settings for a model deployment:

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/quotas/request-quota-increase/request-quota-increase-3.png" alt="Request quota increase">

The deployment uses:

- The 1xL40S / 16 vCPU / 232 GiB RAM flavor
- Two regions
- One pod

The deployment will run two pods, one in each region, so you should request at least the following quota:

- 1 deployment
- 20000 millicores
- 2 GPU L40S

If you configure autoscaling to go up to two pods per region, you should request this quota:

- 1 deployment
- 40000 millicores
- 4 GPU L40S

<alert-element type="info" title="Info">
If you’re not sure about your requirements, request more than you think you need so you can change your autoscaling settings later.
</alert-element>

## Step 3. Send the quota increase request

The **Request** form is on the right. Fill it out with a description explaining why you need the increase, then click the **Send request** button.

<img src="https://assets.gcore.pro/docs/edge-ai/everywhere-inference/quotas/request-quota-increase/request-quota-increase-4.png" alt="Request quota increase">

## Step 4. Finalize the quota increase request

It can take up to 15 minutes until your quotas are updated. After the update is applied, you can deploy AI models or update your autoscaling settings for existing ones.
