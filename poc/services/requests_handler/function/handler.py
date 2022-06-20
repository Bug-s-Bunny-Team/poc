import json

from models import Request


class RequestsHandler:
    def handle_request(self, request: Request):
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'hello from RequestsHandler',
            }),
        }
