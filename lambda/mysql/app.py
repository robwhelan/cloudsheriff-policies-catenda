import sys
import logging
import rds_config
import pymysql
import json
#rds settings
rds_host  = rds_config.rds_instance_endpoint
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def create_tables():
    with conn.cursor() as cur:
        cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        conn.commit()
    return

def handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    returned_items = ''

    with conn.cursor() as cur:
        #cur.execute("create table Employee ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        #cur.execute('insert into Employee (EmpID, Name) values(1, "Joe")')
        cur.execute('select * from Employee')
        returned_items = cur.fetchall()
        for row in returned_items:
            print(row[0], row[1])
        #for row in cur:
        #    logger.info("row: ", row)
    conn.commit()

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'first': returned_items[0][1],
            'second': returned_items[1][1]
        }),
        'isBase64Encoded': False
    }
    return response
