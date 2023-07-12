---
title: add-an-origin-group
displayName: Origin group
published: true
order: 60
toc:
   --1--Add and configure: "add-and-configure-the-origins-group"
   --1--If you change the origins group, will the Host header change?: "if-you-change-the-origins-group-will-the-host-header-change"
---
# Add an origin group

## Add and configure the origins group

1\. Add a new origins group. You can do this in two ways: In the CDN resource settings or in the Origins groups section.

**Option 1.** Open the settings of the desired CDN resource, find the Origin pull protocol option, and click **Add group**.

A new origins group will appear. It won’t automatically bind to the CDN resource. To bind a new group, refresh the browser page, click the ᐯ symbol and select the created group from the drop-down list. Next, click **Save changes**.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960872583313.png" alt="" width="80%">
<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960907587345.png" alt="" width="50%">
</media-gallery>

**Option 2.** Open the **Origins groups** section and click **Add origins group**. The created origins group will appear in the general list of origins groups. It won’t automatically bind to the CDN resource. Please do it manually.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960872715793.png" alt="" width="80%">

A pop-up window for group configuration and adding will appear, regardless of which option you choose. Follow the rest of the steps in it.

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960872728337.png" alt="" width="50%">

3\. Enter the origins group name. It’ll appear in the general list of origins groups and the CDN resource settings.

4\. In the Content origin field, enter the origin IP or its domain name without ```http://``` or ```https://```. The CDN will pull content from this source.

Your origin’s domain name can have multiple IP addresses. The CDN will determine the origin IPs as separate sources and distribute requests to them according to the Round-robin algorithm. In other words, the first request will go to the first source, the second request will go to the second source, and so on.

5\. If the origin is on ports other than 80 and 443, disable the **Use default port** button. The ‘port’ field will appear. Type the port on which the origin is responding.

6\. If you want to add additional content sources, click **Add origin**. If you decide to keep only one origin in the group, skip this step.

When you have more than one origin in a group, you can adjust the balance between them. To do so:

- Select which origins to enable and disable
- Select active and backup origins
- Decide whether to enable the Use next upstream option

<img src="https://assets.gcore.pro/docs/cdn/add-an-origin-group/10960907857937.png" alt="" width="80%">

**Enable/disable origin.** By default, the slider next to each origin is in the **On** position. ‘On’ means that the CDN can pull content from this origin: It has been added to the balance.

If you want to disable the content origin in the group, move the slider to **Off**. You’ll only disable the origin in the current group. It’ll continue to work in other groups. CDN requests will stop coming to the disabled origin in 15 minutes.

You can’t disable the last active origin.

**Active/backup origin.** All new origins are automatically assigned an ‘Active’ status. The CDN pulls content from such origins. The balancing between them is run by the Round-robin algorithm. You can turn the _active_ origin into the _backup_ one by selecting the ‘Use origin as a backup’ option. Backup origins are taken out of balance by default. CDN requests content from them only if the active origin gives a 5xx response code.

**Use next upstream.** This option only works if each origin contains the same content. When enabled, the CDN will call the next origins on the list if the previous one is unavailable and responds with any 4xx or 5xx series response code, except 400. Code 400 is an exception. By getting it, the CDN won’t redirect requests to another source. If all origins are unavailable, the CDN will show the response of the last one in the list.

At first glance, the interaction between the active/backup origins and the Use next upstream option may seem complicated, so to make it easier to understand, let’s look at examples of how it works.

- The Use next upstream option is disabled; all origins are active.

If the active origin responds with an error, the CDN will hand it off to the end user.

- The Use next upstream option is enabled. One origin is active, and the rest are backups.

If the active origin responds with 4xx and 5xx response codes, the CDN will start requesting content from the other origins, moving down the list.

- The Use next upstream option is enabled. All origins are active.

If the first active origin responds with 404, 500, 502, 503, or 504 response codes, the CDN will start requesting content from the other origins, moving down the list.

- The Use next upstream option is disabled. One origin is active, and the rest are backups.

If the active origin doesn’t respond within 5 seconds or responds with a 5xx response code, the CDN will request content from the backup origin. If the active origin responds with a 4xx response code, the CDN won’t request the backup origin and will send an error message to the user.

7\. Click **Add group** to save changes.

## If you change the origins group, will the Host header change?

No. If you switch the CDN resource from one origins group to another, the Host header won’t automatically change. You’ll have to do it manually.