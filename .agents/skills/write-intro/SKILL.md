---
name: write-intro
description: Write the opening paragraph(s) for a documentation tab or section. Use when adding or rewriting an intro for a MethodSection (Portal, REST API, Terraform, etc.) or any article section that needs a short lead-in.
---

Write a short intro that tells the reader what they are about to do or get — nothing more.

---

## What an intro is

An intro orients the reader at the start of a tab or section. It answers in 2–3 sentences: **what can I do here?**

It is not:
- A table of contents ("this tab covers X, Y, and Z")
- A feature description ("gcore_cloud_subnet is a resource that...")
- A tutorial preamble ("in this guide you will learn to...")
- A list of constraints or implementation details

Those belong in the body of the section, not in the intro.

---

## Rules

**Length:** 2–3 sentences. Short sentences. No padding.

**Voice:** Address the task directly. The reader should feel they can scroll past the intro and get to work immediately.

**Do not write:**
- "This tab covers..."
- "This guide will show you..."
- "In this section you will learn..."
- "The following steps will walk you through..."
- Any sentence that starts with "This" and describes the article itself

**Links:** Insert organically where they add value. Not every intro needs links. When links are relevant, choose from:
- [Gcore Terraform provider v2](/developer-tools/terraform/overview) — link the provider when the reader may need setup context
- [Terraform Registry](https://registry.terraform.io/providers/G-Core/gcore/latest/docs) — link when the reader may want the full resource reference beyond what the tab shows
- Specific resource page on the registry — link the resource name inline when naming it
- Related article — link when the reader needs a prerequisite that is covered elsewhere
- Other section in the same article — anchor link when the intro references something below

For Terraform tabs specifically:

- Link the specific resource name inline to its Terraform Registry page when you name it: [`gcore_cloud_volume`](https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cloud_volume)
- Link to the [Terraform provider](/developer-tools/terraform/overview) overview only in hub or setup articles where the reader genuinely needs setup context (create-an-instance, create-a-project, manage-cloud overview). For simple resource articles, omit it — the reader is already inside a Terraform tab and knows what they're doing.
- Never use the full phrase "Gcore Terraform provider v2" as link text — it is 4 words and reads like a label. Use 2–3 word variants: `[Terraform provider]`, `[provider v2]`, `[Gcore provider]`, or weave the link into a natural phrase.
- Do not apply the same template to every article. Each intro should read as if written specifically for that resource.

---

## Examples

### Bad — describes the article, not the reader's task

> This tab covers how to create a subnet, configure DHCP and DNS settings, and manage subnet lifecycle using Terraform.

> The gcore_cloud_network_subnet resource manages the full subnet lifecycle including CIDR allocation, DHCP, and gateway configuration.

> In this section you will learn to provision a subnet with Terraform and understand how field changes affect existing VMs.

### Good — orients the reader, one clear task

> Create a subnet inside an existing [network](/cloud/networking/create-and-manage-a-network) and configure its IP range, DHCP settings, and DNS servers with the [Gcore Terraform provider v2](/developer-tools/terraform/overview). The [`gcore_cloud_network_subnet`](https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cloud_network_subnet) resource supports both IPv4 and IPv6.

> Provision block storage with the [`gcore_cloud_volume`](https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cloud_volume) resource — boot volumes from an OS image, blank data disks, or restored snapshots.

> Add a cloud router to enable outbound internet access via SNAT and routing between subnets. The [`gcore_cloud_network_router`](https://registry.terraform.io/providers/G-Core/gcore/latest/docs/resources/cloud_network_router) resource handles gateway configuration and static route management.

---

## Checklist before writing

1. What is the ONE thing the reader does in this tab? Start there.
2. Is there a key prerequisite worth naming? If yes, link it. If no, skip it.
3. Are both provider v2 and registry links genuinely useful here, or only one?
4. Does each sentence add information, or is it filler?
5. Read the Portal or API intro for the same article — match the level of detail.
