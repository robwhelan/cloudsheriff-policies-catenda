#run this from root directory
function run_policy_file () {
  local file=$1;
  local filename=${file%.*};
  custodian run $file \
    -s s3://cloudjanitorz/drop/ \
    --metrics aws \
    --dryrun
}

cd custom-policies

for file in *.yaml;
do
  run_policy_file $file;
done
