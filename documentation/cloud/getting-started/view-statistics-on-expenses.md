---
title: view-statistics-on-expenses
displayName: Cost reports
published: true
order: 30
toc:
   --1--Cost Report: "cost-report"
   --2--Download Cost Report: "download-cost-report-data"
   --1--Reservation Cost Report: "reservation-cost-report"
   --2--Download Reservation Cost Report: "download-reservation-cost-report-data"
pageTitle: Cost reports| Gcore
pageDescription: Learn how to how to view your expenses on Gcore Edge Cloud resources.
---
# Cost reports

You can check information about Cloud resource usage and associated costs on the following pages: 

* **Cost Report**: view costs for the Cloud resources you’ve used. This report shows data based on the Pay-As-You-Go pricing model and doesn’t include any costs associated with the prepaid resources (active commit features). 
* **Reservation Cost Report**: check monthly resource usage and costs for both consumed and pre-paid resources.

You can also get reports via <a href="https://api.gcore.com/docs/cloud#tag/Cost-Reports/operation/BillingReportHandler.post" target="_blank">API</a>.

Consider that statistics for the last hour might contain incomplete data. For accuracy, we recommend reviewing cost information that was collected more than an hour ago. 

## Cost Report

<alert-element type="info" title="Info">
 
This report doesn't contain information about prepaid resources. If you have any resource reservations, check the <a href="https://gcore.com/docs/cloud/getting-started/view-statistics-on-expenses#reservation-cost-report" target="_blank">Reservation Cost Report</a> for accurate cost data. 

</alert-element>

This report contains data about each Cloud resource you’ve used, which also allows you to forecast pay-as-you-go expenses more accurately.  

You can filter the cost data by:  

* **Project**: View costs for all your projects or just the selected ones. 

* **Region**: Check costs for products created in all regions or just the selected ones. 

* **Resource type**: View costs for the selected resource types. 

* **Consumption period**: View costs for a week, two weeks, or a custom period. Consider that the maximum period you can select is one month.  

The report also contains statistics for deleted projects and regions. To include resource costs from deleted projects, select the **Show deleted projects** checkbox. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/cost-report-deleted-projects-checkbox.png" alt="Show deleted projects checkbox" width="80%">

You can also choose to add inactive projects and regions from the relevant dropdown menu:

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/projects-dropdown.png" alt="Projects dropdown expanded" width="80%">

Cost statistics is dispalyed in a graph and table format. In the graph view, the **Total** tab displays the cumulative costs associated with each Cloud resource. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/cost-report-graph.png" alt="Cost report graph with resource usage" width="80%">

You can also check more granular statistics on the following tabs:  

* Total balance used 
* Resource usage in hours 
* In Gigabyte-minutes by resources 
* In Gigabyte-seconds by resources 
* Millions of pieces
* Gigabytes of used resources  
* The total number of outbound GBs and hours of using different flavors 

Under the graphical presentation, there is a table with more detailed information about resources consumed within a selected period. The table contains the following data: 

* Resource name 
* Resource type 
* Region 
* Project 
* Usage 
* First seen date 
* Last seen date 
* Cost 

You can also use search to find the resource you need and check its usage.

### Download Cost Report data 

To export billing report for the selected period, click **Export CSV** in the top-right corner of the screen. You can download two types of files: 

* **Detailed report**: a detailed breakdown of each resource you are using. 

* **Totals**: the total cost of resources in each location.  

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/cost-report-export-csv.png" alt="Export CSV dropdown with Detailed and Total options" width="80%">

<tabset-element>

#### Detailed CSV report 

The following table describes what information is included in the **Detailed** CSV report file.  

<table>
<thead>
  <tr>
    <th style="text-align: left"><b>Column</b></th>
    <th style="text-align: left"><b>Description</b></th>
  </tr>
</thead>
<tbody>
<tr>
    <td style="text-align: left">Service</td>
    <td style="text-align: left">A name of the Cloud resource that you’ve used.</td>
</tr>
<tr>
    <td style="text-align: left">UUID</td>
    <td style="text-align: left">A universally unique identifier assigned to the resource. Some resources, like IP addresses, don't have a UUID as they’re already unique.</td>
</tr>
<tr>
    <td style="text-align: left">Feature</td>
    <td style="text-align: left">If a resource has multiple configurations (flavors), such as <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes#available-volume-types" target="_blank">different volume types</a>, it’ll be specified in this column.</td>
</tr>
<tr>
    <td style="text-align: left">Tags</td>
    <td style="text-align: left">If you added any tags to the resource, they’ll appear in this column. This column also presents system-generated tags.</td>
