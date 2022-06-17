import json
from pathlib import Path

import boto3
from botocore.exceptions import ClientError


def create_error_response(message: str, code: int = 400):
    return {
        'statusCode': code,
        'body': json.dumps({'error': message}),
    }


def s3_key_exists(bucket_name: str, key: str) -> bool:
    try:
        s3 = boto3.client('s3')
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError:
        return False


def s3_upload_file(bucket_name: str, key: str, src: Path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file(str(src), key)
