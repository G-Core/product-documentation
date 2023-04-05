---
title: add-edit-or-delete-an-invited-user
displayName: Manage
published: true
order: 20
toc:
   --1--Add: "add-a-user"
   --1--Edit: "change-user-s-account-information"
   --1--Delete: "delete-a-user"
   --2--Features: "deletion-features"
---

# Add, edit, or delete an invited user

## Add a user

**Note**: Only the user with the Administrator role can add new users to the account. 

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/invite-user-10.png" alt="">

1\. Click on the profile icon in the lower-right corner of the page and select the Profile settings.

2\. Open the Users section.

3\. Click on the Invite user button.

The pop-up appears. Do the remaining steps in it. 

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/fill-the-form-20.png" alt="">

4\. Enter the name of the invited user.

5\. Enter his or her email address.

6\. Specify the <a href="https://gcore.com/docs/account-settings/users/about-users" target="_blank">Role</a> of the invited user.

7\. Specify the language of the interface.

8\. Click the **Invite user** button.

**Important**: You can invite both existing and previously not registered users.

*   In case a user is not previously registered in the system, an email will be sent to the email address specified in the invitation with a link to create a password. The invited user should accept the invitation. After creating a password, the user can log in to the account.
*   If a user already exists in the system, a notification about the provided access to the account will be sent to the specified email address. After accepting the invitation, a user will be able to select the required account during authorization.

## Change user's account information

User account information can be changed by 

*   the user
*   a user with an account administrator role.

**If you are an account administrator:**

1\. Go to the <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a> section.

2\. Click on the three-point sign next to the user.

3\. Select **Edit**.

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/edit-user-30.png" alt="">

In the pop-up window, you can change your (the user with the Administrator role) username, Role, and Language. As for the other users, in their settings, you can change only Role. 

**If you are a user:**

1\. Click on the profile icon in the lower-right corner of the page.

2\. Go to the Profile settings.

3\. Change your account details on the General tab.

## Delete a user

1\. Open the <a href="https://accounts.gcore.com/profile/users" target="_blank">Users</a> section.

2\. Click on the three-point sign next to the user.

3\. Select **Delete**.

4\. Confirm the deletion.

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/delete-user-40.png" alt="">

Now the user has no access to the current account.

### Deletion features

1\. If a user is a part of several accounts and you want to delete this user from all of them, you should do the steps above from each account.

2\. If a permanent API token was issued by a user who is going to be deleted, first delete the required token. Otherwise, an error will appear.

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/token-deletion-error-50.png" alt="">

3\. After deleting a user, in the API tokens section, his name and email address will be crossed out next to the tokens issued by him, and a hint will be displayed:

<img src="https://assets.gcore.pro/docs/account-settings/users/manage/deletion-massage-60.png" alt="">
