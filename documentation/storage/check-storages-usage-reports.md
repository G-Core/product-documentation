---
title: check-storages-usage-reports
displayName: View statistics
published: true
order: 80
toc:
pageTitle: Object Storage usage reports and statistics | Gcore
pageDescription: Instructions on where to view statistics on Object Storage resource utilization in the Gcore Customer Portal.
---
# Check storages usage reports

For storage billing we use the following metrics:

- Used space 

- Requests

- Traffic

The data for all metrics is available in the Statistics section. It can be requested for a day, two days, week, month, year, or you can choose a custom time period in the calendar on the right. The data can also be sorted by storage types (Object Storage and SFTP Storage), locations, and names.

<img src="https://assets.gcore.pro/docs/storage/check-storages-usage-reports/Screenshot_70.png" alt="Check storages usage reports" width="80%">

Statistics appear in the Gcore Customer Portal within a couple of hours after storage creation. For the S3 storages in the Global 2 location, it always comes a day later. 

On the graphs we show aggregated data: used storage space gets measured every hour, the collected data is analyzed and shown as max and average usage values for a day. The longer the requested time period the more operations has to be done to represent the data so requests for long time periods (a year, for example) can take some time to get processed.

About 350 kB of SFTP storage space is taken by system files: SSH keys, empty directories, robot.txt file. If you created a storage but haven't uploaded anything to it, the statistics will show the space taken by the system files. Keep in mind that in invoices we round the value of used space to the whole number of GB.