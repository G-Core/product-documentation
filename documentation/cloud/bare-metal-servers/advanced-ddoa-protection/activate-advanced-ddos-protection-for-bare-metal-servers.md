---
title: activate-advanced-ddos-protection-for-bare-metal-servers
displayName: Activate Advanced DDoS Protection for bare metal servers
published: true
toc:
   --1--Method 1. When creating a baremetal server: "creating-a-baremetal-server"
   --1--Method 2. By changing the interface configuration: "interface-configuration"
   --1--Method 3. Via the Network tab: "ddos-protection-list"
---
# Activate Advanced DDoS Protection for bare metal servers

## Creating a baremetal server

1. On your Gcore account, click on **Cloud**, then select **Baremetal**.

<img src="https://support.gcore.com/hc/article_attachments/11773280152465" alt="mceclip0.png">

2. Review the settings in the Create baremetal server section, then go to the **Network interface**.

<img src="https://support.gcore.com/hc/article_attachments/11773282277777" alt="mceclip1.png">

3. **Enable Advanced DDoS protection** by clicking on the network interface. Please keep in mind that protection can only be enabled on external interfaces or subinterfaces with public IP addresses. The protection does not cover internal interfaces.

<img src="https://support.gcore.com/hc/article_attachments/11773270922513" alt="mceclip2.png">

4. Click the **Select profile template** dropdown. Be sure to fill in additional parameters of the protection template selected.

<img src="https://support.gcore.com/hc/article_attachments/11773319536529" alt="mceclip3.png">

5. Once you select the profile template, type in the SSH keys and add a name under the **Additional options** section.

<img src="https://support.gcore.com/hc/article_attachments/11773321433361" alt="mceclip4.png" alt="" width=80%>

6. If you’re finished, click the **Create Server** button on the right-hand side.

<img src="https://support.gcore.com/hc/article_attachments/11773276389905" alt="mceclip5.png">

## Interface configuration

1. From the **Cloud** panel, select **Baremetal**, then click the name of your baremetal server.

<img src="https://support.gcore.com/hc/article_attachments/11773445344913" alt="mceclip6.png">

2. Click on the **Networking** tab.

<img src="https://support.gcore.com/hc/article_attachments/11773450082065" alt="mceclip7.png" width="503" height="413">

3\. Click on the interfaces. Click on the kebab menu on the far right-hand side, then choose to enable advanced DDoS protection.

<img src="https://support.gcore.com/hc/article_attachments/11773488996113" alt="mceclip8.png">

4. The **Edit advanced DDoS protection profile** pop-up will appear. Click the dropdown to choose your preference, then hit submit.

<img src="https://support.gcore.com/hc/article_attachments/11773522634769" alt="mceclip9.png">

5. To check, click **DDoS Protection** under the Cloud panel on the left-hand side. The type of security should show as **Advanced**.

<img src="https://support.gcore.com/hc/article_attachments/11773524742417" alt="mceclip10.png">

## DDoS protection list

1. Go to the **Networking** tab on the left-hand menu and click **DDoS Protection** from the dropdown options.

2. In the **DDoS Protection** section, select the baremetal server you want to enable advanced DDoS protection for by clicking the kebab menu on the right side.

<img src="https://support.gcore.com/hc/article_attachments/11773583120913" alt="mceclip13.png">

3. The **Edit advanced DDoS protection profile** pop-up will appear. Click the dropdown to choose your preference. Examples for a profile are the following:

*   CMP block
*   CS:GO
*   Rust ARK
*   Basic L3/L4
*   TCP protection

<img src="https://support.gcore.com/hc/article_attachments/11773590363153" alt="mceclip14.png">

4. Once you have selected the profile, click submit. Be sure to fill in the required fields based on the selected profile.

<img src="https://support.gcore.com/hc/article_attachments/11773623336337" alt="mceclip15.png">

5. Once you’re done, the type of DDoS protection will be changed from basic to advanced, and the name of the profile and other additional parameters will appear.

<img src="https://support.gcore.com/hc/article_attachments/11773625038225" alt="mceclip16.png">