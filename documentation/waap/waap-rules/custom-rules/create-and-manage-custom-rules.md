---
title: create-and-manage-custom-rules
displayName: Create and manage custom rules
published: true
order: 10
toc:
   --1--Create custom WAAP rules: "create-custom-waap-rules"
   --1--Custom rule examples: "examples-of-custom-rule-definitions"
   --2--IP conditions: "rules-with-ip-conditions"
   --2--IP range conditions: "rules-with-ip-range-conditions"
   --2--URL conditions: "rules-with-url-conditions"
   --2--User agent conditions: "rules-with-user-agent-conditions"
   --2--Header conditions: "rules-with-header-conditions"
   --2--Header exists conditions: "rules-with-header-exists-conditions"
   --2--HTTP method conditions: "rules-with-http-method-conditions"
   --2--File extension conditions: "rules-with-file-extension-conditions"
   --2--Content type conditions: "rules-with-content-type-conditions"
   --2--Country conditions: "rules-with-country-conditions"
   --2--Organization conditions: "rules-with-organization-conditions"
   --2--Owner types conditions: "rules-with-owner-types-conditions"
   --2--Session request count conditions: "rules-with-session-request-count-conditions"
   --2--Tag conditions: "rules-with-tag-conditions"
   --2--User defined tag conditions: "rules-with-user-defined-tag-conditions"
   --1--Create rate limit rules: "create-custom-rate-limit-rules"
   --1--Manage existing rules: "manage-existing-rules"
   --2--Edit a rule: "edit-a-rule"
   --2--Delete a rule: "delete-a-rule"
pageTitle: Learn how to add new custom rules and manage the existing ones | Gcore
pageDescription: Learn how to use WAAP custom rules for filtering incoming traffic and blocking malicious requests.
---
# Create and manage custom rules

Custom rules allow you to fine-tune WAF behavior in response to potential security threats. 

You can create the following types of custom rules: <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/create-and-manage-custom-rules#create-custom-waap-rules" target="_blank">custom WAAP rules</a> with if/then conditions or <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/create-and-manage-custom-rules#create-custom-rate-limit-rules" target="_blank">custom rate limit rules</a> that restrict the number of allowed requests for a specific period. 

## Create custom WAAP rules

These rules come with great customization: you can use multiple conditions and constraints to tailor rules to a specific use case.

<alert-element type="tip" title="Tip">
 
If you're looking for more flexibility in creating rules, check our <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules" target="_blank">advanced rules</a>. They offer extended functionality and more customization, such as using the "OR" function that's not available in custom rules. 
 
</alert-element>

To create a new WAF rule:  

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it.  

3\. In the sidebar, navigate to **WAAP Rules**.  

4\. Click **Add custom rule** and configure your rule as follows: 

* **Rule name**: enter a descriptive name for your rule.  

* **Rule status**: enable this toggle if you want to activate the rule after creation. Otherwise, the rule will be disabled, and you’ll need to enable it later.  

* **Rule type**: choose WAF rule. 

* **Description** (optional): provide more context about your rule. 

5\. Define the rule by setting up a condition (IF). The rule structure will differ depending on the rule type. Check out the following sections for guidelines on how to create rules for different use cases.  

6\. (Optional) Next to **AND**, create a second condition to complement the first condition.

<alert-element type="tip" title="Tip">
 
If you create multiple conditions, the rule will only trigger when all conditions are met.
 
</alert-element>

7\. Next to **THEN**, select an action type: Monitor, Allow, Block, Captcha, JavaScript Validation, Tag. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/add-custom-rule.png" alt="Add custom rule page in the Customer Portal">

8\. Click **Save**.  

You’ve successfully created the rule.

## Examples of custom rule definitions

This section provides examples of custom rules that are configured with different types of conditions. 

<alert-element type="warning" title="Warning">

Be cautious when creating rules with **NOT Exact** conditions and **Block** actions for IPs and IP ranges. Such rules will block traffic from any IP address that doesn't exactly match the one specified in the rule. 

