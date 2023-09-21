---
title: add-custom-rules-for-processing-requests
displayName: Create rules
published: true
order: 20
toc:
   --1--About the Rules feature: "what-is-the-rules-tab"
   --1--Why use the feature?: "why-use-the-feature"
   --1--How to use the feature: "how-to-use-the-feature"
   --2--Create a rule: "add-a-new-rule"
   --2--Configure conditions (If section): "configure-set-conditions-for-the-rule-if-section"
   --2--Add rules (Then section): "add-a-rule-for-processing-requests-then-section"
pageTitle: Customize WAF Security Rules | Gcore
pageDescription: Learn how to add and configure custom WAF rules to secure your applications better, helping to prevent malicious requests and increase overall security.
---
# Add custom rules for processing requests
  
## What is the Rules tab

By default, WAF uses two built-in libraries to analyze requests to protect the application:

- The first library analyzes all requests for the presence of various signs of attacks. If any are found, it forwards the request to the second library.
- The second one checks the received request. If it confirms the signs of an attack, the malicious request is blocked. If not, the request will be marked as legitimate and will not be blocked.

On the "Rules" tab, you can add custom rules to adjust the default behavior of WAF when processing requests. This is what the tab with created rules looks like:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/11774209838097.png" alt="Rules tab" width="80%">

The priority of custom rules is higher than it is for ones from the default libraries. If a request has signs of an attack but you’ve added a custom rule to ignore this attack type, the request will be marked as legitimate and will not be blocked. If a custom rule doesn’t exist, WAF will block this request.

When you create rules, you specify conditions for various HTTP request parameters—the URI, method, header, etc.—and rules that determine how WAF should process the request. All requests that come to the application are matched against the specified conditions. If a request matches the conditions, the action from the rule is applied to it. If not, it’s handled by the default WAF libraries. For more information about the conditions, see "[How to use the feature](https://gcore.com/docs/web-security/manage-waf/add-custom-rules-for-processing-requests#how-to-use-the-feature)".

Created rules are automatically grouped into branches based on general conditions and the endpoint (the URI you specified). The top will always be the branch with the highest-level endpoint (e.g., the application root), and the bottom will have branches with lower-level endpoints (e.g., a specific section of the application or a specific file). You can also create rules that won’t be linked to any endpoint. These are called ‘Default rules’ and are inherited by all other branches.

In the example below, the rules are grouped into six branches by endpoints. The branch with the common _backend_ endpoint is on the first line. Other branches (2, 3, 4) also have this endpoint in the path (e.g., _**backend**/editor_). But the first branch is higher because it has the most common condition: /*\*.\*.\* (two asterisks mean any number of nested paths). The tab also has one default rule without specified endpoints. To view it, click the **Default rules** button.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910984238225.png" alt="Rules tab" width="80%">

If you click on a branch, a list of rules attached to it opens. For example, opening the sixth branch includes four distinct rules with specific conditions and one inherited rule from the Default rule. To view it, click the **Distinct and inherited rules** button.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910977514129.png" alt="Rules tab" width="80%">

## Why use the feature?

Let us show a few examples of when rules would be useful.

**Change the default handling of some requests**. The X-AUTHTOKEN custom header is used for authorization on your site. WAF handles the values of this header with the _base64_ parser. This parser may determine some specific symbol combinations in the values (e.g., the = symbol at the end) as a sign of an attack. Because of this, users’ authorization requests can be blocked. To prevent WAF from identifying legitimate requests as malicious, you can create a rule with the *base64* parser for authorization requests disabled.

**Increase the security of your custom application**. Your application is self-developed and not built on an open-source engine (e.g., CMS WordPress, etc.). In this case, the WAF signatures will not be aware of your application’s vulnerabilities because its architecture is more specific than commonly known engines. To improve your application’s security, create rules based on your information about potential vulnerabilities.

## How to use the feature

### Add a new rule

Go to the Rules tab and press the **Add Rule** button.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/11774233052817.png" alt="Rules tab" width="80%">

You can add a rule from the section’s main page or open one of the existing branches and create a rule based on it.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910977570449.png" alt="Rules tab" width="50%">

A shutter will appear on the right side of the screen. Here you should configure conditions in the **If request is** section and add a rule for processing requests in the **Then** section according to the instructions below. Users’ requests will be fulfilled with the specified conditions. If they match, the defined actions will be applied to the requests.

Afterward, press the **Create** button.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910977585937.png" alt="Create rules tab" width="80%">

Note that after the rule’s creation, changes don’t approve immediately. It takes some time to compile the rules and add them to the WAF filtering nodes.

### Configure set conditions for the rule (If section)

You can configure the set of conditions in two ways:

- In advanced form
- In one string.

The second way requires specific knowledge of how to describe the conditions branch via the URI. In this article, we’ll only consider the advanced form method. To configure the set of conditions by advanced form, do the steps below.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910977632785.png" alt="advanced form" width="80%">

1\. Select the HTTP method (POST, GET, PUT, PATCH, DELETE) in the drop-down list or leave the field empty if you want to consider all methods.

2\. Specify the endpoint without the app’s domain (The URL which will be requested) in the field.

If you want to create the default rule, leave this field blank and go to the next step. The field will be automatically filled with the **/\*\*/\*.\*** array.

