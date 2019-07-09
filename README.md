TODO:
1. DONE S3 new object triggers a lambda
2. DONE The lambda can load the data and it knows the policy
3. (2/6) next, need to build tables for each policy (know what data you want to get... normalize everything?)
4. START THE EC2 INSTANCE AND THE RDS DATABASE  
5. write up the insert statements for each table.
6. write up SELECT * statements for different endpoints on the demo dashboard. -- do this for each policy. 6 policies.


File arch.
Policy filename should match the `name` field of the Policy, which should match the database table name.
Pick the database table columns from the default output of the `report` function.


RDS
mysql
cloudjanitorz (username and password)
db name: cloudjanitorz

RDS db
$ aws rds create-db-instance --db-name cloudjanitorz --engine MySQL \
--db-instance-identifier cloudjanitorz --backup-retention-period 3 \
--db-instance-class db.t2.micro --allocated-storage 5 --publicly-accessible \
--master-username cloudjanitorz --master-user-password cloudjanitorz

Connect to mysql:
mysql -h cloudjanitorz.c3cnrieiquqk.us-east-1.rds.amazonaws.com -P 3306 -u cloudjanitorz -p cloudjanitorz

Lambda.
$ aws lambda create-function --function-name cloudjanitorz-load-policy-data --runtime python3.6 \
--zip-file fileb://function.zip --handler app.handler \
--role arn:aws:iam::773548596459:role/lambda_basic_execution \
--timeout 15

$ aws lambda invoke --function-name cloudjanitorz-connectmysql lambda-results

$ aws lambda update-function-configuration \
--function-name cloudjanitorz-connectmysql \
--timeout 15

PACKAGING UP A PYTHON Lambda
cd package
zip -r9 ${OLDPWD}/function.zip .
cd $OLDPWD
zip -g function.zip app.py rds_config.py
aws lambda update-function-code --function-name cloudjanitorz-connectmysql --zip-file fileb://function.zip
aws lambda invoke --function-name cloudjanitorz-connectmysql lambda-results
atom lambda-results

TODO: add individual tables based on how the CSV comes out.

aws lambda invoke --function-name cloudjanitorz-load-policy-data --payload file://payload.json lambda-results


FUTURE IDEAS
1. user interface showing all policies in plain english. when a new one is added, a database table is created, and the minimum access for the role will be added.
