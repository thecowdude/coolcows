'''
Example code for a simple python Slack Bot running in AWS Lambda

Original code from link below which also contains step by step instructions on how to setup things on Slack and AWS
https://medium.com/glasswall-engineering/how-to-create-a-slack-bot-using-aws-lambda-in-1-hour-1dbc1b6f021c
'''

import json
from urllib import parse as urlparse

def lambda_handler(event, context):

    #print(f"EVENT: {event}")

    message_from_slack = dict(urlparse.parse_qsl(event["body"]))

    print(f"BODY: {message_from_slack}")

    slack_command = message_from_slack["command"]
    try:
        slack_command_parameter = message_from_slack["text"]
    except:
        slack_command_parameter = "NO_COMMAND"
        pass

    print(f"SLACK COMMAND SENT: {slack_command} {slack_command_parameter}")

    message_for_slack = "Hello you sent me the following command: " + slack_command + " " + slack_command_parameter


    response_json = {
                'attachments' : [
                    {
                    'text' : message_for_slack,
                    'callback_id': "slashcommand"
                }
                ]
            }

    return {
        'statusCode': 200,
        'body': json.dumps(response_json)
    }
