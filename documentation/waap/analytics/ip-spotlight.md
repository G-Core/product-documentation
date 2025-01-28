---
title: ip-spotlight
displayName: IP Spotlight
published: true
order: 20
toc:
   --1-- Analyze an IP: "analyze-an-ip"
   --1-- Inspect global and domain activity: "inspect-global-and-domain-activity"
   --2-- Global activity: "global-activity"
   --3-- IP threat summary: "ip-threat-summary"
   --3-- IP risk assessment: "ip-risk-assessment"
   --3-- WhoIs: "whois"
   --3-- Top 10 attack targets: "top-10-attack-targets"
   --3-- Attack distribution over time: "attack-distribution-over-time"
   --2-- Domain activity: "domain-activity"
   --3-- Overview: "overview"
   --3-- Top 10 triggered policies: "top-10-triggered-policies"
   --3-- Top 10 visited URLs: "top-10-visited-urls"
   --3-- Top 10 sessions: "top-10-sessions"
   --3-- Top 10 user agents: "top-10-user-agents"
pageTitle: Use system-generated analytics to get detailed information about a specific IP address | Gcore
pageDescription: Learn how to use Gcore WAAP’s IP Spotlight feature for your domain protection.
---
# IP Spotlight

IP Spotlight is a threat analytics tool that provides detailed information about a specific IP address.

It operates on the IP-related information we collect from our network to give you insights about the clients that access your domains. This information helps you make better decisions when creating WAF rules and helps with policy configuration to prevent and mitigate attacks.

<alert-element type="info" title="Info">
The IP Spotlight feature is available on the [Enterprise plan](https://gcorelu.sharepoint.com/:w:/r/sites/technical_writers/_layouts/15/Doc.aspx?sourcedoc=%7BB1815DC7-5466-4D18-A09B-36D928B69808%7D). To enable it for your domain, contact our support team.
</alert-element>

## Analyze an IP

IP Spotlight provides IP details as its source, total number of requests, destinations, whois data, and whether it has been involved in any malicious activity against other domains within our network.

To check an IP address, follow these steps:

1. In [the Gcore Customer Portal](https://accounts.gcore.com/reports/dashboard), navigate to **WAAP** \> **Features**

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-1.png" alt="IP Spotlight">

2. Click **IP Spotlight**
3. In the address field, enter the IP address that you want to inspect
4. Click the **Analyze IP** button

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-2.png" alt="IP Spotlight">

5. All collected information about the address will appear on the **Global Activity** and **Domain Activity** tabs

## Inspect global and domain activity

We analyze IP addresses past activities in two areas: activity across the whole Gcore network (global activity) and interactions specific to your domains (domain activity).

### Global activity

The **Global activity** tab shows generic IP information and insights gathered from other domains on our platform. This data is more aggregate than the domain activity.

#### IP threat summary

In this section, you can find out if we detected any threats to resources in our network in the past.

The section includes the following details:

- The risk assessment score, which has five levels:
  - **No risk**
  - **Low risk**
  - **Medium risk**
  - **High risk**
  - **Extreme risk**
- Total number of requests
- Number of blocked requests
- Number of unique sessions
- Information if the IP address was used for botnet attacks
- The threats and services the IP is known for. The information will be presented as tags associated with the IP addresses, such as SQL injection, injection attacks, or headless browsers.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-3.png" alt="IP Spotlight">

#### IP risk assessment

We query multiple external and internal databases to retrieve and store information about an IP address. This allows IP Spotlight to provide a risk assessment and score related to the IPs’ threat level. This score, ranging from Low to Extreme, allows you to determine what actions to take against any flagged IP that sends requests to your domain.

The High and Extreme risk scores are typically assigned to addresses that exist on external block lists, participate in DDoS attacks, or make a higher number of requests than usual.

<alert-element type="info" title="Info">
If the IP is no longer associated with malicious activity, its score might decrease from extreme to **Low** or even **No risk** over time.
</alert-element>

#### WhoIs

This section provides information from the [global WHOIS database](https://who.is/). It includes details like the name and type of organization that owns the address, its location, related IP ranges, contact information for reporting abuse, and registry details.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-4.png" alt="IP Spotlight">

#### Top 10 attack targets

This section provides you with a map that shows the targets of past attacks originating from the scanned address. It also includes a list of the top 10 targets of these attacks.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-5.png" alt="IP Spotlight">

#### Attack distribution over time

This section displays a graph with the number of blocked requests that are filtered by the triggered WAF policy.

### Domain activity

<alert-element type="info" title="Info">
To view this information, you need to have WAAP enabled for your domain.
</alert-element>

The data displayed on the **Domain activity** tab contains details about IP activity on your domain. Select a domain you want to analyze from the dropdown menu.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-6.png" alt="IP Spotlight">

#### Overview

In this section, you can find the following information about the address’ activity on your domain:

- Total number of requests
- Number of blocked requests
- Number of unique sessions

#### Top 10 triggered policies

This section provides a list and donut chart of policies applied to the IP and a graph displaying how many times each policy triggered.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-7.png" alt="IP Spotlight">

#### Top 10 visited URLs

This section provides you with top 10 URL paths visited by the IP address, along with the number of times these URLs were requested.

#### Top 10 sessions

This section contains a table displaying information about the top 10 sessions from the specified IP to your domain.

You can check the session ID, the date the session took place, the time-to-live (TTL) of the request, if it was blocked, and the session duration.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-8.png" alt="IP Spotlight">

#### Top 10 user agents

Here, you find a table with information about the top 10 user agents that accessed your domain from the specified IP.

<img src="https://assets.gcore.pro/docs/waap/analytics/ip-spotlight/ip-spotlight-9.png" alt="IP Spotlight">
