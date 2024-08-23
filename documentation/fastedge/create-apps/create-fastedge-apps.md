---
title: create-fastedge-apps
displayName: Create a FastEdge app
published: true
order: 30
toc:
--1--Stage 1. Create a Wasm binary file: "stage-1-create-a-wasm-binary-file" 
--1--Stage 2. Deploy an application: "stage-2-deploy-an-application" 
--1--Stage 3. Test an application: "stage-3-test-an-application" 
--1—-Stage 4. Add more functionality: "stage-4-add-more-functionality" 
--1—Troubleshoot an app: "troubleshoot-an-app" 
pageTitle: How to Create an Application with FastEdge | Gcore 
pageDescription: Learn how to deploy a FastEdge application from a custom binary file or from a preconfigured template.
customUrl: /fastedge/getting-started/create-fastedge-apps
---
# Create a FastEdge app 

This guide describes how to create a FastEdge app. Check out our <a href="https://gcore.com/docs/fastedge/getting-started" target="_blank">FastEdge overview</a> article to learn more about the product.

You can create a FastEdge app in two ways: from a custom binary file using <a href="https://github.com/G-Core/FastEdge-sdk-js" target="_blank">JavaScript SDK</a> or <a href="https://github.com/rust-lang/rust" target="_blank">Rust</a> as well as from a preconfigured template. If you chose the latter option, skip Stage 1. 

## Stage 1. Create a Wasm binary file

To get started, create a .wasm file that you will later upload to the Gcore Customer Portal.

<tabset-element>

### Via Rust 

#### Step 1. Set up the environment 

1\. Install the Rust compiler and cargo (package manager):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

2\. Add the Wasm compilation target to Rust compiler:

```
rustup target add wasm32-wasi
```

#### Step 2. Prepare directory structure and a configuration file

1\. Initialize the directory structure:

```
cargo new myapp --lib
```
2\. Create a directory:

```
mkdir myapp/.cargo
```

3\. Set the Wasm compilation target for the project by creating a config file ```myapp/.cargo/config.toml``` with the following content:

```
[build]
target = "wasm32-wasi"
```

4\. Create the project manifest file ```myapp/Cargo.toml``` with the following content:

```
[package]
name = "myapp"
version = "0.1.0"
edition = "2021"
 
[lib]
crate-type = ["cdylib"]
 
[dependencies]
fastedge = "0.1"
```
#### Step 3. Create a source

In this example, we’ll create a simple app that responds with "HTTP 200" and the text “Hello world!” in the response’s body.

Create a main source file src/lib.rs with the following content:

```
use fastedge::{
    body::Body,
    http::{Request, Response, StatusCode, Error},
};
 
#[fastedge::http]
fn main(_req: Request<Body>) -> Result<Response<Body>, Error> {
    Response::builder()
        .status(StatusCode::OK)
        .body(Body::from("Hello world!\n"))
}
```

#### Step 4. Compile a Wasm file

Produce the Wasm binary:

```
cargo build --release
```

The resulting Wasm code will be written to the ```myapp/target/wasm32-wasi/release/myapp.wasm``` file.

### Via JavaScript SDK

A JavaScript code pattern closely resembles <a href="https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API" target="_blank">Service Worker API</a>. You can also find multiple examples in the <a href="https://github.com/G-Core/FastEdge-sdk-js/tree/main/docs/examples" target="_blank">Gcore repository</a>. 

The key aspect of the Wasm configuration is to set up the `addEventListener` that has to synchronously call `event.respondWith` with a callback. This callback can be asynchronous and this is where you’d usually include any custom code to generate a response.

Here’s the sample configuration: 

```
async function app(event) {
   const request = event.request;
   return new Response(`You made a request to ${request.url}`);
}
addEventListener('fetch', (event) => {
   event.respondWith(app(event));
});
```

#### Step 1. Install FastEdge Javascript SDK

