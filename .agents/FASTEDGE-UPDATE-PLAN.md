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

## App types — architecture reference

Three types of FastEdge applications exist. Documentation must reflect all three.

| Type | Target | SDK | Languages |
|------|--------|-----|-----------|
| Modern HTTP apps | wasm32-wasip2 | wstd (WASI-HTTP) | Rust, JavaScript |
| Legacy HTTP apps | wasm32-wasip1 | fastedge crate (Gcore SDK) | Rust only |
| CDN apps | wasm32-wasip1 | Proxy-Wasm | Rust only |

Legacy HTTP apps represent the majority of existing Rust HTTP apps — document as a first-class path.
Modern HTTP apps are the recommended direction for new apps.
CDN apps are a separate section with their own articles.

## Pattern rules

1. Every article that describes an action performable via both the Customer Portal and the REST API
   must use MethodSwitch: Customer Portal tab first, REST API tab second.
2. Management articles (manage apps, templates, secrets, KV) use Portal | API only —
   no language sub-tabs inside. API calls for management are SDK-agnostic.
3. SDK setup articles live in the "Get started" group. Use-case articles reference them
   instead of repeating setup steps.

---

## Navigation structure (target)

```
FastEdge
  ├── fastedge                          (overview landing)
  ├── Get started  (group)
  │   ├── fastedge/getting-started      (overview — already exists)
  │   ├── setup-rust-modern             (wstd, wasip2)
  │   ├── setup-rust-legacy             (fastedge crate, wasip1)
  │   └── setup-javascript              (@gcoredev/fastedge-sdk-js)
  ├── Create apps  (group)
  │   ├── fastedge/create-apps          (landing)
  │   ├── HTTP Applications  (group)
  │   │   ├── create-fastedge-apps      (Portal + API)
  │   │   ├── built-in-templates
  │   │   ├── get-started-rust          (Modern Rust hello-world, references setup-rust-modern)
  │   │   ├── call-external-api-rust    (Modern Rust use-case)
  │   │   └── get-started-rust-legacy   (Legacy Rust hello-world, references setup-rust-legacy)
  │   └── CDN Applications  (group)
  │       ├── integrate-cdn-with-fastedge
  │       └── cdn-properties
  ├── manage-apps
  ├── create-manage-templates
  ├── Secrets Manager  (group)
  ├── Edge Storage  (group)
  ├── cache
  ├── troubleshooting
  └── fastedge-cli
```

---

## Phase 1 — SDK setup articles (do first)

- [x] `fastedge/getting-started/setup-rust-modern.mdx`
- [x] `fastedge/getting-started/setup-rust-legacy.mdx`
- [x] `fastedge/getting-started/setup-javascript.mdx`
- [x] Update `docs.json`: navigation restructured, groups added

---

## Phase 2 — Use-case articles (after Phase 1)

- [x] `fastedge/getting-started/get-started-http.mdx` (Modern Rust HTTP, Portal + API)
- [x] `fastedge/getting-started/call-external-api-rust.mdx` (Portal + API)
- [x] `fastedge/getting-started/get-started-cdn.mdx` (CDN app, Portal + API)
- [x] `fastedge/getting-started/setup-rust-cdn.mdx` (CDN Rust SDK setup)
- [x] `fastedge/render-markdown.mdx`
- [x] `fastedge/geolocation-redirect.mdx`
- [x] `fastedge/getting-started/cdn-properties.mdx`
- [x] Create-apps landing page removed, replaced by Applications nav group
- [ ] New article: `fastedge/getting-started/get-started-rust-legacy.mdx`
- [ ] New article: `fastedge/getting-started/get-started-js.mdx`

---

## Phase 3 — Management articles (add REST API tab)

- [x] `fastedge/manage-apps.mdx`
- [x] `fastedge/create-manage-templates.mdx`
- [x] `fastedge/built-in-templates.mdx` — split into two focused articles
- [x] `fastedge/kv-stores/manage-kv-store.mdx`
- [x] `fastedge/getting-started/integrate-cdn-with-fastedge.mdx`
- [x] `fastedge/secrets-manager/manage-secrets.mdx`
- [x] `fastedge/kv-stores/sorted-set.mdx`
- [x] `fastedge/kv-stores/bloom-filter.mdx`

---

## Phase 4 — Content review

- [x] `fastedge/secrets-manager/slots.mdx`
- [x] `fastedge/kv-stores/how-it-works.mdx`
- [ ] `fastedge/cache.mdx`
- [ ] `fastedge/fastedge-cli.mdx`
- [ ] `fastedge/troubleshooting.mdx`

---

## Notes

- `fastedge/snippets/fastedge-cdn-integration.mdx` — reusable snippet, review only if referenced articles change.
- Test region: Luxembourg 3 (unless article is region-specific).
- Use Playwright MCP for portal screenshots, follow the `update-page` skill.
