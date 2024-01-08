---
title: disable-and-resume-a-service
displayName: Disable/Resume
published: true
order: 20
toc:
   --1--Disable: "disable-services"
   --2--Deletion periods: "when-are-services-and-resources-deleted"
   --1--Resume: "resume-services"
pageTitle: Instructions on How to Disable or Resume Products | Gcore
pageDescription: A step-by-step guide to disable or resume products. Disabling deletes certain resources and settings after a set period.
---
# How to disable or resume services
  
## Disable services

1\. Open the <a href="https://accounts.gcore.com/billing/services" target="_blank">Services</a> page.

2\. Find the service you want to disable, dropdown the service block and click **Disable service**.

<img src="https://assets.gcore.pro/docs/account-settings/billing/services/disable-10.png" alt="Disable a service">

**Note:** After disabling, the service will continue working till the date specified in the Customer Portal. Then, it will be suspended, and you won't be able to use the service. Some time after the suspension, the service and its data (associated resources and settings) will be deleted.

### When are services and resources deleted?

<expandable-element title="What data will be deleted"> 

- **CDN:** CDN resources, SSL certificates, created rules, origin groups; all paid and free features will be turned off
- **Cloud:** VMs with all settings and projects
- **Storage:** storages
- **DNS:** zones, records
- **Streaming:** recources, added files  

</expandable-element>  

<table>
    <tr>
        <td><b>Service</b></td>
        <td><b>Period</b></td>
    </tr>
    <tr>
        <td>CDN</td>
        <td>90 days</td>
    </tr>
    <tr>
        <td>Cloud</td>
        <td>7 days for Basic VM<br>30 days for other services</td>
    </tr>
    <tr>
        <td>Storage</td>
        <td>14 days (if the service was disabled while being in the Trial)<br>30 days (if the service with the paid plan was disabled)<br><b>Note:</b> After deleting manual recovery is available<br> by contacting <a href="mailto:support@gcore.com">technical support</a> for additional 14 days</td>
    </tr>
    <tr>
        <td>DNS</td>
        <td>90 days</td>
    </tr>
    <tr>
        <td>Streaming</td>
        <td>90 days</td>
    </tr>
    <tr>
        <td>Web Security</td>
        <td>5 days</td>
    </tr>
    <tr>
        <td>DDoS Protection</td>
        <td>90 days</td>
    </tr>
</table>

> **Note:** All dates mentioned above are default. They can differ in particular cases if a personal manager or technical support changed amount of the days for your account by mutual preliminary arrangement.  

## Resume services

1\.  Go to the <a href="https://accounts.gcore.com/billing/services" target="_blank">Services</a> tab.

2\.  Find the service you need and click **Resume service**.

<img src="https://assets.gcore.pro/docs/account-settings/billing/services/resume-20.png" alt="Services tab">