---
title: manage-container-registries
displayName: Manage Container Registries
order: 20
published: true
toc:
   --1--Change storage limit: "change-storage-limit"
   --1--Manage images: "manage-images-in-the-container-registry"
   --2--View and manage image artifacts: "view-and-manage-image-artifacts"
   --2--Delete an image: "delete-an-image"
   --2--Delete multiple images: "delete-multiple-images-with-group-actions"
   --1--Manage users: "manage-users-in-the-container-registry"
   --2--Change user permissions: "change-user-permissions"
   --2--Reset user password: "reset-user-password"
   --2--Delete a user: "delete-a-user"
   --2--Delete multiple users: "delete-multiple-users-with-group-actions"
   --1--Delete a registry: "delete-a-registry"
pageTitle: Manage Container Registries | Gcore
pageDescription: Learn how to set up and manage Container Registries, their users, images, and related artifcacts in the Gcore Customer Portal.
---
# Manage Container Registries

All created Container Registries appear in the Gcore Customer Portal on the **Container Registries** page:

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/container-registry-page.png" alt="Container registry page in the Customer Portal" width="80%"> 

You can change the storage limit for a registry, configure its users and images, or delete the registry if you no longer need it. If you have a large number of registries, you can also use search to find the one that you’re looking for. 

<alert-element type="info" title="Info">
 
The Container Registry feature is currently in beta mode. To join the beta, contact the [Gcore support team](mailto:support@gcore.com). 
 
</alert-element>

## Change storage limit

You can adjust your storage limit to host more images in the container registry or optimize storage according to your usage and container requirements. 

To change the storage limit:  

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Container Registries**. 

2\. Find the registry you want to configure and click the three-dot icon next to it. 

3\. Click **Change storage limit**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/container-registry-change-limit.png" alt="Container registry settings with change limit button highlighted" width="80%"> 

4\. Enter a new limit and click **Save** to apply the changes.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/set-new-storage-limit.png" alt="A confirmation dialog to change storage limit" width="80%"> 

The storage limit has been changed. 

## Manage images in the Container Registry

Open the **Images** tab to view the following information about the images within your Container Registry: 

* Image name 

* Artifacts associated with the image 

* The number of times the image was pulled from the registry 

* The date and time when the image was last modified 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/images-tab-cropped.png" alt="Images tab in the registry overview" width="80%"> 

You can do the following actions with images: view and manage related artifacts, pull images from the registry, or delete them. You can also search through the images to find the one that you need.

### View and manage image artifacts

To view image artifacts, click the image name to open it. On the **Artifacts** page, you can check the artifact name, its tags, size, and the last associated push and pull operations. You can also search through the artifacts. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/image-artifacts.png" alt="Images tab with the list of image artifacts" width="80%"> 

To delete an artifact or its tag: 

1\. Find the needed artifact and click the three-dot icon next to it. 

2\. Select the required action from the dropdown and proceed with the instructions. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/delete-image-artifact.png" alt="Image settings with the highlighted delete and delete tags buttons" width="80%"> 

You can also apply group actions to multiple artifacts. To do so, select checkboxes next to the artifacts you want to manage and choose the needed action from the **Group actions** dropdown.

### Delete an image

1\. On the **Images** tab, find the image you want to remove.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/delete-image.png" alt="Image settings with the highlighted delete button" width="80%"> 

2\. Click the three-dot icon and select **Delete**. 

3\. Confirm your action by typing “Delete” in the text field. 

4\. Click **Delete Image**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/confirm-image-deletion.png" alt="Image deletion dialog" width="80%"> 

Your image has been removed from the registry.

### Delete multiple images with group actions

You can simultaneously delete multiple images with **Group actions**. To do so, select checkboxes next to the images you want to manage and use the required action from the dropdown.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/image-group-actions.png" alt="Group actions dropdown on the Images tab" width="80%"> 

## Manage users in the Container Registry

Open the Users tab to view the following information about created users within your Container Registry: 

* Username 

* User permissions  

* The date and time when the user was created 

* (Optional) If the password expiration date was set during user creation, this information will be displayed in the **Expires at** column. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/users-tab.png" alt="Users tab in the registry overview" width="80%"> 

You can change user permissions, generate a new user password, or delete the user from the registry. 

<alert-element type="tip" title="Tip">
 
For details on how to create a user, check the <a href="https://gcore.com/docs/cloud/container-registry/create-container-registry" target="_blank">Create a Container Registry</a> guide. 

</alert-element>

### Change user permissions

For each user, you can configure the following permissions: 

* **Pull images**: this is helpful if you’d like to prevent unauthorized or accidental changes to the Container Registry. In this case, you can restrict permissions for some users to pull operations only. 

* **Push and push images**: this permission grants full access to the registry and allows users to pull and push any new images or image versions to the registry.  

To change user permissions: 

1\. On the **Users** tab, find the user you want to delete and click the three-dot icon next to it.  

2\. Select **Change permissions**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/change-user-permissions.png" alt="Users settings with the highlighted change permissions button" width="80%"> 

3\. Update the permissions as needed and click **Save** to apply the changes.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/select-new-user-permissions.png" alt="Change permissions dialog" width="80%"> 

### Reset user password

A user password is automatically generated during user creation. If the password has expired or the user can’t remember it, you can regenerate a password as follows: 

1\. On the **Users** tab, find the user you want to delete and click the three-dot icon next to it.  

2\. Select **Reset password**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/reset-user-password.png" alt="Users settings with the highlighted reset password button" width="80%"> 

3\. Confirm password reset.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/confirm-password-reset.png" alt="Reset password confirmation dialog" width="80%"> 

4\. Copy the password and save it locally. Keep in mind that you won’t be able to view it again.  

### Delete a user

1\. On the **Users** tab, find the user you want to delete and click the three-dot icon next to it.  

2\. Select **Delete**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/delete-user.png" alt="Users settings with the highlighted delete button" width="80%"> 

3\. Confirm your action by typing “Delete” in the text field. 

4\. Click **Delete user**.

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/confirm-user-deletion.png" alt="Delete user confirmation dialog" width="80%"> 

### Manage multiple users with group actions

There’s an option to simultaneously delete multiple users or change their permissions using **Group actions**. To do so, select checkboxes next to the users you want to modify and then choose the needed action from the **Group actions** dropdown. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/group-actions-users.png" alt="Users settings with the highlighted group actions dropdown" width="80%"> 

## Delete a registry

<alert-element type="warning" title="Warning">
 
If you delete a Container Registry, you will lose all data stored there. This action can’t be reverted.  

</alert-element>

To delete a registry:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Container Registries**. 

2\. Find the registry you want to configure and click its name to open it.  

3\. In the top-right corner of the screen, click the **Actions** dropdown and select **Delete**. 

<img src="https://assets.gcore.pro/docs/cloud/container-registry/manage-container-registries/delete-registry.png" alt="Container registry page with the highlighed delete button" width="80%"> 

4\. Type “Delete” to validate your action.

The registry has been removed. 