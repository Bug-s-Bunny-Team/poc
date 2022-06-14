from .models import BasicScoringService, SQSEventAdapter, S3OutputStrategy
import json

def lambda_handler(event, context):
    try:
        scoringService = BasicScoringService(SQSEventAdapter(), S3OutputStrategy())
        scoringService.score(event)
        return 'Success'
    except Exception as e:
        print('Error processing Event {}'.format(json.dumps(event, indent=2)))
        raise e