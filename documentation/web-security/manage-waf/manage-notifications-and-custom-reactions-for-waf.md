---
title: manage-notifications-and-custom-reactions-for-waf
displayName: Manage triggers
published: true
order: 30
toc:
   --1--What are triggers?: "what-are-triggers"
   --1--Create triggers: "create-triggers"
   --2--Step 1. Сondition: "step-1-choose-a-condition"
   --2--Step 2. Filters: "step-2-add-a-filter"
   --2--Step 3. Reactions: "step-3-add-reactions"
   --2--Step 4. Saving : "step-4-save-the-trigger"
   --1--Disable and delete: "disable-or-delete-a-trigger"
pageTitle: Managing WAF Triggers | Gcore
pageDescription: A guide on managing WAF triggers to tailor your security alerts and responses with condition, filter, and reaction options.
---
# Manage notifications and custom reactions for WAF
  
## What are triggers?

Triggers are tools that allow you to receive notifications and set how WAF should react to some events that it doesn't respond to by default (e.g., behavior attacks).

With triggers, you can:

- Get notified about significant events through your daily workflow tools, like corporate messengers or incident management systems
- Block IP addresses that have sent a certain number of requests or attack vectors
- Detect behavioral attacks based on the number of requests made to specific API endpoints
- Streamline the event list by grouping hits from the same IP address into a single attack
- Monitor a rise in malicious requests detected by WAF nodes, which could suggest an ongoing attack. This allows for timely actions, such as manually blocking the attacker's IP addresses, to mitigate the threat

Each trigger consists of three components:

1.  **Condition** is an event for which the WAF reaction is configured.
2.  **Filters** are additional criteria that detail the conditions.
3.  **Reaction** is the action the WAF will perform if the event meets the added condition and filter.

Let's say, for example, that you want to receive alerts about XSS attacks (if there are more than 2,000 per hour) via e-mail. In this case, you should create a trigger with the following components:

*   Condition. The number of attacks and the value of 2,000 per hour for it.
*   Filter. XSS attack type.
*   Reaction. A message and the e-mail address for integration.

Triggers are managed and collected in the <a href="https://web-protect.gcore.com/waf/triggers/list" target="_blank">Triggers</a> tab.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/manage-notifications-and-custom-reactions-for-waf/triggers-waf-10.png" alt="Triggers" width="80%">

## Create triggers

1. Click **Create trigger**.
2. Choose conditions.
3. Add filters.
4. Add reactions.
5. Save the trigger.

### Step 1. Choose a condition

A condition refers to a system event that you would like to be alerted about. The following conditions are available for notification:

- **Brute force**. Brute force attacks include brute-forcing passwords, session IDs, and account data spoofing. Signs of brute forcing include sending many requests to the same endpoint during the defined time interval.
- **Forced browsing**. Forced browsing is a behavioral attack in which an attacker tries to find directories and files with information about an application's configuration and components. Signs of forced browsing include sending many requests to different endpoints, to which the application responds with a 404 code.
- **BOLA**. BOLA (Broken Object Level Authorization) is a behavioral attack in which an attacker can retrieve or modify an application component by identity through an API, thus bypassing authorization. This attack exploits a vulnerability related to the lack of or insufficient verification of access rights.
- **Weak JWT**. 
- **Number of attack vectors (malicious payloads)**. A malicious payload is the part of a request which contains instructions about what actions should be performed in an attacked application. With a trigger, you can specify how many requests with payloads WAF should react to.
- **Number of attacks, hits, incidents.** With conditions 5–7, you'll set the number of attacks, hits, or incidents about which the WAF should send you an e-mail notification.
- **Denylisted IP**. This will allow you to specify blocked IPs to WAF.
- **Changes in API inventory**.
- **Hits from the same IP.** Using a condition, you can specify the threshold from which hits sent from the same IP should be grouped into a single attack in the <a href="https://web-protect.gcore.com/waf/events/incidents" target="_blank">Events</a> section.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/manage-notifications-and-custom-reactions-for-waf/triggers-waf-20.png" alt="Conditions WAF" width="80%">

Choose a condition and set the lower threshold for the reaction, if the setting is available.

### Step 2. Add a filter 

Filters are used for condition detailing. For example, you can set up reactions to attacks of certain types, such as brute-force attacks, SQL injections, and others.

The following filters are available:

- **URI (only for Brute force, Forced browsing, and BOLA)** is the endpoint to which the requests were sent.
- **Type** is the type of attack in the request or the application vulnerability that an attempt to exploit was made on.
- **Application** is the application that received the request or in which the request was found.
- **IP** is the IP address from which the request was sent.
- **Domain** is the domain of the application to which the request was sent or where the incident was found.
- **Response status** is the code with which the application responded to the request.
- **Target** is part of the application ('Database', 'Server', or 'Client') that was attacked or in which part of the application the vulnerability was found.

Choose one or more filters and set values for them.


<img src="https://assets.gcore.pro/docs/web-security/manage-waf/manage-notifications-and-custom-reactions-for-waf/triggers-waf-30.png" alt="Type filter WAF" width="80%">

### Step 3. Add reactions

The reaction determines what WAF should do if a request fits the condition and filters (if they were set). The set of available reactions also depends on the selected condition.

We list all available reactions below.

- Mark the requests as brute-force or forced browsing attack. Requests will be marked as attacks in the events list but will not be blocked. To block requests, you can add an additional reaction: denylist IP address.
- Mark the requests as BOLA attack. Requests will be marked as attacks in the events list but will not be blocked. To block requests, you can add an additional reaction: denylist IP address.
- Record the JWT vulnerability.
- Add IP to the denylist.
- Add IP to the graylist.
- Send a notification to the SIEM system or Webhook URL configured in the (should be preconfigured by technical support).
- Send a notification to the messenger (should be preconfigured by technical support).

Select one or more reactions. The reactions applicable to the condition are found under the **Number of attacks** section:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/manage-notifications-and-custom-reactions-for-waf/triggers-waf-40.png" alt="Add a reaction WAF" width="80%">

### Step 4. Save the trigger

1\. Click **Create** in the trigger creation modal dialog.

2\. Specify the trigger's name and description (if required) and click **Done**.

## Disable or delete a trigger

Go to the <a href="https://web-protect.gcore.com/waf/triggers/list" target="_blank">Triggers</a> tab, click the three dots next to the trigger you want to disable or delete, select the needed option, and confirm the action.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/manage-notifications-and-custom-reactions-for-waf/10592589376529.png" alt="Disable or delete a trigger" width="80%">

- If you disable a trigger, reactions for the trigger will be stopped until the trigger is enabled again. The disabled triggers are displayed in the list. To re-enable, use the Enable option.
- If you delete a trigger, it'll be permanently stopped and removed from the general list forever.