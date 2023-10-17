---
title: how-the-cdn-service-and-its-additional-options-are-billed
displayName: Billing
published: true
order: 30
toc:
   --1--Understand CDN billing: "understand-cdn-billing"
   --1--Understand additional options billing: "understand-additional-options-billing"
   --1--Service suspension for non-payment: "service-suspension-for-non-payment"
   --1--View charges and payment history: "view-your-charges-and-payment-history"
   --1--Change your billing plan: "change-your-billing-plan"
pageTitle: Guide to CDN service and options billing | Gcore
pageDescription: Understand how CDN services are billed, including monthly traffic limits, overages, and additional options.
---
# How the CDN service and its additional options are billed

You can view the current CDN pricing on <a href="https://gcore.com/pricing" target="_blank">our website</a>. 

## Understand CDN billing

Each plan description shows prices for traffic within a month limit and for overage. There is also a request limit. When the number of requests exceeds your plan's limit, you are charged additionally.

<img src="https://assets.gcore.pro/docs/cdn/how-the-cdn-service-and-its-additional-options-are-billed/image-5.png" alt="Understand CDN billing" width="80%">


|             | Monthly traffic limit                                                                                                                                                                                           | Traffic overage                                                                                                                                                                                                                                                                                                                                                                                                               | Request overage                                                                                                                            |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | The amount of traffic that you can use within the plan. It includes both traffic from your origin to a CDN server and from a CDN server to an end-user. It is renewed on the 1st day of every calendar month. | Amount of traffic used over a plan limit.                                                                                                                                                                                                                                                                                                                                                                                     | Number of requests made over a plan limit. It includes requests both from an end-user to a CDN server and from a CDN server to an origin. |
| Billing     | The system charges a plan fee on the 2nd day of every month.                                                                                                                                                    | The system charges the money in portions of €50/$60 (currency depends on account settings). It adds up the cost of traffic overage and request overage. As soon as the accrued costs reach €50/$60, the system charges this amount.<br><br>Unpaid costs are charged on the 2nd day of a following month. That is, if the total cost of overage is less than €50/$60, the system will charge it on the 2nd day of a following month. |
| Example     | On the 2nd day of a month, you are charged a regular plan fee.                                                                                                                                                  | Within the plan, you can use 5 TB of traffic and 1 billion requests. Let's assume you reach this limit, but continue to use the CDN. The system calculates the total cost of traffic overage and additional requests. Once the accrued costs reach €50/$60, your account is charged.                                                                                                                                          |When activating a plan, you will be charged proportionally for the number of days remaining until the end of the month. For example, you activate a plan that costs €100/month on September 15. Fifteen days remain until the end of September — exactly half a month. This means that initially you will pay half the plan fee, i.e. €50. But on October 2, you will be charged €100 for the whole month up front.|

**Why overage is charged in portions of €50/$60.** This is the credit limit — the maximum value of unpaid costs. With it, you do not need to keep money in your account to pay for possible overage. The CDN will keep working unless the charges for overage exceed the credit limit. Unpaid costs below the credit limit are charged on the 2nd day of a following month together with a plan fee.

For example, you use the Pro 5 TB plan for €100/month, the credit limit is €50. You reach the traffic limit, but the month is not over yet. The price for extra traffic is €0.02/GB. By the end of the month, you've used 100 GB of extra traffic. The accrued cost of overage is €2. This amount does not exceed the credit limit of €50. So, those €2 will be charged next month: instead of the regular plan fee of €100, you will pay €102.

The credit limit may differ from the one that is given in this article. You can always check the current limit in your account Dashboard.

## Understand additional options billing

<img src="https://assets.gcore.pro/docs/cdn/how-the-cdn-service-and-its-additional-options-are-billed/image-7.png" alt="Understand additional options billing" width="80%">

Additional options are listed on <a href="https://gcore.com/pricing" target="_blank">the CDN pricing page</a>. To activate it, contact our technical support via chat or email [support@gcore.com](mailto:support@gcore.com). Each option has a fixed price and is billed together with the plan fee on the 2nd day of every month. For example, if you activate a plan for €100/month and the "Extended statistics" option for €200. On the 2nd day of a following month, the system will charge you €300.

Please note that when you activate the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a>" option, the traffic will be calculated differently. Usually, a traffic plan counts two types of traffic:

- from your origin to a CDN server,
- from a CDN server to an end-user.

When "Origin Shielding" is on, a traffic plan counts three types of traffic:

- from your origin to a shielding server,
- from a shielding server to a CDN server,
- from a CDN server to an end-user.

## Service suspension for non-payment

**Once the cost of overage reaches the credit limit,** the system will charge that amount (equal to the credit limit) from your account. If account payment fails, the linked payment instrument (such as a credit card that you added when signing up) will be charged automatically. If payment fails again, the CDN will stop delivering content to users. Recharge your account manually: the system will charge it for the unpaid costs and reactivate the services. The credit limit will also be renewed — the service will keep running until you reach the credit limit again.

**If on the 2nd day of a month there is not enough money in your account to pay for services**, two options are possible:

- You have no unpaid costs accrued in the previous month. The system charges your account for a plan fee and additional options. But if your account payment fails, the system will charge your linked payment instrument. If it fails too, the system will charge your linked payment instrument two more times: on the 3rd and 4th day of the month. If payment fails on the 5th, _all active services associated with your account_ will be suspended. For example, if you use "CDN" and "Storage", both services will stop working.
- You have unpaid costs accrued in the previous month. The system charges your account first for the unpaid costs, and then for a plan fee and additional options. But if your account payment fails, the system will charge your linked payment instrument. If it fails too, _all active services associated with your account_ will be immediately suspended. For example, if you use "CDN" and "Storage", both services will stop working.

## View your charges and payment history

Log in to your account, click the profile icon and go to "Billing". Find the following sections:

- Expenses — all transactions that have been made to pay for all products and services,
- Payments —all transactions you have made to recharge your account.

<img src="https://assets.gcore.pro/docs/cdn/how-the-cdn-service-and-its-additional-options-are-billed/mceclip0.png" alt="View your charges and payment history">

## Change your billing plan

Click the profile icon in the bottom-left corner of the page, select "Billing", and change to the plan you need.

A new plan will be activated only on the 1st day of a following month.

If you have any questions, please contact us via chat or email [support@gcore.com](mailto:support@gcore.lu). If you are interested in the "Enterprise" plan, please write to our managers [sales@gcore.lu](mailto:sales@gcore.lu).
