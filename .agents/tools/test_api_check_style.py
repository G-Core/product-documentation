"""Unit tests for api_check_style. Run: python -m pytest .agents/tools/test_api_check_style.py"""

from __future__ import annotations

from pathlib import Path

from api_check_style import check_response_outside_tabs, lint

RESPONSE_OUTSIDE_TABS = """## Create

<Tabs>
  <Tab title="Python SDK">
```python
print(policy.id)
```
  </Tab>
  <Tab title="curl">
```bash
curl -X POST "https://api.gcore.com/cloud/v1/lifecycle_policy"
```
  </Tab>
</Tabs>

<p>The API returns:</p>

```json
{"id": 15093, "status": "active"}
```
"""

RESPONSE_INSIDE_CURL_TAB = """## Create

<Tabs>
  <Tab title="Python SDK">
```python
print(policy.id)
```
  </Tab>
  <Tab title="curl">
```bash
curl -X POST "https://api.gcore.com/cloud/v1/lifecycle_policy"
```

<p>The API returns:</p>

```json
{"id": 15093, "status": "active"}
```
  </Tab>
</Tabs>

<p>Save `id` as the policy ID for later calls.</p>
"""

OS_TABS_THEN_CONFIG_JSON = """## Step 1. Add Gcore MCP Server to Cursor

<Tabs>
<Tab title="Windows">

```powershell
notepad $env:USERPROFILE\\.cursor\\mcp.json
```

</Tab>
<Tab title="macOS/Linux">

```bash
nano ~/.cursor/mcp.json
```

</Tab>
</Tabs>

Add the entry to mcp.json:

```json
{
  "mcpServers": {
    "gcore-mcp-server": {}
  }
}
```
"""

API_RETURNS_409_PROSE = """<Tabs>
  <Tab title="Python SDK">
```python
client.dns.zones.disable_dnssec(zone)
```
  </Tab>
  <Tab title="curl">
```bash
curl -X PATCH "https://api.gcore.com/dns/v2/zones/${ZONE_NAME}/dnssec"
```
  </Tab>
</Tabs>

<p>If a DS record is still published at the registrar when the request is sent, the API returns `409 Conflict`.</p>
"""

TASK_POLL_PROSE_AFTER_TABS = """<Tabs>
  <Tab title="curl">
```bash
curl -X PATCH "https://api.gcore.com/cloud/v2/k8s/clusters/..."
```

    Response:

```json
{"tasks": ["facce763-b13a-4792-83ad-fefdcda7ae37"]}
```
  </Tab>
</Tabs>

<p>The API returns a task ID. Poll GET /cloud/v1/tasks/{task_id} every five seconds until state is FINISHED.</p>
"""

JSON_WITHOUT_LABEL = """<Tabs>
  <Tab title="Python SDK">
```python
print(binary.id)
```
  </Tab>
  <Tab title="curl">
```bash
curl -sX POST 'https://api.gcore.com/fastedge/v1/binaries/raw'
```
  </Tab>
</Tabs>

<p>The response contains the binary ID:</p>

```json
{"id": 4695}
```
"""

LANGUAGE_VARIANT_CURL_THEN_JSON = """<Tabs>
  <Tab title="Modern Rust">
```bash
curl -sX POST 'https://api.gcore.com/fastedge/v1/binaries/raw' --data-binary @./release.wasm
```
  </Tab>
  <Tab title="JavaScript">
```bash
curl -sX POST 'https://api.gcore.com/fastedge/v1/binaries/raw' --data-binary @./wasm/app.wasm
```
  </Tab>
</Tabs>

<p>The response contains the binary ID:</p>

```json
{"id": 4695}
```
"""


def test_json_after_method_tabs_is_a_violation() -> None:
    found = check_response_outside_tabs(RESPONSE_OUTSIDE_TABS.splitlines())
    json_hits = [item for item in found if item.text.startswith("```json")]
    assert json_hits
    assert all(item.rule == "response-json-outside-tabs" for item in found)


def test_json_inside_curl_tab_is_clean() -> None:
    assert check_response_outside_tabs(RESPONSE_INSIDE_CURL_TAB.splitlines()) == []


def test_os_tabs_then_config_json_is_clean() -> None:
    assert check_response_outside_tabs(OS_TABS_THEN_CONFIG_JSON.splitlines()) == []


def test_prose_409_without_json_is_clean() -> None:
    assert check_response_outside_tabs(API_RETURNS_409_PROSE.splitlines()) == []


def test_poll_prose_after_in_tab_json_is_clean() -> None:
    assert check_response_outside_tabs(TASK_POLL_PROSE_AFTER_TABS.splitlines()) == []


def test_json_after_curl_without_the_api_returns_label() -> None:
    found = check_response_outside_tabs(JSON_WITHOUT_LABEL.splitlines())
    assert any(item.text.startswith("```json") for item in found)


def test_language_variant_curl_tabs_then_json_is_clean() -> None:
    assert check_response_outside_tabs(LANGUAGE_VARIANT_CURL_THEN_JSON.splitlines()) == []


def test_lint_reads_file(tmp_path: Path) -> None:
    article = tmp_path / "article.mdx"
    article.write_text(RESPONSE_OUTSIDE_TABS, encoding="utf-8")
    found = lint(article)
    assert found
    assert all(item.rule == "response-json-outside-tabs" for item in found)


def test_lint_clean_file(tmp_path: Path) -> None:
    article = tmp_path / "article.mdx"
    article.write_text(RESPONSE_INSIDE_CURL_TAB, encoding="utf-8")
    assert lint(article) == []
