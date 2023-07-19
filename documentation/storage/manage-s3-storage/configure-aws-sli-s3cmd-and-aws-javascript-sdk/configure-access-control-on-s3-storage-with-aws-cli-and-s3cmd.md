---
title: configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd
displayName: Set the ACL and Policy
published: true
order: 30
toc:
   --1--What are ACLs: "what-are-acls"
   --1--What are policies: "what-are-policies"
   --1--Configure access via ACLs and policies: "configure-access-via-acls-and-policies"
   --2--Allow an object downloading by ACL: "allow-an-object-downloading-by-acl"
   --2--Allow a bucket listing by ACL: "allow-listing-of-a-bucket-by-acl"
   --2--Allow an object downloading by policy: "allow-an-object-downloading-by-policy"
   --2--Deny access to a bucket (hide a directory) by policy: "deny-access-to-a-bucket-hide-a-directory-by-policy"
   --2--Allow requests from a particular IP by policy: "allow-requests-from-a-particular-ip-by-policy"
   --2--Allow requests from a particular website by policy: "allow-requests-from-a-particular-website-by-policy"
   --2--Grant a user access to a bucket by policy: "grant-a-user-access-to-a-bucket-by-policy"
pageTitle: ACL and Policy Configuration for S3 Storage | Gcore
pageDescription: A detailed guide on configuring Access Control Lists (ACLs) and policies for S3 storage using AWS CLI and S3cmd.
---
# Configure access control on S3 storage with AWS CLI and S3cmd

## What are ACLs?

ACLs, or Access Control Lists, are sets of rules that determine who has access to objects stored in S3 and what actions they are allowed to perform on those objects. Proper configuration of ACLs helps ensure the security of stored data.

**Note**: The storage owner is responsible for configuring ACLs. Use the <a href="https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html#cli-aws-s3api" target="_blank">AWS CLI</a> or <a href="https://s3tools.org/usage" target="_blank">S3cmd documentation commands</a> to manage ACLs for objects in Gcore S3 storage.

ACLs for objects can be configured for a variety of actions, such as:

| AWS CLI              | S3cmd                    | Description                                               |  
|----------------------|--------------------------|-----------------------------------------------------------|
| --public-read        | --acl-public             | Making an object publicly accessible                      |  
| --private            | --acl-private            | Making an object private                                  | 
| --grant-full-control | --acl-grant=full-control | Granting full control over the bucket                     |  
| --grant-read         | --acl-grant=read         | Allowing the listing of objects in the bucket             |   
| --grant-read-acp     | --acl-grant=read_acp     | Allowing the reading of ACLs                              |   
| --grant-write        | --acl-grant=write        | Allowing recording, overwriting, and deleting of objects  |  
   
## What are policies?

Policies are JSON files that provide a more detailed way to control access to objects and buckets. They allow you to specify which actions a specific user or all users are allowed or denied to perform.

The maximum request size in the policy is 20 KB.

**Note**: The storage owner is responsible for configuring policies. Use the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/list_amazons3.html" target="_blank">AWS CLI documentation actions, conditions, and resource types</a> to manage policies for objects in Gcore S3 storage.

## Configure access via ACLs and policies

We've provided examples of ACLs and policies for some common tasks in managing S3 storage.

In all the commands and JSON files, you need to replace the following with your values:

- Replace _sample.jpg_ with your object.
- Replace _my_bucket_ with your bucket.
- Replace _https://s-ed1.cloud.gcore.lu_ with your hostname.

### Allow an object downloading by ACL

To allow all users to download an object, use the following command with the public ACL action *--acl public-read* (AWS CLI) or *--acl public* (S3cmd).

AWS CLI:

```
aws s3api put-bucket-acl --bucket my_bucket --acl public-read --endpoint-url=https://s-ed1.cloud.gcore.lu 
```

S3cmd:

```
s3cmd setacl s3://my_bucket/sample.jpg --acl-public
```

**Note**: This will make the specified object in the bucket publicly available to everyone.

### Allow listing of a bucket by ACL

To allow all users to list objects in a bucket, use the following command with the public ACL action *--grant-read* (AWS CLI) or *--acl-grant=read* (S3cmd).

AWS CLI:

```
aws s3api put-bucket-acl --bucket my_bucket --acl grant-read --endpoint-url=https://s-ed1.cloud.gcore.lu
```

S3cmd:

```
s3cmd setacl s3://my_bucket/sample.jpg --acl-grant=read 
```

**Note**: This will allow users to list the objects in the bucket, but they won't have permission to read or write them.

### Allow an object downloading by policy

To allow all users to download an object:

1\. Create a JSON file with the following policy:

