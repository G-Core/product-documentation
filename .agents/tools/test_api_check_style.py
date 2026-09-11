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


# --- check_content_before_method_switch ---

CONTENT_BEFORE_METHOD_SWITCH = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

This feature does X and Y.

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
  </MethodSection>
</MethodSwitch>
"""

NO_CONTENT_BEFORE_METHOD_SWITCH = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

<p>This feature does X and Y.</p>

  </MethodSection>
</MethodSwitch>
"""


def test_prose_before_method_switch_is_a_violation() -> None:
    from api_check_style import check_content_before_method_switch
    found = check_content_before_method_switch(CONTENT_BEFORE_METHOD_SWITCH.splitlines())
    assert found
    assert found[0].rule == "content-before-method-switch"


def test_prose_inside_method_section_is_clean() -> None:
    from api_check_style import check_content_before_method_switch
    assert check_content_before_method_switch(NO_CONTENT_BEFORE_METHOD_SWITCH.splitlines()) == []


# --- check_indented_method_section_close ---

INDENTED_METHOD_SECTION_CLOSE = """<MethodSection id="portal" label="Customer Portal">

- Last item.

  </MethodSection>
"""

COLUMN_ZERO_METHOD_SECTION_CLOSE = """<MethodSection id="portal" label="Customer Portal">

- Last item.

</MethodSection>
"""


def test_indented_method_section_close_is_a_violation() -> None:
    from api_check_style import check_indented_method_section_close
    found = check_indented_method_section_close(INDENTED_METHOD_SECTION_CLOSE.splitlines())
    assert found
    assert found[0].rule == "indented-method-section-close"


def test_column_zero_method_section_close_is_clean() -> None:
    from api_check_style import check_indented_method_section_close
    assert check_indented_method_section_close(COLUMN_ZERO_METHOD_SECTION_CLOSE.splitlines()) == []


# --- check_import_os_without_usage ---

IMPORT_OS_WITHOUT_USAGE = """<Tab title="Python SDK">
```python
import os
from gcore import Gcore

client = Gcore()
task = client.streaming.ai_tasks.create(task_name="transcription", url="https://example.com/v.mp4")
print(task.task_id)
```
</Tab>
"""

IMPORT_OS_WITH_USAGE = """<Tab title="Python SDK">
```python
import os
import time
from gcore import Gcore

task_id = os.environ["TASK_ID"]

client = Gcore()
while True:
    task = client.streaming.ai_tasks.get(task_id)
    if task.status in ("SUCCESS", "FAILURE"):
        break
    time.sleep(5)
```
</Tab>
"""


def test_import_os_without_usage_is_a_violation() -> None:
    from api_check_style import check_import_os_without_usage
    found = check_import_os_without_usage(IMPORT_OS_WITHOUT_USAGE.splitlines())
    assert found
    assert found[0].rule == "import-os-without-usage"


def test_import_os_with_usage_is_clean() -> None:
    from api_check_style import check_import_os_without_usage
    assert check_import_os_without_usage(IMPORT_OS_WITH_USAGE.splitlines()) == []


# --- check_go_import_alias ---

GO_IMPORT_BARE_NO_ALIAS = """<Tab title="Go SDK">
```go
import (
    "context"
    "github.com/G-Core/gcore-go"
)
```
</Tab>
"""

GO_IMPORT_WITH_ALIAS = """<Tab title="Go SDK">
```go
import (
    "context"
    gcore "github.com/G-Core/gcore-go"
)
```
</Tab>
"""


def test_go_import_without_alias_is_a_violation() -> None:
    from api_check_style import check_go_import_alias
    found = check_go_import_alias(GO_IMPORT_BARE_NO_ALIAS.splitlines())
    assert found
    assert found[0].rule == "go-import-missing-alias"


def test_go_import_with_alias_is_clean() -> None:
    from api_check_style import check_go_import_alias
    assert check_go_import_alias(GO_IMPORT_WITH_ALIAS.splitlines()) == []


# --- check_prose_without_p_tags ---

PROSE_WITHOUT_P_IN_PORTAL = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

This is bare prose that needs p tags.

<p>This one is already wrapped.</p>

1\. A numbered step.

- A bullet item.

## A heading

<Info>Info block content is fine without p.</Info>

  </MethodSection>
</MethodSwitch>
"""

PROSE_WITHOUT_P_IN_API = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="api" label="REST API">

**Interpreting the result**

<p>On success the result contains:</p>

  </MethodSection>
</MethodSwitch>
"""

