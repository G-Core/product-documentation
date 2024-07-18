---
title: integrate-cdn-with-fastedge
displayName: Integrate CDN with FastEdge
published: true
order: 25
toc:
   --1--How it works: "how-it-works"
   --1--Integrate FastEdge with CDN: "set-up-fastedge-integration-with-cdn"
   --2--Step 1. Create a FastEdge app: "step-1-create-a-fastedge-application"
   --2--Step 2. Enable FastEdge for CDN resource: "step-2-enable-fastedge-functions-for-your-cdn-resource"
   --1--Disconnect FastEdge from CDN: "disconnect-fastedge-from-cdn"
   --1--Delete CDN application in FastEdge: "delete-cdn-application-in-fastedge"               
pageTitle: Extend CDN functionality with FastEdge | Gcore
pageDescription: Learn how to extend CDN functionality by integrating it with FastEdge for advanced authentication, custom headers, and access rules.
---
# Extend CDN functionality with FastEdge 

If you need to introduce additional functionality to Gcore CDN and customize its behavior for various use cases, integrate your CDN resource with <a href="https://gcore.com/fastedge" target="_blank">FastEdge</a>.  

Such a setup allows you to extend the CDN beyond standard features and implement advanced logic for: 

* Authentication checks. Deploy FastEdge apps based on the JWT authentication template or develop a custom authentication functionality.  
* Custom headers modification. Adjust header information on requests for personalized and more secure content delivery.  
* Custom access rules. Use advanced geo-blocking and time-based blocking to control user access to your content and mitigate potential threats. 

## How it works 

Unlike traditional HTTP applications, a CDN application in FastEdge must be developed according to the <a href="https://github.com/proxy-wasm/spec" target="_blank">Proxy-Wasm (WebAssembly for Proxies)</a>. This ensures compatibility and standardization across different CDN environments. 

The application is called at the early stage of CDN processing, allowing for immediate intervention and customization. We're actively working on new interception points across the CDN workflow to cover a wide range of use cases. 

## Set up FastEdge integration with CDN

To get started, you need to have a CDN resource configured for your origin. If you don’t have Gcore CDN set up, follow the instructions from this guide: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource" target="_blank">Create a CDN resource</a>.   

### Step 1. Create a FastEdge application  

You can deploy an application from a predefined template or from a custom Wasm file. If you choose the latter option, make sure that your Wasm binary file is compliant with the <a href="https://github.com/proxy-wasm/spec" target="_blank">WebAssembly standard for proxies</a>. 

<tabset-element>

#### Deploy from the template 

Currently, you can use a predefined template to enable authentication in your application. The template is configured to verify the JSON Web Token (JWT) in the request header. 

To deploy an application from the template: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **FastEdge**. 

2\. Open the **CDN Applications** page and click **Create new application**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/cdn-applications.png" alt="Create FastEdge application button" width="80%">  

3\. In the **Create from a template** section, choose **Validate JWT in Authorization header**. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/validate-jwt.png" alt="Create from a template section with jwt validation template" width="80%">  

4\. Enter a name for your application and, optionally, update its description. 

5\. Add required environment variables—a token signing key that will be used for authentication checks.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/configure-jwt-template.png" alt="JWT template configuration menu" width="80%">  

6\. Click **Save and deploy**. 

Your application has been successfully deployed and can now be accessed through the CDN. If you need to adjust the configuration, click **Configure app**.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/app-deployed-cdn.png" alt="A page with app deployment confirmation" width="80%"> 

#### Deploy a custom CDN application 

If you want to deploy a FastEdge app from your own binary, check the examples of custom implementation in our repository: <a href="https://github.com/G-Core/FastEdge-examples" target="_blank">FastEdge app examples</a>. 

To deploy a FastEdge application from your own binary:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **FastEdge**. 

2\. Open the **CDN Applications** page and click **Create new application**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/cdn-applications.png" alt="Create FastEdge application button" width="80%">  

3\. Click **Upload binary**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/create-custom-app.png" alt="Create custom application section" width="80%">  

4\. Choose your custom binary file. 

5\. Enter a name for your application and, optionally, add a description. 

6\. Add required environment variables that will be used for authentication checks. Enter the data as key-value pairs.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/configure-custom-binary.png" alt="Custom app configuration menu" width="80%"> 

7\. Click **Save and deploy**. 

