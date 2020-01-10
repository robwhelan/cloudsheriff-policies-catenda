**These are the base policies for Cloud Sheriff.**

*Install Cloud Custodian*
MacOSX
https://cloudcustodian.io/docs/quickstart/

Work on these locally, and test them locally. When you commit and push them to the master branch, it tells a lambda to pull the files in to S3. When that is complete, another lambda will turn on an EC2 instance with the CloudCustodian AMI, and using UserData it will copy files and run all of them through Custodian. The EC2 instance provisions lambdas, config rules, etc based on the policies.
