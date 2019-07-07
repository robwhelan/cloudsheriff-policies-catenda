import json
import gzip
import boto3
import botocore
#download the file

s3 = boto3.resource('s3')

def handler(event, context):
    #KEY = 'resources.json.gz'
    print(event)

    response = []
    for record in event['Records']:
        try:
            BUCKET = record['s3']['bucket']['name']
            KEY = record['s3']['object']['key']
            policy_name = KEY.split('/')[0]
            s3.Bucket(BUCKET).download_file(KEY, '/tmp/resources.json.gz')
            with gzip.open('/tmp/resources.json.gz', 'rb') as f:
                file_content = f.read()
                obj = json.loads(file_content)
                response.append({
                    "policy_name": policy_name,
                    "data": obj
                })
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
                return "error, object does not exist"
            else:
                raise
    return response
