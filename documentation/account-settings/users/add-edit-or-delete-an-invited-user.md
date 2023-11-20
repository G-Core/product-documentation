---
title: add-edit-or-delete-an-invited-user
displayName: Manage
published: true
order: 20
toc:
   --1--Invite: "invite-a-user"
   --2--Sending and resending invitations: "sending-and-resending-the-invitation"
   --1--Edit: "change-the-users-account-information"
   --1--Delete: "delete-a-user"
   --2--Features: "deletion-features"
pageTitle: Guide to managing users' roles | Gcore 
pageDescription: A detailed step-by-step guide on inviting, editing, and deleting users in your Gcore account.
---
# Invite, edit, and delete a user

In the article, you’ll learn how to manage users in the Control Panel. You can invite users whether or not they are already registered with Gcore.

## Invite a user

**Note**: Only the user with the <a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">Administrator role</a> can add new users to the account.

1\. Navigate to <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a>.

2\. Click **Invite user**.

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-10.png" alt="A page for inviting users">

The following pop-up will appear, where you will perform the remaining steps. 

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-20-v2.png" alt="A page where you specify interface language, mail, roles">

3\. Enter the name of the invited user. The name can be anything; we recommend using first name and surname for ease of use. It will be displayed in the control panel.

You can invite both existing Gcore users and users who are not yet registered with Gcore:


- If a user isn’t yet in the Gcore system, when you try to add them, an email will be sent to their email address with a link to create a password. The invited user should accept the invitation and create a password. Then, they can log in to the account.
- If a user already exists in the Gcore system, a notification about the new account access will be sent to their email address. After accepting the invitation, users can log in to their account during authorization.

4\. Enter their email address. It will be used to send an invitation to become a user, and for other notifications.

5\.  Specify the language of the interface: English, German, Chinese, or Russian.

6\. Select the CDN service and control panel (IAM) role. Learn more about <a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">which actions are available for each role</a>. 

**Note**: Depending on the role selected in IAM/CDN, the role for Cloud will be automatically selected. For example, if you want to create a user with the Administrator CDN role, the user will also have the most access to the Cloud service.  

7\. Select the scope for the Cloud service. There are two options:

- **Client**. The scope will be applied to all projects. You can either grant no access or assign the administrator role.
- **Project**. You set up roles for each project. Select the project in the left part and the role on the right. Learn more about <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights" target="_blank">which actions are available for each role</a>.

8\. For other services (Billing, DNS, Storage, Streaming, Web security), the invited user will automatically be provided with full permissions (administrator role.)

9\. Click **Invite user**.

That’s it! An entry containing information about the invited user with their unique ID will appear in the <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a> section. From there, you can filter invited users by criteria (e.g., two-factor authentication) and search for a specific user by ID or email.

### Sending and resending the invitation

**Note**: The invitation link is valid only for 24 hours. It will expire if users don’t confirm their email by clicking the link in that timeframe. Account administrators can resend an invitation on the <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a> page by clicking the three dots on the right of the user’s row and clicking **Resend invite**.

After the user has been sent an invitation, their user row will show whether they have accepted the invitation (“Status” column) and whether they have enabled two-factor authentication (column “Two-Factor authentication.”)

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-30.png" alt="How to resend an invitation to a user">

## Change the user’s account information

**Note**: Only the user and the account administrator can change the user account information.

- If you are an account administrator, go to the <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a> section. Click three dots next to the user, then click **Edit**.

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-40.png" alt="Edit a user from the Users page">

In the pop-up window, you can change your (Administrator) username, Role, and Language. As for other users, you can change only their <a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">Role</a>.

- If you are a user, edit your info in the General section of the <a href="https://accounts.gcore.com/profile/general" target="_blank">Account</a> page.

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-50.png" alt="Edit a user on the General page">

## Delete a user

Navigate to <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a>, click the three dots next to the user, then click **Delete**.

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/invite-users-60.png" alt="How to delete a user">

Confirm the deletion.

### Deletion features

- If a user has roles in several accounts and you want to delete the user from all of them, you should do the steps above from each account.
- If a permanent API token was issued by a user who will be deleted, first <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token#delete-an-api-token" target="_blank">delete the required token</a>. Otherwise, an error will appear: “You can’t remove the user as they have active tokens.”
- After deleting a user, their name and email address will be crossed out in the API tokens section next to the tokens issued by them. When you roll over their name, you will see “The user has been deleted”:

<img src="https://assets.gcore.pro/docs/account-settings/users/add-edit-or-delete-an-invited-user/deletion-massage-70.png" alt=" API tokens section" width="80%">
