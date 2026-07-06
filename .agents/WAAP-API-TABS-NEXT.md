# WAAP API Tabs — Next Batch

Статьи для добавления REST API вкладок. Продолжение серии `waap-api-guides`.

Ветка предыдущего батча: `waap-api-guides` (в ревью).

---

## Готово (batch 1 — waap-policies)

1. `waap/waap-policies/waf-and-owasp-top-threats.mdx` ✓
2. `waap/waap-policies/behavioral-waf.mdx` ✓
3. `waap/waap-policies/known-bots.mdx` ✓
4. `waap/waap-policies/ip-reputation.mdx` ✓
5. `waap/waap-policies/cms-protection.mdx` ✓
6. `waap/waap-policies/anti-automation-and-bot-protection.mdx` ✓
7. `waap/waap-policies/advanced-api-protection.mdx` ✓
8. `waap/waap-policies/protocol-validation.mdx` ✓

---

## Следующий батч (batch 2)

| # | Файл | Операция | API endpoint |
|---|------|----------|--------------|
| 1 | `waap/response-pages/create-custom-response-pages.mdx` | Создание page sets и страниц | `POST /waap/v1/domains/{id}/custom-page-sets` |
| 2 | `waap/response-pages/manage-custom-response-pages.mdx` | Update/delete page sets, привязка к домену | `PATCH/DELETE /waap/v1/domains/{id}/custom-page-sets/{set_id}` |
| 3 | `waap/api-discovery-and-protection/api-discovery.mdx` | CRUD endpoints, scan settings, Swagger upload | `api-discovery` + `api-paths` endpoints |
| 4 | `waap/api-discovery-and-protection/configure-api-base-path.mdx` | Добавление/удаление endpoints из base path | `api-paths` API |
| 5 | `waap/api-discovery-and-protection/configure-api-access-with-reserved-tags.mdx` | Создание custom rules с API protection tags | `POST /waap/v1/domains/{id}/custom-rules` |
| 6 | `waap/waap-rules/custom-rules/tag-rules/reserved-tags.mdx` | Создание custom rules с reserved tags | `POST /waap/v1/domains/{id}/custom-rules` |
| 7 | `waap/threat-intelligence/security-insights/manage-insights.mdx` | Mark read, silence, close, reopen insights | `insights` + `insight-silences` API |
| 8 | `waap/threat-intelligence/security-insights/manage-silence-rules.mdx` | Edit/delete silence rules | `insight-silences` API |

---

## Пропущено (не подходят)

- `waap/waap-policies/invalid-user-agent-and-unknown-user-agent.mdx` — концептуальная, нет portal-шагов
- 36 статей — аналитика, FAQ, troubleshooting, navigation landings, read-only

---

## Заметки

- Ветку создавать от свежего main: `git checkout main && git pull && git checkout -b waap-api-tabs-batch2`
- `advanced-rules` и `custom-rules` верхнего уровня — справочные, не процедурные; пропускаем
- Security Insights может зависеть от плана — проверить при тестировании
- `api-discovery.mdx` — богатая статья, может потребовать Structure A (sequential)
