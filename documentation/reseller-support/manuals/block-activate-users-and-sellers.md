---
title: block-activate-users-and-sellers
displayName: Block or activate a seller
published: true
order: 90
toc:
    --1--What is the "Block" feature?: "what-is-the-block-feature"
    --1--Block or activate a seller: "block-or-activate-a-seller"
    --1--Check if a seller is blocked or active: "check-if-a-seller-is-blocked-or-active"
---
# Block or activate sellers

## What is the "Block" feature?

The <a href="https://admin-platform.gcore.top" target="_blank">new admin panel's</a> "Block" feature allows you to block sellers, which is an effective tool for managing access to the admin portal and maintaining a secure and trustworthy community of consumers.

The following restrictions apply to blocked sellers:

- All requests to the IAM API, including authorization tokens, password recovery, and activation requests, are prohibited.
- All active sellers' API tokens are blocked, and creating new tokens is prohibited.

**Note**: The blocking restrictions will remain in effect until you cancel them with the "Activate" feature.

## Block or activate a seller

1\. Go to the <a href="https://admin.gcore.top/users/sellers" target="_blank">Sellers</a> section in the admin portal.

The new page will open, and you can do the remaining steps there.

2\. Find the seller you need using the filters.

3\. Scroll the page on the right and click the three dots.

4\. Select **Block**.

The seller will be blocked.

Click **Activate** if you need to unblock the seller in step #4.

## Check if a seller is blocked or active

1\. Go to the <a href="https://admin.gcore.top/users/sellers" target="_blank">Sellers</a> section in the admin portal.

2\. Find the seller you need by using the filters.

3\. Check the value of the seller in the "Blocked" column.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/block-activate-users-and-sellers/blocked-status-20.png" alt="Blocked column" width="80%">

- If the status is "true", the seller is blocked and cannot access the account and services.
- If the status is "false", the seller is active and has access to the account and services.
