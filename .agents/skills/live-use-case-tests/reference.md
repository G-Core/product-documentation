# Live use-case tests — layout and commands

The tests repository is `C:\Projects\docs-live-use-cases`. It is not a
submodule. Docs PRs do not include it. Contributors without access write a
pickup pack under `_planning/live-use-cases/` in this repo (same relative
paths as `use_cases/` there).

## Folder (tests repo)

```
catalog.yaml
use_cases/{product}/{section}/{slug}/
  scenario.yaml
  python/cases.py
  curl/cases.py
  go/go.mod
  go/happy_test.go
  terraform/cases.py
  samples/{scenario}.{client}.txt
```

`product` and `section` match the article path
(`storage/getting-started/create-an-s3-or-sftp-storage.mdx` →
`use_cases/storage/getting-started/create-an-s3-or-sftp-storage`).

`catalog.yaml` row:

```yaml
- slug: create-an-s3-or-sftp-storage
  product: storage
  pool: general
  path: use_cases/storage/getting-started/create-an-s3-or-sftp-storage
```

`pool: gpu` only for GPU / Bare Metal GPU articles. Default `--all` is
`pool: general`.

## scenario.yaml

```yaml
article: storage/create-an-s3-or-sftp-storage.mdx
slug: create-an-s3-or-sftp-storage
product: storage
section: getting-started
pool: general

scenarios:
  - id: list-locations
    tier: smoke
    title: List Object Storage locations. At least one S3-compatible location is required.
    anchor:
      method_section: api
      heading: "Step 1. List available locations"
    clients:
      python:
        tab: Python SDK
        entry: list_locations
      go:
        tab: Go SDK
        entry: TestListLocations
      curl:
        tab: curl
        entry: list_locations
      terraform:
        skip: Terraform tab does not list locations.

  - id: happy-path
    tier: e2e
    title: Create throwaway S3 storage, list it, delete it.
    anchor:
      method_section: api
      heading: Quickstart
    covers:
      - Step 2. Create S3 storage
    clients:
      python:
        tab: Python SDK
        entry: happy_path
        sample_headings:
          - Quickstart
          - List S3 storages
          - Delete storage
      go:
        tab: Go SDK
        entry: TestHappyPath
        sample_headings:
          - Quickstart
          - List S3 storages
          - Delete storage
      curl:
        tab: curl
        entry: happy_path
        sample_headings:
          - Step 2. Create S3 storage
          - List S3 storages
          - Delete storage
      terraform:
        tab: Terraform
        entry: happy_path
        sample_headings:
          - Create S3 storage
          - Delete S3 storage
```

Rules:

- `anchor.method_section` is `api` or `terraform`. Terraform samples are
  taken from `<MethodSection id="terraform">` (no `Tab` wrapper). API
  samples use the tab title.
- `covers:` = same operation under another heading (Quickstart vs
  Step-by-step). Stops `--scan-coverage` from treating it as a gap.
- `sample_headings:` = fences this client must still match. If the e2e
  does not execute a heading, do not list it.
- Every enabled client needs `tab` and `entry`.
- Skip text must be true tomorrow (`No Terraform tab.`), not a TODO.

## Python and curl

`python/cases.py` and `curl/cases.py`: functions named in `entry`.

- `Gcore()` / `curl` with `GCORE_API_KEY` from dotenv. Do not read the
  docs-repo `.env`.
- Create helpers live in `docs_live/throwaway_*.py` (or `golive/*.go`).
  Reuse them. Do not add one-off scripts in the project root.
- Assert status and required fields. Do not assert example UUIDs from MDX.
- Delete in `finally`. Log leftover deletes.

## Go

Each article `go/` is its own module:

```
module docs-live-use-cases/{slug}

go 1.22

require github.com/G-Core/gcore-go v0.56.0

replace docs-live-use-cases/golive => ../../../../../golive
```

Depth of `replace` is five `../` from
`use_cases/{product}/{section}/{slug}/go`. Package name: slug without
hyphens (`createans3orsftpstorage`).

`client := gcore.NewClient()` (value, not pointer). Tests are
`func TestHappyPath(t *testing.T)`. Runner: `go test -run ^TestHappyPath$`.

Copy `go.sum` from an existing article module, then `go mod tidy`.

## Terraform

Provider v2 only (`TerraformWork` pins `2.0.0-rc.1`). `require_env` for
`GCORE_API_KEY`, `GCORE_CLOUD_PROJECT_ID`, `GCORE_CLOUD_REGION_ID` even
when the resource is not Cloud-region-scoped — `versions.tf` always
injects those variables.

Pattern: write HCL from the article, `init`, `apply`, assert outputs /
`resource_values`, write empty `main.tf`, `apply` (delete). Context
manager still `destroy`s on exit.

Writable vs computed: if apply says the attribute is read-only, the
article used the response field as input. Fix the MDX (Storage SFTP:
input is `sftp_password`, `password` is computed).

## Commands (tests repo)

```powershell
cd C:\Projects\docs-live-use-cases
.\venv\Scripts\python.exe -m docs_live --refresh-samples --article {slug}
.\venv\Scripts\python.exe -m docs_live --article {slug} --client python
.\venv\Scripts\python.exe -m docs_live --article {slug} --client go
.\venv\Scripts\python.exe -m docs_live --article {slug} --client curl
.\venv\Scripts\python.exe -m docs_live --article {slug} --client terraform
.\venv\Scripts\python.exe -m docs_live --scan-coverage
.\venv\Scripts\python.exe -m pytest tests\test_catalog.py -q
```

`--refresh-samples` does not call the API. Run it only after test code
matches the article.

| Orchestrator status | Meaning | Action |
|---------------------|---------|--------|
| passed | Pin matches, live call worked | Done |
| failed | Pin matches, live call failed | Fix article (or rare infra). Do not skip. |
| drift | Heading/tab/fence != pin | Update test to current MDX, then refresh |
| skipped | `skip:` in scenario.yaml | Reason must still be true |

## Pickup (owner)

1. Copy `_planning/live-use-cases/{product}/{section}/{slug}/` to
   `docs-live-use-cases/use_cases/...`
2. Add `catalog.yaml`
3. Add `go/go.mod` + `go.sum` if Go files are present
4. `--refresh-samples --article {slug}`
5. Live-run each enabled client
6. `--scan-coverage`

Do not commit secrets. Do not `git add .`.
