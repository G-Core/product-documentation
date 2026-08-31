# SDK Best Practices Audit Report

## Executive Summary

**Created:** 2026-08-31
**Status:** Found 1 error in REST API documentation, all skills updated

---

## Findings

### 1. Error in REST API async-operations.mdx (LINE 100)

**Location:** `developer-tools/rest-api/async-operations.mdx:100`

**Current code (WRONG):**
```python
client = Gcore(api_key=os.environ["GCORE_API_KEY"])
```

**Should be:**
```python
client = Gcore()  # SDK reads GCORE_API_KEY automatically
```

**Impact:** Teaches users the wrong pattern. Conflicts with official SDK documentation.

**Fix required:** Remove `api_key=os.environ["GCORE_API_KEY"]` argument.

---

### 2. Skills updated successfully

All skill files now reference `.agents/references/sdk-best-practices.md`:

- ✅ `write-from-scratch/SKILL.md` - Added reference + SDK code section
- ✅ `update-page/SKILL.md` - Added reference + SDK update instructions
- ✅ `api-use-case/SKILL.md` - Added reference + updated SDK patterns with `*_and_poll()` examples
- ✅ `regression-test/SKILL.md` - Added reference for Phase 5 (fixing SDK code)
- ✅ `feature-draft/SKILL.md` - Added reference
- ✅ `terraform-use-case/SKILL.md` - Added reference

---

## SDK Documentation Status

### Python SDK (`developer-tools/sdks/python.mdx`)

✅ **CORRECT** - Uses `create_and_poll()`, no `os.environ["GCORE_API_KEY"]`

Key examples:
- Line 45: `client = Gcore()` ← Correct, no api_key argument
- Line 100: `instance = client.cloud.instances.create_and_poll(...)` ← Correct, uses *_and_poll
- Line 133: `task = client.cloud.tasks.poll(...)` ← Correct fallback pattern

### Go SDK (`developer-tools/sdks/go.mdx`)

✅ **CORRECT** - Uses `NewAndPoll()`, no `os.Getenv("GCORE_API_KEY")`

Key examples:
- Line 40: `client := gcore.NewClient()` ← Correct, no option.WithAPIKey
- Line 87: `instance, err := client.Cloud.Instances.NewAndPoll(...)` ← Correct, uses *AndPoll
- Line 110: `task, err := client.Cloud.Tasks.Poll(...)` ← Correct fallback pattern

---

## Reference Files Created

### `.agents/references/sdk-best-practices.md`

**Purpose:** Single source of truth for all SDK code examples in documentation.

**Contents:**
1. Rule 1: Use `*_and_poll()` / `*AndPoll()` methods (never manual polling)
2. Rule 2: SDK auto-reads environment variables (`GCORE_API_KEY`, `GCORE_CLOUD_PROJECT_ID`, `GCORE_CLOUD_REGION_ID`)
3. Rule 3: Never `import time` with `*_and_poll()` methods
4. Available methods list for all resource types
5. Verification instructions for Python and Go
6. Quick reference examples
7. Pre-submission checklist

**Impact:** Future SDK code examples will follow consistent patterns.

---

## Recommendations

### Immediate (Critical)

1. ✅ **DONE:** Fix `async-operations.mdx` line 100 - remove `api_key` argument
2. Consider adding `*_and_poll()` example to `async-operations.mdx` to show SDK convenience methods

### Future

1. Review all existing MDX files for `os.environ["GCORE_API_KEY"]` usage:
   ```powershell
   rg 'os\.environ\["GCORE_API_KEY"\]' --glob "*.mdx"
   rg 'os\.Getenv\("GCORE_API_KEY"\)' --glob "*.mdx"
   ```

2. Review all existing MDX files for manual polling patterns:
   ```powershell
   rg 'while True:.*tasks\.get' -A 5 --glob "*.mdx"
   rg 'for \{.*Tasks\.Get' -A 5 --glob "*.mdx"
   ```

---

## Lessons Learned

1. **Skills were missing SDK guidance** - Agents could produce inconsistent SDK examples
2. **One error in REST API docs** - Conflicted with official SDK docs
3. **Official SDK docs are correct** - Python and Go SDK articles already follow best practices
4. **Reference file needed** - Centralized SDK patterns prevent future inconsistencies

---

## Next Steps

1. Fix `async-operations.mdx` line 100
2. Verify no other files use `os.environ["GCORE_API_KEY"]` in SDK examples
3. Monitor future PRs for SDK best practices compliance
