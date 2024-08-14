---
title: analytics
displayName: Analytics
published: true
order:
toc:
   --1--Overview page: "overview-page"
   --2--WAAP: "waap"
   --2--Status codes: "status-codes"
   --1--WAAP page: "waap-page"
   --2--Web Application Firewall Requests: "web-application-firewall-requests"
   --2--Requests table: "requests-table"
   --2--Threats (last 24 hours): "threats-last-24-hours"
   --2--Top threat origins: "top-threat-origins"   
   --1--DDoS attacks page: "ddos-attacks-page"   
   --2--In-progress attacks: "in-progress-attacks"   
   --2--Attacks requests: "attack-requests"   
   --2--IPs participated: "ips-participated" 
   --2--User agents: "user-agents" 
   --2--URLs targeted: "urls-targeted"                     
pageTitle: Learn about Gcore WAAP analytics | Gcore
pageDescription: Learn about Gcore analytics.
---
# Analytics

WAAP analytics provides comprehensive information about incoming traffic to your domain. It features detailed statistics about recent requests, potential threats, and frequently triggered rules, allowing you to fine-tune your WAAP settings based on the analyzed data. 

The data is displayed in Coordinated Universal Time (UTC) and available on the following pages:  

* **Overview**: Get a consolidated view of all incoming requests that have been inspected by WAAP. 

* **WAAP**: View detailed statistics on the incoming requests and the actions enforced for those requests. 

* **DDoS attacks**: Check for recent attacks and get detailed information about each of them. 

To access analytics for your domain: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/analytics/domains-waap-page.png" alt="Domains page in the Customer Portal" width="80%">

2\. Find the domain where you want to check analytics and click the domain name to open it. 

3\. In the sidebar menu, click **Analytics**. 

<img src="https://assets.gcore.pro/docs/waap/analytics/waap-analytics-page.png" alt="Analytics page in the Customer Portal" width="80%">

<alert-element type="tip" title="Tip">
 
If you want to view analytics for a different domain, use the dropdown in the top-right corner of the screen and select the needed domain.
 
</alert-element>

The information on the Analytics page is displayed according to the selected period. At the top of the page, you can use the time frame dropdown to configure the displayed data.  

To automatically refresh data without reloading the page, enable the **Auto-Refresh** toggle. 

<img src="https://assets.gcore.pro/docs/waap/analytics/auto-refresh-toggle.png" alt="Auto-refresh toggle on the Analytics page" width="80%">

## Overview page

This page features general information about incoming requests and contains two graphs: **WAAP** and **Status codes**. 

### WAAP 

This graph shows the total number of incoming requests for the selected period and the number of requests that have been blocked. 

<img src="https://assets.gcore.pro/docs/waap/analytics/overview-waap.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### Status codes

This graph shows all requests sorted according to the returned status codes: 

* 2xx: Successful 

* 3xx: Redirection 

* 4xx: Client errors 

* 5xx: Server errors  

<img src="https://assets.gcore.pro/docs/waap/analytics/overview-status-codes-graph.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

<alert-element type="info" title="Info">
 
The **Status Codes** graph only displays information from the origin's backend and doesn't include status codes from WAAP, such as 403. 
 
</alert-element>

You can print the chart in pdf format or download it in the following formats: png, pdf, csv, xls.    

## WAAP page

This page features detailed statistics on HTTP requests and displays data in the graph format (Web application firewall requests) and as a table (Requests).

### Web Application Firewall Requests

This graph shows information about actions that were applied to incoming requests. The data is displayed in a plot chart format that gives a comprehensive overview of both good and bad requests–potential security threats detected based on a triggered rule.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waap-requests.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

You can select the following filters to view specific types of requests: 

* **Monitored requests**: total number of requests proceeded by WAAP. 

* **Policy—blocked**: View requests that were blocked because of a triggered default policy. 

* **Custom rule—blocked**: View requests that were blocked because of a triggered custom rule created in your account. 

* **DDoS L7—blocked**: View requests that were blocked because of a triggered default rule related to DDoS. To learn more about how requests can trigger this rule, check out our Configure WAAP for <a href="https://gcore.com/docs/waap/ddos-protection" target="_blank">L7 DDoS protection</a> guide.