For example, if you create the rule "IP is NOT Exact 1.1.1.1", it will block any traffic to your domain except for the one coming from 1.1.1.1.

</alert-element>

### Rules with IP conditions

Rules that contain the IP condition allow you to enforce security controls on incoming traffic based on the IP address of a request. You can create rules to manage traffic for both IPv4 and IPv6 addresses.

To create a rule: 

1\. In the **IF** section, select **IP** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every IP address except for the specified one. To apply the rule only to the specified address, select **--**.  

3\. Enter the IP address. To enter multiple addresses, separate each address with a comma. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered.  

6\. Click **Save**.  

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/ip-rule-definition.png" alt="A sample definition of a rule with IP condition">

### Rules with IP range conditions 

Rules that contain the IP range condition allow you to enforce security controls on incoming traffic based on the specified IP address range. You can create rules to manage traffic for both IPv4 and IPv6 addresses.

To create a rule: 

1\. In the **IF** section, select the **IP range** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every IP range except for the specified one. To apply the rule only to the specified range, select **--**.  

3\. In the text fields, enter the first and the last addresses of the IP range. You can specify up to 30 networks in a single range. Subnet masks are not supported.

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/ip-range-rule-definition.png" alt="A sample definition of a rule with IP range condition">

### Rules with URL conditions

Rules that contain the URL condition allow you to enforce security controls on incoming traffic based on a specific URL. 

To create a rule: 

1\. In the **IF** section, select **URL** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every URL except for the specified one. To apply the rule only to the specified URL, select **--**. 

3\. Define match criteria: 

* Select **Equals** to apply the rule only when the requested URL exactly matches the specified one. For example, if the specified URL is /blog, then when a request is made to /blog, the rule will trigger. If a request is made to /blogarticle, the rule won’t work. 

* Select **Contains** to apply the rule when the requested URL partly matches the specified one. For example, if the specified URL is /blog, then when a request is made to /blog, the rule will trigger. If a request is made to /blogarticle, the rule will work as well. 

4\. In the text field, enter your URL. If you selected Equals in the previous step, you must start the URL with a slash ( / ). 

5\. (Optional) Select another condition in the **AND** section.  

6\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

7\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/url-rule-definition.png" alt="A sample definition of a rule with URL condition">

### Rules with user agent conditions 

Rules that contain the User agent condition allow you to enforce security controls on incoming traffic based on the specified user agent in a request. 

To create a rule: 

1\. In the **IF** section, select **User agent** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every user agent except for the specified one. To apply the rule only to the specified user agent, select **--**. 

3\. Define match criteria: 

* Select **Equals** to apply the rule only when the user agent exactly matches the one you’ve entered. For example, you might add a user agent like Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36.  

* Select **Contains** to apply the rule when the user agent partly matches the specified one. For example, if you enter AppleWebKit, any AppleWebKit user agent will trigger the rule. You can still enter a specific user agent, and any requesting user agent that partially matches the header will trigger the rule.  

4\. In the text field, enter the user agent.  

5\. (Optional) Select another condition in the **AND** section.  

6\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

7\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/user-agent-rule-definition.png" alt="A sample definition of a rule with user agent condition">

### Rules with header conditions 

Rules that contain the Header condition allow you to enforce security controls on incoming traffic based on request headers. In contrast to "header exists" conditions, the “header” ones also validate the value of the header. 

To create a rule: 

1\. In the **IF** section, select **Header** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every header except for the specified one. To apply the rule only to the specified header, select **--**.  

3\. In the text field, enter a header key.  

4\. Define match criteria: 

* Select **Equals** to apply the rule only when the request header exactly matches what you’ve specified.  

* Select **Contains** to apply the rule when the header partly matches what you’ve specified. In this case, you can enter a generic header, and any requesting header that matches this generic one will trigger the rule.  

5\. Enter the header value. 

6\. (Optional) Select another condition in the **AND** section.  

7\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

8\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/header-rule-definition.png" alt="A sample definition of a rule with header condition">

### Rules with header exists conditions 

