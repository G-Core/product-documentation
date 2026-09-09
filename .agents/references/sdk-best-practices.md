# SDK Best Practices Reference

**Read this before writing any SDK code examples in documentation.**

This file defines SDK usage patterns that MUST be followed in all documentation examples.

---

## Rule 1: Use `*_and_poll()` / `*AndPoll()` methods

### ❌ WRONG - Manual polling

```python
# Python - WRONG
result = client.cloud.k8s.clusters.update(cluster_name, logging={"enabled": True})
task_id = result.tasks[0]

while True:
    task = client.cloud.tasks.get(task_id)
    if task.state in ("FINISHED", "ERROR"):
        break
    time.sleep(5)

cluster = client.cloud.k8s.clusters.get(cluster_name)
```

```go
// Go - WRONG
taskList, err := client.Cloud.K8S.Clusters.Update(ctx, clusterName, params)
if err != nil {
    panic(err)
}
taskID := taskList.Tasks[0]

for {
    task, err := client.Cloud.Tasks.Get(ctx, taskID)
    if err != nil {
        panic(err)
    }
    if task.State == "FINISHED" {
        break
    }
    time.Sleep(5 * time.Second)
}

cluster, _ := client.Cloud.K8S.Clusters.Get(ctx, clusterName, params)
```

### ✅ CORRECT - Use SDK convenience methods

```python
# Python - CORRECT
cluster = client.cloud.k8s.clusters.update_and_poll(
    cluster_name,
    logging={"enabled": True}
)
```

```go
// Go - CORRECT
cluster, err := client.Cloud.K8S.Clusters.UpdateAndPoll(ctx, clusterName, params)
if err != nil {
    panic(err)
}
```

### Available `*_and_poll()` methods

**K8S Clusters:**
- Python: `create_and_poll()`, `update_and_poll()`, `delete_and_poll()`, `upgrade_and_poll()`
- Go: `NewAndPoll()`, `UpdateAndPoll()`, `DeleteAndPoll()`, `UpgradeAndPoll()`

**K8S Pools:**
- Python: `create_and_poll()`, `delete_and_poll()`, `resize_and_poll()`
- Go: `NewAndPoll()`, `DeleteAndPoll()`, `ResizeAndPoll()`

**GPU Virtual Clusters:**
- Python: `create_and_poll()`, `delete_and_poll()`, `action_and_poll()`
- Go: `NewAndPoll()`, `DeleteAndPoll()`, `ActionAndPoll()`

**GPU Baremetal Clusters:**
- Python: `create_and_poll()`, `delete_and_poll()`, `rebuild_and_poll()`, `resize_and_poll()`
- Go: `NewAndPoll()`, `DeleteAndPoll()`, `RebuildAndPoll()`, `ResizeAndPoll()`

**Instances:**
- Python: `create_and_poll()`, `delete_and_poll()`, `action_and_poll()`, `resize_and_poll()`
- Go: `NewAndPoll()`, `DeleteAndPoll()`, `ActionAndPoll()`, `ResizeAndPoll()`

**Volumes, Networks, Load Balancers, etc.:**
- Check SDK source: `*_custom.go` (Go) or test with `dir(client.cloud.resource)` (Python)
- Pattern: if a method returns `tasks` array → check for `*_and_poll()` variant

### When `*_and_poll()` is NOT available

If the resource truly doesn't have a `*_and_poll()` method, use `tasks.poll()`:

```python
# Python fallback
result = client.cloud.some_resource.create(...)
task = client.cloud.tasks.poll(
    result.tasks[0],
    polling_interval_seconds=5,
    polling_timeout_seconds=300,
)
resource_id = task.created_resources.some_resources[0]
```

```go
// Go fallback
taskList, err := client.Cloud.SomeResource.New(ctx, params)
task, err := client.Cloud.Tasks.Poll(ctx, taskList.Tasks[0])
resourceID := task.CreatedResources.SomeResources[0]
```

**But first check** - the method probably exists. Don't assume it doesn't.

---

## Rule 2: SDK auto-reads environment variables

### ❌ WRONG - Using `os.environ` / `os.Getenv` for SDK config

```python
# Python - WRONG
import os
from gcore import Gcore

api_key = os.environ["GCORE_API_KEY"]
project_id = int(os.environ["GCORE_CLOUD_PROJECT_ID"])
region_id = int(os.environ["GCORE_CLOUD_REGION_ID"])

client = Gcore(
    api_key=api_key,
    cloud_project_id=project_id,
    cloud_region_id=region_id,
)
```

```go
// Go - WRONG
import "os"

client := gcore.NewClient(
    option.WithAPIKey(os.Getenv("GCORE_API_KEY")),
    option.WithCloudProjectID(parseIntOrPanic(os.Getenv("GCORE_CLOUD_PROJECT_ID"))),
    option.WithCloudRegionID(parseIntOrPanic(os.Getenv("GCORE_CLOUD_REGION_ID"))),
)
```

### ✅ CORRECT - Let SDK read variables automatically