</tr>
<tr>
    <td style="text-align: left">Service_name</td>
    <td style="text-align: left">Name of the service, which is also displayed in the <strong>Name</strong> field in the UI. For example, name of a Virtual Machine.</td>
</tr>
<tr>
    <td style="text-align: left">Region_id</td>
    <td style="text-align: left">ID of a region where the resource has been created. You can check the ID via <a herf="https://api.gcore.com/docs/cloud#tag/Regions" target="_blank">API</a>.</td>
</tr>
<tr>
    <td style="text-align: left">Region_name</td>
    <td style="text-align: left">Name of a geographical location of the data center where the resource has been created.</td>
</tr>
<tr>
    <td style="text-align: left">Project_id</td>
    <td style="text-align: left">ID of a project where the resource has been created. Your project ID is displayed on the <strong>Projects</strong> page, in the <a href="https://gcore.com/docs/cloud/getting-started/projects/create-a-project#view-projects-in-different-layouts" target="_blank">grid view</a>.</td>
</tr>
<tr>
    <td style="text-align: left">Project_name</td>
    <td style="text-align: left">Name of a project where the resource has been created.</td>
</tr>
<tr>
    <td style="text-align: left">Period_from</td>
    <td style="text-align: left">The start date of the resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Period_to</td>
    <td style="text-align: left">The end date of the resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Units</td>
    <td style="text-align: left">The consumption measurement unit. It can be represented as the usage time, such as gbminutes, minutes, milliseconds (MLS), or as the number of consumed resources, measured in bytes or GBS.</td>
</tr>
<tr>
    <td style="text-align: left">Value</td>
    <td style="text-align: left">The numerical measurement of resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Error</td>
    <td style="text-align: left">Any errors associated with the resource usage during the specified period.</td>
</tr>
<tr>
    <td style="text-align: left">Cost</td>
    <td style="text-align: left">Cost of the resource for the specified period.</td>
</tr>
<tr>
    <td style="text-align: left">Currency</td>
    <td style="text-align: left">The type of currency in which the cost is calculated.</td>
</tr>
<tr>
    <td style="text-align: left">Attached_to</td>
    <td style="text-align: left">A Cloud product to which the resource has been connected. For instance, it can be an ID of a Virtual Machine that the volume has been attached to.</td>
</tr>
<tr>
    <td style="text-align: left">Port_id</td>
    <td style="text-align: left">A unique identifier for a network virtual port of a VM. It's used to associate IP addresses and traffic with specific network connections.</td>
</tr>
</tbody>
</table>

#### Summary CSV report 

The following table explains what information is included in the **Totals** CSV report file. 

<table>
<thead>
<tr>
    <th style="text-align: left"><b>Column</b></th>
    <th style="text-align: left"><b>Description</b></th>
</tr>
</thead>
<tbody>
<tr>
    <td style="text-align: left">Type</td>
    <td style="text-align: left">The Cloud resource that you’ve used.</td>
</tr>
<tr>
    <td style="text-align: left">Feature</td>
    <td style="text-align: left">If a resource has multiple configurations (flavors), such as <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes#available-volume-types" target="_blank">different volume types</a>, it’ll be specified in this column.</td>
</tr>
<tr>
    <td style="text-align: left">Region_id</td>
    <td style="text-align: left">ID of a region where the resource has been created. You can check the ID via <a herf="https://api.gcore.com/docs/cloud#tag/Regions" target="_blank">API</a>.</td>
</tr>
<tr>
    <td style="text-align: left">Region_name</td>
    <td style="text-align: left">Name of a geographical location of the data center where the resource has been created.</td>
</tr>
<tr>
    <td style="text-align: left">Period_from</td>
    <td style="text-align: left">The start date of the resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Period_to</td>
    <td>The end date of the resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Units</td>
    <td style="text-align: left">The consumption measurement unit. It can be represented as the usage time, such as gbminutes, minutes, milliseconds (MLS), or as the number of consumed resources, measured in bytes or GBS.</td>
</tr>
<tr>
    <td style="text-align: left">Value</td>
    <td style="text-align: left">The numerical measurement of resource usage.</td>
</tr>
<tr>
    <td style="text-align: left">Error</td>
    <td style="text-align: left">Any errors associated with the resource usage during the specified period.</td>
</tr>
<tr>
    <td style="text-align: left">Cost</td>
    <td style="text-align: left">Cost of the resource during the specified period.</td>
