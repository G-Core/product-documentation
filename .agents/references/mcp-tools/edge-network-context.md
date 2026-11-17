# Edge network context

Load this file only when a skill tells you to.

Call `edge_network_context-ask_support_query` on the `mcp-gateway` server. In Cursor the namespace is `user-mcp-gateway`. The only argument is `question`. Ask one open fact per call.

Use it when a CDN or edge fact is still open after the check this skill already requires (portal, API, Jira, or Confluence). That is an article under `cdn/`, `dns/`, `streaming/`, or `fastedge/`, or a fact about how CDN behaves with WAAP, DNS, FastEdge, or Streaming.

Ask what the customer sees: what an option does, a limit, an error, or that relationship.

Do not call `edge_network_context-ask_dev_query` or `edge_network_context-ask_ops_query` for article text. Those answers are code and infrastructure.

The reply is an input. Do not paste it into the article. A portal or API observation wins. If the tool says the fact is not in its sources, leave the fact unverified. If the tool is missing, say so and continue with the sources this skill already names. Do not invent the fact.