```python
# Python - CORRECT
from gcore import Gcore

client = Gcore()  # Reads GCORE_* env vars automatically
```

```go
// Go - CORRECT
import gcore "github.com/G-Core/gcore-go"

client := gcore.NewClient()  // Reads GCORE_* env vars automatically
```

### SDK auto-reads these variables

**Both Python and Go SDKs:**
- `GCORE_API_KEY`
- `GCORE_CLOUD_PROJECT_ID`
- `GCORE_CLOUD_REGION_ID`

**Go SDK also reads:**
- `GCORE_BASE_URL`

### When to use `os.environ` / `os.Getenv`

**✅ DO use for user-defined variables:**

```python
# Python - CORRECT for user variables
cluster_name = os.environ["CLUSTER_NAME"]  # Not an SDK param
ssh_key_name = os.environ["SSH_KEY_NAME"]  # Not an SDK param
```

```go
// Go - CORRECT for user variables
clusterName := os.Getenv("CLUSTER_NAME")  // Not an SDK param
sshKeyName := os.Getenv("SSH_KEY_NAME")   // Not an SDK param
```

**Rule of thumb:**
- SDK config variables (start with `GCORE_*`) → SDK reads automatically
- User input variables (cluster names, IDs, etc.) → use `os.environ` / `os.Getenv`

---

## Rule 3: Never use `import time` with `*_and_poll()`

### ❌ WRONG

```python
import time  # ← Not needed!
from gcore import Gcore

client = Gcore()
cluster = client.cloud.k8s.clusters.update_and_poll(...)  # SDK polls internally
```

### ✅ CORRECT

```python
from gcore import Gcore

client = Gcore()
cluster = client.cloud.k8s.clusters.update_and_poll(...)
```

The `*_and_poll()` methods handle polling internally. No `time.sleep()` needed.

---

## How to verify if a method exists

### Python SDK

```python
import os
os.environ["GCORE_API_KEY"] = "fake"
os.environ["GCORE_CLOUD_PROJECT_ID"] = "123"
os.environ["GCORE_CLOUD_REGION_ID"] = "1"

from gcore import Gcore
client = Gcore()

# Check available methods
print([m for m in dir(client.cloud.k8s.clusters) if 'poll' in m.lower()])
```

### Go SDK

Check SDK source code:
```
C:\Users\{user}\go\pkg\mod\github.com\!g-!core\gcore-go@{version}\cloud\
```

Look for `*_custom.go` files - they contain `*AndPoll()` methods.

Or check Go SDK documentation:
```
https://pkg.go.dev/github.com/G-Core/gcore-go/cloud
```

---

## Quick reference - Examples

### K8S cluster update

```python
# Python
cluster = client.cloud.k8s.clusters.update_and_poll(
    cluster_name,
    logging={"enabled": True}
)
```

```go
// Go
cluster, err := client.Cloud.K8S.Clusters.UpdateAndPoll(ctx, clusterName,
    cloud.K8SClusterUpdateParams{
        Logging: cloud.K8SClusterUpdateParamsLogging{
            Enabled: gcore.Bool(true),
        },
    })
```

### GPU cluster creation

```python
# Python
cluster = client.cloud.gpu_virtual.clusters.create_and_poll(
    flavor="g2a-ai-8-2-h100-80-1",
    name="my-cluster",
    servers_count=1,
    servers_settings={...},
)
```

```go
// Go
cluster, err := client.Cloud.GPUVirtual.Clusters.NewAndPoll(ctx,
    cloud.GPUVirtualClusterNewParams{
        Flavor:       "g2a-ai-8-2-h100-80-1",
        Name:         "my-cluster",
        ServersCount: 1,
        ServersSettings: cloud.GPUVirtualClusterNewParamsServersSettings{...},
    })
```

### Pool creation

```python
# Python
pool = client.cloud.k8s.clusters.pools.create_and_poll(
    cluster_name,
    name="gpu-pool",
    flavor_id="g2a-gpu-1-24-1",
    min_node_count=1,
)
```

```go
// Go
pool, err := client.Cloud.K8S.Clusters.Pools.NewAndPoll(ctx, clusterName,
    cloud.K8SClusterPoolNewParams{
        Name:         "gpu-pool",
        FlavorID:     "g2a-gpu-1-24-1",
        MinNodeCount: 1,
        ClusterName:  clusterName,
    })
```

---

## Summary checklist

Before submitting any SDK code example:

- [ ] Uses `*_and_poll()` / `*AndPoll()` instead of manual polling loops
- [ ] No `import time` when using `*_and_poll()`
- [ ] No `os.environ["GCORE_API_KEY"]` - SDK reads it automatically
- [ ] No `os.Getenv("GCORE_CLOUD_PROJECT_ID")` - SDK reads it automatically
- [ ] Uses `os.environ` / `os.Getenv` ONLY for user variables (cluster names, etc.)
- [ ] Returns the resource object, not a task ID

If manual polling is truly needed (no `*_and_poll()` exists), verify first by checking SDK source.
