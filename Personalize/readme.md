# Amazon Personalize for building recommendation engine

## Login into AWS account
Login into your AWS account and search for Personalize in the search bar of the landing page

## Create Dataset group
If you have not use personalize before, you can click getting started and first step would be create new dataset group
![Alt Text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.01.17%20PM.png)
Name the data set group 
![Alt Text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.01.43%20PM.png)
### Create user-item interaction dataset and import the data
You can begin by creating the data set for the past user-item interaction. I m keeping the schema default. However you can change it per your data and business requirement.
![Alt Text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.03.03%20PM.png)

For the IAM role for personalize to fetch the data from S3, you can create a new role and grant the permission or use an existing role with the required permission. 

I have uploaded the test data in my example here. You can change the data as per your requirement and your business usecase. But the idea is to have past user-item interaction which is used to train the model. You can upload this to S3 bucket and when you have to import the data and creating the import job, you can specify the bucket in the format : S3://bucketname/retail_v2.csv You can replace it with your file name and bucket name. 
[github](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/retail_v2.csv)

Depending 
![Alt Text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.05.51%20PM.png)


### Create user dataset and import it
For the user dataset, you can click on the create user dataset from the dashboard as in the screenshot above. Provide a name for dataset and create a new schema. For this usercase, I m using the following schema.

{
	"type": "record",
	"name": "Users",
	"namespace": "com.amazonaws.personalize.schema",
	"fields": [
		{
			"name": "USER_ID",
			"type": "string"
		},
		{
			"name": "AGE",
			"type": "int"
		},
		{
			"name": "GENDER",
			"type": "string",
			"categorical": true
		}
	],
	"version": "1.0"
}

For the import job,specify the S3 bucket and IAM role(similar to previous step). The Sample user data which I used is as follows

[github](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/user.csv)

### Create item dataset and import it

For the item dataset,you can create an item data set from the dashboard. Provide a name and schema name. For the schema, I used:
{
	"type": "record",
	"name": "Items",
	"namespace": "com.amazonaws.personalize.schema",
	"fields": [
		{
			"name": "ITEM_ID",
			"type": "string"
		},
		{
			"name": "GENRE",
			"type": "string",
			"categorical": true
		}
	],
	"version": "1.0"
}

You can specify the import job name, IAM role and S3 bucket location. Here is the sample file I used for this exercise:

[github](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/item.csv)

