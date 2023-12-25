---
title: getting-started
displayName: FastEdge (beta)
published: true
toc:
   --1--FastEdge: "what-is-fastedge"
   --1--How it works: "how-fastedge-works"
   --1--Benefits: "key-benefits"
   --1--Use cases: "fastedge-use-cases"
   --1--Features: "fastedge-early-beta-features"
   --1--Limits: "fastedge-limits"
pageTitle: Accelerate Your Web Apps with Serverless Edge Computing | Gcore
pageDescription: Explore FastEdge Beta for low-latency, scalable edge computing, enabling quick development, enhanced security, and personalized user experiences globally.
---
# FastEdge overview

## What is FastEdge?

FastEdge is a new Gcore product, currently in beta, for serverless execution of your apps at the edge. FastEdge lets you launch your apps compiled to WebAssembly on the Gcore scalable CDN network worldwide for quick deployment. There’s no need for any environment configuration or infrastructure maintenance. 

FastEdge can be used for CDN tasks like request modification, frontend serving, image conversion, and custom DNS resolving. See the <a href="https://gcore.com/docs/fastedge/getting-started#fastedge-use-cases" target="_blank">use cases</a> section for more details.

FastEdge is currently in early beta, so it’s available free but has some restrictions. Read about this in the <a href="https://gcore.com/docs/fastedge/getting-started#fastedge-features" target="_blank">FastEdge features</a> section.

## How FastEdge works

There are two approaches to using FastEdge:

- **Without HTTP request modification**. Run select functions at the edge without modifying them. This allows for improved speed and scalability since some code requests are handled by the Edge network servers, rather than needing to arrive at the application’s web server.
- **With HTTP request and response modification**. A FastEdge node will modify HTTP requests according to your functions’ logic. Then, the modified request is sent to the application’s web server. A FastEdge node gets the web server’s HTTP response. It modifies the HTTP response according to your functions’ logic and sends it to the end user. 

For both approaches, the overall concept works in broadly similar ways: 
1. You add your code to our platform. In early beta, you can do so via API. GUI is under development. 
2. We deploy your code on the edge servers worldwide. After that, all traffic to your app is automatically routed and loadbalanced across our numerous nodes.
3. When a request is received from a user, the runtime environment executes the code and sends an HTTP response to the user.
4. FastEdge’s nodes act as origins to terminate HTTP requests, or as proxies to modify them along the way.

## Key benefits

- **Low latency everywhere**. FastEdge runs over Gcore’s global edge network, so your service will be closer to your users regardless of location, resulting in low latency.
- **Quick development**. With FastEdge, you can quickly build highly responsive and personalized apps relying heavily on dynamically generated content.
- **Built for innovation**. FastEdge lets you focus on coding and creativity, taking over all backend orchestration.
- **Enhanced security**. Each edge app runs within the WebAssembly sandbox, isolating it from other edge apps.

## FastEdge use cases

**A/B testing**. Say you’ve developed a new version of an application, but you want only a subset users to access it in order to test its performance and user satisfaction. With FastEdge’s A/B testing feature, you can set the percentage of users who will receive the new version of the site when they request your application. The logic for your split can include other parameters, such as geolocation or a specific subnet.

**Personalization**. For a global business, it’s essential to personalize content for different categories of customers. With the features in FastEdge, you can set logic based on geolocation, IP, or other HTTP request header data. You can present customers in Frankfurt with an app in German and pricing in Euros, and customers in California with English and US dollars.

**Authentication**. Imagine you’ve integrated an educational platform with paid courses with our CDN. To protect the content from unauthorized use, users who pay for a subscription are issued a JWT token. To grant access, your server must match the user’s request parameters (IP, key, validity time) with a validation key. You can bring that validation to FastEdge for faster verification thanks to the system’s distributed nature. The load on your application’s web server will be eliminated because it will only process requests from validated users.

**Image manipulation**. If you run a pay-per-load picture stock, FastEdge’s functions allow you to perform any image conversion you need, including mass converts to WebP, resizing in low resolution, and watermarks to avoid unauthorized use.

**Improved user experience**. Suppose your application uses a CMS that generates non-human-readable URLs for site sections. This can cause negative feedback from users. FastEdge allows you to convert URLs to a user-friendly option in the response upon user request. You can also cut off some undesirable custom HTTP headers in the responses. 

## FastEdge early beta features

FastEdge is in the early beta now. This means:

- Right now, code for FastEdge can be written in JS and Rust. Support for Go is in development.
- Configuration and usage statistics are available only <a href="https://api.gcore.com/docs/fast_edge" target="_blank">via API</a>. The UI is in development.
- During the early beta period, access is completely free. Pricing will be released at a later date.

**Note**: Don't use this product for mission-critical tasks or prod environments until the early beta ends.

## FastEdge limits 

> **Note**: The limits specified in this article are subject to change without prior notice. 

<table>
<thead>
<tr>
<td><b>Limit</b></td>
<td><b>Value</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">Maximum number of apps per customer</td>
<td>3</td>
</tr>
<tr>
<td style="text-align: left">Maximum number of app calls (for all your apps)<br> within one hour (from 00:00 to 59:59)</td>
<td>10,000</td>
</tr>
<tr>
<td style="text-align: left">Maximum number of app calls (for all your apps)<br> within one day (from 00:00:00 to 23:59:59 UTC)</td>
<td>100,000</td>
</tr>
<tr>
<td style="text-align: left">Maximum execution time for a single app call</td>
<td>500 ms</td>
</tr>
<tr>
<td style="text-align: left">Maximum memory use for a single app call</td>
<td>100 MB</td>
</tr>
<tr>
<td style="text-align: left">Maximum network requests from the app for a single app call</td>
<td>3</td>
</tr>
</tbody>
</table>
