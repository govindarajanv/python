import boto3
ec2 = boto3.resource('ec2')
#While the command will finish quickly, it will take some time for the instance to be created
instance = ec2.create_instances(
    ImageId='ami-1e299d7e',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro')
print (instance[0].id)
