---
title: set-the-access-policy-for-a-protected-resource
displayName: Set the Access Policy
published: true
order: 60
toc:
   --1--Country Access Policy: "country-access-policy"
   --1--IP Access Policy: "ip-access-policy"
pageTitle: Access Policy For a Resource Under Protection | Gcore 
pageDescription: A guide on how to set the access policy for a protected resource in the control panel.
---
# Set the access policy for a protected resource

Go to the Web Protection tab > Settings > the Access policy tab to restrict or allow access to your resource.

<img src="https://assets.gcore.pro/docs/web-security/set-the-access-policy-for-a-protected-resource/access_policy_2.png" alt="Access policy tab" width="80%">

## Country access policy

- *None* — set by default, no restrictions.
- *Allow by default* — access is provided for all but specified countries.
- *Block by default* — access is denied for all but specified countries.

## IP access policy 

Add to the *White List* all IP addresses or subnets which should have access to your site: one IP address or subnet (with subnet masks from /24 to /30) per line (use the plus button to add more lines).

Add to the *Black List* all IP addresses or subnets which should have no access to your site: one IP address or subnet (with subnet masks from /24 to /30) per line (use the plus button to add more lines).