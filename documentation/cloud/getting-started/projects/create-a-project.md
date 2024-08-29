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
pageDescription: Learn how to create and manage an Edge Cloud project in the Gcore Customer Portal.
---
# Create and manage projects

Projects are goal-specific folders where you can create Edge Cloud products including Virtual Machines, volumes, and networks. Each project acts as a separate environment; its resources are isolated from the resources in any other project. You can control access to these resources by specifying user permissions on a per-project basis.  

You can view projects in the Gcore Customer Portal via either the **Project** dropdown or the **Cloud Management** page.

<tabset-element>

## From the Project dropdown

1\. Navigate to the Cloud page and select the **Project** dropdown.

2\. Select **View all projects**. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/open-projects-from-dropdown.png" alt="A dropdown displaying a list of projects" width="80%">

3\. The **Projects** page will open. Here you can view, search for, and manage your projects.  

To open the resource management panel for a particular project, click **Open project**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-open-project.png" alt="A list of projects with the highlighted Open project button" width="80%">

## From the Cloud Management page

1\. Navigate to **Cloud** > **Cloud Management**.

2\. Click **Projects**. 

3\. The **Projects** page will open. Here you can view, search for, and manage your projects. 

To open the resource management panel for a particular project, click the project name.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/open-projects.png" alt="A list of projects with the highlighted project name" width="80%">

</tabset-element>

## View projects in different layouts

You can change the layout on the **Projects** page to display the information in two ways:

- **List view**. Presents all projects as a concise list with only the project name and description displayed.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-list.png" alt="" width="80%">

- **Grid view**. Presents all projects as tiles with extra information displayed: project name, ID, and a list of Edge Cloud resources that you can create by clicking the plus button. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/projects-page-grid.png" alt="" width="80%">

You can switch between two layouts by clicking the layout icon to the right of the search bar.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/layout-icon.png" alt="A search bar with adjacent buttons to change page layout" width="80%">

## Create a project 

When you first navigate to the Cloud page, you’ll have only one **Default** project. This project is created automatically for every account and can’t be deleted. 

You can create more projects to organize your cloud resources. The number of projects doesn't affect your expenses, you only pay for resources used.

To create a project:

1\. Navigate to the **Projects** page.

2\. In the upper-right corner of the screen, select **Create project**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/create-project.png" alt="The Projects page with the Create project button highlighted" width="80%">

3\. Enter your project name. Optionally, add a description. 

<alert-element type="info" title="Info">

A project name can contain between 3 and 63 characters, including Latin letters, numbers, hyphens, underscores, spaces, and dots. The name can’t end with a hyphen. 

</alert-element>

4\. Click **Create project**. 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/create-project-annotated.png" alt="A dialog with configuration of project name and description" width="60%">

The new project will appear in your project list. 

## Manage projects

You can edit the project name and description, delete a project if you have the <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights" target="_blank">appropriate permissions</a>, and configure access to the project. 

If you have a large number of projects, you can also use search to find the one that you need.

### Edit project name or description

1\. Navigate to the **Projects** page.

2\. Click the three-dot icon next to the project you want to edit.

3\. Select **Settings**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/annotated-project-settings.png" alt="Project settings menu with Open and Settings options" width="80%">

4\. Update project information and then click **Save changes** to apply the updates.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-save-changes.png" alt="Project settings menu with options to change project name and description" width="80%">

### Manage project access 

To view and modify user access to the project, you need <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#client-administrator" target="_blank">Client Administrator</a> or <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#project-administrator" target="_blank">Project Administrator</a> access. 

To change access to the project:

1\. Open the **Projects** page and find the project you want to update.

2\. Click the three-dot icon next to the project you want to manage.

3\. Select **Settings**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/annotated-project-settings.png" alt="Project settings menu with Open and Settings options" width="80%">

4\. Open the **Access** tab. You’ll see the list of users associated with the project and their access levels. To manage user access, follow the instructions in our guide on <a href="https://gcore.com/docs/cloud/getting-started/projects/users/manage-user-access-to-your-project" target="_blank">how to manage user access to your project</a>.

To configure user access within your account, click "Manage users via profile". 

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/access-project-settings.png" alt="Project access tab displaying one user added to the project" width="80%">

### Delete a project

To delete a project, you need <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#client-administrator" target="_blank">Client Administrator</a> or <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#project-administrator" target="_blank">Project Administrator</a> access. 

<alert-element type="warning" title="Warning">

When you delete a project, all resources inside that project will be permanently deleted and can’t be restored. Default projects can't be deleted.

</alert-element>

To delete a project:

1\. Navigate to the **Projects** page.

2\. Click the three-dot icon next to the project you want to delete.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-settings-delete.png" alt="Project settings menu with Open, Settings, and Delete options" width="80%">

3\. Select **Delete**.

4\. Confirm your action by typing “Delete” in the text field.

5\. Click **Yes, delete**.

<img src="https://assets.gcore.pro/docs/cloud/getting-started/projects/create-a-project/project-conifirm-deletetion.png" alt="Delete project dialog" width="60%">

6\. Your project has been successfully deleted.  
