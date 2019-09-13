#!/usr/bin/env bash

#variables:
#security group id.
#key name.
#iam instance profile.
#stuff to send into user data.
aws ec2 run-instances \
  --image-id ami-059f40689b2b1e15f \
  --instance-type t2.micro \
  --key-name aws-ec2-key-pair \
  --security-group-ids sg-d6cc7ca0 \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=cloud-custodian-worker}]' \
  --user-data file://user_data.sh \
  --iam-instance-profile Name=S3-Admin-Access \
  --count 1
