import json
import boto3

INPUT_PREFIX = "input/"
OUPUT_PREFIX = "output/"

def lambda_handler(event, context):
    bucketName = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
    s3 = boto3.resource('s3')

    try:
        print("Analyzing: " + object_key + " from Bucket: " + bucketName)

        data = s3.Object(bucketName, object_key).get()['Body'].read().decode("utf-8")
        print("Successfully read data")

        response = comprehend.detect_sentiment(Text=data, LanguageCode='en')
        print("Successfully analized")

        outputObject = s3.Object(bucketName, object_key.replace(INPUT_PREFIX, OUPUT_PREFIX, 1))
        assert(object_key != outputObject.key)
        outputObject.put(Body=json.dumps(response, indent=2))
        print("Successfully written output to S3 Bucket: " + bucketName)

        return 'Success'
    except Exception as e:
        print("Error processing object {} from bucket {}. Event {}".format(object_key, bucketName, json.dumps(event, indent=2)))
        raise e
