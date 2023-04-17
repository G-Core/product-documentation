---
title: manage-notifications-and-custom-reactions-for-waf
displayName: Manage triggers
published: true
order: 30
toc:
   --1--What are triggers?: "what-are-triggers"
   --1--Create a trigger: "create-a-trigger"
   --2--1. Triggers: "1-go-to-triggers"
   --2--2. Сondition: "2-choose-a-condition"
   --2--3. Filters: "3-add-a-filter--optional"
   --2--4. Reactions: "4-add-a-reaction"
   --2--5. Name and description: "5-enter-the-name-and-description"
   --1--Disable and delete: "disable-or-delete-a-trigger"
---
# Manage notifications and custom reactions for WAF
  
## What are triggers?

Triggers are tools that allow you to receive notifications and set how WAF should react to some events that it doesn't respond to by default (e.g., behavior attacks).

Each trigger consists of three components:

1.  **Condition** is an event for which the WAF reaction is configured.
2.  **Filters** are additional criteria that detail the conditions.
3.  **Reaction** is the action the WAF will perform if the event meets the added condition and filter.

Let's say, for example, that you want to receive alerts about XSS attacks (if there are more than 2,000 per hour) via e-mail. In this case, you should create a trigger with the following components:

*   Condition. The number of attacks and the value of 2,000 per hour for it.
*   Filter. XSS attack type.
*   Reaction. A message and the e-mail address for integration.

<img src="https://support.gcore.com/hc/article_attachments/10592570751633" alt="">

This is what a tab looks like with two triggers that add IP addresses that meet the conditions to the denylist:

<img src="https://support.gcore.com/hc/article_attachments/10592555347729" alt="">

## Create a trigger

### 1. Go to Triggers

Go to the <a href="https://web-protect.gcore.com/waf/triggers/list" target="_blank">Triggers</a> tab and click **Create trigger**.

<img src="https://support.gcore.com/hc/article_attachments/11773688591889" alt="">

A new window opens.

### 2. Choose a condition

Click the appropriate condition from the list to the right.

<img src="https://support.gcore.com/hc/article_attachments/10592570864017" alt="">

There are ten conditions available for triggers:

1. **Brute force.** Brute force attacks include brute-forcing passwords, session IDs, and account data spoofing. Signs of brute forcing include sending many requests to the same endpoint during the defined time interval.

2. **Forced browsing.** Forced browsing is a behavioral attack in which an attacker tries to find directories and files with information about an application's configuration and components. Signs of forced browsing include sending many requests to different endpoints, to which the application responds with a 404 code.

3. **BOLA.** BOLA (Broken Object Level Authorization) is a behavioral attack in which an attacker can retrieve or modify an application component by identity through an API, thus bypassing authorization. This attack exploits a vulnerability related to the lack of or insufficient verification of access rights.

4. By default, WAF doesn't protect applications from brute-force attacks, forced browsing, or BOLA, so with condition 1, 2, or 3 triggers, you would point WAF to the attack signs and then configure how the firewall should react to them.

**Number of malicious payloads.** A malicious payload is the part of a request which contains instructions about what actions should be performed in an attacked application. With a trigger, you can specify how many requests with payloads WAF should react to.

5–7. **Number of attacks, hits, incidents.** With conditions 5–7, you'll set the number of attacks, hits, or incidents about which the WAF should send you an e-mail notification.

8. **Denylisted IP.** This will allow you to specify blocked IPs to WAF.

9. **Hits from the same IP.** Using a condition, you can specify the threshold from which hits sent from the same IP should be grouped into a single attack in the <a href="https://web-protect.gcore.com/waf/events/incidents" target="_blank">Events</a> section.

10.  **User added.** Using a condition, you'll command WAF to send an e-mail notification when the user is added to the WAF account.

### 3. Add a filter (optional)

Filters detail the chosen condition. The set of available filters depends on the selected condition. In the example below, there are available filters for the 'Number of attacks' condition to the right.

<img src="https://support.gcore.com/hc/article_attachments/10592570987281" alt="">

Click the needed filters from the list to add them to the condition. After that, the filter will display on the left, and you can specify its values.

For example, we added the 'Type' filter and selected 'xss', 'sqli', and 'rce' types to determine only those types of attack we want to be notified about.

<img src="https://support.gcore.com/hc/article_attachments/10592570995985" alt="">

To add other filters, click the one you need on the right.

We list all available filters below.

- **URI (only for Brute force, Forced browsing, and BOLA)** is the endpoint to which the requests were sent.
- **Type** is the type of attack in the request or the application vulnerability that an attempt to exploit was made on.
- **Application** is the application that received the request or in which the request was found.
- **IP** is the IP address from which the request was sent.
- **Domain** is the domain of the application to which the request was sent or where the incident was found.
- **Response status** is the code with which the application responded to the request.
- **Target** is part of the application ('Database', 'Server', or 'Client') that was attacked or in which part of the application the vulnerability was found.
- **User's role** is the role of the user who was added to the WAF account. Available roles: deploy, analytic, admin, superadmin, auditor, partner_admin, partner_auditor, partner_analytic.

### 4. Add a reaction

The reaction determines what WAF should do if a request fits the condition and filters (if they were set). The set of available reactions also depends on the selected condition.

The example below shows two available reactions for the 'Brute force' (requests from the same IP) condition to the right.

Click **Add a reaction** to add the suitable response and set it up if necessary.

<img src="https://support.gcore.com/hc/article_attachments/10592571105937" alt="">

We list all available reactions below.

- **Mark as brute force/forced browsing/BOLA.** WAF shows all attacks with the type brute force, forced browsing, or BOLA in the <a href="https://web-protect.gcore.com/waf/events/incidents" target="_blank">Events</a> section and doesn't block them.
- **Denylist IP address.** WAF blocks the attack by adding the IP address to a denylist.
- **Send e-mail.** WAF sends a notification with the appropriate type of conditions to the specified e-mail address. To set this reaction, you should add the e-mail for integration in the <a href="https://web-protect.gcore.com/waf/settings/integrations" target="_blank">Settings</a> tab ahead of time.
- **Group next hits into one attack.** Group hits according to filters configured in the <a href="https://web-protect.gcore.com/waf/events/incidents" target="_blank">Events</a> section of the WAF in one attack.

### 5. Enter the name and description

Check the trigger components, then enter a name and description if necessary. If no name or description is specified, the trigger will be created with a default name in the format.

New trigger by ```<username>```, ```<creation_date>```, and an empty description.

Click **Create**.

<img src="https://support.gcore.com/hc/article_attachments/10592571112721" alt="">

## Disable or delete a trigger

Go to the <a href="https://web-protect.gcore.com/waf/triggers/list" target="_blank">Triggers</a> tab, click the three dots next to the trigger you want to disable or delete, select the needed option, and confirm the action.

<img src="https://support.gcore.com/hc/article_attachments/10592589376529" alt="">

- If you disable a trigger, reactions for the trigger will be stopped until the trigger is enabled again. The disabled triggers are displayed in the list. To re-enable, use the Enable option.
- If you delete a trigger, it'll be permanently stopped and removed from the general list forever.