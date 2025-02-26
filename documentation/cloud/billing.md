---
title: billing
displayName: Billing
published: true
order: 15
toc:
pageTitle: Edge Cloud billing | Gcore
pageDescription: Learn how to pay for Gcore Edge Cloud services.
---
# Billing

All clients are subscribed to the PAYG (pay-as-you-go) billing plan, which means you only pay for the amount of time they use our Edge Cloud resources. Resources are charged per minute.

<alert-element type="warning" title="Warning">

To start using Edge Cloud services, you must add at least €4/$4 to your balance. To pay monthly, please [reach out to our support team]([url](https://gcore.com/contact-us)).

</alert-element>

As soon as your expenses reach €4/$4, the system will deduct this amount from your existing balance. If your balance has insufficient funds, the system will charge this amount from the added payment method. If payment is successful, you will continue using resources as before until your expenses reach the €4/$4 threshold again.

If the payment fails both from your Gcore balance and the added payment method, the service will be suspended. If you don’t top up your balance within the next 7 days, basic VMs will be deleted. Other cloud resources associated with your account will be deleted in 30 days. To avoid service suspension and ensure uninterrupted access to Cloud resources, you can top up your balance in advance. 

Up-to-date prices for our Edge Cloud resources are available on <a href="https://gcore.com/pricing/cloud" target="_blank">our website</a>.

**Virtual Machines** are charged from the moment you create them until they are completely stopped. Please note that volumes, snapshots, IP addresses (a floating IP, virtual IP, and reserved IP address), images and the Windows license are charged separately. The outgoing traffic is free.

**Volumes, IP addresses (a floating IP, virtual IP, and reserved IP address), images, snapshots** are charged from the moment you create them until the moment you delete them, regardless of whether the Virtual Machine is running or not.

**Bare Metal servers and AI IPUs and GPUs** are charged from the moment you create them until the moment you delete them, regardless of whether the server is running or not. IP addresses (a floating IP, virtual IP, and reserved IP), images, Windows license, and outgoing traffic for Bare Metal are charged separately.


**Managed Logging** is charged per the volume of stored logs.

**Function as a Service** is charged for the amount of compute resources used to execute the function.
