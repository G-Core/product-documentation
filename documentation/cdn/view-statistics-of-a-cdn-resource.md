---
title: view-statistics-of-a-cdn-resource
displayName: Reports
published: true
order: 110
toc:
   --1--Reports overview: "reports-overview"
   --1--Statistics: "statistics"
   --1--Advanced analytics: "advanced-analytics"
   --2--Overview: "advanced-analytics-overview"
   --2--Get: "how-to-get-advanced-analytics"
   --2--Manage: "manage-advanced-analytics"
   --2--How it collects: "how-advanced-analytics-reports-are-collected"
pageTitle: CDN Statistics | Gcore
pageDescription: A comprehensive guide on how to view statistics of your CDN resource.
---
# View statistics of CDN resources

## Reports overview

Reports is a section of your control panel that displays statistics on your CDN resources. There are two tabs in the section:

- Statistics: Basic reports are available on all tariffs
- Advanced analytics: Paid option

**Note**: We recommend requesting statistics two days or more after the desired period ends to ensure you receive the most complete data. Requesting statistics immediately may result in incomplete data.

## Statistics

To view basic statistics:

1\. Go to the <a href="https://cdn.gcore.com/reports/statistics" target="_blank">Statistics</a> page. 

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-10.png" alt="Statistics" width="80%">


2\. Select the relevant resource(s) from the “CDN resource” dropdown menu to display their statistics.

3\. Select the required report:

- Aggregated data: Traffic volume and bandwidth information for the last three months
- Traffic
- Bandwidth
- Response codes
- Cache hit ratio
- Requests
- Traffic by region: Traffic from servers in different regions
- Traffic by country: Traffic from the five countries with the highest traffic
- Image optimization: Hourly count of WebP conversions
- Request time: Time elapsed in seconds between the first bytes of a request being processed and logging after the last bytes were sent to a user
- Upstream response times: Seconds to receive a response from an Origin

4\. Set a specific time interval and the report auto-refresh period.

The appearance of the graph and metrics depend on the characteristic on which it is based. For example, a graph depicting the usage of the “Image optimization” WebP conversion feature would look like this:

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-20.png" alt="Graph and metrics" width="80%">

A graph depicting the Response codes would look as follows:

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-30.png" alt="A graph depicting the Response codes" width="80%">

## Advanced analytics

### Advanced analytics overview

Advanced analytics is a set of reports on requests, traffic, and unique visitors. Data is calculated based on end-user requests. You can filter information with five filters (Countries, Directories, Browsers, Devices, and Operating systems.) 

**Note**: Advanced analytics is a paid option.

### How to get advanced analytics

To activate Advanced analytics, contact us via [support@gcore.com](mailto:support@gcore.com), <a href="https://gcore.com/" target="_blank">chat with us</a>, or write to your account manager. You can enable all filters, or opt for only those required.

After activation, it takes around 24 hours to collect statistics and display the data correctly. Before activation of advanced analytics reports, the Advanced analytics tab displays examples of reports with random data.

### Manage Advanced analytics

To view advanced reports:

1\. Go to the <a href="https://cdn.gcore.com/reports/advanced" target="_blank">Advanced analytics</a> page.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-40.png" alt="Manage Advanced analytics" width="80%">

2\. Specify the resource for which you want to display statistics.

3\. Select the type of advanced analytics: Requests, Traffic, or Unique visitors.

**Note**: Unique users are defined by IP + user-agent parameters.

4\. Choose the period for which you want to display statistics, in either UTC or your local time zone.

5\. Use filters (Geography, Directories, Browsers, Devices, OS) to get a more specific report. For example, you can set an “Android” parameter in the “OS” filter to observe only requests to your web app from users with Android.

<expandable-element title="Geography">

The report below contains information collected based on the parameters specified in the filters. For this filter, you can select which countries will be displayed on the chart.

For quick navigation, type the countries you want to view into the search bar.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-50.png" alt="Map tab" width="80%">

</expandable-element>

<expandable-element title="Directories">

The report shows information about directories that users requested. You can select which directories will be displayed on the chart.

For quick navigation, type the concrete path you want to view into the search bar.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-60.png" alt="Directories tab" width="80%">

</expandable-element>

<expandable-element title="Browsers">

The report below contains information collected based on the parameters specified in the filters. For this filter, you can choose which browsers will be displayed on the chart.

For quick navigation, use the search bar.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-70.png" alt="Browsers tab" width="80%">

</expandable-element>

<expandable-element title="Devices">

The table below contains information collected based on the parameters specified in the filters. For this filter, you can select which devices will be displayed on the chart.

For quick navigation, use the search bar.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-80.png" alt="Devices tab" width="80%">

</expandable-element>

<expandable-element title="OS">

The table below contains information collected based on the parameters specified in the filters. For this filter, you can select which operating systems will be displayed on the chart.

For quick navigation, use the search bar.

<img src="https://assets.gcore.pro/docs/cdn/reports/reports-90.png" alt="OS tab" width="80%">

</expandable-element>

### How Advanced analytics reports are collected

Statistics are used for invoices and displaying data on CDN resources in your personal account.

There are two methods for statistics calculation. 

1. **For billing statistics and invoices**: Accuracy is essential, so we use nginx access logs, which contain a large amount of data. Processing these logs necessitates considerable time and resources, which is why this method isn’t suitable for real-time statistics.
2. **For reports in your personal account**: Speed is important, so we use nginx virtual host traffic status module, which contains information about the current status of resources. We use this method to create and display reports in your personal account.

**Note**: UTC time zone is used for all statistics.