---
title: create-fastedge-apps
displayName: Create a FastEdge app
published: true
order: 10
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

You can create a FastEdge app in two ways: from a custom binary file or a pre-configured template. If you chose the last option, skip the Stage 1. 

## Stage 1. Create a Wasm binary file

To get started, you need to create a .wasm file that you will later upload to the Gcore Customer Portal.

### Step 1. Set up the environment 

1\. Install the Rust compiler and cargo (package manager):

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

2\. Add the Wasm compilation target to Rust compiler:

```
rustup target add wasm32-wasi
```

### Step 2. Prepare directory structure and a configuration file

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
### Step 3. Create a source

For illustration, we’ll create a simple app that responds with "HTTP 200" and the text “Hello world!” in the response’s body.

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

### Step 4. Compile a Wasm file

Produce the Wasm binary:

```
cargo build --release
```

The resulting Wasm code will be written to the ```myapp/target/wasm32-wasi/release/myapp.wasm``` file.

## Stage 2. Deploy an application

<tabset-element>

### Deploy an app from a binary

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Create application**.  

2\. Click **Upload binary**.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/create-custom-app.png" alt="Create an app page with highlighted Upload binary section" width="80%">

3\. Choose your custom binary file.

4\. Click **Save binary** to upload it.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/upload-binary.png" alt="Add raw binary dialog" width="80%">

5\. Enter a name for your application and provide a description if needed.  

6\. (Optional) Add fixed headers to the responses. For example, you may include CORS (Cross-Origin Resource Sharing) headers in each response to ensure secure communication between origins.  

7\. (Optional) If you want to add metadata to the configuration, click **Add parameters** and enter metadata as key-value pairs.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/add-name-headers-metadata.png" alt="Add raw binary dialog" width="80%">

8\. In the top-right corner of the screen, click **Save and deploy**. 

Your application has been successfully deployed. You can now test its configuration and adjust it as described in the following steps.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/deployed-successfully-custom-binary.png" alt="A page with a link to an app and its configuration" width="80%">

### Deploy an app from a template

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Create application**.  

2\. In the **Launch from a template** section, select the preferred template.

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/launch-from-template.png" alt="Section with Github and Markdown templates" width="80%">

3\. Enter a name for your application and update a description if needed. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/github-add-name-description.png" alt="Open page with empty name and description fields" width="80%">

4\. Provide required environment variables for the application: 

* If you selected a GitHub template, enter the repository name and add your personal access token. 

* If you selected a Markdown template, enter the base part of the origin URL and add content from the `<head>` section of an HTML document. 

5\. (Optional) Add metadata as key-value pairs. 

6\. Click **Save and deploy**.  

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/deployed-successfully-github.png" alt="A page with a link to an app and its configuration" width="80%">

Your application has been successfully deployed. You can now test its configuration and adjust it as described in the following steps. 

</tabset-element>

## Stage 3. Test an application

You can test the application after its deployment by clicking the application link on the deployment confirmation screen: 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/test-custom-deployment.png" alt="A page with a link to an app and its configuration" width="80%">

You can also inspect and adjust the configuration from the **Dashboards** page:  

1\. In the Gcore Customer Portal, navigate to **FastEdge** > **Dashboard**. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/open-app-from-dasboard.png" alt="Metrics tab with the list of FastEdge apps" width="80%">

2\. Find the app you want to test and click its name to open it.

3\. Click the app link next to the app status to view the response. 

<img src="https://assets.gcore.pro/docs/fastedge/create-apps/test-app-from-dasboard.png" alt="A page with a link to an app" width="80%">

For example, for the application configured in the Stage 1, the response will be “Hello world!” 

## Stage 4 (Optional). Add more functionality

You can add more functionality to your app. For example, instead of printing “Hello world!”, the app can print all request headers and set a custom response header from the environment settings. Let’s see how to do that. 

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

<alert-element type="info" title="Info">
 
The headers listed in the following step are passed to the FastEdge application, which uses the header content for functionalities like geolocation-aware redirects.
 
</alert-element>


### Step 2. Compile and upload the binary file

Update the application on the edge servers:

1\. Compile a new Wasm file <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#step-4-compile-a-wasm-file" target="_blank">as described in step 4</a>.

2\. Upload it to the Customer Portal as a custom binary file. 

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
 
- <span style="color:#FF5913">custom-header</span>: Added custom header
- <span style="color:#FF5913">dc</span>: Data center
- <span style="color:#FF5913">geoip-*</span>: Client GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code
- <span style="color:#FF5913">server_addr</span>: PoP IP address
- <span style="color:#FF5913">server_name</span>: Application's hostname
- <span style="color:#FF5913">x-forwarded-for</span>: Client IP address
- <span style="color:#FF5913">pop-*</span>: PoP GeoIP data, such as asn, latitude, longitude, region, city, continent, country name, and country code

</expandable-element>

## Troubleshoot an application 

If you’re having issues with your FastEdge application, check out the following sections for helpful tips and troubleshooting suggestions.  

### HTTP status codes 

If your application is correctly configured and works as expected, FastEdge will return the expected status code like "200 OK".

However, in some exceptional situations, you might get the following status codes. Check out the description to understand the root cause and how to fix it. 

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