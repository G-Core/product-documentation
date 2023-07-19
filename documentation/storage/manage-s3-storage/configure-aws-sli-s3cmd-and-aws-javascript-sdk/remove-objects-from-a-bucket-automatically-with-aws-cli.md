---
title: remove-objects-from-a-bucket-automatically-with-aws-cli
displayName: Set the Lifecycle policy
published: true
order: 20
toc:
   --1--What is a lifecycle policy: "what-is-a-lifecycle-policy"
   --1--Lifecycle policy logic: "lifecycle-policy-logic"
   --1--Lifecycle configuration elements: "gcore-lifecycle-configuration-elements"
   --1--Manage with AWS CLI: "manage-a-lifecycle-policy-with-aws-cli"
   --2--add: "add-a-lifecycle-policy-to-your-bucket"
   --2--delete: "delete-a-lifecycle-policy"
   --1--Manage with the UI (for S3 in Luxembourg): "manage-a-lifecycle-policy-with-the-ui"
pageTitle: Managing lifecycle policies for Gcore storage with AWS CLI and UI | Gcore
pageDescription: A tutorial on adding, checking, and deleting lifecycle policies in Gcore storage using AWS CLI helps automatically delete objects after a certain period.
---

# Remove objects from a bucket automatically with AWS CLI

## What is a lifecycle policy?

A lifecycle policy is a file written in XML (or JSON) format that contains rules for automating the movement of objects from one stage of their lifecycle to another. The movement is typically based on the "age" and size of the object, as well as other parameters. You can find more information on the different parameters in the <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html" target="_blank">Amazon documentation</a>.

There are several ways to utilize a Lifecycle Policy. Gcore supports a lifecycle policy, which allows you to set an expiration time for an object and automatically remove it from the bucket once the expiration time is reached.

## Lifecycle policy logic

The process of removing objects starts around midnight UTC.

Three lifecycle states determine the removal time for an object:

**1\. A lifecycle policy is set before the objects are uploaded.** For example, if the lifecycle policy is set for 1 day and you upload your object on January 2nd, it will be removed on January 4th.

**2\. A lifecycle policy is set after the objects are uploaded.** If you upload an object on January 1st (at any time) and then set a lifecycle policy with a file expiration time of 1 day, the file will be deleted on January 3rd.

**3\. A lifecycle policy is removed.** If you delete the lifecycle policy from the bucket, the object it was applied to will not be removed.

## Gcore lifecycle configuration elements

Here is an example of a completed XML file with the lifecycle policy:

```
<LifecycleConfiguration>  
 <Rule>  
  <ID>...</ID>  
  <Prefix/>  
  <Status>Enabled</Status>  
  <Expiration>  
   <Days>...</Days>  
  </Expiration>  
</Rule>  
</LifecycleConfiguration>
```

- **`<Rule>...</Rule>.`** This section includes all the settings below.
- **`<ID>...</ID>.`** Specify a unique identifier for the rule. The ID can be up to 255 characters long and include numbers, Latin letters, and underscores.
- **`<Prefix/>.`** Leave the tag empty if you want to apply the rule to the entire bucket or specify the folder's name.
- **`<Status>...</Status>.`** Specify either "Enabled" or "Disabled". If a rule is in the "Disabled" status, no actions specified in the rule will be performed.
- **`<Expiration><Days>...</Days></Expiration>.`** Specify the days you want the object to be kept in your bucket in the "Expiration" section.

## Manage a lifecycle policy with AWS CLI

### Add a lifecycle policy to your bucket

1\. Create an XML file:

```
<LifecycleConfiguration>  
 <Rule>  
  <ID>one_day</ID>  
  <Prefix/>  
  <Status>Enabled</Status>  
  <Expiration>  
   <Days>1</Days>  
  </Expiration>  
 </Rule>  
</LifecycleConfiguration>
```

Where:

- `ID` is `one_day`.
- The rule is applied to the entire bucket (`<Prefix/>`).
- The rule is active (status is `Enabled`).
- The file expiration time is 1 day.
    

2\. Convert the XML file to the JSON format because the AWS CLI does not support the XML format. Your policy will look like this:

```
{  
 "Rules": [  
 {  
 "ID": "one_day",   
 "Prefix": "",  
 "Status": "Enabled",   
 "Expiration": {  
 "Days": 1  
   }  
  }  
 ]  
}
```

**Note**: The following header value (`"Prefix": ""`) applies the Lifecycle Configuration to the entire bucket. Specify the folder name if you need to apply the policy to a specific folder in the bucket. For example, if the objects are in the `deleteme` folder, the value will be `"Prefix": "deleteme /"`.

3\. Save the file as *lifecycle.json*.

4\. Start the AWS CLI from the directory with the *lifecycle.json* file and run the following command:

```
aws s3api put-bucket-lifecycle --bucket my_bucket --lifecycle-configuration file://lifecycle.json --endpoint-url=https://s-ed1.cloud.gcore.lu 
```

Replace:

- `my_bucket` name in the example with your bucket name.
- `https://s-ed1.cloud.gcore.lu` with your storage endpoint. To choose the correct value for this parameter, use the "<a href="https://gcore.com/docs/storage/manage-s3-storage/s3-service-urls-and-default-region-names" target="_blank">S3 service URLs and default region names</a>" guide.

5\. Check if the policy was uploaded correctly with the following command:

```
aws s3api get-bucket-lifecycle-configuration --bucket my_bucket --endpoint-url=https://s-ed1.cloud.gcore.lu 
```

Replace:

*   `my_bucket` name in the example with your bucket name.
*   `https://s-ed1.cloud.gcore.lu` with your storage endpoint. To choose the correct value for this parameter, use the "<a href="https://gcore.com/docs/storage/manage-s3-storage/s3-service-urls-and-default-region-names" target="_blank">S3 service URLs and default region names</a>" guide.

In the response, you should receive the uploaded JSON file.

### Delete a lifecycle policy 

To delete the policy from the bucket, use the following command:

```
aws s3api delete-bucket-lifecycle --bucket my-bucket --endpoint-url=https://s-ed1.cloud.gcore.lu
```

Replace:

- `my_bucket` name in the example with your bucket name.
- `https://s-ed1.cloud.gcore.lu` with your storage endpoint. To choose the correct value for this parameter, use the "<a href="https://gcore.com/docs/storage/manage-s3-storage/s3-service-urls-and-default-region-names" target="_blank">S3 service URLs and default region names</a>" guide.

## Manage a lifecycle policy with the UI

If you are using S3 storage in Luxembourg, you can manage your lifecycle policy for buckets in the control panel according to the "<a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#add-lifecycle-policy-available-for-s3-in-luxembourg-only">Manage buckets via the control panel</a>" guide.
