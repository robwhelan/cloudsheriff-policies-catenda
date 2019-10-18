**These are the base policies for Cloud Sheriff.**


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




BETTER arch
* logs of rules / config etc should be sent to s3 drop zone
* glue job move data to analytics zone.-- daily, job bookmark enabled.
