import sys
import boto3
db = sys.argv[1]
rds = boto3.client('rds')
try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db,
        SkipFinalSnapshot=True)
    print (response)
except Exception as error:
    print (error)
