---
title: create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files
displayName: Create a rule
published: true
order: 10
toc:
   --1--What is the Rules section?: "what-is-the-rules-section"
   --1--Create rules: "add-rules-in-the-control-panel"
   --2--manually: "create-a-rule-manually"
   --2--from a template: "create-a-rule-from-a-template"
   --1--Examples of rules: "examples-of-rules"
   --2--prohibit image caching: "prohibit-image-caching-in-cdn"
   --2--set CORS for .ttf: "set-access-control-allow-origin-for-ttf-files"
   --1--Disable or enable a rule: "disable-or-enable-a-rule"
pageTitle: Understanding of Rule Creation | Gcore
pageDescription: A guide on how to create a rule manually or from a template.
---
# Create a rule manually or from a template to configure settings for particular files
  
## What is the Rules section?

The Rules section is where you can set CDN options for specified files (unlike in the Resource Settings tab, where you can set options for all files).

For example, you have enabled <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin" target="_blank">CDN caching settings</a> for your resource and set the CDN-controlled option. These settings apply to all files. But for some files, you need to select the Origin-Controlled option. To do that, you need to create the corresponding rule, specifying the paths of these files and adding the Origin-Controlled option. In this case, CDN-Controlled will apply to all files except those specified, where Origin-Controlled will apply.

There is one limitation for the Rules feature: You can add only five custom rules for a CDN resource. You can see how many rules you’ve created in the Rules section.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/11774615568017.png" alt="What is the Rules section" width="80%">

## Add rules in the control panel

### Create a rule manually

1\. Open the Resource settings and go to the Rules tab. Click the **Create rule** button and select **Create blank rule** from the drop-down list.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/11774713174673.png" alt="Create a rule manually" width="80%">

A new page will open. Follow the remaining steps on that page.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612312879889.png" alt="Create a rule manually" width="60%">

2\. Enter the rule name.

3\. Specify the path to the file or folder for which the rule will be applied. The path must start with “**^/**” or “**/**” and cannot contain the domain name of your origin. You can specify a URI or use <a href="https://en.wikipedia.org/wiki/Regular_expression" target="_blank">regular expressions (regex)</a>.

**Note**: If a URI matches multiple rules, the one higher in the order of the rules will be applied. For example, there are two rules on the resource: ```/folder/.*``` (the first rule) and ```/folder/image.jpg``` (the second rule). The first rule will be applied to the ```/folder/image file.jpg``` file.

4\. Select the protocol that the CDN resource will use to pull the files specified in step 4. If files are accessible over the same protocol as the origin, select “Inherit from resource”. If not, select the appropriate option: HTTP, HTTPS, or both protocols at once.

5\. Click the **Add option** button to configure options if necessary. This will bring up the list of options. Click on the options needed (they will be added on the rule creation page), and then click **Close**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612312882577.png" alt="Add option " width="60%">

There are three variants for how the options in the Rules sections interact with the options in the Resource Settings:

| Variant                                         | Interaction method                                              | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Options are not added to the rule               | Option parameters will be inherited from the Resource settings  | You enable the CDN caching option in the Resource settings and then create a rule where you don’t add the CDN caching option. In this case, the caching parameters for the files specified in the rule will be inherited from the appropriate option in the Resource settings.                                                                                                                                                                          |
| An option is added to the rule, but is disabled | Option parameters from the Resource Settings will be disabled   | You enable the Country access policy option with the Allow by default and DE values in the Resource settings. It means that access to all content is restricted in Germany. Then, you add a rule with the disabled <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies#country-access-policy" target="_blank">Country access policy</a> option. In this case, the option parameters from the Resource Settings will not be considered for the content specified in the rule. This means that files specified in the rule will be available in Germany. |
| An option is added to the rule and enabled      | Option parameters from the Resource Settings will be overridden | You enable the Browser caching option with the CDN-Controlled and 4 days values in the Resource Settings. Then, you add a rule with the enabled <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-for-user-browsers" target="_blank">Browser caching</a> option and 30 minutes value. In this case, the files specified in the rule will be cached in the browser for 30 minutes. The rest of the files will be cached for 4 days.                                                                                                               |

6\. Save changes.

### Create a rule from a template

You can use a template to create rules. This is helpful in two cases:

- When you have several resources that require the same kind of rules. You can create one template and use it to add rules for all of your resources.
- When you need to use standard rules for some options (Image Optimization, Streaming via CDN) or operations (Let’s Encrypt issuing by HTTP-01 challenge). You can use our system templates for these purposes.

You can find more information about templates in the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one" target="_blank">Create a CDN resource rule template manually or use a system one</a>" guide.

To create a rule from a template:

1\. Open the settings of the required CDN resource. In the Rules tab, click **Create rule** and select a template from the list.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/11774651473681.png" alt="CDN resource" width="80%">

2\. You will see the form for creating a new rule with pre-filled settings from the template. Check if all the settings suit you; edit the rule if necessary following to the [Create a rule manually](https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files#create-a-rule-manually) section of this article.

3\. Click **Create rule**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/11774588523793.png" alt="Create rule" width="50%">

## Examples of rules

### Prohibit image caching in CDN

To prohibit image caching in CDN:

- Enter **^/.(jpg|css|js)$** to the Rule pattern field.
- Add the CDN caching option with the "CDN Controlled" and "Do not cache" values.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612313082513.png" alt="Prohibit image caching in CDN" width="60%">

### Set Access-Control-Allow-Origin for .ttf files

To set up the Access-Control-Allow-Origin HTTP header only for files with the .ttf extension:

- Enter **/.ttf$** to the Rule pattern field to the Rule pattern field.
- Add the CORS header support option.
- Configure which domains to add the header for. You can find more information about configuring in the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/add-the-access-control-allow-origin-header-to-the-browser-response" target="_blank">Enable CORS header support</a>" guide.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612313089169.png" alt="Set Access-Control-Allow-Origin for .ttf files" width="80%">

## Disable or enable a rule

For some purposes (e.g., testing), you may want to disable rules you’ve created. In this case, the rule will not apply to the specified files, but will still count toward the rule limit.

To disable or enable a rule:

1\. Go to the **Rules** section and open the page for the desired rule.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/11774706636945.png" alt="Rules section " width="80%">

2\. Click **Disable rule** (or **Enable rule**), then click **Save changes**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612313157393.png" alt="Disable rule" width="50%">

Disabled rules will have a Suspended status and enabled rules will have an Active status.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files/10612307136657.png" alt="Suspended status and" width="80%">
