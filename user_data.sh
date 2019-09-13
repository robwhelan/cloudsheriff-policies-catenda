#!/usr/bin/env bash



cd /home/ec2-user

aws s3 cp s3://git-to-amazon-s3-outputbucket-91zt4h9ettwo/robwhelan/cloudjanitorz-demo/master/cloudjanitorz-demo.zip repo.zip
unzip repo.zip

# hi
#rm -rf policies/ #delete this later when you fix the machine image.

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
