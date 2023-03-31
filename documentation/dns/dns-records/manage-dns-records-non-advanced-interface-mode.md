---
title: manage-dns-records-non-advanced-interface-mode
displayName: Manage DNS records (non-advanced)
published: true
order: 20
toc:
   --1--Create: "create-a-dns-record"
   --2--Records settings: "1-go-to-records-settings"
   --2--Record type: "2-select-record-type"
   --2--Domain or subdomain the record belongs to: "3-specify-subdomain-record-belongs-to"
   --2--Content of the record: "4-specify-content-of-record"
   --2--TTL: "5-specify-ttl"
   --2--Completing the configuration: "6-complete-configuration-and-create-resource-record"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
---
  
  
  
  
  

This article describes operations in the non-advanced mode of the "DNS" product interface. Differences in interfaces modes are described in the article "[Getting started with 'DNS'](https://support.gcore.com/hc/en-us/articles/360012142817)".

<img src="https://support.gcore.com/hc/article_attachments/4432998182673/image_21__1_.png" alt="image_21__1_.png" width="474" height="46">

## Create a DNS record

### 1. Go to records settings

Open the “All zones” tab and select the domain zone you want to add records for. Click it or the "Go to records" button next to it.

<img src="https://support.gcore.com/hc/article_attachments/5003716805265/mceclip0.png" alt="mceclip0.png">

Click “Add record”.

<img src="https://support.gcore.com/hc/article_attachments/4432903999889/image_14__2_.png" alt="image_14__2_.png">

You will see the interface for adding new DNS record. Perform other steps in it.

<img src="https://support.gcore.com/hc/article_attachments/5006389623569/mceclip1.png" alt="mceclip1.png">

### 2. Select record type


In the “Type” field, select the type of DNS record. There are seven types available:

*   **А** — defines the IP address the domain corresponds to. A record is for IPv4 addresses of the form 128.128.128.128.
*   **AAAA** — defines the IP address the domain corresponds to. AAAA record is for IPv6 addresses of the form 7625: 0d18: 1fa3: 07d7: 1f44: 8a2e: 07a0: 678h.
*   **NS** — defines addresses of DNS servers serving the domain.
*   **CNAME** — maps resource records of one domain to resource records of another. If you specify a CNAME record for site.com with the value “anothersite.com”, then when you open site.com it will have the same DNS records as anothersite.com has (for example, it will requests the same IP if A/AAAA records for anothersite.com exists).
*   **MX** — defines the server that receives mail for the domain.
*   **TXT**  — defines auxiliary information about the domain. For example, you can specify Sender Policy Framework (SPF) rules that determine mail servers allowed to receive mail.
*   **SRV** — defines the server that operates certain services for the domain.
*   **CAA** — defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name.

### 3. Specify subdomain record belongs to

In the “Name” field, specify the subdomain the record belongs to. To add a record for:

*   main domain (apex/naked domain; in the picture above it is examplesite.co) — leave the field blank;
*   apecific subdomain — enter the name of this subdomain (for example, if you enter "one" in the picture above, the record will be created for one.examplesite.co);
*   all subdomains at once (wildcard record) — enter an asterisk (\*).

### 4. Specify content of record

Fill in the "Content" field. Enter a value appropriate for your record type.

| Record type | Value                                                                                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A           | The IP address (IPv4) of the server of the web page that will open by your domain name.Example: 128.128.128.128                                                                                                                                                                                         |
| AAAA        | The IP address (IPv6) of the server of the web page that will open by your domain name.Example: 7625:0d18:1fa3:07d7:1f44:8a2e:07a0:678h                                                                                                                                                                 |
| NS          | The name of the zone you want to delegate your domain to. Example: ns1.smth.ru                                                                                                                                                                                                                          |
| CNAME       | The domain or domain zone name that your domain should refer to. Example: uuuuu8.cdn.co                                                                                                                                                                                                                 |
| MX          | The name of the mail server that receives mail for your domain. Example: ASPMX.L.GOOGLE.COMIf you are using multiple mail servers, fill in the “Priority” field for each server. The lower the value in this field, the higher the priority.                                                            |
| SRV         | The canonical name of the machine providing the service. Example: sip.example.com                                                                                                                                                                                                                       |
| TXT         | Text information the record should contain.Example: logmein-verification-code=976afe6f-8039-40e4-95a5-261b462                                                                                                                                                                                           |
| CAA         | Defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name. The recording consists of three parts which are separated by a space.CAA [flags] [tag] \"[value]\"The \"value\" must be enclosed in double-quotes (\"\").Example: 0 issue \"comodo.com\" |


### 5. Specify TTL

TTL (time to live) is the interval in seconds used by servers on the Internet to check if the DNS records for your domain have changed.

Example: A-record has a TTL of 300. You have changed the value of this record from “128.0.0.8” to “127.0.0.7”. Within 5 minutes, when requesting your domain, users will be sent to a server with IP 128.0.0.8 (this value will be stored in the cache of recursive DNS servers). But after 5 minutes, the DNS server will check the settings and see the new value of the A-record. Now, when your domain is requested, the DNS server will send users to the server with IP 127.0.0.7.

### 6. Complete configuration and create resource record

After completing the configuration, click the "Add" button. The DNS record with specified parameters will be created.

<img src="https://support.gcore.com/hc/article_attachments/4432965542673/image_20__1_.png" alt="image_20__1_.png">

## Edit a DNS record

1. Go to records of the required DNS zone by clicking the zone name or the "Go to records" button. 

<img src="https://support.gcore.com/hc/article_attachments/5003716805265/mceclip0.png" alt="mceclip0.png">

2. Click on the pencil icon next to the desired resource record.

<img src="https://support.gcore.com/hc/article_attachments/4436706707985/image_15.png" alt="image_15.png">

3. Make changes. 

4. Apply the new settings by clicking "Save".

##  Delete a DNS record

1. Go to records of the required DNS zone by clicking the zone name or the "Go to records" button. 

<img src="https://support.gcore.com/hc/article_attachments/5003716805265/mceclip0.png" alt="mceclip0.png">

2. Click the wastebasket icon next to the desired resource record.

<img src="https://support.gcore.com/hc/article_attachments/4436736225553/image_17.png" alt="image_17.png">

3. Confirm deletion.
