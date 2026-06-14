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
- Region: Luxembourg-3 (`region_id = 148`)
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

### Structure — choose A or B, same rule as the API skill

Read the article's flow type first:

| Flow type | Structure | Signal |
|-----------|-----------|--------|
| Steps feed into each other (network → subnet → VM) | **A — complete state** | "Create" or "Deploy" article |
| Operations are independent (rename, quota, firewall rule) | **B — independent ops** | "Manage" or "Configure" article |

Test: "Can the reader do Step 3 without Steps 1 and 2?" — if yes, Structure B. If no, Structure A.

---

**Structure A — Complete desired state**

Use when the provisioned resources depend on each other (e.g. subnet references `network_id`).

- Opening `<p>` introduces what is provisioned
- `## Create …` section: **one HCL block with ALL interdependent resources** — this is the reader's complete working `.tf` file
- Modification sections (`## Rename …`, `## Delete …`, `## Import …`) also show the **full state**, not partial snippets — a partial block looks like the other resources were removed
- No step-by-step accordion — HCL is self-documenting

```mdx
<MethodSection id="terraform" label="Terraform">

<p>{One sentence: what this section provisions.}</p>

## Create {resources}

<p>{Why/when — one sentence.}</p>

```hcl
resource "gcore_cloud_network" "example" { ... }
resource "gcore_cloud_network_subnet" "example" { ... }
output "network_id" { ... }
```

## Rename {resource}

<p>{Edit `name` in the resource block and run `terraform apply`.}</p>

```hcl
resource "gcore_cloud_network" "example" {
  # ...
  name = "my-network-renamed"
}
resource "gcore_cloud_network_subnet" "example" { ... }  # unchanged
```

## Delete {resources}

<p>{Remove both resource blocks …}</p>

```hcl
# Remove or comment out both blocks:
# resource "gcore_cloud_network" ...
# resource "gcore_cloud_network_subnet" ...
```

```bash
terraform apply
```

</MethodSection>
```

---

**Structure B — Independent operations**

Use when operations are unrelated and can be performed in any order.

- Opening `<p>` introduces the section
- Each `## Section` is self-contained: one HCL block that works on its own

```mdx
<MethodSection id="terraform" label="Terraform">

<p>{One sentence.}</p>

## {Operation name}

<p>{Why/when.}</p>

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

### `<Info>` block — when to use

**Do NOT use an `<Info>` block** as a dumping ground for multiple facts. Instead, use a single opening `<p>` that naturally embeds the provider link.

Use an `<Info>` block only when there is a genuine prerequisite the reader must have before they can use any code in the section (e.g. an existing network ID, a secret ID). Keep it to one sentence.

**Wrong pattern — Info block stuffed with everything:**
```mdx
<Info>
The provider is required. Set project_id. The full reference is on Terraform Registry. See Get started for installation.
</Info>
```

**Correct pattern — single opening `<p>`:**
```mdx
<p>Declare Edge Cloud networks using the [Gcore Terraform provider v2](/developer-tools/terraform/overview).</p>
```

### `<p>` description rules for each section

Every `## Section` must have a `<p>` that tells the reader **why** or **when** — not just **what**.

| Situation | Wrong | Right |
|-----------|-------|-------|
| Create | "Declares a new network." | "Declares a new private network." (if "new" adds no info, just: "Declares a network.") |
| Update | "Updates the network." | "Edit fields in the resource block and run `terraform apply`." |
| Delete | "Deletes the network." | "Remove the resource block — Terraform detects the missing declaration and deletes it on the next `terraform apply`." |
| Data source | "Lists all networks." | "Returns all networks with their IDs and names." |
| Import | "Imports the network." | "Use when a network was created outside Terraform and needs to be managed as code." |

**Forbidden in `<p>`:**
- Technical Terraform jargon the reader doesn't need: "no resource replacement", "in-place update", "idempotent"
- Negative capabilities: "this resource does not accept project_id" — let the code speak
- "your account", "your configuration" — use "the account", "the configuration"
- Link-only sentences: "The full reference is on the [Terraform Registry](...)" — embed links into content sentences
- Banned style guide patterns: "See [X] for more information", "For more details, see [X]"

### Full lifecycle coverage (mandatory)

The Terraform tab must cover the same lifecycle as the Portal and API tabs.  
If the Portal tab has Create + Update + Delete, the Terraform tab must also have Create + Update + Delete.

