---
title: available-rule-types
displayName: Rule types
published: true
order: 25
toc:
   --1--Manage request parsers: "manage-request-parsers"
   --1--Create and apply rules: "create-and-apply-rules"
   --1--Example: "rule-example"
   --1--Rules for data masking: "rules-for-data-masking"
   --2--Masking of the cookie value: "masking-of-a-cookie-value"
   --1--User-defined detection rules: "user-defined-detection-rules"
   --2--Add a new detection rule: "add-a-new-detection-rule"
   --2--Blocking all requests with an incorrect User-agent header: "blocking-all-requests-with-an-incorrect-user-agent-header"
   --1--Ignore certain attack types: "ignore-certain-attack-types"
   --1--Ignoring attack signs in the binary data: "ignoring-attack-signs-in-the-binary-data"
pageTitle: Discover Effective Ways to Manage Web Application Security with WAF Rules | Gcore
pageDescription: Explore how to enhance web application security using various rules and configurations in the WAF system.
---
# Available rule types

## Manage request parsers

The rule **Disable/Enable request parser** allows managing the set of parsers applied to the request during its analysis.

By default, when analyzing the request, the WAF node attempts to sequentially apply each suitable parser to each request element. However, certain parsers can be applied mistakenly so that the WAF node may detect attack signs in the decoded value.

For instance, the WAF node might incorrectly interpret unencoded data as being encoded into Base64, given that Base64 alphabet symbols are frequently found in regular text, token values, UUID values, and other data formats. If the WAF node decodes the unencoded data and identifies signs of attack in the resulting value, a false positive is registered.

To avoid such false positives, the **Disable/Enable request parser** rule can be used to turn off parsers that are incorrectly used on certain request elements.

## Create and apply rules

The rule can be both created and applied within the **Attacks** and **Rules** WAF sections.

- In the **Attacks** section, rules are generated with a pre-existing description of the endpoints where the rule will be applied. This description aligns with the request for which you've clicked the **Rule** button. To finalize the rule setup, choose the rule's type action and ensure all elements of the rule are set up correctly
- In the **Rules** section, you'll need to manually input all components of the rule

To create and apply the rule in the **Rules** section:

1\. Create the rule **Disable/Enable request parser** in the **Rules** WAF section. The rule consists of the following components:

- The condition describes the endpoints where the rule will be applied. - Parsers that should be enabled or disabled for the specific request element.
- The part of request refers to the original request element that should be parsed or left unparsed with the selected parsers. If multiple options are chosen sequentially **in this part of request**, they should represent the order of parsers that the WAF would use to read the necessary request element.

2\. Wait for the rule creation to complete.

## Rule example

Suppose the requests to ```https://example.com/users/``` necessitate the authentication header ```X-AUTHTOKEN```. The header value might include specific combinations of symbols (like ```'='``` at the end) that WAF could potentially decode using the base64 parser.

You can configure the **Disable/Enable request parser** rule to prevent false positives in the USER-AGENT values as follows:

<media-gallery>

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-10.png" alt="Example of the created rule (if section)" width="">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-20.png" alt="Example of the created rule (then section)" width="">

</media-gallery>


## Rules for data masking

The WAF node transmits the following information to the WAF Cloud:

- Serialized requests with detected attacks
- WAF system counters
- System statistics such as CPU load and RAM usage
- WAF system statistics, including the number of processed NGINX requests and Tarantool statistics
- Data about the type of traffic that WAF requires to accurately identify the application structure

Certain information should not be sent outside of the server where it is processed. This generally includes authorization details (like cookies, tokens, passwords), personal data, and payment information.

The WAF Node can mask data in requests. Using this rule, the original value of the specified request point is removed before the request is sent to the postanalytics module and the WAF Cloud. This approach ensures that sensitive data does not unintentionally leave the secure environment.

This rule can impact the visibility of attacks, the verification of active threats, and the identification of brute force attacks.

### Masking of a cookie value

Here's an illustration of such rule creation. Use the <a href="https://gcore.com/docs/web-security/manage-waf/available-rule-types#create-and-apply-rules" target="_blank">instructions above</a>. The rule applies if the following conditions are specified in the **If** section:

- the application is accessible at the domain ```example.com```
- the application uses a ```PHPSESSID``` cookie for user authentication
- security policies deny access to this information for employees using WAF

To create a data masking rule for this cookie, the following actions should be performed in the **Then** section:

1\. Go to the **Rules** tab

2\. Find the branch for ```example.com/**/*.*``` and click **Add rule**

3\. Choose **Mask sensitive data**

4\. Select the *Header* parameter and enter its value ```COOKIE```; select
the ```cookie``` parameter and enter its value ```PHPSESSID``` after **in this part of request**. Options sequentally (if several) selected in in this part of request should reflect a sequence of parsers WAF would apply to read the required request element

5\. Click **Create**

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-30.png" alt="Masking of the cookie value (example)" width="80%">

## User-defined detection rules

In certain situations, it might be beneficial to manually add a signature for attack detection or to create a virtual patch. While WAF doesn't employ regular expressions for attack detection, it does permit users to supplement with additional signatures that are based on regular expressions.

### Add a new detection rule

**Click the Create regexp-based attack indicator** rule and fill in the fields:

- **Regular expression**—this is the signature used. If the value of the subsequent parameter aligns with the expression, the request is identified as an attack. The syntax and specifics of regular expressions are detailed in the <a href="https://gcore.com/docs/web-security/manage-waf/add-custom-rules-for-processing-requests#uri-constructor" target="_blank">instructions for adding rules</a>

