---
title: create-a-fastedge-app-using-javascript-sdk
displayName: JavaScript SDK
published: true
order: 20
toc:
   --1--Overview: "overview"
   --1--Example: "basic-javascript-example"
   --1--1. Prepare Wasm: "stage-1-prepare-a-wasm-binary-file"
   --1--2. Deploy app: "stage-2-deploy-an-app"
   --1--3. Test app: "stage-3-test-an-app"
   --1--(Optional) 4. Add functions: "stage-4-optional-add-more-functionality"
pageTitle: How to Create an JS SQK App with FastEdge | Gcore 
pageDescription: How to create a Wasm binary file in JavaScript SDK and upload the app to our edge network.
---
# Create a FastEdge app using JavaScript SDK

## Overview

This guide explains how to create a FastEdge app using the JavaScript SDK. To learn more about the product, check out our <a href="https://gcore.com/docs/fastedge/getting-started" target="_blank">FastEdge overview</a> article.

<alert-element type="warning" title="Warning">

The JavaScript SDK is currently under development and remains in its beta stage.

</alert-element>

## Basic JavaScript Example

The JavaScript code to be used resembles <a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API" target="_blank">Service Worker API</a>. We have posted different examples in the <a href="https://github.com/G-Core/FastEdge-sdk-js/tree/main/docs/examples" target="_blank">Gcore repository</a>. The following basic example is used for demonstration purposes:

```
async function app(event) {
   const request = event.request;
   return new Response(`You made a request to ${request.url}`);
}
addEventListener('fetch', (event) => {
   event.respondWith(app(event));
});
```

The key point is that the callback for ```addEventListener``` must synchronously call ```event.respondWith```, which includes another callback. This secondary callback can be asynchronous, and it's typically where you would write any custom code. However, it must return a Response.

## Stage 1. Prepare a Wasm binary file

1\. Clone the FastEdge JavaScript SDK repository:

```
git clone git@github.com:G-Core/FastEdge-sdk-js.git
```

The cloned repository already includes the basic example in the ``/dist/index.js`` file for your convenience. 

2\. Navigate to the repository’s root directory:

```
cd FastEdge-sdk-js/ 
```

3\. Use the following command to take the basic example as input from ```/dist/index.js``` and create a Wasm binary as output in ```/dist/main.wasm```.

```
node ./componentize-cli.js dist/index.js dist/main.wasm 
```

## Stage 2. Deploy an app

1\. Upload the Wasm binary to our edge servers by running the <a href="https://api.gcore.com/docs/fastedge#tag/Binaries/operation/storeBinary" target="_blnk">API request</a> from the repository’s root directory.

```
curl -X 'POST' \
    'https://api.gcore.com/fastedge/v1/binaries/raw' \
    -H 'accept: application/json' \
    -H 'Authorization: APIKey <api_key>' \
    -H 'Content-Type: application/octet-stream' \
    --data-binary '@./dist/main.wasm'
```

Here, ```<api_key>``` is your permanent <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a>.

In the response, you will receive the ID of the uploaded binary (```<binary_id>```). Remember to save it, as it will be used in the next step.

2\. Create the app by running the <a href="https://api.gcore.com/docs/fastedge#tag/Apps/operation/addApp" target="_blank">API request</a>:

```
curl -X 'POST' \
   'https://api.gcore.com/fastedge/v1/apps' \
   -H 'name: <app_name>' \
   -H 'accept: application/json' \
   -H 'client_id: 0' \
   -H 'Authorization: APIKey <api_key> ' \
   -H 'Content-Type: application/json' \
   -d '{
   "binary": <binary_id>,
   "plan": "beta",
   "status": 1
}'
```

Where: 

- ```<app_name>``` is the unique name for the app 
- ```<api_key>``` is the API token
- ```<binary_id>``` is the ID of your uploaded Wasm binary

## Stage 3. Test an app

Test the app by running the curl request:

```
curl https://<app_name>.fastedge.gcore.dev/
```

Here, ```<app_name>``` is the actual name of your app assigned in the previous stage. If everything is correct, the response will be: ```You made a request to /```

## Stage 4 (Optional). Add more functionality

You can add more functionality to your app. For instance, instead of printing ```“You made a request to /”```, the app can display all request headers and set a custom response header from the environment settings.

1\. Replace the <a href="https://gcore.com/docs/fastedge/create-apps/create-a-fastedge-app-using-javascript-sdk#basic-javascript-example" target="_blank">basic example</a> in the ```dist/index.js``` with the following code to display request headers and create a custom response header:

