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

- [ ] `fastedge/getting-started/setup-rust-modern.mdx`
      Modern Rust: prerequisites, rustup target add wasm32-wasip2, Cargo.toml with wstd, verify build
- [ ] `fastedge/getting-started/setup-rust-legacy.mdx`
      Legacy Rust: prerequisites, rustup target add wasm32-wasip1, Cargo.toml with fastedge crate, verify build
- [ ] `fastedge/getting-started/setup-javascript.mdx`
      JavaScript: Node.js v20+, npm install @gcoredev/fastedge-sdk-js, CLI tools overview
- [ ] Update `docs.json`: convert fastedge/getting-started from standalone page to group,
      add all three setup articles

---

## Phase 2 — Use-case articles (after Phase 1)

- [ ] Update `fastedge/getting-started/get-started-rust.mdx`:
      Remove setup steps, replace with link to setup-rust-modern, keep hello-world + deploy
- [ ] Update `fastedge/getting-started/call-external-api-rust.mdx`:
      Remove setup steps, replace with link to setup-rust-modern
- [ ] Add Portal deploy tab to both articles (currently API-only deploy)
- [ ] New article: `fastedge/getting-started/get-started-rust-legacy.mdx`
      Legacy Rust hello-world, references setup-rust-legacy, Portal + API deploy
- [ ] New article: `fastedge/getting-started/get-started-js.mdx`
      JavaScript hello-world, references setup-javascript, Portal + API deploy
- [ ] Revise `fastedge/create-apps.mdx` to reflect all three SDK types

---

## Phase 3 — Management articles (add REST API tab)

- [ ] `fastedge/manage-apps.mdx`
- [ ] `fastedge/create-manage-templates.mdx`
- [ ] `fastedge/built-in-templates.mdx`
- [ ] `fastedge/secrets-manager/manage-secrets.mdx`
- [ ] `fastedge/kv-stores/sorted-set.mdx`
- [ ] `fastedge/kv-stores/bloom-filter.mdx`
- [ ] `fastedge/getting-started/integrate-cdn-with-fastedge.mdx`

---

## Phase 4 — Content review

- [ ] `fastedge/secrets-manager/slots.mdx`
- [ ] `fastedge/kv-stores/how-it-works.mdx`
- [ ] `fastedge/getting-started/cdn-properties.mdx`
- [ ] `fastedge/cache.mdx`
- [ ] `fastedge/fastedge-cli.mdx`
- [ ] `fastedge/troubleshooting.mdx`

---

## Already updated

- [x] `fastedge/getting-started/create-fastedge-apps.mdx` — Portal + API (MethodSwitch)
- [x] `fastedge/kv-stores/manage-kv-store.mdx` — Portal + API (MethodSwitch)
- [x] `fastedge/built-in-templates.mdx`
- [x] `fastedge/manage-apps.mdx`
- [x] `fastedge/getting-started.mdx`
- [x] `fastedge/create-manage-templates.mdx`
- [x] `fastedge/getting-started/get-started-rust.mdx` (Modern Rust, needs Phase 2 update)
- [x] `fastedge/getting-started/call-external-api-rust.mdx` (needs Phase 2 update)

---

## Notes

- `fastedge/snippets/fastedge-cdn-integration.mdx` — reusable snippet, review only if referenced articles change.
- Test region: Luxembourg 3 (unless article is region-specific).
- Use Playwright MCP for portal screenshots, follow the `update-page` skill.
