import json
from operator import truediv
from collections import defaultdict
import boto3

INPUT_PREFIX = "input/"
OUPUT_PREFIX = "output/"
BUCKET_NAME = "swe-bucket-bugsbunny"

def key_present(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

def validate_input_json(in_json):
    return key_present(in_json, "id") & key_present(in_json, "caption") & key_present(in_json, "caption") & key_present(in_json, "hashtags")

def add_text_from_rekognition_image(in_json, response):
    in_json.pop('image')
    in_json['texts'] = dict()
    for line in response['TextDetections']:
        if(line['Type']=='LINE'):
            in_json['texts'][f"{line['Id']}"] = line['DetectedText']

def unpack_json_for_comprehend(in_json):
    return list([in_json['caption'], *in_json['texts'].values(), *in_json['hashtags'].values()])

def add_results_from_comprehend(in_json, response):
    n_texts = len(in_json['texts'])
    for item in response['ResultList'] + response['ErrorList']:
        idx = item.pop('Index')
        if(idx==0): 
            in_json['caption'] = [in_json['caption'], item]
        elif(idx-1 < n_texts):
            in_json['texts']['{}'.format(idx-1)] = [in_json['texts']['{}'.format(idx-1)], item]
        else:
            in_json['hashtags']['{}'.format(idx-1-n_texts)] = [in_json['hashtags']['{}'.format(idx-1-n_texts)], item]

def lambda_handler(event, context):
    rekognition = boto3.client(service_name='rekognition', region_name='eu-central-1')
    comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
    s3 = boto3.resource('s3')

    try:
        print("Analyzing SQS Event")

        data_json = json.loads(event['Records'][0]['body'])
        assert(validate_input_json(data_json))
        print("Successfully read data")

        response = rekognition.detect_text(Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': data_json['image']}})
        add_text_from_rekognition_image(data_json, response)
        print('Successfully analized image')

        response = comprehend.batch_detect_sentiment(TextList=unpack_json_for_comprehend(data_json), LanguageCode='en')
        add_results_from_comprehend(data_json, response)
        print('Successfully analized textual information')

        outputObject = s3.Object(BUCKET_NAME, f"scoring/{data_json['id']}.json")
        outputObject.put(Body=json.dumps(data_json, indent=2))
        print('Successfully written output to S3 Bucket: ' + BUCKET_NAME)

        return 'Success'
    except Exception as e:
        print('Error processing Event {}'.format(json.dumps(event, indent=2)))
        raise e
