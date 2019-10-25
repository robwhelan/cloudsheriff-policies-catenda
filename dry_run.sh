#run this from root directory
source ../../custodian/bin/activate

function run_policy_file () {
  local file=$1;
  local filename=${file%.*};
  custodian run $file \
    -s . \
    --dryrun
}

cd custom-policies

for file in *.yaml;
do
  run_policy_file $file;
done
