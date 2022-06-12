import json
from operator import truediv
import boto3

INPUT_PREFIX = "input/"
OUPUT_PREFIX = "output/"

def key_present(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

def lambda_handler(event, context):
    bucketName = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')
    s3 = boto3.resource('s3')

    try:
        print("Analyzing: " + object_key + " from Bucket: " + bucketName)

        assert(object_key.endswith(".json"))
        data_json = json.loads(s3.Object(bucketName, object_key).get()['Body'].read())
        assert(key_present(data_json, "id") & key_present(data_json, "caption") & key_present(data_json, "labels") & key_present(data_json, "hashtags")) 
        print("Successfully read data")

        textList = list([data_json["caption"], *data_json["labels"].values(), *data_json["hashtags"].values()])
        response = comprehend.batch_detect_sentiment(TextList=textList, LanguageCode='en')
        print("Successfully analized")

        n_labels = len(data_json["labels"])
        for item in response["ResultList"]:
            idx = item.pop("Index")
            if(idx==0): 
                data_json["caption"] = item
            elif(idx-1 < n_labels):
                data_json["labels"]['{}'.format(idx-1)] = item
            else:
                data_json["hashtags"]['{}'.format(idx-1-n_labels)] = item

        for item in response["ErrorList"]:
            idx = item.pop("Index")
            if(idx==0): 
                data_json["caption"] = item
            elif(idx-1 < n_labels):
                data_json["labels"]['{}'.format(idx-1)] = item
            else:
                data_json["hashtags"]['{}'.format(idx-1-n_labels)] = item

        outputObject = s3.Object(bucketName, object_key.replace(INPUT_PREFIX, OUPUT_PREFIX, 1))
        assert(object_key != outputObject.key)
        outputObject.put(Body=json.dumps(data_json, indent=2))
        print("Successfully written output to S3 Bucket: " + bucketName)

        return 'Success'
    except Exception as e:
        print("Error processing object {} from bucket {}. Event {}".format(object_key, bucketName, json.dumps(event, indent=2)))
        raise e
