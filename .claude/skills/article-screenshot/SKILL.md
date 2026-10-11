---
name: article-screenshot
description: >-
  Captures one Customer Portal screenshot for a documentation step and crops it to
  the area the step describes, then checks the result. Use when a skill or the user
  needs a new or replacement article screenshot, for example while auditing an
  article, updating a renamed UI, or writing a new article. Chooses the area by
  context (a control, a form, a dialog, a table with its toolbar, a sidebar or side
  panel) instead of the narrowest element, never changes the viewport or zoom, and
  keeps the full screenshot when a crop cannot be verified. Does not edit article
  text.
---

Take a screenshot that shows what one step of an article describes, and nothing that distracts from it.

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| The step text the screenshot illustrates | Yes | The sentence or sentences next to the `<Frame>` |
| Target path | Yes | For example `images/docs/{product}/{slug}/{slug}-image3.png` |
| Portal page already open and in the right state | Yes | Logged in by the user, correct region, resource names `my-*-1` |

## Rules that never change

- Never change the viewport, window size, or zoom.
- Never pass `element` or `target` to `browser_take_screenshot`: it crops by one element and loses the original. Crop afterwards.
- Replace real data with placeholders on the page before the first capture (step 2). Cropping is framing, not protection: the temporary full screenshot must already be clean, because it is the fallback.
- Light mode, English (US). No cursor and no selected text in the image.
- Resource names follow `my-*-1` (`my-instance-1`, `my-network-1`). Never `test-*`, `docs-*`, `regression-*`, Jira IDs, or article slugs.

## Choose the area

**One rule: show what the step is talking about at this moment.** If the step text mentions something, it must be in the frame. If the text does not mention it, leave it out. This applies to every part of the portal, including the sidebar and any side panel.

Choose the smallest functional block that contains everything the step names, plus the context a reader needs to recognise the screen. A single field is almost never enough on its own.

| The step is about | Area to show | Example in this repo |
|---|---|---|
| One control only (a field, toggle, or button) | The control with its label, and the helper text under it when that text explains the choice | `cdn/add-an-origin-group/origin-group-name.png` |
| Several fields, or a section of a form | The whole form card or section, from its first to its last named field, with headings and helper text | `cdn/add-an-origin-group/multiple-origins.png` |
| A dialog or modal | The whole dialog | |
| A list or table page | Page title, the action button, the filters, the table header, and the rows the step discusses | `cdn/add-an-origin-group/origin-groups-page.png` |
| A navigation step ("Navigate to Product > Section"), or any step that names a sidebar item | The sidebar with the named items visible, and the page it opens when the step describes both. See "The sidebar" below | |
| Tabs inside the current page ("on the Settings tab") | The tab strip that holds the named tab, with the area the step then describes | |
| A control that lives in, or is driven by, a side or details panel | The control together with that panel | |
| The result of an action (message, status, new resource) | The element showing the result together with its row or card | |
| A page-level step ("the page opens") or an area that is most of the page | The full viewport, no crop | |

Leave out the portal top bar and the account menu.

**The sidebar.** The portal sidebar is very large, and a customer can get lost in it. The one rule above decides when it appears:
- The step mentions a sidebar item or a navigation path (product, section, subsection): the sidebar is in the frame with every named item visible. Scroll the sidebar if needed so all named items are in the frame.
- The step does not mention the sidebar: it is not in the frame. The customer already knows where they are, so show only the area the step is about.
- Never collapse or change the sidebar to make room. Choose what to include by cropping, not by changing the page.

**Context test:** looking only at the image, could a reader find the described control in the real portal? If the image shows only the control and nothing that identifies the screen (a heading, a section label, neighbouring controls), widen the area.

## Procedure

