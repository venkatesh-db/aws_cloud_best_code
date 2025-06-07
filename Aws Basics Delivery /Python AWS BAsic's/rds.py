
import boto3

rds = boto3.client('rds')

response = rds.describe_db_instances()

for db in response['DBInstances']:
    print("🛢️ DB Identifier:", db['DBInstanceIdentifier'])
