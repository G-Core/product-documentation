---
title: reserved-tags
displayName: Reserved tags
published: true
order: 10
pageTitle: A guide to Gcore WAAP reserved tags | Gcore
pageDescription: Check the list of Gcore reserved tags and learn how use them in custom rules.
---
# Reserved tags

Reserved tags are predefined tags that trigger specific actions in custom rules. They play a key role in <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">tag-generating rules</a>—each rule contains a reserved tag in its <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#rule-conditions" target="_blank">condition</a>.  

## Available reserved tags 

Reserved tags can be divided into two categories: general tags that are used in custom rules with various conditions and API protection tags that are specifically designed to protect your APIs. API protection tags are used with the URL <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#rule-conditions" target="_blank">rule condition</a>.  

General tags: 

* Registered 
* Logged In 
* Paid
* Monitor 
* Ignored Automation 
* Login Page 
* Legitimate Activity 
* Malicious Activity 
* Item Added to Cart 
* Cart Checkout 

API protection tags: 

* API Privileged Access  
* API Admin Access 
* Indicate API Privileged User 
* Indicate API Admin User 
* Ignore Email Address Detection 
* Ignore Phone Number Detection 
* Auth Endpoint  
* Ignore CCN Detection  
* Ignore SSN Detection  

Unlike <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">user-defined tags</a> that are automatically generated based on specific request conditions, reserved tags aren’t customizable. However, you can use them to create a variety of rules, each adjusted to a specific scenario as documented in the following sections.

## Tag requests from logWeged-in, registered, or paid users

The **Registered**, **Logged In**, and **Paid** tags allow you to identify requests from users who have created accounts on your domain, are authenticated, or have paid subscriptions.  

When creating a rule, make sure that you specify a secure condition. For example, explicitly define the IP address from which the requests will be coming (e.g., IP=1.2.3.4). Don't use the conditions that are easy to spoof, such as the User Agent header. 

You can also use a server signal that will serve as a unique identifier and can be used to verify the client. For instance, apply a tag based on a session cookie or a specific HTTP response header.  

For example, you can create the rule that looks for the X-Registered header, which designates registered users: 