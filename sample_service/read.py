from __future__ import print_function
import json
import os

def read(event, context):
    print("Query string: {}".format(str(event['queryStringParameters'])))
    body = {"hello": "world"}
    print("SAMPLE_ENV: {}".format(os.environ['SAMPLE_ENV']))
    return {
             "statusCode": 200,
             "body": json.dumps(body)
         }
