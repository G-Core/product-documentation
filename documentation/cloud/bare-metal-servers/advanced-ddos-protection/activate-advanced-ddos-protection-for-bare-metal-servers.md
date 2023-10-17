---
title: activate-advanced-ddos-protection-for-bare-metal-servers
displayName: Activate Advanced DDoS Protection for bare metal servers
published: true
toc:
   --1--Method 1. When creating a bare metal server: "creating-a-bare-metal-server"
   --1--Method 2. By changing the interface configuration: "interface-configuration"
   --1--Method 3. Via the Network tab: "ddos-protection-list"
pageTitle: Activate DDoS Protection for bare metal servers | Gcore
pageDescription: Activate DDoS Protection for bare metal servers with Gcore. Follow the steps in the article to enable robust defense and uninterrupted uptime.
---
# Activate Advanced DDoS Protection for bare metal servers

## Creating a bare metal server

1. On your Gcore account, click on **Cloud**, then select **Bare Metal Servers**.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773280152465.png" alt="mceclip0.png">

2. Review the settings in the **Create Bare Metal** section, then go to the **Network interface**.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773282277777.png" alt="mceclip1.png">

3. **Enable Advanced DDoS protection** by clicking on the network interface. Please keep in mind that protection can only be enabled on external interfaces or subinterfaces with public IP addresses. The protection does not cover internal interfaces.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773270922513.png" alt="mceclip2.png">

4. Click the **Select profile template** dropdown. Be sure to fill in additional parameters of the protection template selected.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773319536529.png" alt="mceclip3.png">

5. Once you select the profile template, type in the SSH keys and add a name under the **Additional options** section.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773321433361.png" alt="Additional options section" width=80%>

6. If you’re finished, click the **Create Server** button on the right-hand side.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773276389905.png" alt="mceclip5.png">

## Interface configuration

1. From the **Cloud** panel, select **Bare Metal Servers**, then click the name of your bare metal server.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773445344913.png" alt="mceclip6.png">

2. Click on the **Networking** tab.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773450082065.png" alt="mceclip7.png" width="503" height="413">

3\. Click on the interfaces. Click on the kebab menu on the far right-hand side, then choose to enable advanced DDoS protection.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773488996113.png" alt="mceclip8.png">

4. The **Edit advanced DDoS protection profile** pop-up will appear. Click the dropdown to choose your preference, then hit submit.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773522634769.png" alt="mceclip9.png">

5. To check, click **DDoS Protection** under the Cloud panel on the left-hand side. The type of security should show as **Advanced**.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773524742417.png" alt="mceclip10.png">

## DDoS protection list

1. Select **Networking** on the left-hand menu.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773548591761.png" alt="Networking " width=80%>

2. Click **DDoS Protection** from the dropdown options.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773581148049.png" alt="DDoS Protection " width=80%>

3. In the **DDoS Protection** section, select the bare metal server you want to enable advanced DDoS protection for by clicking the kebab menu on the right side.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773583120913.png" alt="mceclip13.png">

4. The **Edit advanced DDoS protection profile** pop-up will appear. Click the dropdown to choose your preference. Examples for a profile are the following:

*   CMP block
*   CS:GO
*   Rust ARK
*   Basic L3/L4
*   TCP protection

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773590363153.png" alt="mceclip14.png">

5. Once you have selected the profile, click submit. Be sure to fill in the required fields based on the selected profile.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773623336337.png" alt="mceclip15.png">

6. Once you’re done, the type of DDoS protection will be changed from basic to advanced, and the name of the profile and other additional parameters will appear.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/advanced-ddos-protection/activate-advanced-ddos-protection-for-bare-metal-servers/11773625038225.png" alt="mceclip16.png">