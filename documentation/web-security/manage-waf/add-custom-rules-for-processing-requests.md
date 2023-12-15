---
title: add-custom-rules-for-processing-requests
displayName: Create rules
published: true
order: 20
toc:
   --1--About Rules: "about-rules"
   --1--Terminology: "terminology"
   --1--Overview: "the-rules-tab-overview"
   --2--Rules: "rules"
   --2--Default rules: "default-rules"
   --1--Create: "create-rules"
   --2--If request is: "if-request-is-section"
   --2--URI constructor: "uri-constructor"
   --2--Using wildcards: "using-wildcards"
   --2--Some details: "some-details"
   --2--Advanced edit: "advanced-edit-form-points"
   --2--Condition types: "condition-types"
   --2--Then: "then-section"
pageTitle: Customize WAF Security Rules | Gcore
pageDescription: Learn how to add and configure custom WAF rules to secure your applications better, helping to prevent malicious requests and increase overall security.
---
# Add custom rules for processing requests
  
## About Rules

On the “Rules” tab, you can review and modify the rules for managing requests activated for the present application profile.

An application profile consists of compiled data about safeguarded applications. This data is utilized to adjust the system's performance during the examination of requests and their subsequent processing in both the post-analysis module and the cloud.

To better comprehend how the rules for processing traffic are implemented, we recommend you familiarize yourself with how the filter node analyzes requests.

**Note**: Changes made to the rules take time to become effective. Creating and implementing these rules into the filter nodes may require some time (up to 2 minutes).

## Terminology

**Point**. A point is an HTTP request parameter. This parameter can be characterized by a series of filters used during the processing of the request, such as headers, body, URL, Base64, and so on. This sequence is also called the point.

**Parsers**. Parsers are request processing filters.

**Rule branch**. A rule branch is defined as the collection of HTTP request parameters and their respective conditions. If these conditions are met, the rules associated with that particular branch will be enforced. For instance, the rule branch ```example.com/**/```. outlines the conditions that correspond to all requests directed to any URL within the domain of ```example.com```.

**Endpoint (Endpoint branch)**. An endpoint branch refers to a branch that doesn't contain any nested rule branches. Ideally, an application endpoint corresponds to a single business function of the protected application. For example, a business function such as authorization could be an endpoint rule branch of ```example.com/login.php```.

**Rule**. A rule refers to the configuration set for processing requests in the filter node, post-analysis module, or the cloud. These processing rules are associated with branches or endpoints. A rule is only implemented on a request if that request fulfills all the conditions outlined in the branch.

## The Rules tab overview

To examine the rules within the application structure, navigate to the **Rules** section in the Gcore Customer Portal. This section shows the branches and endpoints that are already identified.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-10.png" alt="Inspecting Application Profile Rules" width="80%">

Two asterisks ```**``` in a branch description refer to any number of nested paths. For instance, the branch ```/**/*.php``` will contain both ```/index.php``` and ```/app/admin/install.php```.

### Rules 

Within each branch, users can browse through the list of *rules* associated with it. To open the page containing the list of rules, click on the description of the relevant branch.

The rules in a branch are organized according to the *point* field. Rules that impact the whole request, rather than specific parameters, are consolidated into a single line. To view the complete list, click on the line.

The system presents the following parameters for each rule: the last time it was modified, the quantity, the types, and the point.

### Default rules

Default rules, which aren't linked to any specific endpoint, can be created with a specified action. These rules are applied across all endpoints.

To create a default rule, proceed as usual but leave the URI field empty. This will result in a new rule that isn't associated with any endpoint. 

To view the list of default rules you've created, click the "Default rules" button.

**Note**: All branches inherit these default rules.

## Create rules

### If request is section

To create a new rule, go to the **Rules** tab.

Rules can be added to both existing branches as well as new ones. You have the option to either create them from scratch or base them on an existing branch.

To attach a rule to an existing branch, click **Add rule** (this will appear in the pop-up menu on the right when you hover your mouse cursor over the branch description line). This action can also be carried out on the rule page of the respective branch.

If needed, you can alter the branch where the rule will be added. To do this, click the *If request is* clause in the rule-adding form and modify the branch description conditions. If a new branch is formed, it will be displayed on the screen and the view of the application structure will be updated.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-20.jpg" alt="Rules creation interface" width="80%">

### URI constructor

The URI constructor enables you to set up the conditions for a rule by defining the request method and endpoint in a single string:

- For the request method, the URI constructor offers a specific selector. If no method is chosen, the rule will be applicable to requests using any method
- For the request endpoint method, the URI constructor provides the particular field accepting the following value formats:

<media-gallery>

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-30.jpg" alt="URI constructor fields part 1" width="80%">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-40.jpg" alt="URI constructor fields part 2" width="80%">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-50.jpg" alt="URI constructor fields part 3" width="80%">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-60.jpg" alt="URI constructor fields part 4" width="80%">

