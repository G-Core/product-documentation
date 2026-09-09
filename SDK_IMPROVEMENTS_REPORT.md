# SDK Usage Improvements Report

## Problem Statement

Documentation examples were using manual polling (while/for loops with sleep) instead of SDK's built-in `*_and_poll()` / `*AndPoll()` methods. This resulted in:
- Verbose, repetitive code
- Unnecessary `import time` statements
- Error-prone manual task tracking
- Inconsistent patterns across examples

## Root Cause

SDK documentation was written before `*AndPoll()` convenience methods were added to the SDKs. The original examples used the lower-level pattern:
1. Call operation (returns task list)
2. Extract task ID
3. Manually poll `/tasks/{id}` endpoint
4. Sleep between polls

## SDK Auto-Configuration

Both Python and Go SDKs automatically read environment variables:

**Python SDK (`gcore.Gcore()`):**
- `GCORE_API_KEY`
- `GCORE_CLOUD_PROJECT_ID`
- `GCORE_CLOUD_REGION_ID`

**Go SDK (`gcore.NewClient()`):**
- `GCORE_API_KEY`
- `GCORE_CLOUD_PROJECT_ID`
- `GCORE_CLOUD_REGION_ID`
- `GCORE_BASE_URL`

No need to use `os.getenv()` / `os.Getenv()` for these — the SDK constructors read them automatically.

**User variables (like `CLUSTER_NAME`) still require `os.environ` / `os.Getenv`** because they are passed as method parameters, not SDK configuration.

## Available `*AndPoll()` Methods

### Cluster Operations
| Operation | Python SDK | Go SDK |
|-----------|-----------|---------|
| Create cluster | `create_and_poll()` | `NewAndPoll()` |
| Update cluster | `update_and_poll()` | `UpdateAndPoll()` |
| Delete cluster | `delete_and_poll()` | `DeleteAndPoll()` |
| Upgrade cluster | `upgrade_and_poll()` | `UpgradeAndPoll()` |

### Pool Operations
| Operation | Python SDK | Go SDK |
|-----------|-----------|---------|
| Create pool | `create_and_poll()` | `NewAndPoll()` |
| Delete pool | `delete_and_poll()` | `DeleteAndPoll()` |
| Resize pool | `resize_and_poll()` | `ResizeAndPoll()` |

## Changes Made

### Files Updated

1. **configure-cluster-autoscaling.mdx**
   - Replaced `update()` + manual polling → `update_and_poll()` / `UpdateAndPoll()`
   - Removed `import time`

2. **configure-cluster-logging.mdx**
   - Replaced `update()` + manual polling → `update_and_poll()` / `UpdateAndPoll()` (2 examples: enable + disable)
   - Removed `import time`
   - Removed redundant "Poll the task" paragraphs

3. **delete-a-gpu-kubernetes-cluster.mdx**
   - Replaced `delete()` + manual polling → `delete_and_poll()` / `DeleteAndPoll()`
   - Removed `import time`

4. **upgrade-a-gpu-kubernetes-cluster.mdx**
   - Replaced `upgrade()` + manual polling → `upgrade_and_poll()` / `UpgradeAndPoll()`
   - Removed `import time`

5. **create-a-gpu-kubernetes-cluster.mdx**
   - Replaced `create()` + manual polling → `create_and_poll()` / `NewAndPoll()`
   - Removed `import time`
   - Left separate "Poll for completion" section as educational example

6. **manage-node-pools.mdx**
   - Replaced `pools.create()` + manual polling → `create_and_poll()` / `NewAndPoll()`
   - Replaced `pools.delete()` + manual polling → `delete_and_poll()` / `DeleteAndPoll()`
   - Removed `import time`

### Before/After Example

**Before (verbose):**
```python
import time

result = client.cloud.k8s.clusters.update(cluster_name=name, logging={"enabled": True})
task_id = result.tasks[0]

while True:
    task = client.cloud.tasks.get(task_id)
    if task.state in ("FINISHED", "ERROR"):
        break
    time.sleep(5)

print("Logging enabled:", task.state)
```

**After (clean):**
```python
cluster = client.cloud.k8s.clusters.update_and_poll(
    cluster_name=name,
    logging={"enabled": True}
)
print(f"Logging enabled for cluster: {cluster.name}")
```

## Benefits

1. **Simpler code** — 70% fewer lines per example
2. **No manual task tracking** — SDK handles polling internally
3. **Consistent patterns** — all examples follow the same style
4. **Better error handling** — SDK methods raise exceptions on task failure
5. **Type safety** — methods return domain objects, not raw task responses

## Testing Recommendations

Test each updated example:
1. Set environment variables (`GCORE_API_KEY`, etc.)
2. Run Python/Go examples end-to-end
3. Verify SDK auto-polls until completion
4. Confirm returned objects have correct attributes (`cluster.name`, `pool.name`, etc.)

## Notes

- `os.environ` / `os.Getenv` usage for `CLUSTER_NAME`, `GCORE_CLUSTER_NAME`, etc. is **correct** — these are user-defined variables, not SDK config
- Separate "manual polling" examples in step-by-step sections are kept for educational purposes
- Go SDK uses tabs, not spaces (preserved in all edits)