Run the following command `npm install --save-dev @gcoredev/fastedge-sdk-js`

#### Step 2. Create a file

Taking the sample configuration as an input `/src/input.js`, create a Wasm binary as output `/dist/main.wasm`. To do so, use the following command: `npx fastedge-build  ./src/input.js dist/main.wasm`

</tabset-element>

## Stage 2. Deploy an application

For detailed steps on how to deploy a FastEdge app, refer to the relevant sections below: 

* <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#in-the-customer-portal" target="_blank">In the Customer Portal</a>. Follow the instructions if you created a custom Wasm using either the Rust or Javascript SDK, or if you want to create a FastEdge app from a preconfigured template.

* <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#via-command-line" target="_blank">Via command line</a>: Follow the instructions if you want to deploy a custom Wasm using cURL and our API.

### In the Customer Portal

<tabset-element>

#### Deploy an app from a binary

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Create application**.  

2\. Click **Upload binary**.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/create-custom-app.png" alt="Create an app page with highlighted Upload binary section" width="80%">

3\. Choose your custom binary file.

4\. Click **Save binary** to upload it.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/upload-binary.png" alt="Add raw binary dialog" width="80%">

5\. Enter a name for your application and provide a description if needed.  

6\. (Optional) Add fixed headers to the responses. For example, you may include CORS (cross-origin resource sharing) headers in each response to ensure secure communication between origins.  

7\. (Optional) If you want to add metadata to the configuration, click **Add parameters** and enter metadata as key-value pairs.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/add-name-headers-metadata.png" alt="Add raw binary dialog" width="80%">

8\. In the top-right corner of the screen, click **Save and deploy**. 

Your application has been successfully deployed. You can now test its configuration and adjust it as described in the following steps.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/deployed-successfully-custom-binary.png" alt="A page with a link to an app and its configuration" width="80%">

#### Deploy an app from a template

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Create application**.  

2\. In the **Launch from a template** section, select the preferred template.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/launch-from-template.png" alt="Section with Github and Markdown templates" width="80%">

3\. Enter a name for your application and, optionally, update its description. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/github-add-name-description.png" alt="Open page with empty name and description fields" width="80%">

4\. Provide the required environment variables for the application: 

* If you selected a GitHub template, enter the repository name and add your personal access token. 

* If you selected a Markdown template, enter the base part of the origin URL and add content from the `<head>` section of an HTML document. 

5\. (Optional) Add metadata as key-value pairs. 

6\. Click **Save and deploy**.  

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/deployed-successfully-github.png" alt="A page with a link to an app and its configuration" width="80%">

Your application has been successfully deployed. You can now test its configuration and adjust it as described in the following steps. 

</tabset-element>

### Via command line

1\. Upload the Wasm binary to our edge servers by running the following <a href="https://api.gcore.com/docs/fastedge#tag/Binaries/operation/storeBinary" target="_blank">API request</a> from the repo’s root directory. Insert your <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">permanent API token</a> instead of the <span style="color:#FF5913">api_key</span>:

<code-block>

curl -X 'POST' \
  'https://api\.gcore\.com/fastedge/v1/binaries/raw' \
  -H 'accept: application/json' \
  -H 'Authorization: APIKey <span style="color:#FF5913">api_key</span>' \
  -H 'Content-Type: application/octet-stream' \
  --data-binary '@./dist/main.wasm'

</code-block>

In the response, you will receive the ID of the uploaded binary (`<binary_id>`). Make sure to save it, as it will be used in the following step.

2\. Create the app by running the following <a href="https://api.gcore.com/docs/fastedge#tag/Apps/operation/addApp" target="_blank">API request</a>: 

<code-block>

curl -X 'POST' \
  'https://api.gcore.com/fastedge/v1/apps' \
  -H 'name: <span style="color:#FF5913">app_name</span>' \
  -H 'accept: application/json' \
  -H 'client_id: 0' \
  -H 'Authorization: APIKey <span style="color:#FF5913">api_key</span>' \
  -H 'Content-Type: application/json' \
  -d '{
    "binary": <span style="color:#FF5913">binary_id</span>,
    "plan": "beta",
    "status": 1
}'

