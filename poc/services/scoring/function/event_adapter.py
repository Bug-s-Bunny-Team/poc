from abc import ABC, abstractmethod
from db.utils import *
from db.models import *
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
        post = Post.get(id=event['Records'][0]['Sns']['MessageAttributes']['id'])
        sPost = ScoringPost.fromPost(post)
        print("Successfully processed data from SNS subject: " + event['Records'][0]['Sns']['Subject'])
        return sPost