</media-gallery>

The string specified in the URI constructor is automatically parsed into the set of conditions for the following request points:

- ```method```
- ```header``` (The URI constructor allows specifying only the HOST header)
- ```path```, ```action_name```, ```action_ext```. Before confirming the rule creation, please ensure the values of these request points are parsed in one of the following ways:
   - Explicit value of certain ```path``` number + ```action_name``` + ```action_ext``` (optional)
   - Explicit value of ```action_name``` + ```action_ext``` (optional)
   - Explicit value of certain path number without ```action_name``` and without ```action_ext```
- ```query```

The value specified in the URI constructor can be completed by other request points available only in the advanced edit form.

### Using wildcards

Traditionally it's impossible to use wildcards while operating with the URI constructor. But you can accomplish the same outcome by following these steps:

- Instead of wildcards, employ regular expressions within the parsed components of your URI.
- Insert the ```*``` or ```**``` symbol into the URI field to substitute one or multiple components (refer to the examples provided in the previous section).

### Some details

The syntax of regular expressions differs from traditional wildcards, but you can still achieve the same outcomes. For instance, if you want to create a mask that corresponds to:

- ```something-1.example.com/user/create.com``` and
- ```anything.something-2.example.com/user/create.com```

In the context of traditional wildcards, you might attempt to do this by inputting: ```*.example.com/user/create.com```.

However, in WAF, your ```something-1.example.com/user/create.com``` will be parsed as follows:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/add-custom-rules-for-processing-requests/rules-waf-70.png" alt="Wildcard rules creation" width="80%">

```something-1.example.com``` is a header-HOST point. We mentioned that wildcard cannot be used within the point, so instead we need to use regular expression. Set the condition type to REGEX and then use the regular expression WAF specific syntax:

1. Do not use ```*``` in a meaning "any number of symbols"
2. Put all the ```.``` that we want to be interpreted as "actual dots" in square brackets: ```something-1[.]example[.]com```
3. Use ```.``` without brackets as replacement of "any symbol" and ```*``` after it as quantifier "0 or more repetitions of the preceding", so ```.*``` and: ```.*[.]example[.]com```
4. Add ```$``` in the end of the expression to say that what we created must end our component: ```.*[.]example[.]com$```

### Advanced edit form points

The point field indicates which parameter value should be extracted from the request for comparison. At present, not all of the points that the filter node can analyze, are supported.

The following points are currently supported:

- **application**—application ID.
- **proto**—HTTP protocol version (1.0, 1.1, 2.0, etc.).
- **scheme**—http or https.
- **uri**—part of the request URL without the domain (for example, ```/blogs/123/index.php?q=aaa``` for the request sent to ```http://example.com/blogs/123/index.php?q=aaa```).
- **path**, **action_name**, **action_ext**—hierarchical URI component sequence where:
   - **path**—an array with URI parts separated by the / symbol (the last URI part is not included in the array). If only one part in the URI exists, the array will be empty.
   - **action_name**—the last part of the URI after the / symbol and before the first period ```(.)```. This part of the URI is always presented in the request, even if its value is an empty string.
   - **action_ext**—the part of the URI after the last period ```(.)```. It may need to be added to the request.
- **query**—query string parameters.
- **header**—request headers. When you enter a header name, the most common values are displayed in a drop-down list. For
example: ```HOST, USER-AGENT, COOKIE, X-FORWARDED- FOR, AUTHORIZATION, REFERER, CONTENT-TYPE```.
- **method**—request methods. The rule will be applied to requests with any method if the value is not explicitly specified.

### Condition types

- ```EQUAL (=)```. The point value must match precisely with the comparison argument. For example, only *example* matches with the point value *example*.

<expandable-element title="EQUAL condition type for the HOST header value">

We have restricted the EQUAL condition type for the HOST header to cover more requests with the rules. Instead of the EQUAL type, we recommend using the type IEQUAL which allows parameter values in any register.

If you have previously used the EQUAL type, it will be automatically replaced with the IEQUAL type.

</expandable-element>

- ```IEQUAL (Aa)```. The point value must match the comparison argument in any case. For example: *example, ExAmple, exampLe* match with the point value *example*.

- ```REGEX (.*)```. The point value must match the regular expression.
- ```ABSENT ( )```. The request should not contain the designated point. In this case, the comparison argument is not used.

### Then section

The added request processing rule is described in the **Then** section. The following rules are supported:

- Disable/Enable parsers
- Set the filtration mode
- Mask sensitive data
- Set the mode of active threat verification
- Apply a virtual patch
- User-defined detection rules
- Ignore certain attack types
- Ignoring certain attack signs in the binary data