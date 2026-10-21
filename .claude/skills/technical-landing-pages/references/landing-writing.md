# Writing landing text

Load this file when writing or rewriting the text of a landing page, after the design is approved. It covers cards, leads, lists, links, and titles.

It applies to landing pages only. `intro-writing.md` and `docs-styleguide-anti-reference.md` are written for how-to articles and tab intros. Do not load them for a landing.

## Reader

A mid-level reader. They know what a CDN, an origin, a cache, or HTTPS is. They do not know what Gcore calls things or which feature does what. Say what the reader can do or gets first, then name the Gcore term.

Test for every card: could someone who has only heard of the product explain why they would open this link?

## Voice

- Start with the action or the result. An imperative is fine: "Enable HTTPS for visitors by adding an SSL certificate", "Make images load faster with Image Stack".
- "You" and "your" are allowed on a landing in small doses. At most one per card or lead, never in two adjacent sentences, only for something the reader does ("You can also select..."), and never in the opening paragraph. Elsewhere write neutrally. They freshen a line; they must not become the voice of the page. The style checker flags every "you", so show those flags to the user.
- "For example," may start a sentence that gives an example. The style checker flags it too. Show the flag to the user.
- A sentence that starts with "Use" must still state a fact beyond the link: "Use Rules to control how specific files are delivered" is fine, "Use the Rules article" is not.

## Cards

- One subject per card. If two features have no shared task, make two cards. Do not join them under a name that fits neither.
- A card exists when a neighbor is easy to confuse with it, or when it is a separate entry point. Otherwise it is a line in a list. The number of cards is a result, not a target.
- The sentences in a card form one thread. Give them a shared object ("the cache lifetime", then "enter earlier", "leave earlier"), parallel parts inside one sentence, or an example. Two true facts placed side by side do not work.
- Do not link sentences with contrast ("but not", "while") and do not repeat the same verb in adjacent sentences ("settings apply... rules apply...").
- Use a concrete example when the point of a feature is not obvious. "For example, images can be cached longer than HTML pages."
- Leave out what the child article owns: requirements, paid or plan notes, approvals, limits, legacy options, causes of failures, lists of attributes. A landing that warns first loses the reader.
- Do not repeat a boundary with another product if the destination page already states it. Check that the destination states it near the top. Add it there if it does not.
- A grid has no orphan card. Make a card wide only when its role is broader than its neighbors, not for symmetry.

## Links

- Put the link on the phrase that carries the meaning, inside a sentence that states a fact. Never "covers", "leads to", "see", "read".
- Use the name from the interface as link text ("origin pull protocol"), joined with `&nbsp;`.
- One link per destination per page.
- A card with links inside has no `href`. Give a card an `href` only when it has a single destination.
- Several links in one card are justified only when the card is about the difference between those destinations.

## Titles and leads

- Card titles are one to three words: the purpose or the interface term ("Per-file settings", "Secure connections"). Two neighbors do not carry the same meaning.
- Group cards under a heading by the reader's task. The lead under a heading names the task and does not list the names below it ("Monitor CDN performance, analyze traffic, and investigate individual requests using reports and logs").
- A group whose items share no task gets no lead. A heading without a lead is allowed there.
- The page `title` and `sidebarTitle` are both `Overview`.

## Accuracy

- Do not state behavior unconditionally if the child article conditions it. "Cached files stay on the CDN" and not "the CDN keeps each file".
- Do not write a claim that rests on one source, or that two child articles contradict. Leave it out and list it as a gap.
- Describe a feature in the words of its own article. Do not paraphrase a protection or a security feature more strongly.

## Calibration

The CDN landing. The earlier version of each card is on the left, the version that worked is on the right. They show a direction. Do not copy the sentences.

| Card | Before | After |
|------|--------|-------|
| Origins | An origin group defines where the CDN fetches content from. Origin Shielding adds a cache layer in front of the origin, so the origin receives fewer requests. | An origin group points the CDN at the server, bucket, or FastEdge HTTP application that holds the files, and can combine several origins. To reduce the load on that origin, Origin Shielding adds a cache layer in front of it. |
| Cache | Three separate facts about cache lifetime, Purge, and Prefetch. | Cached files stay on the CDN for the cache lifetime. A file can enter the cache earlier with Prefetch, which loads it before the first request, and leave earlier with Purge, which removes it before that lifetime ends. |
| Secure connections | HTTPS applies to two connections: between viewers and the CDN, where... and between the CDN and the origin, where... | Enable HTTPS for visitors by adding an SSL certificate. You can also select the origin pull protocol the CDN uses to connect to your server over HTTP or HTTPS. |
| Access and security | Access policies restrict requests by country, referrer, IP address, or user agent, and secure token makes links expire. WAAP inspects HTTP traffic... | Access policies and secure token decide who can request files, and WAAP can block malicious HTTP requests before they reach the origin. |
| Per-file settings | Rules and Image Stack in one card named "Rules and optimization". | Two cards. Rules: "Use Rules to control how specific files are delivered. For example, images can be cached longer than HTML pages." |
| Video delivery | Prepared HLS, DASH... delivered without transcoding, after a paid plan and, for some formats, approval. A raw RTMP or SRT stream that needs transcoding goes to Gcore Video Streaming. | Video CDN delivers video that is already prepared for playback, in HLS, DASH, HTTP-FLV, or MP4. The requirements and the boundary with Video Streaming moved to the Video CDN overview. |

## Checks before showing the page

1. Read each card as a newcomer to the product. Can they say why they would open the link?
2. After each sentence ask: why is the next sentence here? If the answer is only "another fact about the same thing", connect or split.
3. Remove every requirement, plan note, and limit. Does the card still send the reader to the right place? If yes, it stays removed.
