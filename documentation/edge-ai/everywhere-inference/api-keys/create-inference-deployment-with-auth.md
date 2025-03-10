---
title: create-inference-deployment-with-auth
displayName: Create an inference deployment with authorization
published: true
order: 1
toc:
  --1-- Step 1. Enable authorization: "step-1-enable-authorization"
  --1-- Step 2. Retrieve API key: "step-2-retrieve-the-api-key"
  --1-- Step 3. Use API key for authorization: "step-3-use-api-key-for-authorization"
pageTitle: Create an Inference Deployment with Authorization | Gcore
pageDescription: Learn how to deploy an AI model with authorization enabled and use the API Key for secure access.
---

# Create an inference deployment with authorization

To ensure that only authenticated clients can access your AI models, you must deploy an inference instance with authorization enabled.

## Step 1. Enable authorization

When deploying an AI model, set the `auth_enabled` option to `true`. This means an API Key will be automatically generated and linked to the deployment.

## Step 2. Retrieve the API key

Once the deployment is created with authentication enabled, you can retrieve the API Key via the designated API endpoint.

### API request

The API key can be retrieved via [this endpoint](https://api.gcore.com/docs/cloud#tag/Everywhere-Inference/operation/InferenceInstanceApikeySecretHandlerV3.get). 

<alert-element type="info" title="Info">
The API Key is only available through this endpoint. Store it securely.
</alert-element>

## Step 3. Use the API key for authorization

Once you have retrieved the API Key, include it in your API requests using the `X-API-Key` header.

### Example using OpenAI Python client library

Here’s an example demonstrating how to use the API key for authorization:

```python
from openai import OpenAI

def get_llm_response(message: str) -> str:
    client = OpenAI(api_key=LLM_KEY, base_url=f"{LLM_API}/v1")

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=[
            {"role": "user", "content": message},
        ],
        extra_headers={"X-API-Key": LLM_KEY},
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(get_llm_response("Why is the sky blue?"))
```

<alert-element type="info" title="Info">
For Gcore deployments with authorization enabled, the `X-API-Key` header is mandatory in all API requests.
</alert-element>

To learn more about deploying AI models, refer to [our dedicated guide](https://gcore.com/docs/edge-ai/everywhere-inference/ai-models/deploy-an-ai-model).
