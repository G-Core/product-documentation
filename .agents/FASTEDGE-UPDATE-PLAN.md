# FastEdge Documentation Update Plan

Update each article via portal testing (portal + Playwright) in the order listed below.
Mark each article as done when the PR is merged.

> **IMPORTANT:** Delete this file before merging the final PR.
> This is a working document — it must not appear in the published branch.

---

## Status legend

- [ ] Not started
- [x] Done

---

## Already updated

- [x] `fastedge/getting-started/create-fastedge-apps.mdx`
- [x] `fastedge/built-in-templates.mdx` (new article)
- [x] `fastedge/getting-started/build-a-rust-wasi-app.mdx` (new article)
- [x] `fastedge/kv-stores/manage-kv-store.mdx`
- [x] `fastedge/manage-apps.mdx`

---

## To update

### High priority (core user flows)

- [x] `fastedge/getting-started.mdx` — section landing page
- [x] `fastedge/create-apps.mdx` — landing page, rewritten with SDK overview

### Get started articles (new + refactor)

Both articles follow the same structure: toolchain setup → simple example → build → deploy.

- [ ] Refactor `fastedge/getting-started/build-a-rust-wasi-app.mdx`:
  - Rename to `fastedge/getting-started/get-started-rust.mdx` (sidebarTitle: "Get started with Rust")
  - Keep only: toolchain setup + hello-world example + build + deploy
  - Move the "Fetch data from external API" section to a new use-case article
  - Add redirect in `docs.json` from old slug to new
- [ ] New use-case article (location TBD): "Call an external API from a Rust app" — the complex example currently in build-a-rust-wasi-app.mdx
- [ ] New article: `fastedge/getting-started/get-started-js.mdx` (sidebarTitle: "Get started with JavaScript")
  - Same structure as Rust: Node.js v20+, npm install, fastedge-init, simple handler, fastedge-build, deploy
- [ ] Update `docs.json` navigation (HTTP Applications group) for both new articles
- [ ] Update `fastedge/create-apps.mdx` links to point to new get-started articles
- [ ] `fastedge/create-manage-templates.mdx` — template management via portal

### Secrets Manager

- [ ] `fastedge/secrets-manager/manage-secrets.mdx`
- [ ] `fastedge/secrets-manager/slots.mdx`

### KV Stores

- [ ] `fastedge/kv-stores/how-it-works.mdx`
- [ ] `fastedge/kv-stores/bloom-filter.mdx`
- [ ] `fastedge/kv-stores/sorted-set.mdx`

### CDN integration

- [ ] `fastedge/getting-started/cdn-properties.mdx`
- [ ] `fastedge/getting-started/integrate-cdn-with-fastedge.mdx`

### Other

- [ ] `fastedge/cache.mdx`
- [ ] `fastedge/fastedge-cli.mdx`
- [ ] `fastedge/troubleshooting.mdx`

---

## Notes

- `fastedge/snippets/fastedge-cdn-integration.mdx` — reusable snippet, not a standalone article. Review only if referenced articles change.
- Test region: Luxembourg 3 (unless article is region-specific).
- Use Playwright MCP for screenshots, follow the `update-page` skill.