```
import { getEnv } from 'fastedge::getenv';
async function eventHandler(event) {
   const request = event.request;
   const customEnvVariable = getEnv('MY_CUSTOM_ENV_VAR');
   const headersStr = JSON.stringify(Object.fromEntries(request.headers.entries()), null, 2);
   return new Response(`Headers: ${headersStr}\n`, {
       headers: {
           'Custom-Header': customEnvVariable,
       },
   });
}
addEventListener('fetch', (event) => {
   event.respondWith(eventHandler(event));
});
```

The application logic (e.g., location-aware redirection) assumes the use of the headers listed below. These headers may change in the future. 

2\. Compile a new Wasm binary using the command from the first stage:

```
node ./componentize-cli.js dist/index.js dist/main.wasm 
```

3\. Upload the new Wasm to the edge servers with the API request from the <a href="https://gcore.com/docs/fastedge/create-apps/create-a-fastedge-app-using-javascript-sdk#stage-2-deploy-an-app" target="_blank">second stage</a>. 

Don’t forget to save the ID of the new Wasm binary.

4\. Update the app by running the following API request:

```
curl -X 'PUT' \
 'https://api.gcore.com/fastedge/v1/apps/ <app_id> ' \
 -H 'accept: application/json' \
 -H 'Authorization: APIKey <api_key> ' \
 -H 'Content-Type: application/json' \
 -d '{
   "binary": <new_binary_id>,
   "plan": "beta",
   "status": 1,
   "name": <app_name>,
   "env": ‘{
     "MY_CUSTOM_ENV_VAR": "Custom-Header-Value"
   }
 }
```

Where:

- ```<app_name>``` is the unique name for the app
- ```<app_id>``` is the app ID
- ```<api_key>``` is the API token
- ```<binary_id>``` is the ID of your uploaded Wasm binary

5\. Test the app by running the curl request:

```
curl https://<app_name>.fastedge.gcore.dev/
```

Where ```<app_name>``` is your actual app name assigned at the previous stage. 

If everything is correct, the response will be: 

<code-block>

Headers: {
   "<span style="color:#FF5913">dc</span>": "ed",  
   "<span style="color:#FF5913">my-custom-header</span>": "Custom-Header-Value",  
   "<span style="color:#FF5913">geoip-asn</span>": "199524",  
   "<span style="color:#FF5913">geoip-lat</span>": "49.61130",  
   "<span style="color:#FF5913">geoip-long</span>": "6.12940",  
   "<span style="color:#FF5913">geoip-reg</span>": "LU",  
   "<span style="color:#FF5913">geoip-city</span>": "Luxembourg",  
   "<span style="color:#FF5913">geoip-continent</span>": "EU",  
   "<span style="color:#FF5913">geoip-country-name</span>": "Luxembourg",  
   "<span style="color:#FF5913">geoip-country-code</span>": "LU",  
   "<span style="color:#FF5913">server_addr</span>": "192.2.3.4",  
   "<span style="color:#FF5913">server_name</span>": "bear-wiggle-4732724.fastedge.gcore.dev",  
   "connection": "upgrade",  
   "x-real-ip": "1.2.3.4",  
   "x-cdn-requestor": "ed-hw-edge-preprod-gc39",  
   "<span style="color:#FF5913">x-forwarded-for</span>": "1.2.3.4",  
   "host": "fastedge.gcore.dev",  
   "x-forwarded-proto": "https",  
   "user-agent": "curl/7.81.0",  
   "cdn-loop": "nb1d2; c=11", 
   "<span style="color:#FF5913">pop-country-code</span>": "LU",  
   "<span style="color:#FF5913">pop-reg</span>": "LU",  
   "<span style="color:#FF5913">pop-country-name</span>": "Luxembourg",  
   "<span style="color:#FF5913">pop-lat</span>": "49.6113",  
   "<span style="color:#FF5913">pop-long</span>": "6.1294",  
   "<span style="color:#FF5913">pop-continent</span>": "EU",  
   "<span style="color:#FF5913">pop-city</span>": "Luxembourg",
}

</code-block>

Where:

- <span style="color:#FF5913">custom-header</span> is the added custom header
- <span style="color:#FF5913">dc</span> is the Data center
- <span style="color:#FF5913">geoip-*</span> is the client GeoIP data (e.g., asn, latitude, longitude, region, city, continent, country name and country code)
- <span style="color:#FF5913">server_addr</span> is the PoP IP address
- <span style="color:#FF5913">server_name</span> is the app hostname name
- <span style="color:#FF5913">x-forwarded-for</span> is the client IP address
- <span style="color:#FF5913">pop-*</span> is the PoP GeoIP data (e.g., asn, latitude, longitude, region, city, continent, country name and country code)