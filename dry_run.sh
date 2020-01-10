#run this from root directory
ls custodian/bin/activate

function run_policy_file () {
  source ../custodian/bin/activate

  local file=$1;
  local filename=${file%.*};
  custodian run $file \
    -s out \
    --dryrun
}

cd custom-policies

for file in *.yaml;
do
  run_policy_file $file;
done
