---
title: configure-weight-balancing-and-geobalancing
displayName: Dynamic response 
published: true
order: 10
toc:
   --1--Overview: "How-dynamic-response-works"
   --1--Configure: "configure-dynamic-response"
   --1--Preset settings: "examples-of-preset-settings"
   --2--Geo DNS: "geo-dns"
   --2--Geo distance: "geo-distance"
   --2--Weighted shuffle: "weighted-shuffle"
pageTitle: Configure Dynamic Response for DNSSet | Gcore
pageDescription: Learn how to configure CDN integration.
customUrl: /dns/dns-records/configure-weight-balancing-and-geobalancing
---
# Dynamic response

## How dynamic response works

Gcore's DNS server can provide different DNS responses to different users. For example, you can specify that particular records will be delivered to users in Asia versus users in Europe, or choose the weight for the records, i.e., the probability with which they will be shown in the responses. This is called dynamic response. Depending on which parameter is used to select which record will be shown, it may also be referred to as weight balancing, traffic steering, GeoDNS, or failover.

Pickers are used to control dynamic responses. They determine in what order the DNS query data will be checked and compared with the metadata set for the particular record.

Dynamic response makes the RRSet dynamic. You can add several records and determine which one will be in DNS responses depending on how the query meets the established criteria (e.g., user’s subnet or ASN, geo metadata, etc.)

Dynamic response setup consists of two stages:

1. **Set the metadata** or other data types against which the query parameters will be compared.
2. **Select pickers** to define the sequence in which the resolver will compare the query data for your record and check for matches against the metadata or other criteria of the specified record. 

For example, you can set the “Continent” picker and add metadata of the “continent” type with the value “Africa”. The result is that the record will only be retrieved for users located in Africa.

## Configure dynamic response

1\. Create a DNS record set in the <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#1-go-to-records-settings" target="_blank">advanced mode</a> (steps 1–4.)

2\. Enable the **Dynamic response** toggle.

3\. Select a picker preset from the "Presets" buttons or manually choose pickers from the list on the right. The order of the pickers in the left list dicatate priority: the top picker will be considered first, the second picker considered second, and so on.

<alert-element type="tip" title="Tip">

Presets are editable: You can select a preset and then change the position of pickers or add/remove pickers manually. 

</alert-element>

<expandable-element title="Available pickers">

The following pickers are available:

- **GeoDistance.** Geo proximity to the latlong (latitude and longitude) in the metadata determines the record in the response; the fallback metadata will be ignored.
- **Weighted shuffle.** Weight metadata determines the probability of the record hitting the response. 
- **Default.** Fallback metadata determines the record in the response if no other pickers were selected.
- **ASN.** The match with the ASN (autonomous system number) in the metadata determines the record in the response.
- **Country.** The match with the country in the metadata determines the record in the response.  
- **Continent.** The match with the continent in the metadata determines the record in the response.
- **Region.** The match with the region in the metadata determines the record in the response.
- **IP.** The match with IP address or CIDR notation (in IPv4 and IPv6) determines the record in the response.
- **Healthcheck.** Configure the choice of the record in response depending on the availability determined with <a href="https://gcore.com/docs/dns/dns-failover/about-dns-failover" target="_blank">Healthcheck</a>. 

The **First N** option is also in the list of pickers. It controls the maximum number of records used per response and is added to each preset. The default value is 1.

</expandable-element>

Adjust pickers as follows: 

- To raise or lower a picker, use the drag-and-drop method. 
- To remove a picker, click the cross. 
- To remove all selected pickers, click Clear.

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/pickers-10.png" alt="Dynamic response configuration" width="80%">

4\. Specify the record’s value.

5\. Set appropriate metadata to which the value in the query will be compared and specify the value. You can add several metadata fields for one value by clicking the plus button.

<expandable-element title="Available metadata">

Ten metadata types are available:

- asn (autonomous system number)
- continents
- countries
- regions
- latlong (latitude and longitude)
- fallback (only used in the response if no other metadata type is selected)
- backup (only used in combination with health checks to provide failover capability; if the rest of the records are not “healthy,” backup records will be used to form an answer; if at least one non-backup record is “healthy,” the record with the backup metadata does not participate in the response)
- notes (any comments; for example, you can specify a city, data center name, or cluster name)
weight
- ip (IP address or CIDR notation, IPv4 and IPv6)

</expandable-element>

6\. Click **Add record** to add several records to your response and repeat steps 4 and 5. 

7\. Click **Create**.

That's it. You've configured dynamic response for your DNSset.

## Examples of preset settings

