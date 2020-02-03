import boto3
def lambda_handler(event, context):
    personalizeRt = boto3.client('personalize-runtime')
    ItemId = event["itemId"]
    UserId = event["userId"]
    response = personalizeRt.get_recommendations(
        campaignArn = "arn:aws:personalize:us-west-2:340280328827:campaign/retailcampaign",
        itemId =ItemId,
        userId =UserId,
        numResults=6
        )
    newlist=[]
    count=0
    for item in response['itemList']:
        if item['itemId'] ==ItemId:
            print('input item')
            print(item['itemId'])
            continue
        else:
            count += 1
            if count < 6:
                print('new item')
                print(item['itemId'])
                newlist.append(item)
            else:
                continue
