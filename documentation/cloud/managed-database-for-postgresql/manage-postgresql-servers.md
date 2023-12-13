---
title: manage-postgresql-servers
displayName:  Manage PostgreSQL servers
published: true
order: 10
toc:
   --1--Create a server: "create-a-server"
   --2--Before creation: "before-you-begin"
   --2--Create: "create-a-server"
   --1--Get credentials: "get-your-credentials"
   --1--Upgrade version: "upgrade-the-postgresql-version"
   --1--Delete: "delete-a-server"
   --1--Connect to a PostgreSQL server: "connect-to-a-postgresql-server"
   --2--Before: "before-the-beginning"
   --2--psql client: "connect-using-the-psql-client"
   --2--pgAdmin: "connect-using-pgadmin"
pageTitle: A Guide on how to Manage a PostgreSQL Server | Gcore
pageDescription: This guide describes how to manage (create, get credentials, update version, connect and delete) a PostgreSQL server.
---
#  Manage a PostgreSQL server 

## Create a server

This guide describes how to create a PostgreSQL server.

### Before you begin 

Before you begin, make sure you have enough quotas to create a PostgreSQL cluster. 

1\. Go to **Cloud Management**, then **Quotas Viewer** and select the region.
 
<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-10.png" alt="manage postgresql">

2\. On the **Database Service** tab, select the number of PostgreSQL clusters you need and specify the reason in the field on the right.

3\. Click **Send request**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-20.png" alt="manage postgresql send quotas request">

Your request will be processed within fifteen minutes and the number of quotas will be increased. 

### Create a server

1\. In the Cloud menu, choose the Database for PostgreSQL tab and click **Create PostgreSQL server**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-30.png" alt="manage postgresql create a server">

2\. Choose the region where you want to host your PostgreSQL server.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-40.png" alt="manage postgresql choose region">

3\. Choose the appropriate <a href="https://gcore.com/docs/cloud/managed-database-for-postgresql#supported-versions" target="_blank">PostgreSQL version</a>.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-50.png" alt="manage postgresql select version">

4\. In **Compute**, select the server flavor. Optionally, you can set your own settings via text mode to enter specific database management system (DBMS) settings in the window that opens.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-60.png" alt="manage postgresql select server flavor">

5\. In **Storage**, choose the volume type and size. 

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-70.png" alt="manage postgresql choose volume">

6\. In **PG configuration**, select the appropriate connection pooler:

- Session: This is the standard database connection mode that does not require additional coding. It offers a straightforward way to interact with the database without the overhead of the connection management. However, it does not load the database server with re-creating connections.

- Transactional: This mode is more efficient but requires work with locks. It comes with some limitations:
    - Prepared statements cannot be used in this mode.
    - The use of the SET statement, temporary tables, and locks must be transaction-scoped. This means that these resources are confined to the duration of a specific database transaction.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-80.png" alt="manage postgresql configure pg">

7\. (optionally) Switch on the **Enable High availability** toggle to deploy three replicas with the same configuration to ensure that your database remains accessible even in the event of a server failure. If you turn on this feature, select the appropriate replication mode:

- Asynchronous: In asynchronous replication, servers work independently. The primary database sends the changes to the replicas and does not wait for confirmation that the changes have been applied. This mode is suitable for scenarios where data consistency with some level of delay is acceptable, though high performance is crucial.

- Synchronous: In synchronous replication, the primary database must wait for confirmation that the changes have been applied in the replica databases. The changes are replicated in real time or near-real time. It provides full protection against data loss but may have lower performance.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-90.png" alt="manage postgresql manage replication mode">

You can enable or disable this feature later.

8\. In **Network settings**, configure the network interface.

Choose Public network and configure the Access control list to limit the access to your server to the specified IP addresses.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-100.png" alt="manage postgresql manage network interface">

**Note**: If you add *0.0.0.0/0*, you will allow unrestricted access to all IP addresses from the Internet. We strongly recommend using this setting only temporarily and exclusively on test servers without any sensitive data.

9\. In **Authentication**, add your username.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-110-v2.png" alt="manage postgresql manage authentication">

10\. In **Server details**, specify the server name and database name.

**Note**: The database size limit is 100 GB. This limit is for the beta stage only. If you need a more extensive database size during beta—please get in touch with [support](mailto:support@gcore.com).


<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-120.png" alt="manage postgresql specify server details">

11\. Click **Create PostgreSQL server** in the window on the left-hand side.

The server will be created in a few minutes.

## Get your credentials

This guide explains how to obtain the password to start using your Postgres server and how to reset it if you forget it.

1\. Go to the **Database for PostgreSQL** tab and select the server you need.

