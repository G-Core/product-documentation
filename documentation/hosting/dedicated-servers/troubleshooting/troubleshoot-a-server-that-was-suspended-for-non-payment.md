---
title: Troubleshoot-a-server-that-was-suspended-for-non-payment
displayName: Suspended server
published: true
order: 10
toc:
   --1--How to know that the server was stopped precisely for non-payment: "how-to-know-that-the-server-was-stopped-precisely-for-non-payment"
   --1--How to renew the server: "how-to-renew-the-server"
   --2--Recharge the account balance: "recharge-the-balance"
   --2--Pay for a specific server: "pay-for-a-specific-server"
   --2--Put money on the added card: "put-money-on-the-added-card"
   --1--How to check if the transfer was successful: "how-to-check-if-the-transfer-was-successful"
   --1--How soon the money will be credited to the balance: "how-soon-the-money-will-be-credited-to-the-balance"
   --1--I transferred the money. How soon will the server be up and running?: "i-transferred-the-money-how-soon-will-the-server-be-up-and-running"
   --1--When will the server be deleted, if I do not pay for it?: "when-will-the-server-be-deleted-if-i-do-not-pay-for-it"
pageTitle: Troubleshoot a suspended server | Gcore
pageDescription: Troubleshoot a server that was suspended for non-payment and recharge your balance.
---
# Renew your server (dedicated)

The server stops working if you have not enough money on the account to pay for it. To activate it, recharge the balance.

## How to know that the server was stopped precisely for non-payment

This will be indicated by two signs: the server status is "suspended" and the "minimum amount for service activation" is larger than the amount of money on the balance. To make the server work again, pay for it.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image7.png" alt="How to know that the server was stopped precisely for non-payment" width="80%">
<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image4.png" alt="How to know that the server was stopped precisely for non-payment" width="50%">

## How to renew the server

Different payment methods are available for different servers.

Dedicated server  with auto-renewal:
- Recharge the balance: +
- Pay for a specific server: +
- Put money on the added card*: +

Dedicated server without auto-renewal:
- Recharge the balance: -
- Pay for a specific server: +
- Put money on the added card: -


\* The payment method is available if <a href="https://gcore.com/docs/hosting/payments/set-up-auto-payment" target="_blank">auto payment</a> is enabled on the account only.

You can find out whether auto-renewal is enabled for the dedicated server by the clock icon. If there is the icon — auto-renewal is enabled, if not — it is disabled.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image6.png" alt=" payment method ">
<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image8.png" alt=" payment method ">

### Recharge the balance

_Suitable for what servers:_ dedicated server with auto-renewal.

_How it works_: the money will be credited to the account and go to pay for your unpaid services, including the suspended server. It will be activated immediately. 

_What to do_: in your personal account, click "Add funds". The system will show <a href="https://gcore.com/docs/hosting/payments/pay-for-gcore-services-payment-methods" target="_blank">payment methods</a> available to you. Transfer the money and continue using the service.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image1.png" alt=" payment methods" width="50%">

If the money was charged and did not appear on the balance in 15 minutes (for a transfer through a payment system) or 5 business days (for a bank transfer) <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help.

### Pay for a specific server

_Suitable for what servers:_ all dedicated servers.

_How it works_: you transfer money, and it will be used to pay for a specific server only — even if you have a bunch of other unpaid services.

_What to do_: click the line with the stopped server and click "Renew". The system will offer <a href="https://gcore.com/docs/hosting/payments/pay-for-gcore-services-payment-methods" target="_blank">payment methods</a> available to you. Transfer money and as soon as they are credited to the account the server will be paid and activated.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/mceclip3.png" alt="Renew" width="80%">

**Please note**: If you reach the last payment step and change your mind the system will not turn on the server but will create a payment in the "new" status. The server renewal will be linked to this particular payment — even if you recharge the balance in another way, the server will not start. To make the server work, you need to complete the payment: select it, click "Pay" and transfer the money.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image3.png" alt="Pay" width="80%">

### Put money on the added card

_Suitable for what servers:_ dedicated server with auto-renewal; <a href="https://gcore.com/docs/hosting/payments/set-up-auto-payment" target="_blank">auto payment</a> must be enabled.

_How it works_: when auto payment is enabled, the system first tries to withdraw money to pay for services from the balance, and if it is empty, then tries to withdraw from the card. If there is no money anywhere, the system will stop the services (including your server) and will try to charge the payment again 10, 5, 4, 3, 2, 1, and 0 days before the services expire. As soon as you recharge the balance of the card, the next withdrawal from it will be successful and the server will be paid.

_What to do_: put money on the card and the next withdrawal try will send it to the account balance. Your services will be paid, including server rent.

## How to check if the transfer was successful

If you have recharged your account balance or paid for a specific server by direct transfer, follow the transaction in the "Payments" section. When you reached the step of transferring money the system created a payment. The unpaid payment has the "new" status. As soon as you send money and it will appear on the balance the status will change to "paid".

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image2.png" alt="Payments section" width="80%">

If money has been automatically written off from the card during auto payment, follow the payment status in the "Expenses" section. The system creates a new line there for each attempt to write off funds. As soon as the money is written off, the "Not paid" column will have the value zero, and the "Payments" column will have the number of the created payment, during which the money came to the balance (information about it can be viewed in the "Payments" section). If the money was written off and did not come to the balance within 15 minutes <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment/image5.png" alt="Expenses section" width="80%">

## How soon the money will be credited to the balance

After writing off from a card, the money will be credited to the balance within 15 minutes. After bank transfer — within 5 working days. If money has not come in time <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help you deal with the problem.

## I transferred the money. How soon will the server be up and running?

As soon as the money to pay for the server is credited to the account the server will immediately turn on.

## When will the server be deleted, if I do not pay for it?

If the server has been in the "Stopped" status for 14 days, it would be automatically deleted (except for servers with KVM-SSD-1 and KVM-SAS-1 tariffs; they are automatically deleted 1 day after the non-payment). All data from the server will be erased, and the server will disappear from your personal account.