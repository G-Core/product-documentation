---
title: configure-password-policy
displayName: Configure password policy
published: true
order: 35
---
# Configure password policy

We enforce a predefined password security policy that protects your system from unauthorized access. The policy comprises the following rules: 

* **Password reuse**. After a password expires, a user must create and use three unique passwords before using the old password again. The system stores the last three passwords to prevent immediate reuse. 

* **Password expiration**. You can set up the frequency of password expiration or disable this feature altogether. If the policy is disabled, users can retain their passwords indefinitely. 

## Enable password policy

Before setting up the policy, make sure you have disabled the login/password authentication option. If this setting is already applied, skip **Step 1**. 

### Step 1 (Optional). Enable username/password login 

Before configuring the password policy, make sure that the **Username/Password login** option is enabled for a user. Otherwise, you won’t be able to save the policy settings. 

To enable authorization via username and password: 

1\. In the Admin Portal, navigate to the **Security** settings. 

2\. Click **Authorization**. 

3\. Enable the **Username/Password login** toggle. 

4\. Click **Save** to apply the changes.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-password-policy/authorization.png" alt="SSO in the Admin Portal" width="80%">

### Step 2. Activate password policy 

To configure password frequency change for an account: 

1\. In the Admin Portal, navigate to the **Security** settings. 

2\. Click **Password policy**.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-password-policy/policy-enabled.png" alt="SSO in the Admin Portal" width="80%">

3\. Enable the **Frequency of password changing** toggle.

<img src="https://assets.gcore.pro/docs/reseller-support/manuals/configure-password-policy/policy-disabled.png" alt="SSO in the Admin Portal" width="80%">

4\. Specify the number of days after which the password becomes invalid. The password can be set to expire between 30 and 180 days. 

<alert-element type="tip" title="Tip">

We recommend setting a password change frequency between 60 and 90 days. 

</alert-element>

5\. Click **Save** to apply the changes. 

Two weeks before the expiration date, all users with enabled password policy will start receiving emails reminders about password change. 