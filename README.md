**These are the base policies for Cloud Sheriff.**

Work on these locally, and test them locally. When you commit and push them to the master branch, it tells a lambda to pull the files in to S3. When that is complete, another lambda will turn on an EC2 instance with the CloudCustodian AMI, and using UserData it will copy files and run all of them through Custodian. The EC2 instance provisions lambdas, config rules, etc based on the policies.

To set it all up, you need to have a repo handy from GitLab, GitHub, or BitBucket, then run the `cfn` template `git-copy-clouformation.yaml`.

***

Lambda cheatsheet.
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

aws lambda invoke --function-name cloudjanitorz-load-policy-data --payload file://payload.json lambda-results
