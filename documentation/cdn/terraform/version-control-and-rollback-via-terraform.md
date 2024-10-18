---
title: version-control-and-rollback-via-terraform
displayName: Set up version control and perform rollback
published: true
order: 60
toc:
pageTitle: A guide on how to set up version control and perform a rollback procedure via Terraform | Gcore
pageDescription: Learn how to use Terraform to configure versioning and rollback capabilities for CDN configurations.
---
# Set up version control and roll back to previous configurations

Integrate Terraform and Git to get robust versioning and rollback capabilities for your CDN configurations. This setup ensures better stability of your infrastructure as you can quickly revert any changes with minimal downtime and fewer potential issues. 

Follow the best practices outlined below to efficiently manage and secure your infrastructure changes. 

## Best practices 

* **Use a consistent branching strategy**.  Even if you are working primarily on the main branch, consider creating branches for specific changes. Merge your changes into the main branch only after thorough testing. 

* **Write meaningful commit messages**. This ensures that the history of changes is easy to understand, specifically for contributors who don’t have enough context about the updates. 

* **Regularly tag releases or significant changes**. If there are any issues, it’ll be easier to revert to a stable state. 

* **Test rollback procedures**. This practice minimizes risks when an actual rollback is needed since you know that everything works as expected. 

* **Secure sensitive data**. Use environment variables or secret management services for sensitive data like API tokens. Ensure that these values are not committed to version control. 

## Set up versioning

To proceed with the following steps, you need to configure <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token#create-a-permanent-api-token" target="_blank">API keys</a> and install both <a href="https://git-scm.com/" target="_blank">Git</a> and <a href="https://gcore.com/docs/cdn/terraform/install-and-configure-terraform" target="_blank">Terraform</a> on your machine. 

### Step 1. Initialize a Git repository

Start setting up version control by initializing a Git repository in your Terraform project directory. To do so, run the following command: 

<code-block>

cd your-terraform-project-directory
git init

</code-block>

### Step 2: Organize Terraform files 

Create a *.gitignore* file to ensure sensitive data and other unnecessary files are not committed to version control: 

<code-block>

\# .gitignore
*.tfvars
*.tfstate
*.tfstate.backup
.terraform/

</code-block>

After you create the file, stage your Terraform files for the initial commit: 

<code-block>

git add .
git commit -m "Initial commit of Terraform configuration for CDN resources"

</code-block>

Set an initial tag for versioning and push the changes to your main branch: 

<code-block>

git tag -a v1.0.0 -m "Initial release"
git push origin main --tags

</code-block>

### Step 3. Update Terraform configuration 

Modify your Terraform configuration as needed. After making changes, commit them to your Git repository: 

<code-block>

git add .
git commit -m "Updated CDN resource config"

</code-block>

### Step 4. Add tags 

Tag significant versions of your configuration:

<code-block>

git tag -a v1.0.1 -m "Release version 1.0.1 with updated CDN resource config"
git push origin main --tags

</code-block>

### Step 5. Apply the configuration 

Run the following command: `terraform apply`.

## Roll back your changes 

Sometimes, changes made to your configurations may result in unexpected behavior. Having a rollback strategy allows you to quickly revert to the last known good configuration, minimizing downtime and ensuring stability. 

### Step 1. Identify the state to roll back to 

Identify the version to which you want to roll back using Git tags or commit history. Use `git log` or `git tag`.

### Step 2. Switch to the required version 

Check out the specific version: `git checkout tags/v1.0.0`.

### Step 3. Apply the rollback 

Apply the configuration from the checked-out version: `terraform apply`.

That’s it! You’ve successfully rolled back to the needed version and can continue your work. 