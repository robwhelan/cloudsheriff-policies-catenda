#!/usr/bin/env bash
#cd /home/ec2-user

source ~/custodian/bin/activate;
#cd policies;
export AWS_PROFILE=default

function run_policy_file () {
  local file=$1;
  local filename=${file%.*};
  custodian run $file \
   -s s3://robs-security-account-drop-472651685700 \
   --metrics aws
   #--log-group '/sheriff/'
}

for file in *.yaml;
do
 run_policy_file $file;
done
