---
title: set-up-dns-for-sending-email
displayName: Sending emails
published: true
order: 40
toc:
    --1--Step 1. Set up an A record: "step-1-set-up-an-a-record"
    --1--Step 2. Set up an MX record: "step-2-set-up-an-mx-record"
    --1--Step 3. Set up a PTR record: "step-3-set-up-a-ptr-record"
    --1--Step 4. Set up SPF: "step-4-set-up-an-spf-txt"
    --1--Step 5. Set up DKIM: "step-5-set-up-dkim"
    --1--Step 6. Set up a DMARC policy: "step-6-set-up-a-dmarc-policy-txt"
pageTitle: How to Configure DNS Records to Send Emails | Gcore
pageDescription: Learn how to set up Gcore Managed DNS for sending emails, including setting up A, MX, PTR, SPF, DKIM records, and a DMARC policy.
---
# Configure DNS records to send emails

After setting up your mail server, configuring the correct DNS settings is a crucial step for it to work properly. In particular, it is important to configure the server so that emails sent from it do not end up in spam and attackers can’t send phishing emails on your behalf.

Anti-spam and anti-spoofing measures to counter such threats are configured via DNS. This is because usually only the true owner of the mail server has control over the DNS domain zone and can prove the validity of the mail server configuration.

<alert-element type="info" title="Info">

This product documentation guide describes the DNS configuration for those domains which are already delegated to Gcore name servers. You first need to create a DNS zone according to the guide: <a href="https://gcore.com/docs/dns/manage-a-dns-zone" target="_blank">Getting started with Managed DNS</a>.

</alert-element>

## Step 1. Set up an A record

An A record links a domain name to an IP address. For example, if your mail server's IP address is `192.0.2.1`, you'd set up an A record like this:

```
mail.sample-test.com. IN A 192.0.2.1
```

<img src="https://assets.gcore.pro/docs/dns/dns-records/set-up-dns-for-sending-email/email-records-10.png" alt="Adding an A record" width="85%">

Add an A record according to our guide on how to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">manage DNS records</a>.

## Step 2. Set up an MX record

An <a href="https://gcore.com/learning/dns-mx-record-explained/" target="_blank">MX record</a> binds your domain to the mail server you have created. Without an MX record, incoming mail on your domain will not work. It is recommended that you have more than one mail server so that the second one acts as a backup if the first one fails.
For example, if your domain is `sample-test.com` and your mail server is `mail.sample-test.com`, you'd set up an MX record like this:

```
sample-test.com. IN MX 10 mail.sample-test.com.
```

<img src="https://assets.gcore.pro/docs/dns/dns-records/set-up-dns-for-sending-email/email-records-20.png" alt="Adding an MX record" width="85%">

Add an MX record according to our guide on how to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">manage DNS records</a>.

## Step 3. Set up a PTR record

A PTR record, or reverse DNS record, links an IP address to a domain name. This is helpful for verifying the authenticity of your server. You can learn more about how it works and how to configure it in our guide about <a href="https://gcore.com/docs/dns/dns-records/set-up-a-ptr-record-and-reverse-dns-zone" target="_blank">a PTR record and reverse DNS zone</a>.

PTR records are typically set up by your service provider, so you'll need to get in touch with them to set up a reverse DNS zone (RDNS). Afterwards, you can add a PTR record in the Gcore Customer Portal according to our guide on how to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">manage DNS records</a>.

If the IP Address of your mail server is `192.0.2.1`, you'd set up a PTR record like this:

```
1.2.0.192.in-addr.arpa IN PTR mail.sample-test.com.
```

## Step 4. Set up SPF (TXT)

An SPF (Sender Policy Framework) record defines which IP addresses are allowed to send mail from your domain. Your domain’s security measures help prevent spam from being sent. An SPF record is added as a TXT record in your DNS.
Add an SPF record in the Gcore Customer Portal according to our guide on how to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">manage DNS records</a>. An example of an SPF record is:

```
sample-test.com. IN TXT "v=spf1 mx -all"
```
<img src="https://assets.gcore.pro/docs/dns/dns-records/set-up-dns-for-sending-email/email-records-30.png" alt="Adding a TXT record" width="85%">

This means only the IP addresses for the MX records in `sample-test.com`, i.e. `mail.sample-test.com` (with the IP `192.0.2.1`,) are allowed to send mail on behalf of the domain. `-all` means all other traffic should be considered spam.

## Step 5. Set up a DKIM record 

A <a href="https://gcore.com/learning/what-is-a-dkim-record/" target="_blank">DKIM (DomainKeys Identified Mail) record</a> adds a digital signature to your messages, allowing recipients to verify that the mail indeed came from your server.

A DKIM record is set up as a TXT record but requires a more complex setup process and adjustments of your mail server configuration, including generating a public and private key for signing and verification. This may require some technical knowledge or a utility that automates this process such as a <a href="https://easydmarc.com/tools/dkim-record-generator" target="_blank">DKIM Generator from EasyDMARC</a>, or from <a href="https://dmarcly.com/tools/dkim-record-generator" target="_blank">DMARCLY</a>.

## Step 6. Set up a DMARC policy (TXT)

A DMARC (Domain-based Message Authentication, Reporting, and Conformance) record defines how to handle emails that fail SPF and DKIM checks. This helps minimize harm from spam and security vulnerabilities. When an email is received, the recipient’s mail server checks the sending domain's SPF and DKIM records. If the records pass the checks, the email is considered legitimate. If either or both checks fail, the DMARC policy is examined.

The DMARC policy instructs the recipient's mail server on how to handle failed authentication emails. The policy can be set to none (no action taken), quarantine (mark as spam or place in a separate folder), or reject (block the email).

Here’s an example of a DMARC record in DNS settings:

```
_dmarc.sample-test.com. IN TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@sample-test.com; ruf=mailto:dmarc-forensics@sample-test.com;"
```

<img src="https://assets.gcore.pro/docs/dns/dns-records/set-up-dns-for-sending-email/email-records-40.png" alt="Adding a TXT DMARC record" width="85%">

In this example, the domain owner has set a DMARC policy to `quarantine` any emails that fail authentication. The `rua` parameter specifies the email address where aggregate reports will be sent, while the `ruf` parameter specifies the email address where forensic (detailed) reports will be sent.

You’ve now completed the necessary steps to configure the Gcore Managed DNS for your mail server so there won't be any problems with incoming and outgoing mail.