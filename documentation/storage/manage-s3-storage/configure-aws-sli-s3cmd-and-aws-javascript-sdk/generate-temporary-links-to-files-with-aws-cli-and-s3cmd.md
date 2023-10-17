---
title: generate-temporary-links-to-files-with-aws-cli-and-s3cmd
displayName: Generate a presigned URL
published: true
order: 40
toc:
   --1--What is a presigned URL?: "what-is-a-presigned-url"
   --1--Generate a presigned URL: "generate-a-presigned-url"
   --2--via AWS CLI: "generate-links-in-aws-cli"
   --2--via S3cmd: "generate-links-in-s3cmd"
pageTitle: Guide on how to generate presigned URL | Gcore
pageDescription: Guide about presigned URLs providing temporary access to files and their setup.  
---
# Generate temporary links to files with AWS CLI and S3cmd                   

## What is a presigned URL?

A presigned URL is a temporary link used to access a private file in the storage. Such links can be generated only by those who have <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">access keys</a> (Access key and Secret key) from the storage. As a rule, this is a storage owner.

This is how you work with the presigned URLs:

1\. A storage owner sets the link expiry date and generates a presigned URL.

2\. The owner sends the generated link to the users for whom he/she wants to make the file accessible.

3\. The users receive a link as follows:

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/generate-a-presigned-url/link-explanation-10.png" alt="link ">

4\. After that, users will be able to view and download the file during the link lifespan that has been set by the owner. 

5\. When the link expires, the access will be revoked. When clicking the link, users will see the "AccessDenied" error.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/generate-a-presigned-url/example-temp-link-20.png" alt="AccessDenied" width="80%">

A presigned URL doesn't require user's authentication. This means that everyone with a valid temporary link can access the file. For example, if you send such a link to a user who then forwards it to another person, that person will also be able to view and download files.

To protect the temporary link, you can restrict access by IP in the Access Policy settings. For the appropriate code, refer to the following article: <a href="https://gcore.com/docs/storage/manage-s3-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd" target="_blank">Configure ACL and Policy for S3 storage</a>.

## Generate a presigned URL

We have prepared a guide to generate a presigned URL for two storage management utilities: AWS CLI and S3cmd.

### Generate links in AWS CLI

1\. Open a command-line tool and navigate to the AWS directory.

2\. Paste the command below into AWS and replace the values with your own ones:

```
aws presign s3://example-bucket/image.jpg --expires in 60480 --endpoint-url s-dt2.cloud.gcore.lu
```

where:

- *example-bucket* — the name of the bucket that hosts the file,
- *image.jpg* — the file you want to share,
- *60480* — link lifespan in seconds, the maximum is 7 days,
- *s-dt2.cloud.gcore.lu* — the hostname of your storage that can be found in the "Details" of the storage in your control panel.

3\. Press "Enter". 

Done. The command will generate a link. Copy it and send it to the user you want to share access with.

### Generate links in S3cmd

1\. Open a command-line tool and navigate to the S3cmd directory.

2\. Paste the command below into S3cmd and replace the values with your own ones: 

```
s3cmd signurl s3://example-bucket/image.jpg 1657457538
```

where:

- *example-bucket* — the name of the bucket that hosts the file,
- *image.jpg* — the file you want to share,
- *1657457538* — link expiry time in the Timestamp format, use the <a href="https://epochconverter.com" target="_blank">converter</a> to convert time formats.

You can also set the link expiry date by running the Echo command as an alternative to Timestamp. For example, you can set a lifespan of 7 days by entering the following string:

```
s3cmd signurl s3://example-bucket/image.jpg $(echo "`date +%s` + 3600 * 24 * 7" | bc)
```
where:

- *example-bucket* — the name of the bucket that hosts the file,
- *image.jpg* — the file you want to share,
- *$(echo "`date +%s` + 3600 * 24 * 7 " | bc)* — 7-day offset of the link expiry time.

3\. Press "Enter".

Done. The command will generate a link. Copy it and send it to the user you want to share access with.