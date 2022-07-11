import boto3
from abc import ABC, abstractmethod
from db.utils import *
from db.models import *
from .models import ScoringPost


# SocialProfile.get_or_create(username="test")
# Location.get_or_create(insta_id=1, name="test_loc")
# Post.get_or_create(id=1, shortcode=1, caption="unfortunately today it is raining in Seattle #sad #city", social_profile=1, media_type=MediaType.IMAGE, media_url="test.png", location=1)

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
        postScore = PostScore.get_or_create(post=sPost.id)[0]
        postScore.caption_score = sPost.captionScore
        postScore.media_score = sum(sPost.textsScore.values())/len(sPost.textsScore)
        postScore.save()
        print(f'Successfully written output to Database')
