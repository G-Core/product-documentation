---
title: cdn-timeouts
displayName: Timeouts
published: true
order: 40
toc:
   
pageTitle: Optimize CDN Performance with Gcore Edge Network Timeouts | Gcore 
pageDescription: Maximize efficiency with custom timeouts on Gcore Edge Network's proxied servers.
---
# CDN timeouts

The timeouts set for the servers proxied by the Gcore Edge Network vary from the default values of nginx. The following timeouts are currently in use:

<table>
<thead>
<tr>
<td><b>Directive</b></td>
<td><b>Definition</b></td>
<td><b>Value</b></td>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_read_timeout" target="_blank">proxy_read_timeout</a></td>
<td style="text-align: left">The time limit for receiving a partial response from a proxied server.<br> If no response is received within this time, the connection will be closed. For instructions on how to set up the timeout, check out our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/customize-connection-and-read-timeouts" target="_blank">dedicated guide</a>.</td>
<td>30s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_connect_timeout" target="_blank">proxy_connect_timeout</a></td>
<td style="text-align: left">The time limit for establishing a connection with a proxied server. For instructions on how to set up the timeout, check out our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/customize-connection-and-read-timeouts" target="_blank">dedicated guide</a>.</td>
<td>5s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_send_timeout" target="_blank">proxy_send_timeout</a></td>
<td style="text-align: left">The time limit for sending a request to a proxied server.<br> If no response is received within this time, the connection will be closed.</td>
<td>30s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_core_module.html#client_header_timeout" target="_blank">client_header_timeout</a></td>
<td style="text-align: left">The time limit for a proxy server to read a client request header.<br> If the entire header is not received within this time, the client will receive a 408 (request timeout) error.</td>
<td>10s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_core_module.html#client_body_timeout" target="_blank">client_body_timeout</a></td>
<td style="text-align: left">The time limit for a proxy server to read a client request body.<br> If no data is sent within this time, the client will receive a 408 (Request Time-out) error.</td>
<td>30s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_core_module.html#resolver_timeout" target="_blank">resolver_timeout</a></td>
<td style="text-align: left">The time limit for resolving a name.</td>
<td>5s</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_session_timeout" target="_blank">ssl_session_timeout</a></td>
<td style="text-align: left">The duration for which the client can reuse session parameters.</td>
<td>2h</td>
</tr>
<tr>
<td><a href="https://nginx.org/en/docs/http/ngx_http_v2_module.html#http2_idle_timeout" target="_blank">http2_idle_timeout</a></td>
<td style="text-align: left">The inactivity period after which the connection will be closed.</td>
<td>15s</td>
</tr>
</tbody>
</table>

The timeouts can be changed via [technical support](mailto:support@gcore.com) if you have an enterprise plan.
