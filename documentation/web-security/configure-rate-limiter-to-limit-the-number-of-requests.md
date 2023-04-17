---
title: configure-rate-limiter-to-limit-the-number-of-requests
displayName: Rate Limiter (for PRO and Enterprise plans)
published: true
order: 51
toc:
   --1--What is Bot Protection: "what-is-bot-protection"
   --1--What is Rate Limiter: "what-is-rate-limiter"
   --1--Configure it: "configure-rate-limiter"
---

# Configure Rate limiter to limit the number of requests
  
## What is Bot Protection?

Bot Protection is a module that detects robotic or automated activities that mimic user activity to perform inappropriate operations such as web content and API data scraping, form submission abuse, actual user account takeover, and more. It drops the connections to clear the workflow for you to interact only with real users.

## What is Rate Limiter?

Rate Limiter is an additional feature of Bot Protection that allows you to configure restrictions and specify how many user requests can be sent to your protected resource and web application. It helps reduce the load on our network and your web application by rejecting requests that exceed the set limit.

## Configure Rate Limiter

1\. Go to the <a href="https://control.gcore.com/resources/all" target="_blank">Web Protection</a> section and open the settings of the desired resource.

<img src="https://support.gcore.com/hc/article_attachments/13532571549585" alt="">

2\. Open the **Bot** tab and follow the remaining steps.

3\. Make sure that the Bot Protection is set to **Low** or **High** mode. If set to **Off** mode, the Rate Limiter feature will be inactive, and configurations will be unavailable.

4\. Enter the number of allowed requests to your <a href="https://gcore.com/docs/web-security/create-and-configure-a-protected-resource" target="_blank">protected resource</a> between 1 and 100,000 per second.

5\. Enter the number of allowed requests to the URI of your web application between 1 and 100,000 per second.

**Note**: You can also set the value to **0** in both fields, which means that there are no restrictions on the number of requests.

6\. (Optional) You can create exceptions (rules) to the default settings for certain URIs by specifying the allowed number of requests from one IP to a particular URI:

- Select the method of the request (POST, GET, PUT, PATCH, or DELETE) from the list, if necessary.
- Enter the URI with a maximum of 2048 characters. You can specify a maximum of 10 URIs.
- Specify the number of allowed requests for each URI between 1 and 100,000 per second.

**Note**: Regular expressions are not supported in the URI. The feature only supports full match (e.g., /api/) or prefix match (e.g., /api/*).

7\. Save the changes.

After setting the Rate Limiter, if users or bots send a number of requests exceeding the set value, they will receive an HTTP 429 (Too Many Requests) response code, indicating that the Rate Limiter has restricted unwanted activity.

<img src="https://support.gcore.com/hc/article_attachments/13532718405649" alt="">