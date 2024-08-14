---
title: roubleshoot-5xx-errors
displayName: Troubleshoot 5xx errors
published: true
order: 
pageTitle: A guide on how to fix 5xx errors | Gcore
pageDescription: Discover common causes of 5xx errors and how to fix them.
---
# Troubleshoot 5xx errors

500-class response codes indicate that a server error occurred while WAAP was processing a request.  

You may encounter several types of 500s errors that are commonly caused by incorrect settings, origin server firewalls, origin server issues, or connection timeouts. This guide will help you understand potential error causes and how you might address them. 

## 543 errors 

**Error 543** typically means that all your origin servers are down or there is a network issue preventing access to the origin.  

When this happens, you’ll see the following message:

<img src="https://assets.gcore.pro/docs/waap/troubleshooting/543-error.png" alt="543 error message in the Customer Portal" width="70%">