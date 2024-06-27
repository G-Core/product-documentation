---
title: analytics
displayName: Analytics
published: true
order:
pageTitle: Learn about Gcore WAAP analytics | Gcore
pageDescription: Learn about Gcore analytics.
---
# Analytics

WAAP analytics provides comprehensive information about incoming traffic to your domain. It features detailed statistics about recent requests, potential threats, and frequently triggered rules, allowing you to fine-tune your WAAP settings based on the analyzed data. 

Analytics is available on the following pages:  

* **Overview**: Get a consolidated view of all incoming requests that have been inspected by WAAP. 

* **WAF**: View detailed statistics on the incoming requests and the actions enforced for those requests. 

* **DDoS attacks**: Check for recent attacks and get detailed information about each of them. 

To access analytics for your domain: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/analytics/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to check analytics and click the domain name to open it. 

3\. In the sidebar menu, click **Analytics**. 

<img src="https://assets.gcore.pro/docs/waap/analytics/analytics-page.png" alt="Analytics page in the Customer Portal">

The information on the **Analytics** page is displayed according to the selected period. At the top of the page, you can use the time frame dropdown to configure the displayed data. When you choose a new time frame, data on the graphs will automatically refresh. 

<img src="https://assets.gcore.pro/docs/waap/analytics/time-date-picker.png" alt="Time and date dropdown on the Analytics page in the Customer Portal">

## Overview  

This page features general information about incoming requests and contains two graphs: WAF and Status codes. 

### WAF

This graph shows the total number of incoming requests for the selected period and the number of requests that have been blocked. 

<img src="https://assets.gcore.pro/docs/waap/analytics/overview-waf.png" alt="WAF graph on the Analytics page in the Customer Portal">

You can print the chart or download it in the following formats: png, pdf, csv, xls. 

### Status codes

This graph shows all requests sorted according to the returned status codes: 

* 2xx: Successful 

* 3xx: Redirection 

* 4xx: Client errors 

* 5xx: Server errors  

<img src="https://assets.gcore.pro/docs/waap/analytics/overview-status-codes.png" alt="WAF graph on the Analytics page in the Customer Portal">

You can filter the graph’s data based on the origin of the request: 

* **Edge + origin**: Requests that come from the Edge (cache servers) and origin. 

* **Edge only**: Requests that come from the cache servers only. 

* O**rigin only**: Requests that come from the origin server only. 

You can print the chart in pdf format or download it in the following formats: png, pdf, csv, xls.    

## WAF 

This page features detailed statistics on HTTP requests and displays the Web application firewall requests graph and **Requests** table.

### Web Application Firewall Requests

This graph shows information about actions that were applied to incoming requests. The data is displayed in a plot chart format that gives a comprehensive overview of both good and bad requests–potential security threats detected based on a triggered rule.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-wafr.png" alt="WAF graph on the Analytics page in the Customer Portal">

You can select the following filters to view specific types of requests: 

* **Monitored requests**: total number of requests proceeded by WAAP. 

* **Policy—blocked**: View requests that were blocked because of a triggered default rule. 

* **Custom rule—blocked**: View requests that were blocked because of a triggered custom rule created in your account. 

* **DDoS L7—blocked**: View requests that were blocked because of a triggered, default rule related to DDoS. To learn more about how requests can trigger this rule, check out our Configure WAF for L7 DDoS protection guide. ❗️

* **Passed to origin**: View requests that successfully reached the origin. 

Any changes made to the WAAP requests plot are also displayed in the Requests table below the plot: 

* When you click on a particular data point on the plot, the **Requests** table is filtered accordingly. The date, time, and the corresponding traffic type are updated to show information relevant to what you’ve selected on the plot. 

* When you select a specific filter like **Policy – Blocked**, the **Requests** table is filtered to display only information that matches the same filter.  

<alert-element type="tip" title="Tip">
 
Updating filters on the table doesn’t change the data displayed on the Web Application Firewall Requests graph. 
 
</alert-element>

### Requests 

