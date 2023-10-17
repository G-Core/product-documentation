---
title: block-activate-users-and-sellers
displayName: Block/Activate
published: true
order: 90
toc:
    --1--What is the "Block" feature?: "what-is-the-block-feature"
    --1--Block/Activate a user or seller: "block-activate-a-user-or-seller"
    --1--Check if a user or seller is blocked or active: "check-if-a-user-or-seller-is-blocked-or-active"
---
# Block/Activate users and sellers

## What is the "Block" feature?

The <a href="https://admin-platform.gcore.top" target="_blank">new admin panel's</a> "Block" feature allows you to block users and sellers, which is an effective tool for managing access to the admin or control panel and maintaining a secure and trustworthy community of consumers.

The following restrictions apply to blocked users and sellers:

- All requests to the IAM API, including authorization tokens, password recovery, and activation requests, are prohibited.
- All active users/sellers API tokens are blocked, and creating new tokens is prohibited.

**Note**: The blocking restrictions will remain in effect until you cancel them with the "Activate" feature.

## Block/Activate a user or seller

1\. Depending on who you want to block, the user or seller, go to the <a href="https://admin-platform.gcore.top/users" target="_blank">Users</a> or <a href="https://admin-platform.gcore.top/sellers" target="_blank">Sellers</a> section in the admin panel.

The new page will open, and you can do the remaining steps there.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/block-activate-users-and-sellers/block-users-10.png" alt="Sellers section">

2\. Find the user/seller you need using the filters.

3\. Scroll the page on the right and click the three dots.

4\. Select **Block**.

The user/seller will be blocked.

Click **Activate** if you need to unblock the user/seller in step #4.

## Check if a user or seller is blocked or active

1\. Depending on who you want to check, the user or seller, go to the <a href="https://admin-platform.gcore.top/users" target="_blank">Users</a> or <a href="https://admin-platform.gcore.top/sellers" target="_blank">Sellers</a> section in the admin panel.

2\. Find the user/seller you need using the filters.

3\. Check the value of the user/seller in the "Blocked" column.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/block-activate-users-and-sellers/blocked-status-20.png" alt="Blocked column" width="80%">

- If the status is "true", the user is blocked and cannot access the account and services.
- If the status is "false", the user is active and has access to the account and services.
