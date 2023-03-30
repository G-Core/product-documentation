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
---
  
                    

What is a presigned URL?
------------------------

A presigned URL is a temporary link used to access a private file in the storage. Such links can be generated only by those who have [access keys](https://gcorelabs.com/support/articles/360002072257/#h_01G1110V67GGHCB9Z6BB30HK35) (Access key and Secret key) from the storage. As a rule, this is a storage owner.

This is how you work with the presigned URLs:

1\. A storage owner sets the link expiry date and generates a presigned URL.

2\. The owner sends the generated link to the users for whom he/she wants to make the file accessible.

3\. The users receive a link as follows:

<img src="https://support.gcore.com/hc/article_attachments/7595319666705/Rectangle_969.png" alt="Rectangle_969.png">

4\. After that, users will be able to view and download the file during the link lifespan that has been set by the owner. 

5\. When the link expires, the access will be revoked. When clicking the link, users will see the "AccessDenied" error.

<img src="https://support.gcore.com/hc/article_attachments/7595341367953/image_1875.png" alt="image_1875.png">

A presigned URL doesn't require user's authentication. This means that everyone with a valid temporary link can access the file. For example, if you send such a link to a user who then forwards it to another person, that person will also be able to view and download files.

To protect the temporary link, you can restrict access by IP in the Access Policy settings. For the appropriate code, refer to the following article: [Configure ACL and Policy for S3 storage](https://gcorelabs.com/support/articles/4405490613649/#h_01F2NXTZDJ35E4NF8J41E976YS).

Generate a presigned URL
------------------------

We have prepared a guide to generate a presigned URL for two storage management utilities: AWS CLI and S3cmd.

### Generate links in AWS CLI

1\. Open a command-line tool and navigate to the AWS directory.

2\. Paste the command below into AWS and replace the values with your own ones:

aws presign s3://example-bucket/image.jpg --expires in 60480 --endpoint-url s-dt2.cloud.gcore.lu

where:

*   _example-bucket_ — the name of the bucket that hosts the file,
*   _image.jpg_ — the file you want to share,
*   _60480_ — link lifespan in seconds, the maximum is 7 days,
*   _s-dt2.cloud.gcore.lu_ — the hostname of your storage that can be found in the "Details" of the storage in your control panel.

3\. Press "Enter". 

Done. The command will generate a link. Copy it and send it to the user you want to share access with.

### Generate links in S3cmd

1\. Open a command-line tool and navigate to the S3cmd directory.

2\. Paste the command below into S3cmd and replace the values with your own ones: 

s3cmd signurl s3://example-bucket/image.jpg 1657457538

where:

*   _example-bucket_ — the name of the bucket that hosts the file,
*   _image.jpg_ — the file you want to share,
*   _1657457538 —_ link expiry time in the Timestamp format, use the [converter](https://www.epochconverter.com/) to convert time formats.

You can also set the link expiry date by running the Echo command as an alternative to Timestamp. For example, you can set a lifespan of 7 days by entering the following string:

s3cmd signurl s3://example-bucket/image.jpg $(echo "\`date +%s\` + 3600 \* 24 \* 7" | bc)

where:

*   _example-bucket_ — the name of the bucket that hosts the file,
*   _image.jpg_ — the file you want to share,
*   _$(echo "\`date +%s\` + 3600 \* 24 \* 7 " | bc)_ — 7-day offset of the link expiry time.

3\. Press "Enter".

Done. The command will generate a link. Copy it and send it to the user you want to share access with.