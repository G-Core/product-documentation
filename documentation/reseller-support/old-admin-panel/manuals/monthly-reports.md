---
title: monthly-reports
displayName: Monthly reports
published: true
order: 90
toc:
    --1--Generating report: "generating-report"
    --2--CDN: "cdn"
    --2--Storage: "storage"
    --2--Media Platform: "media-platform"
    --1--Deleting report: "deleting-report"
---

# Monthly reports

Generate monthly reports to analyze your clients' traffic consumption.

Generating report
-----------------

Go to the Reports section in the Administrator panel and click on the Create new report button in the upper-right corner.

<img src="https://assets.gcore.pro/docs/reseller-support/old-admin-panel/manuals/monthly-reports/reports.png" alt="reports.png">

Choose the report parameters in the pop-up window.

<img src="https://assets.gcore.pro/docs/reseller-support/old-admin-panel/manuals/monthly-reports/create_report.png" alt="create_report.png" width="429" height="524">

In the Product field choose a product: CDN, Storage or Media Platform.

In the field Select a service choose components of statistics. Based on these components, you can calculate the cost of services for your customers.

### CDN

1.  _CDN-HTTP/HTTPS Delivery (per GB)_ -total traffic.
2.  _CDN - HTTP/HTTPS Delivery - Bandwidth (Gbps)_ - bandwidth.
3.  _Origin Shielding_ - the number of shieldings (pcs.)
4.  _CDN - HTTP/HTTPS Upstream_ -  traffic from an origin source to CDN servers or  
    from an origin source to a shield, if there is a shield. 
5.  _CDN - HTTP/HTTPS Sent_ - traffic from CDN servers to users.
6.  _CDN - HTTP/HTTPS Shield_ - traffic from a shield to CDN servers.

### Storage

1.  _Used Volume (AVG)_ - average used volume.
2.  _Used Volume (MAX)_ - maximal used volume.
3.  _Data Transfer_ - total traffic.
4.  _Requests_ - the number of requests.

### Media Platform

1.  _Live stream transcoding - Minutes -_ total time of live stream transcoding.
2.  _VOD Storage_ -maximal used volume for VOD

Choose one or more grouping parameters:

*   by client — groups data by client ID,
*   by resource — groups data by CDN-Resource ID or Storage name,
*   by regions — groups data by traffic geographical region (available only for CDN, read more about regions in the [CDN tab](https://reseller.gcorelabs.com/hc/en-us/articles/115005740089-CDN-Tab) article).

Specify a month and a year for which the report should be generated. Due to the internal architecture of stats collection it's best practice to generate the report for the previous month not before the 2nd day of a new month.

Click on the "Create report" button to send a report generation request. The process might take up to 15 minutes. You can see the report status in the "Reports" section in the "Status" column (the status is updated every 15 minutes):

*   Generating — a report is being processed,
*   Ready — a report is ready for download,
*   Failed — an error occurred during the report generation.

Once the report is ready you can download it in CVS format.

Reading report
--------------

The report represents data for a specified month, it uses commas to separate values.

There is a report example below grouped by client and region parameters.

<img src="https://assets.gcore.pro/docs/reseller-support/old-admin-panel/manuals/monthly-reports/1571903258576.png" alt="1571903258576.png">

Report's first line has the reseller's ID and company name (marked as1).

Below (marked as 2) — blocks with data for reseller's clients:

*   There is a separate data block for each client in the report.
*   Only those clients who have generated some traffic (or other statistical data) get included in the report.

The first line in the block is the list of headers. Others — the report data.

At the beginning of the line, there is some data about the client (Client ID, Company name). Then — about the service (Service ID, Service name), the region (Region ID, Region name), and usage (Usage, Unit).

Client ID and Company name are mentioned only in the second line. Then they are not shown.

Example of the line mentioning Client ID and Company name:

234,Client\_one,92,CDN - HTTP/HTTPS Delivery (per GB),7,Latin America,0.0000,GB

Example of the line without Client ID and Company name:

,,92,CDN - HTTP/HTTPS Delivery (per GB),8,Middle East,0.0023,GB

You can look up the full description of the report parameters in the [API documentation](https://reseller.gcorelabs.com/hc/ru/articles/115005838145): "Get a Report in CSV" request.

Deleting report
---------------

To delete a report, go to the "Reports" section, click on the arrow near the "Download" button and choose "Delete".

<img src="https://assets.gcore.pro/docs/reseller-support/old-admin-panel/manuals/monthly-reports/1571907287407.png" alt="1571907287407.png">