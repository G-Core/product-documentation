# WAAP Cookbook — Full Topic List (confirmed)

Все топики проверены против реальных статей продукта.
Подготовлено для обсуждения с командой WAAP.

---

## WAAP only — 11 topics

---

### 1. Block traffic from specific countries

Блокировка трафика из нежелательных стран или регионов. Самый простой сценарий —
настраивается в Customer Portal без технических знаний, без API.

**Gcore features:** WAAP → Custom Rules → Country condition → Block action

---

### 2. Allow traffic from specific countries only, block everything else

Разрешить трафик только из нужных стран (например, только RU + KZ + BY), всё остальное
заблокировать. Используется для сервисов с региональной аудиторией или compliance-требованиями.

**Gcore features:** WAAP → Custom Rules → Country condition + Action priority (Allow > Block)

**Замечание:** требует уточнения по NOT-оператору в custom rules — лучше верифицировать
с разработчиками перед публикацией.

---

### 3. Allow search engine bots and block bad bots

Разрешить Googlebot, Bingbot, SEO-инструменты, платёжные системы (PayPal IPN).
Заблокировать scrapers, headless browsers и неизвестную автоматизацию.
Классическая проблема: включил защиту от ботов — Google перестал индексировать сайт,
заметили через месяц.

**Gcore features:** WAAP → Bot Management → Known Bots (Allow mode) + Anti-automation policy

**Ограничение:** добавить новый бот в Known Bots — только через support. IP-верификации
Googlebot нет (User-Agent spoofable). Надо упомянуть.

---

### 4. Challenge bad bots with CAPTCHA or JavaScript challenge

Вместо жёсткой блокировки подозрительного трафика — проверить через CAPTCHA или
JavaScript challenge. Снижает false positives, продолжает защищать от ботов.
Подходит для публичных сайтов с широкой аудиторией.

**Gcore features:** WAAP → Bot Management + Custom Rules → CAPTCHA / JS Challenge action

---

### 5. Protect admin and high-privilege paths by IP

Закрыть `/admin`, `/wp-admin`, `/dashboard`, `/api/internal` для всех кроме
известных IP-адресов офиса, сотрудников или партнёров. Без VPN, без дополнительного
ПО — только правило в портале.

**Gcore features:** WAAP → Custom Rules → URL condition + IP condition → Allow + Block
(приоритет Allow > Block гарантирует корректную работу)

---

### 6. Geo-block with exceptions for traveling employees and office VPN

Заблокировать страну, но пропустить конкретные IP — для сотрудников в командировке
или корпоративного VPN. Самый частый вопрос на форумах по гео-блокировке:
"как заблокировать Китай, но разрешить нашему сотруднику в Шанхае?"

**Gcore features:** WAAP → Custom Rules → Country condition (Block) + IP Allowlist (Allow exception)

**Ограничение:** нет CIDR/subnet в IP Allowlist и custom rules, максимум 30 сетей на range.

---

### 7. Require specific HTTP headers for API access

Проверять наличие кастомного заголовка (`X-API-Key`, `Authorization`, `X-Internal-Token`)
в каждом запросе к API или внутреннему endpoint. Запросы без заголовка — блокировать.
Простой способ закрыть API без OAuth и сложной аутентификации.

**Gcore features:** WAAP → Custom Rules → Header / Header exists condition → Block action

---

### 8. Protect login pages from bots and automated attacks

Защита `/login`, `/wp-login.php`, `/xmlrpc.php` от automated attacks и ботов.
Важно: это поведенческая защита через bot detection + Login Page tag, а не
rate limiting по счётчику попыток (у нас минимум 21 запроса на окно —
слишком высокий порог для классического "block after 5 failed attempts").

**Gcore features:** WAAP → Bot Management (Anti-automation + Behavioral WAF) +
Custom Rules → Reserved tag "Login Page" + CMS Protection policy (для WordPress)

---

### 9. Allowlist CI/CD pipelines, monitoring tools, and partner integrations

Разрешить GitHub Actions, Datadog, UptimeRobot, партнёрские интеграции не блокироваться
WAF-ом. Через IP Allowlist для статичных IP или через Header-based правило для
инструментов с динамическими IP.

**Gcore features:** WAAP → Firewall → IP Allowlist + Custom Rules → Header condition → Allow +
Reserved tag "Ignored Automation" (только для освобождения от bot protection policies)

**Предупреждение:** IP Allowlist делает полный bypass всех проверок — только для
доверенных статичных IP. Header-based Allow — более безопасный вариант.

