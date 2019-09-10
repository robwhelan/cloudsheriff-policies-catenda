#!/usr/bin/env bash

cd /home/ec2-user && ls

rm -rf policies/ #delete this later when you fix the machine image.

cd custodian && ls
cd bin && ls

source /home/ec2-user/custodian/bin/activate;
mkdir policies && cd policies;
aws s3 cp s3://cloudjanitorz/policies/ . --recursive;

function run_policy_file () {
  #echo $1
  local file=$1;
  local filename=${file%.*};
  custodian run $file \
    -s s3://cloudjanitorz/drop/ \
    --metrics aws \
    --log-group=/the-sheriff/cool ;
}

for file in *.yaml;
do
  run_policy_file $file;
done
