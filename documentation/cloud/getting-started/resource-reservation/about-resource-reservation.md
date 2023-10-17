---
title: about-resource-reservation
displayName: About Resource reservation
published: true
toc:
   --1--What is Resource reservation?: "what-is-resource-reservation"
   --1--Reserve a server: "reserve-a-server"
   --1--Can I cancel my reservation?: "can-i-cancel-my-reservation"
pageTitle: Resource reservation | Gcore
pageDescription: Learn how resource reservation allows long-term rental of cloud resources at a discount.
---
  
# About resource reservation

What is Resource reservation?
-----------------------------

Resource reservation is a service used to rent resources for a long time at a discount. [Cloud](https://gcore.com/cloud) resources are usually rented for a short time and paid by the minute or hour. Resource reservation works like a wholesale purchase: you rent a server for one or three years at once at a reduced price.

You’ll be able to see your discount before buying on a "Discount" line. For example, in the screenshot below, the discount is 58% and the total price is €117 per month. This means that if you ordered a server for a month without the Resource reservation option, you would pay 58% more, or €278 for the month.

![Plan price](https://assets.gcore.pro/docs/cloud/getting-started/resource-reservation/about-resource-reservation/1-plan-price.png)

The service is beneficial if:

*   you plan to use the equipment frequently. Renting resources for a year at a discount is much more cost-effective than overpaying on a short-term rental.
*   you have estimated your workload for next year, and you know how much equipment you will need. You can secure resources for yourself and not worry about the servers in the data center you need to use being sold out if you decide to rent more of them later.

Payment is charged once a month during the reservation period. If you rent a server for a year for $100/month, you’ll be billed $100 monthly for the next 12 months.

Reserve a server
----------------

1. Open the **Reservations** tab and click **Create**. When the reservation configurator opens, follow the steps below.

![The Reservations section in the menu](https://assets.gcore.pro/docs/cloud/getting-started/resource-reservation/about-resource-reservation/2-create-reservation-button.jpeg)

2. Select a region (the city where the equipment is located). Prices may vary depending on the region. Moreover, the region determines the country whose laws your equipment will be subject to. Different countries have different laws about, for example, what types of content can legally be distributed over a server. Usually, our clients choose a region in their country or a neighboring one.

3. Choose the type of server; different server types have different specifications.

4. To run on a Windows server, toggle the **Windows License** switch to on. If you keep this switch toggled off, then your server will run on Linux.

5. Choose the reservation period: one year or three years.

6. Specify the number of servers of this type you want to reserve. The price will depend on the quantity.

7. Give your reservation a name. The name will be shown in the list of reservations.

8. The reservation plan is shown in the upper-right corner. Double-check the price, location, and region, then click "Create".

![Plan price](https://assets.gcore.pro/docs/cloud/getting-started/resource-reservation/about-resource-reservation/1-plan-price.png)

9\. Wait while we process the reservation request. Your reservation will go through four status changes:

*   CREATED: The request has been created, and we are preparing the equipment.
*   IN_PROGRESS: Your server is already reserved, but not yet ready to use. Our billing department is preparing your individual rate plan and preparing to receive payment for the first month of the reservation.
*   ACTIVE: The requested servers are allocated to you. Once you create your desired bare metal server, it will be counted for the reservation.
*   EXPIRED: The reservation period has ended.

If something went wrong with your request, you might see one of the following statuses:

*   FAILED: There was an unexpected technical error; it will be resolved soon. For more details, contact our support team.
*   REJECTED: The reservation request could not be approved. For more details, contact our support team.

![Reservation status](https://assets.gcore.pro/docs/cloud/getting-started/resource-reservation/about-resource-reservation/3-reservation-status.png)

10. We have reserved equipment for you, but you cannot yet see it in your control panel. To access your servers, you’ll need to activate them. To activate your equipment, go to the **Bare Metal Servers** section and create servers with the reserved characteristics (region, Windows license, server type, quantity). You will not be charged for creating them, since it’s included as part of your reservation plan.

If you create a server later or do not create a server at all, your payment will stay the same because the hardware in the data center is set aside for you. Creating a server will simply make it visible in your control panel.

11\. Reserved servers will appear in the list, and you will be able to use them. Your balance will be billed automatically once a month.

Can I cancel my reservation?
----------------------------

You can only cancel reservations with the CREATED status. Reservations with IN_PROGRESS, ACTIVE, or EXPIRED statuses cannot be canceled.