</code-block>

Where: 

* <span style="color:#FF5913">app_name</span> is the unique name of your app. 
* <span style="color:#FF5913">api_key</span> is your permanent API token. 
* <span style="color:#FF5913">binary_id</span> is the ID of your uploaded Wasm binary.

## Stage 3. Test an application

<tabset-element>

### In the Customer Portal

You can test the application after its deployment by clicking the application link on the deployment confirmation screen:

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/test-custom-deployment.png" alt="A page with a link to an app and its configuration" width="80%">

Additionally, you can inspect and adjust the configuration in the Customer Portal on the **Dashboards** page:  

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Dashboard**. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/open-app-from-dasboard.png" alt="Metrics tab with the list of FastEdge apps" width="80%">

2\. Find the app you want to test and click its name to open it.

3\. Click the app link next to the app status to view the response. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/test-app-from-dasboard.png" alt="A page with a link to an app" width="80%">

For example, the response for the application configured in Stage 1 will be “Hello world!” 

### Via cURL

To test the app with cURL, run the following request: `curl https://<app_name_assigned_at_the_previous_stage>.fastedge.gcore.dev/`.  

If everything is set up correctly, the response will be: “You made a request to /” 

</tabset-element>

## Stage 4 (Optional). Add more functionality

You can add more functionality to your app. For example, instead of printing “Hello world!”, the app can print all request headers and set a custom response header from the environment settings. Let’s see how to do that.

<tabset-element>

### Via Rust

#### Step 1. Change the source

To print all request headers and develop a custom response header, replace the current content of the ```myapp/src/lib.rs``` file with the following:

```
use fastedge::{
    body::Body,
    http::{Request, Response, StatusCode, Error},
};
use std::env;
 
#[fastedge::http]
fn main(req: Request<Body>) -> Result<Response<Body>, Error> {
    // print headers
    let mut body: String = "".to_string();
    for (h, v) in req.headers() {
        body.push_str(h.as_str());
        body.push_str(": ");
        match v.to_str() {
            Err(_) => body.push_str("not a valid text"),
            Ok(a) => body.push_str(a),
        }
        body.push_str("\n");
    }
 
    // get value for custom header from the env var
    let value = match env::var("CUSTOM_HEADER").ok() {
        None => return Response::builder()
                    .status(StatusCode::INTERNAL_SERVER_ERROR)
                    .body(Body::from("App misconfigured\n")),
        Some(val) => val
    };
 
    // build response with body and custom header
    Response::builder()
        .status(StatusCode::OK)
        .header("Custom-Header", value)
        .body(Body::from(body))
}
```

<alert-element type="info" title="Info">
 
The headers listed in the following step are passed to the FastEdge application, which uses the header content for functionalities like geolocation-aware redirects.
 
</alert-element>


#### Step 2. Compile and upload the binary file

Update the application on the edge servers:

1\. Compile a new Wasm file <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-4-compile-a-wasm-file" target="_blank">as described in step 4</a>.

2\. Upload it to the Gcore Customer Portal as a custom binary file. 

When you open the app, you’ll see all request headers from the environment settings. It will be similar to the following output:

