import boto3

# project_prefix="BOTO3_"

#Read the required inputs from a file
file_reader = open('/home/ec2-user/govind/.aws/credentials','r')
input_args = file_reader.readlines()
print (input_args)
file_reader.close()

aws_access_key_id = ""
aws_secret_access_key = ""
if (input_args[1].strip().split("=")[0].strip() == 'aws_access_key_id'):
        aws_access_key_id = input_args[1].strip().split("=")[1].strip()

if (input_args[2].strip().split("=")[0].strip()== 'aws_secret_access_key'):
        aws_secret_access_key = input_args[2].strip().split("=")[1].strip()

# read the credentials and region from the setting
ec2 = boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

#create VPC
vpc = ec2.create_vpc(CidrBlock='10.95.0.0/16')

#update tags on the VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": "vpc_from_boto3"}])
vpc.wait_until_available()
print("VPC with vpc id",vpc.id,"is created successfully")

#create an IGW and attach it to the VPC
ig = ec2.create_internet_gateway()
print("IGW with id",ig.id,"is created successfully")
vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print ("IGW",ig.id,"is attached to the VPC",vpc.id)

# create a route table and a public route
route_table = vpc.create_route_table()
route = route_table.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=ig.id)
print("route table with id",route_table.id,"is created successfully")

#create public subnet
subnet = ec2.create_subnet(CidrBlock='10.95.1.0/24', VpcId=vpc.id)

# associate the route table with the subnet so that it becomes public subnet
route_table.associate_with_subnet(SubnetId=subnet.id)
print("Subnet",subnet.id,"is associated with route table",route_table.id)

# Create secuirty group
sec_group = ec2.create_security_group(GroupName='boto3_sg', Description='boto3 sec group', VpcId=vpc.id)
sec_group.authorize_ingress( CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
print("security group with id",sec_group.id,"is created successfully")

# Create instance
instances = ec2.create_instances(ImageId='ami-55378c2a', InstanceType='t2.micro', MaxCount=1, MinCount=1, NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
instances[0].wait_until_running()
print("Instance with instance id",instances[0].id, "is created in subnet",subnet.id)