3\. Press the arrow on the right to open the advanced form. If you specify the endpoint, appeared fields will be filled with the values from the previous step. If you don’t, all fields will be empty.

4. Press the **Add condition** button after adding each condition.

5\. Select the parameters from the drop-down list for the condition. The specified value will be taken for comparison with the users’ requests to your application.

There are six available parameters:

- **header** — the request header. If you choose it, the most common values will be displayed in the drop-down list in the field on the right: HOST, USER-AGENT, COOKIE, X-FORWARDED-FOR, AUTHORIZATION, REFERER, CONTENT-TYPE.
- **path** — the number of the endpoint’s part from 0 on up (index of the element in the array). Note that the last part of the endpoint isn’t included in this field. If there is only one part in the endpoint, leave the field empty. For example, path conditions for the endpoint */backend/statistics/update* would look as follows:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910977627281.png" alt="parameters" width="50%">

- **action_name** — the last part of the endpoint before the point. For example, for the endpoint _backend/index.php, index_ will be an action_name.
- **action_ext** — the last part of the endpoint after the point, which means the extension of the requested file. For example, for the endpoint _backend/index.php, php_ will be an action_ext.
- **query** — the query string parameters.
- **scheme** — http or https.

Select the condition type. There are four available types:

| Type | Meaning                    | Explanation                                                                                                          |
|------|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| =    | Equal                      | The parameter’s value must match precisely with the comparison argument. example = example                           |
| Aa   | IEqual (Equal in any case) | The parameter’s value must match the comparison argument in any case. Example Aa example                             |
| .*   | Regular expression         | The parameter’s value must match the regular expression. Use the <a href="https://github.com/yandex/pire" target="_blank">PIRE library</a>                                        |
| ∅    | Absent                     | The request should not contain the specified parameter. In this case, the comparison argument is not used. example ∅ |

Enter the values that should (or should not) take the parameters specified in the third step.

### Add a rule for processing requests (Then section)

When the conditions are completed, add actions in the *Then* section. These actions will be applied to the requests if they match the conditions.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/9910984485009.png" alt="Add a rule for processing requests" width="80%">

Select the appropriate action from the drop-down list and configure the relevant settings. There are five available actions:

1\.  **Allow binary data.** It is used to adjust the standard attack detection rules for binary data. By default, WAF mistakenly identifies some standard binary characters as attack attributes. You can specify in which part of the query binary characters are allowed. Then WAF won’t check them in the specified part.

2\.  **Ignore certain attack types.** This is used to disable the detection of specific attack types in parts of your application requests. By default, WAF reacts to signs of all attack types regardless of the part of the request. But sometimes, false-positive processing occurs for legitimate requests. For example, when the user posts the description of the malicious SQL command. This part is in the body of the requests. By "Ignore certain attack types", you can set which parts of the requests shouldn’t be analyzed for attack detection.

3\.  **Disable/Enable parsers.** It is used to manage the set of parsers WAF uses for the request analysis. By default, WAF attempts to sequentially apply each suitable parser to each request’s element. But in some cases, it uses inappropriate parsers and detects attack signs in the decoded value so that you can disable the parsers applied to certain request elements.

4\.  **Create regexp-based attack indicator.** It is used for manual attack detection based on regular expressions (regexp). By default, WAF doesn’t use regular expressions but allows adding custom indicators of attacks.

5\.  **Set filtration mode.** It allows you to enable or disable request blocking for different application endpoints. There are four options:

*   By default. WAF will process requests according to its default settings.
*   Disable. Filtration is completely disabled.
*   Monitoring. Requests are analyzed and displayed in the interface but aren’t blocked, even if they are sent from blacklisted IP addresses or contain signs of attacks.
*   Blocking. Malicious requests are blocked and displayed in the interface.