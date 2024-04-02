---
title: create-a-project
displayName: Create a project
published: true
order: 10
toc:
    --1--View projects in different layouts: "view-projects-in-different-layouts"
    --1--Create a project: "create-a-project"
    --1--Manage projects: "manage-projects"
    --2--Edit name and description: "edit-project-name-or-description"
    --2--Manage project access: "manage-project-access"
    --2--Delete project: "delete-a-project"
pageTitle: Create a project | Gcore
pageDescription: Learn how to create and manage a Cloud project in your personal account.
---
# Create and manage projects

Projects are goal-specific folders where you can create instances, volumes, networks, and other cloud products. Each project acts as a separate environment where its resources are isolated from the resources in any other project. You can also control access to these resources by specifying which users belong to a particular project and what permissions they have.  

There are two ways to view projects in the Gcore Customer Portal: either from the **Project** dropdown or from the **Cloud Management** page.

<tabset-element>

## From the Project dropdown

1\. Navigate to the Cloud page and select the **Project** dropdown.

2\. Select **View all projects**. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/open-projects-from-dropdown.png" alt="A dropdown displaying a list of projects" width="80%">

3\. The **Projects** page will open. Here you can view, search, and manage your projects.  

To open the resource management panel for a particular project, click **Open project**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-open-project.png" alt="A list of projects with the highlighted Open project button" width="80%">

## From the Cloud Management page

1\. Navigate to **Cloud** > **Cloud Management**.

2\. Click **Projects**. 

3\. The **Projects** page will open. Here you can view, search, and manage your projects. 

To open the resource management panel for a particular project, click the project name.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/open-projects.png" alt="A list of projects with the highlighted project name" width="80%">

</tabset-element>

## View projects in different layouts

You can change the layout on the **Projects** page to display the information in two ways:

- **List view**. Present all projects as a concise list where only the project name and description are displayed.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-list.png" alt="" width="80%">

- **Grid view**. Present all projects as tiles with extra information displayed: project name, ID, and a list of cloud resources you can create by clicking the plus button. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-grid.png" alt="" width="80%">

You can switch between two layouts by clicking the layout icon to the right of the search bar.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/layout-icon.png" alt="A search bar with adjacent buttons to change page layout" width="80%">

## Create a project 

When you first navigate to the Cloud page, you’ll have only one **Default** project. This project is created automatically for every account and can’t be deleted. 

You can create more projects to organize your cloud resources. The number of projects doesn't affect your expenses. We charge only for the used resources.

To create a project:

1\. Navigate to the **Projects** page.

2\. In the upper-right corner of the screen, select **Create project**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/create-project.png" alt="The Projects page with the Create project button highlighted" width="80%">

3\. Enter your project name. Optionally, you can add a description. 

<alert-element type="info" title="Info">

A project name can contain between 3 and 63 characters, including Latin letters, numbers, hyphens, underscores, spaces, and dots. The name can’t end with a hyphen. 

</alert-element>

4\. Click **Create project**. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/create-project-annotated.png" alt="A dialog with configuration of project name and description" width="80%">

The new project will appear in your project list. 

## Manage projects

You can edit the project name and description, delete a project if you have the <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights" target="_blank">appropriate permissions</a>, and configure access to the project. 

If you have a large number of projects, you can also use search to find the one that you need.

### Edit project name or description

1\. Navigate to the **Projects** page.

2\. Click the three-dot (...) icon next to the project you want to edit.

3\. Select **Settings**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-annotated.png" alt="Project settings menu with Open and Settings options" width="80%">

4\. Update project information and then click **Save changes** to apply the updates.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-save-changes.png" alt="Project settings menu with options to change project name and description" width="80%">

### Manage project access 

To view and modify user access to the project, you need to have the <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#client-administrator" target="_blank">Client Administrator</a> or <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#project-administrator" target="_blank">Project Administrator</a> access level. 

To change access to the project:

1\. Open the **Projects** page and find the project you want to update.

2\. Click the three-dot (...) icon next to the project you want to manage.

3\. Select **Settings**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-annotated.png" alt="Project settings menu with Open and Settings options" width="80%">

4\. Open the **Access** tab. You’ll see the list of users who belong to the project, along with their access levels. To manage user access, follow the instructions in this guide: <a href="https://gcore.com/docs/cloud/getting-started/projects/users/manage-user-access-to-your-project" target="_blank">Manage user access to your project</a>.

To configure user access within your account, click the "Manage users via profile" link. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-access.png" alt="Project access tab displaying one user added to the project" width="80%">

### Delete a project

To delete a project, you need to have the <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#client-administrator" target="_blank">Client Administrator</a> or <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#project-administrator" target="_blank">Project Administrator</a> access level. 

<alert-element type="info" title="Info">

You can’t delete a default project. When you delete any other project, all resources inside that project will be permanently deleted and can’t be restored. 

</alert-element>

To delete a project:

1\. Navigate to the **Projects** page.

2\. Click the three-dot icon (...) next to the project you want to delete.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-delete.png" alt="Project settings menu with Open, Settings, and Delete options" width="80%">

3\. Select **Delete**.

4\. Confirm your action by typing “Delete” in the text field.

5\. Click **Yes, delete**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-conifirm-deletetion.png" alt="Delete project dialog" width="80%">

6\. Your project has been successfully deleted.  