---
title: configure-weight-balancing-and-geobalancing
displayName: Configure balancing 
published: true
order: 25
toc:
   --1--Overview: "overview"
   --1--Balancing: "how-is-balancing-controlled"
   --1--Configure: "configure-balancing-in-the-control-panel"
   --1--Types: "types-of-balancing"
   --2--weight: "balancing-by-weight-default"
   --2--non-coordinate (ip, e.g.): "balancing-by-non-coordinates-meta"
   --2--coordinates: "balancing-by-coordinates-geo-proximity"
pageTitle: Configure weight & Geobalancing in DNS | Gcore
pageDescription: Learn how to configure weight balancing and Geobalancing for DNS records with Gcore.
---
# Configure weight balancing and Geobalancing

## Overview

Our DNS server can provide different DNS responses to different users. For example, you can specify that particular records will be delivered to users from Asia verses Europe, or choose the weight for the records, i.e. the probability with which they will be shown in the responses.

This is called dynamic record selection. Depending on which parameter is used to select which record will be shown, it may also be referred to as weight balancing, traffic steering, GeoDNS, or failover. 

At Gcore, we offer two kinds of balancing: *weight balancing* and *Geobalancing*; the latter is a specific kind of balancing by location. This article will show how to configure weight balancing and Geobalancing by coordinates and other parameters. 

## How is balancing controlled?

Balancing is controlled by the metadata that you add to each record in your RRSet. You can add nine types of data: *ip, asn, continents, countries, latlong, fallback, backup, notes,* and *weight*.

The system will check if a requestor’s IP (usually a recursive DNS) correlates to the specified meta parameters for the records in RRset and our geodatabase. If they do, the system will pick those records for the response. For example, you can add metadata of the “continent” type with the value “Africa” to a record, which will only be given to users from Africa.

Three types of balancing are available:

- By weight (default)
- By non-coordinate meta (all metadata types except latlong)
- By coordinates (geo proximity) 

**Note**: Balancing (Geobalancing and weight balancing) is a paid option, mind your tariff plan limits.

## Configure balancing in the control panel

1. Create a <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">resource record in advanced mode</a> (steps 1–6.)

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/configure-balancing-10.png" alt="Configure balancing in the control panel" width="80%">

2. Move the slider in the **Records selection** using section to enable balancing.

3. Tick the balancing type you wish to select. More details <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing#types-of-balancing" target="_blank">below</a>. 

4. Specify the maximum number of records in one response in the right field. The default value is one record per response.

5. Configure Health Checks if needed. Learn more about them in <a href="https://gcore.com/docs/dns/dns-failover/about-dns-failover" target="_blank">our article</a>.

6. Specify the record’s value.

7. Select appropriate metadata and specify the value. You can add several metadata fields for one value. To do this, click **+**.

8. Click **Add record** if needed and repeat steps 6-7. 

9. Click **Create**.

## Types of balancing

For each type of balancing, we will break down the principle of operation, look at its features, and consider an example.

### Balancing by weight (default)

With weight balancing, you can manage the probability of having a particular record in the answer by specifying its weight.

**Note**: If the metadata field “weight” is left empty, the default value 50 is used. So you can expect the same probability for each record.

Probability is calculated only if the value of max records per answer exceeds the number of resource records. For a record R1 from RRset with weight W1, its probability(P1) is calculated as its weight divided by the sum of the weights of all other records. 

<code-block>
P<sub>1</sub>= W<sub>1</sub> / Sum<sub>i</sub>(W<sub>i</sub>)
</code-block>

**Example**. You have weight balancing enabled, specified max one record per response, and added three records with these weight metadata:

- *1.2.3.4* with the “weight” 90, probability = 0.6
- *4.5.6.7* with the “weight” 10, probability = 0.06(6)
- *7.8.9.0* with the “weight” empty (i.e., set by default to 50,) probability = 0.3(3)

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/configure-balancing-20.png" alt="Balancing by weight" width="80%">

### Balancing by non-coordinates meta

With non-coordinates meta balancing, you can add metadata of different types to each record.

**Note**: The *latlong* and *weight* will be ignored when using non-coordinate metadata.

When a DNS request is made, the answer will be formed using the chosen *Records selection* option and metadata specified for records. The following metadata can be used to be checked against the source of the DNS query:

- IP (IP address or CIDR notation, IPv4 and IPv6)
- ASN (autonomous system number)
- Continents
- Countries
- Fallback (only used in an answer if no other records were selected)
- Backup (only used in combination with Health Checks to provide failover capability; if the rest of the records are not “healthy,” backup records will be used to form an answer; if at least one non-backup record is “healthy,” the record with the backup metadata does not participate in the response)
- Notes (any comments; for example, you can specify a city, data center name, or cluster name)

Our system will check if a user matches the criteria from the metadata in the following order: IP, ASN, country, and continent. The processing logic works like this:

1. Our DNS server receives a request to the domain.

2. If Health Checks are configured, we filter off all “non-healthy” records.

3. The DNS server compares the requestor user’s IP (respecting EDNS(0)) with the IP from the metadata. The server uses records with matched metadata to form an answer if there is a match.

4. If no matches are found, the ASN meta is considered as in step 3.

5. If no matches are found, the country meta is considered as in step 3.

6. If no matches are found, the continent meta is considered as in step 3.

7. If no matches are found, the records with “fallback=true” metadata are considered.

8. If no matches are found, all records are used in the answer (respecting max answers value).

**Example**: You have non-coordinates balancing enabled, specified max one record per response, and you add two records with IP metadata:

- For *10.0.0.0* record, subnet *192.168.1.0/24*
- For *10.0.0.1* record, subnet *192.0.2.0/24* 

Here’s how it looks when you add these records:

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/configure-balancing-30.png" alt="Here’s how it looks when you add these records" width="80%">

If a user with the IP from the subnet *192.168.1.0/24* requests the domain, the record with the value *10.0.0.0* will be returned. If the requestor’s subnet is *192.0.2.0/24*, the *10.0.0.1* record will be returned.

### Balancing by coordinates (geo proximity) 

With coordinates balancing, you can assign coordinates to each record and add the latlong (latitude and longitude) type metadata. Users will receive the record with the nearest coordinates when they request your domain. You can use the map icon to check you’ve entered the correct coordinates—simplyclick on the icon to see the location corresponding to your parameters.

**Example**. A user closer to the coordinate 40.43733088856228/-3.566434349995511 (the center of Madrid) will receive an A record with the value *127.0.0.1*, while a user nearer to 52.20328569593686/21.081144277439293 (the center of Warsaw) will receive an A record with the value *127.0.0.2*.

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/image-3723.png" alt="Balancing by non-coordinates meta" width="80%">

The configuration is complete. As soon as you finish creating records, balancing will be enabled.