1. Scroll so every part of the area is fully visible. Scrolling is allowed. Wait for rendering to finish.
2. **Replace real data with placeholders in the page.** Do it before any capture, and run it again after any navigation or re-render, because the page can bring the real values back.

   **Build every placeholder from the real value as it is displayed on the page.** Keep its shape: the same length, the same separators and prefix, digits stay digits, letters stay letters. A 7-digit ID becomes another 7-digit ID, a token shaped like `12345$` followed by hex keeps that shape, a UUID stays a valid UUID. A placeholder that looks different from the real value makes the screenshot look fake. Rules:

   - The same real value gets the same placeholder everywhere in one article. Different real values get different placeholders, so rows of a table stay distinguishable.
   - Placeholders follow the reserved documentation ranges, so they cannot collide with real data: emails and hostnames use `example.com` (RFC 2606); public IPv4 addresses use `203.0.113.0/24` (RFC 5737, also `192.0.2.0/24` and `198.51.100.0/24`); IPv6 uses `2001:db8::/32` (RFC 3849) or `3fff::/20` (RFC 9637).
   - Private addresses (10.x, 172.16-31.x, 192.168.x) and addresses already in a documentation range stay as they are. They identify nobody.

   | Real data | Placeholder |
   |---|---|
   | Email address | `user@example.com`, then `user2@example.com` |
   | Hostname, URL | same subdomains, registered part replaced: `cdn.resource1.example.com` |
   | Public IPv4 | `203.0.113.10`, then `.11`, `.12` |
   | IPv6 | `2001:db8::1`, then `::2` |
   | Token, key, secret | the same shape, built from the real one (`12345$` + hex stays `12345$` + hex) |
   | Numeric ID (project, account, resource) | the same number of digits: `1234567` for a 7-digit ID, `2345678` for the next |
   | UUID | the same shape, still valid hex |
   | Person or account name | `my-account`, then `my-account-2` |

   First run the generic pass (`browser_evaluate`). It recognises emails, UUIDs, tokens, and public IPv4 addresses in page text and in input values:
   ```javascript
   () => {
     const store = (window.__fakes = window.__fakes || new Map());
     const count = re => [...store.values()].filter(v => re.test(v)).length;
     const shape = (real, n) => {
       let d = n, l = n;
       return real.replace(/[0-9a-zA-Z]/g, c =>
         /[0-9]/.test(c) ? String(d++ % 9 + 1) : /[a-z]/.test(c) ? 'abcdef'[l++ % 6] : 'ABCDEF'[l++ % 6]);
     };
     window.__fakes = store; window.__shape = shape; window.__count = count;
     const isFake = v => [...store.values()].includes(v);
     const isSafeIp = ip => /^(10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|192\.0\.2\.|198\.51\.100\.|203\.0\.113\.)/.test(ip);
     const fakeFor = (real, make) => {
       if (isFake(real)) return real;
       if (!store.has(real)) store.set(real, make(store.size));
       return store.get(real);
     };
     const rules = [
       [/[A-Za-z0-9._%+-]+@(?!example\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g, m => fakeFor(m, () => { const k = count(/@example\.com$/); return k ? `user${k + 1}@example.com` : 'user@example.com'; })],
       [/\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/gi, m => fakeFor(m, n => shape(m, n))],
       [/\b\d+\$[0-9A-Za-z]{16,}\b/g, m => fakeFor(m, n => shape(m, n))],
       [/\b[A-Za-z0-9_-]{40,}\b/g, m => fakeFor(m, n => shape(m, n))],
       [/\b(?:\d{1,3}\.){3}\d{1,3}\b/g, m => isSafeIp(m) ? m : fakeFor(m, () => `203.0.113.${10 + count(/^203\.0\.113\./)}`)],
     ];
     const fake = s => rules.reduce((text, [re, make]) => text.replace(re, make), s);
     const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
     let node, changed = 0;
     while ((node = walker.nextNode())) {
       const value = fake(node.nodeValue);
       if (value !== node.nodeValue) { node.nodeValue = value; changed++; }
     }
     document.querySelectorAll('input, textarea').forEach(el => {
       const value = fake(el.value);
       if (value !== el.value) { el.value = value; changed++; }
     });
     return changed;
   }
   ```
   Then replace what the generic pass cannot recognise: numeric IDs, account and user names, hostnames, IPv6. Read them from the snapshot and list each real value with its kind (`id`, `name`, `host`, `ip6`). The real values exist only inside this browser call. Never write one into the skill, the article, or the report.
   ```javascript
   () => {
     const store = window.__fakes, shape = window.__shape, count = window.__count;
     const items = [['{real value}', 'id'], ['{real account name}', 'name'], ['{real hostname}', 'host']];
     const make = (real, kind) =>
       kind === 'id' ? shape(real, store.size)
       : kind === 'name' ? (count(/^my-account/) ? `my-account-${count(/^my-account/) + 1}` : 'my-account')
       : kind === 'host' ? (real.split('.').length > 2 ? real.split('.').slice(0, -2).join('.') + '.example.com' : 'example.com')
       : `2001:db8::${(count(/^2001:db8::/) + 1).toString(16)}`;
     const fakes = new Map(items.map(([real, kind]) => {
       if (!store.has(real)) store.set(real, make(real, kind));
       return [real, store.get(real)];
     }));
     const apply = s => { for (const [real, fake] of fakes) s = s.split(real).join(fake); return s; };
     const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
     let node;
     while ((node = walker.nextNode())) node.nodeValue = apply(node.nodeValue);
     document.querySelectorAll('input, textarea').forEach(el => { el.value = apply(el.value); });
     return [...fakes.values()];
   }
   ```
   Then scan for anything that still looks like real data. The result must be an empty array. Numeric IDs and names have no pattern, so the scan cannot find them: the visual check in step 7 covers them. A hit on a long word or URL that is not secret is a false positive: check it and leave it.
   ```javascript
   () => {
     const fakes = new Set(window.__fakes ? window.__fakes.values() : []);
     const isSafeIp = ip => /^(10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.|192\.0\.2\.|198\.51\.100\.|203\.0\.113\.)/.test(ip);
     const found = document.body.innerText.match(
       /[A-Za-z0-9._%+-]+@(?!example\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}|\b(?:\d{1,3}\.){3}\d{1,3}\b|\b[A-Za-z0-9_-]{40,}\b|\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/gi
     ) || [];
     return found.filter(v => !fakes.has(v) && !isSafeIp(v));
   }
   ```
   Elements that only show the account (the avatar menu, the user block in the header) can be hidden with `visibility: hidden` instead of replaced. Use `visibility`, not `display: none`, so the layout does not shift.

