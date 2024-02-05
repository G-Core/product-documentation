---
title: data-deletion
displayName: Data deletion
published: true
order: 60
toc:
   --1--Grounds for deletion: "grounds-for-product-and-data-deletion"
   --1--When deletion: "when-are-products-and-data-deleted-after-suspension"
   --1--What data will be deleted: "what-data-will-be-deleted"
pageTitle: Explore when and what Data will be Deleted | Gcore
pageDescription: An article about conditions and periods of data deletion.
---
# Data deletion

## Grounds for product and data deletion

We delete the product, its settings and associated customer data some time after the product was suspended. Products can be suspended in three cases:

1. If you <a href="https://gcore.com/docs/account-settings/billing/disable-and-resume-a-service#disable-services" target="_blank">disabled the product</a> manually.
2. After the end of the <a href="https://gcore.com/docs/account-settings/billing/trial-conditions" target="_blank">trial</a>, if you did not enable any plan.
3. After an unsuccessful payment charge attempt. 

<alert-element type="caution" title="Caution">

If at least one of your products were suspended because of an unsuccessful payment attempt, all other products in your account would be suspended, too.

</alert-element>

## When are products and data deleted after suspension?

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
Cloud 
</td>
<td>
<a href="https://gcore.com/docs/cloud/kubernetes/about-gcore-kubernetes" target="_blank">Managed Kubernetes</a>
</td>
<td rowspan="3">
0<span style="color:#FF5913">*</span>
</td>
</tr>
<tr>
<td>
<a href="https://gcore.com/docs/cloud/faas/about-function-as-a-service" target="_blank">Function as a Service</a>
</td>
</tr>
<tr>
<td>
<a href="https://gcore.com/docs/cloud/caas" target="_blank">Container as a Service</a>
</td>
</tr>
<tr>
<td>
<a href="https://gcore.com/docs/cloud/logging-as-a-service/about-logging-as-a-service" target="_blank">Managed Logging</a>
</td>
<td rowspan="2">
14 days 
</td>
</tr>
<tr>
<td>
<a href="https://gcore.com/docs/cloud/managed-database-postgresql" target="_blank">Managed Database for PostgreSQL</a> 
</td>
</tr>
<tr>
<td>
Other Cloud features (including Basic VM, Virtual Instances, Bare Metal) 
</td>
<td>
48 hours 
</td>
</tr>
<tr>
<td>
Storage 
</td>
<td>&nbsp;</td>
<td>
48 hours 
</td>
</tr>
<tr>
<td>
DNS 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
<tr>
<td>
Streaming 
</td>
<td>&nbsp;</td>
<td>
90 days 
</td>
</tr>
<tr>
<td>
Web Security 
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

<alert-element type="caution" title="Caution">

The mentioned periods are subject to change. Check the <a href="https://gcore.com/legal" target="_blank">Master Services Agreement</a> (item 16) and product specifications.

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
<td>
CDN resources, SSL certificates, created rules, and origin groups 
</td>
</tr>
<tr>
<td rowspan="5">
Cloud 
</td>
<td>
Managed Kubernetes 
</td>
<td>
Nodes with all data stored locally 
</td>
</tr>
<tr>
<td>
Function as a Service 
</td>
<td>
Created functions 
</td>
</tr>
<tr>
<td>
Container as a Service 
</td>
<td>
Created containers 
</td>
</tr>
<tr>
<td>
Managed Logging 
</td>
<td>
Logs and other data 
</td>
</tr>
<tr>
<td>
Managed Database for PostgreSQL 
</td>
<td>
Databases and other data 
</td>
</tr>
<tr>
<td>
Storage
</td>
<td>&nbsp;</td>
<td>
Storages, buckets, all files and objects 
</td>
</tr>
<tr>
<td>
DNS
</td>
<td>&nbsp;</td>
<td>
Zones and records 
</td>
</tr>
<tr>
<td>
Streaming
</td>
<td>&nbsp;</td>
<td>
CDN resources and added media 
</td>
</tr>
<tr>
<td>
Web Security
</td>
<td>&nbsp;</td>
<td>Resources under protection</td>
</tr>
<tr>
<td>
DDoS Protection
</td>
<td>&nbsp;</td>
<td>
DDoS profile 
</td>
</tr>
</tbody>
</table>