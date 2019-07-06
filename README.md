tips

To get a CSV report, first run the policy:
```
$ custodian run -s s3://bigdatalabsrww/custodian-report/ custodian-2.yml
```

Then, get the csv output with special fields:
```
$ custodian report -s s3://bigdatalabsrww/custodian-report/ custodian-2.yml >> output.csv
```

In order to get this CSV file which can be used for "big data for security" then you need to write all policies as resource-specific.

```
custodian report -s s3://bigdatalabsrww/custodian-report/ custodian-2.yml >> output.csv
2019-07-05 19:40:04,980: custodian.commands:ERROR Error: Report subcommand can accept multiple policies, but they must all be for the same resource.
```

RDS
Postgres
cloudjanitorz (username and password)
db name: cloudjanitorpolicies

RDS db
$ aws rds create-db-instance --db-name cloudjanitorz --engine MySQL \
--db-instance-identifier cloudjanitorz --backup-retention-period 3 \
--db-instance-class db.t2.micro --allocated-storage 5 --publicly-accessible \
--master-username cloudjanitorz --master-user-password cloudjanitorz

Lambda.
$ aws lambda create-function --function-name cloudjanitorz-connectmysql --runtime python3.6 \
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
