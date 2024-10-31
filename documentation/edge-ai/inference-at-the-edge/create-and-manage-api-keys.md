---
title: create-and-manage-api-keys
displayName: Create and manage API keys
published: true
order: 30
toc:
    --1—-Create an API key: "create-an-api-key"
    --1--Access a model using API key: "access-a-model-using-api-key"
    --1--Manage API keys: "manage-api-keys"
    --2--Edit API key: "edit-api-key"
    --2--Delete API key: "delete-api-key"
pageTitle: Create and Manage API Keys | Gcore
pageDescription: Learn how to create API keys and attach them to Gcore Inference at the Edge deployments.
---
# Create and manage API keys

Setting up API keys protects deployed AI models from unauthorized access.

You can add multiple API keys to a single deployment, and the same API key can be attached to multiple deployments.

## Create an API key

You can create an API key in different ways: <a href="https://gcore.com/docs/cloud/inference-at-the-edge/deploy-ai-model" target="_blank">during AI model deployment</a>, <a href="https://gcore.com/docs/cloud/inference-at-the-edge/manage-deployments" target="_blank">via a deployed AI model's settings</a>, or on the **API keys** page. Here, we explain the latter approach.

To create an API key and add it to the deployment:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **API keys**.

3\. Click **Create API key**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/create-api-key.png" alt="API keys page with highlighted Add api key button" width="80%">

4\. In the **General** section, specify the API key name. Optionally, add a description.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/general-tab-keys.png" alt="General section with key name and description" width="80%">

5\. In the **Inference instances** dropdown, select one or more deployments for which this key will be required for authentication.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/instances-tab.png" alt="Inference instances section with instance dropdown" width="80%">

6\. In the **Expiration** section, select for how long the key will be valid:

* **Never expire**: The key will remain valid indefinitely.

* **Set an expiration date**: After the specified date, the key will no longer grant access to the attached deployments. By default, the key expires at 00:00 UTC on the specified date.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/expiration-tab.png" alt="Expiration section date options" width="80%">

7\. Click **Create**.

8\. Copy the key and save it locally.

9\. Click **OK, I’ve copied API Key**.

The key has been successfully created.

<alert-element type="warning" title="Warning">

Never share your API key with third parties. This might result in unauthorized access to your deployments.

</alert-element>

## Access a model using API key

To access an AI model where an API key was added as an authorization method, you must include that API key in your cURL request.  

Add your API key to the request header: 

<code-block> 
curl --location 'YOUR_MODEL_ENDPOINT' \ 
--header 'x-api-key: <span style="color:#FF5913">YOUR_API_KEY</span>' 
</code-block>

The following examples demonstrate how to authenticate to an OpenAI model deployed on inference nodes with the API key.

**Example 1** 

<code-block> 
client = OpenAI( 
    base_url="<Inference Endpoint>/v1", 
    api_key="notused", 
    default_headers={ 
        "x-api-Key": "<APIKEY>", 
    } 
) 
completion = client.chat.completions.create( 
  model="<ModelName>", 
  messages=[ 
    {"role": "user", "content": "Hello!"} 
  ] 
) 
print(completion.choices[0].message)
</code-block> 

**Example 2**

<code-block> 
from typing import override
  
from openai import OpenAI

class GcoreCompatibleOpenAI(OpenAI):
    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-Key": api_key}


client = GcoreCompatibleOpenAI(
    base_url="<Inference Endpoint>/v1",
    api_key="<APIKEY>",
)
completion = client.chat.completions.create(
  model="<ModelName>",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)
</code-block> 

## Manage API keys

You can view detailed information about an API key, change the deployments where it's used for authentication, modify the expiration date, or delete the key from the Gcore Customer Portal.

### Edit API key

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Inference at the Edge**.

2\. Click **API keys**.

3\. Find the key you want to edit and click the three-dot icon to open the settings menu.

4\. Click **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/edit-api-key.png" alt="api key settings with highlighted edit button" width="80%">

A new page with the key overview will open. To check a particular functionality, navigate to the relevant tab.

#### General

In this tab, you can update the key name and description.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/general-tab-keys.png" alt="General tab with options to edit key name and description" width="80%">

#### Inference instances

In this tab, you can add or remove deployments where this API key will be required to authenticate.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/instances-tab-keys.png" alt="Instances tab with dropdpwn tp add instances" width="80%">

#### Expiration

If your key is close to expiring, you can modify the expiry date on this tab, ensuring that the key remains a valid authentication method. Alternatively, you can choose the option **Never expire** to keep the key valid indefinitely.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/expiration-tab-keys.png" alt="Expiration tab with options to change expiration date" width="80%">

### Delete API key

1\. In the Gcore Customer Portal, navigate to **Cloud** > **AI infrastructure**.

2\. Open the **Inference at the Edge** page and click **API keys**.

3\. Find the key you want to remove and click the three-dot icon to open the settings menu.

4\. Click **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/delete-api-key.png" alt="api key settings with highlighted delete button" width="80%">

5\. Confirm your action by clicking **Delete API key**.

<img src="https://assets.gcore.pro/docs/cloud/inference-at-the-edge/create-and-manage-api-keys/verify-key-deletion.png" alt="Delete key confirmation dialog" width="80%">

Your API key has been successfully removed. 