---

### 10. Rate limit REST API endpoints

Ограничить количество запросов к конкретным API endpoints по IP или по всему кластеру.
Разные лимиты для разных путей: `/api/search` vs `/api/export` vs `/api/healthcheck`.
Настраивается через WAAP API, не через Customer Portal.

**Gcore features:** WAAP → Advanced Rules → Rate limiting (request.limit_rate) via API

**Ограничение:** минимум 21 запроса на окно (для API — не критично). Только через API,
не через портал. Статья должна содержать готовые примеры кода.

---

### 11. Prevent content scraping

Защита контента сайта от парсеров, price scrapers, автоматического скачивания данных.
Востребовано для медиа, e-commerce, SaaS с платным контентом.

**Gcore features:** WAAP → Bot Management → Anti-scraping policy +
Advanced Rate limiting → URL pattern-based limits

---

## Cross-product — 4 topics

Сценарии, где WAAP используется совместно с другими продуктами Gcore.
Требуют согласования с командами CDN, Cloud и DDoS перед написанием.

---

### 12. Protect your origin server: WAAP + CDN

**Проблема:** если злоумышленник знает IP origin-сервера — он может атаковать его
напрямую, минуя WAF. Классическая ошибка при онбординге.

**Решение:** весь трафик идёт через Gcore CDN → WAAP → origin. На origin (Cloud VM или
dedicated) настраивается firewall allowlist только для Gcore WAAP/CDN IP-диапазонов.

**Gcore features:** CDN + WAAP + Cloud (Gcore VM security groups / firewall)

---

### 13. Layered DDoS defense: WAAP + L4 DDoS Protection

**Проблема:** volumetric атаки (network floods) и application-layer атаки (HTTP floods,
slow POST) — разные угрозы, требуют разных инструментов.

**Решение:** L3/L4 DDoS Protection отражает volumetric на сетевом уровне.
WAAP защищает application layer (L7). Вместе — полный стек защиты.

**Gcore features:** DDoS Protection (L3/L4) + WAAP (L7 DDoS mode + behavioral WAF)

---

### 14. Protect a Gcore Cloud-hosted application end-to-end

**Проблема:** развернул приложение на Gcore Cloud VM — как правильно поставить
WAAP перед ним и убедиться, что origin недоступен напрямую?

**Решение:** полный walkthrough: Cloud VM → WAAP domain setup → allowlist WAAP IPs
на VM security group → проверка что прямой доступ к VM заблокирован.

**Gcore features:** Gcore Cloud (VM + security groups) + WAAP

---

### 15. High availability with DNS failover and WAAP

**Проблема:** если primary origin падает и DNS переключает на backup — сохраняется ли
WAAP-защита? Как настроить failover так, чтобы security posture не нарушалась?

**Gcore features:** Gcore Managed DNS (healthcheck + failover) + WAAP

**Замечание:** требует проверки с командами DNS и WAAP — как именно WAAP обрабатывает
смену origin при DNS failover.

---

## Summary

| # | Topic | Services | Готовность |
|---|-------|----------|------------|
| 1 | Block traffic from specific countries | WAAP | Писать |
| 2 | Allow only specific countries | WAAP | Верифицировать NOT-оператор |
| 3 | Allow search engine bots, block bad bots | WAAP | Писать |
| 4 | Challenge bad bots with CAPTCHA / JS | WAAP | Писать |
| 5 | Protect admin paths by IP | WAAP | Писать |
| 6 | Geo-block with IP exceptions | WAAP | Писать |
| 7 | Require HTTP headers for API access | WAAP | Писать |
| 8 | Protect login pages from bots | WAAP | Писать (с уточнением про behavioral vs rate limit) |
| 9 | Allowlist CI/CD and monitoring tools | WAAP | Писать с предупреждением про full bypass |
| 10 | Rate limit REST API endpoints | WAAP | Писать (developer audience, API-only) |
| 11 | Prevent content scraping | WAAP | Писать |
| 12 | Protect origin server | CDN + WAAP + Cloud | Согласовать с CDN/Cloud |
| 13 | Layered DDoS defense | DDoS Protection + WAAP | Согласовать с DDoS team |
| 14 | Protect Gcore Cloud-hosted app | Cloud + WAAP | Согласовать с Cloud |
| 15 | HA with DNS failover and WAAP | DNS + WAAP | Проверить поведение WAAP при failover |
