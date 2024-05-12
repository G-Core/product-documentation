---
title: connect-to-your-instance-via-ssh
displayName: Configure and manage SSH keys
order: 10
published: true
toc:
   --1--Generate SSH keys: "generate-ssh-keys"
   --2--In the Customer Portal: "generate-ssh-keys-in-the-customer-portal"
   --3--When creating an instance: "generate-an-ssh-key-when-creating-an-instance"
   --3--In the SSH Keys section: "generate-an-ssh-key-in-the-ssh-keys-section"
   --2--Via CLI tools or SSH clients: "generate-ssh-keys-via-cli-tools-or-ssh-clients"
   --3--Terminal or Command Prompt: "terminal-or-command-prompt"
   --3--Windows Subsystem for Linux (WSL): "windows-subsystem-for-linux-wsl"
   --3--PuTTY: "putty"
   --1--Add a public key to the Customer Portal: "add-a-public-ssh-key-to-the-customer-portal"
   --1--Manage SSH keys in the Customer Portal: "manage-sshkeys-in-the-customer-portal"
   --2--Delete SSH keys: "delete-ssh-keys"
   --2--Stop sharing SSH keys: "stop-sharing-ssh-keys"
pageTitle: Configure and Manage SSH Keys | Gcore
pageDescription: Learn how to generate SSH keys, add them to Gcore Customer Portal, delete them, and stop sharing them
customUrl: /cloud/virtual-instances/connect/connect-to-your-instance-via-ssh 
---
# Configure and manage SSH keys

This guide provides instructions for configuring a pair of SSH keys, adding a public key to the Gcore Customer Portal, and managing the keys within the portal.

## Generate SSH keys 

You can generate SSH keys in different ways: 

