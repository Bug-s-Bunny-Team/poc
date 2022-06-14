from abc import ABC, abstractmethod
from enum import Enum, unique
from typing import Dict
import json
import boto3

s3 = boto3.resource('s3')
REGION_NAME = 'eu-central-1'
BUCKET_NAME = 'swe-bucket-bugsbunny'

@unique
class Score(str, Enum):
    MIXED = "MIXED"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    POSITIVE = "POSITIVE"

def key_present(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

class ScoringPost:
    id: str
    caption: str
    image: str
    texts: Dict[int, str]
    hashtags: Dict[int, str]
    captionScore: Score
    textsScore: Dict[int, Score]
    hashtagsScore = Dict[int, Score]

    @classmethod
    def __validate_input_json(cls, in_json):
        return key_present(in_json, "id") & key_present(in_json, "caption") & key_present(in_json, "image") & key_present(in_json, "hashtags")

    @classmethod
    def fromString(cls, string):
        in_json = json.loads(string)
        assert(ScoringPost.__validate_input_json(in_json))
        return cls(
            id = in_json["id"],
            caption = in_json["caption"],
            image = in_json["image"],
            texts = dict(),
            hashtags = { idx: string for idx,string in enumerate(in_json["hashtags"]) },
            textsScore = dict(),
            hashtagsScore = dict()
        )

    def toString(self):
        return json.dumps(self.__dict__)

class EventAdapter(ABC):
    @abstractmethod
    def processEvent(self, event) -> ScoringPost:
        pass

class OutputStrategy(ABC):
    @abstractmethod
    def output(self, sPost: ScoringPost):
        pass

class ScoringService(ABC):
    __e: EventAdapter
    __o: OutputStrategy
    _rekognition = boto3.client(service_name='rekognition', region_name=REGION_NAME)
    _comprehend = boto3.client(service_name='comprehend', region_name=REGION_NAME)
    
    def __init__(self, e: EventAdapter, o: OutputStrategy):
        self.__e = e
        self.__o = o

    def score(self, event):
        sPost = self.__e.processEvent(event)
        self._runRekognition(sPost)
        self._runComprehend(sPost)
        self.__o.output(sPost)

    @abstractmethod
    def _runRekognition(self, sPost: ScoringPost):
        pass

    @abstractmethod
    def _runComprehend(self, sPost: ScoringPost):
        pass

class SQSEventAdapter(EventAdapter):
    def processEvent(self, event) -> ScoringPost:
        print("Processing SQS Event")
        post = ScoringPost.fromString(event['Records'][0]['body'])
        print("Successfully processed data")
        return post

class BasicScoringService(ScoringService):
    @classmethod
    def __add_text_from_rekognition_image(cls, sPost: ScoringPost, rekResult):
        for line in rekResult['TextDetections']:
            if(line['Type']=='LINE'):
                sPost.texts[line['Id']] = line['DetectedText']
    
    @classmethod
    def __unpack_post_for_comprehend(cls, sPost: ScoringPost):
        return list([sPost.caption, *sPost.texts.values(), *sPost.hashtags.values()])

    @classmethod
    def __add_results_from_comprehend(cls, sPost: ScoringPost, compResult):
        n_texts = len(sPost.texts)
        for item in compResult['ResultList'] + compResult['ErrorList']:
            if not key_present(item, "Sentiment"):
                raise Exception("Error " + item["ErrorCode"] + ": " + item["ErrorMessage"])
            else:
                idx = item['Index']
                score = Score(item["Sentiment"])
                if(idx==0): 
                    sPost.captionScore = score
                elif(idx-1 < n_texts):
                    sPost.textsScore[idx-1] = score
                else:
                    sPost.hashtagsScore[idx-1-n_texts] = score

    def _runRekognition(self, sPost: ScoringPost):
        print('Analyzing image')
        response = self._rekognition.detect_text(Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': sPost.image}})
        BasicScoringService.__add_text_from_rekognition_image(sPost, response)
        print('Successfully analized image')

    def _runComprehend(self, sPost: ScoringPost):
        print('Analizying textual information')
        response = self._comprehend.batch_detect_sentiment(TextList=BasicScoringService.__unpack_post_for_comprehend(sPost), LanguageCode='en')
        BasicScoringService.__add_results_from_comprehend(sPost, response)
        print('Successfully analized textual information')

class S3OutputStrategy:
    outputBucket = BUCKET_NAME

    def output(self, sPost: ScoringPost):
        print(f'Writing output to {self.outputBucket} S3 Bucket')
        outputObject = s3.Object(self.outputBucket, f'scoring/{sPost.id}.json')
        outputObject.put(Body=sPost.toString())
        print(f'Successfully written output to {self.outputBucket} S3 Bucket')
