import boto3
from datetime import datetime
import calendar
import json
def lambda_handler(event, context):
    personalize_events = boto3.client(service_name='personalize-events')
    now = datetime.now()
    TIMESTAMP = now.timestamp()
    print(event)
    print(TIMESTAMP)
    tracking_id ="XXXX"
    USER_ID = event["SessionKey"]
    session_id = event["InteractionId"]
    EVENT_TYPE = "user interaction"
    ITEM_ID =event["ProductCode"]
    data = {}
    data['itemId'] = ITEM_ID
    json_data = json.dumps(data)
    personalize_events.put_events(
        trackingId = tracking_id,
        userId= USER_ID,
        sessionId = session_id,
        eventList = [{
            'sentAt': TIMESTAMP,
            'eventType': EVENT_TYPE,
            'properties': json.dumps({
            'itemId': ITEM_ID

            })

            }]
    )
