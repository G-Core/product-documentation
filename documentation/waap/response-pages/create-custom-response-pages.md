---
title: create-custom-response-pages
displayName: Create custom response pages
published: true
order: 10
toc:
   --1--Step 1. Add a new page set for your account: "step-1-add-a-new-page-set-for-your-account"
   --1--Step 2. Give your page set a name: "step-2-give-your-page-set-a-name"
   --1--Step 3. Choose a page type you want to create: "step-3-choose-a-page-type-you-want-to-create"
   --1--Step 4. Configure the selected response page: "step-4-configure-the-selected-response-page"
   --1--Step 5. Configure page status: "step-5-configure-page-status"
   --1--Step 6. Finalize page setup: "step-6-finalize-page-setup"
   --1--Step 7. Associate the page with domains: "step-7-associate-the-page-with-domains"   
pageTitle: A guide on custom response pages | Gcore
pageDescription: Learn more about Gcore custom response pages.
---
# Create custom response pages

In some cases, you might need to personalize the <a href="https://gcore.com/docs/waap/response-pages" target="_blank">response page</a> displayed to users when a particular custom rule or WAAP policy is triggered. For instance, to add contact information, adjust the message according to your brand’s voice and tone, or provide additional validation instructions. 

To do so, you need to create a new custom response page, as described in the following instructions.  

<alert-element type="tip" title="Tip">
 
For guidelines on how to modify or delete custom response pages, as well as change domains where those pages appear, check out the <a href="https://gcore.com/docs/waap/response-pages/manage-custom-response-pages" target="_blank">Manage custom response pages</a> guide. 
 
</alert-element>

## Create a custom response page 

Creating custom response pages allows you to display different messages to your users based on which domains they are navigating to. You can create up to 6 page sets. 

Note that creating custom response pages is only available <a href="https://gcore.com/docs/waap/response-pages/manage-custom-response-pages#manage-custom-response-pages-at-the-account-level" target="_blank">at the account level</a>. You can’t add and modify pages in domain settings.  

### Step 1. Add a new page set for your account 

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a> navigate to **WAAP** > **Features**. You'll be directed to Custom response pages. 

2\. In the upper-right corner of the screen, click **Create Custom Page Set**.

<img src="https://assets.gcore.pro/docs/waap/response-pages/create-page-set-button.png" alt="Highlighted button for creating response page in the Customer Portal" width="80%">

### Step 2. Give your page set a name

1\. Enter a unique name for your page set that's easy to distinguish from the default response pages. The name can be up to 50 characters long.  

2\. Click **Continue to pages** to proceed with the next steps. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/continue-to-pages.png" alt="Create response page set dialog" width="80%">

### Step 3. Configure the selected response page 

1\. In the **Create pages** section, click **Add page**. 

2\. In the sidebar menu that opens, choose the default page type that you want to customize: 

* Browser validation  
* Enable cookies  
* Enable JavaScript   
* Captcha  
* Block  
* Block CSRF 

<img src="https://assets.gcore.pro/docs/waap/response-pages/choose-page-type.png" alt="Crete response page set dialog" width="80%">

### Step 4. Configure the selected response page 

Configure the default response page you’ve selected in the previous step. Note that page customization options will vary depending on the type of page you want to modify. 

#### Browser title 

Add the text that will appear as the title in your web browser's tab where the custom response page is open. The title can be up to 60 characters.  

You can add browser title to the following response pages: Browser validation, Captcha, Block, Block CSRF. 

#### Page title 

Provide the name of your custom page. You can add a page title to all response pages.  

For example, in following screenshot, the text “Sorry, you’ve been blocked” is a page title. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/block-page.png" alt="Block response page" width="80%">

#### Page message 

Enter a body text that will be displayed under the page title. This is a good place to explain why a user has been challenged or blocked and what they should do to pass the check or obtain access to a domain. 

You can add a message to all response pages except for Browser validation. 

For example, in the following screenshot, the message informs users that they need to have JavaScript enabled to access the domain. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/enable-js.png" alt="Enable JavaScript response page" width="80%">

#### Error message 

Provide a message that will be displayed when a client fails to pass the validation. This is only available for a Captcha page. 

#### Upload image (optional) 

Add an image that’ll appear on the page. The image should be in png, svg, or jpg format and have the following dimensions: 460px *130 px, 24KB maximum size.  If you don’t upload an image, then the default image will be applied. 

You can add images to the following response pages: Browser validation, Captcha, Block, Block CSRF. 

Here’s an example of a Block CSRF page with the default Gcore image: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/block-csrf.png" alt="Block CSRF response page" width="80%">

### Step 5. Configure page status 

Optionally, you can enable the **Page active status** toggle to make the custom response page publicly available after creation.  

If you don’t enable the toggle, the page won’t be available for use on any domains, and the default response pages will be used instead. In such a case, you’ll need to manually change its status to **Active**. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/page-status-active-toggle.png" alt="Set page to active toggle enabled" width="80%">

### Step 6. Finalize page setup 

1\. Click **Preview page** to check what it’ll look like.  

2\. If you’re satisfied with the changes, click **Save** to create the page.  

3\. Click **Continue to domains** to proceed with the next steps. 

<img src="https://assets.gcore.pro/docs/waap/response-pages/preview-page-button.png" alt="Preview page button" width="80%">

### Step 7. Associate the page with domains 

1\. Select the domains where the new custom response page will appear.

<img src="https://assets.gcore.pro/docs/waap/response-pages/add-domains-to-new-set.png" alt="Preview page button" width="80%">

2\. Click **Save** to add the page to the selected domains.

Your page will be created with the **Unpublished** state. It’ll change to **Published** after a few moments. 

<alert-element type="info" title="Info">
 
For instructions on how to edit and delete custom response pages, as well as change associated domains, check out the <a href="https://gcore.com/docs/waap/response-pages/manage-custom-response-pages" target="_blank">Manage custom response pages</a> guide.
 
</alert-element>