PROSE_ALL_WRAPPED = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

<p>This is correctly wrapped prose.</p>

<p>1\. A numbered step.</p>

<p>2\. Another step.</p>

- A bullet item.

  </MethodSection>
</MethodSwitch>
"""

NUMBERED_WITHOUT_P = """import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

1\. This numbered item is not wrapped.

2\. Neither is this one.

  </MethodSection>
</MethodSwitch>
"""


def test_bare_prose_in_portal_section_is_a_violation() -> None:
    # Both Portal and API sections require <p> wrapping for prose.
    from api_check_style import check_prose_without_p_tags
    found = check_prose_without_p_tags(PROSE_WITHOUT_P_IN_PORTAL.splitlines())
    assert found, "Bare prose in Portal section must be flagged"
    assert found[0].rule == "prose-without-p-tag"


def test_bold_heading_without_p_is_a_violation() -> None:
    from api_check_style import check_prose_without_p_tags
    found = check_prose_without_p_tags(PROSE_WITHOUT_P_IN_API.splitlines())
    assert found
    assert found[0].rule == "prose-without-p-tag"


def test_numbered_item_without_p_is_a_violation() -> None:
    # Per MDX rules, numbered items inside <MethodSection> must be wrapped in <p>.
    # Without <p>, they merge into a single line in the Mintlify runtime.
    from api_check_style import check_prose_without_p_tags
    found = check_prose_without_p_tags(NUMBERED_WITHOUT_P.splitlines())
    assert len(found) == 2
    assert all(v.rule == "prose-without-p-tag" for v in found)


def test_wrapped_prose_list_heading_are_clean() -> None:
    from api_check_style import check_prose_without_p_tags
    assert check_prose_without_p_tags(PROSE_ALL_WRAPPED.splitlines()) == []


# ---------------------------------------------------------------------------
# warn_content_after_method_switch
# ---------------------------------------------------------------------------

_ARTICLE_WITH_POST_CONTENT = """\
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
<p>Do something in the portal.</p>
</MethodSection>
  <MethodSection id="api" label="REST API">
<p>Do it via API.</p>
</MethodSection>
</MethodSwitch>

## Extra section

<p>This appears on all tabs.</p>
"""

_ARTICLE_WITHOUT_POST_CONTENT = """\
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
<p>Do something in the portal.</p>
</MethodSection>
  <MethodSection id="api" label="REST API">
<p>Do it via API.</p>
</MethodSection>
</MethodSwitch>
"""


def test_content_after_method_switch_fires_warning() -> None:
    from api_check_style import warn_content_after_method_switch
    found = warn_content_after_method_switch(_ARTICLE_WITH_POST_CONTENT.splitlines())
    assert len(found) == 1
    assert found[0].rule == "content-after-method-switch"


def test_no_post_content_no_warning() -> None:
    from api_check_style import warn_content_after_method_switch
    assert warn_content_after_method_switch(_ARTICLE_WITHOUT_POST_CONTENT.splitlines()) == []


# ---------------------------------------------------------------------------
# check_prose_without_p_tags — portal section must be ignored
# ---------------------------------------------------------------------------

_PORTAL_PROSE_NO_P = """\
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
1\\. Open the portal.
Complete the remaining steps.
For Android smartphones, double-tap the player.
</MethodSection>
  <MethodSection id="api" label="REST API">
<p>Enable DVR on a stream.</p>
</MethodSection>
</MethodSwitch>
"""

_API_PROSE_NO_P = """\
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"

<MethodSwitch>
  <MethodSection id="api" label="REST API">
This line has no p tag and should be flagged.
</MethodSection>
</MethodSwitch>
"""


def test_prose_without_p_flags_portal_section() -> None:
    # Portal section is checked the same as API — all prose (including numbered items) needs <p>.
    from api_check_style import check_prose_without_p_tags
    violations = check_prose_without_p_tags(_PORTAL_PROSE_NO_P.splitlines())
    assert len(violations) == 3, f"Expected 3 violations (numbered item + 2 prose lines), got: {violations}"
    assert all(v.rule == "prose-without-p-tag" for v in violations)


def test_prose_without_p_flags_api_section() -> None:
    from api_check_style import check_prose_without_p_tags
    violations = check_prose_without_p_tags(_API_PROSE_NO_P.splitlines())
    assert len(violations) == 1
    assert violations[0].rule == "prose-without-p-tag"
