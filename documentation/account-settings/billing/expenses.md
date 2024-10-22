---
title: expenses
displayName: Expenses
published: true
order: 25
toc:
   --1--Pricing rules overview: "pricing-rules-overview"
   --1--Tax rates and discounts: "tax-rates-and-discounts"
   --1--Filter expense data: "filter-expense-data-in-the-table"  
pageTitle: A guide on how to view information about expenses | Gcore
pageDescription: Learn how to check and filter expense data in the account settings.
---
# Expenses

The <a href="https://portal.gcore.com/accounts/billing/expenses" target="_blank">Expenses</a> page displays the costs of consumed Gcore products that have been billed to your account.

<img src="https://assets.gcore.pro/docs/account-settings/billing/expenses/expenses-page.png" alt="Expenses page in the account settings" width="80%">

For each user in the account, you can check the following information: 

* **ID**: A unique identifier of a user account. It’s used to track billing history, payments, and account activity. 
* **Date**: A date when a Gcore product was consumed. 
* **Service**: A type of a consumed product. For example, Cloud or Streaming.
* **Feature**: A particular product feature that was used. 
* **Pricing rule**: In this column, you can compare your actual product usage agains a pre-agreed commitment (reservation of resources). Check <a href="https://gcore.com/docs/account-settings/billing/expenses#pricing-rules-overview" target="_blank">Pricing rules overview</a> for details. 
* **Usage**: The amount of consumed resource.
* **Sum**: The cost of consumed resource. 

## Pricing rules overview

The **Pricing rules** column can have two statuses: **commitment** or **overcommitment**. This applies to the <a href="https://gcore.com/docs/cloud/getting-started/resource-reservation/about-resource-reservation" target="_blank">resource reservation</a> — renting of resources for a long time at a discount. 

If you see **commitment**, this means that the resource usage is within the limits of your reservation. You're billed based on the agrred rates and terms and pay no additional costs. 

If there’s **overcommitment** status, this means that the resource usage has exceeded the reserved limit. Additional charges will apply based on the overage fees. 

We count overcommit expenses on the 1st day of the month for the pervious month.  

## Tax rates and discounts  

If you click the info icon next to the Sum column, you can view a detailed breakdown of the expense, including the collected taxes and applied discounts: 

* **Expense before tax (€)**: The total amount charged before taxes are applied.  
* **Discount percentage (%)**: The percentage of discount applied to your payment before taxation.  
* **Discount amount (€)**: The actual amount of the discount. 
* **Tax rate (%)**: The percentage of tax applied to your expense. This rate is based on local tax laws or regulations. <a href="https://gcore.com/docs/account-settings/billing/vat-rates-in-different-countries-for-an-individual-and-legal-entity" target="_blank">Check VAT rates in different countries</a>
* **Tax amount (€)**: The total amount of tax you’ll pay.

<img src="https://assets.gcore.pro/docs/account-settings/billing/expenses/tax-calculation.png" alt="Tax calculation dialog" width="80%">

## Filter expense data in the table 

You can filter expenses by the consumption date or by a particular service type. The consumption perdiod is set to month by default, but you can choose a custom period as well. 

To adjust table data, use the relevant filters from the **Service** or **Date** dropdowns.

<img src="https://assets.gcore.pro/docs/account-settings/billing/expenses/table-filters-expenses.png" alt="Expenses table with Service and Date dropdowns highlighted" width="80%">