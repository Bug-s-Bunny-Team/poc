import json
import os

import boto3
from peewee import DoesNotExist
from pydantic import ValidationError

from common.models import Request
from common.utils import create_error_response, extract_insta_shortcode, create_response
from db.models import Post
from db.utils import init_db

from .provider import PostProvider


def lambda_handler(event, context):
    try:
        request = Request(**event)
    except ValidationError as e:
        return create_error_response(str(e))

    init_db()

    provider = PostProvider()

    if request.httpMethod == 'GET':
        return provider.handle_request(request)

    if not request.body:
        return create_error_response('Body is required')

    if url := request.body.get('url'):
        try:
            # check if a post with this shortcode already exists and return it
            shortcode = extract_insta_shortcode(url)
            if not shortcode:
                return create_error_response('Specified URL is invalid')
            post = provider.query_all().where(Post.shortcode == shortcode).get()
            return create_response(provider.serialize(post), 200)
        except DoesNotExist:
            pass
    elif not request.body.get('username'):
        return create_error_response('URL or username not provided')

    # publish scrape request on scrape topic and return something with code 201
    sns = boto3.resource('sns')
    topic = sns.Topic(os.environ['SNS_SCRAPING_TOPIC'])
    topic.publish(Message=json.dumps(request.body))

    return create_error_response('Not implemented')
