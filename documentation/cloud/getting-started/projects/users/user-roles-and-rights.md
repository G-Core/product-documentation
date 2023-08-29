---
title: user-roles-and-rights
displayName: User roles
published: true
order: 10
toc:
pageTitle: User roles | Gcore
pageDescription: Explore user roles and their permissions for your Cloud project.
---
# User roles and rights
Certain roles are assigned to all users in projects. Rights to manage settings, resources, and other users are set according to assigned roles. 

All available roles, their descriptions, and the rights assigned to them are listed below.    


### Client Administrator

Scope: Account

**Account Management:**
- Full access to create, read, list, edit, and delete projects.
- Ability to invite other users to projects and assign them a role (up to the Client Administrator).
- Full access to all cost reports, tasks, and audit logs (user actions).
- Ability to read account quotas and request quota limits increases.
- Full access to create, read, list, edit, and delete resource reservations.

**Resource Management:**
- Full access to create, read, list, edit, and delete any cloud resources in any project of the account. This includes Virtual Instances, Bare Metal Servers, Volumes, Snapshots, File Shares, AI Infrastructure, Kubernetes clusters, Functions, Logging, Images, SSH Keys, Networks, Firewalls, Load Balancers, and more.

### Project Administrator

Scope: Project

**Account Management:**
- Ability to invite other users to the project and assign them a role (up to the Project Administrator).
- Access to the cost report, tasks, and audit logs (user actions) but only for the project. No access to the reservation cost report.
- Ability to read account quotas.

**Resource Management:**
- Full access to create, read, list, edit, and delete any cloud resources in the project, including Virtual Instances, Bare Metal Servers, Volumes, Snapshots, File Shares, AI Infrastructure, Kubernetes clusters, Functions, Logging, Images, SSH Keys, Networks, Firewalls, Load Balancers, and more.

### Project User

Scope: Project

**Account Management:**
- Access to the cost report, tasks, and audit logs (user actions) but only for the project. No access to the reservation cost report.
- Ability to read account quotas.

**Resource Management:**
- Full access to create, read, list, edit, and delete any cloud resources in the project, including Virtual Instances, Bare Metal Servers, Volumes, Snapshots, File Shares, AI Infrastructure, Kubernetes clusters, Functions, Logging, Images, SSH Keys, Networks, Firewalls, Load Balancers, and more.

### Project Internal Network Only User

Scope: Project

**Account Management:**
- Access to the cost report, tasks, and audit logs (user actions) but only for the project. No access to the reservation cost report.
- Ability to read account quotas.

**Resource Management:**
- Limited access to create, read, list, edit, and delete any cloud resources in the project. This includes Virtual Instances, Bare Metal Servers, Volumes, Snapshots, File Shares, AI Infrastructure, Kubernetes clusters, Functions, Logging, Images, SSH Keys, Networks, Firewalls, Load Balancers, etc.

**Extra Limitations:**
- Cannot create resources with a public IP address (virtual and bare metal instances, AI clusters, load balancers, Kubernetes clusters).
- Cannot use floating IP addresses.
- Cannot edit any resources by attaching a public IP address.

### Project Observer

Scope: Project

**Account Management:**
- Access to the cost report, tasks, and audit logs (user actions) but only for the project. No access to the reservation cost report.
- Ability to read account quotas.

**Resource Management:**
- List and read any cloud resources in the project, including Virtual Instances, Bare Metal Servers, Volumes, Snapshots, File Shares, AI Infrastructure, Kubernetes clusters, Functions, Logging, Images, SSH Keys, Networks, Firewalls, Load Balancers, etc.
