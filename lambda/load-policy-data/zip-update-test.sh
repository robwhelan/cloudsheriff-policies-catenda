zip -g function.zip app.py rds_config.py
aws lambda update-function-code --function-name cloudjanitorz-load-policy-data --zip-file fileb://function.zip
aws lambda invoke --function-name cloudjanitorz-load-policy-data --payload file://payload.json lambda-results
atom lambda-results
