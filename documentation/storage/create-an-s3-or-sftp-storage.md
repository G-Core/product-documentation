---
title: create-an-s3-or-sftp-storage
displayName: Create storage
published: true
order: 20
toc:
   --1--Create a storage: "create-a-storage"
   --2--S3 storage: "s3"
   --2--SFTP storage: "sftp"
   --1--Storage status indicator: "storage-status-indicator"
pageTitle: S3 and SFTP storage creation | Gcore
pageDescription: Step-by-step instructions on how to create S3 and SFTP storage.
---
# Create an S3 or SFTP storage

## Create a storage

To create a storage, click the **Add new storage** button in the upper-right corner.

Specify storage name and location.

The location name has two parts: storage type (S3 or SFTP) and city/region where the data center is located. SFTP locations are added/removed from the list automatically depending on the amount of free storage space available.

### S3

**Note**: There are several limits for S3 storages:

1.  You can create maximum 1000 buckets. 
2.  You can place maximum 1 mln objects in one bucket. However, we recommend placing no more than 100 thou objects, so storage performance and availability be higher. If you want to place more than 100 thou ones, it would be better to store them in different buckets. 

To create an S3 storage, specify its name and location, and click the **Create** button.

You will see both access and secret key in the next window. Copy and save them since we show the keys only once.

<img src="https://assets.gcore.pro/docs/storage/create-storage/s3-storage-created-10.png" alt="Create a storage">

The created storage will appear in the storage list.

To see the information (location, hostname), click the **Details** button.

If you have forgotten to copy the keys and want to change them, click the **Generate new keys** button.

The **Delete storage** button automatically deletes all the files in your storage.

<img src="https://assets.gcore.pro/docs/storage/create-storage/s3-storage-settings-20.png" alt="Delete storage">

### SFTP

To create an SFTP storage, specify name, location, and preferred authentication method: SSH key or password. Once the storage is created, you will be able to use both.

<img src="https://assets.gcore.pro/docs/storage/create-storage/sftp-storage-created-30.png" alt="create an SFTP storage,">

To see the hostname, click the **Details** button (use port 2200 to connect to the storage).

Password can be set, removed, and updated. To add new keys (up to 5 per storage) or limit access to the uploaded ones go to the SSH keys manager.

<img src="https://assets.gcore.pro/docs/storage/create-storage/sftp-storage-settings-40.png" alt="Dropdown">

To set an alias or regulate the Expires header value, click **Edit**.

Specify a domain name (subdomains are okay too) in the Server alias field, and add the following record to your DNS settings: CNAME *\<server_name>.\<host>*. For example, if your server name is 12345-test, and it is located in Amsterdam, the record would look like *CNAME 12345-test.ams.origin.gcdn.co.*

Expires header can be modified via the "Expires" field. The default value is a year.

<img src="https://assets.gcore.pro/docs/storage/create-storage/sftp-expires-header-50.png" alt="Edit popup">

## Storage status indicator

Circles on the left from the storage IDs are status indicators.

After creation or settings update (adding keys or changing password), it might take time for the requests to get processed. Orange color indicates a processing state, while green one shows that the storage is ready.