</tr>
<tr>
    <td style="text-align: left">Currency</td>
    <td style="text-align: left">The type of currency in which the cost is calculated.</td>
</tr>
</tbody>
</table>
</tabset-element>

## Reservation Cost Report 

This report presents information about your prepaid and <a href="https://gcore.com/docs/cloud/getting-started/resource-reservation/about-resource-reservation" target="_blank">reserved</a> resources, active commits, and costs for pay-as-you-go services.  

Contrary to the Cost Report, the Reservation Cost Report doesn't show statistics for individual resources and you can only view total data collected for each month.  

You can filter cost data by:  

* **Region**: Check costs for products created in all regions or just the selected ones. 
* **Resource type**: View costs for the selected resource types. 
* **Consumption period**: View costs for a particular month.  

The report also contains statistics for deleted projects and regions. To include costs from deleted projects, select the **Show deleted projects** checkbox. Alternatively, select inactive projects and regions from the relevant dropdown menu. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/projects-dropdown-reservation.png" alt="Projects dropdown" width="80%">

You can view cost data both as a chart or as a table, which contains more detailed information. In the chart view, the **Total** tab displays the cumulative costs associated with reserved Cloud resources. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/reservation-cost-report.png" alt="Reservation cost report graph" width="80%">

Additionally, you can check more granular information on the following tabs: 

* Total € 
* Hours 
* GB Minutes 
* Gigabyte-seconds 
* Millions 
* Gigabytes 
* Flavors, hours 
* Commit usage 

Under the chart, there is a table with a detailed report of resources consumed during the selected timeframe. 

* Resource type 
* Region 
* Commit: the number of reserved resources (active commitments) 
* Usage 
* Commit cost: fixed monthly costs for resources according to your plan.  
* Overcommit cost: costs for overuse of resources within your plan. 
* Total cost

### Download Reservation Cost Report data 

To export the billing report for the selected period, click **Export totals CSV** in the top-right corner of the screen.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/view-statistics-on-expenses/reservation-cost-report-export-csv.png" alt="Export reservation cost report button" width="80%">

The following table explains what information is included in the **Totals** file CSV report file to reserved resources. 

<table>
<thead>
<tr>
    <th style="text-align: left"><b>Column</b></th>
    <th style="text-align: left"><b>Description</b></th>
</tr>
</thead>
<tbody>
<tr>
    <td style="text-align: left">Type</td>
    <td style="text-align: left">The Cloud resource that you’ve reserved for usage.</td>
</tr>
<tr>
    <td style="text-align: left">Feature</td>
    <td style="text-align: left">If a resource has multiple configurations (flavors), such as <a href="https://gcore.com/docs/cloud/virtual-instances/volumes/about-volumes#available-volume-types" target="_blank">different volume types</a>, it’ll be specified in this column.</td>
</tr>
<tr>
    <td style="text-align: left">Region_id</td>
    <td style="text-align: left">ID of a region where the resource has been reserved. You can check the ID via <a herf="https://api.gcore.com/docs/cloud#tag/Regions" target="_blank">API</a>.</td>
</tr>
<tr>
    <td style="text-align: left">Region_name</td>
    <td style="text-align: left">Name of a geographical location of the data center where the resource has been reserved.</td>
</tr>
<tr>
    <td style="text-align: left">Period</td>
    <td style="text-align: left">The timeframe for the displayed statistics.</td>
</tr>
<tr>
    <td style="text-align: left">Units</td>
    <td style="text-align: left">The unit in which your resources are measured. It can be represented as the usage time, such as gbminutes, minutes, milliseconds (MLS), or as the number of consumed resources, measured in bytes or GBS.</td>
</tr>
<tr>
    <td style="text-align: left">Value</td>
    <td style="text-align: left">Total consumed value.</td>
</tr>
<tr>
    <td style="text-align: left">Commit value</td>
    <td style="text-align: left">Total amount of resources that have been reserved.</td>
</tr>
<tr>
    <td style="text-align: left">Commit cost</td>
    <td style="text-align: left">The cost for a reserved amount of cloud resources.</td>
</tr>
<tr>
    <td style="text-align: left">Overcommit cost</td>
    <td style="text-align: left">Additional charges incurred after the resource usage exceeded the committed (reserved) amount.</td>
</tr>
<tr>
    <td style="text-align: left">Error</td>
    <td style="text-align: left">Any errors associated with the reserved resource during the specified period.</td>
</tr>
<tr>
    <td style="text-align: left">Currency</td>
    <td style="text-align: left">The type of currency in which the cost is calculated.</td>
</tr>
</tbody>
</table>