# Amazon Personalize for building recommendation engine
Amazon Personalize is a machine learning service that makes it easy for developers to create individualized recommendations for customers using their applications.Delivering personalization to individuals at scale requires a combination of the right data and the right technology. The algorithms used by Amazon Personalize are designed to overcome common problems when creating custom recommendations – such as new users with no data, popularity biases, and evolving intent of users – to deliver high-quality recommendations that respond to specific needs, preferences, and behavior of your users.Timing is everything. If a customer has spent time browsing products on your site, you need to understand what they're looking for and respond with the right recommendations before they move on to another site. Amazon Personalize can blend real-time user activity data with existing user profile and product information to identify the right product recommendations for your users at that moment.Amazon Personalize enables companies to provide a cohesive and unique experience for every user across all channels and devices. With Amazon Personalize, you can generate a custom personalization model in just a few clicks. Amazon Personalize automates and accelerates the complex machine learning tasks required to build, train, tune, and deploy a personalization model – so you can start delivering relevant experiences for your users quickly.
# About this usecase
I m building recommendation engine for retail in this exercise. I have created some sample data(dummy) with grocery store in mind. You can try this example out with the sample data I have used or even better use your own data. I have provided the steps as if you will be doing it through console, but feel free to use API/CLI as per your wish. 

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
[user item interaction](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/retail_v2.csv)

Once the import job is created you can see the following dashboard: 
![Alt Text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.05.51%20PM.png)


### Create user dataset and import it
For the user dataset, you can click on the create user dataset from the dashboard as in the screenshot above. Provide a name for dataset and create a new schema. For this usercase, I m using the following schema.
```
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
```
For the import job,specify the S3 bucket and IAM role(similar to previous step). The Sample user data which I used is as follows

[user csv](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/user.csv)

### Create item dataset and import it

For the item dataset,you can create an item data set from the dashboard. Provide a name and schema name. For the schema, I used:
```
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
```

You can specify the import job name, IAM role and S3 bucket location. Here is the sample file I used for this exercise:

[item csv](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/TestData/item.csv)

## Create Solution
On the dashboard, you can click create solution once the data import is completed.
Provide a name for the solution. For the recipe, specify **aws-hrnn-metadata** I m keeping the hyperparameter to default for this exercise. Creation of solution can take several hours since personalize is actually creating a model per the data you provided. 
![Alt text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%208.41.51%20PM.png)

## Create Campaign
Once the solution creation is done, you can now use the model created for providing recommendation 
![Alt text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%209.21.47%20PM.png)

##### Campaign ARN Info
You will see the campaign ARN. Please note it and keep it handy
**Campaign ARN Info**
arn:aws:personalize:region:accountid:campaign/retailcampaign

##### Test the Campaign
You can put in the user id and get recommendation.

![Alt text](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/Screen%20Shot%202020-02-02%20at%209.29.12%20PM.png)

**Our recommendation engine is now ready!**

## Get Recommendation API
Having a central core recommendation engine exposing it via an API so all the systems and channels can call the same API to get recommendation is very powerful mechanism. So Let's get started!

### Create Lambda function to get recommendation
Create a Lambda function in python and ensure the IAM role has the permission to invoke personalize API.
The code snippet can be found here. Please make sure to replace the campaign ARN with your own ARN : 
[get recommendation python code](https://github.com/neelamkoshiya/DigitalCustomerEngagementonAWS/blob/master/Images/testrecommendation.py)

### Test Lambda function
```
{
  "userId": "neelam",
  "itemId": "starbucks"
}
```
You can use existing userId which you had the user.csv file or any other. Sometimes you want recommendation for "guest" or "anonymous" user. The recommendation api will respond with recommendation for any of the cases.

Note: The if else loop is to make sure the recommendated items are unique

### Create API

Now that our lambda function is ready. You can create a trigger to the lambda function and select API Gateway






