import boto3
import os
from abc import ABC, abstractmethod
from db.utils import *
from db.models import *
from .models import ScoringPost

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
        create_all_tables()
        SocialProfile.create(username="test")
        Location.create(insta_id=1, name="test_loc")
        Post.create(shortcode=sPost.id, caption=sPost.caption, social_profile=1, media_type=MediaType.IMAGE, media_url="www.media.url", location=1)
        response = PostScore.create(media_score=sum(sPost.textsScore.values())/len(sPost.textsScore), 
                                    caption_score=sPost.captionScore,
                                    post=sPost.id)
        print(f'Successfully written output to Database')
