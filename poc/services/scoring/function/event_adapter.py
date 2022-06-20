from abc import ABC, abstractmethod
from .models import ScoringPost

class EventAdapter(ABC):
    @abstractmethod
    def processEvent(self, event) -> ScoringPost:
        pass

class SQSEventAdapter(EventAdapter):
    def processEvent(self, event) -> ScoringPost:
        print("Processing SQS Event")
        post = ScoringPost.fromString(event['Records'][0]['body'])
        print("Successfully processed data")
        return post

class SNSEventAdapter(EventAdapter):
    def processEvent(self, event) -> ScoringPost:
        print("Processing SNS Event")
        post = ScoringPost.fromString(event['Records'][0]['Sns']['Message'])
        print("Successfully processed data, subject: " + event['Records'][0]['Sns']['Subject'])
        return post