2\. Click **Generate credentials**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-130.jpg" alt="manage postgresql generate credentials">

3\. Copy and save the password now. Once you close the window you will not be able to recover it. 

**Note**: If you forget your password, you can only reset it. A new password will be generated, and the previous one will be deactivated.

4\. Click **OK**.

## Upgrade the PostgreSQL version

If your current PostgreSQL version is not the latest one, you can upgrade it.

1\. Go to the **Database for PostgreSQL** tab and select the server you need.

2\. On the **Overview** tab, click **Update** in the General info section.

**Note**: if you use the latest version, the button will be absent. 

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-140.png" alt="manage postgresql update version">

3\. Select the version you need from the drop-down list and click **Update**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-145.png" alt="manage postgresql update version pop up" width="70%">

## Delete a server

1\. Go to the **Database for PostgreSQL** tab and select the server you want to delete.

2\. Click **Delete server**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-150.jpg" alt="manage postgresql delete server">

3\. In the new window, type in *Delete* and click the **Delete server** button.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-160-v2.png" alt="manage postgresql confirm deletion" width="70%">

## Connect to a PostgreSQL server 

This guide explains what tools you can use to access your PostgreSQL server and how to connect using psql and pgAdmin.

### Before the beginning

Before you connect to your PostgreSQL server, make sure to do the following:

1\. Collect the connection details:

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-170.png" alt="manage postgresql connection details">

- Endpoint. You can find it in the “Connection details”
- Username. You can find it in the “Connection detais”
- Port. You can find it by copying the connection strings in the “Connection details”
- Password. You should have got it separately after creating a server. If you forgot your password, <a href="https://gcore.com/docs/cloud/managed-database-for-postgresql/manage-postgresql-servers#get-your-credentials" target="_blank">reset it</a>. 

2\. Make sure your client computer is in the access control list of the PostgreSQL server. It means that the external IP address of PC which is trying to connect to PostgreSQL should be in allowlist (ACL).

3\. Determine what tool you will use to connect to your server. 

- psql (Postgres Terminal Monitor): The command-line PostgreSQL client, that allows you to enter, edit, and execute SQL commands directly from your terminal or command prompt.

- Native Frontend Tools (e.g., pgaccess, pgAdmin, ApplixWare): They provide graphical user interfaces (GUIs) for PostgreSQL database management. These tools offer a more user-friendly and visual way to create and manipulate databases.

- Programming Languages (e.g., Perl, Tcl): These languages have supported interfaces for PostgreSQL. You can use these languages to write scripts or applications that connect to PostgreSQL databases programmatically. Some of the languages have convenient and powerful GUI toolkits which can help you construct custom applications. For example, pgaccess, mentioned above, is one of such applications written in Tcl/Tk. 

- C Programming with LIBPQ: If you're a C programmer, you can use the LIBPQ subroutine library to write C programs that connect to PostgreSQL databases. This allows you to submit SQL commands from your C program, retrieve results, and manage database interactions programmatically. The detailed information on using LIBPQ can be found in "<a href="https://www.postgresql.org/docs/7.3/programmer.html" target="_blank">The PostgreSQL Programmer's Guide</a>."

### Connect using the psql client

1\. <a href="https://www.postgresql.org/download/" target="_blank">Download the PostgreSQL client</a> from the PostgreSQL website for your operating system in order to install psql.

2\. Start psql by typing the following command in your terminal:

```
psql -h hostname -p port -d dbname -U username
```

Replace ```hostname```, ```port```, ```dbname```, and ```username``` with your custom values.

3\. Enter the password and press **Enter**.

For more details, refer to the <a href="https://www.postgresql.org/docs/" target="_blank">PostgreSQL official documentation</a>.

### Connect using pgAdmin

1\. <a href="https://www.pgadmin.org/" target="_blank">Download</a> and install pgAdmin to your client computer.

2\. Launch pgAdmin.

3\. On the **Dashboard** tab, choose **Add New Server**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-180.png" alt="manage postgresql connect phpmyadmin 1">

4\. In the Create - Server dialog box that appears, type the server’s name in the **General** tab and click **Save**.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-190.png" alt="manage postgresql connect phpmyadmin 2">

5\. Go to the **Connection** tab and enter the host (endpoint,) port, username, and password in the relevant fields.

<img src="https://assets.gcore.pro/docs/cloud/database-for-postgresql/manage-postgresql-servers/manage-postgresql-190.png" alt="manage postgresql connect phpmyadmin 3">

6\. Click **Save**. 

7\. Locate the server you’ve added in the left-side menu and click it to access. For more details, refer to the <a href="https://www.pgadmin.org/docs/" target="_blank">pgAdmin official documentation</a>.