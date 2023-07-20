---
title: configure-rate-limiter-to-limit-the-number-of-requests
displayName: Rate Limiter
published: true
order: 51
toc:
   --1--What is Bot Protection: "what-is-bot-protection"
   --1--What is Rate Limiter: "what-is-rate-limiter"
   --1--Configure it: "configure-rate-limiter"
pageTitle: Rate Limiter | Gcore
pageDescription: A comprehensive guide on how to limit the number of requests with Rate Limiter. 
---
# Configure Rate limiter to limit the number of requests
  
## What is Bot Protection?

Bot Protection is a module that detects robotic or automated activities that mimic user activity to perform inappropriate operations such as web content and API data scraping, form submission abuse, actual user account takeover, and more. It drops the connections to clear the workflow for you to interact only with real users.

## What is Rate Limiter?

Rate Limiter is an additional feature of Bot Protection that allows you to configure restrictions and specify how many user requests can be sent to your protected resource and web application. It helps reduce the load on our network and your web application by rejecting requests that exceed the set limit.

## Configure Rate Limiter

1\. Go to the <a href="https://control.gcore.com/resources/all" target="_blank">Web Protection</a> section and open the settings of the desired resource.

<img src="https://assets.gcore.pro/docs/web-security/configure-rate-limiter-to-limit-the-number-of-requests/13532571549585.png" alt="">

2\. Open the **Bot** tab and follow the remaining steps.

<img src="https://assets.gcore.pro/docs/web-security/configure-rate-limiter-to-limit-the-number-of-requests/14901941266321.png" alt="" width="80%">

3\. Make sure that the Bot Protection is set to **Low** or **High** mode. If set to **Off** mode, the Rate Limiter feature will be inactive, and configurations will be unavailable.

4\. Enter the number of allowed requests to your <a href="https://gcore.com/docs/web-security/create-and-configure-a-protected-resource" target="_blank">protected resource</a> between 1 and 100,000 per second.

5\. Enter the number of allowed requests to the URI of your web application between 1 and 100,000 per second.

**Note**: You can also set the value to **0** in both fields, which means that there are no restrictions on the number of requests.

6\. (Optional) You can create exceptions (rules) to the default settings for certain URIs. To create a rule, click **Add Rule** and specify how many requests can be sent from one IP address to a particular URI:

- If necessary, select the method of the request (POST, GET, PUT, PATCH, or DELETE) from the list. 
- Enter the URI with a maximum of 2048 characters. You can specify a maximum of 10 URIs. 
- Specify the number of allowed requests for each URI between 1 and 100,000 per second.  

**Note**: Regular expressions are not supported in URI. The feature supports only partly match with an asterisk (*) which includes all possible nesting. 

<img src="https://assets.gcore.pro/docs/web-security/configure-rate-limiter-to-limit-the-number-of-requests/14902022060433.png" alt="" width="50%">

For example, your website address is https://test.com, and you create a rule with URI api and the limit of 2 requests per second as follows:

```
Rule:        GET   /api/*   2 
```

So this rule will be spread on all sub URLs in relation to the /api/: ```https://test.com/api/books```, ```https://test.com/api/author/123```, ```https://test.com/api/logs```, and so on.

The number of rules you can create depends on your plan:

<table>
		<thead>
			<tr>
				<th>Tariff plan</th>
				<th>The available amount of rules</th>
			</tr>
			<tr>
				<td>Trial</td>
				<td>1</td>
			</tr>
			<tr>
				<td>Start+</td>
				<td>3</td>
			</tr>
         <tr>
				<td>Pro</td>
				<td>6</td>
			</tr>
         <tr>
				<td>Custom</td>
				<td>10</td>
			</tr>
		</thead>
		<tbody>
		</tbody>
	</table>

**Note**: If the number of created rules is greater than that allowed by your plan, you will receive an error: "*Exceeded maximal amount of rate limiter rules: {amount}*".

7\. Save the changes.

After setting the Rate Limiter, if users or bots send a number of requests exceeding the set value, they will receive an HTTP 429 (Too Many Requests) response code, indicating that the Rate Limiter has restricted unwanted activity.