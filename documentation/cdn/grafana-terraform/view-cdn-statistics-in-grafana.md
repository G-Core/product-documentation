---
title: view-cdn-statistics-in-grafana
displayName: Grafana reports
published: true
order: 10
toc:
   --1--Download and install the Gcore plugin: "download-and-install-the-plugin"
   --1--Configure the Dashboard for a convenient display of information: "configure-the-dashboard"
   --1--Download and install the plugin: "the-download-and-install-the-plugin-step-video-instructions"
   --1--Configure the Dashboard: "configure-the-dashboard-step-video-instructions"
pageTitle: Display CDN Stats in Grafana with Gcore | Gcore
pageDescription: Step-by-step guide to configure CDN statistics in Grafana using Gcore's plugin for comprehensive traffic analysis.
---
# Veiw CDN statistics in Grafana

With the Gcore cdn-stats plugin in Grafana, you can display the CDN statistics by:

- **Total Traffic,** which is total traffic volume, consisting of traffic from origin to CDN or <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> + from <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to CDN + from CDN to users;
- **Byte cache Hit Ratio,** which is the share of cached traffic, calculated using the formula: 1-(traffic from the origin to the CDN or <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a>/traffic from the CDN to users);
- **Edges Traffic,** which is traffic from CDN, consisting of traffic from <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to CDN + from CDN to users;
- **Shield Traffic,** which is traffic from <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to CDN;
- **Origin Traffic,** which is traffic from the origin, consisting of traffic from the origin to the CDN or from the origin to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a>;
- **Total Requests,** which is the number of requests to the CDN;
- **2xx, 3xx, 4xx, 5xx Responses,** which is the number of 2xx, 3xx, 4xx, and 5xx responses;
- **Bandwidth,** which is bandwidth, calculated based on traffic from the origin to the CDN or <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> + from <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to CDN + from CDN to users;
- **Cache Hit Ratio,** which is the share of sending cached content, consisting of responses with cached content / requests to CDN;
- **Shield traffic ratio** is the efficiency of the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a>: how much more traffic is sent from the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> than from the origin, calculated using the formula: (traffic from the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to the CDN - traffic from the origin to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a>) / traffic from the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Shielding</a> to the CDN;

You can group metrics by the following parameters:

- **Clients** is for clients;
- **Resource** is for CDN resources;
- **Region** is for regions;
- **Country** is for countries;
- **Data** is for data centers;
- **Vhost** is for a personal domain.

**Note**: The plugin is designed for Grafana version 7.0 and higher.

To configure CDN statistics in Grafana, you need to:

*   Use Grafana version 7.0 and higher.

Video instructions of the steps:

## Download and install the plugin

<a href="https://github.com/G-Core/cdn-stats-datasource-plugin/releases" target="_blank">Download</a> the gcore-cdn-stats-datasource-1.0.8.zip file with the latest version of the plugin in GitHub.

**Note**: The numbers (1.0.8) in the file name indicate the plugin version and may differ depending on updates.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/_____________.png" alt="Download and install the plugin" >

Unzip the archive to the Grafana plugin folder. By default, this is the *Grafana\grafana\data\plugins* installation folder.

<a href="https://grafana.com/docs/grafana/latest/installation/restart-grafana" target="_blank">Restart</a> and <a href="https://grafana.com/docs/grafana/latest/getting-started/getting-started/#step-2-log-in" target="_blank">log</a> in to Grafana.

Click the gear icon in the menu to open the "Configuration" section, select "Data Sources".

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/data_source.png" alt="Configuration">

Click **Add data source** to add a new resource for getting data.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/_________Data_Source.png" alt="data source" width="50%">

Find the cdn-stats plugin from Gcore and click "Select".

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/cdn-stats.png" alt="cdn-stats plugin" width="80%">

The plugin settings will be opened. Add a permanent API token to the "Auth" section.

You can get a token in your personal account. To do this, go to Profile > API tokens > Create. 

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/mceclip0.png" alt="Add a permanent API token">

Insert the received API token in the API token field in the format: **APIKey** {the received API token}.

For example: ```APIKey 7711$eyJ0eXAiOiJKV```

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/api_token_1.png" alt="Insert the received API token" width="80%">

Click **Save & Test**.

If everything is correct, you will see the following messages: "Datasource updated" and "You successfully authenticated as {Name}".

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/save_test.png" alt="Save " width="80%">

## The Download and install the plugin step video instructions

<iframe width="560" height="315" src="https://www.youtube.com/embed/9XZSTnJjqYs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
</iframe>

## Configure the Dashboard

Click on the **+** in the menu to open the "Create" section, select "Dashboard" to add a new dashboard.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/dashboard.png" alt="Configure the Dashboard" width="50%">

In the next window, click "Add an empty panel" to create a new panel.

 <img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/add_panel.png" alt="Add an empty pane" width="50%">

Make sure that "cdn-stats" is set as the data source in the Query section.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/query.png" alt="query.png" width="50%">

Select the necessary metric, granularity, and grouping (you can select several).

 <img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/query_props_1.png" alt="Select the necessary metric," width="50%">

The "Legend" field displays the values of the Group by field and the name of the metric by default:

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/grafa.jpg" alt="Legend" width="50%">

You can customize the output of legend data.

Set a name for the metric and in brackets {{}} set the parameters specified in the Group by field.

For example, for the settings above, you can set the following format: Traffic quantity — {{resource}}.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/15717167195025.png" alt="Traffic " width="80%">

Open the dashboard settings by clicking on the gear icon in the upper-right corner.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/panel_settings.png" alt="dashboard settings" width="50%">

Go to the "Variables" section and click "Add variable". You can use it to filter the data on the chart.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/add_variable.png" alt="Variables" width="80%">

For example, to be able to filter resources, you need to make the following settings and click "Update":

- In the **_Name_** you can specify the variable name (required).
- In the **_Values for_** you can select a value for the variable: resourceID (resources).
- In the **_Sort_** you can set the sorting order of the elements (optional)
- In the **_Selection Options_** you can set the way of how elements can be selected (optional)
    - In the **_Multi-value_** you can set the ability to select multiple elements.
    - In the **_Include All option_** you can set the ability to select all elements by marking the All value.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/variables_edit.png" alt="Update" width="80%">

Go back to the dashboard by clicking the arrow icon in the upper-left corner of the screen.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/go_back.png" alt="Go back t">

Connect the variable with the Dashboard. To do this, specify its name in the "Resources" field of the "Filters (comma separated)" section.

**Important!** Enter "$" before the variable name.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/filters.png" alt="Resources" width="50%">

Now you can choose resource data to be displayed on the chart.

<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/pane_____.png" alt="chart" width="50%">

Save the Dashboard. To do this, click "Save" in the upper-right corner of the panel.  
  
<img src="https://assets.gcore.pro/docs/cdn/grafana-terraform/view-cdn-statistics-in-grafana/save.png" alt="Save the Dashboard" width="50%">

## Configure the Dashboard step video instructions

<iframe width="560" height="315" src="https://www.youtube.com/embed/EZUdzlpyyDU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>