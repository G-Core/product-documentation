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


def test_json_after_tabs_is_a_violation() -> None:
    lines = RESPONSE_OUTSIDE_TABS.splitlines()
    found = check_response_outside_tabs(lines)
    rules = {item.rule for item in found}
    assert "response-json-outside-tabs" in rules
    json_hits = [item for item in found if item.text.startswith("```json")]
    label_hits = [item for item in found if "The API returns" in item.text]
    assert json_hits
    assert label_hits


def test_json_inside_curl_tab_is_clean() -> None:
    lines = RESPONSE_INSIDE_CURL_TAB.splitlines()
    found = check_response_outside_tabs(lines)
    assert found == []


def test_lint_reads_file(tmp_path: Path) -> None:
    article = tmp_path / "article.mdx"
    article.write_text(RESPONSE_OUTSIDE_TABS, encoding="utf-8")
    found = lint(article)
    assert len(found) >= 1
    assert all(item.rule == "response-json-outside-tabs" for item in found)


def test_lint_clean_file(tmp_path: Path) -> None:
    article = tmp_path / "article.mdx"
    article.write_text(RESPONSE_INSIDE_CURL_TAB, encoding="utf-8")
    assert lint(article) == []
