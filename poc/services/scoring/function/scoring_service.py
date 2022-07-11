import boto3
import os
from abc import ABC, abstractmethod
from .models import ScoringPost, Score
from .event_adapter import EventAdapter
from .output_strategy import OutputStrategy

class ScoringService(ABC):
    __e: EventAdapter
    __o: OutputStrategy
    _rekognition = boto3.client(service_name='rekognition', region_name=os.environ['ENV_REGION_NAME'])
    _comprehend = boto3.client(service_name='comprehend', region_name=os.environ['ENV_REGION_NAME'])
    
    def __init__(self, e: EventAdapter, o: OutputStrategy):
        self.__e = e
        self.__o = o

    def score(self, event):
        sPost = self.__e.processEvent(event)
        self._runRekognition(sPost)
        self._runComprehend(sPost)
        self._calcFinalScore(sPost)
        self.__o.output(sPost)

    @abstractmethod
    def _runRekognition(self, sPost: ScoringPost):
        pass

    @abstractmethod
    def _runComprehend(self, sPost: ScoringPost):
        pass

    @abstractmethod
    def _calcFinalScore(self, sPost: ScoringPost):
        pass



class BasicScoringService(ScoringService):
    @classmethod
    def __parse_rekognition_response(cls, sPost: ScoringPost, rekResult):
        for line in rekResult['TextDetections']:
            if(line['Type']=='LINE'):
                sPost.texts[line['Id']] = line['DetectedText']
    
    @classmethod
    def __unpack_post_for_comprehend(cls, sPost: ScoringPost):
        return list([sPost.caption, *sPost.texts.values(), *sPost.hashtags.values()])

    @classmethod
    def __parse_comprehend_response(cls, sPost: ScoringPost, compResult):
        n_texts = len(sPost.texts)
        if(len(compResult['ErrorList'])>0):
            raise Exception(compResult['ErrorList'])
        for item in compResult['ResultList']:
            idx = item['Index']
            score = Score(item["Sentiment"])
            float_score = item["SentimentScore"]["Positive"]-item["SentimentScore"]["Negative"] if(score == Score.POSITIVE or score==Score.NEGATIVE) else 0.0
            if(idx==0): 
                sPost.captionScore = float_score
            elif(idx-1 < n_texts):
                sPost.textsScore[idx-1] = float_score
            else:
                sPost.hashtagsScore[idx-1-n_texts] = float_score

    def _runRekognition(self, sPost: ScoringPost):
        print('Analyzing image')
        response = self._rekognition.detect_text(Image={'S3Object': {'Bucket': os.environ['ENV_BUCKET_NAME'], 'Name': sPost.image}})
        BasicScoringService.__parse_rekognition_response(sPost, response)
        print('Successfully analized image')

    def _runComprehend(self, sPost: ScoringPost):
        print('Analizying textual information')
        response = self._comprehend.batch_detect_sentiment(TextList=BasicScoringService.__unpack_post_for_comprehend(sPost), LanguageCode='en')
        BasicScoringService.__parse_comprehend_response(sPost, response)
        print('Successfully analized textual information')

    def _calcFinalScore(self, sPost: ScoringPost):
        sPost.finalScore = (sPost.captionScore + sum(sPost.textsScore.values())/len(sPost.textsScore))/2.0 if len(sPost.textsScore) != 0 else 0.0
