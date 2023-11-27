---
title: users
displayName: Users
published: true
toc:
pageTitle: Understanding user roles | Gcore
pageDescription: A detailed guide to user roles and permissions, covering how roles affect service management, personal data changes, etc.
customUrl: /account-settings/users/about-users
---

# About Users

In the Gcore Control Panel, there are roles that define user rights, such as permitted actions to manage the <a href="https://cdn.gcore.com" target="_blank">CDN</a> and <a href="https://streaming.gcore.com" target="_blank">Streaming Platform</a> and change personal data.

**Note**: The <a href="https://cloud.gcore.com" target="_blank">Cloud</a> service has its own role system. Read the "<a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights" target="_blank">User roles and rights</a>" guide for more details. For other Gcore services (<a href="https://dns.gcore.com" target="_blank">DNS Hosting</a>, <a href="https://storage.gcore.com" target="_blank">Storage</a>, <a href="https://control.gcore.com" target="_blank">Web Security and DDoS Protection</a>), roles do not apply. This means that regardless of the user's role, they can perform any actions with the DNS service.

By default, a user who registers an account has the "Administrator" role with the most extensive rights. An Administrator can invite up to five new users to their account daily and assign one of the available roles to each of them:

<table>
<tbody>
<tr style="height: 22px;">
<td style="height: 22px;">Role</td>
<td style="height: 22px;">Role Rights</td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px;">Administrators</td>
<td style="height: 22px;">
<ul><li>Have full rights to manage services and view statistics.</li>
<li>Enable <a href="https://gcore.com/docs/account-settings/set-up-two-factor-authentication" target="_blank">2-Factor authentication</a>.</li>
<li>Change their personal data (email, password, phone, language, company name) in the "<a href="https://accounts.gcore.com/profile/general" target="_blank">Profile</a>" section.</li>
<li>Add new users to the account and assign roles to them.</li>
<li>Change the name, language, and role of the invited users. Other settings (e.g., changing the user's email address) are unavailable.</li>
<li>Delete users.</li>
<li>Create an <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API Token</a> with all roles listed below, including "Administrators".</li>
</ul>
</td>
</tr>
<tr style="height: 22.8px;">
<td style="height: 22.8px;">Engineers</td>
<td style="height: 22.8px;">
<ul><li>Change service settings and view statistics.</li>
<li>Perform Purge and Prefetch in the Control Panel and via API.</li>
<li>Enable <a href="https://gcore.com/docs/account-settings/set-up-two-factor-authentication" target="_blank">2-Factor authentication</a>.</li>
<li>Change their personal data in the "<a href="https://accounts.gcore.com/profile/general" target="_blank">Profile</a>" section.</li>
<li>Create an <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API Token</a> with the roles listed below, including "Engineers".</li>
</ul>
</tr>
<tr style="height: 22px;">
<td style="height: 22px;">
<p>Purge and Prefetch only (API+Web)</p>
</td>
<td style="height: 22px;">
<ul><li>View statistics and settings.</li>
<li>Make API calls to Purge and Prefetch.</li>
<li>Perform Purge and Prefetch in the Control Panel.</li>
<li>Enable <a href="https://gcore.com/docs/account-settings/set-up-two-factor-authentication" target="_blank">2-Factor authentication</a>.</li>
<li>Change their personal data in the "<a href="https://accounts.gcore.com/profile/general" target="_blank">Profile</a>" section.</li>
<li>Create an <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API Token</a> with the roles listed below, including "Purge and Prefetch only (API+Web)".</li>
</ul></td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px;">
<p>Purge and Prefetch only (API)</p>
</td>
<td style="height: 22px;">
<ul>
<li>View statistics and settings.</li>
<li>Make API calls to Purge and Prefetch.</li>
<li>Enable <a href="https://gcore.com/docs/account-settings/set-up-two-factor-authentication" target="_blank">2-Factor authentication</a>.</li>
<li>Change their personal data in the "<a href="https://accounts.gcore.com/profile/general" target="_blank">Profile</a>" section.</li>
<li>Create an <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API Token</a> with the "Users" and "Purge and Prefetch only (API)" roles.</li>
</ul></td>
</tr>
<tr style="height: 22px;">
<td style="height: 22px;">Users</td>
<td style="height: 22px;">
<ul>
<li>View statistics and settings.</li>
<li>Enable <a href="https://gcore.com/docs/account-settings/set-up-two-factor-authentication" target="_blank">2-Factor authentication</a>.</li>
<li>Change their personal data in the "<a href="https://accounts.gcore.com/profile/general" target="_blank">Profile</a>" section.</li>
<li>Create an <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API Token</a> with the "Users" role.</li>
</ul></td>
</tr>
</tbody>
</table>

**Note**: Other CDN and Streaming Platform actions not mentioned in the table are prohibited for roles.

If an administrator invites a new user and assigns two roles to them, the role with more rights will be valid. For example, users who are assigned Users and Engineers roles will possess Engineers rights.
