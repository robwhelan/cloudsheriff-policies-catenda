#!/usr/bin/env bash

aws ec2 run-instances \
  --image-id ami-0b41a85dc0b29ab06 \
  --instance-type t2.micro \
  --key-name aws-ec2-key-pair \
  --user-data file://user_data.sh \
  --iam-instance-profile Name=S3-Admin-Access \
  --count 1