<tabset-element>

### Geo DNS

With the “Geo DNS” preset, you can add metadata of different types to each record.

<alert-element type="warning" title="Warning">

The latlong and weight metadata will be ignored if you don’t add the corresponding pickers from the list.

</alert-element>

When a DNS request is made, the response will be formed using the chosen "Records selection" option and metadata specified for records.

Our system will check if a user matches the criteria from the metadata in the following order: IP, ASN, country, and continent. The processing logic works like this:

1. Gcore's DNS server receives a request to the domain.
2. If Health Checks are configured, we filter off all “non-healthy” records.
3. Gcore's DNS server compares the requestor user’s IP (respecting EDNS(0)) with the IP from the metadata. The server uses records with matching metadata to form an answer if possible.
4. If no matches are found, the ASN meta is considered as in step 3.
5. If no matches are found, the country meta is considered as in step 3.
6. If no matches are found, the continent meta is considered as in step 3.
7. If no matches are found, the region meta is considered as in step 3. 
8. If no matches are found, the records with “fallback=true” metadata are considered.
9. If no matches are found, all records are used in the answer (respecting the max answers value.)

**Example**: You selected the “Geo DNS” preset, specified one record per response in the First N.

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/geo-dns-20.png" alt="Configure Geo DNS preset" width="70%">

Then, you added two records with IP metadata:

- For ```10.0.0.0``` record, subnet 192.168.1.0/24
- For ```10.0.0.1``` record, subnet 192.0.2.0/24

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/geo-dns-30.png" alt="Configure metadata" width="80%">

If a user with the IP from the subnet 192.168.1.0/24 requests the domain, the record with the value ```10.0.0.0``` will be returned. If the requestor’s subnet is 192.0.2.0/24, the ```10.0.0.1``` record will be returned.

### Geo distance

With the “Geo distance” preset, you instruct resolvers to analyze the proximity of the geolocation of the request to the latlong (latitude and longitude) specified in the record’s metadata when a record is requested. Users will receive the record with the nearest coordinates when they request your domain. 

**Example**. You selected the “Geo distance” preset and specified one record per response in the First N.

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/geo-distance-40.png" alt="Configure Geo distance preset" width="80%">

Then, you added two records with the following coordinates:

- For the ```10.0.0.0``` record, latlong *51.52318152049715/-0.13458412218999416* (central London)
- For the ```10.0.0.1``` record, latlong *48.859741241898114/2.3415648470109653* (central Paris)

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/geo-distance-50.png" alt="Configure metadata" width="80%">

<figcaption>The orange color shows where two zones are close together, while the red and yellow show distinct zones</figcaption>

A user closer to the coordinate 51.52318152049715/-0.13458412218999416 (central London) will receive an A record with the value ```10.0.0.0```, while a user nearer to *48.859741241898114/2.3415648470109653* (central Paris) will receive an A record with the value ```10.0.0.1```.

### Weighted shuffle

With the “Weighted shuffle” preset, you can manage the probability of having a particular record in the answer by specifying its weight.

<alert-element type="info" title="Info">

If the metadata field “weight” is left empty, the default value 50, 33.3, 25, and etc. is used. This means each record has equal probability.

</alert-element>

Probability is calculated only if the value of First N exceeds the number of resource records. For a record R<sub>1</sub> from RRset with weight W<sub>1</sub>, its probability(P<sub>1</sub>) is calculated as its weight divided by the sum of the weights of all other records. 

<code-block>
P<sub>1</sub>= W<sub>1</sub> / Sum<sub>i</sub>(W<sub>i</sub>)
</code-block>

**Example**. You enabled the “Weighted shuffle” preset and specified max one record per response in the First N:

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/weighted-shuffle-60.png" alt="Configure Weighted shuffle picker" width="80%">

Metadata was specified as follows: 

- *1.2.3.4* with the “weight” 90, probability = 0.6
- *4.5.6.7* with the “weight” 10, probability = 0.06(6)
- *7.8.9.0* with the “weight” empty (i.e., set by default to 50,) probability = 0.3(3)

<img src="https://assets.gcore.pro/docs/dns/dns-records/configure-weight-balancing-and-geobalancing/weighted-shuffle-70.png" alt="Configure records for weighted shuffle usage" width="80%">

Over the course of 300 answers, each record will appear with the following frequency:
- ```~180``` responses with the record ```1.2.3.4``` (weight 90)
- ```~20``` responses with the record ```4.5.6.7``` (weight 10)
- ```~100``` responses with the record ```7.8.9.0``` (weight 50)

</tabset-element>