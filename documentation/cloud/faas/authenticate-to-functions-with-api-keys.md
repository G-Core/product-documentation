---
title: authenticate-to-functions-with-api-keys 
displayName: Authenticate to functions with API keys
published: true
order: 20
toc:
   --1--Create an API key: "create-an-api-key"
   --1--Change API key settings: "change-api-key-settings"
   --1--Delete an API key: "delete-an-api-key"
   --1--FAQs: "faqs"
pageTitle: Authenticate to functions with API keys | Gcore
pageDescription: Learn how to create and manage API keys to protect your function endpoints from unauthorized access.
---
# Authenticate to functions with API keys 

This guide explains how to add and edit API keys to protect your function endpoints from unauthorized access.

## Create an API key

1. In the **Cloud** menu, go to **Functions**, select **API keys**, and click **Create now**.

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/1.png" alt="API keys for functions in the Cloud menu">

2. In **General information**, specify the API key name (required) and description (optional.)

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/2.png" alt="Fill in the general information about API keys">

3. In **Access to Functions**, specify which functions can be authenticated using the given key.

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/3.png" alt="Specify functions that can be authorized with the API key">

4. For **Expiration**, set the date until when the API key remains valid. Alternatively, if you don’t want to update your key, select **Never expire**.

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/4.png" alt="Set the expiration period for an API key">

5. Click **Create**.

6. Copy and save the key.

**Note**: You will not be able to see the key again. We do not store tokens, so the responsibility for token storage and usage rests with the issuer.

Your API key is active. From now on, anyone attempting to access your function endpoint must include a valid API key in the `X-API-Key` header. Otherwise, they will receive a 401 error.

If you’ve set the expiry date, you’ll get a notification in the customer portal before it expires.

## Change API key settings

You can change the description, expiration date, and functions that can be accessed with a given key. 

1. Go to the API key list, click the three dots next to the key you want to change, and click **Edit**.

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/5.png" alt="Edit API key settings">

2. Go to the tab you need and change the settings as follows:
- **General**: Change the key description.
- **Access to Functions**: Change the functions that can be authenticated with the key.
- **Expiration**: Reset the expiry date.

3. Click **Save**.

## Delete an API key

1. Go to the API key list, click the three dots next to the key you want to delete, and click **Delete**. 

<img src="https://assets.gcore.pro/docs/cloud/faas/authenticate-to-functions-with-api-keys/6.png" alt="Delete an API key">

2. Confirm the deletion. 

## FAQs

1. **What should I do if I forget or lose my API key?**

Delete the key in the customer portal, create a new one and add it to the function.

2. **Can I revoke an API key if it was compromised?**

If your key was compromised, delete it in the customer portal, create a new one and add it to the function.

3. **How can I check if my API key is still valid?**

Valid keys have the status “Active” in the API key list. If an API key is no longer valid, it will have the status “Expired”.