This table displays incoming requests for the past 24 hours, including good and bad ones (potential threats). Request history is retained for 30 days. 

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-requests.png" alt="WAF graph on the Analytics page in the Customer Portal">

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
<b>CAPTCHA</b>: Display requests that were presented with a Captcha screen, regardless of whether the request passed or failed the screen.<br> 
<b>Handshake (JavaScript validation)</b>: Display requests that were presented with a JavaScript validation screen, regardless of whether the request passed or failed the screen.</td>
</tr>
<tr>
<td style="text-align: left">Result</td>
<td style="text-align: left">The result of the request based on the enforced action. For example, if a request was presented with a Captcha, and the request didn’t pass, then the result is “Blocked”.</td>
</tr>
<tr>
<td style="text-align: left">Create rule</td>
<td style="text-align: left">A button that you can select to create a <a href="https://gcore.com/docs/waap/waf-rules/custom-rules" target="_blank">custom rule</a> for the request.</td>
</tr>
<tr>
<td style="text-align: left">Threats (last 24 hours)</td>
<td style="text-align: left">This section displays the most triggered actions and default rules, along with how many times each of them was triggered.</td>
</tr>
</tbody>
</table>

### Threats (last 24 hours) 

This section displays the most triggered actions and default rules, along with how many times each of them was triggered.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-threats.png" alt="WAF graph on the Analytics page in the Customer Portal">

### Top threat origins 

This map and table display the origin location of bad requests (threats) from the last 24 hours. You can view the country from which requests are coming from and the total number of requests for that country.  

<img src="https://assets.gcore.pro/docs/waap/analytics/waf-threat-origins.png" alt="WAF graph on the Analytics page in the Customer Portal">

## DDoS attacks 

We provide detailed analytics related to any DDoS attacks that were detected in your domain. DDoS analytics is stored for 32 days. 

### In-progress attacks 

If there is an active DDoS attack, you’ll see a banner at the top of the page in the Customer Portal. 

Clicking the View attack link will take you to the DDoS analytics page, where you can view more details related to that specific attack. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ddos-in-progress.png" alt="WAF graph on the Analytics page in the Customer Portal">

### Attacks over time 

Requests associated with DDoS attacks are presented in a plot format.  

To filter DDoS request data by the timeframe of each attack, click dropdown menu in the top-right corner of the screen and select the checkbox next to the attack you want to view. You can view up to four sets of timeframes simultaneously. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ddos-over-time.png" alt="WAF graph on the Analytics page in the Customer Portal">

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
<b>Allow</b>: Display requests that were allowed to pass.<br>
<b>Block</b>: Display requests that were blocked.<br>
<b>CAPTCHA</b>: Display requests that were presented with a Captcha screen, regardless of whether the request passed or failed the screen.<br> 
<b>Handshake (JavaScript validation)</b>: Display requests that were presented with a JavaScript validation screen, regardless of whether the request passed or failed the screen.</td>
</tr>
<tr>
<td style="text-align: left">Result</td>
<td style="text-align: left">The result of the request based on the enforced action. For example, if a request was presented with a Captcha, and the request didn’t pass, then the result is “Blocked”.</td>
</tr>
<tr>
<td style="text-align: left">Create rule</td>
<td style="text-align: left">A button that you can select to create a <a href="https://gcore.com/docs/waap/waf-rules/custom-rules" target="_blank">custom rule</a> for the request.</td>
</tr>
<tr>
<td style="text-align: left">Threats (last 24 hours)</td>
<td style="text-align: left">This section displays the most triggered actions and default rules, along with how many times each of them was triggered.</td>
</tr>
</tbody>
</table>

To view more details about a specific request listed in this table, click on the **Request ID**. 

### IPs participated 

This table displays a list of the top IP addresses associated with the selected DDoS attack, along with the total number of times each IP has made a request to your domain. 

<img src="https://assets.gcore.pro/docs/waap/analytics/ips-participated.png" alt="WAF graph on the Analytics page in the Customer Portal">


### Clients, tools, and user agents 

This table displays a list of the top clients, tools, and user agents associated with the selected DDoS attack. It also shows the total number of times each of them has made a request to your site. 

<img src="https://assets.gcore.pro/docs/waap/analytics/clients-tools-agents.png" alt="WAF graph on the Analytics page in the Customer Portal">

### URLs targeted 

This table displays a list of the top URLs that were requested during a DDoS attack, along with the number of times each URL was requested. 

<img src="https://assets.gcore.pro/docs/waap/analytics/urls-targeted.png" alt="WAF graph on the Analytics page in the Customer Portal">