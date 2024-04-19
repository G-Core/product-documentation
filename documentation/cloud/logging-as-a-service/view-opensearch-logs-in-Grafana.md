---
title: view-opensearch-logs-in-grafana
displayName: 'View logs in Grafana with OpenSearch plugin'
published: true
order: 50
pageTitle: View logs in Grafana with OpenSearch plugin | Gcore
pageDescription: Install and connect the OpenSearch Grafana Data Source plugin in Grafana to view logs on Grafana dashboards.
---
# View Gcore Managed Logging logs in Grafana with OpenSearch plugin

The <a href="https://grafana.com/grafana/plugins/grafana-opensearch-datasource/?tab=overview" target="_blank">OpenSearch Grafana Data Source</a> plugin allows you to integrate logs from OpenSearch Dashboards into Grafana. This means that you get a consolidated view of all your metrics in one place and can also benefit from Grafana's advanced alerting and visualization features. Additionally, you gain full control over who can view and manage your logs, ensuring the protection of any sensitive information.

## Step 1. Set up logging in the Gcore Customer Portal

To enable OpenSearch integration with Grafana, you need to configure Managed Logging in the Gcore Customer Portal. You can find more information in our guide <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">Configure Logging and view your logs</a>.

## Step 2. Install OpenSearch plugin in Grafana

If you’ve already installed the plugin, skip these instructions and proceed to **Step 3**.

To install the plugin:

1\. In Grafana, navigate to the **Administration** section and click **Plugins**.

2\. Search for the OpenSearch plugin. In the **State** dropdown, make sure to select **All**. Otherwise, you won’t see the plugin in search results.

3\. Click **Install**.

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-plugins-search.png" alt="Plugins page in Grafana featuring OpenSearch plugin" width="80%">

The installation may take a few minutes.  

## Step 3. Configure the OpenSearch plugin to display logs in Grafana

1\. Open the plugin in Grafana.

2\. In the upper-right corner of the screen, click **Add new data source**. 

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-add-data-source.png" alt="OpenSearch plugin overview in Grafana" width="80%">

3\. Configure the HTTP parameters:

- **URL**: Enter the link of OpenSearch API endpoint. You can find the link in the Gcore Customer Portal on the **Logging** page.

- **Access**: If you select “Server (default)”, the URL will be accessible from the Grafana backend/server. If you choose “Browser”, the URL will be accessible from the browser.

- **Allowed cookies**: Specify which cookies are allowed to be included in requests to the OpenSearch endpoint.

- **Timeout**: Set the maximum waiting time for a response from OpenSearch. This will determine how long Grafana will wait for a response before terminating the connection.

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-opensearch-http-config.png" alt="HTTP settings of the OpenSearch plugin in Grafana" width="80%">

4\. Configure authentication. Select **Basic auth** and use the credentials you’ve configured on the **Logging** page in the Gcore Customer Portal.

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-opensearch-auth-config.png" alt="Authentication settings of the OpenSearch plugin in Grafana" width="80%">

<alert-element type="info" title="Info">
 
After you select the Basic auth, you might see the following error: “OpenSearch error: no permissions for [indices:admin/mappings/get] and User [name=test2, backend_roles=[], requestedTenant=null]”. 

This error doesn’t affect the plugin’s work. You can ignore it and proceed with the next steps. 
 
</alert-element>

5\. Click **Save & test** to save the configuration. 

## Step 3. View your logs in Grafana

The following instructions explain how to create a new dashboard in Grafana and use it to display your log data. You can find detailed instructions on how to use and manage dashboards in the official Grafana guide: <a href="https://grafana.com/docs/grafana/latest/dashboards/" target="_blank">Dashboards</a>.

To display logs on a new Grafana dashboard:

1\. In the sidebar, click **Dashboards**. 

2\. In the upper-right corner of the screen, click **New** > **New dashboard**.

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-add-dashboard.png" alt="Dashboards page in Grafana with the new dashboard button highlighted" width="80%">

3\. Click **Add visualization**.

<img src="https://assets.gcore.pro/docs/cloud/laas/view-logs-in-grafana/grafana-add-visualization.png" alt="Grafana dashboard with the Add visualization button highlighted" width="80%">

4\. Search for the **grafana-opensearch-datasource** plugin and click the plugin name to add data to the dashboard.

Your log data will appear on this new dashboard.