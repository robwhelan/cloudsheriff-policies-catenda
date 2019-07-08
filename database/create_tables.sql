CREATE TABLE underutilized_ec2 (
  InstanceId varchar(56),
  InstanceType varchar(56),
  LaunchTime timestamp,
  VpcId varchar(20),
  PrivateIpAddress varchar(20),
  InstanceState varchar(20),
  CpuUtilization DECIMAL(10,8)
);

insert into underutilized_ec2 (LaunchTime) values("2019-07-06T22:38:27+00:00")
