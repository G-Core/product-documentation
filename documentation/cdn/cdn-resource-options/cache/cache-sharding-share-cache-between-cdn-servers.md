---
title: cache-sharding-share-cache-between-cdn-servers
displayName: Cache Sharding
order: 60
toc:
   --1--Cache Sharding: "what-is-the-cache-sharding-feature"
   --1--How it works: "how-does-the-cache-sharding-feature-work"
   --1--Benefits: "what-are-the-benefits-of-using-cache-sharding"
   --1--How to enable: "how-to-enable-the-cache-sharding-feature"
pageTitle: Understanding of Cache Sharding CDN | Gcore
pageDescription: Uncover the benefits of Cache Sharding in CDN servers—enhanced content storage, reduced origin requests, and improved delivery speed.
---
# Сache Sharding: share cache between CDN servers

## What is the Cache Sharding feature?

Cache Sharding is a feature that allows some CDN servers—grouped together and in the same Point of presence (PoP)—to use one another’s cache to increase the CDN performance. When users request content, a CDN server proxies a request to another server where the cache is located using a consistent hashing algorithm.

This feature is particularly important for websites and applications with a large amount of content stored in the CDN cache and for those where multiple files receive relatively similar numbers of requests, such as e-commerce, video game industry, and VoD streaming.

## How does the Cache Sharding feature work?

In a system without Cache Sharding, a CDN server only checks *its own* cache for a file request. This is inefficient when there are many servers in one PoP: if a server *without* the file gets a request, it retrieves a file from the origin instead of a neighboring server.

When Cache Sharding is enabled for a CDN resource, CDN servers within one PoP (or data center) are clustered to use each others’ cache with the <a href="https://toptal.com/big-data/consistent-hashing#:~:text=according%20to%20Wikipedia).-,Consistent%20Hashing%20is%20a%20distributed%20hashing%20scheme%20that%20operates%20independently,without%20affecting%20the%20overall%20system" target="_blank">consistent hashing algorithm</a>.

Consistent hashing is a method in which data is stored in a hash table using a hash function. The key of each data item is passed through a hash function, which calculates the address in the “hash ring” and determines in which sector of this ring the hash code is. This hash code indicates on which server the data is stored.

**Example**: Assume three CDN servers, A, B, and C, constitute one group. Server A has file X in its cache. When users request X, their request may reach any of the group’s servers (A, B, or C), depending on workload, connectivity, and other factors. If the request hits A, X is served from its cache. 

If the request hits B or C, they calculate a hash code. Based on this, server B or C knows to which server they should send the request in order to serve X from the cache rather than the origin server. Since server A’s cache has the desired file, server B or C will proxy the request, and server A will serve the user file X from its cache.

If the group has no X in its cache, the server that was initially chosen using a consistent hashing algorithm will download file X from the origin and cache it.

If a server fails, it is removed from the group, and the hash will be recalculated to reflect the failed server. Thus, all subsequent requests will be distributed among other servers of the same group. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/cache-sharding-share-cache-between-cdn-servers/cache-sharding-scheme.png" alt="How does the Cache Sharding feature work" width="80%">

## What are the benefits of using Cache Sharding?

Cache Sharding optimizes content storage and distribution. Here are some of its benefits in more detail:

- **More efficient cache use.** Only one copy of a file is needed for all the data center’s servers. This means that each CDN server is used efficiently, rather than being occupied with repeats. 
- **Origin is protected from redundant requests.** CDN servers use the hash key to determine if there is content in the group's cache. The origin is only requested if there is no content cached by the group. This reduces the costs that are incurred when paying for traffic from the CDN servers to the origin. It also lowers the load on the origin server.
- **Improved content delivery speed.** Checking the caches of nearby servers in a group for a file is quicker than routing a request to the origin. This process enhances the “time to first byte” (TTFB,) indicating a more efficient system.

## How to enable the Cache Sharding feature

<a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Newly created CDN resources</a> have Cache Sharding enabled automatically. If you’re a long-term user unsure whether the feature is activated, please contact our [support team](mailto:support@gcore.com) to request activation.

**Note**: The Cache Sharding option is not used for <a href="https://gcore.com/docs/streaming-platform/how-the-streaming-platform-interact-with-the-cdn" target="_blank">Streaming Platform CDN resources</a>.