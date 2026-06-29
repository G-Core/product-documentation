# Edge Cloud — Terraform Tabs Plan

Для каждой статьи добавляем вкладку **Terraform** рядом с существующей **REST API** вкладкой.
Статьи сгруппированы по окружениям — каждое окружение создаётся один раз и переиспользуется для связанных статей. После завершения группы — `terraform destroy`.

Ветка: `tf-cloud-guides` (создана от main).

---

## Порядок работы по окружениям

### ГРУППА A — Foundation (создать один раз, держать до конца групп B–D)

Эти ресурсы нужны почти всем остальным группам. Создать в начале, удалить в конце.

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 1 | `cloud/getting-started/projects/create-a-project.mdx` | Create and manage projects | ✓ done |
| 2 | `cloud/getting-started/request-a-quota-increase.mdx` | Manage resource quotas | skip — нет TF ресурса |

---

### ГРУППА B — Networking (создать сеть, держать для групп C и D)

Сеть + подсеть + роутер + файрвол нужны для VM, LB, File Shares, Bare Metal.

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 3 | `cloud/networking/create-and-manage-a-network.mdx` | Create and manage a network | ✓ done |
| 4 | `cloud/networking/create-and-manage-a-subnetwork.mdx` | Create and manage a subnetwork | ✓ done |
| 5 | `cloud/networking/create-and-manage-a-router.mdx` | Create and manage a router | ✓ done |
| 6 | `cloud/networking/add-and-configure-a-firewall.mdx` | Add and configure a firewall | ✓ done |

---

### ГРУППА C — Virtual Machines (переиспользует сеть из B, удалить VM после)

VM зависит от сети. Volumes, placement groups, snapshots, floating/reserved/VIP IP — всё это делается в рамках одного VM-окружения.

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 7 | `cloud/virtual-instances/volumes/create-and-configure-volumes.mdx` | Create and configure a volume | ✓ done |
| 8 | `cloud/virtual-instances/placement-groups/configure-a-placement-group.mdx` | Configure a placement group | ✓ done |
| 9 | `cloud/virtual-instances/create-an-instance.mdx` | Create a Virtual Machine | ✓ done |
| 10 | `cloud/virtual-instances/customize-initial-setup-for-your-instance.mdx` | Customize the initial setup for a VM | ✓ done |
| 11 | `cloud/virtual-instances/check-the-operational-status-of-your-instance.mdx` | Check the operational status of a VM | ✓ done |
| 12 | `cloud/virtual-instances/snapshots/take-a-snapshot-of-your-file-system.mdx` | Take a snapshot of your file system | skip — нет TF ресурса |
| 13 | `cloud/networking/ip-address/create-and-configure-a-floating-ip-address.mdx` | Create and configure a floating IP | ✓ done |
| 14 | `cloud/networking/ip-address/create-and-configure-a-reserved-ip-address.mdx` | Create and configure a reserved IP | ✓ done |
| 15 | `cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address.mdx` | Create and configure a virtual IP | ✓ done |

→ **`terraform destroy` VM-ресурсов** (сеть из B держим)

---

### ГРУППА D — Load Balancer (переиспользует сеть из B, удалить LB после)

LB нужен сеть + подсеть. TLS-сертификат требует Secrets Manager.

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 16 | `cloud/secrets-manager/upload-a-pkcs12-file.mdx` | Configure secrets for HTTPS LB | ✓ done |
| 17 | `cloud/networking/create-and-configure-a-load-balancer.mdx` | Create and configure a load balancer | ✓ done |
| 18 | `cloud/networking/load-balancers/manage-load-balancers.mdx` | Manage load balancers | ✓ done |
| 19 | `cloud/networking/load-balancers/add-certificates-to-load-balancer.mdx` | Add TLS certificates to a LB | ✓ done |

→ **`terraform destroy` LB + secrets + сеть из B + Foundation из A**

---

### ГРУППА E — Kubernetes (независимая, нужна своя сеть)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 20 | `cloud/kubernetes/clusters/create-a-kubernetes-cluster.mdx` | Create a Kubernetes cluster | ✓ done |
| 21 | `cloud/kubernetes/clusters/upgrade.mdx` | Upgrade a Kubernetes cluster | ✓ done |

→ **`terraform destroy` K8s**

---

### ГРУППА F — CaaS (независимая)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 22 | `cloud/caas/create-a-container.mdx` | Create a container | skip — нет TF ресурса |
| 23 | `cloud/caas/manage-containers.mdx` | Manage containers | skip — нет TF ресурса |

→ **`terraform destroy` CaaS**

---

### ГРУППА G — Container Registry (независимая)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 24 | `cloud/container-registry/create-container-registry.mdx` | Create a Container Registry | skip — нет TF ресурса |
| 25 | `cloud/container-registry/manage-container-registries.mdx` | Manage container registries | skip — нет TF ресурса |

→ **`terraform destroy` Registry**

---

### ГРУППА H — PostgreSQL (независимая)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 26 | `cloud/managed-database-postgresql/manage-postgresql-servers.mdx` | Manage a PostgreSQL server | skip — нет TF ресурса |

→ **`terraform destroy` PostgreSQL**

---

### ГРУППА I — File Shares (нужна сеть, своя)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 27 | `cloud/file-shares/configure-file-shares.mdx` | Configuring file shares | ✓ done |

→ **`terraform destroy` File Shares + сеть**

---

### ГРУППА J — Bare Metal (нужна сеть, своя)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 28 | `cloud/bare-metal-servers/create-a-bare-metal-server.mdx` | Create a Bare Metal server | in progress |

→ **`terraform destroy` Bare Metal + сеть**

---

### ГРУППА K — Images (независимая, только upload)

| # | Файл | Заголовок | Статус |
|---|------|-----------|--------|
| 29 | `cloud/images/upload-an-image-to-the-storage.mdx` | Upload an image to the storage | ✓ done |

---

## Нет Terraform скилла

В `.agents/skills/` нет скилла для написания Terraform-вкладок.
Нужно создать `.agents/skills/terraform-use-case/SKILL.md` по образцу `api-use-case/SKILL.md`.

Основные отличия от API-скилла:
- Тестирование через `terraform init` → `terraform plan` → `terraform apply` → `terraform destroy`
- Provider: `gcore/gcore` (registry.terraform.io)
- Код — HCL блоки `resource`, `data`, `variable`
- Пример структуры: смотреть `dns/dns-plugins/manage-dns-with-terraform-v2.mdx`
- Регион Luxembourg-3: в Terraform `region = "Luxembourg-3"` или через `region_id`

## Заметки

- Ветка: `tf-cloud-guides` (от main)
- Одна статья за раз, 100% живое тестирование
- Terraform provider: проверить актуальную версию на registry.terraform.io/providers/G-Core/gcore
- `ai-navigation` обновлять: добавить "or Terraform" к существующей фразе
