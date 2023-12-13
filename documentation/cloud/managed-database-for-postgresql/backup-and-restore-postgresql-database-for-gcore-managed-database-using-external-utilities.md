---
title: backup-and-restore-postgresql-database-for-gcore-managed-database-for-postgresql-using-external-utilities
displayName: Backup and restore
published: true
order: 20
toc:
   --1--1. Install external utilities: "1-install-external-utilities"
   --1--2. Get credentials: "2-get-your-credentials"
   --1--3. Back up databases: "3-back-up-databases"
   --2--Specific database: "back-up-a-specific-database"
   --2--All databases: "back-up-all-databases" 
   --1--4. Restore databases: "4-restore-databases"
pageTitle: PostgreSQL Database Backup and Restore with Gcore Managed Database | Gcore
pageDescription: Learn how to secure your data with easy PostgreSQL backup and restore on Gcore Managed Database using pg_dump and pg_restore tools.
---
# Backup and restore PostgreSQL database for Managed Database for PostgreSQL using external utilities 

This guide will explain how to backup and restore PostgreSQL databases with the ```pg_dump``` (```pg_dumpall```) and ```pg_restore``` tools.

To protect yourself against data loss, we recommend frequently backing up the databases you manage with <a href="https://gcore.com/docs/cloud/managed-database-for-postgresql" target="_blank">Gcore Managed Database for PostgreSQL</a>.

## 1. Install external utilities

Install backup and restore utilities on your virtual or local server. Below are guides on how to do so for Ubuntu, CentOS, and Windows.

**Note**: You must have root rights to run the commands successfully.  

<expandable-element title="Ubuntu 22.04">

1\. Access your virtual server.

2\. Download the latest available updates and upgrade ```apt```:

```
$ sudo  apt update && sudo apt upgrade
```

3\. To install ``` pg_dump``` and ```pg_restore``` tools, install the Postgres package, which includes them:

```
$ sudo apt install postgresql postgresql-contrib
```
</expandable-element>

<expandable-element title="CentOS 7">

1\. Access your virtual server.

2\. Install the PostgreSQL package:

```
$ sudo yum install postgresql-server
```

The package contains all required tools.

</expandable-element>

<expandable-element title="Windows">

1\. Download the <a href="https://www.enterprisedb.com/downloads/postgres-postgresql-downloads" target="_blank">installer of the relevant PostgreSQL version</a>.

2\. Run the installation process.

</expandable-element>

## 2. Get your credentials

To launch backup and restore tools, you need credentials (``username``, ```password```, ```port```, and ```dbname```) to connect to the Gcore Managed Database server, where databases are stored. You can find credentials in the customer portal, with instructions available in <a href="https://gcore.com/docs/cloud/managed-database-for-postgresql/manage-postgresql-servers#get-your-credentials" target="_blank">our dedicated guide</a>. 

## 3. Back up databases

### Back up a specific database

Use one of the following commands depending on your choice of backup format:

- **Default SQL format**: ```$ pg_dump -U username -W -h hostname -d database_name > database_name.sql``` 
- **TAR format**: ```$ pg_dump -F t -U username -W -h hostname -d database_name > backup_file.tar```
- **Custom format**: ```$ pg_dump -F c -U username -W -h hostname -d database_name > backup_file.dump```
- **Directory format**: ```$ pg_dump -F d -U username -W -h hostname -d database_name -f backup_dir```

Instead of ```username```, ```hostname```, and ```database_name```, enter custom values, which you can access <a href="https://gcore.com/docs/cloud/managed-database-for-postgresql/manage-postgresql-servers#get-your-credentials" target="_blank">using our guide</a>. For ```backup_file``` or ```backup_dir```, specify the relevant name for the backup file or directory.

Below are some other details for the commands:

- ```-W``` prompts the password before connecting to the PostgreSQL server
- ```-F``` specifies the output format of the backup and can be followed by the following flags:
   - ```c``` for custom format
   - ```d``` for directory format
   - ```t``` for tar

### Back up all databases

Run the command:

```
$ pg_dumpall -U username -W -h hostname > all_pg.sql
```

Where: 

- ```all_pg.sql``` is the output backup name
- ```username``` is your username from the customer portal
- ```hostname``` is your hostname from the customer portal

## 4. Restore databases

Run the command: 

```
$ pg_restore -U username -W -h hostname -d database_name < backup_file.tar
```

Where: 

- ```username``` is your username from the customer portal
- ```hostname``` is your hostname from the customer portal  
- ```database_name``` is your database name from the customer portal
- ```backup_file.tar``` is the file or directory with your backup