- **Changing the regular expression specified in the rule**—if you alter the regular expression in an existing **Create regexp-based attack indicator** rule, any **Disable regexp-based attack detection** rules using the previous expression will be automatically deleted

**Note**: To disable attack detection by a new regular expression, you need to create a new **Disable regexp-based attack detection** rule specifying the new regular expression

- **Experimental**—this feature allows you to securely test the trigger of a regular expression without blocking requests. Even when the filter node is in blocking mode, requests won't be blocked. These requests will be viewed as attacks detected via the experimental method and will be hidden from the event list by default. They can be found using the search query ```experimental attacks```

- **Attack**—this refers to the type of attack that will be detected when the parameter value in the request matches the regular expression

- **in this part of request**—this determines the point in the request where the system should detect corresponding attacks. If multiple options are selected sequentially **in this part of the request**, they should represent the order of parsers that WAF would use to read the necessary request element

### Blocking all requests with an incorrect User-agent header

Here's an illustration of such a rule. The rule applies if the following conditions are specified in the **If** section:

- the application is accessible at the domain ```example.com```
- the application uses the ```USER-AGENT``` header

To create a rule for rejecting incorrect format tokens, specify the following in the **Then** section:

1\. Go to the **Rules** tab

2\. Find the branch for ```example.com/**/*.*``` and click **Add rule**

3\. Select **Define as an attack on the basis of a regular expression**

4\. Set **Regex** value as ```^Malicious-Actor$```

5\. Choose **Virtual patch** as the attack type

6\. Set the USER-AGENT header 

7\. Click **Create**

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-40.png" alt="Blocking all requests with an incorrect User-agent header" width="80%">

## Ignore certain attack types

The rule **Ignore certain attack types** allows you to disable the detection of specific types of attacks in certain request elements.

By default, if the WAF node detects signs of any type of attack in any element of a request, it labels the request as an attack. However, some requests that contain signs of attacks might actually be legitimate. For instance, a request publishing a post on the Database Administrator Forum might contain a description of a malicious SQL command, but it's not an attack.

If the WAF node mistakenly identifies a standard request payload as malicious, a false positive is registered. To avoid such false positives, standard attack detection rules may need to be customized using rules of specific types to suit the peculiarities of the protected application. The **Ignore certain attack types** rule is an example of such a custom rule.

Here's an illustration of such rule creation. Use the <a href="https://gcore.com/docs/web-security/manage-waf/available-rule-types#create-and-apply-rules" target="_blank">instructions above</a>. 

Let's consider an example where a user confirms the publication of a post on the Database Administrator Forum. The client sends a POST request to the endpoint ```https://example.com/posts/```. This request has specific properties:

- The content of the post is transmitted in the request body parameter ```postBody```. This content may incorporate SQL commands that WAF could potentially flag as malicious.
- The request body is of the ```application/json``` type.

Here's an example of a cURL request containing an SQL injection:

```
curl -H "Content-Type: application/json" -X POST https://example.com/posts -d '{"emailAddress":"johnsmith@example.com", "postHeader":"SQL injections", "postBody":"My post describes the following SQL injection: ?id=1%20select%20version();"}'
```

To disregard SQL injections in the ```postBody``` parameter of the requests to ```https://example.com/posts/```, the **Ignore certain attack types** rule can be configured in the following way:

<media-gallery>

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-50.png" alt="Ignore certain attack types (if section)" width="">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-60.png" alt="Ignore certain attack types (then section)" width="">

</media-gallery>

## Ignoring attack signs in the binary data

The rules **Allow binary data** and **Allow certain file types** are used to adjust the standard attack detection rules for binary data.

By default, the WAF node analyzes incoming requests for all known attack signs. During the analysis, the WAF node may not consider the attack signs to be regular binary symbols and mistakenly detect malicious payloads in the binary data.

- The rule **Allow binary data** allows fine-tuning attack detection for request elements containing binary data (e.g. archived or encrypted files).
- The rule **Allow certain file types** allows fine-tuning attack detection for request elements containing specific file types (e.g. PDF, JPG).

To adjust the attack detection rules for the binary data passed in the specified request elements, create the rule **Allow binary data** in the **Rules** WAF section. 

The rule consists of the following components:

- Condition describes the endpoints to apply the rule to.
- Part of request points to the original request element containing the binary data.
- Options sequentally (if several) selected **in this part of request** should reflect a sequence of parsers WAF would apply to read the required request element.

To adjust the attack detection rules for certain file types passed in the specified request element, create the rule **Allow certain file types** in the **Rules** WAF section. The rule consists of the following components:

- Condition describes the endpoints to apply the rule to.
- File types to ignore the attack signs in.
- Part of request points to the original request element containing the specified file types.
- Options sequentally (if several) selected **in this part of request** should reflect a sequence of parsers WAF would apply to read the required request element.

Let's consider an example where a user uploads a binary file containing an image using a form on a website. The client sends a POST request of the type ```multipart/form-data``` to ```https://example.com/uploads/```. The binary file is included in the body parameter ```fileContents```.

The **Allow binary data** rule, which fine-tunes attack detection in the ```fileContents``` parameter, is configured as follows:

<media-gallery>

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-70.png" alt="Ignoring attack signs in the binary data rule example (if section)" width="">
<img src="https://assets.gcore.pro/docs/web-security/manage-waf/available-rule-types/rules-waf-80.png" alt="Ignoring attack signs in the binary data rule example (then section)" width="">

</media-gallery>