* **Passed to origin**: View requests that successfully reached the origin. 

Any changes made to the WAAP requests plot are also displayed in the **Requests** table below the plot: 

* When you click on a particular data point on the plot, the **Requests** table is filtered accordingly. The date, time, and the corresponding traffic type are updated to show information relevant to what you’ve selected on the plot. 

* When you select a specific filter like **Policy – Blocked**, the **Requests** table is filtered to display only information that matches the same filter.  

<alert-element type="tip" title="Tip">
 
Updating filters on the table doesn’t change the data displayed on the Web Application Firewall Requests graph. 
 
</alert-element>

### Requests table

This table displays incoming requests for the past 24 hours, including good and bad ones (potential threats). Request history is retained for 30 days. 

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-requests.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

You can select multiple filters to get a more granular view of the displayed information in the table.

<table>
<thead>
<tr>
<td style="text-align: left">Table column</td>
<td style="text-align: left">Description</td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">Request ID</td>
<td style="text-align: left">A unique identifier assigned to each HTTP request. Click the ID to open the <a href="https://gcore.com/docs/waap/analytics#request-details" target="_blank">Request Details</a> page, which provides comprehensive information about the request.</td>
</tr>
<tr>
<td style="text-align: left">Date</td>
<td style="text-align: left">The date and time when a rule was triggered or request occurred.</td>
</tr>
<tr>
<td style="text-align: left">IP</td>
<td style="text-align: left">The origin IP address of the client.</td>
</tr>
<tr>
<td style="text-align: left">Country</td>
<td style="text-align: left">The origin location of the IP.</td>
</tr>
<tr>
<td style="text-align: left">Response code</td>
<td style="text-align: left">HTTP code returned in response to the request.</td>
</tr>
<tr>
<td style="text-align: left">Security rule triggered</td>
<td style="text-align: left">The default or custom rule name that was triggered by the request. You can click on the rule name to view detailed information about the rule and the triggered request.</td>
</tr>
<tr>
<td style="text-align: left">Security action</td>
<td style="text-align: left">The action that was taken against the request:<br><br>
<b>Allow</b>: Display requests that were allowed to pass.<br>
<b>Block</b>: Display requests that were blocked.<br>
<b>CAPTCHA</b>: Display requests that got the CAPTCHA validation screen, regardless of whether the request passed or failed the validation.<br> 
<b>Handshake (JavaScript validation)</b>: Display requests that were presented with a JavaScript validation screen, regardless of whether the request passed or failed the screen.</td>
</tr>
<tr>
<td style="text-align: left">Result</td>
<td style="text-align: left">The result of the request based on the enforced action. For example, if a request was presented with a Captcha, and the request didn’t pass, then the result is “Blocked”.</td>
</tr>
<tr>
<td style="text-align: left">Create rule</td>
<td style="text-align: left">A button that you can select to create a <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rule</a> for the request.</td>
</tr>
<tr>
<td style="text-align: left">Threats (last 24 hours)</td>
<td style="text-align: left">This section displays the most triggered actions and default policies, along with how many times each of them was triggered.</td>
</tr>
</tbody>
</table>

You can download the table data in the CSV format. 


#### Request details

This page provides an in-depth information about a particular request made to your domain. It’s structured into three sections, each focusing on a specific aspect of the request: 

* **Overview**: Provides a high-level summary of the request, including relevant rules and applicable actions, response code, and client details. 

<img src="https://assets.gcore.pro/docs/waap/analytics/request-details-overview.png" alt="Overview section on the request details page" width="80%">

* **Additional information**: Includes a detailed overview of the client, associated organization, and device (if available).

<img src="https://assets.gcore.pro/docs/waap/analytics/request-details-extra-info.png" alt="Additional information section on the request details page" width="80%">

* **Headers**: Contains a complete list of HTTP headers included in the client request and response from the server.

<img src="https://assets.gcore.pro/docs/waap/analytics/request-details-headers.png" alt="Headers section on the request details page" width="80%">

