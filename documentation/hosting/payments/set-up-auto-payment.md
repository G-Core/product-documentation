---
title: set-up-auto-payment
displayName: Auto payment
order: 30
published: true
toc:
   --1--Option activation: "to-enable-this-option"
   --1--Work features of auto payment: "work-features-of-auto-payment"
pageTitle: Set up auto payment | Gcore
pageDescription: Learn how to set up auto-payment for your server.
---
# Set up auto payment

Auto payment is a function that recharges the balance automatically. If you have no enough money on the balance to pay for the service, the system will take the required amount straight out of the bank card. There is a charge-off limit — you specify the maximum amount that can be charged off per month.

Note: auto payment is only used to pay for the plan, and it can't pay for extra usage beyond your plan minutes. For example, if your server plan costs €2 per day, and you have no money in your account, auto payment will charge your card €2 to keep your server running. However, if your server uses more traffic than the plan allows, you don't have enough money in your account to cover the extra usage, your server will stop working. To avoid this, make sure you have enough money in your account to cover any extra usage.

We always send notifications about traffic overcommitment. Having received it, check the balance: if there is no money enough to pay for the overcommitment, recharge the balance manually.

## To enable this option: 

1\. Open the "Billing" section in the personal account and click on the "Auto payment" tab.

<img src="https://assets.gcore.pro/docs/hosting/payments/set-up-auto-payment/________-____________eng.png" alt="Auto payment tab" width="80%">

2\. Read the information about the option, then click "Configure". 

<img src="https://assets.gcore.pro/docs/hosting/payments/set-up-auto-payment/configure_eng_2.png" alt="Configure" width="80%">

3\. Set a maximum payment amount that will be debited from your bank card in case if on the account balance are not enough funds for services’ renewal. 

<img src="https://assets.gcore.pro/docs/hosting/payments/set-up-auto-payment/confirm_eng_3.png"  alt="Set a maximum payment amount" width="80%">

! The system attempts to debit a bank card once a day. If payment is failed, you will be sent a notification. 

A recommended amount of funds in the "Maximum payment amount" field is set automatically. The amount is calculated based on expected expenses for the current services + 10%. You can specify the maximum payment amount by yourself.  

**Note**: If you click on the infinity icon or do not specify the sum, the amount of automatic payments will be unlimited.

After selecting the amount of the auto payment, click the "Confirm" button. 

4\. Confirm your bank card.  

<img src="https://assets.gcore.pro/docs/hosting/payments/set-up-auto-payment/confirm_en_4.png" alt="Confirm your bank card" width="80%">

## Work features of auto payment

- The system creates payments automatically. The payment will be generated if there is a lack of funds on the account balance, and you need to pay for the service with auto-renewal or daily debiting.
- After payment creation, the system performs a charge attempt. In case of failing the charge, you will see a notification from the system in the control panel.
- **Important**! Auto payment does not cover traffic overcommit. To cover overcommit you should fill up your account balance manually.