from __future__ import print_function
import json

def read(event, context):
    print("Query string: {}".format(str(event['queryStringParameters'])))
    body = {"hello": "world"}
    return {
             "statusCode": 200,
             "body": json.dumps(body)
         }
