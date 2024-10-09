---
title: create-manage-templates
displayName: Create and manage templates
published: true
order: 40
toc:
   --1--Create a template: "create-a-template"
   --1--Edit a template: "edit-a-template"
   --1--Delete a template: "delete-a-template"
   --1--Edit a template: "edit-a-template"
   --1--Update template binary: "update-template-binary"
   --1--Create an app from a template: "create-an-app-from-a-template"  
pageTitle: A guide on creating and managing FastEdge templates | Gcore
pageDescription: A short overview of FastEdge application templates, how they can be created and used for creating applications.
---
# Create and manage templates

Templates include predefined configurations for FastEdge apps. Using templates eliminates the need to manually configure each aspect of an application, which speeds up the configuration process and ensures consistency across deployments. 

## Create a template 

Both CDN and HTTP applications have the same template configuration process. 

<tabset-element>

### From the Templates page 

To add a template to the Customer Portal:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. Open the **Templates** page and click **Create template**.

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-button.png" alt="Create template button" width="80%">

3\. Add your custom binary file. Once the upload is finished, the file will be automatically added to the Customer Portal. 

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-upload-binary.png" alt="Add raw binary dialog" width="80%">

4\. Give your template a name. Use a clear and descriptive name to ensure the template is easy to identify. 

5\. (Optional) Add a description to provide extra information about the template. 

6\. (Optional) Add instructions for using the template. Include any critical information that’s important to know when creating an app, such as required variables, headers, and any configuration tips. 

7\. Specify any required parameters.

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-setup.png" alt="Add raw binary dialog" width="80%">

8\. Click **Save template**. 

The template was successfully added. You can use this or any template shared by your admin to create FastEdge applications. To share the template with other users in your account, contact the admin for assistance. 

### From an existing application 

You can convert an existing application into a template for future reuse. The template will be created using the binary of the original application, and it will contain any associated environment variables. 

To add a template from an application: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Applications** page, click the three-dot icon next to the application you want to configure. 

3\. Select **Manage**. 

4\. Click **Actions** and choose **Create template**.

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-from-app.png" alt="Create template from app menu" width="80%">

5\. Review the current configuration and, if necessary, update the template's name and description. 

6\. Click **Save template** to apply the changes. 

</tabset-element>

## Edit a template 

To adjust the template configuration or add new settings: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Templates** page, click the three-dot icon next to the template that you want to edit. 

3\. Click **Edit template**. 

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-from-app.png" alt="Create template from app menu" width="80%">

4\. Update the configuration as you see fit, and then click **Save template** to apply the changes.

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-from-app.png" alt="Create template from app menu" width="80%">

The template has been updated. 

## Delete a template 

<alert-element type="warning" title="Warning">

Deleted templates can’t be restored.  
 
</alert-element>

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Templates** page, click the three-dot icon next to the template that you want to remove. 

3\. Click **Delete template**. 

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/delete-template.png" alt="Delete template" width="80%">

You’ve permanently removed the template from the Customer Portal. 

## Update template binary 

If you want to update the application binary to a newer version or add substantial changes to the template configuration, you can replace the existing WebAssembly (.wasm) file with a new one.  

To update the binary file: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Templates** page, click the three-dot icon next to the template that you want to edit. 

3\. Click **Update template binary**.

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/update-template-binary.png" alt="Update template binary" width="80%">

4\. Add the new .wasm file from your local file system. Once the upload is finished, the file will be automatically added to the Customer Portal. 

<img src="https://assets.gcore.pro/docs/fastedge/create-manage-templates/create-template-upload-binary.png" alt="Upload template binary dialog" width="80%">

5\. Verify the current configuration and click **Save template** to apply the updates. 

## Create an app from a template  

You can deploy a FastEdge application directly from the Templates page: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **FastEdge** and choose the relevant page: **HTTP Applications** or **CDN Applications**. 

2\. On the **Templates** page, find the template you want to use to create an application.  

3\. Click the three-dot icon next to open template settings and select **Create app from template**. 

4\. Proceed with the application configuration as described in the relevant guide: 

 * <a href="https://gcore.com/docs/fastedge/getting-started/create-fastedge-apps#stage-2-deploy-an-application" target="_blank">Create an HTTP app from a template</a>
 * <a href="https://gcore.com/docs/cdn/getting-started/integrate-cdn-with-fastedge#step-1-create-a-fastedge-application" target="_blank">Create a CDN app from a template</a>