Rules that contain the Header exists condition allow you to challenge requests depending on whether a specific header name is present in the request. They don’t check the header value. 

To create a rule: 

1\. In the **IF** section, select **Header Exists** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every header except for the specified one. To apply the rule only to the specified header, select **--**.  

3\. Enter a header key.  

6\. (Optional) Select another condition in the **AND** section.  

7\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

8\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/header-exists-rule-definition.png" alt="A sample definition of a rule with header exists condition">

### Rules with HTTP method conditions 

Rules that contain the HTTP header conditions allow you to enforce security controls on incoming traffic based on provided request methods.  

To create a rule: 

1\. In the **IF** section, select **HTTP method** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every method except for the specified one. To apply the rule only to the specified method, select **--**.  

3\. Select the HTTP method. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/http-method-rule-definition.png" alt="A sample definition of a rule with httm method condition">

### Rules with file extension conditions  

Rules that contain the File extension condition allow you to enforce security controls on incoming traffic based on a file type. 

To create a rule: 

1\. In the **IF** section, select **File extension** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every file except for the specified one. To apply the rule only to the specified file, select **--**. 

3\. In the text field, enter the file extension. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/file-extension-rule-definition.png" alt="A sample definition of a rule with file extension condition">

### Rules with content type conditions  

Rules that contain the Content type conditions allow you to enforce security controls on incoming traffic based on a specific content type. 

To create a rule: 

1\. In the **IF** section, select **Content type** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every content type except for the specified one. To apply the rule only to the specified type of content, select **--**. 

3\. In the text field, enter the content type. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/content-type-rule-definition.png" alt="A sample definition of a rule with content type condition">

### Rules with country conditions  

Rules that contain the Country condition allow you to enforce security controls on incoming traffic based on a country that the request comes from. 

To create a rule: 

1\. In the **IF** section, select **Country** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every country except for the specified one. To apply the rule only to the specified country, select **--**. 

3\. Choose the country. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/country-rule-definition.png" alt="A sample definition of a rule with country condition">

### Rules with organization conditions  

Rules that contain the Organization condition allow you to enforce security controls on incoming traffic based on a specific organization that the request comes from. 

To create a rule: 

1\. In the **IF** section, select **Organization** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every organization except for the specified one. To apply the rule only to the specified organization, select **--**. 

3\. Choose the organization. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/organization-rule-definition.png" alt="A sample definition of a rule with organization condition">

### Rules with owner types conditions  

Rules that contain the Owner types condition allow you to enforce security controls on incoming traffic based on a specific category associated with a related IP range. Such categories can be Commercial, Educational, or Government. The information about these owner-type categories is pulled from the <a href="https://who.is/" target="_blank">global WHOIS database</a>. 

To create a rule: 

1\. In the **IF** section, select **Owner types** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every owner type except for the specified one. To apply the rule only to the specified owner type, select **--**. 

3\. Choose the Owner type from the dropdown. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/owner-types-rule-definition.png" alt="A sample definition of a rule with owner types condition">

### Rules with session request count conditions 

Rules that contain the Sesion request count condition allow you to enforce security controls on incoming traffic based on the number of requests made in a session (per session ID). 

To create a rule: 

1\. In the **IF** section, select **Session request count** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule if the total number of requests in the session is anything other than the specified one. To apply the rule only when the total number of requests in the session is exactly as specified, select **--**. 

3\. Enter a particular number of requests. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/session-request-count-rule-definition.png" alt="A sample definition of a rule with session request count condition">

### Rules with tag conditions 

Rules that contain the Tag condition allow you to enforce security controls on incoming traffic based on a specific tag within the request. For more details on how to create and manage tags, check out Tag generating rules.  

To create a rule: 

1\. In the **IF** section, select **Tag** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every tag except for the specified one. To apply the rule only to the specified tag, select **--**. 

3\. Enter the tag. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/tag-rule-definition.png" alt="A sample definition of a rule with tag condition">

### Rules with user-defined tag conditions 

Rules that contain the User defined tag condition allow you to enforce security controls on incoming traffic based on a specific user-defined tag within the request. 

