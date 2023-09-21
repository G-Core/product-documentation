---
title: troubleshoot-a-server-that-was-suspended-for-non-payment
displayName: Suspended server
published: true
toc:
   --1--How to know that the server was stopped precisely for non-payment: "how-to-know-that-the-server-was-stopped-precisely-for-non-payment"
   --1--How to renew the server: "how-to-renew-the-server"
   --2--Recharge the balance: "recharge-the-balance"
   --2--Put money on the added card: "put-money-on-the-added-card"
   --1--How to check if the transfer was successful: "how-to-check-if-the-transfer-was-successful"
   --1--How soon the money will be credited to the balance: "how-soon-the-money-will-be-credited-to-the-balance"
   --1--I transferred the money. How soon will the server be up and running?: "i-transferred-the-money-how-soon-will-the-server-be-up-and-running"
   --1--When will the server be deleted, if I do not pay for it?: "when-will-the-server-be-deleted-if-i-do-not-pay-for-it"
pageTitle: Troubleshoot a suspended server | Gcore
pageDescription: Troubleshoot a server that was suspended for non-payment and recharge your balance.
---
# Renew your server

The server stops working if you have not enough money on the account to pay for it. To activate it, recharge the balance.

## How to know that the server was stopped precisely for non-payment

This will be indicated by two signs: the server status is "suspended" and the "minimum amount for service activation" is larger than the amount of money on the balance. To make the server work again, pay for it.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment-/image2.png" alt="image2.png">

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment-/image1.png" alt="image1.png" width="50%">
</media-gallery>

## How to renew the server

You can renew the server in two ways: recharge the account balance or put money on the card from which the <a href="https://gcore.com/docs/hosting/payments/set-up-auto-payment" target="_blank">auto payment</a> is debited (to use it you must enable auto payment function).

#### Recharge the balance

How it works: the money will be credited to the account and go to pay for your unpaid services, including the suspended server. It will be activated immediately. 

What to do: in your personal account, click "Add funds". The system will show the <a href="https://gcore.com/docs/hosting/payments/pay-for-gcore-services-payment-methods" target="_blank">payment methods</a> available to you. Transfer the money and continue using the service.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment-/image5.png" alt="Recharge the balance" width="80%">

If the money was charged and did not appear on the balance in 15 minutes (for a transfer through a payment system) or 5 business days (for a bank transfer) <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help.

#### Put money on the added card

How it works: when <a href="https://gcore.com/docs/hosting/payments/set-up-auto-payment" target="_blank">auto payment</a> is enabled, the system first tries to withdraw money to pay for services from the balance, and if it is empty, then tries to withdraw from the card. If there is no money anywhere, the system will stop the services (including your server) and will try to charge the payment again 10, 5, 4, 3, 2, 1, and 0 days before the services expire. As soon as you recharge the balance of the card, the next withdrawal from it will be successful and the server will be paid.

What to do: put money on the card and the next withdrawal try will send it to the account balance. Your services will be paid, including server rent.

## How to check if the transfer was successful

If you have recharged your account balance or paid for a specific server by direct transfer, follow the transaction in the "Payments" section. When you reached the step of transferring money the system created a payment. The unpaid payment has the "new" status. As soon as you send money and it will appear on the balance the status will change to "paid".

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment-/image3.png" alt="Payments" width="80%">

If money has been automatically written off from the card during auto payment, follow the payment status in the "Expenses" section. The system creates a new line there for each attempt to write off funds. As soon as the money is written off, the "Not paid" column will have the value zero, and the "Payments" column will have the number of the created payment, during which the money came to the balance (information about it can be viewed in the "Payments" section). If the money was written off and did not come to the balance within 15 minutes <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-a-server-that-was-suspended-for-non-payment-/image4fixed.png" alt="Expenses" width="80%">

## How soon the money will be credited to the balance

After writing off from a card, the money will be credited to the balance within 15 minutes. After bank transfer — within 5 working days. If money has not come in time <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">write to technical support</a> and we will help you deal with the problem.

## I transferred the money. How soon will the server be up and running?

As soon as the money to pay for the server is credited to the account the server will immediately turn on.

## When will the server be deleted, if I do not pay for it?

If the server has been in the "Stopped" status for 14 days, it would be automatically deleted (except for servers with the KVM-SSD-1 and KVM-SAS-1 tariffs; they are automatically deleted 1 day after the non-payment). All data from the server will be erased, and the server will disappear from your personal account.