---
name: terraform-use-case
description: Add a Terraform tab to an existing Portal + REST API article using the Gcore Terraform provider v2. Use when asked to add Terraform coverage to a cloud article that already has Portal and REST API tabs.
---

Add a `<MethodSection id="terraform" label="Terraform">` section to an existing article
that already has Portal and REST API tabs, using the Gcore Terraform provider **v2 only**.

## Hard rule: v2 only

Always use provider v2. Never write v0 resource names, v0 auth fields, or v0 syntax.
If in doubt about a resource name — check the [Terraform Registry](https://registry.terraform.io/providers/G-Core/gcore/latest/docs) before writing.

---

## Scope — read exactly these files

1. This SKILL.md
2. The existing article specified by the user
3. `cloud/manage-cloud-via-terraform-v2.mdx` — HCL syntax reference for all Cloud resources
4. `.agents/references/mdx-rules.md` — MethodSwitch structure rules
5. `.agents/references/style-guide.md` — writing rules for prose

Also always check the live registry for the resource being documented:
`https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/{resource_name}`

Do not read other articles unless the existing article cross-links to them and the link
is directly relevant to mapping a Portal step to a Terraform resource.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Path to existing article | Yes | Must already have Portal + REST API tabs |
| Real Terraform testing | Yes | **Always required — no exceptions** |

---

## Phase 1 — Read the existing article and registry docs

1. Read the full article — understand what resources are created and what operations are performed
2. Open `cloud/manage-cloud-via-terraform-v2.mdx` — find the matching HCL resource blocks
3. Open the Terraform Registry page for each resource type involved:
   `https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/{resource_name}`

Identify:
- Exact `gcore_*` resource type names (v2 naming — verify on registry)
- Required fields vs optional fields
- How `project_id` and `region_id` are specified
- Whether the resource supports `terraform import`

---

## Phase 2 — Live Terraform testing (always required, always before writing)

**Test first. Write documentation second. Never the other way around.**

All HCL examples must be validated with a real `terraform apply` + `terraform destroy` cycle
before being included in the article.

**Environment:**
- API key: in environment as `GCORE_API_KEY`
- Region: Luxembourg-3 (`region_id = 76`)
- Project: default project (`project_id` from live API or portal)

**Check the latest v2 provider version before testing:**
```powershell
(Invoke-RestMethod "https://registry.terraform.io/v1/providers/G-Core/gcore").versions |
  Where-Object { $_.version -notmatch "alpha|beta|rc" } |
  Select-Object -Last 1 -ExpandProperty version
```

Use the latest stable version. If only alpha is available, use the latest alpha and note it.

**Standard provider block for all tests:**

```hcl
terraform {
  required_providers {
    gcore = {
      source  = "G-Core/gcore"
      version = "~> {LATEST_VERSION}"
    }
  }
}

provider "gcore" {
  api_key = var.api_key
}

variable "api_key"    { type = string, sensitive = true }
variable "project_id" { type = number }
variable "region_id"  { type = number }
```

**Test workflow — every step is mandatory:**

1. Write `main.tf` with the resource configuration
2. Write `terraform.tfvars` with real values (never commit this file)
3. `terraform init` — confirm provider downloads from G-Core/gcore
4. `terraform plan` — verify planned actions, no errors
5. `terraform apply -auto-approve` — confirm resource is created; record the output
6. Verify the resource exists via portal or `terraform show`
7. `terraform destroy -auto-approve` — confirm clean teardown
8. Record: exact field names accepted, any errors, provider version used

---

## Phase 3 — Write the Terraform section

### Structure

The Terraform section always uses **Structure B (independent operations)**:
- No Quickstart section
- No step-by-step accordion
- Each resource or operation = one `## Section` with an HCL block

```mdx
<MethodSection id="terraform" label="Terraform">

<p>{One sentence: what infrastructure this section provisions.}</p>

<Info>
The [Gcore Terraform provider v2](/developer-tools/terraform/overview) is required.
Set `project_id` and `region_id` in each resource block. The full resource reference
is on the [Terraform Registry](https://registry.terraform.io/providers/G-Core/gcore/latest/docs).
</Info>

## {Resource or operation name}

<p>{One sentence: what this HCL block creates or configures.}</p>

```hcl
resource "gcore_{type}" "example" {
  project_id = var.project_id
  region_id  = var.region_id
  # ...
}
```

</MethodSection>
```

### Opening sentence rules

- Do NOT start with "The following Terraform configuration..."
- Do NOT start with "The steps below..."
- Do NOT explain what Terraform is
- DO describe what is provisioned and the outcome

Good: `"Provision a Virtual Machine with a boot volume using declarative HCL."`
Bad: `"The following Terraform configuration creates a VM."` ← "The following"

### `<Info>` block (required, always)

```mdx
<Info>
The [Gcore Terraform provider v2](/developer-tools/terraform/overview) is required. Set `project_id` and `region_id` in each resource block. The full resource reference is on the [Terraform Registry](https://registry.terraform.io/providers/G-Core/gcore/latest/docs).
</Info>
```

If the reader might not have Terraform set up yet, add a sentence:
`"See [Get started with Terraform](/developer-tools/terraform/get-started-with-terraform) for installation and authentication."`

Add prerequisites if needed:
`"...and the ID of an existing [network](/cloud/networking/create-and-manage-a-network)."`

**Never duplicate** installation steps, provider configuration, variables setup, or migration instructions — these all live in `developer-tools/terraform/` and should be linked, not repeated.

### HCL block rules

1. **`project_id = var.project_id` and `region_id = var.region_id` in every resource** — never hardcode
2. **Field names and commands from the live test only** — never write a command or flag that was not tested. If you tested `terraform destroy`, document `terraform destroy`. Never substitute untested variants (e.g. `-target`) without running them first.
3. **Cross-reference other resources** with Terraform expressions: `gcore_cloud_network.main.id`
4. **Comments only for non-obvious fields** — do not comment every line
5. **Include `terraform import` as a comment** when it applies:
   ```hcl
   # terraform import gcore_instance.example '<project_id>/<region_id>/<instance_id>'
   ```
6. **v2 resource names only** — check registry if unsure: `gcore_instance`, `gcore_cloud_network`, `gcore_loadbalancer`, etc.

### What NOT to include

- No provider block — covered in [Terraform overview](/developer-tools/terraform/overview)
- No variables block — covered in [Use variables](/developer-tools/terraform/use-variables-and-organize-a-terraform-project)
- No workflow steps (`terraform init`, `apply`, `plan`) — covered in [Get started with Terraform](/developer-tools/terraform/get-started-with-terraform)
- No installation or authentication instructions — covered in `developer-tools/terraform/`
- No migration instructions from v0 — covered in [Migrate v0 to v2](/developer-tools/terraform/migrate-v0-to-v2)
- No v0 resource names, auth fields, or syntax
- No curl or SDK code

---

## Phase 4 — Add to MethodSwitch

The article has Portal and REST API sections. Add Terraform after API:

```mdx
</MethodSection>
<MethodSection id="terraform" label="Terraform">

  {Terraform content — from Phase 3}

</MethodSection>
</MethodSwitch>
```

Do not modify Portal or REST API sections.

---

## Phase 5 — Update frontmatter

Add "or Terraform" to `ai-navigation`:

Before: `"Create a VM via Customer Portal or REST API."`
After:  `"Create a VM via Customer Portal, REST API, or Terraform."`

Rules: one sentence, max 160 chars, no colons after labels, no `{...}`, no URL paths.

---

## Phase 6 — Review

### Standalone tab test

Mentally delete Portal and API tabs. Can the Terraform reader:

1. Understand what infrastructure is provisioned?
2. Find all required IDs without switching tabs?
3. Copy the HCL, set variables, and `terraform apply` without additional research?

If any answer is **no** — add the missing context.

### MDX checks

- `</MethodSection>` at column 0 after lists
- HCL blocks fenced with ` ```hcl ` language tag
- No `{identifier}` in inline backtick spans
- Import has `.jsx` extension

---

## Output

Show the complete updated article. Then:

```
Article: [path]
Resources: [list of gcore_* resource types used]
Provider version: [version from live test]
Terraform tested: yes — apply+destroy succeeded on Luxembourg-3

Gotchas:
- [non-obvious field behavior from live test]
- [any provider quirks]
```

When the user confirms — load `.agents/skills/pr/SKILL.md` to commit and open a draft PR.