<code-block>
HTTP/2 200
server: nginx
date: Thu, 19 Oct 2023 22:17:46 GMT
content-length: 616
<span style="color:#FF5913">custom-header</span>: foo                          
access-control-allow-origin: *
cache-control: no-store
x-id: ed-hw-edge-preprod-gc39
cache: MISS
accept-ranges: bytes	                                                 
<span style="color:#FF5913">dc</span>: ed                                           	
<span style="color:#FF5913">geoip-</span>asn: 7922                                       
<span style="color:#FF5913">geoip-</span>lat: 37.75580
<span style="color:#FF5913">geoip-</span>long: -121.95270
<span style="color:#FF5913">geoip-</span>reg: CA
<span style="color:#FF5913">geoip-</span>city: San Ramon
<span style="color:#FF5913">geoip-</span>continent: NA
<span style="color:#FF5913">geoip-</span>country-name: United States
<span style="color:#FF5913">geoip-</span>country-code: US
<span style="color:#FF5913">server_addr</span>: 92.223.112.26                          
<span style="color:#FF5913">server_name</span>: mistake-globe-6396.fastedge.gcore.dev	
connection: upgrade
x-real-ip: 1.2.3.4        	
<span style="color:#FF5913">x-forwarded-for</span>: 1.2.3.4                           
host: fastedge.gcore.dev
x-forwarded-proto: https
user-agent: curl/7.88.1
accept: */*
cdn-loop: nb1d2; c=11
<span style="color:#FF5913">pop-</span>long: 6.1294
<span style="color:#FF5913">pop-</span>lat: 49.6113
<span style="color:#FF5913">pop-</span>reg: LU
<span style="color:#FF5913">pop-</span>continent: EU
<span style="color:#FF5913">pop-</span>city: Luxembourg
<span style="color:#FF5913">pop-</span>country-code: LU
<span style="color:#FF5913">pop-</span>country-name: Luxembourg
</code-block>

<expandable-element title="Description of the parameters">
 
- <span style="color:#FF5913">custom-header</span>: Custom header
- <span style="color:#FF5913">dc</span>: Data center
- <span style="color:#FF5913">geoip-*</span>: Client GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code
- <span style="color:#FF5913">server_addr</span>: PoP IP address
- <span style="color:#FF5913">server_name</span>: Application hostname
- <span style="color:#FF5913">x-forwarded-for</span>: Client IP address
- <span style="color:#FF5913">pop-*</span>: PoP GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code

</expandable-element>

### Via JavaScript SDK 

You can add more functionality to your app. For example, instead of printing “You made a request to /”, the app can print all request headers and set a custom response header from the environment settings. 

#### Step 1. Print request headers and add custom response header

Replace the sample configuration in the `src/input.js` with the following code: 

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

The application logic (e.g., location-aware redirection) assumes the use of the headers listed in the following steps. The headers may change in the future.

#### Step 2. Compile a new Wasm binary

Run the command you used in the Stage 1: `npx fastegde-build ./src/input.js ./dist/main.wasm`

#### Step 3. Compile a new Wasm binary

Upload the new Wasm file to the edge servers with the same API request you executed in Stage 2: 

<code-block>

curl -X 'POST' \
  'https://api.gcore.com/fastedge/v1/binaries/raw' \
  -H 'accept: application/json' \
  -H 'Authorization: APIKey <span style="color:#FF5913">api_key</span>' \
  -H 'Content-Type: application/octet-stream' \
  --data-binary '@./dist/main.wasm'

</code-block>

Don’t forget to save the ID of the new Wasm binary, as you’ll need to use it in the following step. 

#### Step 3. Update the app

Run the following API request: 

<code-block>

curl -X 'PUT' \
  'https://api.gcore.com/fastedge/v1/apps/<span style="color:#FF5913">app_id</span>' \
  -H 'accept: application/json' \
  -H 'Authorization: APIKey <span style="color:#FF5913">api_key</span>' \
  -H 'Content-Type: application/json' \
  -d '{
    "binary": <span style="color:#FF5913">new_binary_id</span>,
    "plan": "beta",
    "status": 1,
    "name": <span style="color:#FF5913">app_name</span>,
    "env": {
      "MY_CUSTOM_ENV_VAR": "Custom-Header-Value"
    }
  }'

</code-block>

Where: 

* <span style="color:#FF5913">app_name</span> is the unique name of your app. 
* <span style="color:#FF5913">app_id</span> is the app ID.
* <span style="color:#FF5913">api_key</span> is your <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">permanent API token</a>.
* <span style="color:#FF5913">binary_id</span> is the ID of your uploaded Wasm binary.

#### Step 4. Test the app

Run the following curl request: `curl https://<app_name>.fastedge.gcore.dev/`, where `<app_name>` is the name of your application indicated in the previous step.  

If everything is updated correctly, the response will be: 

<code-block>
{
  "Headers": {
    "<span style="color:#FF5913">dc</span>": "ed",
    "<span style="color:#FF5913">my-custom-header</span>": "Custom-Header-Value",
    "<span style="color:#FF5913">geoip-</span>asn": "199524",
    "<span style="color:#FF5913">geoip-</span>lat": "49.61130",
    "<span style="color:#FF5913">geoip-</span>long": "6.12940",
    "<span style="color:#FF5913">geoip-</span>reg": "LU",
    "<span style="color:#FF5913">geoip-</span>city": "Luxembourg",
    "<span style="color:#FF5913">geoip-</span>continent": "EU",
    "<span style="color:#FF5913">geoip-</span>country-name": "Luxembourg",
    "<span style="color:#FF5913">geoip-</span>country-code": "LU",
    "<span style="color:#FF5913">server_addr</span>": "192.2.3.4",
    "<span style="color:#FF5913">server_addr</span>server_name</span>": "bear-wiggle-4732724.fastedge.gcore.dev",
    "connection": "upgrade",
    "x-real-ip": "1.2.3.4",
    "x-cdn-requestor": "ed-hw-edge-preprod-gc39",
    "<span style="color:#FF5913">server_addr</span>x-forwarded-for</span>": "1.2.3.4",
    "host": "fastedge.gcore.dev",
    "x-forwarded-proto": "https",
    "user-agent": "curl/7.81.0",
    "cdn-loop": "nb1d2; c=11",
    "<span style="color:#FF5913">server_addr</span>pop-</span>country-code": "LU",
    "<span style="color:#FF5913">server_addr</span>pop-</span>reg": "LU",
    "<span style="color:#FF5913">server_addr</span>pop-</span>country-name": "Luxembourg",
    "<span style="color:#FF5913">server_addr</span>pop-</span>lat": "49.6113",
    "<span style="color:#FF5913">server_addr</span>pop-</span>long": "6.1294",
    "<span style="color:#FF5913">server_addr</span>pop-</span>continent": "EU",
    "<span style="color:#FF5913">server_addr</span>pop-</span>city": "Luxembourg"
  }
}
</code-block>

<expandable-element title="Description of the parameters">
 
- <span style="color:#FF5913">my-custom-header</span>: Added custom header
- <span style="color:#FF5913">dc</span>: Data center
- <span style="color:#FF5913">geoip-*</span>: Client GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code
- <span style="color:#FF5913">server_addr</span>: PoP IP address
- <span style="color:#FF5913">server_name</span>: Application hostname
- <span style="color:#FF5913">x-forwarded-for</span>: Client IP address
- <span style="color:#FF5913">pop-*</span>: PoP GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code

</expandable-element>

</tabset-element>

## Troubleshoot an application 

If you’re having issues with your FastEdge application, the following sections offer helpful tips and troubleshooting suggestions.  

### HTTP status codes 

If your application is correctly configured and works as expected, FastEdge will return the expected status code, such as "200 OK."

However, in some exceptional situations, you might get the following status codes. Check the descriptions to understand the root cause. 

<table>
<thead>
  <tr>
    <th>Status code</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>530</td>
    <td>Internal FastEdge error.</td>
  </tr>
    <tr>
    <td>531</td>
    <td>Application has exceeded the allowed memory limit.</td>
  </tr>
      <tr>
    <td>532</td>
    <td>Application has timed out.</td>
  </tr>
      <tr>
    <td>533</td>
    <td>Application has crashed.</td>
  </tr>
</tbody>
</table>
