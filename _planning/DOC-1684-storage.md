# DOC-1684 â€” Object Storage: Article Updates

Branch: `DOC-1684-storage-update`

## Progress legend

| Symbol | Meaning |
|--------|---------|
| [ ] | Not started |
| [~] | In progress |
| [x] | Done |

---

## General state of the section

Unlike the reseller section, Storage articles are mostly in good shape:
- All 15 articles have `ai-navigation` in frontmatter
- All articles use local `/images/docs/` image paths (not old CDN)
- Modern MDX components (`<Note>`, `<Info>`, `<Frame>`) are used in most articles

Issues are more **stylistic and content-level** than structural.

---

## Systematic issues (check in every article touched)

1. **Numbered list formatting** â€” many articles use `1\.` (backslash) instead of `1.`
2. **Bold notes instead of components** â€” `**Note** :` and `**Important note** :` inline in prose instead of `<Note>` component
3. **Code block trailing spaces** â€” closing ` ``` ` followed by a space before line break; should be clean
4. **Old S3 URLs** â€” several articles reference `s-ed1.cloud.gcore.lu`, `s-dt2.cloud.gcore.lu` (old format); new format is `luxembourg-2.storage.gcore.dev` etc. â€” verify which is canonical
5. **Italic variable style** â€” uses `_variable_` markdown italics inside prose; replace with backtick code spans

---

## Article list

### Core articles

| Status | File | Notes |
|--------|------|-------|
| [x] | `storage/create-an-s3-or-sftp-storage.mdx` | Done [DOC-1685](https://jira.gcore.lu/browse/DOC-1685) â€” full regression, 14 findings fixed, screenshots retaken, restructured with Steps and tables
| [x] | `storage/how-storage-is-billed.mdx` | Done [DOC-1686](https://jira.gcore.lu/browse/DOC-1686) â€” 4 regression findings fixed, 5 style fixes, broken link and outdated billing navigation removed |
| [x] | `storage/request-content-directly-from-the-storage.mdx` | Done [DOC-1687](https://jira.gcore.lu/browse/DOC-1687) â€” 2 regression findings (outdated screenshot, SFTP protocol), 6 style fixes |
| [ ] | `storage/use-storage-as-the-origin-for-your-cdn-resource.mdx` | Redo [DOC-1688](https://jira.gcore.lu/browse/DOC-1688) â€” screenshots not retaken (hook was broken); content fixes already committed |
| [ ] | `storage/check-storages-usage-reports.mdx` | Redo [DOC-1689](https://jira.gcore.lu/browse/DOC-1689) â€” screenshot not retaken (hook was broken); content fixes already committed |
| [x] | `storage/4xx-errors-how-to-solve-storage-issues.mdx` | Done [DOC-1690](https://jira.gcore.lu/browse/DOC-1690) â€” 4 regression findings fixed (merged steps, Global 2, endpoint typo, missing Status Page link), content rewrite |

### Manage Object Storage

| Status | File | Notes |
|--------|------|-------|
| [ ] | `storage/manage-object-storage/manage-buckets-via-the-control-panel.mdx` | ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/request-content-directly-from-the-storage.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/s3-service-urls-and-default-region-names.mdx` (DOC-1692) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1692 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/check-storages-usage-reports.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/4xx-errors-how-to-solve-storage-issues.mdx` (DOC-1693) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1693 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/use-storage-as-the-origin-for-your-cdn-resource.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/connect-aws-cli-s3cmd-and-aws-sdk.mdx` (DOC-1694) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1694 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/manage-buckets-via-the-control-panel.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd.mdx` (DOC-1695) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1695 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-sftp-storage/create-and-add-an-ssh-key-to-your-storage.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/generate-temporary-links-to-files-with-aws-cli-and-s3cmd.mdx` (DOC-1696) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1696 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/s3-service-urls-and-default-region-names.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli.mdx` (DOC-1697) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1697 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/4xx-errors-how-to-solve-storage-issues.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-sftp-storage/connect-to-your-storage-with-filezilla.mdx` (DOC-1698) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1698 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/connect-aws-cli-s3cmd-and-aws-sdk.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage.mdx` (DOC-1699) ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md), Ð¿ÐµÑ€ÐµÐ²ÐµÐ´Ð¸ Ñ‚Ð¸ÐºÐµÑ‚ DOC-1699 Ð² In Review. Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/generate-temporary-links-to-files-with-aws-cli-and-s3cmd.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage/manage-sftp-storage/connect-to-your-storage-with-filezilla.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
ÐžÑ‚Ð¼ÐµÑ‚ÑŒ `storage.mdx` ÐºÐ°Ðº done Ð² Ð¿Ð»Ð°Ð½Ðµ (_planning/DOC-1684-storage.md). Ð—Ð°Ñ‚ÐµÐ¼ Ð¿Ñ€Ð¾Ñ‡Ð¸Ñ‚Ð°Ð¹ ÑÐºÐ¸Ð»Ð» (c:\Projects\product-documentation_2\.agents\skills\regression-test\SKILL.md), Ð²Ð¾Ð·ÑŒÐ¼Ð¸ ÑÐ»ÐµÐ´ÑƒÑŽÑ‰ÑƒÑŽ ÑÑ‚Ð°Ñ‚ÑŒÑŽ Ð¸Ð· Ð¿Ð»Ð°Ð½Ð° C:\Projects\product-documentation_2\_planning\DOC-1684-storage.md (## Article list) Ð¸ Ð²Ñ‹Ð¿Ð¾Ð»Ð½Ð¸ Ð¿Ð¾Ð»Ð½Ñ‹Ð¹ Ñ†Ð¸ÐºÐ»: Ñ‚ÐµÑÑ‚Ð¸Ñ€Ð¾Ð²Ð°Ð½Ð¸Ðµ, ÑÐºÑ€Ð¸Ð½ÑˆÐ¾Ñ‚Ñ‹, Ñ„Ð¸ÐºÑÑ‹, ÐºÐ¾Ð¼Ð¼Ð¸Ñ‚. Ð’Ñ…Ð¾Ð´ Ð² Ð¿Ð¾Ñ€Ñ‚Ð°Ð» Ñ‡ÐµÑ€ÐµÐ· C:\Projects\product-documentation_2\access.md â€” Ñ‚Ð¾Ð»ÑŒÐºÐ¾ SSO. Ð ÐµÐ³Ð¸Ð¾Ð½: Luxembourg-3.
 |
| [ ] | `storage/manage-object-storage/s3-service-urls-and-default-region-names.mdx` | Clean table; verify all locations/endpoints are current and complete |

### Configure AWS CLI / S3cmd / SDK

| Status | File | Notes |
|--------|------|-------|
| [ ] | `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/connect-aws-cli-s3cmd-and-aws-sdk.mdx` | AWS JS SDK pinned to old version `2.742.0`; broken link format in HTML example; old S3 URLs; old list style; `_variable_` italics |
| [ ] | `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd.mdx` | `<Info>` block has redundant `**Info**` label inside; `**Note**` inline; old S3 URL |
| [ ] | `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/generate-temporary-links-to-files-with-aws-cli-and-s3cmd.mdx` | **Wrong image path**: uses `manage-s3-storage` instead of `manage-object-storage`; old list style; old hostname `s-dt2.cloud.gcore.lu` |
| [ ] | `storage/manage-object-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli.mdx` | Old list style; old S3 URL; lifecycle UI section references old bucket guide anchor |

### Manage SFTP Storage

| Status | File | Notes |
|--------|------|-------|
| [ ] | `storage/manage-sftp-storage/connect-to-your-storage-with-filezilla.mdx` | Uses "Control Panel" (old term) â€” should be "Customer Portal"; otherwise clean |
| [x] | `storage/manage-sftp-storage/create-and-add-an-ssh-key-to-your-storage.mdx` | Done [DOC-1699](https://jira.gcore.lu/browse/DOC-1699) -- 5 regression findings fixed (navigation path, field label, button name, outdated screenshots, missing step 5), 8 style fixes, 4 new screenshots |

### Overview & landing (do last â€” update after all other articles are done)

> Overview articles must reflect the updated content. Write or revise them only after all substantive articles in the section are finalized.

| Status | File | Notes |
|--------|------|-------|
| [ ] | `storage.mdx` | Landing page; update section descriptions to match updated articles |

---

## Notes

