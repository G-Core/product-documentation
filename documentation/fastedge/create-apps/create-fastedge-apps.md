---
title: create-fastedge-apps
displayName: Rust
published: true
order: 10
toc:
   --1--Stage 1. Create a Wasm binary: "stage-1-create-a-wasm-binary-file"
   --2--Step 1. Set up the environment: "step-1-set-up-the-environment"
   --2--Step 2. Prepare structure and config: "step-2-prepare-directory-structure-and-a-config-file" 
   --2--Step 3. Create a source: "step-3-create-a-source"
   --2--Step 4. Compile: "step-4-compile" 
   --1--Stage 2. Deploy an app: "stage-2-deploy-an-app"
   --2--Step 1. Upload the binary: "step-1-upload-the-binary"
   --2--Step 2. Add a new app: "step-2-add-a-new-app"
   --1--Stage 3. Test an app: "stage-3-test-an-app"
   --1--Stage 4 (Optional). Add functionality: "stage-4-optional-add-more-functionality"
   --2--Step 1. Change the source: "step-1-change-the-source"
   --2--Step 2. Compile and upload binary: "step-2-compile-and-upload-the-binary-file"
   --2--Step 3. Update the app: "step-3-update-the-app"
   --2--Step 4. Test an app: "step-4-test-an-app"
pageTitle: How to Create an Rust App with FastEdge | Gcore 
pageDescription: How to create a Wasm binary file in Rust and upload the app to our edge network.
customUrl: /fastedge/getting-started/create-fastedge-apps
---
# Create a FastEdge app using Rust

This guide describes how to create a FastEdge app. Check out our <a href="https://gcore.com/docs/fastedge/getting-started" target="_blank">FastEdge overview</a> article to learn more about the product.

**Note**: Currently, FastEdge is in early beta.

## Stage 1. Create a Wasm binary file

### Step 1. Set up the environment 

1\. Connect to your server.

2\. Clone the FastEdge SDK to your local directory:

```
git clone git@github.com:G-Core/FastEdgeSDK.git --recurse-submodules 
```

3\. Install the Rust compiler and cargo (package manager):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

4\. Add the Wasm compilation target to Rust compiler:

```
rustup target add wasm32-wasi
```

### Step 2. Prepare directory structure and a config file

**Note**: We assume here that the app will be in ```myapp``` directory, located on the same level as the FastEdgeSDK directory, where the cloned SDK is located.

1\. Initialize the directory structure:

```
cargo new myapp --lib
```
2. Create a directory:

```
mkdir myapp/.cargo
```

3\. Set the Wasm compilation target for the project by creating a config file ```myapp/.cargo/config.toml``` with the following content:

```
[build]
target = "wasm32-wasi"
```

4\. Create a project manifest file ```myapp/Cargo.toml``` with the following content:

```
[package]
name = "myapp"
version = "0.1.0"
edition = "2021"
 
[lib]
crate-type = ["cdylib"]
 
[dependencies]
# relative path to SDK
fastedge = {path="../FastEdgeSDK/fastedge-rust-sdk/"}
```
### Step 3. Create a source

For illustration, we’ll create a simple sample app that responds with HTTP 200 and the text “*Hello world!*” in the response’s body.

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

### Step 4. Compile

Produce the Wasm binary:

```
cargo build --release
```

The resulting Wasm code will be written in ```myapp/target/wasm32-wasi/release/myapp.wasm``` file.

## Stage 2. Deploy an app

Since FastEdge is available in beta, it doesn’t yet have a UI. Therefore, you can only add an application to Edge servers when accessing endpoints via API requests—see the <a href="https://api.gcore.com/docs/fast_edge" target="_blank">API documentation</a> for more details. To send API requests, use a permanent API token; learn more about this in our <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">dedicated guide</a> 

### Step 1. Upload the binary

Execute the API request from the ```myapp``` directory to upload the created Wasm binary file to our edge servers: 

```
 myapp % curl -X 'POST' \
    'https://api.gcore.com/fastedge/v1/binaries/raw' \
    -H 'accept: application/json' \
    -H 'Authorization: APIKey <api_key>' \
    -H 'Content-Type: application/octet-stream' \
    --data-binary '@target/wasm32-wasi/release/myapp.wasm'
```

<alert-element type="note" title="Note">

Replace ```<api_key>``` with actual value.

</alert-element>

