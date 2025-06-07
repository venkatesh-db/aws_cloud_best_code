
import boto3
logs = boto3.client('logs')

def list_log_groups():
    response = logs.describe_log_groups()
    for group in response['logGroups']:
        print(f"Log Group: {group['logGroupName']}")
    print("cloud log's")

list_log_groups()