Your application has been successfully deployed and can now be accessed through the CDN. If you need to adjust the configuration, click **Configure app**. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/app-deployed-cdn-custom.png" alt="A page with app deployment confirmation" width="80%"> 

</tabset-element>

### Step 2. Enable FastEdge functions for your CDN resource 

You can enable the configured Wasm functionality either to the whole CDN resource or just to some URLs.  

<alert-element type="info" title="Info">
 
When integrating your app with CDN, note that the **Interrupt request processing in case of error** checkbox is enabled by default. This ensures that any errors on the FastEdge side will be returned to the browser with the relevant response code.  

If you disable the checkbox, CDN will ignore the error and pass requests directly to the origin. For security considerations, we recommend keeping this checkbox active. 
 
</alert-element>

<tabset-element>

#### For the whole CDN resource  

1\. In the Gcore Customer Portal, navigate to **CDN**. 

2\. Find the resource you want to integrate with FastEdge and open the resource settings.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/cdn-resource-three-dot-icon.png" alt="CDN resources page with resource settings context menu" width="80%"> 

3\. Scroll the page down to the **FastEdge apps** section and enable the toggle **On request headers**. 

Currently, we support only one event - **On request headers**, which can be used for authentication and request header manipulation before calling the origin.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/enable-fastedge-cdn-settings.png" alt="FastEdge apps section in CDN resource settings" width="80%"> 

4\. Choose your application from the dropdown. 

5\. (Optional) **Select the Interrupt request processing in case of error** checkbox.

6\. Click **Save**. 

#### For specific URL paths

You can set up a function within your uploaded FastEdge application to manage incoming request headers only for specific URLs. For example, protect some parts of your content with a JWT token, and keep the other URLs unaffected.  

To enable the function for specific URLs: 

1\. In the Gcore Customer Portal, navigate to **CDN**. 

2\. Find the resource you want to integrate with FastEdge and open the resource settings. 

3\. Click **Rules** > **Create rule**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/cdn-settings-rules-section.png" alt="CDN resource settings with open Rules tab" width="80%"> 

4\. Click **Create blank rule**.  

5\. Give your rule a name. 

6\. In the **Match criteria** section, specify the content that will be affected by the function configured in your FastEdge application. 

7\. In the **Options** section, click **Add option**. 

8\. In the options dialog, find the **FastEdge apps** section and select **On request headers**. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/rule-options-fastedge-app.png" alt="FastEdge apps section in rule options dialog" width="80%"> 

9\. Close the dialog and make sure that the **Enable on request headers** toggle is active. 

10\. Choose your FastEdge application. 

11\. (Optional) **Select the Interrupt request processing in case of error** checkbox.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/rule-options-fastedge-app-enable.png" alt="Enable FastEdge apps section in rule options dialog" width="80%"> 

12\. Click **Create rule**. 

</tabset-element>

## Disconnect FastEdge from CDN 

If you no longer need to use the functionality configured in your FastEdge application, you can disable the FastEdge functions for your CDN resource. 

The steps will slightly differ based on whether you choose to remove FastEdge from the whole CDN resource or just specific URLs. 

1\. In the Gcore Customer Portal, navigate to **CDN**.

2\. Find the resource integrated with FastEdge and open the resource settings.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/cdn-resource-three-dot-icon.png" alt="CDN resources page with resource settings context menu" width="80%"> 

3\. If you enabled FastEdge for the whole resource, disable the toggle **On request headers**. If you enabled Fast Edge just for particular paths, open the **Rules** page and 	disable the toggle for the required rule. 

4\. Click **Save changes**. 

You’ve successfully disconnected your CDN resource from FastEdge. 

## Delete CDN application in FastEdge 

<alert-element type="info" title="Info">
 
You can’t delete a Fastedge application that is enabled for a CDN resource. To remove the application, disconnect it from the CDN resource first.
 
</alert-element>

To delete an application: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **FastEdge**. 

2\. Open the **CDN Applications** page and click the three-dot icon next to the application that you want to remove.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/remove-app-fstedge.png" alt="FastEdge app settings with delete button" width="80%"> 

3\. Click **Delete**.  

4\. Confirm your action by clicking **Yes, delete**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-fastedge/confirm-deletion.png" alt="Confirm app deletion dialog" width="80%"> 

You’ve successfully removed your CDN application from Gcore FastEdge. 
