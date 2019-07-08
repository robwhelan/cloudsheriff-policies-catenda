import json
import gzip
import boto3
import botocore
import rds_config
import pymysql
from decimal import Decimal

rds_host  = rds_config.rds_instance_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

#download the file

#InstanceId = obj["InstanceId"]
#InstanceType =obj[0]["InstanceType"]
#LaunchTime = obj[0]["LaunchTime"]
#VpcId = obj[0]["VpcId"]
#PrivateIpAddress = obj[0]["PrivateIpAddress"]
#InstanceState = obj[0]["State"]["Name"]
#CPUUtilization = obj[0]["c7n.metrics"]["AWS/EC2.CPUUtilization.Average"][0]["Average"]



s3 = boto3.resource('s3')

def create_table():
    with conn.cursor() as cur:
        #cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        conn.commit()


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
                #insert
                with conn.cursor() as cur:
                    for r in obj:
                        #InstanceId = str(r["InstanceId"])
                        #cur.execute(f'insert into underutilized_ec2 (InstanceId, InstanceType, LaunchTime, VpcId, PrivateIpAddress, InstanceState, CpuUtilization) values({r["InstanceId"]}, {r["InstanceType"]}, {r["LaunchTime"]}, {r["VpcId"]}, {r["PrivateIpAddress"]}, {r["State"]["Name"]}, {round(Decimal(r["c7n.metrics"]["AWS/EC2.CPUUtilization.Average"][0]["Average"]),8)})')
                        #print(f'{r["InstanceId"]}, {r["InstanceType"]}, {r["LaunchTime"]}, {r["VpcId"]}, {r["PrivateIpAddress"]}, {r["State"]["Name"]}, {round(Decimal(r["c7n.metrics"]["AWS/EC2.CPUUtilization.Average"][0]["Average"]),8)})')
                        sql = 'insert into underutilized_ec2 (InstanceId, InstanceType, VpcId, InstanceState) VALUES (%s, %s, %s, %s)'
                        cur.execute(sql, (r["InstanceId"], r["InstanceType"], r["VpcId"], r["State"]["Name"]))
                    conn.commit()

                #then tell the websocket about the new data

        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
                return "error, object does not exist"
            else:
                raise
    return response
