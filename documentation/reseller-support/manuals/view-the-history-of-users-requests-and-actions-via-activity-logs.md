---
title: view-the-history-of-users-requests-and-actions-via-activity-logs
displayName: Activity logs
published: true
order: 100
toc:
   --1--Activity logs: "what-is-an-activity-logs-section-for"
   --1--View: "view-users-changes-in-the-activity-logs-section"
   --1--Use filters: "use-filters"
   --1--Client changes: "how-to-look-for-changes-in-a-particular-client"
---

# View the history of users’ requests and actions via Activity logs

## What is an Activity logs section for?

The Activity logs section displays changes that users have made. Users are all the <a href="https://gcore.com/docs/reseller-support/manuals/manage-clients" target="_blank">clients</a> and <a href="https://gcore.com/docs/reseller-support/manuals/manage-sellers" target="_blank">sellers</a> that you have added. Changes they can make include requests sent via the <a href="https://api.gcore.com/docs" target="_blank">API</a> and actions in the <a href="https://auth.gcore.com/login/signin?lang=en" target="_blank">control panel</a>. 

## View users’ changes in the Activity logs section

1\. Go to the https://admin.gcore.top/.

2\. Open Activity logs in the Security section.

The entities will be displayed on the right.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/view-the-history-of-users-requests-and-actions-via-activity-logs/image3499-10.png" alt="Activity logs" width="80%">

You can sort and filter entities by the following columns:

- **Client**: ID of the client that made the request
- **User**: ID of the user that made the request
- **Requested** at: Date and time when the request was made
- **Method**: Request HTTP method, such as GET, POST, PUT, DELETE, or  PATCH
- **Path**: Request URL
- **Data**: Request body
- **Reverted**: Whether the request was rolled back
- **Status** code: Status code that the request returned in the response
- **Remote IP**: IP address from which the request was made
- **Host**: Host from which the request was made

If certain columns are not required, you can disable them. Click **Manage Columns** in the upper right area and turn off the switch.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/view-the-history-of-users-requests-and-actions-via-activity-logs/image3501-20.png" alt="Manage Columns" width="50%">

## Use filters 

You can search for specific requests by setting filters. For example, you can filter out all logs for a user with a specific ID or all requests with the GET method.

To filter logs by a specific parameter: 

1\. Click **Add filter**.
2\. Select the needed search condition, e.g., the period where any changes were made.
3\. Select the period.
4\. Click **Apply filter**.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/view-the-history-of-users-requests-and-actions-via-activity-logs/Group190991-30.png" alt="Use filters" width="80%">

That’s it. As a result, you will see only entities for the specified period (in this case, from June 27, 2023, to July 04, 2023.)

## How to look for changes in a particular client

Clients’ accounts can be changed not only by clients themselves, but also by sellers. For example, a seller can change the service to "Trial" status. In this case, if you try to find the changes in the "Client" column by specifying the client ID, there will be no entity, because it was not the client who made the change. 

To look for all changes, you should specify the client ID in the “Path” filter as shown below.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/view-the-history-of-users-requests-and-actions-via-activity-logs/image3503-40.png" alt="Path filter" width="80%">

With this approach, all entities that are related to the client will be filtered out, regardless of who made the change.
