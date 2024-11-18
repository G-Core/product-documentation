---
title: manage-custom-response-pages
displayName: Manage custom response pages
published: true
order: 20
pageTitle: A guide on managing custom response pages | Gcore
pageDescription: Learn how to manage Gcore custom response pages in the domain settings and at the account level.
---
# Manage custom response pages

There are two ways to access custom response pages: at the **domain** level and at the **account** level. The key difference is that at the domain level, you can only switch between page sets, and it’s not possible to add, modify, or delete pages there.  

<alert-element type="info" title="Info">

For guidelines on how to create custom response pages, check out <a href="https://gcore.com/docs/waap/response-pages/create-custom-response-pages" target="_blank">Create custom response pages</a> guide. 
 
</alert-element>

## Manage custom response pages at the account level 

Custom response pages that are available at the account level relate to all domains in your account. This means that you can modify pages or page sets, and the changes will be inherited by all domains where those pages are active.  

To view page sets, open the **WAAP** page and navigate to **Features**. You'll be directed to the page with all relevant settings. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/response-pages-account-level.png" alt="Response pages functionality in the Customer Portal" width="80%">

Here you can view <a href="https://gcore.com/docs/waap/response-pages#types-of-response-pages" target="_blank">default response pages</a> as well as add, customize, or delete your own custom page sets, which are based on the default ones.  

Each custom response page can have one of the following statuses: 

* **Active**: A page appears on your domain and is visible to users.  

* **Inactive**: A page is created but not publicly available.  

A page set statuses can be:

* **Unpublished**: A page set can get this status after creation. After a short period, it should change to **Published**. 

* **Published**: A page set is ready to use. This means that all pages inside it are in the **Active** status.  

## Manage custom response pages at the domain level 

A domain can have only one active page set at a time.  

To view or change page sets: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**. 

2\. Find the needed domain and click its name to open it. You'll be directed to the **Policies** page. 

3\. In the sidebar, click **Custom response pages**. On this page,  you’ll see all response pages that are currently applied to your domain.  

4\. (Optional) To change a page set, click **Set as active** next to the desired page set.

<alert-element type="info" title="Info">

If your domain has no active page sets, the <a href="https://gcore.com/docs/waap/response-pages#types-of-response-pages" target="_blank">default response pages</a> will be used instead. 
 
</alert-element>

## Update a page set 

You can apply the following actions to the whole set with your custom response pages: select domains where this page set will be applied, add a new page to the page set, edit one of the existing pages, or delete the page set altogether.

Updating custom response pages is only possible on the account level.

<img src="https://assets.gcore.pro/docs/waap/response-pages/update-page-set.png" alt="Update page set on the account level" width="80%">

The process of adding, editing, and removing pages in an existing set are the same as for individual pages: 

* <a href="https://gcore.com/docs/waap/response-pages/create-custom-response-pages" target="_blank">Create custom response pages</a>

* <a href="https://gcore.com/docs/waap/response-pages/manage-custom-response-pages#update-custom-response-pages" target="_blank">Update  custom response pages</a>

### Add a page set to domains

<alert-element type="info" title="Info">
 
If you don’t add customized pages to a domain, one of the <a href="https://gcore.com/docs/waap/response-pages#types-of-response-pages" target="_blank">default response pages</a> will be used instead.
 
</alert-element>

You can apply custom response pages to any domain of your choice. To add a page to a domain: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Features**. You'll be directed to the Custom response pages. Here you’ll see all default and custom response pages.  

2\. Find the page set that you want to modify, and click three-dot icon next to it.

3\. Choose **Select domains**. Click the checkbox next to all domains you would like to apply this page set. If the list is extensive, search for desired domains.

<img src="https://assets.gcore.pro/docs/waap/response-pages/add-page-set-to-domain.png" alt="Add domains to a page set on the account level" width="80%">

4\. Click **Save selection**.  

5\. Confirm your action by clicking **Confirm**. Any pages used on the domain will be replaced by this new page set.

### Update custom response pages 

You can modify various aspects of custom response pages, such as images, tab titles, or error messages. However, changing the page type itself is not possible. For example, you can’t convert a Captcha page into a Block page. If you need a different page type, you must create a new response page of the desired type. 

<alert-element type="info" title="Info">

If you modify a created page in a page set, the changes will be reflected on all domains using that set. 

</alert-element>

To update an existing page: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Features**. You'll be directed to Custom response pages. 

2\. Find the page set that you want to modify and click the three-dot icon next to it. 

3\. Select **Edit page**.

<img src="https://assets.gcore.pro/docs/waap/response-pages/edit-page.png" alt="Edit page button in the page set settings" width="80%">

## Delete custom response pages 

After you delete a page set, any domains that are currently using it will automatically revert back to the default response ages. You can’t restore deleted pages. 

To delete a page: 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Features**. You'll be directed to Custom response pages. 

2\. Find the page set that you want to modify and click the three-dot icon next to it. 

3\. Select **Delete**. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/delete-page.png" alt="Delete page button in the page set settings" width="80%">

4\. Click **Delete**.

Your page has been successfully removed and will no longer be displayed on any domains where it was previously used. 