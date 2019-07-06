zip -g function.zip app.py rds_config.py
aws lambda update-function-code --function-name cloudjanitorz-connectmysql --zip-file fileb://function.zip
aws lambda invoke --function-name cloudjanitorz-connectmysql lambda-results
atom lambda-results