* **Tags**: Lists any tags associated with the request, helping you quickly identify malicious activities related to that request.

<img src="https://assets.gcore.pro/docs/waap/analytics/request-details-tags.png" alt="Tags section on the request details page" width="80%">


### Threats (last 24 hours) 

This section displays the most triggered actions and default policies, along with how many times each of them was triggered.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-threats.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### Top threat origins 

This map and table display the origin location of bad requests (threats) from the last 24 hours. You can view the country from which requests are coming and the total number of requests for that country.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-threat-origins.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

## DDoS attacks page

We provide detailed analytics related to any DDoS attacks that were detected in your domain. DDoS analytics is stored for 32 days. 

### In-progress attacks 

If there is an active DDoS attack, you’ll see a banner at the top of the page in the Customer Portal. 

Clicking the **View attack** link will take you to the DDoS analytics page, where you can view more details related to that specific attack. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ddos-in-progress.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### Attacks over time 

Requests associated with DDoS attacks are presented in a plot format.  

To filter DDoS request data by the timeframe of each attack, click the dropdown menu in the top-right corner of the screen and select the checkbox next to the attack you want to view. You can view up to four sets of timeframes simultaneously. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ddos-over-time.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### Attack requests 

This table displays more fine-grained information about requests associated with attacks. You can search for specific attacks by clicking the Select field dropdown and entering an IP or response code. 

<table>
<thead>
<tr>
<td style="text-align: left">Table column</td>
<td style="text-align: left">Description</td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">Request ID</td>
<td style="text-align: left">A unique identifier assigned to each HTTP request.</td>
</tr>
<tr>
<td style="text-align: left">Date</td>
<td style="text-align: left">The date and time when a rule was triggered or request occurred.</td>
</tr>
<tr>
<td style="text-align: left">IP</td>
<td style="text-align: left">The origin IP address of the client.</td>
</tr>
<tr>
<td style="text-align: left">Response code</td>
<td style="text-align: left">HTTP code returned in response to the request.</td>
</tr>
<tr>
<td style="text-align: left">URL targeted</td>
<td style="text-align: left">Top URLs that were requested during a DDoS attack.</td>
</tr>
<tr>
<td style="text-align: left">Result</td>
<td style="text-align: left">The action that was taken against the request:<br><br>
<ul>
<li>Allow: Display requests that were allowed to pass.</li>
<li>Block: Display requests that were blocked.</li>
<li>CAPTCHA: Display requests that got the CAPTCHA validation screen, regardless of whether the request passed or failed the validation.</li>
<li>Handshake (JavaScript validation: Display requests that were presented with a JavaScript validation screen, regardless of whether the request passed or failed the screen.</li></ul></td>
</tr>
<tr>
<td style="text-align: left">Result</td>
<td style="text-align: left">The result of the request based on the enforced action. For example, if a request was presented with a Captcha, and the request didn’t pass, then the result is “Blocked”.</td>
</tr>
<tr>
<td style="text-align: left">Create rule</td>
<td style="text-align: left">A button that you can select to create a <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rule</a> for the request.</td>
</tr>
<tr>
<td style="text-align: left">Threats (last 24 hours)</td>
<td style="text-align: left">This section displays the most triggered actions and default policies, along with how many times each of them was triggered.</td>
</tr>
</tbody>
</table>

To view more details about a specific request listed in this table, click on the **Request ID**. 

### IPs participated 

This table displays a list of the top IP addresses associated with the selected DDoS attack, along with the total number of times each IP has made a request to your domain. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ips-participated.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### URLs targeted 

This table displays a list of the top URLs that were requested during a DDoS attack, along with the number of times each URL was requested. 

<img src="https://assets.gcore.pro/docs/waap/analytics/urls-targeted.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">

### User agents 

This table displays a list of the top clients, tools, and user agents associated with the selected DDoS attack. It also shows the total number of times each of them has made a request to your site. 

<img src="https://assets.gcore.pro/docs/waap/analytics/user-agents.png" alt="WAF graph on the Analytics page in the Customer Portal" width="80%">