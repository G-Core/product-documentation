---
title: waf-and-owasp-top-threats
displayName: WAF and OWASP top threats
published: true
order: 20
toc:
   --1--Configure policy rules: "configure-policy-rules"
pageTitle: Set up WAF and OWASP top threats WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize WAF and OWASP top threats policy.
---
# WAF and OWASP top threats

The WAF & OWASP Top 10 policy contains a robust set of rules that help protect your application against the most critical security risks standardized by the <a href="https://owasp.org/" target="_blank">Open Web Application Security Project (OWASP)</a>. 

## Configure policy rules 

You can review the WAF & OWASP Top 10 policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/waf-and-owasp-top-threats/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **WAF and OWASP top threats** to expand the section and adjust the policy rules. 

<img src="https://assets.gcore.pro/docs/waap/waf-policies/waf-and-owasp-top-threats/waf-and-owasp-top-threats.png" alt="WAF policies page with the highlighted IP reputation policy">

<alert-element type="info" title="Info">

Only the **Open redirect** and **Personally identifiable information** rules are enabled by default. To enable a rule, turn on the toggle near that rule. 

</alert-element>

The following table features the full list of rules that you can configure as part of the WAF & OWASP top threats policy. These rules correspond to the most common types of threats.  

<table>
<thead>
<tr>
<td style="text-align: left">Rule</td>
<td style="text-align: left">Description</td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">SQL injection</td>
<td style="text-align: left">
In this form of attack, hackers use malicious SQL code to manipulate the backend of a database and access sensitive information like company data, user lists, or private customer details.<br><br>
Enable the rule to detect and block any attempts to alter database queries. 
</td>
</tr>
<tr>
<td style="text-align: left">Cross-site scripting (XSS)</td>
<td style="text-align: left">XSS attacks happen when an attacker uses a web application to send malicious code to a different user.<br><br>
Enable the rule to detect and prevent XSS attacks by analysing incoming requests for malicious script injections and blocking the execution of such scripts.</td>
</tr>
<tr>
<td style="text-align: left">Shellshock exploit</td>
<td style="text-align: left">This is a Bash shell vulnerability that can be exploited by attackers to execute arbitrary code and potentially harmful commands.<br><br>
By enabling the rule, you protect your application against malicious attempts to inject unauthorized commands into Bash environments.</td>
</tr>
<tr>
<td style="text-align: left">Remote file inclusion</td>
<td style="text-align: left">This attack exploits vulnerabilities in web applications, which dynamically reference external scripts.<br><br>
Enable the rule to protect against unauthorized inclusion of remote files.</td>
</tr>
<tr>
<td style="text-align: left">Apache Struts exploit</td>
<td style="text-align: left">Apache struts v1 contains a vulnerability that allows malicious users to exploit the Object-Graph Navigation Language.<br><br>
Enable the rule to safeguard your web application against malicious exploits that target vulnerabilities in the Apache framework.</td>
</tr>
<tr>
<td style="text-align: left">Local file inclusion</td>
<td style="text-align: left">Some attackers can exploit vulnerable inclusion procedures in a web application by injecting files that already exist on a server.<br><br>
Enable the rule to defend against the unauthorized inclusion of local files. </td>
</tr>
<tr>
<td style="text-align: left">Common web application vulnerabilities</td>
<td style="text-align: left">Enable the rule to protect your application against a range of prevalent web vulnerabilities.</td>
</tr>
<tr>
<td style="text-align: left">Web shell execution prevention</td>
<td style="text-align: left">Malicious scripts are often used to escalate and maintain persistent access to compromised web applications. This is a common post-exploitation attack.<br><br>
Enable the rule to block any attempts to execute web shell scripts and to gain unauthorized access to your application.</td>
</tr>
<tr>
<td style="text-align: left">Protocol attack</td>
<td style="text-align: left">These types of attacks are designed to eat up the processing capacity of a network infrastructure resource like server, firewall, or load balancer.<br><br>
Enable the rule to block any attempts to inject and manipulate headers or query parameters through sanitation of insufficient user input. </td>
</tr>
<tr>
<td style="text-align: left">Cross-site request forgery (CSRF)</td>
<td style="text-align: left">CSRF is an attack that exploits a vulnerability in a web application. This happens if the application can’t differentiate between a request generated by an individual user and a request initiated by a user without their consent.<br><br>
Enable the rule to prevent such attacks and ensure the integrity of user interactions with your application.</td>
</tr>
<tr>
<td style="text-align: left">Open redirect</td>
<td style="text-align: left">This vulnerability occurs when attackers exploit unfiltered or unvalidated redirect destinations provided by a client.<br><br>
Enable the rule to defend against unauthorized and potentially malicious URL redirects. 
</tr>
<tr>
<td style="text-align: left">Shell injection</td>
<td style="text-align: left">This vulnerability allows an attacker to execute arbitrary operating system commands on the server that’s running an application.<br><br>
Enable the rule to block malicious attempts to inject unauthorized commands into web application shells.</td>
</tr>
<tr>
<td style="text-align: left">Code injection</td>
<td style="text-align: left">This attack involves injecting malicious code that is interpreted or executed by the application. This is usually possible due to a lack of proper input and output validation.<br><br>
Enable the rule to prevent any attempts to inject unauthorized code or commands into web applications.</td>
</tr>
<tr>
<td style="text-align: left">Sensitive data exposure</td>
<td style="text-align: left">These attacks target sensitive data, aiming to expose critical information about the company, its customers, or its users.<br><br>
Enable the rule to protect against the accidental exposure of application-related data.</td>
</tr>
<tr>
<td style="text-align: left">XML External Entity (XXE)</td>
<td style="text-align: left">This attack occurs when XML input that contains a reference to an external entity is processed by a weakly configured XML parser.<br><br>
Enable the rule to ensure the security and integrity of your XML-based data.</td>
</tr>
<tr>
<td style="text-align: left">Personally identifiable information</td>
<td style="text-align: left">When personally identifiable information (PII) isn’t properly protected, it can cause a security vulnerability and lead to data leakage.<br><br>
Enable the rule to prevent accidental exposure of personal data by searching for private information on the web application responses.</td>
</tr>
<tr>
<td style="text-align: left">Server-side template injection</td>
<td style="text-align: left">Some attackers can use native template syntax to inject a malicious payload into a template and then execute it on the server.<br><br>
Enable the rule to block attempts to inject unauthorized code into your web application templates.</td>
</tr>
</tbody>
</table>