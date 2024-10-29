---
title: tag-rules
displayName: Tag rules
published: true
order: 30
toc:
   --1--Types of tag rules: "types-of-tag-rules"
   --1--Tag based rules: "tag-based-rules"
   --1--Tag generating rules: "tag-generating-rules"
pageTitle: Learn about Gcore tag rules | Gcore
pageDescription: Learn about Gcore tag rules and how to use them for filtering incoming traffic and blocking malicious requests.
---
# Tag rules

As part of the <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">WAAP custom rules</a>, you can create rules based on specific tags to filter incoming traffic. A **tag** contains information about a user and is attached to their request. Tag rules are just one component of our robust rule engine.  

## Types of tag rules 

You can use two types of tag rules: 

* Tag-based rules. Create rules using our <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules/predefined-tags" target="_blank">predefined set of tags</a>. 

* Tag-generating rules. You can create rules that will generate tags based on specific conditions. For example, if the request contains a certain header, tag such request with <code>tagname</code>.
These generated tags are also known as <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">user-defined tags</a> and they can be used to modify custom rules and create more complex ones. 

<alert-element type="info" title="Info">
 
We recommend <a href="https://gcore.com/docs/waap/analytics#request-details" target="_blank">inspecting the details</a> of your WAAP requests before creating tag-based rules. These details contain information about user activity, which can clarify which tags should be used for filtering traffic. 
 
</alert-element>

## Tag-based rules 

We offer a <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules/predefined-tags" target="_blank">predefined set of tags</a> that you can use to create tag-based rules. These tags should be added to “if/then” statements of your rule and let you block or allow certain requests to a domain. 

For example, check the following tag-based rule that blocks traffic if the tag associated with the request contains Hosting Services. You might want to prevent such traffic from reaching your domain because these IPs are more likely to belong to automated users rather than humans. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/tag-rules/add-tag-based-rule.png" alt="Example of a tag-based rule">

## Tag generating rules 

You can also create rules that will generate any tags of your choice based on the conditions you define. These generated tags are known as **user-defined** tags.  

Once you create a user-defined tag, it’s automatically added to the list of pre-defined tags and becomes available for use in a tag-based rule. 

The following examples demonstrate how you can apply user-defined tags. 

Let's say you run an online shop that requires users to log in before checking out an order. You can create a rule that will generate a custom tag called `validuser` if the request header named `set-cookie` contains a cookie named `mycookie`, which indicates that the user is logged in. 

<img src="https://assets.gcore.pro/docs/waap/waap-rules/tag-rules/user-defined-tag.png" alt="Example of a tag-based rule">

In this case, `validuser` will be your new user-defined tag that's now available for use in a tag-based rule.

<img src="https://assets.gcore.pro/docs/waap/waap-rules/tag-rules/user-defined-tag-use-created-tag.png" alt="Example of a tag-based rule">

<alert-element type="info" title="Info">
 
Consider that rules with user-defined tags run before the rules, which use our pre-defined sets of tags. 
 
</alert-element>

For more examples of tag generating rules, check out the following guides: <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules/reserved-tags" target="_blank">Reserved tags</a> (user-defined) and <a href="https://gcore.com/docs/waap/api-discovery-and-protection/configure-api-access-with-reserved-tags" target="_blank">Configure API access with reserved tags</a>. 