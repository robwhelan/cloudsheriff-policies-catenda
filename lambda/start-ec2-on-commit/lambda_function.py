import json
import boto3

def get_user_data(obj, dropzone, loggroup='/the-sheriff/'):
    user_data = '''#!/usr/bin/env bash
    cd /home/ec2-user
    source /home/ec2-user/custodian/bin/activate;
    aws s3 cp ''' + obj + ''' repo.zip
    unzip repo.zip
    cd policies;

    function run_policy_file () {
      local file=$1;
      local filename=${file%.*};
      local log_group="''' + loggroup + '''${filename}"
      custodian run $file \
        -s s3://''' + dropzone + ''' \
        --metrics aws \
        --log-group $log_group ;
    }

    for file in *.yaml;
    do
      run_policy_file $file;
    done
    '''
    return user_data

client = boto3.client('ec2')

def lambda_handler(event, context):
    # TODO implement
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        obj = 's3://' + bucket + '/' + key;
        print('obj:', obj)

        #get s3 dropzone bucket for logs
        dropzone = 'cloudjanitorz/drop/'
        #get loggroup prefix
        loggroup = '/sheriff/'

        user_data = get_user_data(obj, dropzone, loggroup)

        response = client.run_instances(
            ImageId='ami-059f40689b2b1e15f',
            InstanceType='t2.micro',
            KeyName='aws-ec2-key-pair',
            SecurityGroupIds=['sg-d6cc7ca0'],
            UserData=user_data,
            IamInstanceProfile={
                'Name': 'S3-Admin-Access'
            },
            TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'cloud-custodian-worker'
                    }
                ]
            }],
            MinCount=1,
            MaxCount=1
        )



    return {
        'statusCode': 200,
        'body': json.dumps("thanks")
    }
