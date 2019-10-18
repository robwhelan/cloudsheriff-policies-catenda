custodian run -s s3://cloudjanitorz underutilized_ec2.yaml
custodian run -s s3://cloudjanitorz release_unallocated_eips.yaml
custodian run -s s3://cloudjanitorz forgotten_sagemaker_notebook.yaml