To create a rule: 

1\. In the **IF** section, select **User-defined tag** from the dropdown. 

2\. In the following dropdown, select **Not** to apply the rule to every tag except for the specified one. To apply the rule only to the specified tag, select **--**. 

3\. Choose one or more user-defined tags. 

4\. (Optional) Select another condition in the **AND** section.  

5\. In the **THEN** section, select the needed action that will be enforced when the rule is triggered. 

6\. Click **Save**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/user-defined-tag-rule-definition.png" alt="A sample definition of a rule with user-defined tag condition">

## Create custom rate limit rules 

You can create a rate limit rule to limit the number of requests users are allowed to perform against a specific URL. The information about request frequency can also be used to learn about user interaction with your domain. 

To create a rule: 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it.  

3\. In the sidebar, navigate to **WAAP Rules**.   

4\. Click **Add custom rule** and configure your rule as follows: 

* **Rule name**: enter a descriptive name for your rule.  

* **Rule status**: enable this toggle if you want to activate the rule after creation. Otherwise, the rule will be disabled, and you can enable it later.  

* **Rule type**: choose Rate limit rule. 

* **Description** (optional): provide more context about your rule. 

5\. Under **Number of requests**, specify how many requests are required to trigger the rule. 

<alert-element type="info" title="Info">
 
The minimum number of requests required to trigger a request rate condition is 21.
 
</alert-element>

6\. In the **Duration** field, set the time frame for how long the requests will be counted. After this period, the requests will be blocked. We recommend selecting a short time frame (30 seconds or a minute). 

<alert-element type="info" title="Info">
 
The **Duration** field determines the number of requests that will be counted within the specified timeframe. You can’t change the duration of actions (e.g. for how long user requests will be blocked) in the rate limit rules. This is only possible by using the `actionDuration` parameter from our API.  
 
</alert-element>

7\. Select the action that will be applied to each request when the rule is triggered. You can find a detailed overview of rule actions in our <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">rules overview guide</a>. Consider that actions aren’t permanent as they will continue to trigger only until the specified duration time is over. Once this time has passed, the request counter will reset and start again.  

8\. (Optional) In the **user-defined tag**, you can apply any custom tag you’ve created. 

9\. (Optional) In **Path regex**, specify the regular expression with a page path or URL: 

* To protect all application pages, leave the field blank or enter a slash ( / ). 

* To protect a specific page, enter a URL, such as /login. 

10\. (Optional) In **HTTP methods**, select one or more methods that will be included in the rule. In this case, the rule will only be triggered if the customer has specified certain request methods. If no specific methods were chosen by the customer, the rule will apply to all request methods. 
By default, the rule will include all HTTP methods. 

11\. (Optional) In **IP address**, enter a specific IP address to which the rule will apply. By default, the rule applies to all IP addresses that use the application. You can enter multiple IP addresses, one address per line. 

<alert-element type="info" title="Info">

If you specify a URL, HTTP method, or IP address, the rule will only apply to requests that match these fields. If you leave these fields empty, then the rule will be enforced on all requests. 

</alert-element>

12\. Click **Save**.

## Manage existing rules 

You can edit the rule name and description, modify its conditions and status, and delete the rule if you no longer need it. If you have many rules, you can also search for rules by name to find the one you need. 

### Edit a rule 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it.  

3\. In the sidebar, navigate to **WAAP Rules**.   

4\. Find the desired rule and click the three-dot icon to open the settings. 

5\. Click **Edit**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/edit-rule.png" alt="Rule settings with the edit button highlighted">

6\. Adjust your rule as needed and then click **Save** to apply the changes. 

### Delete a rule 

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the needed domain and click its name to open it.  

3\. In the sidebar, navigate to **WAAP Rules**.   

4\. Find the desired rule and click the three-dot icon to open the settings. 

5\. Click **Delete**. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/create-and-manage-custom-rules/delete-rule.png" alt="Rule settings with the delete button highlighted">

6\. Click **Confirm Delete** to verify your action.

The custom rule has been removed.
