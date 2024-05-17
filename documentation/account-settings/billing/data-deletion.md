---
title: data-deletion
displayName: Data deletion
published: true
order: 60
toc:
   --1--Grounds for deletion: "grounds-for-product-and-data-deletion"
   --1--When deletion: "when-are-services-and-data-deleted-after-suspension"
   --1--What data will be deleted: "what-data-will-be-deleted"
pageTitle: Explore when and what Data will be Deleted | Gcore
pageDescription: An article about conditions and periods of data deletion.
---
# Data deletion

## Grounds for product and data deletion

We delete a service, its settings, and associated customer data after the service is suspended. The duration depends on the product; scroll down for full details.

Products can be suspended in three cases:

1. If you <a href="https://gcore.com/docs/account-settings/billing/disable-and-resume-a-service#disable-services" target="_blank">disabled the product</a> manually.
2. At the end of a <a href="https://gcore.com/docs/account-settings/billing/trial-conditions" target="_blank">Base Trial</a>, if you didn't enable a plan.
3. After an unsuccessful payment charge attempt. If one of your products is suspended because of an unsuccessful payment attempt, all other products in your account are also suspended.

## When are services and data deleted after suspension?

After a service is suspended, we don't immediately delete it and its associated <a href="https://gcore.com/docs/account-settings/billing/data-deletion#what-data-will-be-deleted" target="_blank">customer data</a>. The period between suspension and deletion depends on the product.  

After the product is suspended, some time passes before it will be deleted with all <a href="https://gcore.com/docs/account-settings/billing/data-deletion#what-data-will-be-deleted" target="_blank">customer data</a>. The period between suspension and deletion depends on the product.  

<alert-element type="warning" title="Warning">

All periods mentioned below are applied to all Gcore accounts by default. They can differ in particular cases if a personal manager or technical support changes the number of days for your account by mutual preliminary arrangement.

</alert-element>

<table>
<tr>
<td>
<strong>Product</strong>
</td>
<td>
<strong>Feature</strong>
</td>
<td>
<strong>Period after suspension</strong>
</td>
</tr>
<tr>
<td>
CDN 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
<tr>
<td rowspan="6">
Edge Cloud 
</td>
<td style="text-align: left">
<a href="https://gcore.com/docs/cloud/kubernetes/about-gcore-kubernetes" target="_blank">Managed Kubernetes</a>
</td>
<td rowspan="3">
0<span style="color:#FF5913">*</span>
</td>
</tr>
<tr>
<td style="text-align: left">
<a href="https://gcore.com/docs/cloud/faas/about-function-as-a-service" target="_blank">Function as a Service</a>
</td>
</tr>
<tr>
<td style="text-align: left">
<a href="https://gcore.com/docs/cloud/caas" target="_blank">Container as a Service</a>
</td>
</tr>
<tr>
<td style="text-align: left">
<a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">Managed Logging</a>
</td>
<td rowspan="2">
14 days 
</td>
</tr>
<tr>
<td style="text-align: left">
<a href="https://gcore.com/docs/cloud/managed-database-postgresql" target="_blank">Managed PostgreSQL</a> 
</td>
</tr>
<tr>
<td style="text-align: left">
Other Edge Cloud features (including Basic VM, Virtual Machines, Bare Metal) 
</td>
<td>
48 hours 
</td>
</tr>
<tr>
<td>
Object Storage 
</td>
<td>&nbsp;</td>
<td>
48 hours 
</td>
</tr>
<tr>
<td>
Managed DNS 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
<tr>
<td>
Video Streaming 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
<tr>
<td>
Web Application Security 
</td>
<td>&nbsp;</td>
<td>
5 days 
</td>
</tr>
<tr>
<td>
DDoS Protection 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
</table>

<span style="color:#FF5913">*</span>Data stored on worker nodes will be deleted immediately after suspension. Data stored on volumes attached to the cluster will be deleted within 48 hours.

<alert-element type="warning" title="Warning">

The durations mentioned above are applied to all Gcore accounts by default. They can differ in particular cases if a personal manager or technical support changes the number of days for your account by mutual preliminary arrangement.

The standard durations are subject to change. Check the <a href="https://gcore.com/legal" target="_blank">Master Services Agreement</a> (item 16) and product specifications.


</alert-element>

## What data will be deleted?

<table>
<tbody>
<tr>
<td>
<strong>Product</strong>
</td>
<td>
<strong>Feature</strong>
</td>
<td>
<strong>Data to be deleted</strong>
</td>
</tr>
<tr>
<td>
CDN 
</td>
<td>&nbsp;</td>
<td style="text-align: left">
CDN resources, SSL certificates, created rules, and origin groups 
</td>
</tr>
<tr>
<td rowspan="5">
Edge Cloud 
</td>
<td style="text-align: left">
Managed Kubernetes 
</td>
<td style="text-align: left">
Nodes with all data stored locally 
</td>
</tr>
<tr>
<td style="text-align: left">
Function as a Service 
</td>
<td style="text-align: left">
Created functions 
</td>
</tr>
<tr>
<td style="text-align: left">
Container as a Service 
</td>
<td style="text-align: left">
Created containers 
</td>
</tr>
<tr>
<td style="text-align: left">
Managed Logging 
</td>
<td style="text-align: left">
Logs and other data 
</td>
</tr>
<tr>
<td style="text-align: left">
Managed PostgreSQL 
</td>
<td style="text-align: left">
Databases and other data 
</td>
</tr>
<tr>
<td>
Object Storage
</td>
<td>&nbsp;</td>
<td style="text-align: left">
Storages, buckets, all files and objects 
</td>
</tr>
<tr>
<td>
Managed DNS
</td>
<td>&nbsp;</td>
<td style="text-align: left">
Zones and records 
</td>
</tr>
<tr>
<td>
Video Streaming
</td>
<td>&nbsp;</td>
<td style="text-align: left">
CDN resources and added media 
</td>
</tr>
<tr>
<td>
Web Application Security
</td>
<td>&nbsp;</td>
<td style="text-align: left">Resources under protection</td>
</tr>
<tr>
<td>
DDoS Protection
</td>
<td>&nbsp;</td>
<td style="text-align: left">
DDoS profile 
</td>
</tr>
</tbody>
</table>