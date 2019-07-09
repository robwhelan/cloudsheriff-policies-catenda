create database cloudjanitorz;
  use cloudjanitorz;

CREATE TABLE underutilized_ec2 (
  InstanceId varchar(56),
  InstanceType varchar(56),
  LaunchTime timestamp,
  VpcId varchar(20),
  PrivateIpAddress varchar(20),
  InstanceState varchar(20),
  CpuUtilization DECIMAL(10,8)
);

CREATE TABLE release_unallocated_eips (
  AllocationId varchar(56),
  PublicIp varchar(56)
);

CREATE TABLE forgotten_sagemaker_notebook (
  NotebookInstanceArn varchar(112), /* need longer space for long arns */
  NotebookInstanceName varchar(56),
  CreationTime timestamp
);
