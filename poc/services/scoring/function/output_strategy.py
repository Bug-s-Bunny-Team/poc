from .models import ScoringPost
from abc import ABC, abstractmethod
from db import init_db
import boto3
import os

class OutputStrategy(ABC):
    @abstractmethod
    def output(self, sPost: ScoringPost):
        pass

class S3OutputStrategy:
    outputBucket = os.environ['ENV_BUCKET_NAME']
    s3 = boto3.resource('s3')

    def output(self, sPost: ScoringPost):
        print(f'Writing output to {self.outputBucket} S3 Bucket')
        outputObject = self.s3.Object(self.outputBucket, f'scoring/{sPost.id}.json')
        outputObject.put(Body=sPost.toString())
        print(f'Successfully written output to {self.outputBucket} S3 Bucket')

class DBOutputStrategy:

    def output(self, sPost: ScoringPost):
        print(f'Writing output to Database')
        init_db()

        print(f'Successfully written output to Database')
