---
title: ddos-protection
displayName: L7 DDoS protection
published: true
order:
pageTitle: A guide on Gcore L7 DDoS protection | Gcore
pageDescription: Learn about L7 DDoS protection measures, when DDoS protection mode gets activated, and how it works.
---
# L7 DDoS protection

We offer protection for your web applications, websites, and APIs from DDoS attacks at the <a href="https://osi-model.com/application-layer/" target="_blank">application layer</a> (layer 7) in the OSI model. These attacks are often performed in bursts and aren’t always volumetric in nature.  

DDoS protection is always enabled, even if WAAP is in <a href="https://gcore.com/docs/waap/getting-started/waap-modes#monitor-mode" target="_blank">monitor mode</a>. Once a DDoS attack is identified, the system activates a DDoS mode. 

<alert-element type="tip" title="Tip">
 
The DDoS attack statistics and other related data are available on the <a href="https://gcore.com/docs/waap/analytics#ddos-attacks-page" target="_blank">DDoS attacks</a> analytics page.
 
</alert-element>

## When DDoS mode is activated 

DDoS mode is activated if any of the following conditions is met.  

<table>
<thead>
<tr>
    <th style="text-align: left;">Condition</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Threshold values</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;">
    <td>Global threshold</td>
    <td>This mechanism identifies DDoS attacks whose traffic patterns consist of a slow rise in traffic over a set period of time.<br><br>
    <strong>DDoS mode is activated</strong> when the customizable threshold value is met, AND the current number of requests is at least two times (2X) the previous 10-second window. 
    </td>
    <td><ul><strong>Default</strong>:
    <li>This mechanism has a default DDoS threshold of 5000 requests per 10 seconds.</li></ul>
    <ul><strong>Minimum</strong>:
    <li>This mechanism has a minimum DDoS threshold of 250 requests per 10 seconds.</li></ul>
    <ul><strong>Maximum</strong>:
    <li>This mechanism has a maximum threshold of 10,000 requests per 10 seconds.</li></ul>
    </td>
</tr>
<tr style="text-align: left;">
    <td>Burst threshold</td>
    <td>This mechanism identifies sudden bursts in traffic.<br><br>
    <strong>DDoS mode is activated</strong> when the customizable threshold value is met, AND the number of requests is at least five times (5X) the last 2-second interval.
    </td>
    <td><ul><strong>Default</strong>:
    <li>This mechanism has a default value of 500 requests per 2 seconds.</li></ul>
    <ul><strong>Minimum</strong>:
    <li>This mechanism has a minimum DDoS threshold of 30 requests per 2 seconds.</li></ul>
    <ul><strong>Maximum</strong>:
    <li>This mechanism has a maximum threshold of 1,000 requests per 2 seconds.</li></ul>
    </td>
</tr>
<tr style="text-align: left;">
    <td>Sub-second threshold</td>
    <td>This threshold protects WAAP servers against attacks from traffic bursts.<br><br>
   When this threshold is reached, the DDoS mode will activate on the affected WAAP server (not the WAAP cluster).
    </td>
    <td><ul><strong>Default</strong>:
    <li>This mechanism has a default value of 50 seconds.</li>
    <li>By default, StackPath maintains this threshold.</li>
 </ul>
    </td>
</tr>
</tbody>
</table>

<alert-element type="info" title="Info">
 
If you’re using WAAP <a href="https://gcore.com/docs/waap/billing#pro" target="_blank">Pro</a> or <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise</a> plan, you can adjust the threshold values. Contact [our support team](mailto:support@gcore.com) for assistance.
 
</alert-element>

## What happens when DDoS mode is activated

* Every request is challenged with JavaScript validation. This challenge detects if a valid user and not an automated tool is making the request. If a user passes the validation, they will not be challenged on future requests. 

* DDoS mode will be active for a minimum duration of 10 minutes and then for the duration of the attack. 

* Any automated layer traffic is blocked. This action won’t be applied to large search engines, such as Google or Bing. 

* WAAP’s bot-detection technology will block bots that share IP addresses with human users or frequently change their IP addresses. 

* WAAP DDoS protection uses an AI-driven IP filtering profiler that analyzes daily traffic patterns from known users. This helps the system distinguish normal traffic from traffic that might be part of a DDoS attack.

As an additional protection measure, we recommend manually adding your API endpoints to the <a href="" target="_blank">API base path</a>. This will enhance the system's ability to protect your endpoints and reduce the likelihood of false positives. 