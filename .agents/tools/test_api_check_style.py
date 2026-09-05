"""Unit tests for api_check_style. Run: python -m pytest .agents/tools/test_api_check_style.py"""

from __future__ import annotations

from pathlib import Path

from api_check_style import (
    check_combined_step_labels,
    check_forbidden_sdk_patterns,
    check_method_switch_import,
    check_response_outside_tabs,
    lint,
)

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

FORBIDDEN_SDK_PATTERNS = """<Tabs>
  <Tab title="Python SDK">
```python
client = Gcore(api_key=os.environ["GCORE_API_KEY"])
```
  </Tab>
  <Tab title="Go SDK">
```go
client := gcore.NewClient(option.WithAPIKey(os.Getenv("GCORE_API_KEY")))
result, err := client.Cloud.Something.Do(context.TODO(), params)
```
  </Tab>
</Tabs>
"""

CANONICAL_SDK_PATTERNS = """<Tabs>
  <Tab title="Python SDK">
```python
client = Gcore()
cluster = client.cloud.k8s.clusters.create_and_poll(name="my-cluster")
```
  </Tab>
  <Tab title="Go SDK">
```go
client := gcore.NewClient()
ctx := context.Background()
cluster, err := client.Cloud.K8S.Clusters.NewAndPoll(ctx, params)
```
  </Tab>
</Tabs>
"""

COMBINED_STEP_LABELS = """## Quickstart

<Tabs>
  <Tab title="Python SDK">
```python
# Step 1. List flavors
# Step 3+4. Create and poll
instance = client.cloud.instances.create_and_poll()
```
  </Tab>
  <Tab title="Go SDK">
```go
// Step 3+4. Create and poll
cluster, err := client.Cloud.K8S.Clusters.NewAndPoll(ctx, params)
```
  </Tab>
</Tabs>
"""

SEPARATE_STEP_LABELS = """## Quickstart

<Tabs>
  <Tab title="Python SDK">
```python
# Step 1. List flavors
# Step 2. Create instance
instance = client.cloud.instances.create_and_poll()
```
  </Tab>
</Tabs>
"""

METHOD_SWITCH_IMPORT_BARE = """import { MethodSwitch, MethodSection } from "/snippets/method-switch"

<MethodSwitch>
</MethodSwitch>
"""

METHOD_SWITCH_IMPORT_JSX = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
</MethodSwitch>
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


def test_gcore_api_key_ctor_and_go_placeholders_are_violations() -> None:
    found = check_forbidden_sdk_patterns(FORBIDDEN_SDK_PATTERNS.splitlines())
    rules = {item.rule for item in found}
    assert rules == {"sdk-gcore-api-key-ctor", "sdk-with-api-key", "sdk-context-todo"}


def test_canonical_sdk_patterns_are_clean() -> None:
    assert check_forbidden_sdk_patterns(CANONICAL_SDK_PATTERNS.splitlines()) == []


def test_combined_step_labels_are_violations() -> None:
    found = check_combined_step_labels(COMBINED_STEP_LABELS.splitlines())
    assert len(found) == 2
    assert all(item.rule == "combined-step-label" for item in found)


def test_separate_step_labels_are_clean() -> None:
    assert check_combined_step_labels(SEPARATE_STEP_LABELS.splitlines()) == []


def test_method_switch_import_without_jsx_is_a_violation() -> None:
    found = check_method_switch_import(METHOD_SWITCH_IMPORT_BARE.splitlines())
    assert found
    assert found[0].rule == "method-switch-import"


def test_method_switch_import_with_jsx_is_clean() -> None:
    assert check_method_switch_import(METHOD_SWITCH_IMPORT_JSX.splitlines()) == []
