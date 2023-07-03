---
title: view-statistics-of-a-cdn-resource
displayName: Reports
published: true
order: 110
toc:
   --1--Statistics: "statistics"
   --1--Advanced Analytics: "advanced-analytics"
   --2--Filters: "filters"
   --2--Report types: "report-types"
   --3--Geography: "geography"
   --3--Directories: "directories"
   --3--Browsers: "browsers"
   --3--Devices: "devices"
   --3--OS: "os"
   --2--How statistics are collected: "how-statistics-are-collected"
---
# View statistics of a CDN resource

## Statistics

Statistics on traffic volume, bandwidth, response codes, cache hit ratio, requests, traffic from servers in different regions, and traffic from the top 5 countries **are included in the price of all tariffs**.

To view basic reports, go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> page, and select the "Reports" section, "Statistics" tab.

In the "Statistic" tab, there are statistics data for:

- Traffic;   
- Bandwidth;  
- Response codes; 
- Cache hit ratio;  
- Requests;
- Traffic by region (it shows traffic from servers in different regions);
- Traffic by country (it shows traffic from countries);
- Image optimization. 

<img src="https://assets.gcore.pro/docs/cdn/reports/1.png" alt="">

On the Statistics tab, you can: 

- Select CDN resources to display statistics: one resource, several, or all resources. 

<img src="https://assets.gcore.pro/docs/cdn/reports/2.png" alt="" width="50%">

- Select the required report.

<img src="https://assets.gcore.pro/docs/cdn/reports/3.png" alt="" width="50%">

**Note**:  The "Aggregated Data" report displays traffic volume and bandwidth information for the last three months. The "Traffic by Country" report shows the top 5 countries with the highest traffic.

- Set a specific time interval and the report auto-refresh period.

<img src="https://assets.gcore.pro/docs/cdn/reports/4.png" alt="" width="80%"> 

The appearance of the graph and metrics depend on the characteristic on which it is based. For example, a graph depicting the usage of the Image optimization feature would look like this:

<img src="https://assets.gcore.pro/docs/cdn/reports/5.png" alt="" width="80%">

And a graph depicting the Response codes would look as follows:

<img src="https://assets.gcore.pro/docs/cdn/reports/6.png" alt="" width="80%">

## Advanced Analytics

Advanced analytics is a set of paid reports on requests, traffic, and unique users, grouped by "Countries", "Directories", "Browsers", "Devices", and "Operating systems".

**Note**: Advanced analytics is a paid option. To activate, contact us via [support@gcore.com](mailto:support@gcore.com), chat, or write to your account manager. You can start all reports or only those required, such as "Directories" and "Devices".

Before activation of advanced analytics reports, the Advanced Analytics tab displays examples of reports with random data.

**Note**: After reports activation, collecting statistics and displaying the data correctly will take about 24 hours. 

### Filters

For more detailed analysis, use filters. They are applied to all available report types.

1\. Specify the resource you want to display statistics for.

2\. Select the type of advanced analytics: requests, traffic, or unique users.

**Note**: Unique users are defined by IP + user-agent parameters.

3\. Choose the period for which you want to display statistics.

4\. In the filters by country, directory, browser, device, and operating system, you can specify the parameters displayed on the charts in the reports.

<img src="https://assets.gcore.pro/docs/cdn/reports/7.png" alt="" width="80%">

The parameters specified in the filters influence the data displayed in all report types.

For example, suppose you select "PC" in the "Device" filter. In that case, other reports (Geography, Directories, Browsers, OS) will display data based on your choice, e.g., countries with traffic/unique users/requests from PCs or traffic/unique users/requests from browsers running from PCs.

**Note**: Filters by country, directory, browser, devices, and operating systems are available depending on whether the required report type is activated. Filters are not available for a demo mode.

### Report types

#### Geography

The Geography report shows the traffic, requests, or unique users from different countries. Data is calculated based on end-user requests.

The map shows data for all world's countries.

The table below contains information collected based on the parameters specified in the filters. Here you can select the countries that will be displayed on the chart.

To quickly navigate through countries, use the search.

<img src="https://assets.gcore.pro/docs/cdn/reports/8.png" alt="" width="80%">

#### Directories

The report shows information about directories that users requested.

The table below contains information collected based on the parameters specified in the filters. Here you can select the directories that will be displayed on the chart.

For quick navigation, use the search.


#### Browsers

The table below contains information collected based on the parameters specified in the filters. Here you can choose the browsers that will be displayed on the chart.

For quick navigation, use the search.

#### Devices

The table below contains information collected based on the parameters specified in the filters. Here you can select the devices that will be displayed on the chart.

For quick navigation, use the search.

#### OS

The table below contains information collected based on the parameters specified in the filters. Here you can select the operating systems displayed on the chart.

For quick navigation, use the search.

### How statistics are collected 

Statistics are used for invoices and displaying data on CDN resources in your personal account.

There are two methods for statistics calculation. The first is based on accuracy, which is needed to create invoices, and the second is based on speed and relevance, which are needed to create and display reports in your personal account.

1\. For billing statistics and invoices, we use Nginx access logs. It is resource logs we collect, process, and store. There are a lot of logs that contain a large amount of data. Their processing requires time and resources, so we do not use them as real-time statistics.

2\. For real-time reports, we use Nginx virtual host traffic status module. It is a special request to get information about the current resources state.

**Note**: The UTC zone is used for all statistics.