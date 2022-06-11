import json


def lambda_handler(event, context):
    message = event.get('message')
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message,
        }),
    }
