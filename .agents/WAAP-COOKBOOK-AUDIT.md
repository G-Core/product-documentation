# WAAP Cookbook — Audit of Feasibility

Что реально поддерживается, что ограничено, что надо проверить дополнительно.
Основано на чтении реальных статей продукта.

---

## Topic 1: Protect login endpoints from brute force

### Что работает
- Reserved tag "Login Page" — можно отметить /login как login page, WAAP усиливает
  поведенческую защиту на этом endpoint
- Anti-automation bot protection — блокирует headless browsers и скрипты
- CMS protection policy — покрывает WordPress специфику (wp-login, xmlrpc)

### Критическое ограничение
- Advanced rate limiting — минимум 21 запрос на окно. Стандартный защитный порог
  для логина — 5-10 неудачных попыток в минуту. Это не работает на нашем rate limiting.
  Кроме того, advanced rate limiting настраивается ТОЛЬКО через API, не через портал.

### Вывод
**Частично можно.** Bot protection + Login Page tag + CMS policy дают реальную защиту
от ботов и automated attacks. Но тонкой rate limiting защиты типа "block after 5 failed
logins per minute per IP" — нет. Если об этом написать, надо честно обозначить что мы
защищаем иначе (behavioral), а не через счетчик попыток.

---

## Topic 2: Reduce false positives without disabling protection

### Что работает
- Events + Reference ID: клиент может найти заблокированный запрос по ID из блок-страницы
- Custom rule Allow action: Allow имеет наивысший приоритет над Block/CAPTCHA/Challenge,
  можно создать точечное исключение по IP, URL, Header, User-Agent, Country
- IP Allowlist: быстрое "разблокировать" для конкретного IP

### Критическое ограничение
- Silence Rules — только для уведомлений двух типов (Attack on disabled policy,
  Allowed high-risk IP). Это НЕ инструмент для управления false positives WAF-правил.
  Пользователи, которые ищут "observe mode" / "count mode" / "monitor before block" —
  этого у нас нет.
- Нет аналога "set rule to LOG only" — нельзя перевести конкретное WAF policy в режим
  наблюдения без отключения.

### Вывод
**Можно, но это ручной процесс.** Статья реально поможет: покажет как найти событие,
прочитать Reference ID, создать точечный Allow. Это решает проблему, но честно — менее
удобно чем у конкурентов. Писать можно, но без обещания "log mode".

---

## Topic 3: Allow Googlebot and SEO crawlers, block bad bots

### Что работает
- Known Bots: Google, Bing, Slack, Facebook, Twitter и SEO/monitoring tools уже в списке.
  Настройка через портал — переключить в Allow.
- Anti-automation и Anti-scraping policies: блокируют неизвестную автоматизацию
- "Ignored Automation" reserved tag: позволяет добавить кастомный бот через User-Agent
  custom rule + тег, который освобождает его от bot protection policies

### Критическое ограничение
- Known Bots список управляется Gcore, добавить новый бот — только через support.
- Нет IP-based верификации для Googlebot (как у Cloudflare). User-Agent — spoofable.
  WAAP не делает reverse DNS lookup для подтверждения что Googlebot настоящий.
- "Ignored Automation" tag освобождает только от anti-automation policies, не от всех
  WAF правил.

### Вывод
**Можно для стандартных случаев.** Статья про "включить Known Bots для Googlebot,
включить anti-automation, добавить кастомный бот через Ignored Automation" — реальная
и полезная. Ограничение по кастомным ботам надо честно указать.

---

## Topic 4: Rate limit REST API endpoints

### Что работает
- Advanced rate limiting поддерживает: URL (regex), method_list, scope (IP или cluster),
  status_list, tag — всё что нужно для точечного API rate limiting
- Можно сделать разные лимиты для разных endpoints через разные правила
- Scope=IP защищает от individual attacker, scope=cluster от DDoS на origin

### Критические ограничения
- Минимум 21 запроса на окно. Для API это менее критично чем для логина
  (API обычно нужны лимиты типа 200/hour, 1000/day — это выполнимо)
- Настройка ТОЛЬКО через API, не через Customer Portal. Разработчик должен работать
  с WAAP API чтобы создать rate limiting rule. Это документировано, но барьер.

### Вывод
**Можно, аудитория — developer.** Minimum 21 для API use case — не блокер. Но статья
должна чётко сказать "настраивается через WAAP API" и дать конкретные примеры
request.limit_rate() для типичных сценариев (/api/search, /api/export, auth endpoint).

---

## Topic 5: Geo-block by country with exceptions for VPN/travelers

### Что работает
- Custom rules с условием Country: чётко поддерживается, доступно в портале
- Действия: Block, CAPTCHA, JS Challenge — на выбор
- Allow приоритет выше Block: можно создать Allow rule для конкретных IP ПОВЕРХ
  Block rule по стране. Приоритетная система (Allow=2, Block=3) гарантирует корректную
  работу.
- IP Allowlist: явный allow который бьёт всё остальное

### Ограничения (не блокеры)
- IP Allowlist: нет CIDR/subnet, максимум 30 networks per range, IPv4 и IPv6 раздельно
- Custom rule IP condition: тоже только individual IPs или range (first-last),
  не CIDR notation

### Вывод
**Полностью можно.** Это самый чистый topic — функционал есть полностью, в портале,
без API. Паттерн "geo-block + IP exception для офисов/сотрудников" работает как надо.
Ограничение CIDR надо упомянуть.

---

## Topic 6: Allowlist CI/CD pipelines and monitoring tools

### Что работает
- IP Allowlist: Allow in Firewall — полностью обходит все security checks.
  Documentally confirmed: "exclude the user from any security checks"
- "Ignored Automation" reserved tag: позволяет custom rule по User-Agent/Header
  которая освобождает запросы только от anti-automation policies (не от WAF rules)
- Custom rule Allow action по Header: можно сделать "если есть header X-Monitor-Token
  со значением Y — Allow"

### Критическое ограничение
- IP Allowlist делает полный bypass всех проверок. Если IP скомпрометирован —
  он проходит мимо всей защиты. Документация это подтверждает: "exclude from any
  security checks". Это НЕ scoped exception как в AWS WAF.
- "Ignored Automation" tag — только bot protection bypass, не WAF rules bypass.
  Если CI/CD триггерит WAF rule (например, scanner behavior) — этот тег не поможет.
- Нет механизма "skip specific rule for specific source" как у Cloudflare.

### Вывод
**Можно, но с честным предупреждением.** IP Allowlist работает и это реальный use case.
Но надо написать: "это полный bypass, используйте только для доверенных static IP".
Тему "scoped exception" (bypass только одного правила для одного источника) — у нас нет,
обещать нельзя.

---

## Итог по приоритетам для написания

| # | Topic | Статус | Почему |
|---|-------|--------|--------|
| 5 | Geo-block + IP exception | ПИСАТЬ ПЕРВЫМ | Полностью работает, в портале, без ограничений |
| 3 | Googlebot + bot protection | ПИСАТЬ | Работает для типичного случая, ограничения объяснимы |
| 2 | False positives / troubleshoot | ПИСАТЬ | Реально помогает, ручной процесс — это честно |
| 6 | Allowlist CI/CD | ПИСАТЬ с оговорками | Работает, но предупреждение про full bypass обязательно |
| 4 | Rate limit API | ПИСАТЬ для developer аудитории | Работает, но API-only — надо указать |
| 1 | Login brute force | ПЕРЕПИСАТЬ КОНЦЕПЦИЮ | Rate limiting min 21 — не подходит для login. Переформулировать как "bot-based protection" а не "rate limit after N attempts" |