- [In the Gcore Customer Portal](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#generate-ssh-keys-in-the-customer-portal)
- [Via CLI tools and SSH clients](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#generate-ssh-keys-via-cli-tools-or-ssh-clients)

<alert-element type="warning" title="Warning">

Never share your private SSH key or password with third parties. Doing so may result in unauthorized access to your VM and the compromise of sensitive information stored there. 

</alert-element>

### Generate SSH keys in the Gcore Customer Portal

You can create SSH keys when creating a VM or generate them separately in the [SSH Keys](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#generate-an-ssh-key-in-the-ssh-keys-section) section. 

After you generate the keys, a public key will be added to the system and appear in the “SSH Keys” section, along with any other keys that you've added or created. A private key will be downloaded to your local storage.

<alert-element type="info" title="Info">

When naming a public key, consider that the name can contain only Latin characters, underscores, spaces, and dots. Its length must be between 3 and 63 characters.

</alert-element>

<tabset-element>

#### Generate an SSH key when creating a Gcore Virtual Machine 

While creating a VM, in Step 8, you'll be asked to choose one of the following options in the “SSH key” section:
Oksana, please add a direct link to creating a VM page (in the Gcore CP) in line 56
- **Select SSH key**: Add a key that's already stored in the Gcore Customer Portal by selecting it from the dropdown list.
- **Add a new SSH key**: Add an existing key generated via CLI tools or SSH client.
- **Generate an SSH key**: Create a new key.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/create-instance-ssh-keys.png" alt="SSH keys section with three options: select, generate, or add a new SSH key" width="80%">

To generate a new key:

1\. Click **Generate SSH key**. A new dialog box will open.

2\.  Enter the key name to identify the key in the system. 

3\. Select **Create SSH key** and save the public key locally.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/autogenerate-ssh-key.png" alt="A dialog with options to name and create an SSH key" width="80%">
 
#### Generate an SSH key in the Gcore Customer Portal

Generate a pair of SSH keys separately, then use a public key for authentication when creating your VM.

To generate the keys:

1\. In the Gcore Customer Portal, go to **Cloud** > **SSH Keys**.

2\. Click **Autogenerate SSH key**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/cloud-ssh-keys-annotated.png" alt="An SSH keys tab in the Gcore Customer Portal" width="80%">

3\. Enter the key name and select **Create SSH key**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/autogenerate-ssh-key.png" alt="A dialog with options to name and create an SSH key" width="80%">

4\. The public key will be added to a VM and the private key will be saved to your local storage.

</tabset-element>

## Generate SSH keys via CLI tools or SSH clients

<tabset-element>

### Terminal or command prompt 

Follow these instructions to generate SSH keys on Linux, macOS, or Windows 10/11 devices:

1\. Open Terminal (Linux, macOS) or Command Prompt (cmd.exe on Windows).

2\. Run the following command to generate a key pair: 

```
ssh-keygen -t rsa -b 2048
```

You'll be asked to enter the file where the keys should be saved. You can specify a custom location (for example, `.ssh/`), or press **Enter** to save the keys to the default directory. The default directory is `~/.` for Linux/macOS and `C:\Users\\` for Windows.

4\. Press **Enter**.

5\. You’ll be asked to enter a password for the key as an additional security step. You can either create a password and enter it every time you connect via SSH or leave the field empty and press **Enter** to create the key without a password.

6\. Confirm the password by entering it again, or leave the field empty and press **Enter**. You can find your key in the default directory or in the custom location you've specified during the key creation.

7\. The public key will be saved in the .pub file. You need to add this public key to your VM as described in our guide on [adding a public SSH key to the Customer Portal](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#add-a-public-ssh-key-to-the-customer-portal). 

### Windows subsystem for Linux (WSL)

You can use various distributions of Linux on Windows 11 to generate SSH keys and connect to your VM. This requires the WSL to be installed on your device; follow the <a href="https://learn.microsoft.com/en-us/windows/wsl/install" target="_blank">official Microsoft guide</a> to do so.

To generate SSH keys via WSL:

1\. Open Windows Command Prompt or PowerShell.

2\. Launch a default Linux distribution inside your current command line by running this command: `wsl.exe`. 
There are multiple ways to run a Linux distribution, you can read more about them in Microsoft's guide to <a href="https://learn.microsoft.com/en-us/windows/wsl/install#ways-to-run-multiple-linux-distributions-with-wsl" target="_blank">ways to run multiple Linux distributions with WSL</a>.

3\. Run the following command to generate a key pair:

```ssh-keygen -t rsa -b 2048
```

4\. You'll be asked to enter the file where the keys should be saved. You can specify a custom location (for example, `.ssh/`) or press **Enter** to save the keys to the default directory. The default directory is `C:\Users\\`.

5\. Press **Enter**.

6\. You’ll be asked to enter a password for the key. You can either create a password or leave the field empty and press **Enter** to create the key without a password.

7\. Confirm the password by entering it one more time or leave the field empty and press **Enter**. You can find your key in the default directory or in the custom location you've specified during the key creation.

8\. The public key will be saved in the .pub file. You need to add this public key to your VM as described in our guide on [adding a public SSH key to the Customer Portal](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#add-a-public-ssh-key-to-the-customer-portal).

### PuTTY 

Follow these instructions to generate SSH keys on Windows 10/11 devices:

1\. Download and install the <a href="https://putty.org/" target="_blank">PuTTY package</a>.

2\. Launch the PuTTYgen app.

3\. Find the “Type of key to generate” parameter and select RSA. 

4\. In the “Number of bits in a generated key” field, set the value to `2048`.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/puttygen-connect.png" alt="Puttygen app with two options selected: RSA type of key and 2048 number of bits" width="80%">

5\. Click **Generate**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/puttygen-generate-key.png" alt="Puttygen app with a generated public key" width="80%">

6\. (Optional) You can enhance the security of your private key by setting up a passphrase, which will be required each time you connect via SSH. To set it up, enter a passphrase in the ‘Key passphrase' field and retype it in the 'Confirm passphrase' field.

7\. While the key is being generated, move the cursor in the “Key” field until the key appears in the field. Click **Save private key** to download the key to your local storage.

<alert-element type="info" title="Info">

If you generated your SSH keys via PuTTYgen or in the Gcore Customer Portal and you want to connect to your instance via PuTTY, you need to convert the keys to the .ppk format as described in our article on <a href="https://gcore.com/docs/cloud/ssh-keys/convert-an-ssh-key-from-pem-to-ppk" target="_blank"> converting an SSH key to a PPK format</a>. 

</alert-element>

</tabset-element>


## Add a public SSH key to the Customer Portal

If you didn’t generate your SSH key via the Gcore Customer Portal, you need to add your public key there. 
To add the key: 

1\. In the Gcore Customer Portal, go to **Cloud** > **SSH keys**.

2\. Select **Add SSH key**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/cloud-ssh-keys-add.png" alt="An SSH keys tab in the Gcore Customer Portal" width="80%">

3\. In the “SSH key Content” field, paste the public key. 

4\. Add a key name and select **Add SSH key**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/add-ssh-key-annotated.png" alt="An SSH keys tab in the Gcore Customer Portal" width="80%">

5\. The key will appear in the list of SSH keys, and you can select this key as an authentication method when creating a new instance. 

<alert-element type="info" title="Info">

After you add a public key, it’ll be automatically shared with all users who belong to the same project. To change the key’s visibility, follow the instructions from our guide on how to [stop sharing SSH keys](https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh#stop-sharing-ssh-keys)

</alert-element>
 
## Manage SSH keys in the Gcore Customer Portal

You can delete a public SSH key from the Gcore Customer Portal, share the key with other users in the same project, or make the key only visible to you. 

### Delete SSH keys

Only the user who created an SSH key or added the public key to the Gcore Customer Portal can delete that key.
To delete the key:

1\. In the Gcore Customer Portal, go to **Cloud** > **SSH keys**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/cloud-ssh-keys.png" alt="An SSH keys tab in the Gcore Customer Portal" width="80%">

2\. Find the SSH key you want to delete and click on the three-dot icon.  

3\. Click **Delete**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/delete-ssh-keys.png" alt="SSH key options menu displaying the Delete button" width="80%">

## Stop sharing SSH keys

After you add or generate an SSH key in the Gcore Customer Portal, the public key is automatically shared with all users in the same project. 

To stop sharing the key and only make it visible to you:

1\. In the Gcore Customer Portal, go to **Cloud** > **SSH keys**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/cloud-ssh-keys.png" alt="An SSH keys tab in the Gcore Customer Portal" width="80%">

2\. Find the SSH key you want to delete and click on the three-dot icon.  

3\. Click **Stop sharing**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/stop-sharing-ssh-keys.png" alt="SSH key options menu displaying the Stop sharing button" width="80%">

You can always start sharing the key again by following the same steps and selecting **Share** from the three-dot icon.
