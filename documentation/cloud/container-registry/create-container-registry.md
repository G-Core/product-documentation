---
title: create-container-registry
displayName: Create a Container Registry
order: 10
published: true
toc:
   --1--Step 1. Add a registry to the Customer Portal: "step-1-add-a-registry-to-the-customer-portal"
   --1--Step 2. Create a user: "step-2-create-a-user"
   --1--Step 3. Push your image to the Container Registry: "step-3-push-your-image-to-the-container-registry"
   --1--Step 4 (Optional). Pull the image from the Registry: "step-4-optional-pull-the-image-from-the-container-registry"
pageTitle: Create a Container Registry | Gcore
pageDescription: Learn how to create a Container Registry in the Gcore Customer Portal and use it for managing OCI-compatible artifacts.
---
# Create a Container Registry

Container Registry provides a centralized location for all OCI-compatible artifacts, such as container images and Helm charts, making it easy to view and manage them in one place.

<alert-element type="info" title="Info">
 
Container Registry is currently in beta mode. To join the beta, contact the [Gcore support team](mailto:support@gcore.com). 
 
</alert-element>

Use the following steps to add a new registry. For instructions on how to manage an existing registry, check out our <a href="https://gcore.com/docs/cloud/container-registry/manage-container-registries" target="_blank">dedicated guide</a>. 

To create and manage the Container Registry, you need to have the <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#project-administrator" target="_blank">Project Administrator</a> or <a href="https://gcore.com/docs/cloud/getting-started/projects/users/user-roles-and-rights#client-administrator" target="_blank">Client Administrator</a> permissions.  

## Step 1. Add a registry to the Customer Portal

Start by creating a registry to which you will push OCI-compatible artifacts: 

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Container Registries**. 

2\. Click **Create Container Registry**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/container-registry-page-create.png" alt="Container registry page in the Customer Portal" width="80%"> 

3\. Choose the region for the registry location. If you plan to store and manage images for other Gcore services, select the same region where those services are created. 

4\. Specify the registry name. 

<alert-element type="tip" title="Tip">
 
A registry name should consist of lowercase Latin characters, which can be separated by dashes. 
 
</alert-element>

5\. Indicate the storage limit. It defines the amount of data that can be stored within the registry, including Docker images, artifacts, and image versions.  

6\. Click **Create Registry**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/create-registry.png" alt="Create Container registry dialog in the Customer Portal" width="80%"> 

The registry will appear along with the other registries on the **Container Registries** page.  

## Step 2. Create a user

To push and pull images from the registry, you need to authenticate as a particular user who has the required permissions for such operations.  

To add a new user to the registry: 

1\. Click the registry name to open it. 

2\. Open the **Users** tab and click **Add users**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/users-tab-empty.png" alt="Users tab with no users created" width="80%"> 

3\. Configure the user and its access: 

* **Username**: Enter a username. It should consist of lowercase Latin characters, which can be separated by dashes. 

* **Permissions**: Allow a user to either push or pull images to the registry or do both operations. 

* **Set activity duration**: enable this toggle to set the expiration date for user credentials. If you leave the toggle disabled, the user will retain indefinite access to the registry.  

4\. Click **Save**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/add-user.png" alt="Add users dialog" width="80%"> 

5\. Copy and save the generated user password because you won’t be able to check it again. If you forget the password, you’ll have to regenerate it. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/save-password.png" alt="A dialog with a username and password" width="80%"> 

You can now log in as the created user and push or pull images from the Container Registry, as described in the following steps.  

## Step 3. Push your image to the Container Registry

When you open a registry, you can view the sample push and pull commands by clicking the relevant buttons. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/push-pull-commands.png" alt="Registry overview page with highlighted push and pull buttons" width="80%"> 

To push a Docker image to the registry: 

1\. Log in to the registry: docker login `<your-registry-endpoint>`. For example, `docker login registry.luxembourg-2./10-01-test/`. 

2\. Enter the username of the user created in <a href="https://gcore.com/docs/cloud/container-registry/create-container-registry#step-2-create-a-user" target="_blank">Step</a>.  

3\. Enter the user password.  

4\. After you enter the credentials, you should see the “Login succeeded” message.  

5\. (Optional) Tag your image: `docker tag source_image:tag target_repository:target_tag`.  

6\. Push an image to the registry: `docker push <your-registry-endpoint/your-Docker-image>`.

The image will appear in the Container Registry on the **Images** tab. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/create-container-registry/images-tab.png" alt="Registry overview page with highlighted images tab" width="80%"> 

For instructions on how to view and manage images, check out the <a href="https://gcore.com/docs/cloud/container-registry/create-container-registry" target="_blank">Manage Container Registries</a> guide. 

## Step 4 (Optional). Pull the image from the Container Registry

If you want to test how to pull the image and verify that everything works as expected, use the following command:  

```
docker pull <your-registry-endpoint/your-Docker-image> 
```

The image will be pulled locally. 