3. Take the full-viewport screenshot: `browser_take_screenshot(scale="css")`. Use the path printed in the tool result.
4. Immediately take `browser_snapshot(boxes=true)`, with no interaction in between. Each element has `[box=x,y,width,height]` in CSS pixels relative to the viewport.
5. Pick the boxes by the table above. For a whole form, dialog, or card use the box of that container. For a control plus a side panel, pass one box for each. Several `--box` values are combined into one area.
6. Crop from the full screenshot:
   ```powershell
   python .agents/tools/crop_screenshot.py {full.png} {target-path} --box x,y,w,h [--box x,y,w,h ...] --pad 12
   ```
   Padding is 8–16 px and must stay below half the gap to the neighbouring element. The tool never modifies the input and warns when a box reaches outside the screenshot, when the crop is very small, or when it covers almost the whole screenshot.
7. **Look at the result** (open the image file) and check every item:
   - the area chosen by the table is fully visible
   - the context test passes
   - no text or control is cut in half at the edges. If a neighbouring element is partly cut, reduce `--pad` or use the parent container
   - no large empty margins
   - no real data: every email, ID, token, address, and name is a placeholder, and each keeps the shape of the real value
   - nothing from another state (an open dropdown, a tooltip, a different dialog)
8. If a check fails, change the boxes or the padding and crop again from the same full screenshot. Up to three attempts.
9. If the crop still fails, put the full-viewport screenshot at the target path instead (`Copy-Item {full.png} {target-path} -Force`) and say so in the report, so the user can crop it by hand.
10. Delete the temporary full screenshot. Only the final image stays in `images/docs/`.

## Report

```
Screenshot: {target-path}
Step: {the step text, shortened}
Area: {what was chosen and why, one line}
Boxes: {the --box values}
Checks: passed / full viewport kept because {reason}
```

Do not commit. Updating the `<Frame>` and the alt text in the article is the calling skill's job.