**For Update:** Show the updated HCL block (same resource, changed field values). Add a `<p>` explaining that editing fields and running `terraform apply` applies changes.

**For Delete:** Always show a code block. The standard pattern:
1. `<p>` — explain that removing the block causes deletion on next apply
2. HCL block — show the block commented out so the reader knows exactly what to remove
3. Bash block — `terraform apply`

```mdx
<p>Remove the resource block — Terraform detects the missing declaration and deletes it on the next `terraform apply`.</p>

```hcl
# Remove or comment out this block:
# resource "gcore_cloud_network" "example" {
#   name       = "my-network"
#   project_id = var.project_id
#   region_id  = var.region_id
# }
```

```bash
terraform apply
```
```

**Do not skip testing a command before documenting it.** If a variant seems logical but was not run during testing, it must be tested first or omitted entirely.

### HCL block rules

1. **`project_id = var.project_id` and `region_id = var.region_id` in every resource** — never hardcode
2. **Field names and commands from the live test only** — document exactly what was tested. If the test used `terraform destroy`, the article shows `terraform destroy`. Never substitute a different command or flag without testing it first — even if it seems equivalent.
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

## Phase 6 — Style guide review (HARD STOP — do this before every output)

**Read `.agents/references/style-guide.md` in full. Then go sentence by sentence through every line written in this session and check each item below. Do not skip. Do not do this from memory.**

### Checklist — run each item, fix before continuing

**Voice:**
- [ ] No "you" or "your" in any prose — use "the account", "the configuration"
- [ ] No forbidden words: just, simply, obviously, ensure, platform, seamlessly, leverage, for example, such as
- [ ] No meta-preamble: "The following configuration...", "The steps below...", "This section covers..."
- [ ] No "does not support", "is not available", "is not supported" — rewrite to tell the reader where to go instead

**`<p>` and `<Info>` descriptions:**
- [ ] `<Info>` blocks used only for a single genuine prerequisite — never multiple facts
- [ ] If an `<Info>` lists token + project_id + region_id → merge into opening `<p>` as inline prereqs
- [ ] Each `<p>` under a heading says WHY or WHEN — not just WHAT
- [ ] Stop when the point is made — no appended clauses that add nothing

**Links:**
- [ ] Link text 1–2 words maximum
- [ ] No banned patterns: "For more details, see [X]", "For a full walkthrough, see [X]", "See [X] for more information", "Refer to [X]"
- [ ] No standalone sentences whose only purpose is to host a link — embed the link in a content sentence or remove it

**Headings:**
- [ ] Every `##` and `###` heading must be followed by a prose `<p>` sentence before any code block, table, or list
- [ ] Sentence case: "Create a network" not "Create a Network"
- [ ] No What/How/Why/When openers
- [ ] "platform" → "region default", "the service", or name the specific thing

**Code after headings:**
- [ ] After `## Clean up` / `## Delete` / `## Destroy` — `<p>` BEFORE the code block, not after

**Lifecycle completeness:**
- [ ] Mentally delete Portal and API tabs — can the Terraform reader create, update, AND delete the resource without switching tabs?

**Links:**
- Link text 1–2 words maximum
- Each URL linked only once per article — subsequent mentions plain text
- No standalone link sentences: "The full reference is on the [Terraform Registry](...)"
- No banned patterns: "See [X] for more information", "For more details, see [X]"

**Headings:**
- Sentence case: "Create a network" not "Create a Network"
- No What/How/Why/When openers
- No infinitives: "To create" → "Create"
- Every heading must be followed by a prose sentence before code

**Formatting:**
- Em-dashes spaced: ` — ` not `—`
- Bold only for UI elements, not for emphasis
- Code language tag always present: ` ```hcl `, ` ```bash `

**Lifecycle completeness:**
- Mentally delete Portal and API tabs — can the Terraform reader create, update, AND delete the resource without switching tabs?
- If any operation is missing — add it before showing the result

---

## Phase 7 — Standalone tab and MDX checks

**Standalone tab test:** Mentally delete Portal and API tabs. Can the Terraform reader:

1. Understand what infrastructure is provisioned?
2. Find all required IDs without switching tabs?
3. Copy the HCL, set variables, and `terraform apply` without additional research?

If any answer is **no** — add the missing context.

**MDX checks:**

- `</MethodSection>` at column 0 after lists
- HCL blocks fenced with ` ```hcl ` language tag
- Bash blocks fenced with ` ```bash `
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
