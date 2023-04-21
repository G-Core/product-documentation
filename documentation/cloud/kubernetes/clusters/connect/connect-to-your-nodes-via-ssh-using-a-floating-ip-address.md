---
title: connect-to-your-nodes-via-ssh-using-a-floating-ip-address
displayName: SSH connection
published: true
toc:
   --1--Assign a floating IP: "assign-a-floating-ip-address"
   --1--Connect to a node: "connect-to-your-node-via-ssh"
---
  
# Connect to your nodes via SSH using a floating IP address

Cluster nodes are virtual machines, so you can connect to your node via <a href=“https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address” target="_blank">a floating IP address</a>.

## Assign a floating IP address

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://support.gcore.com/hc/article_attachments/13321601561489" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click the required pool to expand the menu, find the node you want to connect to and click **Add IP**.

<img src="https://support.gcore.com/hc/article_attachments/13321623319825" alt="Screenshot_2023-02-27_at_14.23_1.jpg" width="528" height="463">

3\. In the new window, create a new floating IP address or attach an existing one.

*   To create a new floating IP address, go to the **Assign a floating IP** section, switch on the **Assign to existing instance** toggle, choose the node and interface, and click **Create a new floating IP**.

[<img src="https://support.gcore.com/hc/article_attachments/13321686078225" alt="Screenshot_2023-02-06_at_15.45_2.png">](https://support.gcorelabs.com/hc/article_attachments/4407809222801/image-5.png)

*   To assign an existing floating IP address, find the required one in the list below the **Assign a floating IP** section and click **Assign to instance**.

<img src="https://support.gcore.com/hc/article_attachments/13321799776529" alt="Screenshot_2023-02-06_at_15.45_1.png" width="486" height="315">

In the new window, choose the node and the interface and click **Assign floating IP**.

The floating IP has been assigned to the node, and you can now access it.

## Connect to your node via SSH

Run the command in the command line utility:

```
ssh core@**\[floating IP address\]** -i "**\[path to the private SSH key**\]"
```

Replace **\[floating IP address\]** with the actual floating IP address of the node and **\[path to the private SSH key**\] with the path to the private key on your local machine.