For more details, read the <a href="https://api.gcore.com/docs/fast_edge#tag/Binaries/operation/storeBinary" target="_blank">API documentation</a>.

After executing the request, you will get the ID binary. Save it; you’ll need it in the next step.

### Step 2. Add a new app

Execute the following API request to create the app:

```
curl -X 'POST' \
    'https://api.gcore.com/fastedge/v1/apps' \
    -H 'name: <app_name>' \
    -H 'accept: application/json' \
    -H 'client_id: 0' \
    -H 'Authorization: APIKey <api_key>' \
    -H 'Content-Type: application/json' \
    -d '{
    "binary": <binary_id>,
    "plan": "beta",
    "status": 1
}'
```

**Note**: Replace ```<app_name>``` (use the unique one), ```<api_key>``` and ```<binary_id>``` with actual values.

<expandable-element title="Available plans">

**Note**: The “plan” field contains the name of the plan. The plan includes the limits for the application, such as maximum execution duration and maximum used memory. To get the list of available plans, execute the special <a href="https://api.gcore.com/docs/fast_edge#tag/Plans/operation/listPlans" target="_blank">API request</a>. To get the plan details, use the following <a href="https://api.gcore.com/docs/fast_edge#tag/Plans/operation/getPlan" target="_blank">API request</a>. For more information, read the <a href="https://api.gcore.com/docs/fast_edge#tag/Apps/operation/addApp" target="_blank">API documentation</a>.
 
You will get a response similar to this:

```
{
  "id": 19,
  "name": "app_name"
}
```

</expandable-element>

**Note**: If you don’t specify the “name” field in the API request, it will be auto-generated.

Save the app’s ID; it will be helpful in the future if you need to make changes to the app.  

## Stage 3. Test an app

To test the app, run the following request:

```
curl https://<app_name>.fastedge.gcore.dev/ 
```
Replace ```<app_name>``` in the URL with the actual app name returned in the <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-2-add-a-new-app" target="_blank">previous step</a>.
The response will be “Hello world!”

## Stage 4 (Optional). Add more functionality

You can add more functionality to your app. For example, instead of printing “Hello world!” the app can print all request headers and set a custom response header from the environment settings. Let’s see how to do that.

### Step 1. Change the source

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

**Note**: Printed headers are available for the app so that the app has logic based on these headers, such as location-aware redirects. Please note that the list of headers may change in the future.


### Step 2. Compile and upload the binary file

Prepare to update the application on edge servers. To do this, compile a new Wasm file with the <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-4-compile" target="_blank">previous instructions</a> and upload it to the edge <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-1-upload-the-binary" target="_blank">using these instructions</a>.   

**Note**: Save the ID of the new binary.

### Step 3. Update the app

Execute the following request to update the app:

```
curl -X 'PUT' \
  'https://api.gcore.com/fastedge/v1/apps/<app_id>' \
  -H 'accept: application/json' \
  -H 'Authorization: APIKey <api_key>' \
  -H 'Content-Type: application/json' \
  -d '{
  "binary": <new_binary_id>,
  "plan": "beta",
  "status": 1,
  "name": <app_name>,
  "env": {
    "CUSTOM_HEADER": "foo"
  }
}'
```

Note: Replace ```<api_key>```, ```<app_id>```, ```<app_name>``` and ```<new_binary_id>``` with actual values.

For more information, read the <a href="https://api.gcore.com/docs/fast_edge#tag/Apps/operation/updateApp" target="_blank">API documentation</a>.

### Step 4. Test an app

To test the new data of the app, run the following request:

```
curl https://<app_name>.fastedge.gcore.dev/ 
```

Replace ```<app_name>``` in the URL with the actual app name returned in the <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-3-update-the-app" target="_blank">previous step</a>.

You will get the content similar to the following:

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

Where:

- <span style="color:#FF5913">custom-header</span> is the added custom header
- <span style="color:#FF5913">dc</span> is the Data center
- <span style="color:#FF5913">geoip-*</span> is the client GeoIP data (e.g., asn, latitude, longitude, region, city, continent, country name and country code)
- <span style="color:#FF5913">server_addr</span> is the PoP IP address
- <span style="color:#FF5913">server_name</span> is the app hostname name
- <span style="color:#FF5913">x-forwarded-for</span> is the client IP address
- <span style="color:#FF5913">pop-*</span> is the PoP GeoIP data (e.g., asn, latitude, longitude, region, city, continent, country name and country code)