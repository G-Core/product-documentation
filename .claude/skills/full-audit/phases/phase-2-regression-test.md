# Phase 2 — Regression test

**Mindset: you are a customer reading this article for the first time.**
You have no prior knowledge of the product. You follow the article literally.
If something is unclear, confusing, or missing — it is a finding.

Record results in the formats from `../finding-formats.md` (VERIFIED OK, FINDING, UNVERIFIED).

## Resource naming

Any resource created during testing (instance, cluster, network, volume, bucket, container, firewall, load balancer, or any other cloud object) must have a name a real customer would give it on their first day.

**Correct:** `my-instance-1`, `my-cluster-1`, `my-network-1`, `my-volume-1`, `my-bucket-1`, `my-vm-1`, `my-lb-1`, `my-registry-1`.

**Never use:** `docs-*`, `audit-*`, `test-*`, `regression-*`, `doc-*`, article slugs, Jira ticket IDs, or any name that signals internal tooling. Resource names appear in published screenshots, and names like `test-audit-vm` make the article look written by automation. The rule applies to everything created in Phases 2, 3, and 5. The full table is in `.agents/references/mcp-tools/playwright.md`.

## Execution rules

- Follow the article's steps in exact order.
- At each step, use `browser_snapshot` to read the actual current UI labels, button
  names, field names, and navigation paths.
- If the article says to create something — create it.
- If the article says to delete something — delete it.
- If something the article describes does not exist or works differently — do not skip it.
  Explore what the portal actually shows now and document the divergence as a FINDING. Make a full investigation of functionality related to this.
- If a step requires a prerequisite resource (a network, a cluster, an SSH key,
  a volume, a load balancer, etc.) that does not yet exist:

  **MANDATORY: Create the resource before proceeding. Do NOT skip or note as UNVERIFIED.**

  The test account has all necessary quotas in **Luxembourg-3**. There is no valid
  reason to skip portal testing because a resource does not exist yet.

  - Create the required resource in Luxembourg-3 using the portal.
  - Name it using the standard naming pattern (`my-lb-1`, `my-vm-1`, etc.).
  - Then continue testing the article from the step that requires it.
  - Note the resource creation as "test environment setup" — not a finding.

  This applies to: Load Balancers, Virtual Machines, Networks, Routers, Subnetworks,
  Volumes, SSH Keys, Security Groups, Floating IPs, Reserved IPs, Kubernetes clusters,
  Secrets, Container Registries, and any other prerequisite.

  **The only valid reason to mark something UNVERIFIED is if the feature is gated
  (requires a special plan, a support ticket, or is physically unavailable in the
  portal UI). Absence of a test resource is never a valid reason.**

  After the test is complete, delete the resources created during testing
  (or leave them if they will be needed for subsequent articles in the same batch).

- If a feature is genuinely unavailable in this region or account (gated by plan,
  requires support enablement, or does not appear in the portal) — note it as a
  finding, describe how far you got, and mark related findings as UNVERIFIED.

## Non-portal articles

Some articles require tools other than the Customer Portal. Identify the article type
before starting Phase 2 and apply the rules below.

**General rule: never stop because a tool or environment is unavailable.**
If a testing environment is inaccessible — no GUI app, no CLI tool, no portal access
for a specific feature — do NOT wait for the user, do NOT ask for permission.
Skip testing for those specific steps, apply style guide and MDX checks to the full
article, and document the untested steps as UNVERIFIED in Phase 4. Continue to Phase 5
and beyond as normal. Style guide compliance applies to every article regardless of
whether its steps can be portal-verified.

#### Terminal articles (AWS CLI, S3cmd, shell commands)

The test machine has PowerShell and internet access. AWS CLI and S3cmd can be
installed and used directly.

**Testing rules:**

1. Verify that the tool is installed before following the article steps:
   ```powershell
   aws --version
   s3cmd --version
   ```
   If a tool is not installed — install it following the article's own instructions
   (if the article covers installation) or using the tool's official installer.
   Installation is test-environment setup, not a FINDING.

2. Obtain real credentials from the portal before running any command:
   - Navigate to the storage in the portal.
   - Copy the Access Key, Secret Key, and endpoint URL from the storage Details.
   - Use these credentials in all commands. Never fabricate credentials.

3. Follow every command in the article, run it in PowerShell, and record the actual
   output. Compare the expected output described in the article with what the terminal
   shows.

4. If a command produces an error — investigate whether the article's syntax is wrong
   or the endpoint has changed. Record as a FINDING with category `Broken flow`.

5. If a command produces no output where output is expected — record as a FINDING.

6. Files created during testing (JSON, XML, config files) must be deleted after the
   test unless the article explicitly says to keep them.

**What cannot be tested in terminal:**
- AWS JavaScript SDK examples — verify the SDK version and syntax only; mark
  version-specific claims as needing manual browser verification.

#### GUI desktop application articles (FileZilla, WinSCP, etc.)

The agent cannot open or interact with GUI desktop applications.
**Do not stop. Do not ask the user for access. Proceed immediately with style-only mode.**

**Testing rules:**

1. Skip Phase 2 portal testing entirely for GUI-only steps. Do not attempt to
   navigate the portal for steps that belong to the external app.

2. Proceed directly to Phase 6 (style guide check) and Phase 7 (MDX rules check)
   for the full article — these phases apply regardless of tool type.

3. Mark all GUI-specific steps as UNVERIFIED in the Phase 4 findings summary
   (not in the article text itself). Use this format:
   ```
   UNVERIFIED: GUI desktop application step — cannot be tested by agent.
   Location: Step N / section "[heading]"
   Instruction: [the step verbatim]
   Concern: Requires manual verification with [app name] installed locally.
   ```

4. Screenshot replacement for GUI app screenshots: do NOT retake them in Phase 3.
   Mark them in the screenshot checklist as `SKIP — GUI app, manual retake required`.

5. Note all GUI-only UNVERIFIED items in the Jira ticket description (Phase 4)
   so a human can complete the visual verification.

#### Reference table articles (endpoint URLs, region names)

Articles that consist mainly of tables of URLs, endpoints, or region names
do not have portal steps to follow. Verify the data differently:

1. Cross-reference each URL against the portal:
   - Navigate to a storage → Details to see the actual endpoint format.
   - Compare with the table in the article.

2. If the table lists regions or locations, verify each one exists in the portal's
   region dropdown or storage creation form.

3. Record any mismatch as a FINDING with category `UI label mismatch` or
   `Deprecated option`.

---

## Screenshots during Phase 2

If a portal state that is transient and cannot be reproduced later (a mid-wizard dialog,
a resource-dependent state, an error message triggered by a specific action) differs
from the article screenshot — capture it NOW and note both the old filename and the
new filename as a FINDING with category `Outdated screenshot`.

For all other screenshots, record a FINDING with category `Outdated screenshot` if
the UI has changed, and note the portal URL and navigation path. All static screenshots
will be retaken systematically in Phase 3.

**Do not apply any fixes during this phase. Collect all findings first.**

After completing all steps, clean up any test resources created during testing
(instances, networks, etc.).
