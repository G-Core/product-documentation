---
title: view-cdn-statistics-in-grafana
displayName: Grafana reports
published: true
order: 10
toc:
   --1--Download and install the Gcore plugin.: "download-and-install-the-plugin"
   --1--Configure the Dashboard for a convenient display of information.: "configure-the-dashboard"
   --1--Download and install the plugin.: "the-download-and-install-the-plugin-step-video-instructions"
   --1--Configure the Dashboard.: "configure-the-dashboard-step-video-instructions"
---
With the **Gcore cdn-stats plugin** in Grafana, you can display the CDN statistics by:

*   **Total Traffic,** which is total traffic volume, consisting of traffic from origin to CDN or [Shielding](https://www.gcore.com/support/articles/214080309/) + from [Shielding](https://www.gcore.com/support/articles/214080309/) to CDN + from CDN to users;
*   **Byte cache Hit Ratio,** which is the share of cached traffic, calculated using the formula: 1-(traffic from the origin to the CDN or [Shielding](https://www.gcore.com/support/articles/214080309/)/traffic from the CDN to users);
*   **Edges Traffic,** which is traffic from CDN, consisting of traffic from [Shielding](https://www.gcore.com/support/articles/214080309/) to CDN + from CDN to users;
*   **Shield Traffic,** which is traffic from [Shielding](https://www.gcore.com/support/articles/214080309/) to CDN;
*   **Origin Traffic,** which is traffic from the origin, consisting of traffic from the origin to the CDN or from the origin to the [Shielding](https://www.gcore.com/support/articles/214080309/);
*   **Total Requests,** which is the number of requests to the CDN;
*   **2xx, 3xx, 4xx, 5xx Responses,** which is the number of 2xx, 3xx, 4xx, and 5xx responses;
*   **Bandwidth,** which is bandwidth, calculated based on traffic from the origin to the CDN or [Shielding](https://www.gcore.com/support/articles/214080309/) + from [Shielding](https://www.gcore.com/support/articles/214080309/) to CDN + from CDN to users;
*   **Cache Hit Ratio,** which is the share of sending cached content, consisting of responses with cached content / requests to CDN;
*   **Shield traffic ratio** is the efficiency of the [Shielding](https://www.gcore.com/support/articles/214080309/): how much more traffic is sent from the [Shielding](https://www.gcore.com/support/articles/214080309/) than from the origin, calculated using the formula: (traffic from the [Shielding](https://www.gcore.com/support/articles/214080309/) to the CDN - traffic from the origin to the [Shielding](https://www.gcore.com/support/articles/214080309/)) / traffic from the [Shielding](https://www.gcore.com/support/articles/214080309/) to the CDN;

You can group metrics by the following parameters:

*   **Clients** is for clients;
*   **Resource** is for CDN resources;
*   **Region** is for regions;
*   **Country** is for countries;
*   **Data** is for data centers;
*   **Vhost** is for a personal domain.

**Important!** The plugin is designed for Grafana version 7.0 and higher.

To configure CDN statistics in Grafana, you need to:

*   Use Grafana version 7.0 and higher.

Video instructions of the steps:

Download and install the plugin
===============================

[Download](https://github.com/G-Core/cdn-stats-datasource-plugin/releases) the gcore-cdn-stats-datasource-1.0.8.zip file with the latest version of the plugin in GitHub.

**Please note!** The numbers (1.0.8) in the file name indicate the plugin version and may differ depending on updates.

<img src="https://support.gcore.com/hc/article_attachments/4407335142673/_____________.png" alt="_____________.png">

Unzip the archive to the Grafana plugin folder. By default, this is the _Grafana\\grafana\\data\\plugins_ installation folder.

[Restart](https://grafana.com/docs/grafana/latest/installation/restart-grafana/) and [log](https://grafana.com/docs/grafana/latest/getting-started/getting-started/#step-2-log-in) in to Grafana.

Click the gear icon in the menu to open the "Configuration" section, select "Data Sources".

<img src="https://support.gcore.com/hc/article_attachments/4407335183377/data_source.png" alt="data_source.png" width="239" height="535">

Click "Add data source" to add a new resource for getting data.

<img src="https://support.gcore.com/hc/article_attachments/4407335221649/_________Data_Source.png" alt="_________Data_Source.png" width="588" height="226">

Find the cdn-stats plugin from Gcore and click "Select".

<img src="https://support.gcore.com/hc/article_attachments/4407335231249/cdn-stats.png" alt="cdn-stats.png" width="654" height="471">

The plugin settings will be opened. Add a permanent API token to the "Auth" section.

You can get a token in your personal account. To do this, go to Profile - > API tokens ->Create. 

<img src="https://support.gcore.com/hc/article_attachments/5084801251089/mceclip0.png" alt="mceclip0.png">

Insert the received API token in the API token field in the format: **APIKey** {the received API token}.

For example: APIKey 7711$eyJ0eXAiOiJKV

<img src="https://support.gcore.com/hc/article_attachments/4407343367825/api_token_1.png" alt="api_token_1.png" width="620" height="365">

Click "Save & Test".

If everything is correct, you will see the following messages: "Datasource updated" and "You successfully authenticated as {Name}".

<img src="https://support.gcore.com/hc/article_attachments/4407343414417/save_test.png" alt="save_test.png" width="629" height="238">

The Download and install the plugin step video instructions
===========================================================

Configure the Dashboard
=======================

Click on the " + " in the menu to open the "Create" section, select "Dashboard" to add a new dashboard.

<img src="https://support.gcore.com/hc/article_attachments/4407343451665/dashboard.png" alt="dashboard.png" width="488" height="419">

In the next window, click "Add an empty panel" to create a new panel.

 <img src="https://support.gcore.com/hc/article_attachments/4407335370897/add_panel.png" alt="add_panel.png" width="562" height="236">

Make sure that "cdn-stats" is set as the data source in the Query section.

<img src="https://support.gcore.com/hc/article_attachments/4407335400849/query.png" alt="query.png" width="566" height="330">

Select the necessary metric, granularity, and grouping (you can select several).

 <img src="https://support.gcore.com/hc/article_attachments/4407343476625/query_props_1.png" alt="query_props_1.png">

The "Legend" field displays the values of the Group by field and the name of the metric by default:

<img src="https://support.gcore.com/hc/article_attachments/4407335444113/grafa.jpg" alt="grafa.jpg" width="304" height="395">

You can customize the output of legend data.

Set a name for the metric and in brackets {{}} set the parameters specified in the Group by field.

For example, for the settings above, you can set the following format: Traffic quantity — {{resource}}.

<img src="https://support.gcore.com/hc/article_attachments/4407335414929/_______________.jpg" alt="_______________.jpg" width="380" height="511">

Open the dashboard settings by clicking on the gear icon in the upper-right corner.

<img src="https://support.gcore.com/hc/article_attachments/4407335500945/panel_settings.png" alt="panel_settings.png" width="393" height="437">

Go to the "Variables" section and click "Add variable". You can use it to filter the data on the chart.

<img src="https://support.gcore.com/hc/article_attachments/4407343597073/add_variable.png" alt="add_variable.png">

For example, to be able to filter resources, you need to make the following settings and click "Update":

*   In the **_Name_** you can specify the variable name (required).
*   In the **_Values for_** you can select a value for the variable: resourceID (resources).
*   In the **_Sort_** you can set the sorting order of the elements (optional)
*   In the **_Selection Options_** you can set the way of how elements can be selected (optional)
    *   In the **_Multi-value_** you can set the ability to select multiple elements.
    *   In the **_Include All option_** you can set the ability to select all elements by marking the All value.

<img src="https://support.gcore.com/hc/article_attachments/4407335683601/variables_edit.png" alt="variables_edit.png" width="655" height="507">

Go back to the dashboard by clicking the arrow icon in the upper-left corner of the screen.

<img src="https://support.gcore.com/hc/article_attachments/4407343815441/go_back.png" alt="go_back.png">

Connect the variable with the Dashboard. To do this, specify its name in the "Resources" field of the "Filters (comma separated)" section.

**Important!** Enter "$" before the variable name.

<img src="https://support.gcore.com/hc/article_attachments/4407343830545/filters.png" alt="filters.png" width="565" height="272">

Now you can choose resource data to be displayed on the chart.

<img src="https://support.gcore.com/hc/article_attachments/4407335732625/pane_____.png" alt="pane_____.png" width="572" height="447">

Save the Dashboard. To do this, click "Save" in the upper-right corner of the panel.  
  
<img src="https://support.gcore.com/hc/article_attachments/4407335808017/save.png" alt="save.png">

Configure the Dashboard step video instructions
===============================================