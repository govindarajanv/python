-	Jenkins to perform build and deployment on all the nodes
-	once deployment is done, AMI snapshot should be taken
-	In Auto scaling group, if one node goes down, a new node should be spinned up with new or the latest AMI
-	Node provisioned should have valid name set dynamically

Approach
========

-	Jenkins to perform build and deployment on all the nodes
	-	Post build steps
		-	Use scp plugin to copy the artifacts to the targetted node
		-	Use ssh plugin to perform remote operations on the node
		-	Use Deploy plugin to perform the task of deployment
	-	Use python script to copy the artifacts and do remote orchestration
-	AMI Snapshot to be taken
	-	boto3 client.create_image() to be called from Jenkins job
	- 	you can use SQLite DB to store the AMI id and timestamp in Jenkins server
		or
		use AWS Dynamodb/S3
-	Update the launch configuration to use the AMI and Update the Auto Scaling group
	-	as-create-launch-config $NEW_CONFIG_NAME --image-id ami-67890 --instance-type t1.micro --group $YOUR_GROUP  -monitoring-disabled
	-	as-update-auto-scaling-group blog-cluster-group --launch-configuration blog-cluster-3
	-	Insert/Update the sqlite db or S3/Dynamodb the newly launched instance details	
-	point#4 is already taken care of
	
-	
