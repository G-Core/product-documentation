---
title: traceparent-header-for-troubleshooting
displayName: Traceparent 
published: true
order: 6
toc:
   --1--Overview: "overview"
   --1--How it works: "how-it-works"
   --2--Request header: "request-header"
   --2--Response header: "response-header"
   --1--Raw logs: "traceparent-in-raw-logs"
pageTitle: Discover Traceparent HTTP Header for Efficient Request Tracing | Gcore
pageDescription: Explore how the traceparent HTTP header aids in request identification, troubleshooting and offers improved service communication.
---
# Traceparent header for troubleshooting

## Overview

We have initiated support for the traceparent HTTP header, as outlined in the <a href="https://www.w3.org/TR/trace-context/" target="_blank">W3C Trace Context specification</a>. This move is aimed at standardizing the methods of transmitting and modifying tracing information between services.

>**Note:** Currently, we don't support the *tracestate* request header, which is also part of the same specification. For now, it's simply passed on.

## How it works

### Request header

The <a href="https://www.w3.org/TR/trace-context/#traceparent-header" target="_blank">traceparent</a> header comprises four fields: version, trace-id, parent-id, and trace-flags. They are detailed in <a href="https://www.w3.org/TR/trace-context/#bib-rfc5234" target="_blank">Augmented Backus-Naur Form (ABNF) notation</a> and are designed to identify the incoming request in a tracing system.

We accept client-passed traceparent request headers. Within the Gcore Edge Network, only the *parent-id* field can be modified, while the *trace-id* remains constant. Thus, you can freely pass the traceparent header from your origin without worrying about losing the route as it traverses through the CDN.

If the traceparent request header isn't utilized on your end, we will generate it following the specification.

### Response header

The traceparent response header is always included in the set of headers for requests processed through our network. You can locate the value using browser debug tools (e.g., Chrome DevTools) or curl.

<media-gallery>

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/traceparent-header-for-troubleshooting/traceparent-devtools.png" alt="Where to view traceparent header in Google Chrome" width="80%">

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/traceparent-header-for-troubleshooting/traceparent-curl.png" alt="How to view traceparent header in console" width="80%">

</media-gallery>

You can use the traceparent response header to track the request or send it to [technical support](mailto:support@gcore.com) for troubleshooting. 

## Traceparent in Raw logs 

We have extended the support for the traceparent header to the <a href="" target="_blank">Raw logs</a> feature (field *$http_traceparent*), for example:

```
00-d5fe1dc9035165ce36952daf29686b6c-14330be33197dd1a-01
```

In this case:

- ```d5fe1dc9035165ce36952daf29686b6c``` represents the 16-byte array (trace-id)
- ```14330be33197dd1a``` denotes the 8-byte array (parent-id)