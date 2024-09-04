---
title: troubleshoot-blocked-users
displayName: Troubleshoot blocked users
published: true
order: 20
pageTitle: A guide on troubleshooting blocked users  | Gcore
pageDescription: Learn how to troubleshoot blocked users.
---
# Troubleshoot blocked users

Use this guide to troubleshoot cases when WAAP displays a block or challenge <a href="https://gcore.com/docs/waap/response-pages" target="_blank">response page</a> to your users. 

When a user is presented with a response page, they will see the following information: 

* **Reference ID**: This ID is unique to each chain of requests that triggered a particular policy or custom rule. By using reference ID, you can search through your requests and determine why a security screen was displayed to that user. 

* **IP addres**s: IP address of the client that made the request. 

* **Date and time**: A date and time when the request was made. 

This information can also be useful for diagnostic purposes and troubleshooting. If you encounter issues with a specific page and require assistance from our support team, we recommend providing these details in your support request. 

## View and inspect requests

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**.

<img src="https://assets.gcore.pro/docs/waap/analytics/domains-waap-page.png" alt="Domains page in the Customer Portal" width="80%">

2\. Find the domain where you want to check analytics and click the domain name to open it. 

3\. In the sidebar menu, click **Analytics** > **WAAP**.

<img src="https://assets.gcore.pro/docs/waap/analytics/waap-analytics-page.png" alt="Analytics page in the Customer Portal" width="80%">

4\. In the **Requests** table, open the **Selected Field** dropdown and choose **Reference ID**. You can find the ID on the <a href="https://gcore.com/docs/waap/analytics#request-details" target="_blank">Request details</a> page.

5\. In the search field, enter the Reference ID of a request. The table will be updated to display all requests with matching reference IDs. You can use this information to find possible patterns in the incoming traffic.

<img src="https://assets.gcore.pro/docs/waap/analytics/search-requests-by-reference-id.png" alt="Requests table with search by Reference ID" width="80%">

6\. Click the request ID view detailed information about the rule and the triggered request, such as HTTP method, client IP, country of origin, user agent, and more.

This information helps you understand why a user was blocked or challenged. Thus, you can decide if the user's behavior is acceptable and they can access your domain or should remain blocked. 
After analyzing the request details, you can create WAAP rules to block or allow the user.
