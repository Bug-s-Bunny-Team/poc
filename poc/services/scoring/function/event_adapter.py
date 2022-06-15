from .models import ScoringPost
from abc import ABC, abstractmethod

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
