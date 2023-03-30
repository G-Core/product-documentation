---
title: view-statistics-of-a-cdn-resource
displayName: Reports
published: true
order: 110
toc:
   --1--Statistics: "statistics"
   --2--Advanced Analytics: "advanced-analytics"
   --2--Filters: "filters"
   --2--Report types: "report-types"
   --2--Geography: "geography"
   --2--Directories: "directories"
   --2--Browsers: "browsers"
   --2--Devices: "devices"
   --2--OS: "os"
   --2--How statistics are collected: "how-statistics-are-collected"
---
Go to the CDN service -> Reports to view reports on the CDN resources  

**_The time zone of the statistics is UTC._** 

In the Reports section there are: 

statistics for: 

*   traffic   
*   bandwidth  
*   response codes 
*   cache hit ratio  
*   requests  
*   traffic from servers in different regions 
*   traffic from countries 

advanced analytics on the requests, traffic, and unique users, grouped by:    

*   countries 
*   directories 
*   browsers 
*   devices 
*   operating systems  

**Note!** Advanced analytics is a paid option, to activate, contact us via [support@gcore.com](mailto:support@gcorelabs.com),  chat or write to your account manager.  

Statistics
==========

<img src="https://support.gcore.com/hc/article_attachments/4402761383313/_______________.png" alt="_______________.png">Statistics on traffic volume, bandwidth, response codes, cache hit ratio,  requests, traffic from servers in different regions, and traffic from the top 5 countries **_are included in the price of all tariffs._**  

Go to the CDN service-> Reports->Statistics to view basic reports.  

On the Statistics tab, you can:  

*   Select CDN resources to display statistics: one resource, several, or all resources. <img src="https://support.gcore.com/hc/article_attachments/4402753857937/____________________.png" alt="____________________.png" width="323" height="413">
*    Select the required report.

<img src="https://support.gcore.com/hc/article_attachments/4402761383057/________________________.png" alt="________________________.png">

**Note!**  The Aggregated Data report displays information on traffic volume and bandwidth for the last 3 months. The Traffic by Country report displays the top 5 countries with the highest traffic. 

*   Set a specific time interval.

<img src="https://support.gcore.com/hc/article_attachments/4402761382801/_______________________.png" alt="_______________________.png">

*   Set the report auto-refresh period.

<img src="https://support.gcore.com/hc/article_attachments/4402753857681/___________________.png" alt="___________________.png">

Advanced Analytics
------------------

Advanced analytics is a set of paid reports on requests, traffic, unique users, grouped by: 

1.  Countries
2.  Directories
3.  Browsers
4.  Devices
5.  Operating systems

You can activate all reports or only those that are required, for example, Directories and Devices. 

To activate, contact us via email [(support@gcore.com)](mailto:support@gcorelabs.com), chat, or write to your account manager.

**Please note** that after reports activation, it will take about 24 hours to collect statistics and display the data correctly. 

! Before activation of advanced analytics reports, the Advanced Analytics tab displays examples of reports with random data.

Filters
-------

<img src="https://support.gcore.com/hc/article_attachments/360015200017/____________________________.png" alt="____________________________.png">For more detailed analysis, use filters. They are applied to all available report types.

1\. Specify the resource you want to display statistics for.

<img src="https://support.gcore.com/hc/article_attachments/360015258978/__________________.png" alt="__________________.png" width="400" height="325">

2\. Select the type of advanced analytics: requests, traffic, or unique users.

<img src="https://support.gcore.com/hc/article_attachments/360015200077/__________________________.png" alt="__________________________.png" width="502" height="240">

**Please, note!**  Unique users are defined by a set of IP + user-agent parameters.

3\. Choose the period for which you want to display statistics.

<img src="https://support.gcore.com/hc/article_attachments/360015259018/_____________________________.png" alt="_____________________________.png" width="517" height="223">

4\. In the filters by country, directory, browser, device, and operating system, you can specify the parameters that will be displayed on the charts in the reports below.

<img src="https://support.gcore.com/hc/article_attachments/360015259038/________________________________.png" alt="________________________________.png">

The parameters specified in the filters influence the data displayed in all report types.

_For example_, if you select PC in the Device filter, other reports (Geography, Directories, Browsers, OS) will display data based on your choice, i.e. countries with traffic/unique users/requests from PCs or, for example, traffic/unique users/requests from browsers running from PCs.

**Please, note!**  Filters by country, directory, browser, devices, and operating systems are available depending on whether the required report type is activated or not. Filters are not available for a demo mode.

Report types
------------

**Geography**
-------------

The Geography report shows the traffic, requests, or unique users from different countries. Data is calculated based on end-user requests.

The map shows data for all world's countries.

The table below contains information collected based on the parameters specified in the filters. Here you can select the countries that will be displayed on the chart.

To quickly navigate through countries, use the search.

**Directories**
---------------

The report shows information about directories that were requested by users.

The table below contains information collected based on the parameters specified in the filters. Here you can select the directories that will be displayed on the chart.

For quick navigation, use the search.

<img src="https://support.gcore.com/hc/article_attachments/360015259078/_______________.png" alt="_______________.png">
-----------------------------------------------------------------------------------------------------------------------

**Browsers**
------------

The table below contains information collected based on the parameters specified in the filters. Here you can choose the browsers that will be displayed on the chart.

For quick navigation, use the search.

<img src="https://support.gcore.com/hc/article_attachments/360015200117/_____________.png" alt="_____________.png">**Devices**
------------------------------------------------------------------------------------------------------------------------------

The table below contains information collected based on the parameters specified in the filters. Here you can select the devices that will be displayed on the chart.

For quick navigation, use the search.

<img src="https://support.gcore.com/hc/article_attachments/360015200157/_______________.png" alt="_______________.png">**OS**
-----------------------------------------------------------------------------------------------------------------------------

The table below contains information collected based on the parameters specified in the filters. Here you can select the operating systems that will be displayed on the chart.

For quick navigation, use the search.

<img src="https://support.gcore.com/hc/article_attachments/360015259398/________________.png" alt="________________.png">

How statistics are collected 
-----------------------------

Statistics are used both for invoices and for displaying data on CDN resources in your personal account.  

There are two methods for statistics calculation. The first one is based on accuracy, which is needed to create invoices, and the second one is based on speed and relevance, which are needed to create and display reports in your personal account. 

*   **_For billing statistics and invoices,_** we use _Nginx access logs._ It is resource logs we collect, process and store. 

There are a lot of logs, which contain a large amount of data. Their processing requires time and resources, so we do not use them as real-time statistics. 

*   _**For real-time reports**_**,** we use _Nginx virtual host traffic status module._ It is a special request to get information about the current state of resources.

**Note!** The UTC time zone is used for all statistics.