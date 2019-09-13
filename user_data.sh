#!/usr/bin/env bash

cd /home/ec2-user
source /home/ec2-user/custodian/bin/activate;
aws s3 cp s3://git-to-amazon-s3-outputbucket-91zt4h9ettwo/robwhelan/cloudjanitorz-demo/master/cloudjanitorz-demo.zip repo.zip
unzip repo.zip
cd policies;

function run_policy_file () {
  local file=$1;
  local filename=${file%.*};
  local log_group="/the-sheriff/${filename}"
  custodian run $file \
    -s s3://cloudjanitorz/drop/ \
    --metrics aws \
    --log-group $log_group ;
}

for file in *.yaml;
do
  run_policy_file $file;
done
