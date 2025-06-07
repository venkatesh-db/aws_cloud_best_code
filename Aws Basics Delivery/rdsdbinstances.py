
import boto3

rds = boto3.client('rds')

def list_rds_instances():
    response = rds.describe_db_instances()
    for db in response['DBInstances']:
        print(f"DB Instance: {db['DBInstanceIdentifier']} - Status: {db['DBInstanceStatus']}")

list_rds_instances()
