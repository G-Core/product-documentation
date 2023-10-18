---
title: generate-monthly-reports
displayName: Monthly reports
published: true
order: 80
toc:
   --1--Generating report: "generating-report"
   --2--CDN: "cdn"
   --2--Storage: "storage"
   --2--Streaming: "streaming"
   --1--Reading report: "reading-report"
   --1--Deleting report: "deleting-report"
---
# Generate monthly reports

Generate monthly reports to analyze your clients' traffic consumption.

## Generating report

Go to the "Reports" section in the Admin panel and click on the Create new report button in the upper-right corner.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/generate-monthly-reports/create-report-10.png" alt="Reports section ">

Choose the report parameters in the pop-up window.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/generate-monthly-reports/report-page-20.png" alt="report parameters " width="50%">

In the "Product" field choose a service.

In the "Features" field choose components of statistics. Based on these components, you can calculate the cost of services for your customers.

### CDN

1. CDN-HTTP/HTTPS Delivery (per GB) -total traffic.
2. CDN - HTTP/HTTPS Delivery - Bandwidth (Gbps) - bandwidth.
3. Origin Shielding - the number of shieldings (pcs.)
4. CDN - HTTP/HTTPS Upstream -  traffic from an origin source to CDN servers or from an origin source to a shield, if there is a shield. 
5. CDN - HTTP/HTTPS Sent - traffic from CDN servers to users.
6. CDN - HTTP/HTTPS Shield - traffic from a shield to CDN servers.
7. Image optimization service - the number of images transformed on the Image optimization service.
8. Raw Logs - the number of resources that used Raw Logs

### Storage

1. Used Volume (AVG) - average used volume.
2. Used Volume (MAX) - maximal used volume.
3. Data Transfer - total traffic.
4. Requests - the number of requests.

### Streaming

1. Live stream transcoding - Minutes - total time of live stream transcoding.
2. Live stream transcoding - Sream - number of active simultaneous streams
3. VOD Storage - maximal used volume for VOD

Choose one or more grouping parameters:

- by client — groups data by client ID,
- by resource — groups data by CDN-Resource ID or Storage name,
- by regions — groups data by traffic geographical region.

Specify a month and a year for which the report should be generated. 

**Note**: Due to the internal architecture of stats collection, it's best practice to generate the report for the previous month not before the 2nd day of a new month.

Click on the "Create report" button to send a report generation request. The process might take up to 15 minutes. You can see the report status in the "Reports" section in the "Status" column (the status is updated every 15 minutes):

- Generating — a report is being processed,
- Ready — a report is ready for download,
- Failed — an error occurred during the report generation.

Once the report is ready you can download it in CVS format.

## Reading report

The report represents data for a specified month, it uses commas to separate values.

There is a report example below grouped by client and region parameters.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/generate-monthly-reports/example-of-report-30.png" alt="report" width="80%">

Report's first line has the reseller's ID and company name (marked as1).

Below (marked as 2) — blocks with data for reseller's clients:

- There is a separate data block for each client in the report.
- Only those clients who have generated some traffic (or other statistical data) get included in the report.

The first line in the block is the list of headers. Others — the report data.

At the beginning of the line, there is some data about the client (Client ID, Company name). Then — about the service (Service ID, Service name), the region (Region ID, Region name), and usage (Usage, Unit).

Client ID and Company name are mentioned only in the second line. Then they are not shown.

Example of the line mentioning Client ID and Company name:

```
234,Client_one,92,CDN - HTTP/HTTPS Delivery (per GB),7,Latin America,0.0000,GB
```

Example of the line without Client ID and Company name:

```
,,92,CDN - HTTP/HTTPS Delivery (per GB),8,Middle East,0.0023,GB

```

You can look up the full description of the report parameters in the API documentation: "Get a Report in CSV" request.

## Deleting report

To delete a report, go to the "Reports" section, on the three dots in the "Actions" column, and choose "Delete".

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/generate-monthly-reports/delete-report-40.png" alt="Deleting report" width="80%">