```
{  
"Statement": [   
 {  
"Effect": "Allow",  
"Principal": "*",  
"Action": "s3:GetObject",  
"Resource": "arn:aws:s3:::my_bucket/*"  
  }  
 ]  
}
```

2\. Apply the access policy to the bucket with the following command.

AWS CLI:

```
aws s3api put-bucket-policy --policy file://policy.json --endpoint-url=https://s-ed1.cloud.gcore.lu --bucket my_bucket
```

S3cmd:

```
s3cmd setpolicy policy_name.json s3://my_bucket/
```

As a result, the object in the bucket will be publicly available.

**Note**: This policy allows you to directly access the files, but it doesn't allow you to list the files in the bucket.

### Deny access to a bucket (hide a directory) by policy

To deny all users access to the "s3:GetObject" operation on a specific directory in a bucket while still allowing access to the higher-level bucket:

1\. Create a JSON file with the following policy:

```
{  
"Statement": [   
 {   
"Effect": "Allow",  
"Principal": "*",  
"Action": "s3:GetObject",  
"Resource": "arn:aws:s3:::my_bucket/*"   
 },  
 {   
"Effect": "Deny",  
"Principal": "*",  
"Action": "s3:GetObject",  
"Resource": "arn:aws:s3:::my_bucket/secret/*"   
  }  
 ]  
}
```

**Note**: Replace _arn:aws:s3:::my_bucket/secret/*_ with the path to the directory you want to hide and _arn:aws:s3:::my_bucket/*_ with the path to the higher-level bucket.

2\. Apply the policy to the bucket with the following command.

AWS CLI:

```
aws s3api put-bucket-policy --policy file://policy.json --endpoint-url=https://s-ed1.cloud.gcore.lu --bucket my_bucket
```

S3cmd:

```
s3cmd setpolicy policy_name.json s3://my_bucket/
```

### Allow requests from a particular IP by policy

To allow requests to the storage bucket from a specified IP address:

1\. Create a JSON file with the following policy:

```
{  
"Statement":   
 [  
  {  
"Sid": "IPAllow",  
"Effect": "Allow",  
"Principal": "*",  
"Action": "s3:*",  
"Resource": [  
"arn:aws:s3:::",  
"arn:aws:s3:::/*"  
            ],  
"Condition":   
    {  
"IpAddress": {"aws:SourceIp": "10.0.0.0/24"}  
    }  
  }  
 ]  
}
```

**Note**: Replace *10.0.0.0/24* with your desired IP address.

2\. Apply the policy to the bucket with the following command.

AWS CLI:

```
aws s3api put-bucket-policy --policy file://policy.json --endpoint-url=https://s-ed1.cloud.gcore.lu --bucket my_bucket
```

S3cmd:

```
s3cmd setpolicy policy_name.json s3://my_bucket/
```

### Allow requests from a particular website by policy

To allow referrals to the storage bucket from specified websites:

1\. Create a JSON file with the following policy:

```
{  
"Statement":  
 [  
  {  
"Sid":"Allow get requests originating from www.example.com and example.com.",  
"Effect":"Allow",  
"Principal":"*",  
"Action":["s3:GetObject","s3:GetObjectVersion"],  
"Resource":"arn:aws:s3:::/*",  
"Condition":  
     {  
"StringLike":{"aws:Referer":["http://www.example.com/*","http://example.com/*"]}  
     }  
   }  
 ]  
}
```

**Note**: Replace *http://www.example.com/* and *http://example.com/* with your desired websites.

2\. Apply the policy to the bucket with the following command.

AWS CLI:

```
aws s3api put-bucket-policy --policy file://policy.json --endpoint-url=https://s-ed1.cloud.gcore.lu --bucket my_bucket
```

S3cmd:

```
s3cmd setpolicy policy_name.json s3://my_bucket/
```

### Grant a user access to a bucket by policy 

To grant a user access to a bucket:

1\. Create a JSON file with the following policy:

```
{    
"Statement":[   
  {   
"Effect":"Allow",   
"Principal": {"AWS":["arn:aws:iam:::user/1234-test"]},   
"Action":["s3:GetObject","s3:ListBucket"],   
"Resource":["arn:aws:s3:::my_bucket/*", "arn:aws:s3:::my_bucket"]   
  }   
 ]   
} 
```

**Note**: Replace *1234-test* with the actual name of your storage in your account, and *arn:aws:s3:::my_bucket* with the actual name of your bucket.

2\. Apply the policy to the bucket with the following command.

AWS CLI:

```
aws s3api put-bucket-policy --policy file://policy.json --endpoint-url=https://s-ed1.cloud.gcore.lu --bucket my_bucket
```

S3cmd:

```
s3cmd setpolicy policy_name.json s3://my_bucket/
```